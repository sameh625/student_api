from django.db import models

# Student(name, email, year)
# Course(title, code, credits)
# Enrollment(student, course, grade)

class Student(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    year = models.PositiveIntegerField(null=True,blank=True)

    def __str__(self):
        return  self.name
    
class Course(models.Model):
    title = models.CharField(max_length=20)
    code = models.CharField(max_length=15, unique=True)
    credits = models.PositiveIntegerField(default=3)

    def __str__(self):
        return self.title
    
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")

    def __str__(self):
        return f"{self.student.name} ==> {self.course.title}"
    

