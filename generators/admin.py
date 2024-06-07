from django.contrib import admin
from .models import MyClass, Aspect, MyClassElement, AspectElement

admin.site.register([MyClass, Aspect, MyClassElement, AspectElement])

# summary glossary index page info, complications lvl1, lvl2, lvl3
# submit: quest y descripcion
# submit: complications, description.
# static web pages?