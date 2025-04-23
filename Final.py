#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 09:36:57 2025

@author: juan
"""
import streamlit as st
recomendaciones_vino = {
    "Gazpacho andaluz": [
        {
            "vino": "Pazo de Señoráns Albariño",
            "calidad": "Estándar",
            "explicacion": "Fresco y afrutado, realza el frescor del gazpacho.",
            "tipo": "Blanco",
            "uva": "Albariño",
            "region": "Rías Baixas",
            "notas": "Cítricos, manzana verde, hierba fresca",
            "copa": 3.5,
            "botella": 25.0
        },
        {
            "vino": "Do Ferreiro Cepas Vellas",
            "calidad": "Alta gama",
            "explicacion": "Más mineral y complejo, ideal para sofisticar este plato.",
            "tipo": "Blanco",
            "uva": "Albariño",
            "region": "Rías Baixas",
            "notas": "Mineral, floral, fruta de hueso",
            "copa": 6.0,
            "botella": 45.0
        }
    ],
    "Tortilla española": [
        {
            "vino": "Muga Rosado",
            "calidad": "Estándar",
            "explicacion": "Equilibrado, complementa la textura de la tortilla.",
            "tipo": "Rosado",
            "uva": "Garnacha y Viura",
            "region": "Rioja",
            "notas": "Fresa, cítrico, floral",
            "copa": 3.0,
            "botella": 20.0
        },
        {
            "vino": "Chivite Las Fincas Rosado",
            "calidad": "Alta gama",
            "explicacion": "Más sofisticado y elegante, resalta los sabores del huevo y la patata.",
            "tipo": "Rosado",
            "uva": "Garnacha y Tempranillo",
            "region": "Navarra",
            "notas": "Fruta roja, pétalos de rosa, frescura",
            "copa": 5.0,
            "botella": 35.0
        }
    ],
    "Ensaladilla rusa": [
        {
            "vino": "Mar de Frades Albariño",
            "calidad": "Estándar",
            "explicacion": "Acidez refrescante que corta la untuosidad de la mayonesa.",
            "tipo": "Blanco",
            "uva": "Albariño",
            "region": "Rías Baixas",
            "notas": "Fruta tropical, salino, floral",
            "copa": 3.5,
            "botella": 24.0
        },
        {
            "vino": "Gramona Gessamí",
            "calidad": "Alta gama",
            "explicacion": "Aromático y elegante, armoniza con la delicadeza del plato.",
            "tipo": "Blanco",
            "uva": "Muscat, Sauvignon Blanc",
            "region": "Penedès",
            "notas": "Jazmín, lichi, lima",
            "copa": 5.5,
            "botella": 40.0
        }
    ],
    "Almejas a la marinera": [
        {
            "vino": "Terras Gauda",
            "calidad": "Estándar",
            "explicacion": "Marida bien con mariscos y salsas marineras.",
            "tipo": "Blanco",
            "uva": "Albariño, Loureiro",
            "region": "Rías Baixas",
            "notas": "Melocotón, limón, mineral",
            "copa": 4.0,
            "botella": 28.0
        },
        {
            "vino": "Belondrade y Lurton",
            "calidad": "Alta gama",
            "explicacion": "Complejo y elegante, eleva el perfil del plato.",
            "tipo": "Blanco fermentado en barrica",
            "uva": "Verdejo",
            "region": "Rueda",
            "notas": "Mantequilla, piña madura, tostado",
            "copa": 6.5,
            "botella": 48.0
        }
    ],
    "Pimientos de padrón": [
        {
            "vino": "Txakoli Ameztoi",
            "calidad": "Estándar",
            "explicacion": "Refrescante y chispeante, limpia el paladar del toque picante.",
            "tipo": "Blanco espumoso",
            "uva": "Hondarrabi Zuri",
            "region": "Getariako Txakolina",
            "notas": "Manzana verde, cítricos, mineral",
            "copa": 3.0,
            "botella": 22.0
        },
        {
            "vino": "Lagar de Cervera Albariño",
            "calidad": "Alta gama",
            "explicacion": "Mayor cuerpo y mineralidad para acompañar este plato ligero.",
            "tipo": "Blanco",
            "uva": "Albariño",
            "region": "Rías Baixas",
            "notas": "Pera, flores blancas, toques salinos",
            "copa": 5.0,
            "botella": 38.0
        }
    ],
    "Paella Valenciana": [
        {
            "vino": "Cune Crianza",
            "calidad": "Estándar",
            "explicacion": "Frutal y con estructura media, acompaña bien al arroz.",
            "tipo": "Tinto",
            "uva": "Tempranillo",
            "region": "Rioja",
            "notas": "Frutos rojos, vainilla, ligero tostado",
            "copa": 3.5,
            "botella": 23.0
        },
        {
            "vino": "Finca Terrerazo",
            "calidad": "Alta gama",
            "explicacion": "Más profundo y complejo, ideal si la paella lleva carne.",
            "tipo": "Tinto",
            "uva": "Bobal",
            "region": "Valencia",
            "notas": "Ciruela negra, especias, mineral",
            "copa": 6.0,
            "botella": 42.0
        }
    ],
    "Cordero asado al horno": [
        {
            "vino": "Ramón Bilbao Reserva",
            "calidad": "Estándar",
            "explicacion": "Tinto con cuerpo para acompañar la intensidad del cordero.",
            "tipo": "Tinto",
            "uva": "Tempranillo",
            "region": "Rioja",
            "notas": "Fruta madura, cuero, especias",
            "copa": 4.0,
            "botella": 30.0
        },
        {
            "vino": "Pago de Carraovejas",
            "calidad": "Alta gama",
            "explicacion": "Potente, estructurado y elegante, realza el sabor del plato.",
            "tipo": "Tinto",
            "uva": "Tinto Fino, Cabernet Sauvignon",
            "region": "Ribera del Duero",
            "notas": "Mora, vainilla, tostado",
            "copa": 7.0,
            "botella": 55.0
        }
    ],
    "Merluza a la gallega": [
        {
            "vino": "Albariño Martín Códax",
            "calidad": "Estándar",
            "explicacion": "Fresco y ligero, marida bien con pescados blancos.",
            "tipo": "Blanco",
            "uva": "Albariño",
            "region": "Rías Baixas",
            "notas": "Melón, manzana, hierbas",
            "copa": 3.5,
            "botella": 26.0
        },
        {
            "vino": "Valdesil Godello sobre lías",
            "calidad": "Alta gama",
            "explicacion": "Más cremoso y mineral, aporta complejidad al plato.",
            "tipo": "Blanco",
            "uva": "Godello",
            "region": "Valdeorras",
            "notas": "Hinojo, cítricos, mineral",
            "copa": 6.0,
            "botella": 44.0
        }
    ],
    "Croquetas de jamón ibérico": [
        {
            "vino": "Viña Alberdi Reserva",
            "calidad": "Estándar",
            "explicacion": "Redondo y sabroso, acompaña el carácter del jamón.",
            "tipo": "Tinto",
            "uva": "Tempranillo",
            "region": "Rioja",
            "notas": "Cereza madura, vainilla, tabaco",
            "copa": 4.0,
            "botella": 28.0
        },
        {
            "vino": "Pesquera Reserva",
            "calidad": "Alta gama",
            "explicacion": "Más intenso y estructurado, ideal con embutidos ibéricos.",
            "tipo": "Tinto",
            "uva": "Tempranillo",
            "region": "Ribera del Duero",
            "notas": "Fruta negra, especias, roble",
            "copa": 6.5,
            "botella": 50.0
        }
    ],
    "Pollo al ajillo": [
        {
            "vino": "Enate Chardonnay 234",
            "calidad": "Estándar",
            "explicacion": "Su acidez contrasta con el ajo, equilibrando sabores.",
            "tipo": "Blanco",
            "uva": "Chardonnay",
            "region": "Somontano",
            "notas": "Fruta blanca, mantequilla, toque cítrico",
            "copa": 3.5,
            "botella": 24.0
        },
        {
            "vino": "Remírez de Ganuza Blanco",
            "calidad": "Alta gama",
            "explicacion": "Con crianza, potencia los matices del plato.",
            "tipo": "Blanco fermentado en barrica",
            "uva": "Viura, Malvasía",
            "region": "Rioja",
            "notas": "Crema, nuez, albaricoque",
            "copa": 6.0,
            "botella": 46.0
        }
    ]
}
# --- Función para recomendar vinos ---
def recomendar_vino(plato, tipo_preferido, dulzor, region):
    vinos_disponibles = recomendaciones_vino.get(plato, [])
    # En esta versión básica, devolvemos las dos recomendaciones tal como están
    # Se puede mejorar aplicando filtros en función de las preferencias del usuario
    return vinos_disponibles

# --- Interfaz principal ---
st.set_page_config(page_title="Chin Chin 🍷", layout="centered")
st.title("🍷 Chin Chin: Tu Sumiller Virtual")
st.markdown("Explora maridajes únicos y encuentra el vino ideal para tu plato.")

# --- Formulario personalizado ---
with st.form("formulario_usuario"):
    nombre = st.text_input("👤 ¿Cuál es tu nombre?")
    edad = st.number_input("🎂 ¿Qué edad tienes?", min_value=0, step=1)
    genero = st.selectbox("🧑‍🤝‍🧑 ¿Cuál es tu género?", ["Prefiero no decirlo", "Femenino", "Masculino", "Otro"])
    frecuencia = st.selectbox("📅 ¿Con qué frecuencia sueles beber vino?", ["Ocasionalmente", "Semanalmente", "A diario"])
    tipo_vino = st.selectbox("🍇 ¿Qué tipo de vino prefieres?", ["Tinto", "Blanco", "Rosado", "Espumoso", "Me da igual"])
    dulzor = st.selectbox("🍬 ¿Qué nivel de dulzor prefieres?", ["Seco", "Semiseco", "Dulce", "Me da igual"])
    region_favorita = st.selectbox("🌍 Elige una región vitivinícola favorita", [
        "🌿 Ribera del Duero", "🌊 Rías Baixas", "🔥 Priorat", "🌞 La Toscana", "🌬 Borgoña", "🌄 Valle del Napa"
    ])
    plato = st.selectbox("🍽 ¿Qué plato vas a disfrutar?", list(recomendaciones_vino.keys()))
    enviar = st.form_submit_button("🔍 Buscar vinos")

# --- Resultado de recomendación ---
if enviar:
    if edad < 18:
        st.warning("🚫 Está prohibida la venta de alcohol a menores de 18 años.")
    else:
        st.success(f"🍷 Recomendaciones para {nombre}:")
        vinos = recomendar_vino(plato, tipo_vino, dulzor, region_favorita)
        if vinos:
            for vino in vinos:
                st.write(f"### {vino['calidad']} – {vino['vino']}")
                st.write(f"📝 {vino['explicacion']}")
                st.write(f"🍇 Tipo: {vino['tipo']} | Uva: {vino['uva']}")
                st.write(f"🌍 Región: {vino['region']} | Notas: {vino['notas']}")
                st.write(f"💶 Copa: {vino['copa']} € | Botella: {vino['botella']} €")
                st.markdown("---")
        else:
            st.warning("😕 Aún no tenemos una recomendación para este plato. ¡Pronto la añadiremos!")
