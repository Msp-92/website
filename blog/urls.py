from django.urls import path
from .views import HomePage , BlogPage , PostDetail

urlpatterns = [
    path('', HomePage.as_view(),name='home'),
    path('blog/', BlogPage.as_view(),name='blog'),
    path('blog/<slug:slug>', PostDetail.as_view(),name='post-detail'),
]
