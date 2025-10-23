# 📊 Progress Tracker - AWS + FastAPI Learning Journey

**Fecha de inicio:** 24 de Octubre, 2025  
**Ultima actualizacion:** 24 de Octubre, 2025 - 01:45 AM  
**Plataforma:** Windows 11 + CMD

---

## 🎯 Estado Actual

**📍 SEMANA 1 - DAY 1: FastAPI + S3 Setup**  
**Progreso:** 50% completado  
**Tiempo invertido hoy:** ~1.5 horas  
**Proximo paso:** Completar Prompt 5 (Tests) y Prompt 6 (README)

---

## ✅ Completado Hoy - 24 Octubre 2025

### Setup Inicial
- ✅ Repositorio GitHub creado: `aws-fastapi-learning`
- ✅ Estructura de carpetas completa
- ✅ Git inicializado y primer commit
- ✅ Claude Code CLI instalado y configurado
- ✅ API Key de Anthropic configurada

### Week 01 - Day 1: FastAPI + S3 Upload API (50% done)

#### Archivos creados:
- ✅ `main.py` - FastAPI app con 3 endpoints
  - GET `/` - Root endpoint con info de la API
  - GET `/health` - Health check
  - POST `/upload` - Upload de archivos a S3 (pendiente AWS config)
- ✅ `requirements.txt` - Dependencias completas
- ✅ `.env.example` - Template de variables de entorno
- ✅ `venv/` - Virtual environment configurado
- ✅ App corriendo localmente en `http://localhost:8000`

#### Prompts completados con Claude Code CLI:
- ✅ **Prompt 1:** FastAPI basico con endpoints `/` y `/health`
- ✅ **Prompt 2:** requirements.txt con dependencias
- ✅ **Prompt 3:** Endpoint POST `/upload` para S3
- ✅ **Prompt 4:** .env.example creado

#### Problemas resueltos:
- ✅ Error de encoding UTF-8 (usar solo ASCII en codigo)
- ✅ Permisos de PowerShell (cambiado a CMD)
- ✅ FastAPI corriendo sin errores

---

## ⏸️ PAUSADO AQUI - Checkpoint para manana

**Ultimo comando ejecutado:**
```cmd
uvicorn main:app --reload
# App funcionando correctamente en http://localhost:8000
```

**Estado del codigo:**
- ✅ FastAPI funcionando
- ✅ Swagger UI disponible en `/docs`
- ⚠️ Tests pendientes
- ⚠️ README del day1 pendiente
- ⚠️ AWS no configurado aun (esperado)

---

## 📋 Siguiente Sesion - Checklist Completo

### Para retomar manana (25 Octubre):

#### 1. Abrir el proyecto
```cmd
REM Navega al proyecto
cd C:\Users\juanm\Documents\GitHub\aws-fastapi-learning\week01-fundamentals\day1-iam-s3

REM Activa el entorno virtual
venv\Scripts\activate.bat

REM Verifica que todo este OK
python --version
pip list
```

#### 2. Inicia Claude Code CLI
```cmd
claude
```

---

## 🎯 Prompts Pendientes

### ⬜ Prompt 5: Tests (PENDIENTE - 10 minutos)
```
Crea tests/test_main.py con pytest que pruebe:
- El endpoint /health
- El endpoint / (info)
- Mock del endpoint /upload usando pytest-mock (sin conectarse realmente a S3)
- Usa pytest, httpx y pytest-mock
- NO uses tildes ni caracteres especiales
```

**Despues de crear los tests:**
```cmd
REM Actualiza requirements.txt si es necesario
pip install pytest httpx pytest-mock

REM Ejecuta los tests
pytest tests/ -v

REM Deberias ver:
REM tests/test_main.py::test_health PASSED
REM tests/test_main.py::test_root PASSED  
REM tests/test_main.py::test_upload_mock PASSED
```

---

