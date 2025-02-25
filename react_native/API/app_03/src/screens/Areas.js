import React, {useEffect, useState} from 'react';
import {ActivityIndicator, FlatList, Text, View, StyleSheet, Button} from 'react-native';
import api from "../config/Api";

export default function App({navigation}) {
  const [areas, setAreas] = useState([]);

  // Função para recuperar os usuários
  const getAreas = async () => {
    // Requisição para a API indicando a rota
    await api.get("/areas/?format=json")
      .then((response) => { // Acessar o then quando a API retornar status sucesso
        //console.log(response.data.users);
        // Atribuir os dados retornado da API
        setAreas(response.data);
      }).catch((err) => { // Acessar o catch quando a API retornar status erro
        if (err.response) { // Acessa o IF quando a API retornar erro
          Alert.alert("Ops", err.response.data.mensagem);
        } else { // Acessa o ELSE quando a API não responder
          Alert.alert("Ops", "Erro: Tente mais tarde!");
        }
      });
  }

  const removerArea = async (id) => {
    // Requisição para a API indicando a rota
    rota = "/areas/remover/"+id+"/"
    
    await api.delete(rota)
      .then((response) => { 
        getAreas();
      }).catch((err) => { // Acessar o catch quando a API retornar status erro
        if (err.response) { // Acessa o IF quando a API retornar erro
          Alert.alert("Ops", err.response.data.mensagem);
        } else { // Acessa o ELSE quando a API não responder
          Alert.alert("Ops", "Erro: Tente mais tarde!");
        }
      });
  }

  // Executar quando o usuário carregar a tela e chamar a função getUsers
  useEffect(() => {
    getAreas();
  }, []);

  return (
    <View style={estilo.tela}>
      <Button title="Cadastrar"
                    onPress={() => {
                  navigation.navigate("Area_Cadastrar")
                    }} />
           
        <FlatList
          data={areas}
          keyExtractor={({id}) => id}
          renderItem={({item}) => (
            <Text>
              {item.nome}
              |
              <Button title="Editar"
                    onPress={() => {
                      navigation.navigate("Area_Editar", {id: item.id, nome:item.nome})
                    }} />
              |
              <Button title="Remover"
                    onPress={() => {
                      removerArea(item.id)
                    }} />
            </Text>
          )}
        />

        
    </View>
  );
};


const estilo = StyleSheet.create({
  tela: {
    flex: 1,
    padding: 24
  }

});

