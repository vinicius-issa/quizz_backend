from django.contrib import admin
from .models import Choice, Question
from django.contrib import messages


def take_iscorrect(elem):
    return elem.is_correct


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        if len(instances):
            instances.sort(key=take_iscorrect)
            corrects = 0
            corrects_choice_saved = Choice.objects.filter(
                question=instances[0].question.id,
                is_correct=True)

            if corrects_choice_saved.exists():
                corrects = 1
                correct_choice_saved = corrects_choice_saved[0]
            else:
                correct_choice_saved = None

            for instance in instances:
                if correct_choice_saved:
                    if instance.id == correct_choice_saved.id:
                        if not instance.is_correct:
                            corrects -= 1
                            instance.save()
                    elif instance.is_correct:
                        corrects += 1
                else:
                    if instance.is_correct:
                        corrects += 1
            print ('Corrects: {}'.format(corrects))
            if corrects <= 1:
                for instance in instances:
                    instance.save()
                formset.save_m2m()
            else:
                messages.set_level(request, messages.ERROR)
                messages.error(request, 'Exists more than one correct option')


admin.site.register(Question, QuestionAdmin)
