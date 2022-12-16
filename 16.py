import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))
flows = {}
adj_lists = {}
candidates = []
for line in lines:
    split = line.split(" ")
    curr = split[1]
    num = int(re.findall(r'-?\d+', line)[0])
    to_list = ""
    if "valves" in line:
        to_list = line.split(" valves ")[1]
    else:
        to_list = line.split(" valve ")[1]
    flows[curr] = num
    adj_lists[curr] = to_list.split(", ")
    if num > 0:
        candidates.append(curr)

def bfs(curr, pairwise):
    q = [curr]
    visited = set()
    level = 0
    while q:
        for _ in range(len(q)):
            node = q.pop(0)
            visited.add(node)
            pairwise[curr][node] = level
            for adj in adj_lists[node]:
                if adj not in visited:
                    q.append(adj)
        level += 1
# For every node in the graph, find the shortest path to every other node using bfs
pairwise = {}
for node in adj_lists:
    pairwise[node] = {}
    bfs(node, pairwise)

def flow(mask):
    result = 0
    for b in range(len(candidates)):
        if (1 << b & mask):
            result += flows[candidates[b]]
    return result

def solve():
    dp = [ [ [ -10**9 for _ in range(2**len(candidates)) ] for _ in range(len(candidates)) ] for _ in range(31) ]
    ans = 0
    ans2 = 0
    # Mark out the starting points, every other point will have a score of -10**9
    for i in range(len(candidates)):
        d = pairwise["AA"][candidates[i]]
        dp[d+1][i][1 << i] = 0
    # dp[i][k][j] = max score we can get if we are at node k at time i with mask j
    # Go through every minute
    for i in range(1, 31):
        # Go through every possible mask
        for j in range(1 << len(candidates)):
            # Go through every possible point to be at
            for k in range(len(candidates)):
                # If this is not a node we want to open, just skip
                if ((1 << k & j) == 0):
                    continue
                f = flow(j)
                # We can choose to just stay where we are and not do anything
                hold = dp[i-1][k][j] + f
                dp[i][k][j] = max(hold, dp[i][k][j])
                ans = max(ans, dp[i][k][j])
                # Check every other node and decide if we want to move there
                for l in range(len(candidates)):
                    # This node is not one we want open, skip
                    if(((1 << l) & j) != 0):
                        continue
                    d = pairwise[candidates[k]][candidates[l]]
                    # We won't get to this node in time so don't check it
                    if i + d + 1 >= 31:
                        continue
                    # If doing what we have so far and then moving to that node is 
                    # better than what we have so far for being at that node at that time 
                    # with those nodes active, update it
                    val = dp[i][k][j] + f*(d+1)
                    if val > dp[i+d+1][l][j | (1 << l)]:
                        dp[i+d+1][l][j | (1 << l)] = val
    # We can reuse our p1 dp array for p2,
    # we just need to find the best way to split the mask into two parts
    for i in range(1 << len(candidates)):
        for j in range(1 << len(candidates)):
            if (i & j) != j:
                continue
            me = -10**9
            elephant = -10**9
            for k in range(len(candidates)):
                me = max(me, dp[26][k][j])
            # The elephant takes all the valves that I don't take
            for k in range(len(candidates)):
                elephant = max(elephant, dp[26][k][i& ~j])
            ans2 = max(ans2, me+elephant)
    return (ans, ans2)

answers = solve()
print("Part one:", answers[0])
print("Part two:", answers[1])
