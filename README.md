# QuantumLearn-

Tu ecosistema multiagente para dominar la ciencia de datos.

## Descripción General
Este proyecto es una aplicación web desarrollada con **Streamlit** que funciona para dar apoyo a los estudiantes de **Data Science**. Utiliza la librería **CrewAI** para la gestión de agentes de inteligencia artificial especializados en diversas tareas, tales como:

- Generación de exámenes
- Evaluación de respuestas
- Creación de flashcards
- Explicación de conceptos
- Recomendación de material de estudio

Los agentes interactúan con el usuario a través de la API de **OpenAI** para proporcionar respuestas en tiempo real según la funcionalidad seleccionada.


## Tecnologías Utilizadas
- **Python**
- **Streamlit** (para la interfaz de usuario)
- **CrewAI** (para la creación y gestión de agentes IA)
- **OpenAI API** (para la generación de respuestas y contenido)
- **JSON** (para el procesamiento de datos)

## Configuración y Ejecución
### Requisitos Previos
Antes de ejecutar la aplicación, asegúrate de tener instaladas las siguientes dependencias:
```bash
pip install streamlit crewai openai
```

### Ejecución de la Aplicación
Para iniciar la aplicación, ejecuta el siguiente comando:
```bash
streamlit run app.py
```

>[!NOTE]  
Para usar el codigo se necesita una APIKEY de OpenAI.
----


## Estructura del Código
### 1. Configuración Inicial
- Se configura la página de **Streamlit** con un título y diseño de pantalla ancha.
- Se solicita al usuario ingresar su **API Key de OpenAI** a través de la barra lateral.

### 2. Creación de Agentes
Se definen cinco agentes especializados en distintas tareas:
- **Test Creator:** Genera preguntas de evaluación sobre Data Science.
- **Test Evaluator:** Evalúa respuestas y proporciona retroalimentación.
- **Flashcard Generator:** Crea tarjetas de memoria.
- **Concept Explainer:** Explica conceptos complejos de manera sencilla.
- **Personalized Tutor:** Recomienda materiales de estudio personalizados.

Cada agente se define con un **rol, meta, historia de fondo, modelo de lenguaje** y configuraciones adicionales.

### 3. Selección de Funcionalidad
El usuario elige una de las siguientes opciones desde la barra lateral:
- **Generar Examen**: Genera preguntas basadas en un tema ingresado.
- **Evaluar Respuestas**: Analiza una respuesta dada y proporciona feedback.
- **Crear Flashcards**: Genera tarjetas de memoria con preguntas y respuestas.
- **Explicar Concepto**: Explica un concepto con ejemplos y estructura markdown.
- **Recomendar Material**: Sugerencias de cursos, artículos y ejercicios según el nivel del usuario.

Si el usuario no ha ingresado su API Key, la aplicación muestra una advertencia y no permite continuar.

### 4. Ejecución de las Tareas
Dependiendo de la opción seleccionada, la aplicación:
1. **Crea una tarea** con una descripción específica y un agente asignado.
2. **Crea una Crew** que asocia el agente con la tarea.
3. **Ejecuta la Crew** y obtiene el resultado.
4. **Formatea la respuesta** para mejorar la legibilidad.
5. **Muestra el resultado** en la interfaz de usuario.

### 5. Formateo de Respuestas
La función `format_response(text)` se encarga de limpiar y dar formato a la respuesta generada por el modelo. Si la salida es JSON, intenta formatearla adecuadamente.

## Conclusión
Este asistente de aprendizaje basado en inteligencia artificial facilita el estudio y aprendizage de Data Science mediante una interfaz intuitiva y funcionalidades diseñadas para mejorar la comprensión y evaluación de conocimientos.

