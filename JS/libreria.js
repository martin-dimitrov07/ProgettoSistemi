"use strict";

const JSONSERVER_URL = "http://localhost:3000"
const APACHE_URL = "";
// Se la url è vuota viene assegnata l'origine da cui è stata scaricata la pagina
// Nelle chiamate AJAX se io non passo la URL (URL vuota = "") lui usa la URL corrente del sito web corrente
// cioè lui fa una richiesta alla cartella dove c'è la pagina principale (index.html, index.php)

function inviaRichiesta(method, url, parameters = {}) {
	let axiosOptions = {
		"baseURL": APACHE_URL,
		"url": url,
		"method": method.toUpperCase(),
		"headers": {
			"Accept": "application/json",
		},
		"timeout": 5000,
		"responseType": "json",
	}
	if (parameters instanceof FormData) {
		axiosOptions.headers["Content-Type"] = 'multipart/form-data;'
		axiosOptions["data"] = parameters     // Accept Blob
	}
	else if (method.toUpperCase() == "GET") {
		// Il server anche nelle chiamate GET si aspetta i parametri passati in urlencoded
		axiosOptions.headers["Content-Type"] = 'application/x-www-form-urlencoded;charset=utf-8'
		axiosOptions["params"] = parameters   // Accept plain object or URLSearchParams
	}
	else {
		// Il server json-server si aspetta i parametri passati in formato json
		// axiosOptions.headers["Content-Type"] = 'application/json;charset=utf-8'
		// Il server anche NON nelle chiamate GET si aspetta i parametri passati in urlencoded
		axiosOptions.headers["Content-Type"] = 'application/x-www-form-urlencoded;charset=utf-8'
		axiosOptions["data"] = parameters
	}
	return axios(axiosOptions)
}


function errore(err) {
	if (!err.response)
		alert("Connection Refused or Server timeout");
	else if (err.response.status == 200)
		alert("Formato dei dati non corretto : " + err.response.data);
	else
		alert("Server Error: " + err.response.status + " - " + err.response.data)
}

