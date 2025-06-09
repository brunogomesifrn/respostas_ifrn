import {Text, View, Button} from 'react-native'

export default function Contato({navigation}){
    return (
        <View>
            <Text>Tela de Contato</Text>
            <Text>E-mail: bruno.gomes@ifrn.edu.br</Text>
            <Button
                title='Ir para Index'
                onPress={ () => {
                    navigation.navigate("Index");
                }}
                />
        </View>
    );
}