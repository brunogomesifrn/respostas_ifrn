import {View, Text} from 'react-native'

export default function Disciplina({route, navigation}){
    const {nome, ch} = route.params;
    return (
        <View>
            <Text>Nome: {nome}</Text>
            <Text>CH: {ch}</Text>
        </View>
    );
}