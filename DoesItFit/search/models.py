#encoding: utf-8
from django.db import models

# Create your models here.

class Article(models.Model):
    """
    Article représentant un meuble
    """
    name = models.CharField(max_length=100,db_index=True)
    price = models.FloatField()
    img_url = models.URLField()
    width = models.IntegerField()
    height = models.IntegerField()
    lenght = models.IntegerField()
    color = models.CharField(max_length=50)
    ref = models.CharField(max_length=255)
    url = models.URLField()
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    vendor = models.ForeignKey('VendorWebsite', on_delete=models.CASCADE)
    
    def __str__(self):
        """ 
        Affichage de l'article
        """
        return self.name
    
    
class VendorWebsite(models.Model):
    """
    Site marchand du vendeur de meubles
    """
    name = models.CharField(max_length=100,db_index=True)
    url = models.URLField()
    url_search = models.CharField(max_length=255)
    re_articles_number = models.CharField(max_length=255)
    re_article_link = models.CharField(max_length=255)
    articles_per_page = models.IntegerField()
    re_name = models.CharField(max_length=255)
    re_price = models.CharField(max_length=255)
    re_img = models.CharField(max_length=255)
    re_width = models.CharField(max_length=255)
    re_height = models.CharField(max_length=255)
    re_lenght = models.CharField(max_length=255)
    re_color = models.CharField(max_length=255)
    re_ref = models.CharField(max_length=255)
    
    def __str__(self):
        """ 
        Affichage du site
        """
        return self.name