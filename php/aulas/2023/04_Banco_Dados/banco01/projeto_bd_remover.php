<?php
    $codigo = $_GET["codigo"];

    include "conexao.php";

    $sql = "DELETE FROM projeto 
    WHERE codigo=$codigo";

    $result = $conn->query($sql);

    if($result){
        $conn->close();
        header("Location: projetos.php");
        die();
    }

?>