numbers = [3, 4, 5, 6, 7, 8, 10, 12, 13]
for i in range(len(numbers)):
    with open(f"video{numbers[i]}.txt", 'r') as f:
        lines = f.readlines()

    lines = [line.replace('\n', ' ') for line in lines]

    with open(f"video{numbers[i]}_new.txt", 'w') as f:
        f.writelines(lines)
