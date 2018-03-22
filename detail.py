from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod

@view_function
def process_request(request, p:cmod.Product = None):

    context = {
        'prod': p,
    }
    return request.dmp.render('detail.html', context)
