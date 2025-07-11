import streamlit as st
import os
from crewai import Agent, Task, Crew
from openai import OpenAI
import json

# Configuración de la página
st.set_page_config(page_title="QuantumLearn Asistente de Aprendizaje", page_icon="��", layout="wide")

# Título principal
st.title("Asistente de Aprendizaje Data Science")

# Configuración de la API key
api_key = st.sidebar.text_input("Ingresa tu OpenAI API Key", type="password")
if api_key:
    os.environ["OPENAI_API_KEY"] = api_key

# Función para crear agentes
def create_agents():
    test_creator = Agent(
        role="Test Creator",
        goal="Diseñar preguntas de evaluación desafiantes y relevantes sobre Data Science.",
        backstory="Especialista en evaluación educativa con un profundo conocimiento en ciencia de datos.",
        verbose=True,
        allow_delegation=False,
        model="gpt-4.1"
    )
    
    test_evaluator = Agent(
        role="Test Evaluator",
        goal="Calificar respuestas con precisión y proporcionar retroalimentación clara.",
        backstory="Profesor con experiencia en la evaluación de exámenes de Data Science.",
        verbose=True,
        allow_delegation=False,
        model="gpt-4.1"
    )
    
    flashcard_generator = Agent(
        role="Flashcard Generator",
        goal="Generar tarjetas de memoria efectivas sobre Data Science.",
        backstory="Experto en técnicas de aprendizaje activo y retención de información.",
        verbose=True,
        allow_delegation=False,
        model="gpt-4.1"
    )
    
    concept_explainer = Agent(
        role="Concept Explainer",
        goal="Explicar conceptos de Data Science de manera clara y accesible.",
        backstory="Docente apasionado por simplificar temas complejos.",
        verbose=True,
        allow_delegation=False,
        model="gpt-4.1"
    )

    tutor_personalized = Agent(
        role="Personalized Tutor",
        goal="Sugerir materiales de estudio personalizados que refuercen los conocimientos del estudiante.",
        backstory="Mentor en aprendizaje adaptativo, capaz de seleccionar recursos óptimos para cada estudiante.",
        verbose=True,
        allow_delegation=False,
        model="gpt-4.1"
    )
    
    return {
        "test_creator": test_creator,
        "test_evaluator": test_evaluator,
        "flashcard_generator": flashcard_generator,
        "concept_explainer": concept_explainer,
        "tutor_personalized": tutor_personalized
    }

# Sidebar para selección de funcionalidad
st.sidebar.title("Funcionalidades")
option = st.sidebar.selectbox(
    "¿Qué deseas hacer?",
    ["Generador de examenes", "Evaluador de respuestas", "Flashcards", "Traductor de conceptos", "Recomendador de Material"]
)

# Verificar API key antes de continuar
if not api_key:
    st.warning("Por favor, ingresa tu API key de OpenAI en el sidebar para comenzar.")
    st.stop()

# Crear agentes
agents = create_agents()

# Función para formatear la respuesta
def format_response(text):
    # Convertir CrewOutput a string si es necesario
    if hasattr(text, 'raw'):
        text = str(text.raw)
    else:
        text = str(text)
    
    # Eliminar marcadores de "Human:" o "Assistant:" si existen
    if "Human:" in text:
        text = text.split("Human:")[-1]
    if "Assistant:" in text:
        text = text.split("Assistant:")[-1]
    
    # Limpiar el texto
    text = text.strip()
    
    # Si el texto parece ser JSON, intentar formatearlo
    if text.startswith("{") or text.startswith("["):
        try:
            return json.loads(text)
        except:
            pass
    
    return text

# Lógica principal basada en la selección
if option == "Generador de examenes":
    st.header("🎯 Generador de Exámenes")
    tema = st.text_input("Ingresa el tema específico del examen:")
    num_preguntas = st.number_input("Número de preguntas", min_value=1, max_value=10, value=5)
    
    if st.button("Generar Examen"):
        with st.spinner("Generando examen..."):
            task = Task(
                description=f"Genera {num_preguntas} preguntas sobre {tema} en Data Science. Incluye tanto teoría como práctica. Formatea la respuesta en una lista numerada clara.",
                agent=agents["test_creator"],
                expected_output="Lista numerada de preguntas de examen sobre el tema especificado, incluyendo teoría y práctica."
            )
            crew = Crew(
                agents=[agents["test_creator"]],
                tasks=[task]
            )
            result = crew.kickoff()
            st.success("¡Examen generado!")
            st.markdown("---")
            st.markdown(format_response(result))

