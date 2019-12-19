from django.contrib import admin
from .models import Todo, SignUp # add this

class TodoAdmin(admin.ModelAdmin):  # add this
  list_display = ('title', 'description', 'completed') # add this

# Register your models here.
admin.site.register(Todo, TodoAdmin) # add this
admin.site.register(SignUp) # add this