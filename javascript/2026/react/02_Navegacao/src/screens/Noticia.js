import {View, Text, StyleSheet} from 'react-native'
import { Titulos } from '../components/Titulos';
import estilo from '../styles/Estilo';

export default () => {
    return (
        <View>
            <Titulos 
            titulo="Texto do Título"
            subtitulo="Texto do Subtitulo">
            </Titulos>
            <Text style={estilo.noticia}>Notícia</Text>
        </View>
    );
}

