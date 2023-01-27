from rest_framework import serializers

from .models import Product, Comment, Like

class ProductSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()
        
    def get_comment_count(self, obj):
        return obj.comment_set.all().count()
        #return Comment.objects.filter(product=obj).count()
    
    class Meta:
        model = Product
        fields = '__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    member_username = serializers.SerializerMethodField()
    tstamp = serializers.DateTimeField(
        read_only=True, format='%Y-%m-%d %H:%M:%S'
    )
    
    def get_product_name(self, obj):
        return obj.product.name
    
    def get_member_username(self, obj):
        return obj.member.username
    
    class Meta:
        model = Comment
        fields = '__all__'
        
class CommentCreateSerializer(serializers.ModelSerializer):
    member = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        required=False
    )
    
    def validate_member(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError('member is required')
        return value
    
    class Meta:
        model = Comment
        fields = '__all__'
        # extra_kwargs = {'member': { 'required': False }}
        
        
class LikeCreateSerializer(serializers.ModelSerializer):
    # member를 body로 받는 게 아니라 자동으로 넣겠다는 설정
    member = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        required=False
    )
    
    # 유효성 검사 -> 에러에 대한 적절한 결과 설정
    def validate_member(self, value):   # _member : member라는 값에 대한 유효성 검사를 하겠다
        if not value.is_authenticated:
            raise serializers.ValidationError('member is required')
        return value
    
    class Meta:
        model = Like
        fields = '__all__'