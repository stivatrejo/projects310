#!/usr/bin/env python
# coding: utf-8

# # ¡Hola  !🙋🏻‍♂️
# 
# Te escribe Lisandro Saez, soy revisor de código en Tripleten y tengo el agrado de revisar el proyecto que entregaste.
# 
# Para simular la dinámica de un ambiente de trabajo, si veo algún error, en primer instancia solo los señalaré, dándote la oportunidad de encontrarlos y corregirlos por tu cuenta. En un trabajo real, el líder de tu equipo hará una dinámica similar. En caso de que no puedas resolver la tarea, te daré una información más precisa en la próxima revisión.
# 
# Encontrarás mis comentarios más abajo - **por favor, no los muevas, no los modifiques ni los borres**.
# 
# ¿Cómo lo voy a hacer? Voy a leer detenidamente cada una de las implementaciones que has llevado a cabo para cumplir con lo solicitado. Verás los comentarios de esta forma:
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si todo está perfecto.
# </div>
# 
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si tu código está bien pero se puede mejorar o hay algún detalle que le hace falta. Se aceptan uno o dos comentarios de este tipo en el borrador, pero si hay más, deberías hacer las correcciones. Es como una tarea de prueba al solicitar un trabajo: muchos pequeños errores pueden hacer que un candidato sea rechazado.
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si de pronto hace falta algo o existe algún problema con tu código o conclusiones.
# </div>
# 
# Puedes responderme de esta forma (no te preocupes, no es obligatorio):
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Hola, muchas gracias por tus comentarios y la revisión.
# </div>
# 
# ¡Empecemos!

# # Déjame escuchar la música

# # Contenido <a id='back'></a>
# 
# * [Introducción](#intro)
# * [Etapa 1. Descripción de los datos](#data_review)
#     * [Conclusiones](#data_review_conclusions)
# * [Etapa 2. Preprocesamiento de datos](#data_preprocessing)
#     * [2.1 Estilo del encabezado](#header_style)
#     * [2.2 Valores ausentes](#missing_values)
#     * [2.3 Duplicados](#duplicates)
#     * [2.4 Conclusiones](#data_preprocessing_conclusions)
# * [Etapa 3. Prueba de hipótesis](#hypothesis)
#     * [3.1 Hipótesis 1: actividad de los usuarios y las usuarias en las dos ciudades](#activity)
# * [Conclusiones](#end)

# ## Introducción <a id='intro'></a>
# Como analista de datos, tu trabajo consiste en analizar datos para extraer información valiosa y tomar decisiones basadas en ellos. Esto implica diferentes etapas, como la descripción general de los datos, el preprocesamiento y la prueba de hipótesis.
# 
# Siempre que investigamos, necesitamos formular hipótesis que después podamos probar. A veces aceptamos estas hipótesis; otras veces, las rechazamos. Para tomar las decisiones correctas, una empresa debe ser capaz de entender si está haciendo las suposiciones correctas.
# 
# En este proyecto, compararás las preferencias musicales de las ciudades de Springfield y Shelbyville. Estudiarás datos reales de transmisión de música online para probar la hipótesis a continuación y comparar el comportamiento de los usuarios y las usuarias de estas dos ciudades.
# 
# ### Objetivo:
# Prueba la hipótesis:
# 1. La actividad de los usuarios y las usuarias difiere según el día de la semana y dependiendo de la ciudad.
# 
# 
# ### Etapas
# Los datos del comportamiento del usuario se almacenan en el archivo `/datasets/music_project_en.csv`. No hay ninguna información sobre la calidad de los datos, así que necesitarás examinarlos antes de probar la hipótesis.
# 
# Primero, evaluarás la calidad de los datos y verás si los problemas son significativos. Entonces, durante el preprocesamiento de datos, tomarás en cuenta los problemas más críticos.
# 
# Tu proyecto consistirá en tres etapas:
#  1. Descripción de los datos.
#  2. Preprocesamiento de datos.
#  3. Prueba de hipótesis.
# 
# 
# 
# 
# 
# 
# 

