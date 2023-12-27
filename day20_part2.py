from collections import deque
from math import lcm


def min_button_presses(lines):
    # module name: (type, [target1, target2, ...])
    module_to_type_target = dict()
    states = dict()
    broadcast_targets = []
    for line in lines:
        left, right = line.split(" -> ")
        targets = right.split(", ")
        if left == "broadcaster":
            broadcast_targets = targets
        else:
            module_type = left[0]
            module_name = left[1:]
            module_to_type_target[module_name] = (module_type, targets)
            if module_type == "%":
                states[module_name] = 0
            else:
                states[module_name] = dict()
                # this will get updated in next pass
    for module, (type, targets) in module_to_type_target.items():
        for target in targets:
            if target in module_to_type_target and module_to_type_target[target][0] == "&":
                states[target][module] = 0
    # exacly one module goes to final rx module and it's conjuction module(sends low pulse if all inputs are high)
    # in that module goes few other conjuction modules, which all has to sent high pulse to final module which will send
    # low pulse to rx module
    # cycles are verified in code below, so we use math.lcm to speed up the process

    (final,) = [module for module, (_, targets)
                in module_to_type_target.items() if "rx" in targets]
    cycle_length = {module: None for module,
                    (_, targets) in module_to_type_target.items() if final in targets}
    cycle_seen_counter = {module: 0 for module in cycle_length.keys()}

    count = 0
    upper_limit = 1000000
    # upper limit used to avoid infinite loops
    while count < upper_limit:
        count += 1
        # each press of button sends low pulse
        # now we have bfs like solving of the circuit
        # items in queue:(source, target, pulse)
        queue = deque([("broadcaster", target, 0)
                      for target in broadcast_targets])
        while queue:
            source, target, pulse = queue.popleft()
            if target not in module_to_type_target:
                continue
            module_type, new_targets = module_to_type_target[target]
            # check cycle conditions
            if target == final and pulse == 1:
                if not cycle_length[source]:
                    cycle_length[source] = count
                cycle_seen_counter[source] += 1
                # verify cycles
                assert cycle_seen_counter[source] * \
                    cycle_length[source] == count
                if all(cycle_seen_counter.values()):
                    return lcm(*cycle_length.values())

            if module_type == "%" and pulse == 0:
                states[target] = (states[target] + 1) % 2
                for new_target in new_targets:
                    queue.append((target, new_target, states[target]))
            elif module_type == "&":
                states[target][source] = pulse
                new_pulse = 0
                for key, val in states[target].items():
                    if val == 0:
                        new_pulse = 1
                        break
                for new_target in new_targets:
                    queue.append((target, new_target, new_pulse))
    return None


# Read input
with open("day20.txt", "r") as f:
    lines = f.read().splitlines()
    print(min_button_presses(lines))
