import {Text, View, Button} from 'react-native'

export default function Index({navigation}){
    return (
        <View>
            <Text>Tela Inicial</Text>
            
            <Button
                title='Ir para Contato'
                onPress={ () => {
                    navigation.navigate("Contato");
                }}
                testID='b_contato'
            />
        </View>
    );
}