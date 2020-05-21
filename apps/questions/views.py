from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User


# Create your views here.
def answer(request):
    return Response({}, 200)


@api_view(['POST'])
def signup(request):
    username = request.data['username']
    try:
        user = User(username=username)
        user.save()
        return Response({'user_id':user.id}, 200)    
    except Exception:
        print('error')
        return Response({'error': 'duplicate username'}, 400)

    


def question(request):
    return Response({}, 200)
