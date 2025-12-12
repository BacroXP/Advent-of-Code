import libs.input

sol1, sol2 = 0, 0


def evaluate(target, todo, allow_concatenation):
    if len(todo) == 1:
        return todo[0] == target

    if evaluate(target, [todo[0] + todo[1]] + todo[2:], allow_concatenation):
        return True

    if evaluate(target, [todo[0] * todo[1]] + todo[2:], allow_concatenation):
        return True

    if allow_concatenation:
        concatenated = int(str(todo[0]) + str(todo[1]))
        if evaluate(target, [concatenated] + todo[2:], allow_concatenation):
            return True

    return False


for line in libs.input.file():
    target, todo = line.strip().split(':')
    target = int(target)
    todo = [int(x) for x in todo.strip().split()]

    if evaluate(target, todo, allow_concatenation=False):
        sol1 += target

    if evaluate(target, todo, allow_concatenation=True):
        sol2 += target
    
print(sol1)
print(sol2)
