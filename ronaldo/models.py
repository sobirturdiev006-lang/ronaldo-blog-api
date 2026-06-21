from django.db import models

class About(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(default=0)
    finished_projects = models.IntegerField(default=0)
    c = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Resume(models.Model):
    year = models.CharField()
    title = models.CharField(max_length=50)
    learn_center = models.CharField(max_length=50)
    description = models.TextField()
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.year

class Malaka(models.Model):
    year = models.CharField()
    title = models.CharField(max_length=50)
    learn_center = models.CharField(max_length=50)
    description = models.TextField()
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.year
class Tajriba(models.Model):
    title = models.CharField(max_length=50)
    percent = models.FloatField(default=0)
    mini_percent = models.FloatField(default=0)
    mini_percent2 = models.FloatField(default=0)
    time = models.CharField(default=0)
    time2 = models.CharField(default=0)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class M_tajriba(models.Model):
    title = models.CharField(max_length=50)
    percent = models.FloatField(default=0)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Sovrinlar(models.Model):
    year = models.CharField()
    learn_center = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_published = models.BooleanField(default=True)

class Service(models.Model):
    title = models.CharField(max_length=50)
    title2 = models.CharField(max_length=50)
    description = models.TextField()
    is_published = models.BooleanField(default=True)


    def __str__(self):
        return self.title

class Projects(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    design_name = models.CharField(max_length=50)
    design_type = models.CharField(max_length=50)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    infor = models.CharField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=50)
    year = models.CharField(default=0)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField()
    phone = models.CharField(default=0)
    email = models.EmailField()
    website = models.URLField(default="")
    is_published = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " " + str(self.created_date)
