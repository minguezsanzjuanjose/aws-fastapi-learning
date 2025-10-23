# 🚀 AWS + FastAPI Learning Journey - 12 Semanas

Plan intensivo para dominar AWS con **FastAPI** enfocado en **Data Engineering**, **Machine Learning** y **APIs Modernas**.

## 🎯 Objetivos

- ✅ Dominar AWS con FastAPI como framework principal
- ✅ Crear portfolio con 4 proyectos API demostrables
- ✅ Obtener certificacion AWS Solutions Architect Associate
- ✅ Desarrollar skills en IaC, CI/CD, MLOps y GenAI
- ✅ Estar preparado para entrevistas tecnicas AWS + Python

## 📚 Estructura del Proyecto

```
aws-fastapi-learning/
├── week01-fundamentals/         # IAM, S3, EC2, VPC + FastAPI basico
├── week02-serverless/           # Lambda, API Gateway, DynamoDB
├── week03-containers/           # ECS, RDS, Docker + FastAPI production
├── week04-data-ingestion/       # Data Lake APIs, S3, Glue, Athena
├── week05-streaming/            # Kinesis, real-time APIs, WebSockets
├── week06-orchestration/        # Step Functions, EventBridge
├── week07-ml-training/          # SageMaker + FastAPI ML APIs
├── week08-ml-serving/           # Model serving, predictions API
├── week09-genai/                # Bedrock, RAG, GenAI APIs
├── week10-iac/                  # CDK, CloudFormation, Terraform
├── week11-cicd/                 # CodePipeline, monitoring, security
├── week12-portfolio/            # Proyectos finales production-ready
├── projects/                    # 4 proyectos principales
│   ├── project1-ecommerce-api/
│   ├── project2-analytics-api/
│   ├── project3-ml-platform/
│   └── project4-genai-rag/
├── scripts/                     # Scripts utiles y setup
├── PROGRESS.md                  # Tracking de progreso
└── README.md                    # Este archivo
```

## 📊 Progreso General

### FASE 1: Fundamentos AWS + FastAPI (Semanas 1-3)
- [🟡] **Semana 1:** IAM, S3, EC2 + FastAPI CRUD con S3 (EN PROGRESO)
  - [🟡] Day 1: Setup + FastAPI basico (50%)
  - [⬜] Day 2: AWS Setup (IAM + S3)
  - [⬜] Day 3: EC2 Deploy
- [⬜] **Semana 2:** Lambda, API Gateway, DynamoDB + Serverless FastAPI
- [⬜] **Semana 3:** VPC, RDS, ECS + FastAPI containerizado
- [⬜] **Proyecto 1:** E-Commerce API 3-tier

### FASE 2: Data Engineering APIs (Semanas 4-6)
- [⬜] **Semana 4:** Data Lake, Glue, Athena + Ingestion API
- [⬜] **Semana 5:** Kinesis, Streaming + Real-time Analytics API
- [⬜] **Semana 6:** Step Functions, EventBridge + Orchestration API
- [⬜] **Proyecto 2:** Real-time Data Pipeline API

### FASE 3: Machine Learning APIs (Semanas 7-9)
- [⬜] **Semana 7:** SageMaker Training + ML Orchestration API
- [⬜] **Semana 8:** SageMaker Endpoints + Predictions API
- [⬜] **Semana 9:** Bedrock, RAG + GenAI Assistant API
- [⬜] **Proyecto 3:** ML Platform API End-to-End
- [⬜] **Proyecto 4:** GenAI RAG Application

### FASE 4: DevOps & Production (Semanas 10-12)
- [⬜] **Semana 10:** IaC (CDK, CloudFormation, Terraform)
- [⬜] **Semana 11:** CI/CD, Monitoring, Security, Secrets
- [⬜] **Semana 12:** Portfolio profesional + Certificacion

## 🛠️ Stack Tecnologico

### Core Technologies
- **Framework:** FastAPI 0.104+ (Python 3.11+)
- **ASGI Server:** Uvicorn
- **ORM:** SQLAlchemy 2.0
- **Validation:** Pydantic v2
- **Testing:** Pytest + httpx
- **Async:** asyncio, aiohttp

### AWS Services por Categoria

#### Compute & Containers
- **EC2:** Hosting tradicional
- **Lambda:** Serverless functions (con Mangum para FastAPI)
- **ECS Fargate:** Container orchestration
- **API Gateway:** REST & WebSocket APIs

#### Storage & Databases
- **S3:** Object storage, Data Lakes
- **RDS:** PostgreSQL (SQLAlchemy)
- **DynamoDB:** NoSQL, high-performance
- **ElastiCache:** Redis para caching

