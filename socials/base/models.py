from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from ckeditor.fields import RichTextField
from django.urls import reverse

from .utils import preprocess_text_for_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    fname = models.TextField(blank=True)
    lname = models.TextField(blank=True)
    username=models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')

    def __str__(self):
        return(str(self.user)) 

    def get_absolute_url(self):
        return reverse('home')

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user

class Post(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(null=True,blank=True,upload_to="images/")
    title_tag=models.CharField(max_length=255,default="")
    author=models.ForeignKey(Profile,on_delete=models.CASCADE)
    caption=RichTextField(blank=True,null=True)
    post_date=models.DateField(auto_now_add=True)
    location=models.CharField(max_length=255,default="")
    no_of_likes=models.IntegerField(default=0)
    is_hate = models.BooleanField(default=False)

    def predict_is_hate(self, loaded_model):
        # Get the text from the caption field
        text = self.caption
        print("Original Text:", text)

        # Preprocess the text using the new preprocessing function
        preprocessed_text = preprocess_text_for_model(text)

        # Make predictions using the loaded model
        prediction = loaded_model.predict(preprocessed_text)
        print("Prediction:", prediction)


        # Assuming your model predicts a binary outcome (0 or 1)
        is_hate = prediction[0] > 0.5

        # Update the is_hate field in the model
        self.is_hate = is_hate

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

    def get_owner_pp(self):
        return self.author.profileimg.url

    def profileid(self):
        return self.author.user.id

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    is_hate = models.BooleanField(default=False)

    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)

    def get_absolute_url(self):
        return reverse('home')

class LikePost(models.Model):
    post_id=models.CharField(max_length=500)
    username=models.CharField(max_length=100)

    def __str__(self):
        return self.username



