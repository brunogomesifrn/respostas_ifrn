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
    $nome = $_POST["nome"];
    $nascimento = $_POST["nascimento"];
    $idade = $_POST["idade"];
    $sexo = $_POST["sexo"];
    $disciplinas = $_POST["disciplinas"];

    echo "<p>Nome Digitado: $nome </p>";
    echo "<p>Data de nascimento: $nascimento </p>";
    echo "<p>Idade: $idade </p>";
    echo "<p>Sexo: $sexo </p>";
    
    echo "<p>Disciplinas Marcadas</p>";
    foreach($disciplinas as $disc){
        echo "<p> $disc </p>";
    }

    ?>
</body>
</html>