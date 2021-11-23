from operator import add,mul

with open('aoc2019_2.txt','r') as f:
    data = f.read().split(',')
data = [int(n) for n in data]    
data[1],data[2] = 12,2

memory = data[:]    

def intcode(noun,verb, memory):
    memory[1],memory[2] = noun, verb
    ops = {1:add, 2:mul}
    for pointer in range(0,len(memory)-4,4):
        instruction = memory[pointer:pointer+4]
        op = instruction[0]
        if op == 99:
            break
        elif op in [1,2]:
            ope = ops[op]
            a = memory[instruction[1]]
            b = memory[instruction[2]]
            index = instruction[3]
            memory[index] = ope(a,b)
    return memory[0]
        
part1 = intcode(12,2,memory)
print(part1,'\n')
#part2

target = 19690720

for noun in range(100):
    for verb in range(100):
        memory = data[:]
        output = intcode(noun, verb, memory)
        if output == target:
            answer =   noun*100+verb
            

print(f'part1= {part1}  part2= {answer}')
