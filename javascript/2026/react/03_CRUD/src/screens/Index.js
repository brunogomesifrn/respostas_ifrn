import { View, Text, Button } from 'react-native';

export default function Index({navigation}){
   
    return (
        <View>
            <Text>Tela Inicial</Text>
            <Button 
            title="Cursos"
            onPress={()=>navigation.navigate('Cursos')}
            />
                
            


        </View>
    );
}