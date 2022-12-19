import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import defaultdict, deque

# Each robot can collect 1 of its resource type per minute. 
# It also takes one minute for the robot factory (also conveniently from your pack) 
# to construct any type of robot, although it consumes the necessary
#  resources available when construction begins.
# 24 minutes

# Heuristic weighted for geodes
def heur(state):
    ore, clay, obsidian, geodes, _, _, _, _, _ = state
    return 1000*geodes + 100*obsidian + 10*clay + ore

def apply_heuristic(time, depth, queue):
    if time < depth:
        queue = deque(sorted(queue, key=heur, reverse=True))
        queue = deque(list(queue)[:70000])
        depth = time
    return depth, queue

def generate_states(state):
    new_states = [list(state) for _ in range(5)]
    for i in range(4):
        for s in new_states:
            s[i] += s[i+4]
    for s in new_states:
        s[8] -= 1
    return new_states

def prune(state, maxore, obsidian_clay, geode_obsidian):
    state = list(state)
    orecurr,clay_curr,obcurr,geodecurr,oremachine,claymachine,obsidianmachine,geodemachine,time = state
    for i, compare in [[4, maxore], [5, obsidian_clay], [6, geode_obsidian]]:
        state[i] = min(compare, state[i])
    for i, comp in [[0, maxore - state[4]], [1, obsidian_clay - state[5]], [2, geode_obsidian - state[6]]]:
        state[i] = min(time*comp*(time-1), state[i])
    return tuple(state)

def bfs(ore_cost, clay_cost, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian, start_time):
    best = 0
    starting = (0, 0, 0, 0, 1, 0, 0, 0, start_time)
    queue = deque([starting])
    seen = set()
    depth = start_time
    while queue:
        state = queue.popleft()
        orecurr,clay_curr,obcurr,geodecurr,oremachine,claymachine,obsidianmachine,geodemachine,time = state
        depth, queue = apply_heuristic(time, depth, queue)
        best = max(best, geodecurr)
        if time==0: continue
        maxore = max([ore_cost, clay_cost, obsidian_ore, geode_ore])
        state = prune(state, maxore, obsidian_clay, geode_obsidian)
        if state in seen: continue
        seen.add(state)
        new_states = generate_states(state)
        queue.append(tuple(new_states[0]))
        orebase = orecurr + oremachine
        claybase = clay_curr + claymachine
        obsidianbase = obcurr + obsidianmachine
        for i, pred, costs, add in [[1, orecurr >= ore_cost, [ore_cost,0,0], [1,0,0,0]],
                                    [2, orecurr >= clay_cost, [clay_cost, 0,0], [0,1,0,0]],
                                    [3, orecurr >= obsidian_ore and clay_curr >= obsidian_clay, [obsidian_ore,obsidian_clay,0], [0,0,1,0]],
                                    [4, orecurr >= geode_ore and obcurr >= geode_obsidian, [geode_ore,0,geode_obsidian], [0,0,0,1]]]:
            if not pred: continue
            new_states[i][0] = orebase - costs[0]
            new_states[i][1] = claybase - costs[1]
            new_states[i][2] = obsidianbase - costs[2]
            for j in range(len(add)):
                if add[j]:
                    new_states[i][j+4] += 1
            queue.append(tuple(new_states[i]))
    print(best)
    return best

result = 0
for idx, line in enumerate(lines):
    idx, orecost, claycost, obsidianore, obsidianclay, geodeore, geodeobsidian = map(int, re.findall(r'\d+', line))
    result += idx*(bfs(orecost, claycost, obsidianore, obsidianclay, geodeore, geodeobsidian, 24))
print(result)