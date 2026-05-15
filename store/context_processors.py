from .models import Artisan


#  -------- ARTISAN STATUS --------
def artisan_status(request):
    is_artisan = False
    if request.user.is_authenticated:
        is_artisan = Artisan.objects.filter(user=request.user).exists()
    return { 'is_artisan': is_artisan }