#### Data Engineering
- **Kinesis Data Streams:** Real-time ingestion
- **Kinesis Firehose:** Delivery a S3/Redshift
- **Glue:** ETL jobs, Data Catalog
- **Athena:** SQL queries sobre S3
- **EMR:** Big data processing (Spark)
- **Step Functions:** Workflow orchestration

#### Machine Learning & AI
- **SageMaker:** Training, tuning, endpoints
- **SageMaker Pipelines:** MLOps automation
- **Feature Store:** Feature management
- **Model Monitor:** Drift detection
- **Bedrock:** Claude, Llama, GenAI models
- **Knowledge Bases:** RAG implementation

#### DevOps & Security
- **CDK (Python):** Infrastructure as Code
- **CloudFormation:** IaC templates
- **CodePipeline:** CI/CD orchestration
- **CodeBuild:** Build automation
- **Secrets Manager:** Credentials management
- **KMS:** Encryption keys
- **Cognito:** User authentication
- **WAF:** API protection
- **CloudWatch:** Logs, metrics, alarms
- **X-Ray:** Distributed tracing

## 💰 Control de Costos

- **Presupuesto estimado:** $50-80 para 12 semanas
- **Billing alerts:** $5, $10, $20, $50
- **Estrategia de ahorro:**
  - ✅ Maximo uso de Free Tier
  - ✅ Spot Instances para training y EMR
  - ✅ Destruir recursos despues de cada practica
  - ✅ Lambda over EC2 cuando sea posible
  - ✅ ECS Fargate Spot pricing
  - ✅ S3 Intelligent Tiering
  - ✅ Review semanal de costos

## 🏆 Los 4 Proyectos del Portfolio

### Proyecto 1: E-Commerce API (3-tier Architecture)
**Duracion:** Semana 3  
**Stack:** VPC + ALB + ECS Fargate + RDS PostgreSQL + S3 + CloudFront  
**FastAPI Features:**
- Authentication JWT + refresh tokens
- CRUD completo (productos, usuarios, ordenes)
- Upload de imagenes a S3 con presigned URLs
- Paginacion, filtros, busqueda
- Background tasks con Celery + Redis
- Rate limiting por usuario
- Documentacion OpenAPI interactiva

**Skills:** Alta disponibilidad, Auto Scaling, Multi-AZ, CDN, Security Groups

---

### Proyecto 2: Real-time Analytics API
**Duracion:** Semana 6  
**Stack:** API Gateway + Lambda + Kinesis + DynamoDB + Athena + S3  
**FastAPI Features:**
- WebSockets para eventos real-time
- Async endpoints para ingesta masiva
- Streaming data con Server-Sent Events (SSE)
- Queries on-demand a Athena
- Metrics dashboard
- Event-driven architecture

**Skills:** Serverless, Event streaming, Real-time processing, Data Lake queries

---

### Proyecto 3: ML Platform API
**Duracion:** Semana 8  
**Stack:** ECS + SageMaker + S3 + RDS + ElastiCache Redis  
**FastAPI Features:**
- Endpoints para trigger training jobs
- Hyperparameter tuning orchestration
- Model versioning y registry
- Predictions API con caching inteligente
- A/B testing de modelos
- Model performance monitoring
- Batch predictions

**Skills:** MLOps, Model serving, Caching strategies, A/B testing, Monitoring

---

### Proyecto 4: GenAI Assistant API (RAG)
**Duracion:** Semana 9  
**Stack:** Lambda + Bedrock + Knowledge Base + S3 + API Gateway + Cognito  
**FastAPI Features:**
- Chat API con streaming responses
- Document upload y vectorizacion automatica
- Context-aware conversations
- Multi-tenancy (usuarios aislados)
- Conversation history en DynamoDB
- Rate limiting por usuario
- Token counting y cost tracking

**Skills:** GenAI, RAG architecture, Vector embeddings, Streaming, Multi-tenancy

## 📖 Recursos de Aprendizaje

