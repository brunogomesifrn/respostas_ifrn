from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .models import Areas, Publicos, Cursos
from .serializers import AreaSerializer, PublicoSerializer, CursoSerializer
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .serializers import UsuarioCadastroSerializer

# Autenticação
@api_view(['POST'])
def LoginAPI(request):

    username = request.data.get('username')
    password = request.data.get('password')

    usuario = authenticate(
        username=username,
        password=password
    )

    if usuario is None:
        return Response(
            {'erro': 'Usuário ou senha inválidos'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    refresh = RefreshToken.for_user(usuario)

    return Response({
        'access': str(refresh.access_token),
        'refresh': str(refresh),
        'usuario': {
            'id': usuario.id,
            'username': usuario.username,
            'nome_completo': usuario.nome_completo,
            'email': usuario.email
        }
    })

# Retornar dados de Usuário
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def PerfilAPI(request):
    usuario = request.user
    return Response({
        'id': usuario.id,
        'username': usuario.username,
        'nome_completo': usuario.nome_completo,
        'email': usuario.email,
        'cpf': usuario.cpf,
        'matricula': usuario.matricula
    })

# Cadastro de Usuário
@api_view(['POST'])
def UsuarioCadastrarAPI(request):
    serializer = UsuarioCadastroSerializer(
        data=request.data
    )
    if serializer.is_valid():
        usuario = serializer.save()
        return Response(
            {
                'mensagem': 'Usuário cadastrado com sucesso',
                'id': usuario.id,
                'username': usuario.username
            },
            status=status.HTTP_201_CREATED
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AreasListarAPI(request):
    lista_areas = Areas.objects.all()
    serializer = AreaSerializer(lista_areas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def AreaInserirAPI(request):
    serializer = AreaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, 
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors, 
                    status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def AreaEditarAPI(request, id):
    #area = Areas.objects.get(pk=id)
    area = get_object_or_404(Areas, pk=id)
    serializer = AreaSerializer(data=request.data, instance=area)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, 
                        status=status.HTTP_200_OK)
    return Response(serializer.errors, 
                    status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def AreaRemoverAPI(request, id):
    area = get_object_or_404(Areas, pk=id)
    area.delete()
    return Response(
        status=status.HTTP_204_NO_CONTENT
    )




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def PublicosListarAPI(request):
    lista_publicos = Publicos.objects.all()
    serializer = PublicoSerializer(lista_publicos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def PublicoInserirAPI(request):
    serializer = PublicoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, 
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors, 
                    status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def PublicoEditarAPI(request, id):
    publico = get_object_or_404(Publicos, pk=id)
    serializer = PublicoSerializer(data=request.data, instance=publico)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, 
                        status=status.HTTP_200_OK)
    return Response(serializer.errors, 
                    status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def PublicoRemoverAPI(request, id):
    publico = get_object_or_404(Publicos, pk=id)
    publico.delete()
    return Response(
        status=status.HTTP_204_NO_CONTENT
    )





@api_view(['GET'])
@permission_classes([IsAuthenticated])
def CursosListarAPI(request):
    lista_cursos = Cursos.objects.all()
    serializer = CursoSerializer(lista_cursos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CursoInserirAPI(request):
    serializer = CursoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, 
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors, 
                    status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def CursoEditarAPI(request, id):
    curso = get_object_or_404(Cursos, pk=id)
    serializer = CursoSerializer(data=request.data, instance=curso)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, 
                        status=status.HTTP_200_OK)
    return Response(serializer.errors, 
                    status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def CursoRemoverAPI(request, id):
    curso = get_object_or_404(Cursos, pk=id)
    curso.delete()
    return Response(
        status=status.HTTP_204_NO_CONTENT
    )