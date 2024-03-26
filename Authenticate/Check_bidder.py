import jwt
from Bidder.models import Bidder
def Check_bidder_auth(request):
    token = request.COOKIES.get('bid_token')
    if not token:
        return False
    try:
        token_layers = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return False

    bidder = Bidder.objects.filter(id=token_layers['id']).first()
    if bidder is not None:
        return True