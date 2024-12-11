<?php

$nome = $_POST["categoria"];

include "banco/conexao.php";

$conn = conectar();

$result = $conn->query("INSERT INTO categoria (nome) VALUES ('$nome')");

if($result){
    desconectar($conn);
    header("Location: categorias.php");
    die();
}else{

}

?>