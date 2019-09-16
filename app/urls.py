
import rest_framework.routers

from . import views


router = rest_framework.routers.DefaultRouter()

router.register(r'clients', views.ClientViewSet, basename='client')
router.register(r'favorite-products', views.FavoriteProductsViewSet, basename='favorite-products')

urlpatterns = router.urls 