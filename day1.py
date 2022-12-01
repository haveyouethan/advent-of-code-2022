fp = 'aoc2022/day1.txt'

with open(fp,'r') as f:
    input = f.readlines()

# transform input string into list of each elf's list of calories
clean_input = (','.join([x.strip() for x in input])).split(',,')

# calculate total calories for each individual elf
lst_elf = []
for calories in clean_input:
    total_cal = sum([int(x) for x in calories.split(',')])
    lst_elf.append(total_cal)

# calc max of all elfs
soln1 = max(lst_elf)
print(f"Ans 1: {soln1}")


# sort elfs in descending order, and sum the top 3 elf's calories
lst_elf_sorted = sorted(lst_elf, reverse=True)
soln2 = sum(lst_elf_sorted[:3])
print(f"Ans 2: {soln2}")