elif option == "Flashcards":
    st.header("📚 Generador de Flashcards")
    tema = st.text_input("Ingresa el tema para las flashcards:")
    num_cards = st.number_input("Número de flashcards", min_value=1, max_value=10, value=5)
    
    if st.button("Generar Flashcards"):
        with st.spinner("Generando flashcards..."):
            task = Task(
                description=f"Crea {num_cards} flashcards sobre {tema} en Data Science. Para cada flashcard, usa el formato '**Pregunta:** [pregunta]\\n**Respuesta:** [respuesta]\\n\\n'",
                agent=agents["flashcard_generator"],
                expected_output="Conjunto de flashcards con preguntas y respuestas sobre el tema especificado."
            )
            crew = Crew(
                agents=[agents["flashcard_generator"]],
                tasks=[task]
            )
            result = crew.kickoff()
            st.success("¡Flashcards generadas!")
            st.markdown("---")
            st.markdown(format_response(result))

elif option == "Traductor de conceptos":
    st.header("🎓 Traductor de conceptos")
    concepto = st.text_input("¿Qué concepto de Data Science quieres que te explique?")
    
    if st.button("Explicar"):
        with st.spinner("Generando explicación..."):
            task = Task(
                description=f"Explica el concepto de {concepto} de manera clara y con ejemplos prácticos. Usa markdown para formatear la respuesta con títulos, subtítulos y viñetas donde sea apropiado.",
                agent=agents["concept_explainer"],
                expected_output="Explicación detallada del concepto con ejemplos prácticos y analogías."
            )
            crew = Crew(
                agents=[agents["concept_explainer"]],
                tasks=[task]
            )
            result = crew.kickoff()
            st.success("¡Explicación generada!")
            st.markdown("---")
            st.markdown(format_response(result))

elif option == "Evaluador de respuestas":
    st.header("📝 Evaluador de Respuestas")
    pregunta = st.text_area("Ingresa la pregunta:")
    respuesta = st.text_area("Ingresa tu respuesta:")
    
    if st.button("Evaluar"):
        with st.spinner("Evaluando respuesta..."):
            task = Task(
                description=f"Evalúa la siguiente respuesta a la pregunta: '{pregunta}'\nRespuesta: {respuesta}\n\nFormatea tu evaluación usando el siguiente esquema markdown:\n\n**Puntuación**: [X/10]\n**Fortalezas**:\n- punto 1\n- punto 2\n\n**Áreas de mejora**:\n- punto 1\n- punto 2\n\n**Recomendaciones**:\n[tus recomendaciones]",
                agent=agents["test_evaluator"],
                expected_output="Evaluación detallada de la respuesta con retroalimentación constructiva y sugerencias de mejora."
            )
            crew = Crew(
                agents=[agents["test_evaluator"]],
                tasks=[task]
            )
            result = crew.kickoff()
            st.success("¡Evaluación completada!")
            st.markdown("---")
            st.markdown(format_response(result))

elif option == "Recomendador de Material":
    st.header("📚 Recomendación de Material")
    tema = st.text_input("¿Sobre qué tema necesitas recomendaciones?")
    nivel = st.selectbox("¿Cuál es tu nivel de conocimiento?", ["Principiante", "Intermedio", "Avanzado"])
    
    if st.button("Obtener Recomendaciones"):
        with st.spinner("Buscando recursos personalizados..."):
            task = Task(
                description=f"""
                Recomienda materiales de estudio sobre {tema} para un estudiante de nivel {nivel}. 
                Formatea tu respuesta usando markdown con las siguientes secciones y asegurando que cada recurso incluya un enlace:
                
                ## Cursos Online
                - [Título del curso](URL)
                
                ## Artículos y Tutoriales
                - [Título del artículo](URL)
                
                ## Videos Recomendados
                - [Título del video](URL)
                
                ## Ejercicios Prácticos
                - [Título del ejercicio](URL)
                
                Proporciona una breve descripción de por qué cada recurso es útil.
                """,
                agent=agents["tutor_personalized"],
                expected_output="Lista detallada de recursos de aprendizaje personalizados con enlaces y explicaciones sobre su relevancia y utilidad."
            )
            crew = Crew(
                agents=[agents["tutor_personalized"]],
                tasks=[task]
            )
            result = crew.kickoff()
            st.success("¡Recomendaciones generadas!")
            st.markdown("---")
            st.markdown(format_response(result))


            #streamlit run app.py 