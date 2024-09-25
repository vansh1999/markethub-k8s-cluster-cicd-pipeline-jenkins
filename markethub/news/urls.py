from django.urls import path

from . import views


urlpatterns = [

	path("" , views.home , name="home"),
	path("/get_prices" , views.get_prices , name="get_prices")
	

]