from django.db import models

# Create your models here.


class Portfolio(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    position = models.CharField(max_length=200, blank=True, null=True)
    experience = models.CharField(max_length=200, blank=True, null=True)
    portfolio_link_id = models.ForeignKey(
        "PortfolioLink", blank=True, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(
        upload_to='static/profile/', blank=True, null=True)


class PortfolioLink(models.Model):
    select = (
        ("Web", "Web"),
        ("Mobile App", "Mobile App")
    )
    project_name = models.CharField(max_length=200, blank=True, null=True)
    project_type = models.CharField(
        max_length=200, blank=True, null=True, choices=select)
    link = models.CharField(max_length=200, blank=True, null=True)
    project_image = models.ImageField(upload_to='static/portfolio_img/')
