import streamlit as st
import pandas as pd
import joblib

clf = joblib.load("model/modelo.pkl")

st.title("¡Calcula el precio de los coches en Pakistan!")


# Seleccionamos la marca de coches junto a sus modelos.

car = st.selectbox(
    '¿Qué modelo de coche quieres ver?',
    ("Suzuki", "Honda", "Toyota", "Daihatsu", "Hyundai", "Mitsubishi", "KIA", "Changan", "FAW", "Chevrolet", "Mercedes"))

if car == "Suzuki":
    model = st.selectbox(
        "¿Qué modelo buscas?",
        ('Ravi', 'Bolan', 'Swift', 'Wagon R', 'Cultus VXR', 'Every', 'Baleno', 'Mehran VXR', 'Alto', 'Cervo', 'Every Wagon', 'Liana', 'Mehran VX', 'Khyber', 'Cultus VXL'),
    )

elif car == "Honda":
        model = st.selectbox(
        "¿Qué modelo buscas?",
        ('City IDSI', 'City Vario', 'Civic Prosmetic', 'City IVTEC', 'City Aspire', 'Civic Oriel', 'Civic VTi', 'Civic EXi', 'Civic VTi Oriel')
    )
elif car == "Toyota":
        model = st.selectbox(
        "¿Qué modelo buscas?",
        ('Passo', 'Corolla XLI', 'Corrolla Altis', 'Altis Grande', 'Yaris', 'Corolla GLI', 'Corolla Assista', 'Corolla Axio', 'Surf', 'Prius', 'ISIS'),
    )
elif car == "Daihatsu":
        model= st.selectbox(
        "¿Qué modelo buscas?",
        ('Move', 'Mira', 'Terios Kid', 'Cuore', 'Hijet')
    )
elif car == "Hyundai":
        model = st.selectbox(
        "¿Qué modelo buscas?",
        ["Santro"]
    )
elif car == "Mitsubishi":
        model = st.selectbox(
        "¿Qué modelo buscas?",
        ('Pajero Mini', 'Ek Wagon', 'Lancer', 'Minicab Bravo', 'Minica')
    )
elif car == "KIA":
        model = st.selectbox(
        "¿Qué modelo buscas?",
        ('Picanto', 'Classic', 'Spectra', 'Sportage')
    )
elif car == "Changan":
        model = st.selectbox(
        "¿Qué modelo buscas?",
        ('Karvaan', 'Alsvin')
    )
elif car == "FAW":
        model = st.selectbox(
        "¿Qué modelo buscas?",
        ('X-PV', 'V2')
    )
elif car == "Chevrolet":
        model = st.selectbox(
        "¿Qué modelo buscas?",
        ('Joy', 'Exclusive')
    )
elif car == "Mercedes":
        model = st.selectbox(
        "¿Qué modelo buscas?",
        ('E Class', 'C Class')
    )

st.divider()


#El año minimo y maximo se comprueba en la comprobacion de datos.
age_car = st.slider("¿De qué año es el coche?", 1989, 2024) 
age_car_float = float(age_car)
st.write("El año es ", age_car_float)

# El valor maximo de kilometros se comprueba en la extraccion de datos.
km_car = st.number_input("¿Cuantos Kilometros tiene el coche?")
st.write("Los Kilometros recorridos son ", km_car)

st.divider()

# Tipo de combustible
gas = st.selectbox(
    "Selecciona el tipo de combustible",
    ("Petrol", "CNG", "Hybrid", "Diesel")
)

# Montaje 
assembly = st.selectbox(
    "¿Cual es la procedencia del coche?",
    ("Local", "Imported")
)

# Transmission
transmission = st.selectbox(
    "Tipo de transmision tiene del coche",
    ("Manual", "Automatic")
)

st.divider()

if st.button("Comprobar"):
    X = pd.DataFrame([[car, model, age_car_float, km_car, gas, assembly, transmission,]], columns=["Make", "Model", "Year", "KM's driven", "Fuel", "Assembly", "Transmission"])
    X["Make"] = X["Make"].replace(["Suzuki", "Honda", "Toyota", "Daihatsu", "Hyundai", "Mitsubishi", "KIA", "Changan", "FAW", "Chevrolet", "Mercedes"], [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0])
    X["Model"] = X["Model"].replace(['City IVTEC', 'Alto', 'Bolan', 'Cuore', 'Corolla GLI', 'Mehran VXR', 'Mira', 'Santro', 'Wagon R','Civic Prosmetic', 'Corolla XLI', 'Swift', 'Cultus VXR', 'City Aspire', 'Corrolla Altis', 'Yaris', 'Hijet', 'Every', 'City IDSI', 'Passo', 'Civic Oriel', 'Move', 'Baleno', 'Lancer', 'Altis Grande', 'City Vario', 'Picanto', 'Karvaan', 'Alsvin', 'Ravi', 'X-PV', 'Classic', 'Ek Wagon', 'V2', 'Terios Kid', 'Joy', 'Pajero Mini', 'Spectra', 'Exclusive', 'Sportage', 'C Class', 'E Class', 'Minica', 'Minicab Bravo', 'Civic EXi', 'Mehran VX', 'Corolla Assista', 'Civic VTi', 'Cervo', 'Corolla Axio', 'Every Wagon', 'Liana', 'Surf', 'Civic VTi Oriel', 'Khyber', 'Cultus VXL', 'Prius', 'ISIS'], [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0, 51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0])
    X["Fuel"] = X["Fuel"].replace(["Petrol", "CNG", "Hybrid", "Diesel"], [0.0, 1.0, 2.0, 3.0])
    X['Assembly'] = X['Assembly'].replace(["Local", "Imported"], [0.0, 1.0])
    X["Transmission"] = X["Transmission"].replace(["Manual", "Automatic"], [0.0, 1.0])
    #st.text(f"Tipos de datos después de conversiones: {X.dtypes}")
    prediction = clf.predict(X)[0]
    st.markdown(f"<h4>El valor estimado es: {round(prediction, 2)} Rs</h2>", unsafe_allow_html=True)