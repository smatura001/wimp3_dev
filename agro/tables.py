# tables.py
import django_tables2 as tables
from .models import PestRiskEntry

class PestRiskListTable(tables.Table):
    class Meta:
        model = PestRiskEntry
        template_name = "django_tables2/bootstrap4.html"  # or bootstrap5
        fields = ("id", "district_id", "pest_alert_lvl_id", "drought_alert_lvl_id", "temp_max", "temp_min", "precip_min", "precip_max", "effect", "info", "actions")
