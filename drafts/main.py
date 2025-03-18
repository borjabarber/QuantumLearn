from crewai import Agent, Task, Crew
from openai import OpenAI
import os

# Configurar la API de OpenAI
os.environ["OPENAI_API_KEY"] = ""

# Definir los agentes

# Agente que genera exámenes
test_creator = Agent(
    role="Test Creator",
    goal="Diseñar preguntas de evaluación desafiantes y relevantes sobre Data Science, abarcando teoría y aplicaciones prácticas.",
    backstory="Especialista en evaluación educativa con un profundo conocimiento en ciencia de datos. Crea exámenes estructurados para medir comprensión teórica y habilidades analíticas.",
    verbose=True,
    model="gpt-3.5-turbo"
)

# Agente que evalúa respuestas
test_evaluator = Agent(
    role="Test Evaluator",
    goal="Calificar respuestas con precisión y proporcionar retroalimentación clara y útil para mejorar la comprensión del estudiante.",
    backstory="Profesor con experiencia en la evaluación de exámenes de Data Science.",
    verbose=True,
    model="gpt-3.5-turbo"
)

# Agente que crea tarjetas de memoria
flashcard_generator = Agent(
    role="Flashcard Generator",
    goal="Generar tarjetas de memoria efectivas que ayuden a reforzar conceptos clave de Data Science de forma clara y memorable.",
    backstory="Experto en técnicas de aprendizaje activo y retención de información, con experiencia en la creación de material didáctico interactivo.",
    verbose=True,
    model="gpt-3.5-turbo"
    instructions="Si la pregunta no está relacionada con Data Science, responde con 'Lo siento, solo puedo responder preguntas sobre Data Science'."
)

# Agente que explica conceptos
concept_explainer = Agent(
    role="Concept Explainer",
    goal="Explicar conceptos de Data Science de manera clara y accesible, utilizando ejemplos prácticos y analogías intuitivas.",
    backstory="Docente apasionado por simplificar temas complejos, facilitando la comprensión a estudiantes con distintos niveles de experiencia.",
    verbose=True,
    model="gpt-3.5-turbo"
    instructions="Si la pregunta no está relacionada con Data Science, responde con 'Lo siento, solo puedo responder preguntas sobre Data Science'."
)

# Agente que analiza el desempeño del estudiante
performance_analyzer = Agent(
    role="Performance Analyzer",
    goal="Identificar patrones en los errores de los estudiantes y proporcionar estrategias de mejora basadas en datos.",
    backstory="Especialista en análisis de datos educativos, con experiencia en detectar tendencias de desempeño y optimizar estrategias de aprendizaje.",
    verbose=True,
    model="gpt-3.5-turbo"
)

# Agente que recomienda material personalizado
tutor_personalized = Agent(
    role="Personalized Tutor",
    goal="Sugerir materiales de estudio personalizados que refuercen los conocimientos del estudiante según sus necesidades específicas.",
    backstory="Mentor en aprendizaje adaptativo, capaz de seleccionar recursos óptimos para cada estudiante con base en su rendimiento académico.",
    verbose=True,
    model="gpt-3.5-turbo"
)

# Definir las tareas

# Tarea genera exámenes
task_create_test = Task(
    description="Genera un conjunto de 10 preguntas bien estructuradas sobre Data Science, incluyendo teoría, estadística y aplicaciones prácticas. Las preguntas deben ser desafiantes y fomentar el pensamiento crítico.",
    agent=test_creator,
    expected_output="Lista de 10 preguntas de evaluación con una combinación equilibrada de teoría y práctica, diseñadas para medir comprensión y habilidades."
)

#Tarea evalúa respuestas
task_evaluate_test = Task(
    description="Revisa y califica las respuestas de un estudiante en un examen de Data Science. Proporciona puntuaciones detalladas junto con comentarios explicativos y sugerencias de mejora.",
    agent=test_evaluator,
    expected_output="Informe de evaluación detallado con puntuaciones, análisis de errores y retroalimentación específica para cada respuesta."
)

# Tarea tarjetas de memoria
task_generate_flashcards = Task(
    description="Crea 10 tarjetas de memoria para reforzar conceptos clave de Data Science. Cada tarjeta debe contener una pregunta concisa y una respuesta clara.",
    agent=flashcard_generator,
    expected_output="Colección de 10 tarjetas de memoria bien diseñadas con preguntas y respuestas que ayuden a la memorización efectiva de conceptos clave relacionados con data science."
    
)

# Tarea conceptos
task_explain_concept = Task(
    description="Explica el concepto de Machine Learning de manera clara y accesible. Usa ejemplos prácticos, gráficos o analogías para mejorar la comprensión.",
    agent=concept_explainer,
    expected_output="Explicación didáctica de machine learning con ejemplos prácticos y analogías intuitivas que faciliten su comprensión a distintos niveles."
    
)

#tarea desempeño
task_analyze_performance = Task(
    description="Analiza los errores recurrentes en respuestas del estudiante sobre regresión logística. Identifica patrones y brinda estrategias específicas de mejora.",
    agent=performance_analyzer,
    expected_output="Informe con análisis de patrones de error y recomendaciones estratégicas para mejorar el desempeño del estudiante en regresión logística de manera unica sin que se parezca a la respuesta de nigun otro agente,el informe esta dirigido al estudiante."
)

#tarea Recomendación
task_recommend_material = Task(
    description="Sugerir materiales de estudio personalizados para un estudiante con dificultades en conceptos relacionados con data Science. Incluir artículos, videos y ejercicios prácticos adecuados a su nivel.",
    agent=tutor_personalized,
    expected_output="Lista de recursos de estudio personalizados, con explicaciones y ejercicios diseñados para mejorar la comprensión de los conceptos necesarios."
)

# Crear el Crew
teacher_assistant_crew = Crew(
    agents=[test_creator, test_evaluator, flashcard_generator, concept_explainer, performance_analyzer, tutor_personalized],
    tasks=[task_create_test, task_evaluate_test, task_generate_flashcards, task_explain_concept, task_analyze_performance, task_recommend_material]
)

# Ejecutar las tareas
teacher_assistant_crew.kickoff()