# [Volver a Contenidos](#back)

# ## Etapa 1. Descripción de los datos <a id='data_review'></a>
# 
# Abre los datos y examínalos.

# Necesitarás `pandas`, así que impórtalo.

# In[2]:


import pandas as pd # Importar pandas


# Lee el archivo `music_project_en.csv` de la carpeta `/datasets/` y guárdalo en la variable `df`:

# In[3]:


df = pd.read_csv('/datasets/music_project_en.csv')# Leer el archivo y almacenarlo en df


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Bien hecho! Siempre es importante que pasemos el set de datos que estamos usando a `DataFrame`!</div>
# 

# Muestra las 10 primeras filas de la tabla:

# In[8]:


print(df.head(10))# Obtener las 10 primeras filas de la tabla df


# Obtén la información general sobre la tabla con un comando. Conoces el método que muestra la información general que necesitamos.

# In[9]:


df.info()# Obtener la información general sobre nuestros datos


# Estas son nuestras observaciones sobre la tabla. Contiene siete columnas. Almacenan los mismos tipos de datos: `object`.
# 
# Según la documentación:
# - `' userID'`: identificador del usuario o la usuaria;
# - `'Track'`: título de la canción;
# - `'artist'`: nombre del artista;
# - `'genre'`: género de la pista;
# - `'City'`: ciudad del usuario o la usuaria;
# - `'time'`: la hora exacta en la que se reprodujo la canción;
# - `'Day'`: día de la semana.
# 
# Podemos ver tres problemas con el estilo en los encabezados de la tabla:
# 1. Algunos encabezados están en mayúsculas, otros en minúsculas.
# 2. Hay espacios en algunos encabezados.
# 3. `Detecta el tercer problema por tu cuenta y descríbelo aquí`.
# No utilizan el metodo snake_case, se puede ver en la cloumna userID, con dicho metodo seria user_id.
# 
# 

# ### Escribe observaciones de tu parte. Estas son algunas de las preguntas que pueden ser útiles: <a id='data_review_conclusions'></a>
# 
# `1.   ¿Qué tipo de datos tenemos a nuestra disposición en las filas? ¿Y cómo podemos entender lo que almacenan las columnas?`
# Los datos almacenados en las filas son toods tipo object. Viendo las primeras 10 filas, se puede apreciar que todos son tipo string, aunque haya columnas con números como userID, estas son alfanúmericas, así como la columna de time, que tiene el formato HH:MM:SS. Lo que almacena cada columna, ya está descrito en las observaciones del paso anterior.
# `2.   ¿Hay suficientes datos para proporcionar respuestas a nuestra hipótesis o necesitamos más información?`
# Sí, hay suficientes datos para dar respuesta a la hipotesis, pues las columnas de genre, artist y track, nos dan informaci{on sobre el tipo de musica que se escucha, y las columnas de city y Day, nos proporcionan la informacion necesari para analizar si el compprtamiento cambia en cuanto a ciudad y día. 
# `3.   ¿Notaste algún problema en los datos, como valores ausentes, duplicados o tipos de datos incorrectos?`
# Sí, el DataFrame contiene valores ausentes, los que imposibilitan funciones importantes como count(), también duplicados tanto explícitos como implícitos, lo que generaría un mal cálculo al momento de comprobar la hipótesis. Por lo que la limpieza de datos es crucial para un buen análisis de los mismos.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Gran trabajo! Es importante que antes de encarar cualquier problema que queramos resolver con Python, nos paremos a pensar bien en qué consisten los datos con los que vamos a trabajar!
# </div>

# [Volver a Contenidos](#back)

# ## Etapa 2. Preprocesamiento de datos <a id='data_preprocessing'></a>
# 
# El objetivo aquí es preparar los datos para que sean analizados.
# El primer paso es resolver cualquier problema con los encabezados. Luego podemos avanzar a los valores ausentes y duplicados. Empecemos.
# 
# Corrige el formato en los encabezados de la tabla.
# 

# ### Estilo del encabezado <a id='header_style'></a>
# Muestra los encabezados de la tabla (los nombres de las columnas):

