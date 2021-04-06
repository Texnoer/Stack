class Stack:
    def __init__(self):
        self.el = []

    # проверка стека на пустоту. Метод возвращает True или False.
    def isEmpty(self):
        if self.el:
            return False
        else:
            return True

    # добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self, new_el):
        self.el.append(new_el)

    # удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        return self.el.pop()

    # возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self):
        return self.el[-1]

    # возвращает количество элементов в стеке.
    def size(self):
        return len(self.el)


# проверка сбалансированности скобок и правильно вложены друг в друга.
def balance_levels(brackets):
    bracket = Stack()
    for element in brackets:
        if element in open_bracket:
            bracket.push(element)
        elif element in close_bracket.values():
            if bracket.isEmpty():
                return "Несбалансированно"
            else:
                if close_bracket[bracket.peek()] == element:
                    bracket.pop()
                else:
                    return "Несбалансированно"
    if bracket.size() == 0:
        return "Сбалансированно"
    else:
        return "Несбалансированно"


if __name__ == '__main__':
    open_bracket = {'(', '[', '{'}
    close_bracket = {'(': ')', '[': ']', '{': '}'}
    test_1 = balance_levels('(((([{}]))))')
    test_2 = balance_levels('[[{())}]')
    print(test_1)
    print(test_2)

