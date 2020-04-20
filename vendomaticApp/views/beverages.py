from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from vendomaticApp.models import Beverage

class BeverageSerializer(serializers.HyperlinkedModelSerializer):
    """
    JSON serializer for beverages
    
    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    
    # beverage = BeverageSerializer()
    
    class Meta:
        model = Beverage
        #makes it click
        url = serializers.HyperlinkedIdentityField(
            view_name="beverages",
            lookup_field='id'
        )
        fields = ('id', 'name', 'quantity')
        
        
class Beverages(ViewSet):
    """
    Beverages for Vendomatic API
    
    """
    
    #Handles a post request allowing creation with http request
    def create(self, request):
        """
        Handle POST operations
       
        Returns:
            Response -- JSON serialized Order instance
        """
        new_beverage = Beverage()
        
        new_beverage.save()

        serializer = BeverageSerializer(
            new_beverage,
            context={'request': request}
            )

        return Response(serializer.data)

    
    # # Get a Single Item 
    # def retrieve(self, request, pk=None):
    #     """Handle GET requests for a single beverage.
        
    #     Fetch call to get one order by order id:
    #         http://localhost:8000/beverages/${id}
        
    #     Returns:
    #         Response -- JSON serialized Order instance
    #     """
    #     try:
    #         beverage = Beverage.objects.get(pk=pk)
    #         serializer = BeverageSerializer(beverage, context={'request': request})
    #         return Response(serializer.data)
    #     except Exception as ex:
    #         return HttpResponseServerError(ex)


    # # handles GET all
    # def list(self, request):
    #     """Handle GET requests to beverages resource
        
    #     Fetch call to get all orders in the database:
    #         http://localhost:8000/beverages
        
        
    #     Returns:
    #         Response -- JSON serialized list of orders
    #     """
    #     # list of beverage instances
    #     beverages = Beverage.objects.all()
            
    #     # takes beverages and converts to JSON
    #     serializer = BeverageSerializer(
    #         orders,
    #         many=True, #query has multiple items otherwise serializer will only return one object
    #         context={'request': request}
    #     )
    #     # Return the JSON
    #     return Response(serializer.data)


    # # handles PUT
    # def update(self, request, pk=None):
    #     """
    #     Handle PUT requests for a beverage
        
    #     Returns:
    #         Response -- Empty body with 204 status code
    #     """
    #     beverage = Beverage.objects.get(pk=pk)
    #     beverage.name = request.data["name"]
    #     beverage.quantity= request.data["quantity]
    #     order.save()

    #     serializer = OrderSerializer(
    #         beverage,
    #         context={'request': request}
    #         )

    #     return Response(serializer.data)


    # # handles DELETE
    # def destroy(self, request, pk=None):
    #     """
    #     Handles DELETE requests for a single beverage
        
    #     Returns:
    #         Response -- 204, 404, or 500 status code
    #     """
    #     try:
    #         beverage = Beverage.objects.get(pk=pk)
    #         beverage.delete()

    #         return Response({}, status=status.HTTP_204_NO_CONTENT)
        
    #     except Beverage.DoesNotExist as ex:
    #         return Response({'message': ex.args[0]},
    #         status=status.HTTP_404_NOT_FOUND)

    #     except Exception as ex:
    #         return Response({'message': ex.arg[0]},