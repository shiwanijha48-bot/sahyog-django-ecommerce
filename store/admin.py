from django.contrib import admin
from django.contrib.auth.models import User

#  Register your models here
from .models import Product, Artisan, ArtisanApplication


# PRODUCT ADMIN
admin.site.register(Product)


# ARTISAN ADMIN
admin.site.register(Artisan)


# ARTISAN APPLICATION ADMIN
@admin.register(ArtisanApplication)
class ArtisanApplicationAdmin(admin.ModelAdmin):

    list_display = ('name', 'village', 'craft', 'approved')

    actions = ['approve_artisans']

    def approve_artisans(self, request, queryset):

        for application in queryset:

            # prevent duplicate approval
            if application.approved:
                continue

            # create username
            username = application.name.replace(" ", "").lower()

            # avoid duplicate usernames
            if User.objects.filter(username=username).exists():
                username = username + str(application.id)

            # create login account
            user = User.objects.create_user(
                username=username,
                password='artisan123'
            )

            # create artisan profile
            Artisan.objects.create(
                user=user,
                name=application.name,
                village=application.village,
                craft=application.craft,
                story=application.story,
                image=application.image,
            )

            # mark approved
            application.approved = True
            application.save()

        self.message_user(
            request,
            "Selected artisans approved successfully."
        )

    approve_artisans.short_description = "Approve selected artisans"