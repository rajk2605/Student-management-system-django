from django.db import models

class studentModel(models.Model):
    rno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    marks = models.IntegerField()
    
    def __str__(self):
        return str(self.rno) + " " + str(self.name) + " " + str(self.marks)