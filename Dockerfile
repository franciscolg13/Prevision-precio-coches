FROM python:3.8
RUN pip install streamlit pandas scikit-learn==1.2.2
COPY src/app.py /app/
COPY model/modelo.pkl /app/model/modelo.pkl
COPY csv/car.csv /app/csv/car.csv 
WORKDIR /app
ENTRYPOINT ["streamlit", "run", "app.py"]