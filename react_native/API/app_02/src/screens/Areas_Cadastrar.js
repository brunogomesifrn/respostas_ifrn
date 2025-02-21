import { View, Text, TextInput, Button} from 'react-native'
import { useState} from 'react'
import api from '../config/Api'

export default function app({navigation}){
    const [nome, alterarNome] = useState("");

    const cadastrar = () => {
        
        const area = {
            "nome": nome
        }

        api.put("/areas/adicionar/", area)
        .then((response)=>{
            navigation.navigate("Areas");
        })
        .catch((err) => {

        })

    }

    return (
        <View>
            <Text>Tela de Cadastro</Text>
            <Text>Digite o nome:</Text>
            <TextInput
            onChangeText={alterarNome}
            />
            <Button
            title="Cadastrar"
            onPress={cadastrar} />
        </View>
    );
}