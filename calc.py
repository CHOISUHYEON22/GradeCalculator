def calc(ranking: int, same_ranking_num: int, student_num: int) -> int:
    percentage = (ranking + same_ranking_num) / student_num * 100
    if percentage <= 4: grade = 1
    elif percentage <= 11: grade = 2
    elif percentage <= 23: grade = 3
    elif percentage <= 40: grade = 4
    elif percentage <= 60: grade = 5
    elif percentage <= 77: grade = 6
    elif percentage <= 89: grade = 7
    elif percentage <= 96: grade = 8
    else: grade = 9
    return grade


def average_grade(grade: tuple, semester_hour: tuple) -> float:
    return sum(map(lambda x, y: x * y, grade, semester_hour)) / sum(semester_hour)
