##Method 1
def get_gang(graph, cur, mems):
    nexts = graph[cur]
    for nex in nexts:
        if nex not in mems:
            mems.add(nex)
            get_gang(graph, nex, mems)

n, c = map(int, input().split())
graph = {}
for i in range(1, n + 1):
    graph[i] = set()
que = set()
for i in range(c):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
    que.add(a)
    que.add(b)
# print(graph)
debug_mode = n == 72715
max_size = 1
while len(que) > 0:
    cur = que.pop()
    members = set()
    members.add(cur)
    get_gang(graph, cur, members)
    que = que - members
    max_size = max(max_size, len(members))
print(max_size)











## Method 2
no_of_people , no_of_combination = map(int,input().split())
gangs={i:set([i]) for i in range(1,no_of_people+1)}
for i in range (no_of_combination):
    person1,person2=map(int,input().split())
    gangs[person1].add(person2)
    gangs[person2].add(person1)
ans={}
res = 0
for gang in gangs:
    ans[gang] = {gang}
    for person in gangs[gang]:
        ans[gang] = ans[gang]|gangs[person]
        gangs[person] = gangs[person] | ans[gang]
    if res<len(list(ans[gang])):
        res = len(list(ans[gang]))
print(res)