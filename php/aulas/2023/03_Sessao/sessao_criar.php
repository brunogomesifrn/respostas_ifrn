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

    /*
    Sempre que for utilizar sessão em uma página,
    independente de ser a primeira vez, segunda
    ou para encerrar uma sessão, devemos utilizar
    inicialmente a função session_start();
    */

    session_start();

    $_SESSION["usuario"] = "brunovisk";

    ?>
</body>
</html>