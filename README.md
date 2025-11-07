# Hackathon IBM

Stack Docker Compose pour RAG pour le Pôle Léonard de Vinci avec intégration IBM watsonx.ai via LiteLLM.

## Architecture

- **Open WebUI** : Interface utilisateur web (port 3000)
- **PostgreSQL** : Base de données principale
- **Redis** : Cache et gestion WebSocket
- **Qdrant** : Base de données vectorielle
- **LiteLLM** : Proxy OpenAI-compatible pour IBM watsonx.ai
- **Docling** : Service de traitement et conversion de documents (PDF, DOCX, PPTX, etc.)

## Configuration

### Variables watsonx.ai à modifier

**IMPORTANT** : Avant de lancer la stack, vous devez modifier les variables IBM watsonx.ai dans le fichier [docker-compose.yml](docker-compose.yml) (lignes 46-49) :

```yaml
environment:
  WATSONX_URL: "https://eu-de.ml.cloud.ibm.com"
  WATSONX_APIKEY: "VOTRE_CLÉ_API"
  WATSONX_API_KEY: "VOTRE_CLÉ_API"
  WATSONX_PROJECT_ID: "VOTRE_PROJECT_ID"
```

Remplacez :
- `WATSONX_APIKEY` et `WATSONX_API_KEY` : Votre clé API IBM Cloud
- `WATSONX_PROJECT_ID` : L'ID de votre projet watsonx.ai
- `WATSONX_URL` : L'URL de votre région (par défaut : eu-de)

## Lancement de la stack

### Prérequis

- Docker
- Docker Compose

### Démarrage

1. Cloner le repository :
```bash
git clone <url-du-repo>
cd hackathon-openwebui
```

2. Modifier les variables watsonx.ai dans [docker-compose.yml](docker-compose.yml)

3. Lancer la stack :
```bash
docker-compose up -d
```

4. Vérifier que tous les services sont démarrés :
```bash
docker-compose ps
```

5. Accéder à l'interface :
```
http://localhost:3000
```

### Arrêt

```bash
docker-compose down
```

### Arrêt avec suppression des volumes

```bash
docker-compose down -v
```

## Ports utilisés

- **3000** : Open WebUI
- **5432** : PostgreSQL
- **6379** : Redis
- **6333** : Qdrant API
- **6334** : Qdrant gRPC
- **4000** : LiteLLM
- **5001** : Docling API

## Logs

Pour consulter les logs d'un service :

```bash
docker-compose logs -f <service>
```

Exemples :
```bash
docker-compose logs -f openwebui
docker-compose logs -f litellm
docker-compose logs -f docling
```

## Volumes

Les données persistantes sont stockées dans les volumes Docker suivants :
- `openwebui_data` : Données Open WebUI
- `pg_data` : Base de données PostgreSQL
- `redis_data` : Données Redis
- `qdrant_data` : Base de données vectorielle Qdrant

## Services et APIs

### Docling - Traitement de documents

Docling est un service de conversion et de traitement de documents qui prend en charge :

- **Formats supportés** : PDF, DOCX, PPTX, HTML, Images
- **Fonctionnalités** : Extraction de texte, extraction de tableaux, OCR
- **API** : <http://localhost:5001>
- **Documentation** : <http://localhost:5001/docs>
- **Interface UI** : <http://localhost:5001/ui>

Le service Docling est automatiquement lié à Open WebUI via la variable d'environnement `DOCLING_API_URL`.

