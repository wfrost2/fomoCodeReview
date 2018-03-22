from django.conf import settings
from django_mako_plus import view_function, jscontext
from django.http import HttpResponseRedirect
from catalog import models as cmod

@view_function
def process_request(request, product:cmod.Product=None):
    if product is None:
        return HttpResponseRedirect('/catalog/index/')
    # request.lastProduct = product
    if product in request.last_five:
        request.last_five.remove(product)
    request.last_five.insert(0, product)
    context = {
        'product' : product,
        'category' : product.category,

    }
    # print(products, categories)
    return request.dmp.render('/detail.html', context)
