from pathlib import Path

from .indicators import average_attendance, class_count, student_count
from .loader import load_classes, load_school
from .school import School


DATA_PATH = Path(__file__).resolve().parent / "data"


class EduEngine:
    """Motor de indicadores educacionais do módulo Edu2100."""

    def __init__(self, data_path=DATA_PATH):
        data_path = Path(data_path)
        self.school = School.from_manifest(load_school(data_path / "escola_demo.yaml"))
        self.classes = load_classes(data_path / "turmas.csv")

    @property
    def school_name(self):
        return self.school.name

    @property
    def municipality(self):
        return self.school.municipality

    @property
    def students(self):
        return student_count(self.classes)

    @property
    def class_total(self):
        return class_count(self.classes)

    @property
    def average_attendance(self):
        return average_attendance(self.classes)

    @property
    def okrs(self):
        return self.school.okrs

    def summary(self):
        return {
            "escola": self.school_name,
            "municipio": self.municipality,
            "alunos": self.students,
            "turmas": self.class_total,
            "frequencia_media": self.average_attendance,
            "metas_okr": self.okrs,
        }