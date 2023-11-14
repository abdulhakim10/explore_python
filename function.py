sub_count = int(input("how many want to calculate:"))
total = 0
avg = 0

for count in range(sub_count):
    mark = int(input("enter mark: {} ".format(count + 1)))
    total += mark
    avg = total / (count + 1)

print("total mark is: {} and average is: {}".format(total, avg))