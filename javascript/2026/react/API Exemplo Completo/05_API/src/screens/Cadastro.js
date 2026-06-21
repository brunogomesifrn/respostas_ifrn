import React, { useState } from "react";

import { View, TextInput, Button, Alert} from "react-native";

const API_URL = "http://192.168.1.146:8000/api/v1";

export default function Cadastro({ navigation }) {

  const [username, setUsername] = useState("");
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [cpf, setCpf] = useState("");
  const [matricula, setMatricula] = useState("");
  const [password, setPassword] = useState("");

  async function cadastrar() {

    try {

      const response = await fetch(API_URL+'/cadastrar/',
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            username,
            nome_completo: nome,
            email,
            cpf,
            matricula,
            password
          })
        }
      );

      const data = await response.json();

      if (!response.ok) {

        Alert.alert(
          "Erro",
          JSON.stringify(data)
        );

        return;
      }

      Alert.alert(
        "Sucesso",
        "Usuário cadastrado."
      );

      navigation.goBack();

    } catch {

      Alert.alert(
        "Erro",
        "Falha ao conectar à API."
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
        placeholder="Nome Completo"
        value={nome}
        onChangeText={setNome}
      />

      <TextInput
        placeholder="E-mail"
        value={email}
        onChangeText={setEmail}
      />

      <TextInput
        placeholder="CPF"
        value={cpf}
        onChangeText={setCpf}
      />

      <TextInput
        placeholder="Matrícula"
        value={matricula}
        onChangeText={setMatricula}
      />

      <TextInput
        placeholder="Senha"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />

      <Button
        title="Cadastrar"
        onPress={cadastrar}
      />

    </View>
  );
}