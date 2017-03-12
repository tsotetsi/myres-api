from myres.apps.api.serializers import UserProfileSerializer


def login_response_payload_handler(token, user=None, request=None):
    """
    Returns the response data for both the login and refresh views.
    """
    return {
        'token': token,
        'user': UserProfileSerializer(user, context={'request': request}).data,
    }
