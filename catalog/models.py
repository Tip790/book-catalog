from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default="4.00")
    
    def __str__(self):
        return self.title
        return self.price
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.body