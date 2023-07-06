from django.urls import path
from . import views

app_name='file'  #신규

urlpatterns = [
    path('pptx_viewer/', views.pptx_viewer, name='pptx_viewer'),
    path('xlsx_viewer/', views.xlsx_viewer, name='xlsx_viewer'),
    path('pdf_viewer/', views.pdf_viewer, name='pdf_viewer'),
    path('hwpx_viewer/', views.hwpx_viewer, name='hwpx_viewer'),
]
