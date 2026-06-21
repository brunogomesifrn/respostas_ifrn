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