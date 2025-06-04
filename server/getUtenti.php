<?php
header("Content-Type: application/json; charset=utf-8");
require("mysqli.php");

session_start();

$user = $_SESSION["NomeUtente"];

$conn = openConnection();
$sql = "SELECT * FROM utenti
WHERE username != '$user' AND username != 'server';";

$data = executeQuery($conn, $sql);

$conn->close();

http_response_code(200);
echo json_encode($data);
?>