### Documentacion Oficial
- [AWS Documentation](https://docs.aws.amazon.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [AWS Free Tier](https://aws.amazon.com/free/)
- [AWS Skill Builder](https://skillbuilder.aws/)

### Cursos y Tutoriales
- AWS Solutions Architect Associate (Stephane Maarek - Udemy)
- FastAPI - The Complete Course (Udemy)
- AWS Well-Architected Framework
- [Real Python - FastAPI](https://realpython.com/fastapi-python-web-apis/)

### Comunidades
- [r/aws](https://reddit.com/r/aws)
- [FastAPI Discord](https://discord.gg/fastapi)
- AWS Community Builders
- [Python Discord](https://discord.gg/python)

## 📅 Timeline y Compromiso

- **Inicio:** 24 Octubre 2025
- **Finalizacion:** Enero 2026
- **Tiempo diario:** 1-2 horas (7-14 horas/semana)
- **Revision semanal:** Domingos
- **Check-in mensual:** Revisar progreso y ajustar

## 🎓 Certificacion Objetivo

**AWS Certified Solutions Architect - Associate (SAA-C03)**
- **Duracion:** 130 minutos
- **Preguntas:** 65 (multiple choice)
- **Passing score:** 720/1000
- **Costo:** $150 USD
- **Preparacion:** Ultimas 2 semanas + Semana 12

## 📏 Reglas de Oro

1. **🔥 Codigo todos los dias** - Aunque sea 30 minutos
2. **📝 Documentar todo** - README en cada ejercicio
3. **💸 Destruir recursos** - Checklist despues de cada sesion
4. **🧪 Testing obligatorio** - Pytest para cada endpoint
5. **🏗️ Diagramas de arquitectura** - Visualizar antes de codear
6. **🚀 Deploy early, deploy often** - Ver errores reales
7. **📊 Consistencia > Intensidad** - Mejor 1h diaria que maratones

## ✅ Metricas de Exito

### Portfolio
- [⬜] 4 proyectos completos en GitHub con documentacion profesional
- [⬜] Diagramas de arquitectura de cada proyecto
- [⬜] README profesionales con screenshots
- [⬜] Tests con >80% coverage en proyectos principales

### Skills Tecnicas
- [⬜] Certificacion AWS Solutions Architect Associate obtenida
- [⬜] 50+ commits en GitHub durante las 12 semanas
- [⬜] Dominio de FastAPI (async, WebSockets, background tasks)
- [⬜] Experiencia con IaC (CDK o Terraform)

### Preparacion Profesional
- [⬜] LinkedIn actualizado con proyectos y skills
- [⬜] Portfolio website desplegado (puede ser en S3 + CloudFront)
- [⬜] 3 proyectos demostrables en video (< 5 min c/u)
- [⬜] Preparado para entrevistas tecnicas AWS + Python

### Networking
- [⬜] Conectar con 10+ profesionales AWS en LinkedIn
- [⬜] Participar en 1 meetup/webinar AWS
- [⬜] Publicar 1 articulo tecnico en Medium/Dev.to

## 🎯 Primera Semana - Quick Start

### Week 1 - Day 1: Setup (24 Oct 2025)
- [✅] Crear repositorio GitHub
- [✅] Setup estructura de proyecto
- [✅] Instalar Claude Code CLI
- [✅] Crear primera FastAPI app
- [🟡] Tests y documentacion (50% done)

### Week 1 - Day 2: AWS Fundamentals
- Crear cuenta AWS Free Tier
- Configurar IAM users, roles, policies
- Crear bucket S3
- Probar upload real desde FastAPI

### Week 1 - Day 3: EC2 Deploy
- Launch EC2 instance
- Deploy FastAPI con Nginx + Uvicorn
- Security groups configuration
- Domain setup (opcional)

### Week 1 - Weekend: Mini Proyecto
- API completa de file management
- Tests con >80% coverage
- Documentacion profesional
- Deploy en EC2

## 🚨 Control de Costos - Checklist Diario

```bash
# Corre este script al final de cada sesion
./scripts/cleanup.sh

# Checklist manual:
□ Lambda functions eliminadas
□ EC2 instances stopped/terminated
□ RDS instances deleted (si no es proyecto principal)
□ ECS tasks stopped
□ S3 buckets vaciados (o con lifecycle policies)
□ CloudWatch logs con retention policy
```

## 📞 Comunidad y Soporte

**GitHub:** [tu-usuario]/aws-fastapi-learning  
**LinkedIn:** [Tu perfil]  
**Email:** [tu@email.com]

---

**🔥 Motivacion:** "Cada linea de codigo es un paso hacia convertirte en un AWS + Python engineer que las empresas buscan activamente."

**🎯 Meta Final:** Portfolio de 4 proyectos production-ready que demuestren expertise en AWS, FastAPI, Data Engineering, ML y GenAI.

---

*Ultima actualizacion: 24 Octubre 2025*  
*Stack principal: FastAPI + AWS + Python 3.11+*  
*Objetivo: AWS Solutions Architect Associate + Portfolio profesional*

## 📊 Estadisticas Actuales

- **Dias completados:** 0.5 / 84
- **Semanas completadas:** 0 / 12  
- **Proyectos completados:** 0 / 4
- **Tiempo invertido:** ~1.5 horas
- **Commits totales:** 3+

---

**Ver progreso detallado:** [PROGRESS.md](./PROGRESS.md)