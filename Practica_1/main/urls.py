from django.urls import path, re_path
from . import views
from registro import views as v
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('<int:id>', views.index, name = 'index'),
    path('', views.home, name = 'home'),
    path('create/', views.create, name = 'create'),
    path('home/', views.home, name = 'home'),
    path('salir/', views.logged_out, name = 'logged_out'),
    path('editar_datos/', views.editar, name = 'editar'),
    path('accounts/login/', views.home, name = 'home'),
    path('profile/<str:nom>', views.profile, name='profile' ),
    path('actualizar/<str:username>/',v.profile, name='actualizar'),
    path('upload/', views.upload, name='upload'),
    path('files/',views.files_list, name = 'files list'),
    path('edicion/<int:id_archivo>',views.edicion, name = 'edicion'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
