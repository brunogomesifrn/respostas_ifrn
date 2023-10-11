<?php

$nome = $_POST["nome"];
$data = $_POST["data"];
$valor = $_POST["valor"];

include "conexao.php";

$sql = "INSERT INTO projeto 
(nome, data_inicio, valor)
VALUES ('$nome', '$data', $valor);";

$result = $conn->query($sql);
if($result){
    $conn->close();
    header("Location: projetos.php");
    die();
}


?>