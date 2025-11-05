# **PLANT – Descrizione dei flussi e delle API**

## **Architettura generale**

L’architettura del sistema prevede chiamate tra i microservizi **Plant BS (borepurposingmgmt)** e **Plant MS (meRepurposingReg)**, secondo il seguente schema:

```
Client
↓ 
Plant BS (borepurposingmgmt)
↓ 
Plant MS (meRepurposingReg)
↓
Database
```

---

Il modulo **Plant BS** espone tre endpoint REST che permettono di:

1. Recuperare i dettagli di un singolo **Plant**.
2. Effettuare una ricerca di uno o più **Plant** in base a filtri di ricerca.
3. Aggiornare le informazioni di un **Plant** esistente.

---

## **GET /v1/plants/{id}**

### **Descrizione**

Consente di ottenere i dettagli di un Plant specifico tramite il suo identificativo univoco `id`.

### **Flusso operativo**

1. Il **Client** effettua una richiesta `GET /v1/plants/{id}` al microservizio **BS (borepurposingmgmt)**.
2. Il **Plant BS** riceve la richiesta, la elabora impostando gli opportuni parametri e inoltra la chiamata verso il microservizio **MS (meRepurposingReg)**.
3. Il microservizio **Plant MS** interroga il **Database** per recuperare i dati del Plant corrispondente all'identificativo univoco indicato.
4. La risorsa trovata `PlantDetailDTOResponse` viene restituita a **MS** , che restituisce la risposta al microservizio **BS**.
5. Il microservizio **Plant BS** inoltra la risposta e il JSON corrispondente al Client.

### **Risposte possibili**

* **200 OK** → Risorsa trovata; i dettagli sono restituiti in formato JSON.
* **400 Bad Request** → Parametro `id` non valido.
* **404 Not Found** → Nessuna risorsa trovata corrispondente all’identificativo indicato.
* **500 Internal Server Error** → Errore durante l’elaborazione o nella comunicazione con il servizio remoto.

---

## **POST /v1/plants/search**

### **Descrizione**

Consente di cercare uno o più Plant in base alla configurazione di parametri di ricerca.

### **Flusso operativo**

1. Il **Client** invia una richiesta `POST /v1/plants/search` contenente un body JSON conforme al modello `PlantSearchDTORequest`, al microservizio **BS (borepurposingmgmt)**.
2. Il **Plant BS** riceve la richiesta, la elabora impostando gli opportuni parametri e inoltra la chiamata verso il microservizio **MS (meRepurposingReg)**.
3. Il microservizio **Plant MS** esegue la query sul **Database** in base ai filtri di ricerca ricevuti.
4. I risultati della ricerca vengono restituiti a **MS**, che inoltra al microservizio **BS** una response con un body JSON conforme al modello `WrapperPlantDTOResponse`.
5. Il microservizio **Plant BS** inoltra la risposta e il JSON corrispondente al Client.

### **Risposte possibili**

* **200 OK** → Ricerca completata con successo; la risposta contiene la lista dei Plant trovati.
* **500 Internal Server Error** → Errore generico nella chiamata remota o durante l’elaborazione.

---

## **PATCH /v1/plants/{id}**

### **Descrizione**

Consente di aggiornare le informazioni di un **Plant** esistente tramite il suo identificativo univoco `id`.

### **Flusso operativo**

1. Il **Client** effettua una richiesta `PATCH /v1/plants/{id}` contenente un body JSON conforme al modello `PlantUpdateDTORequest` con i campi da aggiornare, al microservizio **BS (borepurposingmgmt)**.
2. Il **Plant BS** riceve la richiesta, la elabora impostando gli opportuni parametri e inoltra la chiamata verso il microservizio **MS (meRepurposingReg)**.
3. Il microservizio **Plant MS** interroga il **Database** aggiornando i campi indicati dal JSON Request.
4. L'esito dell'aggiornamento viene restituito a **MS**, che inoltra la risposta al microservizio **BS**.
5. Il microservizio **Plant BS** inoltra la risposta al Client.

### **Risposte possibili**

* **204 No Content** → Aggiornamento eseguito con successo; nessun contenuto restituito.
* **400 Bad Request** → Parametri o corpo della richiesta non validi.
* **404 Not Found** → Risorsa non trovata.
* **500 Internal Server Error** → Errore durante l’elaborazione o nella comunicazione con il servizio remoto.
