from django.contrib import admin

# Register your models here.
from .models import Months, District, Zone, CommodityType, CommodityCategory, PestAlertLevel, DroughtAlertLevel, PestRiskEntryStart, PestRiskEntry, PestRiskEffect, PestRiskAction

admin.site.register(Months)
admin.site.register(District)
admin.site.register(Zone)
admin.site.register(CommodityCategory)
admin.site.register(CommodityType)
admin.site.register(PestAlertLevel)
admin.site.register(DroughtAlertLevel)
#admin.site.register(Livestock)

admin.site.register(PestRiskEntryStart)
admin.site.register(PestRiskEntry)
admin.site.register(PestRiskEffect)
admin.site.register(PestRiskAction)