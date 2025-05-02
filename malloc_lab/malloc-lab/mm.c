/*
 * mm-naive.c - The fastest, least memory-efficient malloc package.
 *
 * In this naive approach, a block is allocated by simply incrementing
 * the brk pointer.  A block is pure payload. There are no headers or
 * footers.  Blocks are never coalesced or reused. Realloc is
 * implemented directly using mm_malloc and mm_free.
 *
 * NOTE TO STUDENTS: Replace this header comment with your own header
 * comment that gives a high level description of your solution.
 */
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <unistd.h>
#include <string.h>

#include "mm.h"
#include "memlib.h"

/*********************************************************
 * NOTE TO STUDENTS: Before you do anything else, please
 * provide your team information in the following struct.
 ********************************************************/
team_t team = {
    /* Team name */
    "ateam",
    /* First member's full name */
    "Harry Bovik",
    /* First member's email address */
    "bovik@cs.cmu.edu",
    /* Second member's full name (leave blank if none) */
    "",
    /* Second member's email address (leave blank if none) */
    ""};

/* single word (4) or double word (8) alignment */
#define ALIGNMENT 16
#define WSIZE 4 /* header/footer size */
#define PTR_SIZE sizeof(void *) /* pointer size */
#define MIN_FREE_BLOCK_SIZE (WSIZE + PTR_SIZE + PTR_SIZE + WSIZE)
#define CHUNKSIZE (1 << 12) /* Extend heap by this amount (bytes) */

#define MAX(x, y) ((x) > (y) ? (x) : (y))

/* Pack a size and allocated bit into a word */
#define PACK(size, alloc) ((size) | (alloc))

/* Read and write a word at address p */
#define GET(p) (*(unsigned int *)(p))
#define PUT(p, val) (*(unsigned int *)(p) = (val))

/* Read the size and allocated fields from address p */
#define GET_SIZE(p) (GET(p) & ~0x7)
#define GET_ALLOC(p) (GET(p) & 0x1)

/* Given block ptr bp, compute address of its header and footer */
#define HDRP(bp) ((char *)(bp) - WSIZE)
#define FTRP(bp) ((char *)(bp) + GET_SIZE(HDRP(bp)) - (WSIZE*2))

/* Given block ptr bp, compute address of next and previous blocks */
#define NEXT_BLKP(bp) ((char *)(bp) + GET_SIZE(((char *)(bp)-WSIZE)))
#define PREV_BLKP(bp) ((char *)(bp) - GET_SIZE(((char *)(bp)-(WSIZE*2))))

#define NEXT_FREE(bp) (*(void **)(bp)) // bp를 형변환 한거야 이중연결리스트로 그래서 bp가 가르키는 메모리공간에 다른블록을 가르키는 포인터가 생겨버리는거지 그걸 역참조해서 NEXT_FREE(bp)는 bp안에 다른블록을 가르키는 포인터의 값을 나타 내는 아이가 된거야.
#define PREV_FREE(bp) (*(void **)((char *)(bp) + PTR_SIZE)) // 그럼이것도 NEXT_FREE와 비슷하지만 한가지 다른게 bp의 시작주소 payload가 가르키는 메모리공간이 아니라 payload에다 4를 더한 주소에 prev_free를 저장하거나 읽는거야

#define SET_NEXT_FREE(bp, ptr) (NEXT_FREE(bp) = (ptr)) // 그럼 이건 위에는 포인터주소에 역참조한 상황이니까 거기에다가 ptr이라는 주소값을 넣은거지 즉 next인 주소를 넣은거지
#define SET_PREV_FREE(bp, ptr) (PREV_FREE(bp) = (ptr)) // 현재 가르키는 블록의 payload+wsize 위치에 이전 free블록의 주소를 저장하는거지

// #define NEXT_FRPTR(bp) (bp)
#define PREV_FRPTR(bp) ((char *)(bp) + GET_SIZE(((char *)(bp)+(WSIZE*2))))

/* rounds up to the nearest multiple of ALIGNMENT */
#define ALIGN(size) (((size) + (ALIGNMENT - 1)) & ~0xf)

#define SIZE_T_SIZE (ALIGN(sizeof(size_t)))

static void *free_root = NULL; /* Pointer to the first free block */
static char *heap_listp;

// Helper functions for free list manipulation
static void add_to_free_list(void *bp);
static void remove_from_free_list(void *bp);

int mm_init(void);
static void *extend_heap(size_t words);
static void *find_fit(size_t asize);
static void place(void *bp, size_t asize);
static void *coalesce(void *bp);


/*
 * mm_init - initialize the malloc package.
 */