### ⬜ Prompt 6: README del Day 1 (PENDIENTE - 5 minutos)
```
Crea un README.md en la carpeta week01-fundamentals/day1-iam-s3/ que explique:
- Titulo: Day 1 - FastAPI + S3 Upload API
- Descripcion breve del proyecto
- Requisitos previos (Python 3.11+, cuenta AWS pendiente)
- Instalacion paso a paso para Windows usando CMD
- Como configurar las variables de entorno
- Como correr la aplicacion con uvicorn
- Como correr los tests con pytest
- Endpoints disponibles con ejemplos
- Estructura de archivos del proyecto
- Proximos pasos (AWS setup)
- NO uses tildes ni caracteres especiales
```

---

### ⬜ Commit y Push (PENDIENTE - 2 minutos)
```cmd
REM Desactiva el venv primero
deactivate

REM Ve a la raiz del proyecto
cd C:\Users\juanm\Documents\GitHub\aws-fastapi-learning

REM Añade todos los cambios
git add .

REM Verifica el status
git status

REM Commit
git commit -m "feat(week01-day1): Add tests and documentation - Day 1 complete"

REM Push a GitHub
git push origin main
```

---

## 🚀 Despues de completar Day 1 (100%)

### Day 2: AWS Setup (Estimado: 30-40 minutos)

#### Tareas principales:
- [ ] **Crear cuenta AWS Free Tier**
  - Ir a: https://aws.amazon.com/free/
  - Registro completo
  - Verificacion de tarjeta (no se cobra)
  - Configurar billing alerts ($5, $10, $20)

- [ ] **Configurar IAM User**
  - Crear usuario IAM para desarrollo
  - Asignar politica: `AmazonS3FullAccess`
  - Crear Access Keys (Access Key ID + Secret Access Key)
  - Guardar credenciales de forma segura

- [ ] **Instalar y configurar AWS CLI**
  ```cmd
  REM Descargar AWS CLI v2 para Windows
  REM https://aws.amazon.com/cli/
  
  REM Configurar
  aws configure
  REM Ingresa: Access Key ID, Secret Access Key, Region (us-east-1)
  
  REM Verificar
  aws s3 ls
  ```

- [ ] **Crear Bucket S3**
  ```cmd
  REM Via AWS CLI
  aws s3 mb s3://fastapi-learning-[tu-nombre-unico]
  
  REM O via Console: https://s3.console.aws.amazon.com/
  ```

- [ ] **Configurar .env con credenciales reales**
  ```cmd
  copy .env.example .env
  notepad .env
  
  REM Completa con tus valores reales:
  REM AWS_ACCESS_KEY_ID=AKIAXXXXXXXXXXXXXXXX
  REM AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  REM AWS_REGION=us-east-1
  REM S3_BUCKET_NAME=fastapi-learning-tu-nombre
  ```

- [ ] **Probar upload real a S3**
  ```cmd
  REM Corre la app
  uvicorn main:app --reload
  
  REM Ve a http://localhost:8000/docs
  REM Prueba el endpoint POST /upload con un archivo pequeño
  REM Verifica en AWS S3 Console que el archivo se subio
  ```

- [ ] **Commit y push**
  ```cmd
  git add .
  git commit -m "feat(week01-day2): AWS S3 integration working - Day 2 complete"
  git push origin main
  ```

---

### Day 3: Ampliar la API (Estimado: 1 hora)

- [ ] Endpoint GET `/files` - Listar archivos en S3
- [ ] Endpoint DELETE `/files/{filename}` - Eliminar archivo
- [ ] Endpoint GET `/files/{filename}/download` - Presigned URL para descarga
- [ ] Actualizar tests para nuevos endpoints
- [ ] Actualizar README con nuevos endpoints
- [ ] Deploy opcional en EC2 (si quieres avanzar)

---

## 📈 Estadisticas de Progreso

### General
- **Semanas completadas:** 0 / 12
- **Dias completados:** 0.5 / 84 (0.6%)
- **Proyectos completados:** 0 / 4
- **Lineas de codigo:** ~150
- **Commits totales:** 3

