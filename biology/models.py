from django.db import models

# Create your models here.
class Units(models.Model):
    unitId = models.AutoField(primary_key=True, auto_created=True)
    unitName = models.CharField(max_length=200)
    
    def __str__(self):
        return self.unitName


class Notes(models.Model):
    noteId = models.AutoField(primary_key=True, auto_created=True)
    unitId = models.ForeignKey(Units, default=1, on_delete=models.CASCADE)
    noteTitle = models.CharField(max_length=200)
    noteContent = models.TextField()
    
    def __str__(self):
        return self.noteTitle
    