import { Text, View, Button, StyleSheet, TextInput} from 'react-native';
import React, { useState } from 'react'
import api from "../config/Api"


export default function App({navigation}) {
    
    const [text, onChangeText] = useState();

  const cadastrar = async () => {

    const area = {
        "nome": text
    }

    await api.put("/areas/adicionar/", area)
      .then((response) => { 
        navigation.navigate("Areas")
      }).catch((err) => { // Acessar o catch quando a API retornar status erro
        if (err.response) { // Acessa o IF quando a API retornar erro
          Alert.alert("Ops", err.response.data.mensagem);
        } else { // Acessa o ELSE quando a API não responder
          Alert.alert("Ops", "Erro: Tente mais tarde!");
        }
      });
  }

    return (
        <View style={estilo.tela}>
            <Text>CADASTRO</Text>
            
            <Text>Nome:</Text>

            <TextInput 
            onChangeText={onChangeText}
             />
            
            <Button title="Cadastrar"
            onPress={() => {
                cadastrar()
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
    
