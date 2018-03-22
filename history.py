from catalog import models as cmod

class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        product_ids = request.session.get('last_five', [])
        request.last_five = []
        for p in product_ids:
            request.last_five.append(cmod.Product.objects.get(id=   p))


        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        product_ids = []
        for p in request.last_five:
            product_ids.append(p.id)

        if len(product_ids) > 6:
            product_ids.pop()

        request.session['last_five'] = product_ids

        return response
