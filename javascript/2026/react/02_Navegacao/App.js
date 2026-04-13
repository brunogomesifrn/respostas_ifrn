import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import Index from './src/screens/Index';
import Instituto from './src/screens/Instituto';
import Noticia from './src/screens/Noticia';
import Disciplina from './src/screens/Disciplina';

const Stack = createNativeStackNavigator();

export default function App(){
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName='Index'>
        <Stack.Screen name="Index" component={Index} />
        <Stack.Screen name="Instituto" component={Instituto} />
        <Stack.Screen name="Noticia" component={Noticia} />
        <Stack.Screen name="Disciplina" component={Disciplina} />
    </Stack.Navigator>
    </NavigationContainer>
  );
}