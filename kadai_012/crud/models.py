from django.db import models
from django.urls import reverse


class Category(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Product(models.Model): # 商品一覧のクラス
  name = models.CharField(max_length=200) # 商品名（文字列、200字以内）
  price = models.PositiveIntegerField() # 値段（正の整数）
  category = models.ForeignKey(Category, on_delete=models.CASCADE) # カテゴリークラスとのリレーション（1:多の、多側にリレーション設定を書くのでProductに書いている）on_delete=はカテゴリーが削除されたときの処理で、models.CASCADEは属する商品も一緒に削除するという設定。
  img = models.ImageField(blank=True, default='noImage.png') # 画像を追加するとき、画像なしで追加可能（blank=True）、そのときはnoImage.pngが適用されるよ
  detail = models.TextField(blank=True, null=True)

  def __str__(self): # 自分の名前を表示するときの設定
    return self.name # その名前を表示（djangoではデフォルトでこれがobject(〇)でreturnするようになっている）
  
  def get_absolute_url(self): # 新規作成画面の登録ボタンを押したときの遷移先
    return reverse('list') # CreateViewは、登録後どのurlに行くかを探している。get_absolute_urlを定義すると行き先が決まる。reverse()関数は、'list'というurlの名前から、crud/list/を逆引きするためのもの。