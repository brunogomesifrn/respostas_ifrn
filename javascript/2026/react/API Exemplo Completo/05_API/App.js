import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

import Index from "./src/screens/Index";
import Cursos from "./src/screens/Cursos";
import Areas from "./src/screens/Areas";
import Publicos from "./src/screens/Publicos";
import Login from "./src/screens/Login";
import Cadastro from "./src/screens/Cadastro";
import Perfil from "./src/screens/Perfil";

const Stack = createNativeStackNavigator();

export default function App() {
  return (
  <NavigationContainer>
    <Stack.Navigator initialRouteName="Index">
      <Stack.Screen name="Index" component={Index} />
      <Stack.Screen name="Cursos" component={Cursos} />
      <Stack.Screen name="Areas" component={Areas} />
      <Stack.Screen name="Publicos" component={Publicos} />
      <Stack.Screen name="Login" component={Login} />
      <Stack.Screen name="Cadastro" component={Cadastro} />
      <Stack.Screen name="Perfil" component={Perfil} />
    </Stack.Navigator>
  </NavigationContainer>
  );
}