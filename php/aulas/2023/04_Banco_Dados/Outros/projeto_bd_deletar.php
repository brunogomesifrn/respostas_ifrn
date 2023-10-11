<?php
$codigo = $_GET['codigo'];

include "conexao.php";

$sql = "DELETE FROM projeto WHERE codigo=$codigo";

if ($conn->query($sql)) {
    $conn->close();
    header("Location: projetos.php");
    die();
} else {
    echo "Error deleting record: " . $conn->error;
}

$conn->close();

?>