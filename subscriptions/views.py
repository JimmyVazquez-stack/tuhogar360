from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, View
from django.utils import timezone

#Stripe imporation
import stripe
from django.conf import settings    
from django.http import JsonResponse
from django.views import View
from .models import Price
from .models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY

class SubscribeView(TemplateView):
    template_name = 'subscribe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['levels'] = SubscriptionLevel.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        level_id = request.POST.get('level_id')
        level = SubscriptionLevel.objects.get(pk=level_id)
        UserSubscription.objects.create(
            user=request.user,
            subscription_level=level,
            end_date=timezone.now() + timezone.timedelta(days=30)  # Suscripción mensual por defecto
        )
        return redirect('subscription_success')

class SubscriptionSuccessView(TemplateView):
    template_name = 'subscription_success.html'

class ManageSubscriptionView(TemplateView):
    template_name = 'manage_subscription.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_subscription = UserSubscription.objects.get(user=self.request.user)
        context['user_subscription'] = user_subscription
        return context

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs["pk"])
        domain = "https://yourdomain.com"
        if settings.DEBUG:
            domain = "http://127.0.0.1:1000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/subscriptions/success/',
            cancel_url=domain + '/subscriptions/cancel/',
        )
        print(checkout_session.url)
        return redirect(checkout_session.url)
    
class SuccessView(TemplateView):
    template_name = "success.html"
 
class CancelView(TemplateView):
    template_name = "cancel.html"

 
class ProductLandingPageView(TemplateView):
    template_name = "landing.html"
 
    def get_context_data(self, **kwargs):
        product = Product.objects.get(name="Suscripcion level 1")
        prices = Price.objects.filter(product=product)
        context = super(ProductLandingPageView,
                        self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "prices": prices
        })
        return context