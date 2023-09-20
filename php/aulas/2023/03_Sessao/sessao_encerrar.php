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
    session_start();

    // session_unset() remove variáveis de sessão
    session_unset();

    // session_destroy() encerra toda a sessão
    session_destroy();
    ?>
</body>
</html>