import React, { useEffect, useState} from "react";
import { View, Text, Button} from "react-native";

import AsyncStorage from "@react-native-async-storage/async-storage";

const API_URL = "http://192.168.1.146:8000/api/v1";

export default function Perfil({ navigation }) {

  const [usuario, setUsuario] = useState(null);

  async function carregarPerfil() {

    try {

      const token =
        await AsyncStorage.getItem(
          "access"
        );

      const response =
        await fetch(
          `${API_URL}/perfil/`,
          {
            headers: {
              Authorization:
                `Bearer ${token}`
            }
          }
        );
      const data = await response.json();
      if (!response.ok) {
        navigation.replace(
          "Login"
        );
        return;
      }
      setUsuario(data);
    } catch {
      navigation.replace("Login");
    }
  }

  async function logout() {

    await AsyncStorage.removeItem("access");
    await AsyncStorage.removeItem("refresh");

    navigation.replace(
      "Login"
    );
  }

  useEffect(() => {
    carregarPerfil();
  }, []);

  /*
  if (!usuario) {
    return (
      <Text>
        Carregando...
      </Text>
    );
  }
*/
  return (

    <View style={{ padding: 20 }}>

      <Text>
        Nome: {usuario?.nome_completo}
      </Text>

      <Text>
        Email: {usuario?.email}
      </Text>

      <Text>
        CPF: {usuario?.cpf}
      </Text>

      <Text>
        Matrícula: {usuario?.matricula}
      </Text>

      <Button
        title="Sair"
        onPress={logout}
      />

    </View>
  );
}