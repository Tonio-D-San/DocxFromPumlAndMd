# **COUNTERPART – Descrizione dei flussi e delle API**

## **Architettura generale**

L’architettura del sistema prevede chiamate tra i microservizi **Counterpart BS (borepurposingmgmt)**, **Counterpart MS (meRepurposingReg)**, **DocumentNode MS (meEcDocument)**, secondo il seguente schema:
```
Client
↓
Counterpart BS (borepurposingmgmt)
|   ↓
|   DocumentNode MS (meEcDocument)
↓ 
Counterpart MS (meRepurposingReg)
↓
Database
```

---

Il modulo **Counterpart BS** espone sei endpoint REST che permettono di:

1. Recuperare i dettagli di una singola **Counterpart**.
2. Creare una nuova **Counterpart** con un flusso esteso che prevede la creazione asincrona dei "document node" correlati.
3. Aggiornare una **Counterpart** esistente.
4. Eliminare una **Counterpart**.
5. Cercare una o più **Counterpart** in base a criteri di filtro.
6. Importare più **Counterpart** da un file Excel.

---

## **GET /v1/counterparts/{id}**

### **Descrizione**

Consente di ottenere i dettagli di una **Counterpart** specifica tramite il suo identificativo `id`.

### **Flusso operativo**

1. Il **Client** effettua una richiesta `GET /v1/counterparts/{id}` al microservizio **BS (borepurposingmgmt)**.
2. Il **Counterpart BS** riceve la richiesta, la elabora e inoltra la chiamata verso il microservizio **MS (meRepurposingReg)**.
3. Il microservizio **Counterpart MS** interroga il **Database** per recuperare i dati del Counterpart corrispondente all'identificativo univoco indicato.
4. La risorsa trovata `CounterpartDetailDTOResponse` viene restituita a **MS**, che restituisce la risposta al microservizio **BS**.
5. Il microservizio **Counterpart BS** inoltra la risposta e il JSON corrispondente al Client.

### **Risposte possibili**

* **200 OK** → Risorsa trovata; i dettagli di Counterpart vengono restituiti in formato JSON.
* **400 Bad Request** → Parametro `id` non valido.
* **404 Not Found** → Nessuna risorsa trovata per l’identificativo indicato.
* **500 Internal Server Error** → Errore durante l’elaborazione o nella comunicazione con il servizio remoto.

---

## **PATCH /v1/counterparts/{id}**

### **Descrizione**

Consente di aggiornare le informazioni di una **Counterpart** esistente attraverso il suo identificativo univoco `id`.

### **Flusso operativo**

#### **Richiesta di aggiornamento**

1. Il **Client** effettua una richiesta `PATCH /v1/counterparts/{id}` contenente il body JSON conforme al modello `CounterpartDTORequest` con i campi da aggiornare, al microservizio **BS (borepurposingmgmt)**.
2. **Counterpart BS** riceve la richiesta, la elabora convertendo il body JSON in un wrapper conforme al modello `WrapperCounterpartUpdateDTORequest` per l'update multiplo e inoltra la richiesta verso il microservizio **MS (meRepurposingReg)**.
3. Il microservizio **Counterpart MS** interroga il **Database** aggiornando i campi indicati dal JSON Request.
4. L'esito dell'aggiornamento viene restituito a **MS**, che inoltra la risposta al microservizio **BS**.

#### **Flusso asincrono di aggiornamento del Document Node**

1. **Counterpart BS** avvia un flusso asincrono per l'aggiornamento dei **Document Node** ed effettua una chiamata `GET /v1/counterparts/{id}` al microservizio **MS**.
2. **MS** riceve la richiesta e interroga il **Database** per recuperare i dettagli di una Counterpart attraverso il suo identificativo univoco. 
3. **BS** riceve il JSON di risposta conforme al modello `CounterpartDetailDTOResponse` come esito della ricerca. 
4. **BS** verifica le modifiche apportate alla Counterpart, nello specifico effettua dei controlli sui campi name e country, ed eventualmente sulla base alle variazioni, invoca il microservizio **DocumentNode MS (meEcDocument)** per la rinomina o spostamento del **Node**.
5. **DocumentNode MS** effettua una chiamata `PUT /v1/documents/{nodeId}` inviando come body della richiesta un JSON conforme al modello `UpdateNodeDTORequest` con le informazioni aggiornate del Document Node.
6. **BS** riceve dal microservizio **DocumentNode MS** l'esito dell'operazione di aggiornamento del Node.
8. **BS** invia una risposta al Client con l'esito dell'operazione complessiva di aggiornamento.
5. 
Il microservizio **Counterpart BS** inoltra la risposta al Client.

### **Risposte possibili**

