import csv

ruta = "C:\\Users\\gabri\\Escritorio\\GIT_gsolaromerEduca\\Sola_Gabriel_Rec_DAPI_UT2_Parte3_2M\\class.csv"

def calculate_grade(ruta):
    '''La función recibirá las notas de todos los apartados evaluados 
    de cada alumno/a y devolverá una nota final y un valor Verdadero/Falso 
    en función de si ha aprobado o suspendido. La función deberá calcular 
    la nota final mediante la siguiente fórmula, redondearla con dos decimales 
    y evaluar si el/la alumno/a ha superado la asignatura (NotaFinal >= 5):

    NotaFinal = (Practica01 + Practica02 +Practica03)/3 * 0,3 +
    max(Examen; Recuperacion)* 0,6 + Actitud * 0,1
    
    Parámetros:
        - Fichero class.csv
        - Seis float con las diferentes notas de cada alumno: 
        Practica01, Practica02, Practica03, Examen, Recuperacion, Actitud.
        
    Salida:
        - El alumno ha superado la asignatura o no.'''
    
    resultados = []

    with open(ruta, newline='', encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for fila in reader:

            Practica01 = float(fila['Practica01'].replace(",", "."))

            Practica02 = float(fila['Practica02'].replace(",", "."))

            Practica03 = float(fila['Practica03'].replace(",", "."))

            Examen = float(fila['Examen'].replace(",", "."))

            Recuperacion = float(fila['Recuperacion'].replace(",", "."))

            Actitud = float(fila['Actitud'].replace(",", "."))

            NotaFinal = (Practica01 + Practica02 + Practica03) / 3 * 0.3 + max(Examen, Recuperacion) * 0.6 + Actitud * 0.1

            NotaFinal = round(NotaFinal, 2)

            aprobado = NotaFinal >= 5

            resultados.append((NotaFinal, aprobado))

    return print(resultados)

calculate_grade(ruta)