"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path # path()を使えるようにする
from crud import views # view.pyのクラスを使えるようにインポート
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # adminにアクセスされたら、admin.site.urls（管理者画面をユーザーに返す）を実行
    path('', views.TopView.as_view(), name="top"), # トップページ
    path('crud/', views.ProductListView.as_view(), name="list"), # 商品一覧ページ
    path('crud/new/', views.ProductCreateView.as_view(), name="new"), # 新規作成画面（listのテンプレートに、新規作成時の移動先としてnewを指定しているから、このパスが該当し、逆説的にcrud/new/のURLが完成する）
    path('crud/edit/<int:pk>', views.ProductUpdateView.as_view(), name="edit"),
    # <int:pk>の部分は商品のIDが入る。
    path('crud/delete/<int:pk>', views.ProductDeleteView.as_view(), name="delete"),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)