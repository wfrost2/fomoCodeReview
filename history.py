from catalog import models as cmod


class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        prod_ids = request.session.get('lastfive', 0)
        #test code
        print(prod_ids)

        #create empty list
        request.lastfive = []

        #find each product using the prod_ids and append it to the request.lastfivelist
        if prod_ids is not 0:
            for p in prod_ids:
                product = cmod.Product.objects.filter(id=p)
                for pr in product:
                    request.lastfive.append(pr)
        else:
            request.lastfive.append(prod_ids)

        #check cmd prompt to see if it looks right
        print('this is the new request.last five before appending current item')
        print(request.lastfive)


        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        #list of ids
        ids = []


        #removes 7th element
        if len(request.lastfive) is 7:
            print('deleting this')
            print(request.lastfive[6])
            request.lastfive.pop()

        #turn product objects into id ints
        for prod in request.lastfive:
            ids.append(prod.id)

        #list of ints to request.session
        request.session['lastfive'] = ids

        return response
