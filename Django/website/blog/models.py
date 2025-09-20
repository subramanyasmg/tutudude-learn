from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    public_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def summary(self):
        return self.body[:100]

    def pub_date(self):
        return self.public_date.strftime('%b %d, %Y')

    def __str__(self):
        return self.title


    # class Meta:
    #     ordering = ['-public_date']
    #