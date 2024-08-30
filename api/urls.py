from django.urls import path
from rest_framework import routers
from .views import *
from .api import *
from . import views

router = routers.DefaultRouter()
router.register('api/volunteers',VolunteerViewSet, 'Volunteer')
router.register('api/contactus',ContactUsViewSet, 'ContactUs')
router.register('api/donations',DonationViewset,'Donation')

urlpatterns = [
   path('initiate-payment/', InitiatePaymentView.as_view(), name='initiate_payment'),
   path('verify-payment/', VerifyPaymentView.as_view(), name='verify_payment'),
   path('api/news/',NewsList.as_view(), name='news_list'),
   path('api/gallery/',GalleryList.as_view(), name='gallery')
    ] + router.urls 
