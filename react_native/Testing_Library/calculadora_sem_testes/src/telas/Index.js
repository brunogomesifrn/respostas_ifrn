import { Text, View, Button, StyleSheet } from 'react-native';

export default ({navigation}) => {
    return(
      <View style={estilo.container}>

       <View style={estilo.cabecalho}>
        <Text style={estilo.texto_cabecalho}>Calculadora</Text>
       </View>

       <View style={estilo.menu}>

        <Button title="Calculadora do BG"
            onPress={() => {
            navigation.navigate("Calculadora")
            }} />
       </View>
        
      </View>
   )
  }

  const estilo = StyleSheet.create({
    container: {
        flexDirection: 'column',
        flex: 4,
        alignItems: 'center'
        //justifyContent: 'space-around',
    },
    cabecalho:{
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
    },
    texto_cabecalho:{
        fontWeight: 'bold',
        fontSize: 30
    },
    menu:{
        flex: 5,
        justifyContent: 'space-around',
    }
  });