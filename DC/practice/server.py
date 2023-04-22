processes = int(input("Enter number of processes : "))
resources = int(input("Enter number of resources : "))

print(f"\nEnter allocated resources for each process : \n")
allocated = [[int(i) for i in input(f"Process {j+1} : ").split()] for j in range(processes)]

print(f"\nEnter maximum resources for each process : \n")
max_need = [[int(i) for i in input(f"Process {j+1} : ").split()] for j in range(processes)]

print(f"\nEnter available resources : \n")
available = [int(x) for x in input().split()]

safe_sequence = []
visited = [0] * processes

def can_allocate_resources(i):
    for j in range(resources):
        if max_need[i][j] - allocated[i][j] > available[j]:
            return False
    return True

def release_resources(i):
    for j in range(resources):
        available[j] += allocated[i][j]
    visited[i] = 1
    safe_sequence.append(i)

while visited.count(0) != 0:
    not_found = True
    for i in range(processes):
        if visited[i] == 0 and can_allocate_resources(i) == True:
            release_resources(i)
            not_found = False
            
    if not_found:
        break

if len(safe_sequence) == processes:
    print(f"\nThe processes are in safe state and the safe sequence is : {safe_sequence}")
else:
    print("\nThe processes are in an unsafe state")