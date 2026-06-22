from django.urls import path
from .views import *

urlpatterns = [
    
   path('login/', LoginAPI),
   path('perfil/', PerfilAPI),
   path('cadastrar/', UsuarioCadastrarAPI),

   path('areas/listar/', AreasListarAPI, name='AreasListarAPI'),
   path('areas/inserir/', AreaInserirAPI, name='AreaInserirAPI'),
   path('areas/editar/<int:id>/', AreaEditarAPI, name="AreaEditarAPI"),
   path('areas/remover/<int:id>/', AreaRemoverAPI, name="AreaRemoverAPI"),

   path('publicos/listar/', PublicosListarAPI, name='PublicosListarAPI'),
   path('publicos/inserir/', PublicoInserirAPI, name='PublicoInserirAPI'),
   path('publicos/editar/<int:id>/', PublicoEditarAPI, name="PublicoEditarAPI"),
   path('publicos/remover/<int:id>/', PublicoRemoverAPI, name="PublicoRemoverAPI"),

   path('cursos/listar/', CursosListarAPI, name='CursosListarAPI'),
   path('cursos/inserir/', CursoInserirAPI, name='CursoInserirAPI'),
   path('cursos/editar/<int:id>/', CursoEditarAPI, name="CursoEditarAPI"),
   path('cursos/remover/<int:id>/', CursoRemoverAPI, name="CursoRemoverAPI"),

   path('cursos/listar/pag/', CursosListarPaginatorAPI, name='CursosListarPaginatorAPI'),

]