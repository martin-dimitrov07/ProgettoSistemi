<?php
function openConnection(): mysqli
{
    define("DB_NAME", "dischi");
    // In questo modo si definisce che si sta usando un database che si trova sul nostro computer
    // Se invece il database fosse su un altro computer, è necessario inserirne l'indirizzo IP
    define("DB_HOST", "localhost");
    // mySql quando crea un database, viene creato un utente root, per ogni database che viene creato
    define("DB_USER", "root");
    define("DB_PASS", "");

    // Serve per abilitare il try and catch sulle linee successive, di base lui non è abilitato
    mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);

    try {
        // Questo crea una nuova connessione al database people
        $con = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
        // Serve ad impostare un determinato set di caratteri che il server deve utilizzare per comunicare con il DB
        $con->set_charset("utf8mb4");
        return $con;
    } catch (mysqli_sql_exception $err) {
        // Questo errore 503 indica che è impossibile connettersi con il database 
        http_response_code(503);
        // die scrive sulla pagina, come la echo, la differenza è che poi lo script finisce lì
        die("<b>Errore connessione al DB</b> " . $err->getMessage());
    }
}

function executeQuery($con, $sql): mixed
{
    try {
        $result = $con->query($sql);

        // Se non è un booleano significa che la chiamata non è di tipo GET
        if (!is_bool($result)) {
            // fetch_all converte da recordSet a vettore enumerativo di JSON, solo in caso di chiamate GET
            $data = $result->fetch_all(MYSQLI_ASSOC);
        } else {
            // Converto da record PHP a vettore enumerativo di JSON solo nel caso delle chiamate GET
            $data = $result;
        }
        return $data;
    } catch (mysqli_sql_exception $err) {
        // La connessione è necessario chiuderla, dato che si rischia che molte connessioni rimangano aperte inutilmente, che 
        // inoltre impegnano il database. Ogni volta che lo script parte, apre una nuova connessione, quindi per evitare saturazione del
        // database bisogna chiudere la connessioni quando non serve
        $con->close();
        http_response_code(503);
        die("<b>Errore query</b>" . $err->getMessage());
    }
}

function CheckParams($param): mixed
{
    //per accedere a una variabile globale devo scrivere "global" seguito dal nome della variabile
    global $conn;
    //php consegna tutti i parametri dentro $_REQUEST
    if (isset($_REQUEST[$param]))
        //ritorna il valore del parametro(nel primo caso il contenuto del textBox)
        return $_REQUEST[$param];
    else {
        //errore di parametri mancanti
        http_response_code(400);
        $conn->close();
        die("Parametro $param mancante");
    }
}
?>