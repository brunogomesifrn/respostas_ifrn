import React, { useState } from 'react'
import { Text, View, StyleSheet, TouchableOpacity } from 'react-native';

export default ({navigation}) => {
    const [tela, alterarTela] = useState("");
    
    const zerar = () => {
        alterarTela("");
    }

    const operacao = (texto) => {
        alterarTela(tela+texto);
    }

    const resultado = () => {
        alterarTela(eval(tela));
    }

    return(
        <View style={estilo.container}>
            <View style={estilo.tela}>
                <Text style={estilo.conteudo} testID='tela'>{tela}</Text>
            </View>

            <View style={estilo.linha}>
                
                <TouchableOpacity  
                style={estilo.botao}
                onPress={zerar} >
                    <Text>Zerar</Text>
                </TouchableOpacity>

                <TouchableOpacity  
                style={estilo.botao}
                onPress={()=>{operacao("/")}} >
                    <Text>/</Text>
                </TouchableOpacity>

                <TouchableOpacity  
                style={estilo.botao}
                onPress={()=>{operacao("*")}} >
                    <Text>*</Text>
                </TouchableOpacity>

                <TouchableOpacity  
                style={estilo.botao}
                onPress={()=>{operacao("-")}} >
                    <Text>-</Text>
                </TouchableOpacity>
            </View>

            <View style={estilo.linha}>
                <TouchableOpacity  
                style={estilo.botao}
                onPress={()=>{operacao("7")}} >
                    <Text>7</Text>
                </TouchableOpacity>

                <TouchableOpacity  
                style={estilo.botao}
                onPress={()=>{operacao("8")}} >
                    <Text>8</Text>
                </TouchableOpacity>

                <TouchableOpacity  
                style={estilo.botao}
                onPress={()=>{operacao("9")}} >
                    <Text>9</Text>
                </TouchableOpacity>

                <TouchableOpacity  
                style={estilo.botao}
                onPress={()=>{operacao("+")}} >
                    <Text>+</Text>
                </TouchableOpacity>
            </View>

            <View style={estilo.linha}>
                <TouchableOpacity  
                style={estilo.botao}
                onPress={()=>{operacao("4")}} >
                    <Text>4</Text>
                </TouchableOpacity>

                <TouchableOpacity  
                style={estilo.botao}
                onPress={()=>{operacao("5")}} >
                    <Text>5</Text>
                </TouchableOpacity>

                <TouchableOpacity  
                style={estilo.botao}
                onPress={()=>{operacao("6")}} >
                    <Text>6</Text>
                </TouchableOpacity>

                <TouchableOpacity  
                style={estilo.botao}
                onPress={()=>{operacao("*")}} >
                    <Text>*</Text>
                </TouchableOpacity>
            </View>


            <View style={estilo.linha}>
                
                <TouchableOpacity  
                style={estilo.botao}
                onPress={()=>{operacao("1")}} >
                    <Text>1</Text>
                </TouchableOpacity>

                <TouchableOpacity  
                style={estilo.botao}
                onPress={()=>{operacao("2")}} >
                    <Text>2</Text>
                </TouchableOpacity>

                <TouchableOpacity  
                style={estilo.botao}
                onPress={()=>{operacao("3")}} >
                    <Text>3</Text>
                </TouchableOpacity>

                <TouchableOpacity  
                style={estilo.botao}
                onPress={()=>{operacao(",")}} >
                    <Text>.</Text>
                </TouchableOpacity>
            </View>

            <View style={estilo.linha}>
            <TouchableOpacity  
                style={estilo.botao}
                onPress={()=>{operacao("0")}} >
                    <Text>0</Text>
                </TouchableOpacity>

                <TouchableOpacity  
                style={estilo.botao}
                onPress={()=>{operacao("(")}} >
                    <Text>(</Text>
                </TouchableOpacity>

                <TouchableOpacity  
                style={estilo.botao}
                onPress={()=>{operacao(")")}} >
                    <Text>)</Text>
                </TouchableOpacity>

                <TouchableOpacity  
                style={estilo.botao}
                onPress={resultado} >
                    <Text>=</Text>
                </TouchableOpacity>
            </View>

            <View style={estilo.linha}>
            <TouchableOpacity  
                style={[estilo.botao, estilo.voltar]}
                onPress={() => {
                    navigation.navigate("Index")
                  }} >
                    <Text>VOLTAR</Text>
                </TouchableOpacity>
            </View>

</View>
   )
  }

  const estilo = StyleSheet.create({
    container: {
        flexDirection: 'column',
        flex: 1,
        alignItems: 'center',
    },
    tela:{
        width: '100%',
        flex: 1,
        alignItems: 'flex-start',
        justifyContent: 'center',
        backgroundColor: 'black',
        //borderTopWidth: 2,
        //borderBottomWidth: 2,
        paddingLeft: 10,
    },
    conteudo:{
        fontSize: 20,
        color: 'white',
        fontWeight: 'bold'
    },
    linha:{
        flex: 1,
        flexDirection: 'row',
        justifyContent: 'space-around',
        width: '100%',
        height: '100%',
        margin: 2,

    },
    botao:{
        backgroundColor: 'beige',
        margin: 2,
        height: '100%',
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
        borderWidth: 2,
    },
    voltar:{
        backgroundColor: 'wheat',
    }
  });