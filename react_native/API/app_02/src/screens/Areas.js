import {View, Text, FlatList, Button} from 'react-native'
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

            <Button 
            title="Cadastrar Área"
            onPress={()=>navigation.navigate("Areas_Cadastrar")} 
            />

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