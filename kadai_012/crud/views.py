from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy


class TopView(TemplateView): # 指定したhtmlを表示するviewを作る。
  template_name = "top.html" # 表示したいhtmlファイルは"top.html"だよ。（setting.pyでEMPLATES = ['APP_DIRS': True]としているから、アプリケーション（crud）内のtemplatesファイルにアクセスできる）


# データを一覧表示するためのクラス（ListViewを継承）
class ProductListView(ListView): # （テンプレート側に対して、model一覧のオブジェクトを「object_list」という名前で渡す）
  model = Product # 何を表示するか＝product
  template_name = "list.html" # 表示したいhtmlファイルは"list.html"だよ。但し、ListViewを使う場合は、テンプレート名がデフォルトで「モデル名.list.html」となる。今回の場合はmodel=Productとしているので、テンプレート名はproduct_list.htmlとなる。なので、上記のように明示しなくても自動的にテンプレート名はproduct_list.htmlになっている。

  paginate_by = 3 # 1ページに表示する数を指定

class ProductCreateView(CreateView): # 新規作成に特化したクラス
  model = Product # 何を作る？：Product
  fields = '__all__' # 新規作成時にユーザーが入力するフィールドを指定、__all__は全てを作成するという意味で、この場合models内のProductクラスで定義しているnameとpriceを入力するフィールドが出現する。
  # tenplate_name = デフォルトでmodel名_form.htmlになっているので記載不要。


class ProductUpdateView(UpdateView): # 編集に特化したクラス
  model = Product # 何を編集する？:Product
  fields = '__all__'
  template_name_suffix = '_update_form' # デフォルトでproduct_form.htmlになってしまっている。name_suffixで末尾を指定してあげることで、_formのところが_update_formになる。つまり、product_update_form.html。


class ProductDeleteView(DeleteView): # 削除に特化したクラス
  model = Product
  success_url = reverse_lazy('list') # 削除時に遷移するURL、listから逆引きしてね。クラスの読み込み時点では、urls.pyが未だ完全に読み込まれていないため、reverse('list')だとエラーになる。lazyを付けることで遅延評価して、タイムラグによるエラーを防ぐ。
  # template_name = デフォルトでproduct_confirm_delete.html