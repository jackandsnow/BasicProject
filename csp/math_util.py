def get_median(data_list):
    """
    get median form data list
    :param data_list: data list
    :return: median
    """
    data_list.sort()
    length = len(data_list)
    half = length // 2
    if length % 2 == 0:
        return (data_list[half] + data_list[~half]) / 2
    else:
        return data_list[half]


def generate_postfix(infix):
    """
    generate postfix expression str
    :param infix: infix expression str, like '2x3+8/3'
    :return: postfix expression str, like '23x83/+'
    """
    op_rank = {'x': 2, '/': 2, '+': 1, '-': 1}
    stack = []
    post_list = []
    for s in infix:
        if s in '+-x/':  # operator
            while stack and op_rank.get(stack[-1]) >= op_rank.get(s):  # priority
                post_list.append(stack.pop())
            stack.append(s)
        else:  # operand
            post_list.append(s)
    while stack:
        post_list.append(stack.pop())
    return ''.join(post_list)


def calculate_postfix(postfix):
    """
    calculate postfix expression
    :param postfix: postfix expression str, like '23x83/+'
    :return: int result, like 2x3+8/3=6+2=8
    """
    stack = []
    for p in postfix:
        if p in '+-x/':  # operator
            value_2 = int(stack.pop())
            value_1 = int(stack.pop())
            if p == '+':
                result = value_1 + value_2
            elif p == '-':
                result = value_1 - value_2
            elif p == 'x':
                result = value_1 * value_2
            else:
                result = value_1 // value_2
            stack.append(result)
        else:
            stack.append(p)
    return stack.pop()
