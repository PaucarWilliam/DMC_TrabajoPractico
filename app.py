import streamlit as st

st.set_page_config(
    page_title="Proyecto Modulo 1",
    page_icon="",
    layout="wide"

)

# MENU LATERAL

menu = st.sidebar.selectbox(
    "Navegacion",
    [
        "Home",
        "Ejercicio 1",
        "Ejercicio 2",
        "Ejercicio 3",
        "Ejercicio 4"
    ]
)


# ESTRUCTURA DE NAVEGACIÓN

if menu == "Home":
    st.title("Proyecto Aplicado en Streamlit – Fundamentos de Programación")

    st.write("**Nombre del estudiante:** William Samuel Kenneth Paucar Huayta")
    st.write("**Curso:** Especialización en Python for Analytics")
    st.write("**Módulo:** Python Fundamentals")
    st.write("**Año:** 2026")

    st.write("---")

    st.write("### Descripción del Proyecto")
    st.write(
        "Esta aplicación interactiva desarrollada en Streamlit integra los conceptos "
        "fundamentales aprendidos en el Módulo 1, incluyendo variables, estructuras "
        "de datos, control de flujo, funciones, programación funcional y "
        "programación orientada a objetos (POO)."
    )

    st.write("---")

    st.write("### Tecnologías Utilizadas")
    st.write("- Python")
    st.write("- Streamlit")

elif menu == "Ejercicio 1":
    st.title("Ejercicio 1")
    # Entrada de datos
    presupuesto = st.number_input(
        "Ingrese el presupuesto:", min_value=0.0, step=1.0)
    gasto = st.number_input("Ingrese el gasto:", min_value=0.0, step=1.0)

    # Boton para evaluar
    if st.button("Evaluar Presupuesto"):

        diferencia = presupuesto - gasto

        # Condicional
        if gasto <= presupuesto:
            st.success("El gasto está dentro del presupuesto.")
        else:
            st.warning("El presupuesto ha sido excedido.")

        # Mostrar diferencia
        st.write(f"Diferencia entre presupuesto y gasto: {diferencia}")

elif menu == "Ejercicio 2":
    st.title("Ejercicio 2 – Registro de Actividades Financieras")

    # Inicializa lista en sesion si no existe
    if "actividades" not in st.session_state:
        st.session_state.actividades = []

    # Inputs
    nombre = st.text_input("Nombre de la actividad:")
    tipo = st.selectbox("Tipo de actividad:", [
                        "Inversión", "Operativa", "Marketing", "Otro"])
    presupuesto = st.number_input("Presupuesto:", min_value=0.0, step=1.0)
    gasto_real = st.number_input("Gasto Real:", min_value=0.0, step=1.0)

    # Botón para agregar
    if st.button("Agregar actividad"):

        actividad = {
            "nombre": nombre,
            "tipo": tipo,
            "presupuesto": presupuesto,
            "gasto_real": gasto_real
        }

        st.session_state.actividades.append(actividad)
        st.success("Actividad agregada correctamente.")

    # Mostrar tabla
    if st.session_state.actividades:
        st.subheader("Lista de Actividades")
        st.dataframe(st.session_state.actividades)

        st.subheader("Estado de cada actividad")

        # Recorrer lista y evaluar
        for act in st.session_state.actividades:
            if act["gasto_real"] <= act["presupuesto"]:
                estado = "Dentro del presupuesto"
            else:
                estado = "Presupuesto excedido"

            st.write(f"Actividad: {act['nombre']} → {estado}")


elif menu == "Ejercicio 3":
    st.title("Ejercicio 3")

    if "actividades" not in st.session_state or not st.session_state.actividades:
        st.warning(
            "no hay activades registradas. Primero agregue actividades en el Ejercicio 2")

    else:
        # Definir la funcion
        def calcular_retorno(actividad, tasa, meses):
            return actividad["presupuesto"] * tasa * meses
        # Inputs
        tasa = st.slider("Seleccione la tasa ", min_value=0.0,
                         max_value=1.0, step=0.001)
        meses = st.number_input(
            "Ingrese la cantidad de meses", min_value=1, step=1)

        if st.button("Calcular Retorno"):
            # Usamos programacion funcional como lo requirieron map y lambda

            retornos = list(
                map(
                    lambda act: {
                        "nombre": act["nombre"],
                        "retorno_esperado": calcular_retorno(act, tasa, meses)
                    },
                    st.session_state.actividades
                )
            )
            st.subheader("Resultados del Retorno Esperado")

            for r in retornos:
                st.write(
                    f"Actividad: {r['nombre']} → Retorno esperado: {r['retorno_esperado']}")
elif menu == "Ejercicio 4":
    st.title("Ejercicio 4")
    st.title("Ejercicio 4 – Modelado con Programación Orientada a Objetos")

    # Verificar que existan actividades
    if "actividades" not in st.session_state or not st.session_state.actividades:
        st.warning("No hay actividades registradas. Primero agregue actividades en el Ejercicio 2.")
    else:

        # ==============================
        # Definición de la clase
        # ==============================

        class Actividad:

            def __init__(self, nombre, tipo, presupuesto, gasto_real):
                self.nombre = nombre
                self.tipo = tipo
                self.presupuesto = presupuesto
                self.gasto_real = gasto_real

            def esta_en_presupuesto(self):
                return self.gasto_real <= self.presupuesto

            def mostrar_info(self):
                return f"Actividad: {self.nombre} | Tipo: {self.tipo} | Presupuesto: {self.presupuesto} | Gasto Real: {self.gasto_real}"

        st.subheader("Actividades como Objetos")

        # Convertir diccionarios en objetos
        objetos_actividades = []

        for act in st.session_state.actividades:
            objeto = Actividad(
                act["nombre"],
                act["tipo"],
                act["presupuesto"],
                act["gasto_real"]
            )
            objetos_actividades.append(objeto)

        # Mostrar información de cada objeto
        for obj in objetos_actividades:
            st.write(obj.mostrar_info())

            if obj.esta_en_presupuesto():
                st.success("Cumple con el presupuesto")
            else:
                st.warning("Presupuesto excedido")

            st.write("---")
