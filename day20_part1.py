from collections import deque


def pulse_product(lines):
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

    buttton_presses = 1000
    pulse_count = {0: 0, 1: 0}

    for count in range(buttton_presses):
        # each press of button sends low pulse; we have 1000 presses
        # increase for initial low pulse(button -> broadcaster)
        pulse_count[0] += 1
        # now we have bfs like solving of the circuit
        # items in queue:(source, target, pulse)
        queue = deque([("broadcaster", target, 0)
                      for target in broadcast_targets])
        while queue:
            source, target, pulse = queue.popleft()
            # print(source + " - " + str(pulse) +" -> " + target)
            pulse_count[pulse] += 1
            if target not in module_to_type_target:
                continue
            module_type, new_targets = module_to_type_target[target]
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
    return pulse_count[0] * pulse_count[1]


# Testing
test1 = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""
ans1 = 32000000
assert pulse_product(test1.splitlines()) == ans1

# Read input
with open("day20.txt", "r") as f:
    lines = f.read().splitlines()
    print(pulse_product(lines))
