# **PROJECT_TASK – Descrizione dei flussi e delle API**

## **Architettura generale**

L’architettura del sistema prevede chiamate tra diversi microservizi, secondo il seguente schema:

```
Client
↓ (REST API – chiamata al BS)
ProjectTaskAPI (borepurposingmgmt)
↓ (chiamata interna BS)
ProjectTaskService (borepurposingmgmt)
↓ (chiamata al MS)
ProjectTaskControllerReadWrite (meRepurposingReg)
↓
Database
```

---

Il modulo **ProjectTask API** espone quattro endpoint REST che permettono di:

1. Recuperare la lista di **Tasks** tramite l' identificativo univoco del Project a cui sono associati.
2. Creare un nuovo **Task** associato ad un progetto specifico.
3. Aggiornare in modalità massiva gli stessi campi dei **Tasks**, associati ad un Project.
4. Aggiornare in modalità multipla campi diversi dei **Tasks** indicati, associati ad un Project.

---
## **GET /v1/projects/{projectId}/tasks**

### **Descrizione**

Consente di ottenere l’elenco dei **Task** associati ad un progetto specifico tramite l'identificativo univoco **projectId**.

### **Flusso operativo**

1. Il **Client** effettua una richiesta `GET /v1/projects/{projectId}/tasks`.
2. La **ProjectTask API BS** (borepurposingmgmt) riceve la richiesta e la inoltra al ProjectTask Service BS per l’elaborazione.
3. Il **ProjectTask Service** prepara la richiesta remota impostando gli opportuni parametri di query e inoltra la richiesta verso il microservizio remoto **ProjectTask API (meRepurposingReg)**, sull'endpoint: {meRepurposingRegEndPoint}/v1/tasks?startDate=&endDate=&docRequired=&deactivated= 
4. Il microservizio interroga il **Database** per recuperare i Task associati al projectId secondo i filtri impostati.
5. Le risorse trovate vengono restituite alla **ProjectTask API**, che restituisce la risposta al client.

### **Risposte possibili**

* **200 OK** → Risorsa trovata; i dettagli sono restituiti in formato JSON.
* **400 Bad Request** → Parametri non validi o richiesta errata.
* **404 Not Found** → Nessuna risorsa trovata associata all’identificativo indicato.
* **500 Internal Server Error** → Errore durante l’elaborazione o nella comunicazione con il servizio remoto.

---
## **POST /v1/projects/{projectId}/tasks**

### **Descrizione**

Consente di creare un nuovo **Task** associato ad un progetto specifico tramite l'identificativo univoco **projectId**.

### **Flusso operativo**

1. Il Client effettua una richiesta: `POST /v1/projects/{projectId}/tasks` con un body JSON conforme al modello `TaskCreateDTORequest`.
2. La **ProjectTask API** inoltra la richiesta al **ProjectTask Service** (borepurposingmgmt), che gestisce la logica di instradamento.
3. **ProjectTask Service** effettua una chiamata POST /v1/projects/{projectId}/tasks verso il microservizio remoto **ProjectTask API MS** (meRepurposingReg) passando il body TaskCreateDTORequest e l'identificativo del progetto a cui associare il nuovo Task.
4. Il microservizio meRepurposingReg elabora la richiesta e interagisce con il Database creando un nuovo record.
5. L’esito dell’operazione e l'identificativo della nuova risorsa creata `IdentifierDTOResponse` vengono restituite alla **ProjectTask API**, che restituisce la risposta al Client.

### **Risposte possibili**

* **201 Created** → Risorsa creata correttamente; viene restituito l'identificativo della risorsa appena creata.
* **400 Bad Request** → Parametri non validi o richiesta errata.
* **404 Not Found** → Nessuna risorsa corrispondente all’identificativo indicato è stata trovata.
* **500 Internal Server Error** → Errore durante l’elaborazione o nella comunicazione con il servizio remoto.

---

## **PATCH /v1/projects/{projectId}/tasks/bulk**

### **Descrizione**

Consente di applicare lo stesso aggiornamento su un campo comune per tutti i Task indicati, associati ad un progetto specifico tramite l'identificativo univoco projectId.

### **Flusso operativo**

1. Il Client effettua una richiesta: `PATCH /v1/projects/{projectId}/tasks/bulk` con un body JSON conforme al modello `WrapperTaskUpdateBulkDTORequest`, contenente quindi la lista di Tasks da aggiornare e i relativi campi modificati.
2. La **ProjectTask API** inoltra la richiesta al **ProjectTask Service** (borepurposingmgmt), che gestisce la logica di instradamento.
3. **ProjectTask Service** inoltra la richiesta PATCH /v1/projects/{projectId}/tasks/bulk verso il microservizio remoto **ProjectTask API MS** (meRepurposingReg) passando il body WrapperTaskUpdateBulkDTORequest e l'identificativo del progetto.
4. Il microservizio meRepurposingReg elabora la richiesta e interagisce con il Database aggiornando massivamente i Task indicati associati al projectId.
5. La **ProjectTask API** riceve l'esito dell'aggiornamento e restituisce la risposta al Client.

### **Risposte possibili**

* **204 No Content** → Aggiornamento completato con successo; nessun contenuto restituito.
* **400 Bad Request** → Parametri o corpo della richiesta non validi.
* **404 Not Found** → Uno o più task non trovati, o progetto corrispondende all'identificativo indicato inesistente.
* **500 Internal Server Error** → Errore durante l’elaborazione o la comunicazione con il servizio remoto.

---

## **PATCH /v1/projects/{projectId}/tasks/multi**

### **Descrizione**

Consente di applicare aggiornamenti su campi differenti per i Task indicati, associati ad un progetto specifico tramite l'identificativo univoco projectId.

### **Flusso operativo**

1. Il Client effettua una richiesta: `PATCH /v1/projects/{projectId}/tasks/multi` con un body JSON conforme al modello `WrapperTaskUpdateMultiDTORequest`, contenente quindi la lista di Tasks da aggiornare e i relativi campi modificati.
2. La **ProjectTask API** inoltra la richiesta al **ProjectTask Service** (borepurposingmgmt), che gestisce la logica di instradamento.
3. **ProjectTask Service** inoltra la richiesta PATCH /v1/projects/{projectId}/tasks/bulk verso il microservizio remoto **ProjectTask API MS** (meRepurposingReg) passando il body WrapperTaskUpdateMultiDTORequest e l'identificativo del progetto.
4. Il microservizio meRepurposingReg elabora la richiesta e interagisce con il Database aggiornando massivamente i Task indicati associati al projectId.
5. La **ProjectTask API** riceve l'esito dell'aggiornamento e restituisce la risposta al Client.

### **Risposte possibili**

* **204 No Content** → Aggiornamento completato con successo; nessun contenuto restituito.
* **400 Bad Request** → Parametri o corpo della richiesta non validi.
* **404 Not Found** → Uno o più task non trovati, o progetto corrispondende all'identificativo indicato inesistente.
* **500 Internal Server Error** → Errore durante l’elaborazione o la comunicazione con il servizio remoto.

---

