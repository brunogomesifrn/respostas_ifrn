Me ajude a elaborar o arquivo Curso.js em React Native, que fará um CRUD de Cursos através de uma API criada em Django, de forma mais simples possível. Vou lhe passar os códigos de 2 arquivos .js já feitos para Areas e Publicos, e depois o código do projeto Django.

# React Native

## Area.js

import {View, Text, FlatList, TextInput, Button} from 'react-native';
import { useState, useEffect} from 'react';

export default function Areas(){
    const [areas, setArea] = useState([]);
    const [id, setId] = useState('');
    const [nome, setNome] = useState('');

    const API = 'http://192.168.1.146:8000/api/v1/areas/';

    async function listar(){
        try{
            const resposta = await fetch(API+'listar/');
            const dados = await resposta.json();
            setArea(dados);
        }catch(erro){
            console.log(erro);
        }
    }

    useEffect(()=>{
        listar();
    },[]);

    async function adicionar(){
        const nova_area = {
            "nome": nome
        }

        await fetch(API+'inserir/',{
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(nova_area)
        });
        listar();
        setId("");
        setNome("");
    }

    function editar(item){
        setNome(item.nome);
        setId(item.id);
    }

    async function atualizar(){
        const area_editar = {
            "nome": nome
        }

        await fetch(API+"editar/"+id+"/", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(area_editar)
        });
        listar();
        setId("");
        setNome("");
    }

    async function remover(id_remover) {
        await fetch(API + 'remover/' + id_remover + '/', {
            method: 'DELETE'
        });
        listar();
        setId('');
        setNome('');
    }


    return (
        <View>
            <Text>Áreas</Text>

            <Text>ID:</Text>
            <TextInput 
            value={id}
            onChangeText={setId} />

            <Text>Nome:</Text>
            <TextInput 
            value={nome}
            onChangeText={setNome} />

            <Button 
            title="Adicionar"
            onPress={adicionar} />

            <Button
            title="Atualizar"
            onPress={atualizar} />


            <FlatList
            data={areas}
            keyExtractor={(item) => item.id.toString()}
            renderItem={({item})=> (
                <View>
                    <Text>
                        {item.id} - {item.nome}
                        <Button 
                            title="EDITAR"
                            onPress={()=> {
                                editar(item)
                            }} 
                        />
                         <Button
                            title="Remover"
                            onPress={() => {
                                remover(item.id)
                            }}
                            />
                        </Text>
                </View>
            )} />
        </View>
    )
}

## Publico.js
import {View, Text, FlatList, TextInput, Button} from 'react-native';
import { useState, useEffect} from 'react';

export default function Publicos(){
    const [publicos, setPublico] = useState([]);
    const [id, setId] = useState('');
    const [nome, setNome] = useState('');

    const API = 'http://192.168.1.146:8000/api/v1/publicos/';

    async function listar(){
        try{
            const resposta = await fetch(API+'listar/');
            const dados = await resposta.json();
            setPublico(dados);
        }catch(erro){
            console.log(erro);
        }
    }

    useEffect(()=>{
        listar();
    },[]);

    async function adicionar(){
        const novo_publico = {
            "nome": nome
        }

        await fetch(API+'inserir/',{
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(novo_publico)
        });
        listar();
        setId("");
        setNome("");
    }

    function editar(item){
        setNome(item.nome);
        setId(item.id);
    }

    async function atualizar(){
        const publico_editar = {
            "nome": nome
        }

        await fetch(API+"editar/"+id+"/", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(publico_editar)
        });
        listar();
        setId("");
        setNome("");
    }

    async function remover(id_remover) {
        await fetch(API + 'remover/' + id_remover + '/', {
            method: 'DELETE'
        });
        listar();
        setId('');
        setNome('');
    }


    return (
        <View>
            <Text>Públicos</Text>

            <Text>ID:</Text>
            <TextInput 
            value={id}
            onChangeText={setId} />

            <Text>Nome:</Text>
            <TextInput 
            value={nome}
            onChangeText={setNome} />

            <Button 
            title="Adicionar"
            onPress={adicionar} />

            <Button
            title="Atualizar"
            onPress={atualizar} />


            <FlatList
            data={publicos}
            keyExtractor={(item) => item.id.toString()}
            renderItem={({item})=> (
                <View>
                    <Text>
                        {item.id} - {item.nome}
                        <Button 
                            title="EDITAR"
                            onPress={()=> {
                                editar(item)
                            }} 
                        />
                         <Button
                            title="Remover"
                            onPress={() => {
                                remover(item.id)
                            }}
                            />
                        </Text>
                </View>
            )} />
        </View>
    )
}


# Django

## Mmodel.py
from django.db import models

class Areas(models.Model):
    nome = models.CharField("Nome", max_length=100)

class Publicos(models.Model):
	nome = models.CharField('Nome', max_length=100)

class Cursos(models.Model):
	titulo = models.CharField('Nome', max_length=150)
	resumo = models.TextField('Resumo', max_length=500)
	carga_horaria = models.IntegerField('Carga Horária')
	data_inicio = models.DateField('Data de Início')
	vagas = models.IntegerField('Vagas')
	area = models.ForeignKey(Areas, on_delete=models.PROTECT)
	publicos = models.ManyToManyField(Publicos)
	foto = models.ImageField('Foto', upload_to='media')

## serializers.py
from rest_framework import serializers
from .models import Areas, Publicos, Cursos

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areas
        fields = ['id', 'nome']

class PublicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicos
        fields = ['id', 'nome']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = ['titulo', 'descricao', 'autor', 'vagas', 'area', 'publicos']

## views.py

from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .models import Areas, Publicos, Cursos
from .serializers import AreaSerializer, PublicoSerializer, CursoSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def AreasListarAPI(request):
    lista_areas = Areas.objects.all()
    serializer = AreaSerializer(lista_areas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def AreaInserirAPI(request):
    serializer = AreaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, 
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors, 
                    status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
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
def AreaRemoverAPI(request, id):
    area = get_object_or_404(Areas, pk=id)
    area.delete()
    return Response(
        status=status.HTTP_204_NO_CONTENT
    )




@api_view(['GET'])
def PublicosListarAPI(request):
    lista_publicos = Publicos.objects.all()
    serializer = PublicoSerializer(lista_publicos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def PublicoInserirAPI(request):
    serializer = PublicoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, 
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors, 
                    status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
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
def PublicoRemoverAPI(request, id):
    publico = get_object_or_404(Publicos, pk=id)
    publico.delete()
    return Response(
        status=status.HTTP_204_NO_CONTENT
    )





@api_view(['GET'])
def CursosListarAPI(request):
    lista_cursos = Cursos.objects.all()
    serializer = CursoSerializer(lista_cursos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CursoInserirAPI(request):
    serializer = CursoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, 
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors, 
                    status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
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
def CursoRemoverAPI(request, id):
    curso = get_object_or_404(Cursos, pk=id)
    curso.delete()
    return Response(
        status=status.HTTP_204_NO_CONTENT
    )

## urls.py

from django.urls import path
from .views import *

urlpatterns = [
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

]
