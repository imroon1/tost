from django.conf.urls import url
from .views import (
		ProductListView, 
		# product_list_view, 
		# ProductDetailView,
		ProductDetailSlugView,
		# ProductFeaturedListView,
		# ProductFeaturedDetailView,
		# product_detail_view
		)

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
	url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),

]


