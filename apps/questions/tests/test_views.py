import pytest
from apps.questions.models import Choice, Question, Response as Answer
from django.contrib.auth.models import User
from apps.questions.views import signup, question, answer
from django.urls import reverse


@pytest.fixture(autouse=True)
def populate_db(request, db):
    user = User(
        username='usertest',
        password='Str0ng-password')
    user.save()

    questions_titles = ["Question1", "Question2"]
    choices_titles = ["Title1", "Title2", "Title3", "Title4"]
    for title in questions_titles:
        question = Question(question=title)
        question.save()
        for choice_title in choices_titles:
            choice = Choice(
                choice=choice_title,
                is_correct=False,
                question=question)
            choice.save()
        choice = Choice(
            choice='Title5',
            is_correct=True,
            question=question)
        choice.save()


def test_signup(rf):
    path = reverse('signup')

    request = rf.get(path)
    response = signup(request)
    assert response.status_code == 405

    request = rf.post(path, {'username': 'usertest2'})
    response = signup(request)
    assert response.status_code == 200
    print (response.data)
    assert response.data['user_id'] > 0

    response = signup(request)
    assert response.status_code == 400


@pytest.mark.django_db
def test_get_questions(rf):

    user = User.objects.first()
    path = reverse('question', kwargs={'user_id': user.id})

    request = rf.get(path)
    response = question(request, user.id)
    assert response.status_code == 200
    assert len(response.data['unanswered']) == 2
    assert len(response.data['answered']) == 0

    choice = Choice.objects.first()
    answer = Answer(user=user, choices=choice)
    answer.save()
    response = question(request, user.id)
    assert len(response.data['unanswered']) == 1
    assert len(response.data['answered']) == 1


@pytest.mark.django_db
def test_answer(rf):
    user = User.objects.first()
    choice = Choice.objects.first()
    path = reverse('answer')

    assert Answer.objects.all().count() == 0

    request = rf.post(path, {'user': user.id, 'choice_id': choice.id})
    response = answer(request)
    assert response.status_code == 302
    assert Answer.objects.all().count() == 1
