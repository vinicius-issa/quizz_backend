from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from apps.questions.models import Response as Answer, Question, Choice
from .serializers import ChoiceSerializer, QuestionSerializer


# Create your views here.
def answer(request):
    return Response({}, 200)


@api_view(['POST'])
def signup(request):
    username = request.data['username']
    try:
        user = User(username=username)
        user.save()
        return Response({'user_id': user.id}, 200)
    except Exception:
        print('error')
        return Response({'error': 'duplicate username'}, 400)


@api_view(['GET'])
def question(request, user_id):
    questions = Question.objects.all()
    unanswered = []
    answered = []
    answers = Answer.objects.filter(user_id=user_id)

    for answer in answers:
        questions = questions.exclude(id=answer.choices.question.id)
        choice_json = ChoiceSerializer(answer.choices).data
        answered.append(choice_json)

    for question in questions:
        if question.exist_correct_response():
            choices = Choice.objects.filter(question=question)
            question_json = QuestionSerializer(question).data
            choices_json = ChoiceSerializer(choices, many=True).data
            question_json['choices'] = choices_json
            unanswered.append(question_json)

    data = {
        'answered': answered,
        'unanswered': unanswered
    }
    return Response(data, 200)
    
