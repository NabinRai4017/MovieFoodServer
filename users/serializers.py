from dj_rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer
from rest_framework import serializers
from dj_rest_auth.models import TokenModel
from dj_rest_auth.serializers import UserDetailsSerializer as DefaultUserDetailsSerializer


class LoginSerializer(RestAuthLoginSerializer):
    username = None



class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """
    user = DefaultUserDetailsSerializer(many=False, read_only=True)  # this is add by myself.
    class Meta:
        model = TokenModel
        fields = ('key', 'user')  