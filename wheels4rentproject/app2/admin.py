from django.contrib import admin
from .models import Registration, CarModels, Admin, Contact

admin.site.register(Registration)
admin.site.register(CarModels)
admin.site.register(Admin)
admin.site.register(Contact)