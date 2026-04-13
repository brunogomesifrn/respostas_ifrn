import {Text, StyleSheet, View, Image, Button} from 'react-native'
import { SafeAreaView } from 'react-native-safe-area-context';
import {useNavigation} from '@react-navigation/native';
import { Link } from '@react-navigation/native';

export default function App(){
    const navigation = useNavigation();
  return (
    <View>
      <Text>Olá Mundo</Text>
      <Text style={[
        estilo.texto, 
        {fontWeight: 'bold'}
        ]}>Texto2</Text>

        <Button
        title="Ir para a Tela Instituto"
        onPress={() => navigation.navigate('Instituto')} />

        <Link screen="Instituto">Ir para Instituto via Link</Link>

        <Button
        title="Ir para Noticia"
        onPress={
            () => navigation.navigate('Noticia')
        } />

        <Button
        title="Ir para Disciplina"
        onPress={() => 
            navigation.navigate('Disciplina',
            {
                nome: 'Des para Disp Móveis',
                ch: 4
            })
        }
        ></Button>

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
