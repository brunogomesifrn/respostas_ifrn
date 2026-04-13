import {View, Text, Button} from 'react-native'

export default function Instituto({navigation}){
    return (
        <View>
            <Text>Tela Instituicao</Text>
            <Button
            title="Voltar para Index"
            onPress={() => navigation.navigate('Index')}
            />
        </View>
    );
}