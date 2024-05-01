from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_jwt.authentication import JWTAuth

from people.models import User, Profile

# convert NunjaAPI to NinjaExtraAPI
api = NinjaExtraAPI()
# add JWt routes
api.register_controllers(NinjaJWTDefaultController)

# Since we have JWTAuth, we can use the auth parameter to protect the route and able to reach to this api when we have a valid token.
@api.get("/add", auth=JWTAuth())
def add(request, a: int, b: int):
    return {"result": a + b}

# register API
@api.post("/register")
def register(request, username: str, password: str, date_of_birth: str, address: str, phone_number: str):
    user = None
    try:
        user = User.objects.get(username=username)
        return {"error": "User already exists"}
    except User.DoesNotExist:
        pass

    try:
        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user, date_of_birth=date_of_birth, address=address, phone_number=phone_number)
        user.save()
    except Exception as e:
        if user:
            user.delete()
        return {"error": str(e)}
    return {"success": "User created"}