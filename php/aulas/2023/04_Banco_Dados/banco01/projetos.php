<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Projetos</h1>
    <p><a href="projeto_cadastro.php">CADASTRAR</a></p>
    <p>Cursos Cadastrados:</p>

    <?php
    include 'conexao.php';
    
    $sql = "SELECT * FROM projeto";
    $result = $conn->query($sql);

    if($result->num_rows>0){
        while($row = $result->fetch_assoc()){
            echo "<p>Nome: ".$row["nome"].
            "Data: ".$row["data_inicio"].
            "Valor: ".$row["valor"].
            "<a href='projeto_bd_remover.php?codigo=".
            $row["codigo"]."'>REMOVER</a></p>";
            
        }
    }else{
        echo "<p>Nenhum projeto</p>";
    }

    $conn->close();
    ?>

</body>
</html>