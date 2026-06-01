import {View, Text, FlatList, TextInput, Button} from 'react-native';
import { useState, useEffect} from 'react';

export default function Areas(){
    const [areas, setArea] = useState([]);
    const [id, setId] = useState('');
    const [nome, setNome] = useState('');

    const API = 'http://10.41.1.179:8000/api/v1/areas/';

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
                        }} />
                        </Text>
                </View>
            )} />
        </View>
    )
}