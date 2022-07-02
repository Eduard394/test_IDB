from django.db import models

class PhoneBook(models.Model):
    """Representa un registro en el libro de telefonos.
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = False

    def __str__(self):
        return f"{self.first_name} {self.phone}"
