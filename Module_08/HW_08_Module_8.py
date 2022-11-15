import collections


def get_count_visits_from_ip(ips):
    return collections.Counter(ips)


def get_frequent_visit_from_ip(ips):
    a = collections.Counter(ips)
    return a.most_common(1)


student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_marks)
print(mark_counts)  # Counter({4: 4, 6: 3, 1: 3, 2: 2, 7: 2, 3: 2, 5: 2})


print(get_count_visits_from_ip(student_marks))