* **204 No Content** → Aggiornamento completato con successo; nessun contenuto restituito.
* **400 Bad Request** → Parametri o corpo della richiesta non validi.
* **404 Not Found** → Risorsa non trovata per l'identificativo indicato.
* **500 Internal Server Error** → Errore durante l’elaborazione o la comunicazione con il servizio remoto.

---

## **POST /v1/counterparts**

### **Descrizione**

Consente di creare una o più **Counterpart**. Il flusso di creazione è articolato e prevede anche la creazione asincrona dei **Node document** associati a ciascun Counterpart e il successivo aggiornamento dei record con il riferimento al node document.

### **Flusso operativo**

#### **Richiesta di creazione**

1. Il **Client** invia una richiesta `POST /v1/counterparts` con un body JSON conforme al modello `CounterpartDTORequest` al microservizio **BS (borepurposingmgmt)**.
2. **Counterpart BS** riceve la richiesta, converte il body JSON in un wrapper conforme al modello `WrapperCounterpartCreateDTORequest`e lo passa come body JSON nella chiamata `POST /v1/counterparts/multi` verso il microservizio **MS (meRepurposingReg)** per la creazione multipla.
3. Il microservizio **Counterpart MS** interroga il **Database** e inserisce le nuovi Counterpart.
4. L'esito dell'inserimento dei nuovi record viene restituito a **MS** che inoltra il JSON Response conforme al modello `CreateMultiDTOResponse`, contenente gli identificativi ids[] delle Counterpart creati, al microservizio **BS**. 

#### **Flusso asincrono**

1. In parallelo, il **BS** avvia un flusso asincrono per la creazione dei **Document Node** associati a ciascuna **Counterpart**. 
2. **BS** recupera la lista degli Id dei Counterpart appena creati e costruisce una richiesta di ricerca per ottenere le informazioni complete dei Counterpart effettuando una chiamata `POST /v1/counterparts/search` verso **MS**.
2. Il **Counterpart MS** esegue la query sul Database e restituisce al **BS** un body JSON conforme al modello`WrapperCounterpartDTOResponse`.
3. Per ciascuna Counterpart recuperata, Il **BS** costruisce una request `CreateNodeDTORequest` contenente i dati necessari per la creazione del document node e invia una richiesta `POST /v1/documents/nodes` al microservizio **DocumentNode MS (meEcDocument)**.
4. **BS** recupera e associa ad ogni Counterpart il nodeId relativo; la lista viene wrappata in un JSON conforme al modello `WrapperCounterpartUpdateDTORequest` e utilizzata come body per la chiamata successiva di aggiornamento dei Counterpart.
5. **BS** utilizza come body JSON `WrapperCounterpartUpdateDTORequest` ed effettua una chiamata `PATCH /v1/counterparts/multi` verso il microservizio **Counterpart MS** per l'aggiornamento multiplo dei Counterpart.
6. **MS** interroga il Database aggiornando i record di Counterpart tramite l'associazione con il nodeId e comunica l'esito dell'aggiornamento a **BS**.
7. **Counterpart BS** restituisce al Client l'esito complessivo dell'operazione di creazione dei Counterpart.


### **Risposte possibili**

* **201 Created** → Creazione avvenuta con successo; risposta contenente gli identificativi delle nuove risorse.
* **400 Bad Request** → Parametri o corpo della richiesta non validi.
* **404 Not Found** → Risorse correlate non trovate.
* **409 Conflict** → Risorsa già esistente.
* **500 Internal Server Error** → Errore durante la creazione o nella comunicazione con il servizio remoto.

---

## **DELETE /v1/counterparts/{id}**

### **Descrizione**

Consente di eliminare una **Counterpart** esistente tramite il suo identificativo `id`.

### **Flusso operativo**

1. Il **Client** effettua una richiesta di eliminazione `DELETE /v1/counterparts/{id}` verso **Counterpart BS**, indicando l’identificativo del Counterpart da eliminare.
2. **Counterpart BS** riceve la richiesta e la inoltra al microservizio **Counterpart MS**.
3. Il microservizio **MS** interroga il **Database** ed elimina la risorsa corrispondente all'indentificativo indicato.
4. L'esito dell'operazione di eliminazione viene restituito al **BS** che inoltra la risposta al Client.

### **Risposte possibili**

* **204 No Content** → Eliminazione completata con successo; nessuna contenuto restituito.
* **400 Bad Request** → Parametri non validi.
* **404 Not Found** → Risorsa non trovata.
* **409 Conflict** → Impossibile eliminare la risorsa per vincoli o relazioni esistenti.
* **500 Internal Server Error** → Errore durante l’elaborazione o la comunicazione con il servizio remoto.

---

## **POST /v1/counterparts/search**

### **Descrizione**

Permette di cercare una o più **Counterpart** in base a specifici parametri di filtro.

### **Flusso operativo**

