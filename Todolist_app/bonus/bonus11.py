def get_avg():
    with open("bonus/files/data.txt","r") as file:
        data = file.readlines()

    values = data[1:] #List Slicing
    values = [float(i) for i in values] #List Comprehension
    avg = sum(values) / len(values)
    return avg

average = get_avg()
print(average)