# In[5]:


print(df.columns)# Muestra los nombres de las columnas


# Cambia los encabezados de la tabla de acuerdo con las reglas del buen estilo:
# * Todos los caracteres deben ser minúsculas.
# * Elimina los espacios.
# * Si el nombre tiene varias palabras, utiliza snake_case.

# Anteriormente, aprendiste acerca de la forma automática de cambiar el nombre de las columnas. Vamos a aplicarla ahora. Utiliza el bucle for para iterar sobre los nombres de las columnas y poner todos los caracteres en minúsculas. Cuando hayas terminado, vuelve a mostrar los encabezados de la tabla:

# In[11]:


df.columns = [col.lower() for col in df.columns]
print(df.columns) # Bucle en los encabezados poniendo todo en minúsculas


# Ahora, utilizando el mismo método, elimina los espacios al principio y al final de los nombres de las columnas e imprime los nombres de las columnas nuevamente:

# In[12]:


df.columns = [col.strip() for col in df.columns]
print(df.columns)# Bucle en los encabezados eliminando los espacios


# Necesitamos aplicar la regla de snake_case a la columna `userid`. Debe ser `user_id`. Cambia el nombre de esta columna y muestra los nombres de todas las columnas cuando hayas terminado.

# In[13]:


df.columns = [col.replace('userid','user_id') for col in df.columns]
print(df.columns)# Cambiar el nombre de la columna "userid"


# Comprueba el resultado. Muestra los encabezados una vez más:

# In[14]:


print(df.columns)# Comprobar el resultado: la lista de encabezados


# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Te felicito, los encabezados se ven geniales!
# </div>

# [Volver a Contenidos](#back)

# ### Valores ausentes <a id='missing_values'></a>
#  Primero, encuentra el número de valores ausentes en la tabla. Debes utilizar dos métodos en una secuencia para obtener el número de valores ausentes.

# In[17]:


print(df.isna().sum())# Calcular el número de valores ausentes


# No todos los valores ausentes afectan a la investigación. Por ejemplo, los valores ausentes en `track` y `artist` no son cruciales. Simplemente puedes reemplazarlos con valores predeterminados como el string `'unknown'` (desconocido).
# 
# Pero los valores ausentes en `'genre'` pueden afectar la comparación entre las preferencias musicales de Springfield y Shelbyville. En la vida real, sería útil saber las razones por las cuales hay datos ausentes e intentar recuperarlos. Pero no tenemos esa oportunidad en este proyecto. Así que tendrás que:
# * rellenar estos valores ausentes con un valor predeterminado;
# * evaluar cuánto podrían afectar los valores ausentes a tus cómputos;

# Reemplazar los valores ausentes en las columnas `'track'`, `'artist'` y `'genre'` con el string `'unknown'`. Como mostramos anteriormente en las lecciones, la mejor forma de hacerlo es crear una lista que almacene los nombres de las columnas donde se necesita el reemplazo. Luego, utiliza esta lista e itera sobre las columnas donde se necesita el reemplazo haciendo el propio reemplazo.

# In[19]:


cols_missing_values = ['track','artist','genre']
for col in cols_missing_values:
    df[col].fillna('unknown', inplace=True)
# Bucle en los encabezados reemplazando los valores ausentes con 'unknown'


# Ahora comprueba el resultado para asegurarte de que después del reemplazo no haya valores ausentes en el conjunto de datos. Para hacer esto, cuenta los valores ausentes nuevamente.

# In[20]:


print(df.isna().sum())# Contar valores ausentes


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Te felicito por haber eliminado los NaNs! Es una parte fundamental del análisis de datos!
# </div>
# 

# [Volver a Contenidos](#back)

# ### Duplicados <a id='duplicates'></a>
# Encuentra el número de duplicados explícitos en la tabla. Una vez más, debes aplicar dos métodos en una secuencia para obtener la cantidad de duplicados explícitos.

# In[21]:


print(df.duplicated().sum())# Contar duplicados explícitos


