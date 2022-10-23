def total_salary(path) -> float:
    sum_of_salary = 0
    salary_report = open(path, mode='r')
    try:
        while True:
            line = salary_report.readline()
            if not line:
                break
            _, value = line.split(',')
            sum_of_salary += float(value)
    finally:
        salary_report.close()
    return sum_of_salary


summary = total_salary(
    r'C:\Users\nsher\Documents\! VSCode Projects\Learn_Python\Module_06\file_for_1task.txt')
print(summary)
