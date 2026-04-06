import {View, Text, StyleSheet} from 'react-native'

/*
Esta é a função básica
Precisa ser exportada com o default
Pode ser nomeada, sem nome e arrow function
*/
export default function App(){
  return (
    <View style={estilo_2.tela}>
      {/*
      View e Text são componentes
      da própria biblioteca React Native
       */}
      <Text>Olá Mundo!</Text>
      <Text style={{color: 'red'}}>Olá Mundo 2!</Text>
      <Text style={estilo_1}>IFRN</Text>
      <Text style={estilo_2.texto}>TSI</Text>
    </View>
  );
}

const estilo_1 = {
  color: 'blue',
  fontSize: 20
}

const estilo_2 = StyleSheet.create({
  tela: {
    backgroundColor: 'yellow',
    flex: 1
  },
  texto: {
    fontWeight: 'bold',
    color: 'red'
  }
})