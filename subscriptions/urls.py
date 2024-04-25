from django.urls import path
from .views import (SubscribeView, 
                    SubscriptionSuccessView, 
                    ManageSubscriptionView,
                    CreateCheckoutSessionView,
                    SuccessView,
                    CancelView,
                    ProductLandingPageView)

urlpatterns = [
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('subscription_success/', SubscriptionSuccessView.as_view(), name='subscription_success'),
    path('manage_subscription/', ManageSubscriptionView.as_view(), name='manage_subscription'), 
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('', ProductLandingPageView.as_view(), name='landing'),
]