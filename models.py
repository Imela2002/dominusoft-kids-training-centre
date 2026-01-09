from django.db import models

class News(models.Model):
    title = models.CharField(max_length=80)
    subheading = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title

class ProgramCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(null=True, upload_to="program_img/")
    button_label = models.CharField(max_length=20, default="View Programs")

    def _str_(self):
        return self.name

class Program(models.Model):
    category = models.ForeignKey(ProgramCategory, default="1", on_delete=models.CASCADE, related_name="programs", null=True, blank=True)
    program_name = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.CharField(max_length=30)

    def _str_(self):
        return self.program_name

class ContactMessage(models.Model):
    emri = models.CharField(max_length=50)
    mbiemri = models.CharField(max_length=50)
    email = models.EmailField()
    mesazhi_juaj = models.TextField()

    def _str_(self):
        return self.emri


# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
# python manage.py createsuperuser

# python -m venv venv
# venv\Scripts\activate
# pip install django
# python -m pip install Pillow