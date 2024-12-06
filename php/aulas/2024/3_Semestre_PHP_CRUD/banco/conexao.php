<?php

function conectar(){
    $servidor = "localhost";
    $usuario = "root";
    $senha = "123";
    $banco = "aula_jogo_02";

    $conn = new mysqli($servidor, $usuario, $senha, $banco);
    
    return $conn;
}


function desconectar($conn){
    $conn->close();
}


?>