# Ahora, elimina todos los duplicados. Para ello, llama al método que hace exactamente esto.

# In[22]:


df = df.drop_duplicates()# Eliminar duplicados explícitos


# Comprobemos ahora si eliminamos con éxito todos los duplicados. Cuenta los duplicados explícitos una vez más para asegurarte de haberlos eliminado todos:

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Te felicito por haber eliminado los duplicados! Es una parte fundamental del análisis de datos!
# </div>
# 

# In[23]:


print(df.duplicated().sum())# Comprobar de nuevo si hay duplicados



# Ahora queremos deshacernos de los duplicados implícitos en la columna `genre`. Por ejemplo, el nombre de un género se puede escribir de varias formas. Dichos errores también pueden afectar al resultado.

# Para hacerlo, primero mostremos una lista de nombres de género únicos, ordenados en orden alfabético. Para ello:
# * Extrae la columna `genre` del DataFrame.
# * Llama al método que devolverá todos los valores únicos en la columna extraída.
# 

# In[26]:


unique_genre = sorted(df['genre'].unique())

print(unique_genre)


# Busca en la lista para encontrar duplicados implícitos del género `hiphop`. Estos pueden ser nombres escritos incorrectamente o nombres alternativos para el mismo género.
# 
# Verás los siguientes duplicados implícitos:
# * `hip`
# * `hop`
# * `hip-hop`
# 
# Para deshacerte de ellos, crea una función llamada `replace_wrong_genres()` con dos parámetros:
# * `wrong_genres=`: esta es una lista que contiene todos los valores que necesitas reemplazar.
# * `correct_genre=`: este es un string que vas a utilizar como reemplazo.
# 
# Como resultado, la función debería corregir los nombres en la columna `'genre'` de la tabla `df`, es decir, remplazar cada valor de la lista `wrong_genres` por el valor en `correct_genre`.
# 
# Dentro del cuerpo de la función, utiliza un bucle `'for'` para iterar sobre la lista de géneros incorrectos, extrae la columna `'genre'` y aplica el método `replace` para hacer correcciones.

# In[32]:


def replace_wrong_genres(df, wrong_genres, correct_genre):

    for genre in wrong_genres:
        df['genre'] = df['genre'].replace(genre, correct_genre)
    return df# Función para reemplazar duplicados implícitos


# Ahora, llama a `replace_wrong_genres()` y pásale tales argumentos para que retire los duplicados implícitos (`hip`, `hop` y `hip-hop`) y los reemplace por `hiphop`:

# In[33]:


wrong_genres = ['hip', 'hop', 'hip-hop']
correct_genre = 'hiphop'

df = replace_wrong_genres(df, wrong_genres, correct_genre)# Eliminar duplicados implícitos


# Asegúrate de que los nombres duplicados han sido eliminados. Muestra la lista de valores únicos de la columna `'genre'` una vez más:

# In[34]:


print(sorted(df['genre'].unique()))# Comprobación de duplicados implícitos


# [Volver a Contenidos](#back)

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Te felicito por haber eliminado los duplicados implícitos!
# </div>
# 

# ### Tus observaciones <a id='data_preprocessing_conclusions'></a>
# 
# `Describe brevemente lo que has notado al analizar duplicados, cómo abordaste sus eliminaciones y qué resultados obtuviste.`
# Los duplicados explícitos es bastante sencillo de identificar, al buscar los duplicados implícitos, se vuelve un poco más difícil, pues se debe prestar atención a la lectura y buena interpretaci{on de los valores, pues se debe estar seguro de que se trate de lo mismo. En el caso de hiphop, fue sencillo deducir que los géneros mal escritos, se trata del mismo, pero sí hay valores un poco más complicado de ineterpretar, pues aunque el ejercicio no lo requería, hay dos géneros que pueden ser lo mismo, pero tal vez no, que es el latin y latino, probablemente sea el mismo, pero tal vez latin sea algún género de música en latin, mejor no meterse con eso. Al eliminar los duplicados, los valores cambiaron de 65079 a 61253, esa diferencia de 3826 valores, ayuda a que el análisis sea más concreto y verdadero.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Te felicito por la precisión que muestras a la hora de realizar las observaciones!</div>
# 
# 

