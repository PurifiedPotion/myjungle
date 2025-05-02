import sys
input = sys.stdin.read

data = input().split()
t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    applicants = []

    for _ in range(n):
        doc_rank = int(data[index])
        interview_rank = int(data[index + 1])
        applicants.append((doc_rank, interview_rank))
        index += 2

    applicants.sort()

    count = 1
    best_interview = applicants[0][1]
    for i in range(1, n):
        if applicants[i][1] < best_interview:
            count += 1
            best_interview = applicants[i][1]

    results.append(str(count))

print("\n".join(results))