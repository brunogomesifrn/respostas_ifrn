<?php

$categoria = $_POST["categoria"];
$id = $_POST["id"];

include "banco/conexao.php";

$conn = conectar();

$sql = "UPDATE categoria SET nome='$categoria' WHERE id=$id";

$result = $conn->query($sql);

if($result){
    desconectar($conn);
    header("Location: categorias.php");
    die();
}else{
    echo "Deu errado!";
}





?>