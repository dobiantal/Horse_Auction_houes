import jwt
from Bidder.models import Bidder
class Bidder_auth_checker:
    def Check_bidder_auth(self,request):
        self.token = request.COOKIES.get('bid_token')
        if not self.token:
            return False
        try:
            token_layers = jwt.decode(self.token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return False

        self.bidder = Bidder.objects.filter(id=token_layers['id']).first()
        if self.bidder is not None:
            return True