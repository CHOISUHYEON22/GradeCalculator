def drop_while(F, COLL):
        TF_TUPLE = tuple(map(F, COLL))
        return COLL[:TF_TUPLE.index(False)] if False in TF_TUPLE else COLL


def grade_calc(ranking: int, same_ranking_num: int, student_num: int) -> tuple:
    percentage = (ranking + same_ranking_num) / student_num * 100
    division = (0, 4, 11, 23, 40, 60, 77, 89, 96, 100)
    grade = len(drop_while(lambda x: percentage > x, division))
    pos_in_grade = (percentage - division[grade - 1]) / (division[grade] - division[grade - 1]) * 100
    return grade, round(pos_in_grade, 2)


def average_grade(grade: tuple, semester_hour: tuple) -> float:
    return round(sum(map(lambda x, y: x * y, grade, semester_hour)) / sum(semester_hour), 2)
