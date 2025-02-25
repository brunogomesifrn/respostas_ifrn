import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';
import Index from './src/screens/Index';
import Areas from './src/screens/Areas';
import Area_Cadastrar from './src/screens/Area_Cadastrar';
import Area_Editar from './src/screens/Area_Editar';
const Stack = createNativeStackNavigator();

export default function App() {
  return (
  <NavigationContainer>
    <Stack.Navigator initialRouteName="Index">
        <Stack.Screen name="Index" component={Index} />
        <Stack.Screen name="Areas" component={Areas} />
        <Stack.Screen name="Area_Cadastrar" component={Area_Cadastrar} />
        <Stack.Screen name="Area_Editar" component={Area_Editar} />
    </Stack.Navigator>
  </NavigationContainer>
);
};