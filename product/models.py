from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=125, verbose_name='상품명')
    price = models.IntegerField(verbose_name='가격')
    product_type = models.CharField(max_length=8, verbose_name='상품유형',
        choices=(
            ('단품', '단품'),
            ('세트', '세트')
            )
    )
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')
    
    class Meta:
        db_table = 'shinhan_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'    
        


# 댓글 모델 만들기
# 사용자 외래키, 상품 외래키, 댓글 내용, tstamp
# 관리자 페이지에 등록해서
# 관리자 페이지 통해서 댓글 3개 작성

class Comment(models.Model):
    member = models.ForeignKey('member.Member',  on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey('product.Product',  on_delete=models.CASCADE, verbose_name='상품')
    content = models.TextField(verbose_name='댓글 내용')
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')
    
    class Meta:
        db_table = 'shinhan_product_comment'
        verbose_name = '상품 댓글'
        verbose_name_plural = '상품 댓글' 
        


class Like(models.Model):
    member = models.ForeignKey('member.Member',  on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey('product.Product',  on_delete=models.CASCADE, verbose_name='상품')
    
    class Meta:
        db_table = 'shinhan_product_like'
        verbose_name = '상품 좋아요'
        verbose_name_plural = '상품 좋아요' 