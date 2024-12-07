

def evaluate(target, todo, allow_concatenation):
    # Escape Mechanism
    if len(todo) == 1:
        return todo[0] == target

    # Start Recursivtree for '+'
    if evaluate(target, [todo[0] + todo[1]] + todo[2:], allow_concatenation):
        return True

    # Start Recursivtree for '*'
    if evaluate(target, [todo[0] * todo[1]] + todo[2:], allow_concatenation):
        return True

    # Start Recursivtree for '||'
    if allow_concatenation:
        concatenated = int(str(todo[0]) + str(todo[1]))
        if evaluate(target, [concatenated] + todo[2:], allow_concatenation):
            return True

    return False

def sol(address):
    p1, p2 = 0, 0

    for line in open(address).read().strip().strip().split('\n'):
        target, todo = line.strip().split(':')
        target = int(target)
        todo = [int(x) for x in todo.strip().split()]

        if evaluate(target, todo, allow_concatenation=False):
            p1 += target

        if evaluate(target, todo, allow_concatenation=True):
            p2 += target
    
    print(p1)
    print(p2)

sol("test.txt")
sol("input.txt")
