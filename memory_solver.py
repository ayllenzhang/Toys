round = 0

def get_input():
    global round
    round += 1
    print(f'Round {round}:')
    s = input()
    screen, buttons = s.split(' ')
    return int(screen), [int(digit) for digit in buttons]


## Round 1
screen_num, button_nums = get_input()
pos1 = 2 if screen_num < 3 else 3 if screen_num == 3 else 4
num1 = button_nums[pos1 - 1]
print(f'pos {pos1}, num {num1}\n')


## Round 2
screen_num, button_nums = get_input()

if screen_num == 2 or screen_num == 4:
    pos2 = pos1
    num2 = button_nums[pos2 - 1]
elif screen_num == 1:
    pos2 = button_nums.index(4) + 1
    num2 = 4
else:
    pos2 = 1
    num2 = button_nums[0]

print(f'pos {pos2}, num {num2}\n')


## Round 3
screen_num, button_nums = get_input()

if screen_num == 3:
    pos3 = 3
    num3 = button_nums[2]
else:
    num3 = num2 if screen_num == 1 else num1 if screen_num == 2 else 4
    pos3 = button_nums.index(num3) + 1

print(f'pos {pos3}, num {num3}\n')


## Round 4
screen_num, button_nums = get_input()
pos4 = 1 if screen_num == 2 else pos1 if screen_num == 1 else pos2
num4 = button_nums[pos4 - 1]
print(f'pos {pos4}, num {num4}\n')

## Round 5
screen_num, button_nums = get_input()
num5 = num1 if screen_num == 1 else num2 if screen_num == 2 else num4 if screen_num == 3 else num3
pos5 = button_nums.index(num5) + 1
print(f'pos {pos5}, num {num5}\n')
