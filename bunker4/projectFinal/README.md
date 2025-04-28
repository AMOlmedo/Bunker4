# 🛠️ TP SRE/DevOps: “bunker4 Público en Docker Swarm”

## 🎯 Objetivo general
Desplegar públicamente un sistema con **Frontend React + Backend Python + Base de datos**, gestionado con **Ansible**, desplegado vía **GitHub Actions** en un **cluster Docker Swarm**, y monitoreado con **Prometheus + Grafana**.  

---

## 📦 Tecnologías mínimas a incluir
- **DEVOPS**:  ≥ 2 containers Docker (Front + Back + DB)  
- **Configuration Mgmt**: Ansible 
- **CI/CD**: GitHub Actions (o Jenkins)  
- **SRE**: Docker Swarm cluster + Prometheus + Grafana  
- **Licencia**: GPL, BSD o Creative Commons

---

## 🗺️ Hoja de Ruta

| Fase                            | Duración  | Entregable clave                                              |
|---------------------------------|-----------|----------------------------------------------------------------|
| 1. Planificación & preparación  | 1 día     | `README.md` con alcance, tech stack, diagrama ASCII            |
| 2. Infraestructura básica       | 2 días    | VPS o LXD/Proxmox provisionado vía Ansible (playbook)          |
| 3. Contenerización              | 3 días    |  
  - `Dockerfile` para **backend** (Python + Flask/Django)  
  - `Dockerfile` para **frontend** (React)  
  - `docker-compose.yml` local de prueba  
| 4. Cluster Swarm & CM           | 2–3 días  |  
  - Playbook Ansible que:  
    1. Instala Docker en N nodos (manager + workers)  
    2. Inicializa Swarm y une workers  
    3. Despliega stack Swarm con `docker stack deploy`  
| 5. CI/CD con GitHub Actions     | 2 días    | Workflow que:  
  1. Construye y taggea imágenes (front/back)  
  2. Pushea a Docker Hub (o registro propio)  
  3. Conecta por SSH al manager y actualiza stack Swarm  
| 6. Base de datos                | 1–2 días  |  
  - Servicio DB (PostgreSQL/MySQL) en Swarm  
  - Persistencia de volúmenes  
| 7. Monitoreo & alertas          | 2 días    |  
  - Prometheus scrapea servicios Swarm  
  - Grafana con dashboard UP/DOWN y latencia  
  - Alertmanager notifica (mail o webhook)  
| 8. Pruebas de resiliencia       | 1 día     | Chaos simple:  
  - Apagar un worker y verificar autosaneado  
  - Rotación de contenedores sin downtime  
| 9. Documentación final & licencia | 1 día   |  
  - `README.md` completo con pasos de deploy  
  - Licencia libre (GPL/BSD/CC) en `LICENSE`  
  - Capturas `/screenshots` de demo y alertas  

---

## 🔧 Detalle de pasos principales

### 1. Planificación & README
- Definí tu VPS o contenedor LXD/Proxmox en la nube (p.ej. DigitalOcean, Hetzner)  
- Esquematizá:

