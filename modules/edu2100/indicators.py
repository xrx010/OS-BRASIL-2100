def student_count(classes):
    return sum(row["alunos"] for row in classes)


def class_count(classes):
    return len(classes)


def average_attendance(classes):
    if not classes:
        return 0.0
    return sum(row["frequencia_media"] for row in classes) / len(classes)