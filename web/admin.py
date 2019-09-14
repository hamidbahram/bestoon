from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Expense)
class AdminExpense(admin.ModelAdmin):
    pass

@admin.register(models.Income)
class AdminIncome(admin.ModelAdmin):
    pass
