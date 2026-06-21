import React, { useState } from "react";
import { View, TextInput, Button, Alert } from "react-native";

import AsyncStorage from "@react-native-async-storage/async-storage";

const API_URL = "http://192.168.1.146:8000/api/v1";

export default function Login({ navigation }) {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  async function login() {

    try {

      const response = await fetch(API_URL+'/login/',
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            username,
            password
          })
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error();
      }

      await AsyncStorage.setItem(
        "access",
        data.access
      );

      await AsyncStorage.setItem(
        "refresh",
        data.refresh
      );

      navigation.replace("Perfil");

    } catch {

      Alert.alert(
        "Erro",
        "Usuário ou senha inválidos"
      );

    }
  }

  return (
    <View style={{ padding: 20 }}>

      <TextInput
        placeholder="Usuário"
        value={username}
        onChangeText={setUsername}
      />

      <TextInput
        placeholder="Senha"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />

      <Button
        title="Entrar"
        onPress={login}
      />

      <Button
        title="Cadastrar"
        onPress={() => navigation.navigate("Cadastro")}
      />

    </View>
  );
}