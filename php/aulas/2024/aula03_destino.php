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
        $nome_digitado = $_GET["nome"];
        $email_digitado = $_GET["email"];
        
        echo "<p>Nome recebido: $nome_digitado </p>";
        echo "<p>E-mail recebido: $email_digitado </p>";
    ?>
</body>
</html>