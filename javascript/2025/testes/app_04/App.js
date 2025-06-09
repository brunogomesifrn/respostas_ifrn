import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import Index from "./src/screens/Index";
import Contato from "./src/screens/Contato";

const Stack = createNativeStackNavigator();

export default function App(){
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Index">
        <Stack.Screen name="Index" component={Index} />
        <Stack.Screen name="Contato" component={Contato} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}