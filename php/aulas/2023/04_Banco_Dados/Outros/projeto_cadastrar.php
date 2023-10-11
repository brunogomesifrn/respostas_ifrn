<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

<?php
    $codigo = "";
    $nome = "";
    $data_inicio = "";
    $valor = "";
    
    if (isset($_GET['codigo'])) {
        $codigo = $_GET['codigo'];
        include "conexao.php";
        $sql = "SELECT * FROM projeto where codigo=$codigo";
        $result = $conn->query($sql);

        if ($result->num_rows > 0) {
            while($row = $result->fetch_assoc()) {
                $codigo = $row["codigo"];
                $nome = $row["nome"];
                $data_inicio = $row["data_inicio"];
                $valor = $row["valor"];
            }
        } else {
            echo "0 results";
        }
        $conn->close();
    }

    
    

?>
    <h1>Cadastrar Projeto</h1>
    <?php
    if (isset($_GET['codigo'])) {
        echo "<form action='projeto_bd_editar.php' method='post'>";
    }else{
        echo "<form action='projeto_bd_registro.php' method='post'>";
    }
    
?>
    <p>
        <label for="nome">Nome</label>
        <input type="text" name="nome" id="nome" value="<?php echo $nome;?>" />
    </p>
    <p>
        <label for="data">Data de Início</label>
        <input type="date" name="data_inicio" id="data" value="<?php echo $data_inicio;?>"/>
    </p>
    <p>
        <label for="valor">Valor</label>
        <input type="number" name="valor" id="valor" step="0,01" value="<?php echo $valor;?>"/>
    </p>
    <input type="hidden" name="codigo" value="<?php echo $codigo;?>" />
    <p>
        <input type="submit" value="Enviar" />
    </p>
    </form>
</body>
</html>