class ThreeAddressCode:
    def __init__(self):
        self.items = []
        self.code_dict = {}
        self.s_size = -1
        self.d_size = 0

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        self.s_size += 1

    def pop(self):
        if self.isEmpty():
            return 0
        else:
            self.s_size -= 1
            return self.items.pop()

    def seek(self):
        if self.isEmpty():
            return False
        else:
            return self.items[self.s_size]

    def generate(self, expr):
        for i in expr:
            # if i == '-':
            #     op1 = self.pop()
            #     result = self.createCode(op1,None,i)
            #     self.push(result)
            #     print(self.items)
            if i.isalpha():
                self.push(i)
                # print(self.items)
            else:
                op1 = self.pop()
                op2 = self.pop()
                result = self.createCode(op1, op2, i)
                self.push(result)
                # print(self.items)
        return self.code_dict

    def createCode(self, op1, op2, i):
        # if i == '-' and op2 is None:
        #     curr_t = f't{self.d_size}'
        #     self.code_dict[curr_t] = f"{i} {op1}"
        curr_t = f't{self.d_size}'
        self.code_dict[curr_t] = f"{op1} {i} {op2}"
        self.d_size += 1
        return curr_t
        
def generateTable(generated_code,lhs):
    i = 0
    last_t = ''
    print(f'# | {"Op":^7} | {"Arg1":^7} | {"Arg2":^7} | {"Result":^7} |')
    print('- '*22)
    for key, value in generated_code.items():
        valueLst = value.split(' ')
        print(f'{i} | {valueLst[1]:^7} | {valueLst[0]:^7} | {valueLst[2]:^7} | {key:^7} |')
        last_t = key
        i += 1
    print(f'{i} | {"=":^7} | {last_t:^7} | {"None":^7} | {lhs:^7} |')

s = ThreeAddressCode()
expr = input('enter the postfix expression')
lhs=expr[0]
value = s.generate(expr[2:])
print('the result of postfix expression', expr, 'is')
print(value)
generateTable(value,lhs)
