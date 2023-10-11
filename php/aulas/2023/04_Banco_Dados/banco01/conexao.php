<?php

$servidor = "localhost";
$usuario = "root";
$senha = "123";
$banco = "aula_01";

$conn = mysqli_connect($servidor, $usuario, $senha, $banco);

if($conn->connect_error){
    echo "Deu ruim!";
}else{
    //echo "Deu bom!";
}

//$conn->close();

?>