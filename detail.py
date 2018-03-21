from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
from django.http import HttpResponse

@view_function
def process_request(request, p:cmod.Product = None):

    # this is for the detail page
    prod = cmod.Product.objects.all()
    print('below is the prod id')
    print(p.id)
    if p is not None:
        prod = prod.get(id=p.id)

    #this helps know to hide the new element lastfive
    itemid = "#item" + str(p.id)



    # this is for middleware
    #if id is part of last five then delete and add new
    for pop in request.lastfive:
        if p.id is pop.id:
            request.lastfive.remove(pop)
            print('i was removed for my twin')
            print(pop.id)

    #add new
    request.lastfive.insert(0, p)

    #print for help on cmd prompt
    print('this is last five')
    print(request.lastfive)
    print('this is the size')
    print(len(request.lastfive))




    context = {
        'prod': prod,
        jscontext('itemid'): itemid,
    }
    return request.dmp.render('detail.html', context)
