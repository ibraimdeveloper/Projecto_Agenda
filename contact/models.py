from django.db import models

# Create your models here.


# first_name(string), last_name(string), email(string), phone_number(string)
# created_date(date), description(text), category (foreign key), show(boolean)
# owner(foreign key), picture(imagem)


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)


    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'