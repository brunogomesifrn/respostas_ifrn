import { StyleSheet, Text, View, Image, Button } from 'react-native';

export default function App() {
  return (
    <View>
      <Text>Olá Mundo!</Text>
      <Text>Bruno Gomes</Text>
      <Text>{5+4}</Text>
      {/*<Text>{alert("Oláááá")}</Text>*/}
      <Text style={{color: 'brown', 
           textAlign: 'center'}}>IFRN</Text>
        <Text style={estilo_1}>Interface</Text>
        <Text style={estilo_2.curso}>TSI</Text>
        <Text style={estilo_2.materia}>React</Text>
        <Image style={estilo_2.imagem} source={require("./assets/react.png")} />
        <Button title="Pressionse" onPress={()=>alert("Olá")} />
    </View>
  );
}

const estilo_1 = {
  textAlign: "right",
  fontStyle: "italic"
}

const estilo_2 = StyleSheet.create({
  curso: {
    textAlign: "center",
    color: "#006400",
    fontWeight: "800"
  },
  materia: {
    letterSpacing: 4,
    fontSize: 10
  },
  imagem: {
    width: 10
  }
});