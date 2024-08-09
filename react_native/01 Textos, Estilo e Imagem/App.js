import {Text, View, StyleSheet, Image} from 'react-native';

export default function App() {
  return (
    <View>
      {/* Aula de ReactNative :D */}
      <Text style={{marginTop: 100, color: 'green'}}>Olá Mundo!</Text>
      <Text style={estilo}>Primeira aula</Text>
      <Text>{1+5}</Text>
      <Text style={estilo_2.instituicao}>IFRN</Text>
      <Text style={estilo_2.disciplina}>Teste de Software</Text>
      <Image style={estilo_2.imagem} source={require('./images/ifcang.jpg')}/>
    </View>
  );
}

const estilo_2 = StyleSheet.create({
  imagem: {
    aspectRatio: 1,
    width: 5
  },  
  instituicao: {
    textAlign: 'right',
    color: 'gray'
  },
  disciplina: {
    fontStyle: 'italic'
  }
})

const estilo = {
  fontSize: 10, 
  color: 'red'
}