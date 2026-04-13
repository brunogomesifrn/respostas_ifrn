import {Text, StyleSheet, View, Image} from 'react-native'
import { SafeAreaView } from 'react-native-safe-area-context';

export default function App(){
  return (
    <View>
      <Text>Olá Mundo</Text>
      <Text style={[
        estilo.texto, 
        {fontWeight: 'bold'}
        ]}>Texto2</Text>
    <Image source={require('../../assets/ifrn.jpg')} />
    </View>
  );
}

const estilo = StyleSheet.create({
  texto: {
    color: 'red',
    fontSize: 20
  }
});
