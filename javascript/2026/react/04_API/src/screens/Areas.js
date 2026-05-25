import {View, Text, FlatList, Button} from 'react-native';
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
    },[])


    return (
        <View>
            <Text>Áreas</Text>
            <FlatList
            data={areas}
            keyExtractor={(item) => item.id.toString()}
            renderItem={({item})=> (
                <View>
                    <Text>{item.id} - {item.nome}</Text>
                </View>
            )} />
        </View>
    )
}