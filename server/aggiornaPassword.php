<?php
header("Content-Type: application/json; charset=utf-8");
require("mysqli.php");

$password = CheckParams("password");
$username = CheckParams("username");

$conn = openConnection();
$sql = "UPDATE utenti
SET password = '$password'
WHERE username = '$username';";

$data = executeQuery($conn, $sql);

$conn->close();

http_response_code(200);
echo json_encode($data);
?>