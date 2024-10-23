# Put your function here
def timesTable(n):
    timetable = []
    for i in range (1, n+1):
        row = []
        for j in range(1, n+1):
            row.append(i*j)
        timetable.append(row)
    return timetable

# testing
nums = int(input())
print(timesTable(nums))
