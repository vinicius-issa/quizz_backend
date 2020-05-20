import pytest
from apps.questions.models import Choice, Question, Response
from django.contrib.auth.models import User


@pytest.fixture
def new_question(django_db_blocker):
    question_title = "How are you?"
    with django_db_blocker.unblock():
        question = Question(question=question_title)
        question.save()
    return question


@pytest.fixture(scope="module")
def new_question_with_incorrect_choices(django_db_blocker):
    titles = ["Choice1", "Choice2", "Choice3", "Choice4"]
    question_title = "How are you?"
    with django_db_blocker.unblock():
        question = Question(question=question_title)
        question.save()
        for title in titles:
            choice = Choice(
                choice=title,
                is_correct=False,
                question=question
            )
            choice.save()
        question.save()
    return question


@pytest.mark.django_db
def test_create_question(new_question):
    assert new_question.id == 1


@pytest.mark.django_db
def test_create_choices(new_question):
    choice_title = "Fine, Thanks"
    choice = Choice(
        choice=choice_title,
        is_correct=False,
        question=new_question
    )
    choice.save()
    assert choice.id == 1


@pytest.mark.django_db
def test_question_exist_correct_choices(new_question_with_incorrect_choices):
    question = new_question_with_incorrect_choices
    assert not question.exist_correct_response()
    choice = Choice(
        choice="Correct choice",
        is_correct=True,
        question=question
    )
    choice.save()
    assert question.exist_correct_response()


@pytest.mark.django_db
def test_create_response(new_question):
    choice = Choice(choice='Fine, Thanks', question=new_question)
    choice.save()
    user = User(username='userTest', password='Str0ng-Password')
    user.save()
    response = Response(user=user, choices=choice)
    response.save()
    assert response.id == 1
