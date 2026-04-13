import {View, Text} from 'react-native'

export function Titulos(props) {
    return(
        <View>
            <Text>{props.titulo}</Text>
            <Text>{props.subtitulo}</Text>
        </View>
    );
}