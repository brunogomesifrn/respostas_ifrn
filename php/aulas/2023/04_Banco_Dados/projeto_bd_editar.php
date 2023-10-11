<?php

$codigo = $_POST['codigo'];
$nome = $_POST['nome'];
$data_inicio = $_POST['data_inicio'];
$valor = $_POST['valor'];

include "conexao.php";

// Inserir normalmente
$sql = "UPDATE projeto SET
 nome='$nome',
 data_inicio ='$data_inicio',
 valor=$valor
 WHERE codigo=$codigo";

if ($conn->query($sql) === TRUE) {
  $conn->close();
  header("Location: projetos.php");
  die();
} else {
  echo "<p>Erro: " . $sql . "<br />" . $conn->error."</p>";
  $conn->close();
}



?>