1. Il **Client** effettua una richiesta di ricerca `POST /v1/counterparts/search` verso **Counterpart BS** con un body JSON conforme al modello `CounterpartSearchDTORequest` contenente i criteri di ricerca.
2. **Counterpart BS** riceve e inoltra la richiesta al **Counterpart MS**.
3. Il microservizio **MS** interroga il **Database** in base ai filtri di ricerca forniti.
4. **MS** restituisce il JSON response conforme al modello `WrapperCounterpartDTOResponse` a **BS**.
5. L'esito dell'operazione di ricerca viene restituito al **BS** che inoltra la risposta al Client.

### **Risposte possibili**

* **200 OK** → Ricerca completata con successo; la risposta contiene la lista delle controparti trovate.
* **500 Internal Server Error** → Errore durante l’elaborazione o la comunicazione con il servizio remoto.

---

## **POST /v1/counterparts/import**

### **Descrizione**

Consente di importare più **Counterpart** a partire da un file Excel contenente i dati.

### **Flusso operativo**

#### **Upload e parsing del file**

1. Il **Client** invia una richiesta `POST /v1/counterparts/import`con il file Excel allegato nel body (multipart/form-data o binario).
2. **Counterpart BS** riceve la richiesta, elabora il contenuto del file e costruisce un JSON conforme al modello `WrapperCounterpartCreateDTORequest` per la richiesta di creazione multipla.

#### **Richiesta di creazione**

1. **Counterpart BS** utilizza come body JSON `WrapperCounterpartCreateDTORequest` nella chiamata `POST /v1/counterparts/multi` verso il microservizio **MS (meRepurposingReg)** per la creazione multipla.
2. Il microservizio **Counterpart MS** interroga il **Database** e inserisce i nuovi Counterpart.
3. L'esito dell'inserimento dei nuovi record viene restituito a **MS** che inoltra il JSON Response conforme al modello `CreateMultiDTOResponse`, contenente gli identificativi ids[] dei Counterpart creati, al microservizio **BS**.

#### **Flusso asincrono**

1. In parallelo, il **BS** avvia un flusso asincrono per la creazione dei **Document Node** associati a ciascuna **Counterpart**.
2. **BS** recupera la lista degli Id dei Counterpart appena creati e e costruisce una richiesta di ricerca per ottenere le informazioni complete dei Counterpart effettuando una chiamata `POST /v1/counterparts/search` verso **MS**.
2. Il **Counterpart MS** esegue la query sul Database e restituisce al **BS** un body JSON conforme al modello`WrapperCounterpartDTOResponse`.
3. Per ciascuna Counterpart recuperato, Il **BS** costruisce una request `CreateNodeDTORequest` contenente i dati necessari per la creazione del document node e invia una richiesta `POST /v1/documents/nodes` al microservizio **DocumentNode MS (meEcDocument)**.
4. **BS** recupera e associa ad ogni Counterpart il nodeId relativo; la lista viene wrappata in un JSON conforme al modello `WrapperCounterpartUpdateDTORequest` e utilizzata come body per la chiamata successiva di aggiornamento dei Counterpart.
5. **BS** utilizza come body JSON `WrapperCounterpartUpdateDTORequest` ed effettua una chiamata `PATCH /v1/counterparts/multi` verso il microservizio ** Counterpart MS** per l'aggiornamento multiplo dei Counterpart.
6. **MS** interroga il Database aggiornando i record di Counterpart tramite l'associazione con il nodeId e comunica l'esito dell'aggiornamento a **BS**.
7. **Counterpart BS** restituisce al Client l'esito complessivo dell'operazione di creazione dei Counterpart.


### **Risposte possibili**

* **201 Created** → Creazione avvenuta con successo; risposta contenente gli identificativi delle nuove risorse.
* **400 Bad Request** → Parametri o corpo della richiesta non validi.
* **404 Not Found** → Risorse correlate non trovate.
* **409 Conflict** → Risorsa già esistente.
* **500 Internal Server Error** → Errore durante la creazione o nella comunicazione con il servizio remoto.

---

## **Riepilogo Endpoint**

| Metodo     | Endpoint                  | Descrizione                                   |
|------------|---------------------------|-----------------------------------------------|
| **GET**    | `/v1/counterparts/{id}`   | Recupera i dettagli di una Counterpart.       |
| **PATCH**  | `/v1/counterparts/{id}`   | Aggiorna i dati di una Counterpart esistente. |
| **POST**   | `/v1/counterparts`        | Crea una nuova Counterpart.                   |
| **DELETE** | `/v1/counterparts/{id}`   | Elimina una Counterpart.                      |
| **POST**   | `/v1/counterparts/search` | Effettua una ricerca dei Counterpart.         |
| **POST**   | `/v1/counterparts/import` | Importa Counterpart da un file Excel.         |

---