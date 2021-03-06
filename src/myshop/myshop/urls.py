from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('orders/', include('myshop.apps.orders.urls', namespace='orders')),
	path('payment/', include('myshop.apps.payment.urls', namespace='payment')),
	path('cart/', include('myshop.apps.cart.urls', namespace='cart')),
	path('coupons/', include('myshop.apps.coupons.urls', namespace='coupons')),

	path('', include('myshop.apps.shop.urls', namespace='shop')),

] + static(settings.MEDIA_URL,
							document_root=settings.MEDIA_ROOT)