# [Volver a Contenidos](#back)

# ## Etapa 3. Prueba de hipótesis <a id='hypothesis'></a>

# ### Hipótesis: comparar el comportamiento del usuario o la usuaria en las dos ciudades <a id='activity'></a>

# La hipótesis afirma que existen diferencias en la forma en que los usuarios y las usuarias de Springfield y Shelbyville consumen música. Para comprobar esto, usa los datos de tres días de la semana: lunes, miércoles y viernes.
# 
# * Agrupa a los usuarios y las usuarias por ciudad.
# * Compara el número de canciones que cada grupo reprodujo el lunes, el miércoles y el viernes.
# 

# Realiza cada cálculo por separado.
# 
# El primer paso es evaluar la actividad del usuario en cada ciudad. Recuerda las etapas dividir-aplicar-combinar de las que hablamos anteriormente en la lección. Tu objetivo ahora es agrupar los datos por ciudad, aplicar el método apropiado para contar durante la etapa de aplicación y luego encontrar la cantidad de canciones reproducidas en cada grupo especificando la columna para obtener el recuento.
# 
# A continuación se muestra un ejemplo de cómo debería verse el resultado final:
# `df.groupby(by='....')['column'].method()`Realiza cada cálculo por separado.
# 
# Para evaluar la actividad de los usuarios y las usuarias en cada ciudad, agrupa los datos por ciudad y encuentra la cantidad de canciones reproducidas en cada grupo.
# 
# 

# In[35]:


city_count = df.groupby(by='city')['track'].count()
print(city_count)# Contar las canciones reproducidas en cada ciudad


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Gran trabajo utilizando `groupby()` para agrupar valores por ciudad!</div>
# 

# `Comenta tus observaciones aquí`
# Al agrupar las canciones reproducidas por ciudad, podemos ver fácilmente como es que en Springfield se escucha mucha más música. Esto comprueba la mitad de nuestra hipótesis, de que el comportamiente difiere de una ciudad a otra.

# Ahora agrupemos los datos por día de la semana y encontremos el número de canciones reproducidas el lunes, miércoles y viernes. Utiliza el mismo método que antes, pero ahora necesitamos una agrupación diferente.
# 

# In[36]:


day_count = df.groupby(by='day')['track'].count()
print(day_count)# Calcular las canciones reproducidas en cada uno de los tres días


# `Comenta tus observaciones aquí`
# Al analizar los datos por día, podemos percatranos de que el comportamiento efectivamente varía. Lo que me pone a pensar en los factores que lo originen, por ejemplo, pienso que el viernes (el día que más reproducciones hay), se deba a que la gente sale y/o hace fiestas, lo que contribuya a una mayor reproducción de canciones.

# Ya sabes cómo contar entradas agrupándolas por ciudad o día. Ahora necesitas escribir una función que pueda contar entradas según ambos criterios simultáneamente.
# 
# Crea la función `number_tracks()` para calcular el número de canciones reproducidas en un determinado día **y** ciudad. La función debe aceptar dos parámetros:
# 
# - `day`: un día de la semana para filtrar. Por ejemplo, `'Monday'` (lunes).
# - `city`: una ciudad para filtrar. Por ejemplo, `'Springfield'`.
# 
# Dentro de la función, aplicarás un filtrado consecutivo con indexación lógica.
# 
# Primero filtra los datos por día y luego filtra la tabla resultante por ciudad.
# 
# Después de filtrar los datos por dos criterios, cuenta el número de valores de la columna 'user_id' en la tabla resultante. Este recuento representa el número de entradas que estás buscando. Guarda el resultado en una nueva variable y devuélvelo desde la función.

# In[38]:


