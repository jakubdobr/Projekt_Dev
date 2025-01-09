#uzywa lekkiego obrazu Pythona jako bazy
FROM python:3.11-slim

#ustawia folder roboczy w kontenerze na /app

WORKDIR /app

#kopiuje wszystkie pliki z repetytorium do kontenera

COPY . .

#instaluje zaleznosci z pliczku txt

RUN pip install --no-cache-dir -r requirements.txt

#udostepnienie porstu 5000 dla aplikacji ktora jest w pliku Python

EXPOSE 5000

#Uruchamia aplikacje za pomoca pliczku pythona czyli main.py

CMD ["python", "main.py"]