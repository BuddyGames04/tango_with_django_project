from django.contrib import admin
from rango.models import Category, Page

# Define a custom admin class for the Page model
class PageAdmin(admin.ModelAdmin):
    # This attribute specifies the order in which fields should appear in the list display.
    list_display = ( 'title', 'category', 'url')

# Register the Category model with the default admin interface
admin.site.register(Category)

# Register the Page model with the custom admin interface
admin.site.register(Page, PageAdmin)