def number_tracks(day,city):# Declara la función number_tracks() con dos parámetros: day= y city=.

    filtered_day =df[df['day'] == day]# Almacena las filas del DataFrame donde el valor en la columna 'day' es igual al parámetro day=

    filtered_city = filtered_day[filtered_day['city'] == city]# Filtra las filas donde el valor en la columna 'city' es igual al parámetro city=

    number_tracks = filtered_city['user_id'].count()# Extrae la columna 'user_id' de la tabla filtrada y aplica el método count()

    return number_tracks# Devolve el número de valores de la columna 'user_id'


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Te felicito por el excelente trabajo que has hecho con las funciones!</div>
# 
# 
# 
# 

# Llama a `number_tracks()` seis veces, cambiando los valores de los parámetros para que recuperes los datos de ambas ciudades para cada uno de los tres días.

# In[45]:


day= 'Monday'
city = 'Springfield'
springfield_monday = number_tracks(day, city)
print(f'El número de canciones reproducidas en {city} el lunes: {springfield_monday}') # El número de canciones reproducidas en Springfield el lunes


# In[42]:


day= 'Monday'
city = 'Shelbyville'
shelbyville_monday = number_tracks(day, city)
print(f'El número de canciones reproducidas en {city} el lunes: {shelbyville_monday}')# El número de canciones reproducidas en Shelbyville el lunes


# In[44]:


day= 'Wednesday'
city = 'Springfield'
springfield_wednesday = number_tracks(day, city)
print(f'El número de canciones reproducidas en {city} el miércoles: {springfield_wednesday}')# El número de canciones reproducidas en Springfield el miércoles


# In[43]:


day= 'Wednesday'
city = 'Shelbyville'
shelbyville_wednesday = number_tracks(day, city)
print(f'El número de canciones reproducidas en {city} el miércoles: {shelbyville_wednesday}')# El número de canciones reproducidas en Shelbyville el miércoles


# In[46]:


day= 'Friday'
city = 'Springfield'
springfield_friday = number_tracks(day, city)
print(f'El número de canciones reproducidas en {city} el viernes: {springfield_friday}')# El número de canciones reproducidas en Springfield el viernes


# In[47]:


day= 'Friday'
city = 'Shelbyville'
shelbyville_friday = number_tracks(day, city)
print(f'El número de canciones reproducidas en {city} el viernes: {shelbyville_friday}')# El número de canciones reproducidas en Shelbyville el viernes


# **Conclusiones**
# 
# `Comenta si la hipótesis es correcta o se debe rechazar. Explica tu razonamiento.`
# La hipótesis es correcta, pues como podemos apreciar en los datos arrojados por medio de la filtración, la actividad difiere en cuanto al día de la semana y la ciudad, siendo Springfield quien más actividad tiene, pero si nos fijamos bien, la actividad en ambas ciudades fluctua de la misma manera, comenzando el lunes con un número grande de reproducciones, pero decreciendo para el miércoles y llegando a su punto máximo el viernes.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Grandísimo trabajo con el análisis de hipótesis. Felicitaciones!</div>
# 

# [Volver a Contenidos](#back)

# # Conclusiones <a id='end'></a>

# `Resume aquí tus conclusiones sobre la hipótesis.`
# La hipótesis para comenzar se me hace buena, tiene fundamentos, sin embargo al ir analizando el comportamiento en ambas ciudades, surgen más dudas, como por ejemplo, el tamaño de población de ambas ciudades, las edades de los usuarios e incluso los géneros. Al tener en cuenta más factores, se vuelve más complicado el procesar los datos, pero se llega a conclusiones sobre el comportamiento más sesgadas, que pueden ayudar a tomar decisiones en cuanto a marketing o analizar problemáticas, pero muy buen ejercicio.

# ### Nota
# En proyectos de investigación reales, la prueba de hipótesis estadística es más precisa y cuantitativa. También ten en cuenta que no siempre se pueden sacar conclusiones sobre una ciudad entera a partir de datos de una sola fuente.
# 
# Aprenderás más sobre la prueba de hipótesis en el sprint de análisis estadístico de datos.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Felicitaciones por el excelente trabajo que hiciste durante todo el sprint!</div>
# 
# 
# 

# [Volver a Contenidos](#back)
