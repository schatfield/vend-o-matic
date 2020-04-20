
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from vendomaticApp.models import Coin

class CoinSerializer(serializers.HyperlinkedModelSerializer):
    """
    JSON serializer for coins
    
    Arguments:
        serializers.HyperlinkedModelSerializer
    """
        
    class Meta:
        model = Coin
        #makes it click
        url = serializers.HyperlinkedIdentityField(
            view_name="coins",
            lookup_field='id'
        )
        fields = ('id', 'coin_count')
        
        
class Coins(ViewSet):
        
    """Coins for Vendomatic API"""


# # handles PUT
    def update(self, request, pk=None):
        """Handle PUT requests for an order
        Returns:
            Response -- Empty body with 204 status code
        """
        print("anything")
        coin = Coin.objects.get(pk=pk)

        # += add on to record total
        # when the client makes a request, it is added onto the coin_count property bc of +=
        # ["coin"] is the name of a property in the data object, it has to match this name you give it in postman
        coins_inserted = request.data["coin"]
        # todo: error checks
        # if more than one coin or 0, throw error

        coin.coin_count += coins_inserted
    
        #this is another way of doing the same thing. store coin.coin_count into a variable
        # current_total = coin.coin_count
        # coin.coin_count = current_total + coins_inserted
        
        coin.save()

        serializer = CoinSerializer(
            coin,
            context={'request': request}
            )

        return Response(serializer.data)


    # handles DELETE
    def destroy(self, request, pk=None):
        """Handles DELETE requests for a single park area
        Returns:
            Response -- 204, 404, or 500 status code
        """
        coin = Coin.objects.get(pk=pk)
        # how do we store the amount coins someone has entered? in this variable- you have grabbed the value we need to change
        inserted_coins = coin.coin_count
        coin.coin_count = 0
        coin.save()

        response = Response({}, status=status.HTTP_204_NO_CONTENT)
        response['X-Coins'] = inserted_coins    
        return response


#         try:
#             order = Order.objects.get(pk=pk)
#             order.delete()

#             return Response({}, status=status.HTTP_204_NO_CONTENT)
        
#         except Order.DoesNotExist as ex:
#             return Response({'message': ex.args[0]},
#             status=status.HTTP_404_NOT_FOUND)

#         except Exception as ex:
#             return Response({'message': ex.arg[0]},