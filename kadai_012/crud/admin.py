from django.contrib import admin # 管理画面を使うたものモジュール
from .models import Product, Category # modelsで定義したProduct,Categoryクラスをインポート
from django.utils.safestring import mark_safe

# 商品管理画面をカスタマイズするためのクラスを定義(adminモジュールのModelAdmin(管理画面をカスタマイズするためのクラス)を継承)
class ProductAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'price', 'category','image') #id以外はmodels.pyで定義している
  search_fields = ('name',) # 名前で検索できるようにする
  list_filter = ('category',) # 絞り込み

  def image(self, obj):
    return mark_safe('<img src="{}" style="width:auto height:50px;">'.format(obj.img.url))


class CategoryAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')
  search_fields = ('name',)


#adimnモジュールの.site.register＜データ管理ページ（編集できる）を追加＞.(何を追加するか：Product, ProductAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.register(Category, CategoryAdmin)