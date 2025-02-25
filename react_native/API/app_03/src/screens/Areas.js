import React, {useEffect, useState} from 'react';
import {ActivityIndicator, FlatList, Text, View, StyleSheet, Button} from 'react-native';
import api from "../config/Api";

export default function App({navigation}) {
  const [areas, setAreas] = useState([]);

  const getAreas = async () => {
    await api.get("/areas/?format=json")
      .then((response) => { 
        setAreas(response.data);
      }).catch((err) => { 
        if (err.response) { 
          Alert.alert("Erro", err.response.data.mensagem);
        } else { 
          Alert.alert("Erro", "Erro: Tente mais tarde!");
        }
      });
  }

  const removerArea = async (id) => {
    rota = "/areas/remover/"+id+"/"
    await api.delete(rota)
      .then((response) => { 
        getAreas();
      }).catch((err) => { 
        if (err.response) { 
          Alert.alert("Erro", err.response.data.mensagem);
        } else { 
          Alert.alert("Erro", "Erro: Tente mais tarde!");
        }
      });
  }

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

