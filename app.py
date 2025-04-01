
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import time

# Configuración de la página
st.set_page_config(
    page_title="BIAmed - Dictado médico con inteligencia artificial",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    :root {
        --biamed-purple: #8A00FF;
        --biamed-purple-light: #D899FF;
        --biamed-gray: #F6F6F9;
        --biamed-gray-light: #F9F9FB;
    }
    
    html, body, .stApp {
        font-family: 'Inter', sans-serif;
    }
    
    /* Gradiente de BIAmed */
    .biamed-gradient-text {
        background: linear-gradient(90deg, #8A00FF 0%, #D899FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        color: transparent;
        font-weight: 700;
    }
    
    .biamed-card {
        background-color: white;
        border-radius: 12px;
        border: 1px solid #F0F0F5;
        padding: 24px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .biamed-card:hover {
        transform: translateY(-2px);
        box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.08);
    }
    
    .bg-purple-gradient {
        background: linear-gradient(90deg, #8A00FF 0%, #D899FF 100%);
    }
    
    .btn-purple {
        background: linear-gradient(90deg, #8A00FF 0%, #D899FF 100%);
        color: white;
        font-weight: 600;
    }
    
    .btn-white {
        background-color: white;
        color: #8A00FF;
        font-weight: 600;
        border: 1px solid white;
    }
    
    .btn-outline {
        background-color: transparent;
        color: white;
        font-weight: 600;
        border: 1px solid white;
    }
    
    .header {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background-color: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(8px);
        border-bottom: 1px solid #F0F0F5;
        padding: 12px 0;
    }
    
    .avatar-placeholder {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background-color: rgba(138, 0, 255, 0.1);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #8A00FF;
        font-weight: bold;
    }
    
    /* Ocultar elementos de Streamlit que no necesitamos */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    .stDecoration {display:none;}
    
    /* Para crear secciones con fondo alternado */
    .section-gray {
        background-color: #F9F9FB;
        padding: 50px 0;
        margin: 0 -100vw;
        padding-left: calc(100vw - 50%);
        padding-right: calc(100vw - 50%);
    }
    
    /* Estilo para pestañas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        border-radius: 4px;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: white;
        color: #8A00FF;
    }
</style>
""", unsafe_allow_html=True)

# Función simulada para un envío de formulario
def handle_demo_form():
    with st.spinner('Enviando solicitud...'):
        time.sleep(1.5)  # Simular carga
    st.success('¡Solicitud recibida! Nos pondremos en contacto contigo muy pronto.')
    return True

# Header - Encabezado fijo
with st.container():
    st.markdown("""
    <div class="header">
        <div style="display: flex; align-items: center; justify-content: space-between; max-width: 1200px; margin: 0 auto; padding: 0 16px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <div style="width: 32px; height: 32px; border-radius: 4px;" class="bg-purple-gradient"></div>
                <span style="font-weight: 700; font-size: 24px; letter-spacing: -0.5px;">
                    BIA<span style="font-weight: 800;">MED</span>
                </span>
            </div>
            
            <div style="display: none; gap: 32px; align-items: center;">
                <a href="#beneficios" style="font-weight: 500; color: #333; text-decoration: none;">Beneficios</a>
                <a href="#funcionamiento" style="font-weight: 500; color: #333; text-decoration: none;">Cómo funciona</a>
                <a href="#testimonios" style="font-weight: 500; color: #333; text-decoration: none;">Testimonios</a>
                <a href="#preguntas" style="font-weight: 500; color: #333; text-decoration: none;">FAQ</a>
            </div>
            
            <div style="display: flex; gap: 12px;">
                <button style="padding: 8px 16px; border-radius: 4px; border: 1px solid #E5E7EB; background-color: white; font-weight: 500; font-size: 14px;">
                    Iniciar sesión
                </button>
                <button class="btn-purple" style="padding: 8px 16px; border-radius: 4px; border: none; font-size: 14px;">
                    Solicitar demo
                </button>
            </div>
        </div>
    </div>
    <div style="height: 70px;"></div>  <!-- Espaciador para compensar el header fijo -->
    """, unsafe_allow_html=True)

# Sección Hero
with st.container():
    cols = st.columns([5, 5])
    
    with cols[0]:
        st.markdown("""
        <div style="padding-top: 40px;">
            <div style="display: inline-flex; align-items: center; border-radius: 9999px; border: 1px solid #E5E7EB; padding: 4px 12px; margin-bottom: 16px;">
                <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: #8A00FF; margin-right: 8px;"></span>
                <span style="font-size: 14px;">Tecnología de reconocimiento de voz avanzada</span>
            </div>
            
            <h1 style="font-size: 48px; line-height: 1.1; font-weight: 700; margin-bottom: 16px;">
                Dictado médico con<br/>
                <span class="biamed-gradient-text">inteligencia artificial</span>
            </h1>
            
            <p style="font-size: 18px; color: #4B5563; margin-bottom: 24px;">
                Redacta notas médicas y de seguros hasta 3 veces más rápido con reconocimiento de voz de última generación. Especialmente diseñado para profesionales de la salud.
            </p>
            
            <div style="display: flex; gap: 16px; margin-bottom: 24px;">
                <button class="btn-purple" style="padding: 12px 24px; border-radius: 8px; border: none;">
                    Solicitar una demostración
                </button>
                <button style="padding: 12px 24px; border-radius: 8px; background-color: white; color: #8A00FF; border: 1px solid #8A00FF;">
                    Ver cómo funciona
                </button>
            </div>
            
            <div style="display: flex; flex-wrap: wrap; gap: 24px; margin-top: 24px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="color: #8A00FF;">✓</span>
                    <span style="font-size: 14px; color: #4B5563;">Sin periodo de entrenamiento</span>
                </div>
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="color: #8A00FF;">✓</span>
                    <span style="font-size: 14px; color: #4B5563;">Integración sencilla</span>
                </div>
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="color: #8A00FF;">✓</span>
                    <span style="font-size: 14px; color: #4B5563;">Soporte 24/7</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        with st.container():
            st.markdown('<div class="biamed-card">', unsafe_allow_html=True)
            st.markdown("<h3 style='font-size: 20px; font-weight: 700; text-align: center; margin-bottom: 16px;'>Solicita una demostración gratuita</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: #6B7280; margin-bottom: 24px;'>Descubre cómo BIAmed puede transformar tu práctica</p>", unsafe_allow_html=True)
            
            # Formulario de demostración
            with st.form("demo_form"):
                col1, col2 = st.columns(2)
                with col1:
                    nombre = st.text_input("Nombre completo", placeholder="Nombre y apellido")
                with col2:
                    email = st.text_input("Email profesional", placeholder="correo@clinica.com")
                
                telefono = st.text_input("Teléfono", placeholder="+34 600 000 000")
                institucion = st.text_input("Centro médico / Hospital", placeholder="Nombre de la institución")
                
                rol = st.selectbox(
                    "Rol / Especialidad",
                    ["Selecciona tu rol", "Médico", "Médico especialista", "Administrador", "Director médico", "Otro"]
                )
                
                mensaje = st.text_area("¿Alguna pregunta o comentario adicional?", 
                                      placeholder="Escribe aquí tus dudas o necesidades específicas",
                                      height=100)
                
                submitted = st.form_submit_button("Solicitar demostración", use_container_width=True)
                if submitted:
                    success = handle_demo_form()
            
            st.markdown("<p style='text-align: center; font-size: 12px; color: #6B7280; margin-top: 16px;'>Al enviar este formulario, aceptas nuestra política de privacidad y términos de servicio.</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

# Sección de Beneficios
st.markdown("<div id='beneficios' style='height: 60px;'></div>", unsafe_allow_html=True)  # Ancla para navegación
st.markdown("""
<div class="section-gray">
    <div style="max-width: 1200px; margin: 0 auto; padding: 0 16px;">
        <div style="text-align: center; max-width: 768px; margin: 0 auto 48px auto;">
            <h2 style="font-size: 36px; font-weight: 700; margin-bottom: 16px;">
                Beneficios <span class="biamed-gradient-text">para profesionales médicos</span>
            </h2>
            <p style="font-size: 18px; color: #4B5563;">
                BIAmed transforma la forma en que los médicos y centros sanitarios gestionan la documentación clínica con tecnología de vanguardia.
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Crear una grid de beneficios
beneficios = [
    {
        "icon": "⏱️",
        "title": "Ahorra hasta 2 horas diarias",
        "description": "Reduce el tiempo dedicado a la documentación hasta en un 70%, permitiéndote enfocarte más en tus pacientes."
    },
    {
        "icon": "✅",
        "title": "Minimiza errores de documentación",
        "description": "Disminuye significativamente los errores en reportes médicos y documentos de seguros con reconocimiento de voz preciso."
    },
    {
        "icon": "📈",
        "title": "Aumenta la productividad",
        "description": "Atiende más pacientes sin comprometer la calidad del servicio ni la precisión de la documentación."
    },
    {
        "icon": "❤️",
        "title": "Mejora la experiencia del paciente",
        "description": "Dedica más tiempo a la interacción con tus pacientes y menos a la pantalla o a las notas."
    },
    {
        "icon": "🧠",
        "title": "IA especializada en terminología médica",
        "description": "Reconoce términos médicos especializados con alta precisión, incluyendo nombres de medicamentos y procedimientos."
    },
    {
        "icon": "🛡️",
        "title": "Cumple con normativas sanitarias",
        "description": "Garantiza el cumplimiento de HIPAA, GDPR y otras normativas de privacidad de datos médicos."
    }
]

# Organizar los beneficios en filas de 3
for i in range(0, len(beneficios), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(beneficios):
            with cols[j]:
                st.markdown(f"""
                <div class="biamed-card">
                    <div style="display: inline-flex; align-items: center; justify-content: center; width: 48px; height: 48px; border-radius: 8px; background-color: rgba(138, 0, 255, 0.1); margin-bottom: 16px;">
                        <span style="font-size: 24px;">{beneficios[i+j]['icon']}</span>
                    </div>
                    <h3 style="font-size: 18px; font-weight: 700; margin-bottom: 8px;">{beneficios[i+j]['title']}</h3>
                    <p style="color: #4B5563;">{beneficios[i+j]['description']}</p>
                </div>
                """, unsafe_allow_html=True)

# Sección de Demostración del Producto
st.markdown("<div id='funcionamiento' style='height: 60px;'></div>", unsafe_allow_html=True)  # Ancla para navegación
st.markdown("""
<div style="padding: 80px 0;">
    <div style="max-width: 1200px; margin: 0 auto; padding: 0 16px;">
        <div style="text-align: center; max-width: 768px; margin: 0 auto 48px auto;">
            <h2 style="font-size: 36px; font-weight: 700; margin-bottom: 16px;">
                Dictado médico <span class="biamed-gradient-text">inteligente y preciso</span>
            </h2>
            <p style="font-size: 18px; color: #4B5563;">
                Con BIAmed, documentar consultas, diagnósticos e informes es tan sencillo como hablar. 
                Nuestro sistema aprende constantemente para entender mejor tu vocabulario específico.
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Demo del producto
cols = st.columns([3, 2])
with cols[0]:
    st.markdown("""
    <div class="biamed-card" style="overflow: hidden; position: relative;">
        <div style="aspect-ratio: 16/9; background-color: #F9F9FB; position: relative; margin-bottom: 16px; border-radius: 8px; overflow: hidden;">
            <div style="position: absolute; inset: 0; background: linear-gradient(135deg, rgba(138, 0, 255, 0.2), rgba(216, 153, 255, 0.3)); display: flex; align-items: center; justify-content: center;">
                <button style="padding: 12px 20px; border-radius: 8px; background-color: rgba(255, 255, 255, 0.8); border: none; font-weight: 600; display: flex; align-items: center; gap: 8px;">
                    <span style="display: inline-block; width: 0; height: 0; border-style: solid; border-width: 8px 0 8px 12px; border-color: transparent transparent transparent #8A00FF;"></span>
                    <span>Ver demostración</span>
                </button>
            </div>
            
            <!-- Área de consulta procesada (simulada) -->
            <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 16px;">
                <div style="background-color: rgba(255, 255, 255, 0.95); border-radius: 8px; padding: 12px; border: 1px solid #F0F0F5; display: flex; align-items: center; justify-content: space-between; backdrop-filter: blur(4px);">
                    <span style="font-weight: 500; font-size: 14px;">Consulta procesada</span>
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <div style="width: 12px; height: 12px; border-radius: 50%; background-color: #8A00FF; animation: pulse 2s infinite;"></div>
                        <span style="font-size: 14px; color: #6B7280;">Transcripción completada</span>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Controles de audio (simulado) -->
        <div style="padding: 16px; background-color: white; display: flex; align-items: center; gap: 16px; border-top: 1px solid #F0F0F5;">
            <div style="display: flex; items-center; gap: 12px;">
                <div style="width: 40px; height: 40px; border-radius: 50%; background: linear-gradient(90deg, #8A00FF 0%, #D899FF 100%); display: flex; align-items: center; justify-content: center; color: white;">
                    <span>🎙️</span>
                </div>
                <div style="width: 128px;">
                    <div style="width: 100%; height: 6px; background-color: #F0F0F5; border-radius: 9999px; overflow: hidden;">
                        <div style="width: 75%; height: 100%; background: linear-gradient(90deg, #8A00FF 0%, #D899FF 100%);"></div>
                    </div>
                </div>
            </div>
            <div style="margin-left: auto; font-size: 14px; color: #6B7280;">
                00:04:35
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with cols[1]:
    st.markdown("""
    <div style="display: flex; flex-direction: column; gap: 24px; height: 100%; justify-content: center;">
        <div>
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                <div style="width: 32px; height: 32px; border-radius: 50%; background-color: rgba(138, 0, 255, 0.1); display: flex; align-items: center; justify-content: center; color: #8A00FF; font-weight: 700;">1</div>
                <h3 style="font-size: 20px; font-weight: 700;">Habla naturalmente</h3>
            </div>
            <p style="padding-left: 40px; color: #4B5563;">
                Dicta tus notas médicas con un lenguaje natural, sin necesidad de comandos especiales o pausas artificiales.
            </p>
        </div>
        
        <div>
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                <div style="width: 32px; height: 32px; border-radius: 50%; background-color: rgba(138, 0, 255, 0.1); display: flex; align-items: center; justify-content: center; color: #8A00FF; font-weight: 700;">2</div>
                <h3 style="font-size: 20px; font-weight: 700;">Transcripción instantánea</h3>
            </div>
            <p style="padding-left: 40px; color: #4B5563;">
                El sistema convierte tu voz en texto de forma inmediata, permitiéndote ver y editar el contenido en tiempo real.
            </p>
        </div>
        
        <div>
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                <div style="width: 32px; height: 32px; border-radius: 50%; background-color: rgba(138, 0, 255, 0.1); display: flex; align-items: center; justify-content: center; color: #8A00FF; font-weight: 700;">3</div>
                <h3 style="font-size: 20px; font-weight: 700;">Revisa y confirma</h3>
            </div>
            <p style="padding-left: 40px; color: #4B5563;">
                Revisa la transcripción, realiza ajustes si es necesario y confirma para guardar directamente en el historial del paciente.
            </p>
        </div>
        
        <button class="btn-purple" style="display: inline-flex; align-items: center; gap: 8px; padding: 12px 24px; border-radius: 8px; border: none; margin-top: 16px; align-self: flex-start;">
            <span>📄</span>
            <span>Ver documentación técnica</span>
        </button>
    </div>
    """, unsafe_allow_html=True)

# Sección de Testimonios
st.markdown("<div id='testimonios' style='height: 60px;'></div>", unsafe_allow_html=True)  # Ancla para navegación
st.markdown("""
<div class="section-gray">
    <div style="max-width: 1200px; margin: 0 auto; padding: 0 16px;">
        <div style="text-align: center; max-width: 768px; margin: 0 auto 48px auto;">
            <h2 style="font-size: 36px; font-weight: 700; margin-bottom: 16px;">
                Lo que dicen nuestros <span class="biamed-gradient-text">usuarios</span>
            </h2>
            <p style="font-size: 18px; color: #4B5563;">
                Profesionales médicos de diversas especialidades confían en BIAmed para optimizar su documentación clínica.
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Testimonios
testimonios = [
    {
        "nombre": "Dra. Laura Martínez",
        "rol": "Cardióloga, Hospital Universitario",
        "cita": "BIAmed ha revolucionado mi consulta. Ahora puedo dedicar más tiempo a mis pacientes y menos a la documentación. La precisión del reconocimiento de términos cardiológicos es impresionante.",
        "estrellas": 5
    },
    {
        "nombre": "Dr. Carlos Vega",
        "rol": "Director Médico, Clínica Privada",
        "cita": "Implementamos BIAmed en toda nuestra clínica y los resultados son extraordinarios. Los médicos están más satisfechos y hemos reducido los costos administrativos en un 30%.",
        "estrellas": 5
    },
    {
        "nombre": "Dr. Antonio Ruiz",
        "rol": "Médico de Familia",
        "cita": "La facilidad de uso y la capacidad de integración con nuestro sistema existente hizo que la transición fuera perfecta. Ahora termino mis notas antes de que el paciente salga de la consulta.",
        "estrellas": 4
    }
]

cols = st.columns(3)
for i, testimonio in enumerate(testimonios):
    with cols[i]:
        # Crear estrellas
        estrellas_html = ""
        for j in range(5):
            if j < testimonio["estrellas"]:
                estrellas_html += '<span style="color: #FFB800;">★</span>'
            else:
                estrellas_html += '<span style="color: #E5E7EB;">★</span>'
                
        st.markdown(f"""
        <div class="biamed-card">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px;">
                <div style="display: flex; gap: 12px; align-items: center;">
                    <div class="avatar-placeholder">
                        {testimonio['nombre'].split()[0][0]}{testimonio['nombre'].split()[1][0]}
                    </div>
                    <div>
                        <h4 style="font-weight: 700; font-size: 16px;">{testimonio['nombre']}</h4>
                        <p style="font-size: 14px; color: #6B7280;">{testimonio['rol']}</p>
                    </div>
                </div>
                <div>
                    {estrellas_html}
                </div>
            </div>
            <blockquote style="color: #4B5563; font-style: italic;">
                "{testimonio['cita']}"
            </blockquote>
        </div>
        """, unsafe_allow_html=True)

# Características técnicas
st.markdown("""
<div style="padding: 80px 0;">
    <div style="max-width: 1200px; margin: 0 auto; padding: 0 16px;">
        <div style="text-align: center; max-width: 768px; margin: 0 auto 48px auto;">
            <h2 style="font-size: 36px; font-weight: 700; margin-bottom: 16px;">
                Características <span class="biamed-gradient-text">técnicas avanzadas</span>
            </h2>
            <p style="font-size: 18px; color: #4B5563;">
                BIAmed combina tecnología de vanguardia con una experiencia de usuario intuitiva para transformar la documentación médica.
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Pestañas de características técnicas
tab1, tab2, tab3 = st.tabs(["Funcionalidad", "Tecnología", "Seguridad"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="biamed-card">
            <div style="font-size: 32px; color: #8A00FF; margin-bottom: 16px;">🧩</div>
            <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 8px;">Reconocimiento contextual</h3>
            <p style="color: #4B5563;">
                Comprende el contexto médico y adapta la transcripción a la especialidad del profesional, mejorando la precisión con el uso.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="biamed-card">
            <div style="font-size: 32px; color: #8A00FF; margin-bottom: 16px;">⚙️</div>
            <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 8px;">Personalización avanzada</h3>
            <p style="color: #4B5563;">
                Adapta el sistema a tu vocabulario específico, terminología preferida y estructura de documentos habituales.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("""
        <div class="biamed-card">
            <div style="font-size: 32px; color: #8A00FF; margin-bottom: 16px;">📊</div>
            <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 8px;">Análisis e informes</h3>
            <p style="color: #4B5563;">
                Genera automáticamente informes estructurados y extrae datos clave para análisis clínicos y administrativos.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="biamed-card">
            <div style="font-size: 32px; color: #8A00FF; margin-bottom: 16px;">☁️</div>
            <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 8px;">Integración con HIS/EMR</h3>
            <p style="color: #4B5563;">
                Se integra perfectamente con los principales sistemas de historia clínica electrónica y gestión hospitalaria.
            </p>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="biamed-card">
            <div style="font-size: 32px; color: #8A00FF; margin-bottom: 16px;">🖥️</div>
            <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 8px;">IA de última generación</h3>
            <p style="color: #4B5563;">
                Procesamiento del lenguaje natural (NLP) especializado en terminología médica con redes neuronales profundas.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="biamed-card">
            <div style="font-size: 32px; color: #8A00FF; margin-bottom: 16px;">📱</div>
            <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 8px;">Compatible con múltiples dispositivos</h3>
            <p style="color: #4B5563;">
                Funciona en ordenadores, tablets y smartphones, permitiendo flexibilidad total para los profesionales médicos.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("""
        <div class="biamed-card">
            <div style="font-size: 32px; color: #8A00FF; margin-bottom: 16px;">💻</div>
            <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 8px;">Funcionamiento offline</h3>
            <p style="color: #4B5563;">
                Capacidad de trabajar sin conexión a internet, sincronizando los datos cuando la conexión se restablece.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="biamed-card">
            <div style="font-size: 32px; color: #8A00FF; margin-bottom: 16px;">📱</div>
            <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 8px;">Aplicaciones nativas</h3>
            <p style="color: #4B5563;">
                Disponible como aplicación web y aplicaciones nativas para iOS y Android para máximo rendimiento.
            </p>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="biamed-card">
            <div style="font-size: 32px; color: #8A00FF; margin-bottom: 16px;">🔒</div>
            <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 8px;">Encriptación de extremo a extremo</h3>
            <p style="color: #4B5563;">
                Toda la información se encripta utilizando protocolos de seguridad avanzados para garantizar la confidencialidad de los datos.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="biamed-card">
            <div style="font-size: 32px; color: #8A00FF; margin-bottom: 16px;">🛡️</div>
            <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 8px;">Cumplimiento normativo</h3>
            <p style="color: #4B5563;">
                Conforme con HIPAA, GDPR, LOPD y otras regulaciones internacionales de protección de datos sanitarios.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("""
        <div class="biamed-card">
            <div style="font-size: 32px; color: #8A00FF; margin-bottom: 16px;">🖥️</div>
            <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 8px;">Procesamiento local</h3>
            <p style="color: #4B5563;">
                Opción de procesamiento de datos dentro de las instalaciones del cliente para máxima seguridad.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="biamed-card">
            <div style="font-size: 32px; color: #8A00FF; margin-bottom: 16px;">🛡️</div>
            <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 8px;">Auditorías de seguridad</h3>
            <p style="color: #4B5563;">
                Realizamos auditorías de seguridad regulares por entidades externas para garantizar la protección de datos.
            </p>
        </div>
        """, unsafe_allow_html=True)

# Sección de FAQ
st.markdown("<div id='preguntas' style='height: 60px;'></div>", unsafe_allow_html=True)  # Ancla para navegación
st.markdown("""
<div class="section-gray">
    <div style="max-width: 1200px; margin: 0 auto; padding: 0 16px;">
        <div style="text-align: center; max-width: 768px; margin: 0 auto 48px auto;">
            <h2 style="font-size: 36px; font-weight: 700; margin-bottom: 16px;">
                Preguntas <span class="biamed-gradient-text">frecuentes</span>
            </h2>
            <p style="font-size: 18px; color: #4B5563;">
                Encuentra respuestas a las dudas más comunes sobre BIAmed
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Preguntas frecuentes
faqs = [
    {
        "pregunta": "¿Cómo se integra BIAmed con nuestro sistema actual?",
        "respuesta": "BIAmed cuenta con API abiertas y conectores específicos para los principales sistemas de historia clínica electrónica del mercado. Nuestro equipo técnico se encarga de todo el proceso de integración, garantizando una transición suave y sin interrupciones en su servicio."
    },
    {
        "pregunta": "¿Qué precisión tiene el reconocimiento de voz para terminología médica?",
        "respuesta": "BIAmed alcanza una precisión superior al 98% para terminología médica general, y por encima del 95% para especialidades médicas específicas. El sistema aprende continuamente de las correcciones, mejorando con el uso y adaptándose a su vocabulario específico."
    },
    {
        "pregunta": "¿Necesito entrenar al sistema para que reconozca mi voz?",
        "respuesta": "No, BIAmed funciona sin entrenamiento previo. El sistema utiliza algoritmos avanzados de IA que se adaptan instantáneamente a diferentes acentos, tonos y formas de hablar. No obstante, cuanto más lo utilice, mejor será la adaptación a sus patrones específicos de dictado."
    },
    {
        "pregunta": "¿Qué idiomas soporta la plataforma?",
        "respuesta": "Actualmente, BIAmed soporta español (con sus variantes regionales), inglés, francés, alemán, italiano y portugués. Estamos trabajando continuamente para añadir más idiomas a nuestra oferta."
    },
    {
        "pregunta": "¿Cómo garantizan la seguridad y confidencialidad de la información?",
        "respuesta": "Implementamos encriptación de extremo a extremo, servidores seguros con certificación ISO 27001, y procesamiento que cumple con HIPAA, GDPR y otras normativas de protección de datos sanitarios. Todos nuestros procesos están diseñados priorizando la seguridad y confidencialidad de la información médica."
    }
]

# Crear componente de acordeón personalizado para FAQ
for i, faq in enumerate(faqs):
    with st.expander(faq["pregunta"]):
        st.markdown(f"""
        <p style="color: #4B5563; padding: 8px 0;">{faq["respuesta"]}</p>
        """, unsafe_allow_html=True)

# Sección CTA
st.markdown("""
<div style="position: relative; padding: 80px 0; margin-top: 80px; overflow: hidden;">
    <div style="position: absolute; inset: 0; background: linear-gradient(90deg, #8A00FF 0%, #D899FF 100%); opacity: 0.9;"></div>
    
    <div style="position: relative; z-index: 10; max-width: 800px; margin: 0 auto; text-align: center; color: white; padding: 0 16px;">
        <h2 style="font-size: 36px; font-weight: 700; margin-bottom: 24px;">
            Transforma tu práctica médica hoy
        </h2>
        <p style="font-size: 18px; color: rgba(255, 255, 255, 0.9); margin-bottom: 32px;">
            Únete a miles de profesionales médicos que ya están ahorrando tiempo y mejorando su documentación con BIAmed.
        </p>
        
        <div style="display: flex; flex-wrap: wrap; gap: 16px; justify-content: center; margin-bottom: 24px;">
            <button class="btn-white" style="padding: 12px 24px; border-radius: 8px;">
                Solicitar demostración
            </button>
            <button class="btn-outline" style="padding: 12px 24px; border-radius: 8px; display: flex; align-items: center; gap: 8px;">
                <span>Contactar con ventas</span>
                <span style="display: inline-block; width: 0; height: 0; border-style: solid; border-width: 5px 0 5px 8px; border-color: transparent transparent transparent white;"></span>
            </button>
        </div>
        
        <p style="font-size: 14px; color: rgba(255, 255, 255, 0.8);">
            Sin compromiso. Cancelación en cualquier momento.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<footer style="background-color: white; border-top: 1px solid #F0F0F5; padding: 48px 0;">
    <div style="max-width: 1200px; margin: 0 auto; padding: 0 16px;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 32px; margin-bottom: 48px;">
            <div>
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 16px;">
                    <div style="width: 32px; height: 32px; border-radius: 4px;" class="bg-purple-gradient"></div>
                    <span style="font-weight: 700; font-size: 24px; letter-spacing: -0.5px;">
                        BIA<span style="font-weight: 800;">MED</span>
                    </span>
                </div>
                <p style="color: #6B7280; margin-bottom: 16px;">
                    Soluciones avanzadas de reconocimiento de voz diseñadas específicamente para profesionales de la salud.
                </p>
                <div style="display: flex; gap: 16px; margin-top: 8px;">
                    <a href="#" style="color: #6B7280; text-decoration: none;">📱</a>
                    <a href="#" style="color: #6B7280; text-decoration: none;">📘</a>
                    <a href="#" style="color: #6B7280; text-decoration: none;">📸</a>
                    <a href="#" style="color: #6B7280; text-decoration: none;">📢</a>
                </div>
            </div>
            
            <div>
                <h4 style="font-weight: 700; font-size: 18px; margin-bottom: 16px;">Productos</h4>
                <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 8px;">
                    <li><a href="#" style="color: #6B7280; text-decoration: none; hover: color: #8A00FF;">BIAmed Voice</a></li>
                    <li><a href="#" style="color: #6B7280; text-decoration: none; hover: color: #8A00FF;">BIAmed Analytics</a></li>
                    <li><a href="#" style="color: #6B7280; text-decoration: none; hover: color: #8A00FF;">BIAmed Mobile</a></li>
                    <li><a href="#" style="color: #6B7280; text-decoration: none; hover: color: #8A00FF;">BIAmed Enterprise</a></li>
                    <li><a href="#" style="color: #6B7280; text-decoration: none; hover: color: #8A00FF;">Integraciones</a></li>
                </ul>
            </div>
            
            <div>
                <h4 style="font-weight: 700; font-size: 18px; margin-bottom: 16px;">Recursos</h4>
                <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 8px;">
                    <li><a href="#" style="color: #6B7280; text-decoration: none; hover: color: #8A00FF;">Blog</a></li>
                    <li><a href="#" style="color: #6B7280; text-decoration: none; hover: color: #8A00FF;">Guías y tutoriales</a></li>
                    <li><a href="#" style="color: #6B7280; text-decoration: none; hover: color: #8A00FF;">Casos de éxito</a></li>
                    <li><a href="#" style="color: #6B7280; text-decoration: none; hover: color: #8A00FF;">Webinars</a></li>
                    <li><a href="#" style="color: #6B7280; text-decoration: none; hover: color: #8A00FF;">Soporte</a></li>
                </ul>
            </div>
            
            <div>
                <h4 style="font-weight: 700; font-size: 18px; margin-bottom: 16px;">Empresa</h4>
                <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 8px;">
                    <li><a href="#" style="color: #6B7280; text-decoration: none; hover: color: #8A00FF;">Sobre nosotros</a></li>
                    <li><a href="#" style="color: #6B7280; text-decoration: none; hover: color: #8A00FF;">Contacto</a></li>
                    <li><a href="#" style="color: #6B7280; text-decoration: none; hover: color: #8A00FF;">Empleo</a></li>
                    <li><a href="#" style="color: #6B7280; text-decoration: none; hover: color: #8A00FF;">Privacidad</a></li>
                    <li><a href="#" style="color: #6B7280; text-decoration: none; hover: color: #8A00FF;">Términos y condiciones</a></li>
                </ul>
            </div>
        </div>
        
        <div style="border-top: 1px solid #F0F0F5; padding-top: 32px; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; color: #9CA3AF; font-size: 14px;">
            <p>© {time.strftime("%Y")} BIAmed. Todos los derechos reservados.</p>
            <div style="display: flex; flex-wrap: wrap; gap: 16px; margin-top: 16px;">
                <a href="#" style="color: #9CA3AF; text-decoration: none; hover: color: #8A00FF;">Política de privacidad</a>
                <a href="#" style="color: #9CA3AF; text-decoration: none; hover: color: #8A00FF;">Términos de servicio</a>
                <a href="#" style="color: #9CA3AF; text-decoration: none; hover: color: #8A00FF;">Política de cookies</a>
            </div>
        </div>
    </div>
</footer>
""", unsafe_allow_html=True)
