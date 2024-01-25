from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='author_profiles/', null=True, blank=True)
    author_id = models.CharField(max_length=15, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.author_id:
            city_code = f"AR{self.city[:3].upper()}"
            latest_author = Author.objects.filter(city=self.city).order_by('-id').first()
            if latest_author:
                last_author_id = int(latest_author.author_id[-4:])
                self.author_id = f"{city_code}{str(last_author_id + 1).zfill(4)}"
            else:
                self.author_id = f"{city_code}0001"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    num_pages = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author.name}"

