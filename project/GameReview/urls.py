
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

app_name = "GameReview"

urlpatterns = [
    path('pages/',views.pageIndex,name='Pages'),
    #Main App
    path('',views.home,name='Index'),
    path('about',views.about, name="About"),
    path('reviews',views.ReviewList.as_view(), name="ReviewListar"),
    path('reviews/new',views.ReviewAdd.as_view(), name="ReviewAgregar"),
    path('reviews/<pk>/',views.ReviewDetail.as_view(), name="ReviewDetalle"),
    path('reviews/<pk>/edit',views.ReviewEdit.as_view(), name="ReviewEditar"),
    path('reviews/<pk>/delete',views.ReviewDelete.as_view(), name="ReviewBorrar"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)