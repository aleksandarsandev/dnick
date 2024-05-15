from django.db import models

# Create your models here.
class Publishing_House(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    year=models.IntegerField()
    website = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    COVER_CHOISES = [
        ("Hard", "Hard"),
        ("Soft","Soft")
    ]
    CATEGORY_CHOISES = [
        ("Romance","Romance"),
        ("Thriler","Thriler"),
        ("Biography","Biography"),
        ("Classic","Classic"),
        ("Drama","Drama"),
        ("History","History")
    ]
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to="cover_images/",null=True,blank=True)
    isbn=models.CharField(max_length=15)
    year=models.IntegerField()
    publishing_house=models.ForeignKey(Publishing_House,on_delete=models.CASCADE)
    pages=models.IntegerField()
    dimensions=models.CharField(max_length=11)
    cover_type=models.CharField(max_length=5,choices=COVER_CHOISES)
    price=models.IntegerField()
    genre=models.CharField(max_length=15,choices=CATEGORY_CHOISES)

    def __str__(self):
        return self.title



