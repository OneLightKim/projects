"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# 사용자가 요청할 주소 생성, 생성된 앱의 Views 함수와 연결 - routing
from django.contrib import admin
from django.urls import path, include
from viewer.views import main, index1, hwpx_viewer,xlsx_viewer, pptx_viewer, pdf_viewer, file_viewer, test
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index1/', index1),
    path('main/', main),
    # path('hwpx_viewer/',hwpx_viewer),
    # path('xlsx_viewer/',xlsx_viewer),
    # path('pptx_viewer/',pptx_viewer),
    path('file/',include('viewer.urls')),
    # path('pdf_viewer/',pdf_viewer),
    path('hwpxtxt_viewer/',file_viewer),
    path('xlsxtxt_viewer/',file_viewer),
    path('pptxtxt_viewer/',file_viewer),
    path('pdftxt_viewer/',file_viewer),
    path('test/',test),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

