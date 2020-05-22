from rest_framework import serializers

class QuestionSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=200)
    id = serializers.ReadOnlyField()

    class Meta:
        read_only = True



class ChoiceSerializer(serializers.Serializer):
    choice = serializers.CharField(max_length=200)
    id = serializers.ReadOnlyField()
    is_correct = serializers.BooleanField()
    question = QuestionSerializer(read_only=True)





