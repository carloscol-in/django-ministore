from rest_framework.views import APIView

from app.store.models import Products


class ListProducts(APIView):
    

    def post(self, request, *args, **kwargs):
        product_data = request.data
        Products.objects.create(product_data)
