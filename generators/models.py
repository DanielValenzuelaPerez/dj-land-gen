from django.db import models


class MyClass(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.name


class MyClassElement(models.Model):
    name = models.CharField(max_length=50)
    class_name = models.ForeignKey('MyClass', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Class element"
        verbose_name_plural = "Class elements"

    def __str__(self):
        return self.name


class Aspect(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AspectElement(models.Model):
    name = models.CharField(max_length=50)
    aspect_name = models.ForeignKey('Aspect', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
