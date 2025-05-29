<?php
header("Content-type:application/json; charset-utf-8");
require("mysqli.php");

// si definisce questa costante della durata di 30 secondi, questo è il modo per definire le varibili costanti, sempre espresso in secondi
define("TIMEOUT", 30);

$conn = OpenConnection();

$user = CheckParams("username");
$pwd = CheckParams("password");

// Prevenzione attacchi di SQL Injection
$user = $conn->real_escape_string($user);
$pwd = $conn->real_escape_string($pwd);

// In questa query user è un case unsensitive ma la passowrd deve essere case sensitive
$sql = "SELECT * FROM utenti WHERE userName = '$user'";

$data = ExecuteQuery($conn, $sql);

if (count($data) == 0) {
    http_response_code(401);
    die("Username errato");
} else if ($data[0]["Pwd"] != $pwd) {
    http_response_code(401);
    die("Password errata");

} else {
    // Crea la sessione
    session_start();

    // time() restiiituisce data e ora correnti in secondi, timeout è un timeout di durata della sessione che è deciso da noi
    $_SESSION ["Scadenza"] = time() + TIMEOUT;
    $_SESSION ["NomeUtente"] = $data[0]["userName"];

    // Restituisce sempre il nome che vogliamo dare al cookie di sessione
    setcookie(session_name(), session_id(), $_SESSION ["Scadenza"], "/");

    http_response_code(200);
    echo (json_encode("ok"));
}
?>