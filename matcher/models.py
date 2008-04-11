from django.db import models

# Create your models here.

class HashType(models.Model):
    idHashType = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    def __unicode__(self):
	return self.description

    class Admin:
	pass

class FileInstance(models.Model):
    idFile = models.AutoField(primary_key=True)
    hash = models.CharField(max_length=128)
    fileLength = models.IntegerField()
    machine = models.CharField(max_length = 20)
    fullPath = models.CharField(max_length = 300)
    fileName = models.CharField(max_length = 100)
    idHashType = models.ForeignKey(HashType)
    def __unicode__(self):
	return self.fileName + " on " + self.machine

    class Admin:
	pass
