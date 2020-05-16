from django.db import models


class EducationLevel(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    rank = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title


class SubjectStudy(models.Model):
    title = models.CharField(max_length=255)
    status = models.BooleanField()
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


class ExamType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Exam(models.Model):
    university = models.CharField(max_length=255)
    education_level = models.ForeignKey(EducationLevel, on_delete=models.PROTECT)
    subject_study = models.ForeignKey(SubjectStudy, on_delete=models.PROTECT)
    education_year = models.CharField(max_length=255)
    semester = models.CharField(max_length=255)
    exam_type = models.ForeignKey(ExamType, on_delete=models.PROTECT)
