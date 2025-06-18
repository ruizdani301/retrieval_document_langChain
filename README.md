
# 🧠 Búsqueda Semántica en PDFs con LangChain y Google Generative AI

Este proyecto realiza una búsqueda semántica en un documento PDF utilizando **LangChain**, **Google Generative AI Embeddings**, y un **almacenamiento de vectores en memoria** (`InMemoryVectorStore`).

## 🚀 ¿Qué hace este script?

1. Carga todas las páginas de un archivo PDF.
2. Convierte cada página en un documento para análisis semántico.
3. Usa embeddings del modelo de Google `gemini-embedding-exp-03-07`.
4. Realiza una búsqueda semántica de la consulta: `"SQS or EventBridge"`.
5. Imprime el fragmento más relevante encontrado.

---

## 🛠️ Requisitos

- Python 3.9+
- Una clave de API de Google Generative AI
- LangChain y los siguientes paquetes instalados:

```bash
pip install langchain langchain-google-genai langchain-community

Agrega tu API key como variable de entorno en el script o en tu terminal:
export GOOGLE_API_KEY="tu-clave-de-api"

Coloca tu archivo PDF en la misma carpeta del script y renómbralo como texto.pdf (o cambia el nombre del archivo

Uso
Coloca tu archivo PDF en la misma carpeta del script y renómbralo como texto.pdf (o cambia el nombre en el código).

Ejecuta el script:

bash
Copy
Edit
python main.py
El resultado será una página del PDF cuyo contenido es más similar a la consulta "SQS or EventBridge".

🧪 Ejemplo de salida
bash
Copy
Edit
Page 1: Akaunt Backend Technical Challenge
You have been tasked with building two microservices...
📄 Créditos
Este proyecto usa:

LangChain

Google Generative AI Embeddings

LangChain Community Loaders

✅ Futuras mejoras
Soporte para múltiples consultas

Uso de almacenamiento persistente (como FAISS o Chroma)

Interfaz gráfica para subir documentos y hacer consultas


