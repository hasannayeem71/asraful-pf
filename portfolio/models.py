from django.db import models

# Create your models here.
class recentProject(models.Model):
    projectname = models.CharField(max_length=200)
    projectcatagory = models.CharField(choices=(
        ('Web Design',"Web Design"),
        ('web development',"Web Development"),
        ('Wordpress',"wordpress"),
    ),
      max_length=60,null=True,blank=True
      )
    websitelink = models.TextField(default="#",blank=True,null=True)
    Picture = models.ImageField( )
    def __str__(self):
        return str(self.projectname)
    
    
class message(models.Model):  
    firstName = models.CharField(max_length=80,null=False)
    lastname = models.CharField(max_length=50,null=True)
    email = models.EmailField()
    message = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return str(self.firstName)