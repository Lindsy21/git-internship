def calculate_average(scores):
    return sum(scores) / len(scores)


def determine_result(average):
    if average >= 50:
        return "PASS"
    else:
        return "FAIL"
