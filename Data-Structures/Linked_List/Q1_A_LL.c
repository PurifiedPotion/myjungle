//////////////////////////////////////////////////////////////////////////////////

/* CE1007/CZ1007 Data Structures
Lab Test: Section A - Linked List Questions
Purpose: Implementing the required functions for Question 1 */

//////////////////////////////////////////////////////////////////////////////////

#include <stdio.h>
#include <stdlib.h>

//////////////////////////////////////////////////////////////////////////////////

// 노드 정의하는 구조체
typedef struct _listnode{
	int item;					// 이 노드가 저장할 데이터
	struct _listnode *next;		// 다음 노드를 가리키는 포인터로써, 연결 리스트에서 다음 노드로 이동할 수 있게 해줌
} ListNode;						// You should not change the definition of ListNode
// 위 노드 정의 구조체 덕분에, struct _listnode 대신 ListNode라는 이름 사용 가능

// 리스트 전체를 관리하는 구조체
typedef struct _linkedlist{
	int size;					// 노드 개수 저장
	ListNode *head;				// 머리 노드를 가리키는 포인터
} LinkedList;					// You should not change the definition of LinkedList
// 위 리스트 전체 관리 구조체 덕분에, struct _linkedlist 대신 LinkedList라는 이름 사용 가능

///////////////////////// function prototypes ////////////////////////////////////

//You should not change the prototype of this function
int insertSortedLL(LinkedList *ll, int item);

void printList(LinkedList *ll);
void removeAllItems(LinkedList *ll);
ListNode *findNode(LinkedList *ll, int index);
int insertNode(LinkedList *ll, int index, int value);
int removeNode(LinkedList *ll, int index);


//////////////////////////// main() //////////////////////////////////////////////

int main()
{
	LinkedList ll;		// LinkedList라는 타입의 변수 ll 선언, ll은 LinkedList 구조체 변수중 하나
	int c, i, j;
	c = 1;

	//Initialize the linked list 1 as an empty linked list
	ll.head = NULL;		// ll변수의 머리노드를 NULL로 저장
	ll.size = 0;		// ll변수의 크기를 0으로 저장

	printf("1: Insert an integer to the sorted linked list:\n");
	printf("2: Print the index of the most recent input value:\n");
	printf("3: Print sorted linked list:\n");
	printf("0: Quit:");

	while (c != 0)
	{
		printf("\nPlease input your choice(1/2/3/0): ");
		scanf("%d", &c);

		switch (c)
		{
		case 1:
			printf("Input an integer that you want to add to the linked list: ");
			scanf("%d", &i);
			j = insertSortedLL(&ll, i); // 새로운 int 값 리스트에 추가
			printf("The resulting linked list is: ");
			printList(&ll);
			break;
		case 2:
			printf("The value %d was added at index %d\n", i, j);
			break;
		case 3:
			printf("The resulting sorted linked list is: ");
			printList(&ll);
			removeAllItems(&ll);
			break;
		case 0:
			removeAllItems(&ll);
			break;
		default:
			printf("Choice unknown;\n");
			break;
		}


	}
	return 0;
}

//////////////////////////////////////////////////////////////////////////////////

int insertSortedLL(LinkedList *ll, int item)
{
	ListNode *cur;

	if (ll == NULL)
		return -1;

	if (ll->head == NULL){
		insertNode(ll, 0, item);
		return 0;
	}

	else 
	{
		cur = ll->head;
		int count = 0;
		while (cur != NULL && cur->item < item)
		{
			cur = cur->next;
			count++;
		}
		insertNode(ll,count,item);
		return 0;
		/*
		pre->next = malloc(sizeof(ListNode));
		pre->next->item = item;
		pre->next->next = cur;
		ll->size++;
		return 0;
		*/
	}
}

///////////////////////////////////////////////////////////////////////////////////

void printList(LinkedList *ll){

	ListNode *cur;						// ListNode라는 cur 포인터 선언
	if (ll == NULL)						// ll 포인터가 NULL 이면 return
		return;
	cur = ll->head;						// cur 포인터에 머리 노드 저장

	if (cur == NULL)					// cur(머리노드)가 NULL이면
		printf("Empty");				// 비어있다고 printf
	while (cur != NULL)					// cur(처음에 머리노드)가 NULL이 아니면
	{
		printf("%d ", cur->item);		// cur포인터의 item을 printf
		cur = cur->next;				// cur포인터를 next 포인터로 이동
	}
	printf("\n");
}