int mm_init(void)
{
    /* Create the initial empty heap */
    if ((heap_listp = mem_sbrk(4*WSIZE)) == (void *)-1)
        return -1;
    PUT(heap_listp, 0);
    PUT(heap_listp + (1*WSIZE), PACK((WSIZE*2), 1));
    PUT(heap_listp + (2*WSIZE), PACK((WSIZE*2), 1));
    PUT(heap_listp + (3*WSIZE), PACK(0, 1));
    heap_listp += (2*WSIZE);
    free_root = NULL;
    // next_ptr = heap_listp; /* Reset next_ptr to NULL */

    /* Extend the empty heap with a free block of CHUNKSIZE bytes */
    if (extend_heap(CHUNKSIZE/WSIZE) == NULL)
        return -1;
    return 0;
}

static void *extend_heap(size_t words)
{
    char *bp;
    size_t size;

    /* Allocate an even number of words to maintain alignment */
    // size 계산은 바이트 단위로, ALIGNMENT(16)의 배수로 맞춤
    size = (words * WSIZE); // words는 WSIZE 단위이므로 총 바이트 계산
    size = ALIGN(size);     // 최종 크기를 16의 배수로 올림 (이게 더 안전)
    // size = (words % 2) ? (words + 1) * WSIZE : words * WSIZE; // 원래 로직도 가능은 함

    if ((long)(bp = mem_sbrk(size)) == -1)
        return NULL;

    /* Initialize free block header/footer and the epilogue header */
    PUT(HDRP(bp), PACK(size, 0));           /* Free block header */
    PUT(FTRP(bp), PACK(size, 0));           /* Free block footer */
    PUT(HDRP(NEXT_BLKP(bp)), PACK(0, 1)); /* New epilogue header */

    /* Coalesce if the previous block was free and add block to free list */
    // free_root 설정 및 포인터 초기화는 coalesce에서 처리
    return coalesce(bp);
}

/*
 * mm_malloc - Allocate a block by incrementing the brk pointer.
 *     Always allocate a block whose size is a multiple of the alignment.
 */
void *mm_malloc(size_t size)
{
    size_t asize;
    size_t extendsize;
    char * bp;

    /* Ignore spurious requests */
    if (size == 0)
        return NULL;

    size_t needed = size + (WSIZE * 2);
    
    /* Adjust block size to include overhead and alignment reqs. */
    if (needed <= MIN_FREE_BLOCK_SIZE)
        asize = MIN_FREE_BLOCK_SIZE;
    else
        asize = ALIGN(needed);

    /* Search the free list for a fit */
    if ((bp = find_fit(asize)) != NULL)
    {
        place(bp, asize);
        return bp;
    }

    /* No fit found. Get more memory and place the block */
    extendsize = MAX(asize, CHUNKSIZE);
    if ((bp = extend_heap(extendsize/WSIZE)) == NULL)
        return NULL;
    place(bp, asize);
    return bp;
}



static void *find_fit(size_t asize)
{
    /* First-fit search */
    void *bp;

    // free_root (리스트 헤드) 부터 시작해서 NULL 만날 때까지 순회
    for (bp = free_root; bp != NULL; bp = NEXT_FREE(bp))
    {
        // GET_ALLOC은 필요 없을 수 있음 (free list에는 free 블록만 있어야 함)
        // 하지만 안전을 위해 남겨둘 수 있음
        // if (!GET_ALLOC(HDRP(bp)) && (asize <= GET_SIZE(HDRP(bp))))
        if (asize <= GET_SIZE(HDRP(bp))) // 크기만 비교
        {
            return bp; // 적합한 블록 찾음
        }
    }
    return NULL; /* No fit */
}

// place 함수 수정
static void place(void *bp, size_t asize)
{
    size_t csize = GET_SIZE(HDRP(bp));
    // void *cur_free_next = NEXT_FREE(bp); // Helper 사용 시 필요 없어짐
    // void *cur_free_prev = PREV_FREE(bp); // Helper 사용 시 필요 없어짐

    // 먼저 free list에서 현재 블록(bp)을 제거
    remove_from_free_list(bp);

    if ((csize - asize) >= (MIN_FREE_BLOCK_SIZE)) // 분할 가능한 경우
    {
        // 할당될 부분 설정
        PUT(HDRP(bp), PACK(asize, 1));
        PUT(FTRP(bp), PACK(asize, 1));

        // 남은 free 부분 설정
        void *next_bp = NEXT_BLKP(bp); // 남은 블록 포인터
        PUT(HDRP(next_bp), PACK(csize - asize, 0));
        PUT(FTRP(next_bp), PACK(csize - asize, 0));

        // 남은 free 블록을 free list에 다시 추가
        add_to_free_list(next_bp);
    }
    else // 분할 불가능한 경우 (전체 블록 사용)
    {
        PUT(HDRP(bp), PACK(csize, 1));
        PUT(FTRP(bp), PACK(csize, 1));
        // free list에서 이미 제거했으므로 추가 작업 필요 없음
    }
}

/*
 * mm_free - Freeing a block does nothing.
 */
void mm_free(void *ptr)
{
    size_t size = GET_SIZE(HDRP(ptr));

    PUT(HDRP(ptr), PACK(size, 0)); /* 헤더에 동일한 사이즈와 할당되지 않은 정보로 update */
    PUT(FTRP(ptr), PACK(size, 0)); /* 푸터에 동일한 사이즈와 할당되지 않은 정보로 update */
    coalesce(ptr); /* free 끼리 병합 */
}

