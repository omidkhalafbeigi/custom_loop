max_number = [1, 4, 5, 5]
index = len(max_number) - 1
generated_number = [0, 0, 0, 0]
writer = open('results.txt', mode='w')


while True:
    generated_number[index] += 1
    print(generated_number)
    writer.write(str(generated_number) + '\n')
    if generated_number == max_number: break
    all_examined = False
    while all_examined is False:
        if generated_number[index] >= max_number[index]:
            generated_number[index] = 0
            if generated_number == max_number: break
            if index > 0:
                index -= 1
            else:
                generated_number[index] += 1
                all_examined = True
        else:
            generated_number[index] += 1
            print(generated_number)
            writer.write(str(generated_number) + '\n')
            if generated_number == max_number: break
            index = len(max_number) - 1
            all_examined = True

writer.close()
    
