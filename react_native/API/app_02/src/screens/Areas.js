import {View, Text, FlatList} from 'react-native'
import { useEffect, useState } from 'react'
import api from '../config/Api'

export default function App({navigation}){

    const [areas, listarAreas] = useState([])

    const getAreas = async () => {
        
        await api.get("/areas/listar/")
        .then((response)=>{
            listarAreas(response.data);
        }).catch((err)=>{

        })
    }

    useEffect(() => {
        getAreas();
    },[]);

    return (
        <View>
            <Text>ÁREAS</Text>
            <FlatList 
            data={areas} 
            keyExtractor={({id})=>id}
            renderItem={({item})=>(
                <Text>Nome: {item.nome}</Text>
            )}
            />
        </View>
    );
}