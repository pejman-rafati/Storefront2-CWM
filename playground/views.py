from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection
from tags.models import TaggedItem


def say_hello(request):
    collection = Collection.objects.get(pk=11)
    collection.title = 'Games'
    collection.featured_product = None
    collection.save()
    return render(request, 'hello.html', {'name': 'pejman'})
    # queryset = Product.objects.filter(
    # id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')

    # queryset1 = Order.objects.select_related(
    #     'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:3]
    # queryset2 = Product.objects.prefetch_related('promotions') ---- , 'products2': list(queryset2)
