from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views

router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
router.register('reviews', views.ReviewViewSet)
urlpatterns = router.urls
