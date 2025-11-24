# **Nexus Risk Engine 🧠**

**Microservicio de evaluación de riesgo crediticio de alto rendimiento. Actúa como el "cerebro" analítico de la plataforma Nexus Finance.**

## **📖 Descripción**

Este servicio es **Stateless** (sin estado) y está diseñado para recibir perfiles financieros, aplicar reglas heurísticas avanzadas (simulando modelos de Machine Learning) y retornar una decisión de crédito en milisegundos.

Se comunica con el **Backend Core (Java)** mediante una API REST, desacoplando la lógica de negocio transaccional de la lógica analítica.

## **🏗️ Arquitectura (Clean Architecture)**

Adaptamos los principios de arquitectura limpia al ecosistema Python:

app/  
├── api/ \# Capa de Interfaz (Controladores REST)  
├── services/ \# Lógica de Negocio (Algoritmos de Scoring)  
├── schemas/ \# DTOs y Validación de Datos (Pydantic)  
└── core/ \# Configuración e Infraestructura

## **🛠️ Stack Tecnológico**

| Componente        | Tecnología            | Versión  | Razón de Uso                                              |
| :---------------- | :-------------------- | :------- | :-------------------------------------------------------- |
| **Lenguaje**      | Python                | **3.12** | Última versión estable con mejoras de velocidad.          |
| **API Framework** | FastAPI               | 0.115+   | Validación automática y performance asíncrono.            |
| **Servidor**      | Uvicorn               | Standard | Servidor ASGI para producción.                            |
| **Validación**    | Pydantic V2           | 2.5+     | Validación de esquemas de datos ultra-rápida (Rust core). |
| **Cálculo**       | Pandas / Scikit-learn | 2.x      | Procesamiento numérico y modelos predictivos.             |

## **⚙️ Capacidades del Motor**

### **Endpoint: POST /api/v1/evaluate-risk**

Analiza variables como:

- **Relación Deuda/Ingreso (DTI):** Calcula la capacidad de pago real.
- **Edad y Estabilidad:** Ponderación demográfica.
- **Historial simulado:** Reglas de penalización por comportamiento.

**Respuesta Generada:**

- score: Puntaje numérico (300-850).
- risk_level: Clasificación (LOW, MEDIUM, HIGH).
- is_approved: Decisión booleana final.
- suggested_interest_rate: Tasa dinámica basada en el riesgo.
- max_approved_amount: Límite de crédito sugerido.

## **🚀 Ejecución**

### **Docker (Recomendado)**

Este servicio se levanta automáticamente mediante el orquestador principal del proyecto.

```bash# Puerto externo mapeado
http://localhost:8000
```

### **Documentación Automática**

FastAPI genera documentación interactiva automáticamente:

- 👉 **Swagger/OpenAPI:** [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)
- 👉 **ReDoc:** [http://localhost:8000/redoc](https://www.google.com/search?q=http://localhost:8000/redoc)

## **👤 Autor**

**Angel Antonio Cancho Corilla** \- _Software Engineer_
