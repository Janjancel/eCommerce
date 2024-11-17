from django.contrib import admin
from .models import Furniture

# Register your models here.
class FurnitureAdmin(admin.ModelAdmin):
  list_display = ("prodName", "category", "price","availability",)
  prepopulated_fields = {"slug": ("prodName", "category")}

admin.site.register(Furniture, FurnitureAdmin)