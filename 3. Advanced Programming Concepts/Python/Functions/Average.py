def evaluate_performance(marks):
    total = 0
    for m in marks:
        total += m

    average = total / len(marks)
    if average >= 40:
        status = "Pass"
    else:
        status = "Fail"
    return total,average,status

mark = [50, 60, 90, 80, 76]
totalmarks, Status, average = evaluate_performance(mark)
print("Total Marks : ",totalmarks)
print("Average Marks : ",average)
print("Status : ",Status)
