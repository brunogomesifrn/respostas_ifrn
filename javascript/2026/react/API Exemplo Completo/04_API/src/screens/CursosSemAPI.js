import { useState } from 'react';
import {View, Text, TextInput, Button, FlatList} from 'react-native'

export default function Cursos(){
    const [cursos, setCursos] = useState([]);
    const [id, setId] = useState('');
    const [titulo, setTitulo] = useState('');
    const [vagas, setVagas] = useState('');

    function adicionar(){
        let novo_curso = {
            'id': id,
            'titulo': titulo,
            'vagas': vagas
        }

        setCursos([...cursos, novo_curso]);
        setId('');
        setTitulo('');
        setVagas('');
    }

    function editar(item){
        setId(item.id);
        setTitulo(item.titulo);
        setVagas(item.vagas);
    }

    function atualizar(){
        let nova_lista = [];
        for(let i=0; i<cursos.length; i++){
            if(cursos[i].id == id){
                nova_lista[i] = {
                    'id': id,
                    'titulo': titulo,
                    'vagas': vagas
                }
            }else{
                nova_lista[i] = cursos[i];
                
            }
        }
        setCursos(nova_lista);
        setId('');
        setTitulo('');
        setVagas('');
    }

    function remover(id_remover){
        let nova_lista = []
        for(let i=0; i<cursos.length; i++){
            if(cursos[i].id != id_remover){
                nova_lista[i] = cursos[i];
            }
        }
        setCursos(nova_lista);
        setId('');
        setTitulo('');
        setVagas('');
    }

    return (
    <View>
        <Text>Cursos</Text>
        
        <Text>ID:</Text>
        <TextInput 
        value={id}
        onChangeText={setId}
        />

        <Text>Título:</Text>
        <TextInput 
        value={titulo}
        onChangeText={setTitulo}/>

        <Text>Vagas:</Text>
        <TextInput 
        value={vagas}
        onChangeText={setVagas}/>

        <Button title="Adicionar" 
        onPress={adicionar}/>
        
        <Button title="Atualizar" 
        onPress={atualizar}/>

        <FlatList 
        data={cursos}
        keyExtractor={(item)=>item.id}
        renderItem={({item})=>(
            <View>
                <Text>
                    {item.id},{item.titulo},{item.vagas}
                    <Button title="Editar" 
                    onPress={()=>{editar(item)}}/>
                    <Button title="Remover" 
                    onPress={() => {remover(item.id)}} />
                </Text>
            </View>
        )}
        />
    </View>
    );
}