<?php
    $nome = "";
    if(isset($_GET["id"])){
        $id = $_GET["id"];
        
        include "banco/conexao.php";
        $conn = conectar();
        $sql = "SELECT * FROM categoria WHERE id=$id";
        $result = $conn->query($sql);

        if($result->num_rows > 0){
            while($row = $result->fetch_assoc()){
                $nome = $row["nome"];
            }
        }
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Cadastrar Categoria</h1>
    
    <?php
    if(isset($_GET["id"])){
    ?>
    
    <form action="bd_categoria_editar.php" method="post">

    <?php
    }else{
    ?>

    <form action="bd_categoria_adicionar.php" method="post">

    <?php
    }
    ?>
        <p>
            <label for="cat">Nome:</label>
            <input type="text" name="categoria" id="cat" value="<?php echo $nome; ?>"/>
        </p>

        <p>
            <input type="submit" value="Enviar"/>
        </p>

    </form>

</body>
</html>