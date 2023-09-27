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
    $sql = "SELECT * FROM projetos";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            echo "<p>Codigo: " . $row["codigo"]. " - Nome: " . $row["nome"]. "</p>";
        }
    } else {
        echo "Nenhum projeto cadastrado";
    }
    $conn->close();
    ?>
</body>
</html>