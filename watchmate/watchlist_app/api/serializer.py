from rest_framework import serializers

from ..models import Watchlist,Streamplatform

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields='__all__'


class StreamplatformSerializer(serializers.ModelSerializer):
    ##showing  list of flim in each plat from by using related name nested serializer
    watchlist = WatchlistSerializer(many= True,read_only=True)

    ## StringRelatedField may be used to represent the target
    ## of the relationship using its __str__ method.
    # watchlist= serializers.StringRelatedField(many=True)


    ##PrimaryKeyRelatedField may be used to represent the target of
    ## the relationship using its primary key.
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    ##HyperlinkedRelatedField may be used to represent the target 
    ##of the relationship using a hyperlink.
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='Watchlist_Update_Delete'
    # )

    
    class Meta:
        model = Streamplatform
        fields='__all__'
