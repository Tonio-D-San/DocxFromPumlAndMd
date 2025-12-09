# Solo infrastrutturale

- !.idea/*&!src/* → Non confronti sia la cartella .idea che la cartella src (perché la migrazione è infrastrutturale)

## Legenda
|             | Significato                                                                                                          |
|-------------|----------------------------------------------------------------------------------------------------------------------|
| [Da rifare] | L'attività era stata già completata ma per esigenze esterne e.g. cambio branch di partenza si è dovuta ripetere      |
| [Rifatto]   | L'attività precedentemente descritta come "Da rifare" è stata completata con successo                                |
| [OK]        | L'attività è stata completata con successo                                                                           |
| [X]         | L'attività non è stata completata e si sta lavorando per capire il problema                                          |
| [Non serve] | L'attività è stata precedentemente assegnata e poi, successivamente, tolta. Scrivere nel campo "Note" la motivazione |
| [Attendere] | L'atttività è stata sospesa per motivi esterni. Scrivere nel campo "Note" la motivazione                             |

## Servizi
| Migrato     | Buildato    | Deployato   | Codice    | Template   | Branch di partenza              | Branch di migrazione        | Link Repository                                                                                                         | Commit                                   | Build                                                                                                                     | Note                                                                     | Link Deploy Qa                                                                                     | 
|-------------|-------------|-------------|-----------|------------|---------------------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [Da rifare] | [Da rifare] | [Non serve] | bp00058   | pltb030    | master                          | migrazione/template_to_1.17 | https://bitbucket.springlab.enel.com/projects/GLGT-AP35622-MS-PLATFORM/repos/glgt-bp00058-lan-booilcmptanalysis/browse  | 1c3f98fcb8c0c156c5bfa244d452d0bc36d47e15 | https://bamboo.springlab.enel.com/browse/GLGTAP35622MSPLATFORM-GLGTBP00058DEVBOOILCMPTANALYSISAPPLANCUSTOMV1-BUILDSRC-159 | Da controllare se ci sono conflitti dal branch di sviluppo attuale       | -------------------------------------------------------------------------------------------------- | 
| [Rifatto]   | [Attendere] | [Attendere] | bp00058   | pltb030    | feature/R4_2025                 | migrazione/template_to_1.17 | https://bitbucket.springlab.enel.com/projects/GLGT-AP35622-MS-PLATFORM/repos/glgt-bp00058-lan-booilcmptanalysis/browse  | 921b7d04a2b88df37c56232f1f41b062457c562f |                                                                                                                           | Nessun conflitto in data 20/11/2025                                      |                                                                                                    |
| [OK]        | [OK]        | [OK]        | bp00182   | pltb030    | master                          | migrazione/template_to_1.17 | https://bitbucket.springlab.enel.com/projects/GLGT-AP35622-MS-PLATFORM/repos/glgt-bp00182-lan-bogmi/browse              | 74eba688e6952efd130de69e70f0bf9e62d26acb | https://bamboo.springlab.enel.com/browse/GLGTAP35622MSPLATFORM-GLGTBP00182DEVBOGMIAPPLANCUSTOMV1-40                       |                                                                          | https://bamboo.springlab.enel.com/deploy/viewDeploymentResult.action?deploymentResultId=1910576778 | 
| [OK]        | [OK]        | [Non serve] | bp00195   | pltb030    | master                          | migrazione/template_to_1.17 | https://bitbucket.springlab.enel.com/projects/GLGT-AP35622-MS-PLATFORM/repos/glgt-bp00195-lan-bottoperations/browse     | 4df00a2835d07b01d94ff5c4ea5ca0f7d4f0a9e4 | https://bamboo.springlab.enel.com/browse/GLGTAP35622MSPLATFORM-GLGTBP00195DEVBOTTOPERATIONSAPPLANCUSTOMV1-BUILDSRC-206    | Il team di sviluppo ha preso in carico la migrazione per questo servizio | -------------------------------------------------------------------------------------------------- | 
| [OK]        | [Non serve] | [Non serve] | bp00199   | pltb030    | master                          | migrazione/template_to_1.17 | https://bitbucket.springlab.enel.com/projects/GLGT-AP35622-MS-PLATFORM/repos/glgt-bp00199-lan-bottadministration/browse | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | Il team di sviluppo ha preso in carico la migrazione per questo servizio | -------------------------------------------------------------------------------------------------- | 
| [OK]        | [Non serve] | [Non serve] | bp00200   | pltb030    | master                          | migrazione/template_to_1.17 | https://bitbucket.springlab.enel.com/projects/GLGT-AP35622-MS-PLATFORM/repos/glgt-bp00200-lan-bottcontract/browse       | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | Il team di sviluppo ha preso in carico la migrazione per questo servizio | -------------------------------------------------------------------------------------------------- | 
| [OK]        | [OK]        | [OK]        | bp00212   | pltb030    | master                          | migrazione/template_to_1.17 | https://bitbucket.springlab.enel.com/projects/GLGT-AP35622-MS-PLATFORM/repos/glgt-bp00212-lan-boinstrmntmgmt/browse     | 9a2aa3d096a47dbb5a5087b702de0cadc0fcc073 | https://bamboo.springlab.enel.com/browse/GLGTAP35622MSPLATFORM-GLGTBP00212DEVBOINSTRMNTMGMTAPPLANCUSTOMV1-158             |                                                                          | https://bamboo.springlab.enel.com/deploy/viewDeploymentResult.action?deploymentResultId=1910576920 | 
| -----       | ----------  | ----------  | --------- | ---------- | ------------------------------- | --------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- | 
| [OK]        | [OK]        | [OK]        | mp00399   | pltm003    | master                          | migrazione/template_to_3.33 | https://bitbucket.springlab.enel.com/projects/GLGT-AP35622-MS-PLATFORM/repos/glgt-mp00399-lan-megmiweb/browse           | 362052c1b01fb760afea0231b53beef85d6c00bf | https://bamboo.springlab.enel.com/browse/GLGTAP35622MSPLATFORM-GLGTMP00399DEVMEGMIWEBAPPLANCUSTOMV1-46                    | Build ok. 1Console megmiweb-mem: 148%                                    | https://bamboo.springlab.enel.com/deploy/viewDeploymentResult.action?deploymentResultId=1910577441 | 
| [OK]        | [OK]        | [OK]        | mp00400   | pltm003    | master                          | migrazione/template_to_3.33 | https://bitbucket.springlab.enel.com/projects/GLGT-AP35622-MS-PLATFORM/repos/glgt-mp00400-lan-megmiboroscopia/browse    | 22244486c8c28a8175927d885301abf9198c2cbb | https://bamboo.springlab.enel.com/browse/GLGTAP35622MSPLATFORM-GLGTMP00400DEVMEGMIBOROSCOPIAAPPLANCUSTOMV1-48             |                                                                          | https://bamboo.springlab.enel.com/deploy/viewDeploymentResult.action?deploymentResultId=1910577788 | 
| [OK]        | [OK]        | [Attendere] | mp00443   | pltm003    | master                          | migrazione/template_to_3.33 | https://bitbucket.springlab.enel.com/projects/GLGT-AP35622-MS-PLATFORM/repos/glgt-mp00443-lan-megmilogic/browse         | af56d2698e3722ef718fac8e33237685facfc590 | https://bamboo.springlab.enel.com/browse/GLGTAP35622MSPLATFORM-GLGTMP00443DEVMEGMILOGICAPPLANCUSTOMV1-TES-87              | Ci sono problemi con aws. Restituisce 403 Forbidden                      |                                                                                                    | 
| [OK]        | [Non serve] | [Non serve] | mp00489   | pltm003    | master                          | migrazione/template_to_3.33 | https://bitbucket.springlab.enel.com/projects/GLGT-AP35622-MS-PLATFORM/repos/glgt-mp00489-lan-meargosintegration/browse | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | Il team di sviluppo ha preso in carico la migrazione per questo servizio | -------------------------------------------------------------------------------------------------- | 
| [OK]        | [OK]        | [OK]        | mp00482   | pltm003    | master                          | migrazione/template_to_3.33 | https://bitbucket.springlab.enel.com/projects/GLGT-AP35622-MS-PLATFORM/repos/glgt-mp00482-lan-meinstrumentation/browse  | 4c495710bbbeb4e78131a57f0c58ef1404bbb546 | https://bamboo.springlab.enel.com/browse/GLGTAP35622MSPLATFORM-GLGTMP00482DEVMEINSTRUMENTATIONAPPLANCUSTOMV1-425          |                                                                          | https://bamboo.springlab.enel.com/deploy/viewEnvironment.action?id=538804507                       | 
| -----       | ----------- | ----------  | --------- | ---------- | ------------------------------- | --------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- | 
| [OK]        | [Non serve] | [Non serve] | mp00453   | pltm006    | master                          | migrazione/template_to_2.36 | https://bitbucket.springlab.enel.com/projects/GLGT-AP35622-MS-PLATFORM/repos/glgt-mp00453-lan-mettoperations/browse     | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | Il team di sviluppo ha preso in carico la migrazione per questo servizio | -------------------------------------------------------------------------------------------------  | 
| [OK]        | [Non serve] | [Non serve] | mp00461   | pltm006    | master                          | migrazione/template_to_2.36 | https://bitbucket.springlab.enel.com/projects/GLGT-AP35622-MS-PLATFORM/repos/glgt-mp00461-lan-mettcontract/browse       | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | Il team di sviluppo ha preso in carico la migrazione per questo servizio | -------------------------------------------------------------------------------------------------- | 
| [OK]        | [Non serve] | [Non serve] | mp00462   | pltm006    | master                          | migrazione/template_to_2.36 | https://bitbucket.springlab.enel.com/projects/GLGT-AP35622-MS-PLATFORM/repos/glgt-mp00462-lan-mettadminstration/browse  | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | Il team di sviluppo ha preso in carico la migrazione per questo servizio | -------------------------------------------------------------------------------------------------- | 
| [Da rifare] | [Non serve] | [Non serve] | mp00172   | pltm006    | master                          | migrazione/template_to_2.36 | https://bitbucket.springlab.enel.com/projects/GLGT-AP35622-MS-PLATFORM/repos/glgt-mp00172-lan-meoilcmptanalysis/browse  | 1dcb2278c4b28d377e67915db640f1081cde0f4e | https://bamboo.springlab.enel.com/browse/GLGTAP35622MSPLATFORM-GLGTMP00172DEVMEOILCMPTANALYSISAPPLANCUSTOMV1-270          | Da controllare se ci sono conflitti dal branch di sviluppo attuale       | -------------------------------------------------------------------------------------------------- | 
| [Rifatto]   | [Attendere] | [Attendere] | mp00172   | pltm006    | feature/DBOIL-0_project-startup | migrazione/template_to_2.36 | https://bitbucket.springlab.enel.com/projects/GLGT-AP35622-MS-PLATFORM/repos/glgt-mp00172-lan-meoilcmptanalysis/browse  | 8a3439b7dfa38bab9d6db3f87f7a0365c1a2d1d0 |                                                                                                                           | Nessun conflitto in data 20/11/2025                                      |                                                                                                    |

| Codice  | Nome               | Template | Versione template | Project      | Link Template Confluence                                                              | Link Template Git                                                                                          |
|---------|--------------------|----------|-------------------|--------------|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| bp00058 | booilcmptanalysis  | pltb030  | 1.17              | WORA         | https://confluence.springlab.enel.com/spaces/EPLTCSDTP/pages/766770720/pltb030+-+1.17 | https://bitbucket.springlab.enel.com/projects/GLIN-DL00001-MS-PLATFORM/repos/glin-pltb030-lan-tb030/browse |
| bp00182 | bogmi              | pltb030  | 1.17              | GMI Digital  | https://confluence.springlab.enel.com/spaces/EPLTCSDTP/pages/766770720/pltb030+-+1.17 | https://bitbucket.springlab.enel.com/projects/GLIN-DL00001-MS-PLATFORM/repos/glin-pltb030-lan-tb030/browse |
| bp00195 | bottoperations     | pltb030  | 1.17              | Task Tracker | https://confluence.springlab.enel.com/spaces/EPLTCSDTP/pages/766770720/pltb030+-+1.17 | https://bitbucket.springlab.enel.com/projects/GLIN-DL00001-MS-PLATFORM/repos/glin-pltb030-lan-tb030/browse |
| bp00199 | bottadministration | pltb030  | 1.17              | Task Tracker | https://confluence.springlab.enel.com/spaces/EPLTCSDTP/pages/766770720/pltb030+-+1.17 | https://bitbucket.springlab.enel.com/projects/GLIN-DL00001-MS-PLATFORM/repos/glin-pltb030-lan-tb030/browse |
| bp00200 | bottcontract       | pltb030  | 1.17              | Task Tracker | https://confluence.springlab.enel.com/spaces/EPLTCSDTP/pages/766770720/pltb030+-+1.17 | https://bitbucket.springlab.enel.com/projects/GLIN-DL00001-MS-PLATFORM/repos/glin-pltb030-lan-tb030/browse |
| bp00212 | boinstrmntmgmt     | pltb030  | 1.17              | WASP-GISA    | https://confluence.springlab.enel.com/spaces/EPLTCSDTP/pages/766770720/pltb030+-+1.17 | https://bitbucket.springlab.enel.com/projects/GLIN-DL00001-MS-PLATFORM/repos/glin-pltb030-lan-tb030/browse |
| mp00399 | megmiweb           | pltm003  | 3.33              | GMI Digital  | https://confluence.springlab.enel.com/spaces/EPLTCSDTP/pages/760514982/pltm003+-+3.33 | https://bitbucket.springlab.enel.com/projects/GLIN-DL00001-MS-PLATFORM/repos/glin-pltm003-lan-tm003/browse |
| mp00400 | megmiboroscopia    | pltm003  | 3.33              | GMI Digital  | https://confluence.springlab.enel.com/spaces/EPLTCSDTP/pages/760514982/pltm003+-+3.33 | https://bitbucket.springlab.enel.com/projects/GLIN-DL00001-MS-PLATFORM/repos/glin-pltm003-lan-tm003/browse |
| mp00443 | megmilogic         | pltm003  | 3.33              | GMI Digital  | https://confluence.springlab.enel.com/spaces/EPLTCSDTP/pages/760514982/pltm003+-+3.33 | https://bitbucket.springlab.enel.com/projects/GLIN-DL00001-MS-PLATFORM/repos/glin-pltm003-lan-tm003/browse |
| mp00489 | meargosintegration | pltm003  | 3.33              | Task Tracker | https://confluence.springlab.enel.com/spaces/EPLTCSDTP/pages/760514982/pltm003+-+3.33 | https://bitbucket.springlab.enel.com/projects/GLIN-DL00001-MS-PLATFORM/repos/glin-pltm003-lan-tm003/browse |
| mp00482 | meinstrumentation  | pltm003  | 3.33              | WASP-GISA    | https://confluence.springlab.enel.com/spaces/EPLTCSDTP/pages/760514982/pltm003+-+3.33 | https://bitbucket.springlab.enel.com/projects/GLIN-DL00001-MS-PLATFORM/repos/glin-pltm003-lan-tm003/browse |
| mp00453 | mettoperations     | pltm006  | 2.36              | Task Tracker | https://confluence.springlab.enel.com/spaces/EPLTCSDTP/pages/760522138/pltm006+-+2.36 | https://bitbucket.springlab.enel.com/projects/GLIN-DL00001-MS-PLATFORM/repos/glin-pltm006-lan-tm006/browse |
| mp00461 | mettcontract       | pltm006  | 2.36              | Task Tracker | https://confluence.springlab.enel.com/spaces/EPLTCSDTP/pages/760522138/pltm006+-+2.36 | https://bitbucket.springlab.enel.com/projects/GLIN-DL00001-MS-PLATFORM/repos/glin-pltm006-lan-tm006/browse |
| mp00462 | mettadminstration  | pltm006  | 2.36              | Task Tracker | https://confluence.springlab.enel.com/spaces/EPLTCSDTP/pages/760522138/pltm006+-+2.36 | https://bitbucket.springlab.enel.com/projects/GLIN-DL00001-MS-PLATFORM/repos/glin-pltm006-lan-tm006/browse |
| mp00172 | meoilcmptanalysis  | pltm006  | 2.36              | WORA         | https://confluence.springlab.enel.com/spaces/EPLTCSDTP/pages/760522138/pltm006+-+2.36 | https://bitbucket.springlab.enel.com/projects/GLIN-DL00001-MS-PLATFORM/repos/glin-pltm006-lan-tm006/browse |

## Note template
| Template | Versione template | Note                                                                                                          |
|----------|-------------------|---------------------------------------------------------------------------------------------------------------| 
| pltb030  | 1.17              |                                                                                                               |
| pltm003  | 3.33              | Il file data governance non è da inserire perché altrimenti la build si rompe nella fase: **platform update** |
| pltm006  | 2.36              |                                                                                                               |

## Link utili
|                               | Link                                                                                                                                    |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Link confluence migrazioni    | https://confluence.springlab.enel.com/spaces/EPLTCSDTP/pages/777136172/EDP-2025.05.SP0+-+Templates+-+Room+Release+Notes+-+Distributable |
| Link servizi                  | https://bitbucket.springlab.enel.com/projects/GLGT-AP35622-MS-PLATFORM                                                                  |
| Link template bitbucket       | https://bitbucket.springlab.enel.com/projects/GLIN-DL00001-MS-PLATFORM                                                                  |
| Tool per logs (1console-dev)  | https://glin-platform-1console-dev.enelint.global/                                                                                      |
| Tool per logs (1console-qa)   | https://glin-platform-1console-qa.enelint.global/                                                                                       |
| Tool per logs (1console-prod) | https://glin-platform-1console-prod.enelint.global/                                                                                     |

- OpenSearch: https://vpc-glgt-ap35622-dev-es-log1-bfslclko5pduqhbiyffmf3px5u.eu-central-1.es.amazonaws.com/_dashboards/app/data-explorer/discover#?_a=(discover:(columns:!(_source),isDirty:!f,sort:!()),metadata:(indexPattern:%2705c32470-9d0e-11eb-b505-5fb18dd26631%27,view:discover))&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_q=(filters:!((%27$state%27:(store:appState),meta:(alias:!n,disabled:!f,index:%2705c32470-9d0e-11eb-b505-5fb18dd26631%27,key:module-id,negate:!f,params:(query:mesaskpiperformance),type:phrase),query:(match_phrase:(module-id:mesaskpiperformance)))),query:(language:kuery,query:%27%27))

---

# 📘 **Guida Migrazione Template — Versione Markdown**

## Come iniziare

### **Impostare il template**

1. Consultare il file **Servizi enel.xlsx**.
2. Scegliere il servizio e, sulla stessa riga, vedere il valore corrispondente nella colonna **Template**.
3. Aprire il file **Versioni template prerelease.xlsx**.
4. Cercare la riga che, nel campo **Artifact**, ha il valore visto al punto 2.
5. Aprire il link Bitbucket presente nella colonna **Link**.
6. Clonare il progetto e allinearsi alla commit indicata nella colonna **Commit** (git checkout).

---

### **Impostare il servizio**
7. Copiare il valore del campo **Code** del servizio scelto (nel file Servizi enel.xlsx).
8. Collegarsi al repository Bitbucket delle piattaforme Enel: `https://bitbucket.springlab.enel.com/projects/GLGT-AP35622-MS-PLATFORM`
9. Cercare nel repo il valore copiato al punto 7 e aprire il progetto.
10. Confermare che nel nome del progetto compare il valore del campo **Name**.
11. Clonare il progetto in locale.
12. Fare checkout sull’ultima commit del **master**, quindi creare un branch: `migrazione/template_to_VERSION_TEMPLATE` dove VERSION = valore del campo *Current Release* (nel file Template versioni prerelease.xlsx).

---
### **Impostare l’attività**

13. Aprire WinMerge **solo** tramite:

    ```
    "c:\Program Files\WinMerge\WinMergeU.exe" /cfg Backup/EnableFile=0
    ```

    (evita la creazione dei .bak)
14. Come **1° file**, selezionare la cartella `repo_structure` del **template** (spunta *Sola lettura*).
15. Come **2° file**, selezionare la cartella del **servizio**.
16. Premere *Confronta* e iniziare a lavorare.

---

# 🧱 **Regole di Allineamento — Progetto**

## **Cartella root del progetto**

### `containers/`

* Deve essere **identica** al template.
* Se ci sono opzioni tipo `-Xms100m`, chiedere se mantenerle.

### `Hooks/` (dev/qa/prod)

* Di solito non si tocca.
* Valori diversi: controllare `.env`.
* I valori devono combaciare con:

    * `infrastructure/helm/values/values.yml`
    * `{{ValueComponent}}`, `{{sc}}`, `{{giasId}}`.

---

## **infrastructure/**

### `aws/`

* Non si tocca, dovrebbe essere identica.

### `helm/values.yml`

Controllare:

* Tutti i valori presenti nel template devono essere presenti anche nel servizio.
* I campi **in più** → si possono eliminare.
* I campi **in meno** → si aggiungono.
* Campi `events:`:

    * Se `enable: true` → lasciare (usa Kafka).
    * Se `false` → si può eliminare.
    * Conferma uso Kafka: controllare `platform/events/`

        * `events-published.json`
        * `events-subscribed.json`

### `values/dev.yaml`, `qa.yaml`, `prod.yaml`

* Risorse CPU/RAM devono avere request e limits.
* Se presente `logServerUrl`, **non toccarla**.
* `replicas:` non si tocca.
* `endpointOrchestrated:` non si tocca.

---

## **helm/templates/**

* `helpers.tpl` → **identico**

* `configmap-events.yaml` → **identico**

* `configmap-fluentbt.yaml` → **identico**

* `configmap.yaml` → **delicato**

    * Deve essere quasi identico.
    * Se trovi “events sidecar”, va **eliminato** (spostato in configmap-events).
    * Dopo data strutturale → tutto uguale.
    * `log4j` e `local_debug` devono esserci.
    * Variabili obsolete → eliminare.
    * Variabili diverse → controllare in:
        * `dev.yaml`
        * `qa.yaml`
        * `prod.yaml`
    * Regola sacra: *elimina o aggiungi solo se nei file dedicati esiste/non esiste la corrispondenza*.

* `deployment.yaml` → **identico**

* `hpa.yaml` → identico, tranne `apiVersion`

    * Se il servizio non ha `hpa.yaml`, togli `beta` → es: `v2beta2` → `v2`.

* `keda.yaml` → identico

* `service.yaml` → identico

---

## **platform/**

### `api/openapi.yaml`

* Non dovrebbe essere modificato.

### `publish_info.yaml`

* `{{ValueComponent}}` e `{{giasId}}` devono coincidere con quelli in Hooks.

### `catalog/`

* `metadata.yaml` → può cambiare.

    * La description va verificata (se c’è t.b.d. → chiedere).
* `metrics.yaml` → identico.
* `readme` → identici.
* `template/`

    * se manca → copiare.
    * se ci sono placeholder tipo `{{variabile}}` → inserirli.

---

## **tqs/**

* `portman/` non serve allinearlo.

---

## **File vari**

* `build.sh` → **identico al template (a cazzo duro)**.
* `automation_conf.yaml`

    * tutto identico
    * **template_version** deve riflettere il template usato.
* `.gitignore` → può cambiare solo il nome del package.

---

# 🧩 **src/**

* Se i package differiscono → serve refactor completo.
* `event-build-settings.xml` → uguale (a meno di info importanti).
* `readme` → uguale.
* `pom.xml`

    * controllare la sezione **required** (template e servizio devono combaciare).
* `resources/logback.yaml` → uguale.
* `resources/application.yaml`:

    * copiare la sezione **platform** dal template.
    * **endpointOrchestrated** → lasciare invariato.
    * Il resto → allineare al template.

---

# 🚀 Build & Push

1. Maven reload project.
2. `mvn clean`.
3. Eseguire `build_script.sh` → lancia `mvn clean verify` → **deve uscire build success**.
4. Commit:

   ```
   feat: migration template
   ```
5. Push sul branch.

---

# 📦 Deploy

1. Eseguire `mvn clean verify`.
2. Commit message: `feat:migration template`.
3. Su Bitbucket → sezione **Commit** → copiare l’ID della commit.
4. Andare su **Builds**.
5. Aprire la build recente → si finisce su **Bamboo**.
6. In alto a destra → **Run > Run customized…**
7. Nel campo **Revision** incollare la commit.

### Due scenari:
#### **8.1. Compare PIPELINE_TYPE**
* Impostarlo a `full`.
* Run.

#### **8.2. PIPELINE_TYPE non c’è**
* Run → fallirà.
* Ritornare al punto 4 → ora comparirà (torna allo scenario 8.1).

---

### Dopo la build

10. Aprire OpenSearch: *(link lungo evitato, tanto ce l’hai già)*
11. Login con AzureID → Discover → filtro:

* Field: `module-id`
* Operator: `is`
* Value: *nome del servizio*

12. Controllare assenza errori/exceptions relativi alla build.
13. Se tutto ok → merge su **master** e rifare build come allo scenario 8.1.

---