void removeAllItems(LinkedList *ll)
{
	ListNode *cur = ll->head;			// ListNode라는 cur 포인터 선언 + 머리노드로 이동
	ListNode *tmp;						// ListNode라는 tmp 포인터 선언

	while (cur != NULL){				// cur 포인터가 NULL이 아니면
		tmp = cur->next;				// tmp 포인터를 cur의 next 포인터로 옮긴다
		free(cur);						// cur 포인터 메모리 수동해제
		cur = tmp;						// cur 포인터를 tmp 포인터(cur의 next)로 저장한다
	}									// 이거를 tmp와 cur가 NULL일때까지 반복
	ll->head = NULL;					// ll 머리노드를 NULL 로 저장
	ll->size = 0;						// ll 크기를 0으로 저장
}


ListNode *findNode(LinkedList *ll, int index){

	ListNode *temp;										// temp를 포인터 선언

	if (ll == NULL || index < 0 || index >= ll->size)	// ll이라는 포인터가 NULL을 가리키는 경우 이거나 index가 음수이거나 index가 리스트의 크기 이상인 경우
		return NULL;

	temp = ll->head;									// 포인터를 머리 노드로 저장

	if (temp == NULL || index < 0)						// 포인터가 NULL 이거나 index가 음수이면
		return NULL;

	while (index > 0){									// index가 양수일 때
		temp = temp->next; 								// 포인터를 다음 노드로 넘김
		if (temp == NULL)								// 포인터가 NULL 이면
			return NULL;
		index--;										// index 1 감소
	}

	return temp;										// 포인터 주소 반환
}

int insertNode(LinkedList *ll, int index, int value){

	ListNode *pre, *cur;													// pre와 cur 포인터 선언

	if (ll == NULL || index < 0 || index > ll->size + 1)					// ll 포인터가 NULL이거나 index가 음수이거나 index가 LinkedList의 size+1보다 크거나
		return -1;

	// If empty list or inserting first node, need to update head pointer
	if (ll->head == NULL || index == 0){									// 머리 노드가 NULL 이거나 index가 0이면
		cur = ll->head;														// cur 포인터에 머리노드 저장
		ll->head = malloc(sizeof(ListNode));								// 머리노드에 ListNode의 Byte만큼 메모리 할당
		ll->head->item = value;												// 머리노드의 item에 매개변수 value 저장
		ll->head->next = cur;												// 머리노드의 next에 cur 포인터(head 포인터) 저장
		ll->size++;															// LinkedList size 1증가
		return 0;
	}


	// Find the nodes before and at the target position
	// Create a new node and reconnect the links
	if ((pre = findNode(ll, index - 1)) != NULL){							// index의 앞 노드주소가 NULL이 아니라면, NULL이면 index주소 잘못됨
		cur = pre->next;													// cur 포인터를 pre(index 이전노드) next로 저장
		pre->next = malloc(sizeof(ListNode));								// pre의 next에 ListNode의 Byte만큼 메모리 할당
		pre->next->item = value;											// pre의 next의 item 에 매개변수 value 저장
		pre->next->next = cur;												// pre의 next의 next에 원래의 next값 저장
		ll->size++;															// LinkedList의 사이즈를 1증가
		return 0;
	}

	return -1;
}


int removeNode(LinkedList *ll, int index){

	ListNode *pre, *cur;

	// Highest index we can remove is size-1
	if (ll == NULL || index < 0 || index >= ll->size)
		return -1;

	// If removing first node, need to update head pointer
	if (index == 0){
		cur = ll->head->next;
		free(ll->head);
		ll->head = cur;
		ll->size--;

		return 0;
	}

	// Find the nodes before and after the target position
	// Free the target node and reconnect the links
	if ((pre = findNode(ll, index - 1)) != NULL){

		if (pre->next == NULL)
			return -1;

		cur = pre->next;
		pre->next = cur->next;
		free(cur);
		ll->size--;
		return 0;
	}

	return -1;
}
