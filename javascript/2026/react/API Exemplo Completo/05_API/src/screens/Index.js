import { View, Text, Button } from 'react-native';

export default function Index({navigation}){
   
    return (
        <View>
            <Text>Tela Inicial</Text>
            <Button 
            title="Cursos"
            onPress={()=>navigation.navigate('Cursos')}
            />
            <Button 
            title="Areas"
            onPress={()=>navigation.navigate('Areas')}
            />

            <Button 
            title="Publicos"
            onPress={()=>navigation.navigate('Publicos')}
            />

            <Button 
            title="Login"
            onPress={()=>navigation.navigate('Login')}
            />

            <Button 
            title="Perfil"
            onPress={()=>navigation.navigate('Perfil')}
            />
                
            


        </View>
    );
}