import {View, Text, Button, TextInput} from 'react-native'
import {useState} from 'react'

export default function App(){

    const [nome, alterarNome] = useState("Bruno")
    const [texto, alterarTexto] = useState("")

    return (
        <View>
            <Text>Tela de Estado</Text>
            <Text>{nome}</Text>
            <Button 
            title="Alterar Nome"
            onPress={()=>alterarNome("Novo Nome")}
            />

            <Text>Digite um texto:</Text>

            <TextInput 
            onChangeText={alterarTexto}/>

            <Button title="Alterar com campo" 
            onPress={()=>alterarNome(texto)}/>
        </View>
    );
}