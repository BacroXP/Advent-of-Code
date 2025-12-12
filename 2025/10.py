import libs.input
import z3

sol1, sol2 = 0, 0

for line in libs.input.file():
    parts = line.split()

    goal_str = parts[0][1:-1]
    goal_mask = sum(1 << i for i, c in enumerate(goal_str) if c == '#')

    button_specs = parts[1:-1]
    button_masks = []
    button_bits = []

    for spec in button_specs:
        nums = [int(x) for x in spec[1:-1].split(',')]
        mask = sum(1 << n for n in nums)
        button_masks.append(mask)
        button_bits.append(nums)

    best = len(button_specs)

    for subset in range(1 << len(button_specs)):
        acc = 0
        cost = 0

        for i in range(len(button_specs)):
            if subset >> i & 1:
                acc ^= button_masks[i]
                cost += 1

        if acc == goal_mask and cost < best:
            best = cost

    sol1 += best

    joltage_spec = parts[-1]
    target_vals = [int(x) for x in joltage_spec[1:-1].split(',')]

    vars = [z3.Int(f'btn{i}') for i in range(len(button_specs))]
    constraints = []

    for idx, target in enumerate(target_vals):
        terms = [vars[j] for j in range(len(button_specs)) if idx in button_bits[j]]
        constraints.append(sum(terms) == target)

    opt = z3.Optimize()
    opt.minimize(sum(vars))

    for c in constraints:
        opt.add(c)

    for v in vars:
        opt.add(v >= 0)

    opt.check()
    model = opt.model()

    for d in model.decls():
        sol2 += model[d].as_long()

print(sol1)
print(sol2)
