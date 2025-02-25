import { Text, View, Button, StyleSheet, TextInput} from 'react-native';
import React, { useState } from 'react'
import api from "../config/Api"


export default function App({route, navigation}) {
    
    const [text, onChangeText] = useState();

  const editar = async () => {

    const area = {
        "id": route.params.id,
        "nome": text
    }

    rota = "/areas/atualizar/"+route.params.id+"/";
  
    await api.post(rota, area)
      .then((response) => { 
        navigation.navigate("Areas")
      }).catch((err) => { 
        if (err.response) { 
          Alert.alert("Erro", err.response.data.mensagem);
        } else {
          Alert.alert("Erro", "Erro: Tente mais tarde!");
        }
      });
  }
  
    return (
        <View style={estilo.tela}>
            <Text>EDIÇÃO</Text>
            
            <Text>Nome: {route.params.nome}</Text>
            <Text>Novo Nome: </Text>
            <TextInput 
            onChangeText={onChangeText}
            
             />
            
            <Button title="Editar"
            onPress={() => {
                editar()
            }} />
        </View>
    );
};


const estilo = StyleSheet.create({
    tela: {
        flex: 1,
        padding: 20
    }
})
    
