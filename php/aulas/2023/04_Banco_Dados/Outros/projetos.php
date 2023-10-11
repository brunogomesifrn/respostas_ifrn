<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>PROJETOS</h1>
    <a href="projeto_cadastrar.php">Cadastrar</a>
    
    <p>Projetos cadastrados:</p>
    <?php
    include "conexao.php";
    $sql = "SELECT * FROM projeto";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            echo "<p>Codigo: " . $row["codigo"]. 
            " - Nome: " . $row["nome"]. 
            "- Data: ".$row["data_inicio"].
            "- Valor: ".$row["valor"].
            " | <a href='projeto_bd_deletar.php?codigo=".$row["codigo"]."'>REMOVER</a>".
            " | <a href='projeto_cadastrar.php?codigo=".$row["codigo"]."'>EDITAR</a>".
            "</p>";
            
        }
    } else {
        echo "Nenhum projeto cadastrado";
    }
    $conn->close();
    ?>
</body>
</html>