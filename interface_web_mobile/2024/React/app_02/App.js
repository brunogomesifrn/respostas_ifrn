import { NavigationContainer } 
from "@react-navigation/native";
import { createNativeStackNavigator } 
from "@react-navigation/native-stack";

import Index from './src/screens/Index';
import Perfil from './src/screens/Perfil';
import Estado from './src/screens/Estado';
import Areas from './src/screens/Areas';

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator intialRouteName="Index">
        <Stack.Screen name="Index" component={Index} />
        <Stack.Screen name="Perfil" component={Perfil} />
        <Stack.Screen name="Estado" component={Estado} />
        <Stack.Screen name="Areas" component={Areas} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
