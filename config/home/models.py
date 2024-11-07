from django.db import models

# Create your models here.



class PortfolioItem(models.Model):
    title = models.CharField(max_length=100)  # عنوان پروژه
    description = models.TextField()  # توضیحات پروژه
    image = models.ImageField(upload_to='media/portfolio_images/')  # تصویر پروژه
    tech = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد پروژه
    
    def __str__(self):
        return self.title



class Message(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} : {self.message}"