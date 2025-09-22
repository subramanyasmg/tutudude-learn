from rest_framework import serializers
from helloworld.models import Post


class BlogSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('id','created_by',)

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return Post.objects.create(**validated_data)