import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';
import Index from './src/telas/Index';
import Calculadora from './src/telas/Calculadora';

const Stack = createNativeStackNavigator();

export default function App() {
  return (
  <NavigationContainer>
    <Stack.Navigator initialRouteName="Index">
        <Stack.Screen name="Index" component={Index} />
        <Stack.Screen name="Calculadora" component={Calculadora} />
    </Stack.Navigator>
  </NavigationContainer>
);
};