### Week 1 Progress
- **Day 1:** 50% ✅ (en progreso)
- **Day 2:** 0% ⬜
- **Day 3:** 0% ⬜
- **Weekend Project:** 0% ⬜

---

## 💡 Notas y Aprendizajes

### Session 1 - 24 Octubre 2025

#### ✅ Logros
- Setup inicial completado sin problemas mayores
- FastAPI funcionando localmente con Swagger UI
- Estructura de proyecto bien organizada
- Claude Code CLI configurado correctamente

#### ⚠️ Problemas encontrados y resueltos
1. **Encoding UTF-8**
   - Problema: SyntaxError con caracteres especiales
   - Solucion: Usar solo ASCII en codigo, guardar archivos como UTF-8
   
2. **PowerShell permisos**
   - Problema: Restricciones de ejecucion en PowerShell
   - Solucion: Cambiar a CMD para todos los comandos

#### 💡 Tips aprendidos
- Swagger UI en `/docs` es excelente para probar endpoints
- Claude Code CLI funciona mejor con prompts especificos y sin tildes
- Importante activar venv antes de trabajar
- Git commit frecuente es buena practica

#### 🎯 Para mejorar
- Leer documentacion de FastAPI sobre async/await
- Revisar buenas practicas de manejo de errores
- Aprender mas sobre testing con pytest

---

## 🔗 Links Utiles

### Proyecto
- **GitHub Repo:** https://github.com/juanm/aws-fastapi-learning
- **Progreso detallado:** Este archivo (PROGRESS.md)
- **README principal:** ../README.md

### AWS
- **AWS Console:** https://console.aws.amazon.com/
- **S3 Console:** https://s3.console.aws.amazon.com/
- **IAM Console:** https://console.aws.amazon.com/iam/
- **Free Tier:** https://aws.amazon.com/free/

### Desarrollo
- **FastAPI Docs:** https://fastapi.tiangolo.com/
- **Anthropic Console:** https://console.anthropic.com/
- **Python Docs:** https://docs.python.org/3/

### Aprendizaje
- **AWS Skill Builder:** https://skillbuilder.aws/
- **FastAPI Tutorial:** https://fastapi.tiangolo.com/tutorial/

---

## 🎯 Objetivos a Largo Plazo

### Semana 12 (Enero 2026)
- [ ] Completar las 12 semanas del curso
- [ ] 4 proyectos completos en portfolio
- [ ] Certificacion AWS Solutions Architect Associate
- [ ] 50+ commits en GitHub
- [ ] LinkedIn actualizado con proyectos
- [ ] Preparado para entrevistas tecnicas

### Proximos hitos
- **Semana 1:** Fundamentos (IAM, S3, EC2)
- **Semana 4:** Primer proyecto de Data Engineering
- **Semana 7:** Primer proyecto de ML
- **Semana 12:** Certificacion + Portfolio completo

---

## 📅 Calendario de Sesiones

| Fecha | Sesion | Duracion | Completado |
|-------|--------|----------|------------|
| 24 Oct 2025 | Day 1 Setup | 1.5h | 50% ✅ |
| 25 Oct 2025 | Day 1 Finish + Day 2 | 1-2h | Pendiente ⬜ |
| 26 Oct 2025 | Day 3 | 1h | Pendiente ⬜ |

---

**Proxima sesion:** 25 Octubre 2025  
**Objetivo:** Completar Day 1 (tests + docs) e iniciar AWS setup

**Recordatorio:** Actualizar este archivo despues de cada sesion con:
- Logros del dia
- Problemas encontrados
- Tiempo invertido
- Proximo objetivo

---

**🔥 Motivacion diaria:**  
"Cada dia de practica te acerca mas a ser un experto en AWS + FastAPI. Keep going!"

---

*Ultima sesion: 24 Oct 2025 - 01:45 AM*  
*Tiempo total invertido: 1.5 horas*  
*Siguiente paso: Completar tests y README del Day 1*