// coalesce 함수 수정 (Helper 함수 사용)
static void *coalesce(void *bp)
{
    // 프롤로그 블록 바로 뒤 또는 에필로그 블록 바로 앞인지 확인하여 FTRP/HDRP 접근 보호
    void *prev_blk = PREV_BLKP(bp);
    void *next_blk = NEXT_BLKP(bp);

    // GET_ALLOC은 헤더/푸터에서 읽으므로 주소 유효성 먼저 체크
    // Prologue block's footer is always allocated.
    // Epilogue block's header is always allocated.
    size_t prev_alloc = GET_ALLOC(FTRP(prev_blk)); // Can read footer unless bp is first block
    size_t next_alloc = GET_ALLOC(HDRP(next_blk)); // Can read header unless bp is last block
    size_t size = GET_SIZE(HDRP(bp));

    // Case 1: No merge needed
    if (prev_alloc && next_alloc) {
        add_to_free_list(bp); // Add the newly freed block to the list
        return bp;
    }

    // Case 2: Merge with next block
    else if (prev_alloc && !next_alloc) {
        remove_from_free_list(next_blk); // Remove next block from list
        size += GET_SIZE(HDRP(next_blk));
        PUT(HDRP(bp), PACK(size, 0));
        PUT(FTRP(bp), PACK(size, 0)); // Footer position is now FTRP(next_blk), but FTRP uses HDRP size, so this works
        add_to_free_list(bp); // Add the merged block to the list
        return bp;
    }

    // Case 3: Merge with previous block
    else if (!prev_alloc && next_alloc) {
        remove_from_free_list(prev_blk); // Remove previous block from list
        size += GET_SIZE(HDRP(prev_blk));
        bp = prev_blk; // Move bp to the beginning of the merged block
        PUT(HDRP(bp), PACK(size, 0));
        PUT(FTRP(bp), PACK(size, 0)); // Footer position is original FTRP(bp)
        add_to_free_list(bp); // Add the merged block to the list
        return bp;
    }

    // Case 4: Merge with both previous and next blocks
    else { // (!prev_alloc && !next_alloc)
        remove_from_free_list(prev_blk); // Remove previous block
        remove_from_free_list(next_blk); // Remove next block
        size += GET_SIZE(HDRP(prev_blk)) + GET_SIZE(HDRP(next_blk)); // Use HDRP for next block size
        bp = prev_blk; // Move bp to the beginning of the merged block
        PUT(HDRP(bp), PACK(size, 0));
        PUT(FTRP(bp), PACK(size, 0)); // Footer position is FTRP(next_blk)
        add_to_free_list(bp); // Add the final merged block to the list
        return bp;
    }
    // 마지막 free_root = bp; 제거
}

/*
 * mm_realloc - Implemented simply in terms of mm_malloc and mm_free
 */
void *mm_realloc(void *ptr, size_t size)
{
    void *oldptr = ptr;
    void *newptr;
    size_t copySize;

    newptr = mm_malloc(size);
    if (newptr == NULL)
        return NULL;
    copySize = GET_SIZE(HDRP(oldptr)) - (WSIZE*2);
    if (size < copySize)
        copySize = size;
    memcpy(newptr, oldptr, copySize);
    mm_free(oldptr);
    return newptr;
}

// --- Helper 함수 (place, coalesce 에서 사용) ---
// Free list 맨 앞에 블록 추가 (LIFO)
static void add_to_free_list(void *bp) {
    if (free_root == NULL) { // 리스트가 비어있을 때
        SET_NEXT_FREE(bp, NULL);
        SET_PREV_FREE(bp, NULL);
        free_root = bp;
    } else { // 리스트에 블록이 있을 때
        SET_NEXT_FREE(bp, free_root);
        SET_PREV_FREE(bp, NULL);
        SET_PREV_FREE(free_root, bp); // 기존 루트의 PREV를 새 블록으로
        free_root = bp; // 루트를 새 블록으로 업데이트
    }
}

// Free list에서 블록 제거
static void remove_from_free_list(void *bp) {
    void *prev_free = PREV_FREE(bp);
    void *next_free = NEXT_FREE(bp);

    if (prev_free == NULL) { // bp가 리스트의 첫 번째 블록일 때
        free_root = next_free; // 다음 블록을 루트로 설정
    } else { // bp가 중간 또는 마지막 블록일 때
        SET_NEXT_FREE(prev_free, next_free); // 이전 블록의 NEXT를 다음 블록으로
    }

    if (next_free != NULL) { // bp가 마지막 블록이 아닐 때
        SET_PREV_FREE(next_free, prev_free); // 다음 블록의 PREV를 이전 블록으로
    }
    // bp의 포인터는 초기화할 필요 없음 (어차피 할당되거나 병합될 것임)
}