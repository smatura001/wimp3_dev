import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Months(models.Model):
    id = models.BigAutoField(primary_key=True)
    month_name = models.CharField(max_length=20)
    published_date = models.DateTimeField(auto_now=True,null=True)
    updated_datetime = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self): return self.month_name

class CommodityCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=20)
    published_date = models.DateTimeField(auto_now=True,null=True)
    updated_datetime = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self): return self.description

class CommodityType(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=100)
    commodity_category = models.ForeignKey(CommodityCategory, related_name='commodity_category', on_delete=models.CASCADE,null=True)
    published_date = models.DateTimeField(auto_now=True,null=True)
    updated_datetime = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self): return self.description

class Zone(models.Model):
    id = models.BigAutoField(primary_key=True)
    zone_name = models.CharField(max_length=50)
    published_date = models.DateTimeField(auto_now=True,null=True)
    updated_datetime = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self): return self.zone_name

class District(models.Model):
    id = models.BigAutoField(primary_key=True)
    district_area = models.CharField(max_length=100)
    zone_id = models.ForeignKey(Zone, related_name='zone_id', on_delete=models.CASCADE,null=True)
    published_date = models.DateTimeField(auto_now=True,null=True)
    updated_datetime = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self): return self.district_area

class PestAlertLevel(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=50)
    color_hex = models.CharField(max_length=7,null=True)
    published_date = models.DateTimeField(auto_now=True,null=True)
    updated_datetime = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self): return self.description

class DroughtAlertLevel(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=50,null=True)
    action_level = models.TextField(null=True)
    color_hex = models.CharField(max_length=7,null=True)
    published_date = models.DateTimeField(auto_now=True,null=True)
    updated_datetime = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self): return self.title

class PestRiskEffect(models.Model):
    id = models.BigAutoField(primary_key=True)
    effect_description = models.TextField(null=True)
    published_date = models.DateTimeField(auto_now=True,null=True)
    updated_datetime = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self): return self.effect_description

class PestRiskAction(models.Model):
    id = models.BigAutoField(primary_key=True)
    action_description = models.TextField(null=True)
    published_date = models.DateTimeField(auto_now=True,null=True)
    updated_datetime = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self): return self.action_description

class PestRiskEntryStart(models.Model):
    id = models.BigAutoField(primary_key=True)
    months  = models.JSONField()   # to store multiple months (checkbox list)
    year    = models.IntegerField(default=0)
    commodity_id   = models.ForeignKey(CommodityType, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.commodity_id} - {self.months} - {self.id}"

class PestRiskEntry(models.Model):
    id    = models.BigAutoField(primary_key=True)
    pest_risk_start_id   = models.ForeignKey(PestRiskEntryStart, on_delete=models.CASCADE,null=True)
    district_id    = models.ForeignKey(District, on_delete=models.CASCADE,null=True)
    pest_alert_lvl_id       = models.ForeignKey(PestAlertLevel, on_delete=models.CASCADE,null=True)
    drought_alert_lvl_id    = models.ForeignKey(DroughtAlertLevel, on_delete=models.CASCADE,null=True)
    temp_min    = models.DecimalField(default=0.00,max_digits=5,decimal_places=2)
    temp_max    = models.DecimalField(default=0.00,max_digits=5,decimal_places=2)
    precip_min  = models.DecimalField(default=0.0,max_digits=20,decimal_places=1)
    precip_max  = models.DecimalField(default=0.0,max_digits=20,decimal_places=1)
    effect      = models.ForeignKey(PestRiskEffect, on_delete=models.CASCADE,null=True)
    info        = models.CharField(max_length=500)
    actions     = models.ForeignKey(PestRiskAction, on_delete=models.CASCADE,null=True)
    published_date = models.DateTimeField(auto_now=True,null=True)
    updated_datetime = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self): return self.id