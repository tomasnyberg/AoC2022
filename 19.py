import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import defaultdict, deque

# Heuristic weighted for the higher value items
def heur(state):
    ore, clay, obsidian, geodes, _, _, _, _, _ = state
    return 1000*geodes + 100*obsidian + 10*clay + ore

def apply_heuristic(time, depth, queue, heur_size):
    if time < depth:
        queue = deque(sorted(queue, key=heur, reverse=True))
        queue = deque(list(queue)[:heur_size])
        depth = time
    return depth, queue

def new_states(state, costs, oldstate, queue):
    orecurr, clay_curr, obcurr, _, oremachine, claymachine, obsidianmachine, _, _ = oldstate
    ore_cost, clay_cost, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian = costs
    new_states = [list(state) for _ in range(5)]
    for i in range(4):
        for s in new_states:
            s[i] += s[i+4]
    for s in new_states:
        s[8] -= 1
    for i, pred, costs, add in [[0, True, [0,0,0], [0,0,0,0]],
                                [1, orecurr >= ore_cost, [ore_cost,0,0], [1,0,0,0]],
                                [2, orecurr >= clay_cost, [clay_cost, 0,0], [0,1,0,0]],
                                [3, orecurr >= obsidian_ore and clay_curr >= obsidian_clay, [obsidian_ore,obsidian_clay,0], [0,0,1,0]],
                                [4, orecurr >= geode_ore and obcurr >= geode_obsidian, [geode_ore,0,geode_obsidian], [0,0,0,1]]]:
        if not pred: continue
        for j, base in enumerate([orecurr + oremachine, clay_curr + claymachine, obcurr + obsidianmachine]):
            new_states[i][j] = base - costs[j]
        for j in range(len(add)):
            if add[j]:
                new_states[i][j+4] += 1
        queue.append(tuple(new_states[i]))
    return new_states

def prune(state, maxore, obsidian_clay, geode_obsidian):
    state = list(state)
    for i, compare in [[4, maxore], [5, obsidian_clay], [6, geode_obsidian]]:
        state[i] = min(compare, state[i])
    for i, comp in [[0, maxore - state[4]], [1, obsidian_clay - state[5]], [2, geode_obsidian - state[6]]]:
        state[i] = min(state[-1]*comp*(state[-1]-1), state[i])
    return tuple(state)

def bfs(ore_cost, clay_cost, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian, start_time, heur_size):
    best = 0
    starting = (0, 0, 0, 0, 1, 0, 0, 0, start_time)
    queue = deque([starting])
    seen = set()
    depth = start_time
    while queue:
        state = queue.popleft()
        geodecurr,time = state[3], state[-1]
        oldstate = state[:]
        depth, queue = apply_heuristic(time, depth, queue, heur_size)
        best = max(best, geodecurr)
        if time==0: continue
        maxore = max([ore_cost, clay_cost, obsidian_ore, geode_ore])
        state = prune(state, maxore, obsidian_clay, geode_obsidian)
        if state in seen: continue
        seen.add(state)
        costs = [ore_cost, clay_cost, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian]
        new_states(state, costs, oldstate, queue)
    return best

part_one = 0
part_two = 1
for idx, line in enumerate(lines):
    idx, orecost, claycost, obsidianore, obsidianclay, geodeore, geodeobsidian = map(int, re.findall(r'\d+', line))
    if idx < 4:
        part_two *= bfs(orecost, claycost, obsidianore, obsidianclay, geodeore, geodeobsidian, 32, 500000)
    part_one += idx*(bfs(orecost, claycost, obsidianore, obsidianclay, geodeore, geodeobsidian, 24, 70000))

print("Part one:", part_one)
print("Part two:", part_two)