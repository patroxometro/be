import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.markdown('# Seguimiento de *alertas HMS*')
st.markdown('## Bienvenid@.')
st.markdown('#### Este sitio es para revisar el seguimiento de los estudiantes con alerta HMS en miVidaTec.')

archivo_alertas = st.file_uploader('Sube el archivo de las alertas HMS más reciente:')
archivo_reporte = st.file_uploader('Ahora, sube el reporte que descargaste de miVidaTec con los casos de acompañamiento')

if archivo_alertas:
    df_alertas = pd.read_excel(archivo_alertas)
    st.header('Alertas HMS')
    st.write(df_alertas)
    st.markdown('## Regiones y campus')
    data = df_alertas['Región']
    region_count = df_alertas['Región'].value_counts()
    campus_count = df_alertas['Campus'].value_counts()
    
    fig, (ax1, ax2) = plt.subplots(2,1, figsize=(6, 12))
    colors =  ("orange", "gold", "darkorchid", "dodgerblue", "forestgreen")
    ax1.pie(region_count, labels=region_count.index, autopct='%1.1f%%', startangle=90, colors=colors)
    ax1.axis('equal')
    ax1.set_title('Alertas por región')

    bars = ax2.bar(campus_count.index, campus_count, color='skyblue')
    ax2.set_title('Alertas por campus')
    ax2.set_xlabel('Campus')
    ax2.set_ylabel('Cantidad')
    ax2.set_xticklabels(campus_count.index, rotation=90) 
    for bar in bars:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, yval, int(yval), 
                ha='center', va='bottom', color='black')

    st.pyplot(fig)



if archivo_reporte:
    #columnas_para_usar = ['Matrícula Tec de Monterrey', 'Nombre del contacto', 'Campus/Sede', 'Zona Regional', 'Categoría', 'Subcategoría', 'Impresión Diagnóstica', 'Asunto', 'Estado', 'Estado Derivación', 'Rol', 'Tipo', 'Tipo', 'Nivel de Preocupación']
    df_reporte = pd.read_excel(archivo_reporte, skiprows=10, header=0)
    df_reporte = df_reporte[:-5]
    #df_reporte = df_reporte.drop(columns=columnas_para_usar)
    df_reporte = df_reporte[['Matrícula Tec de Monterrey', 'Nombre del contacto', 'Campus/Sede', 'Zona Regional', 'Categoría', 'Subcategoría', 'Impresión Diagnóstica', 'Asunto', 'Estado', 'Estado Derivación', 'Rol', 'Tipo', 'Nivel de Preocupación']]
    common = df_alertas[df_alertas['identificador'].isin(df_reporte['Matrícula Tec de Monterrey'])]
    df_reporte['Matrícula Tec de Monterrey'] = df_reporte['Matrícula Tec de Monterrey'].astype(str)
    common['identificador'] = common['identificador'].astype(str)
    df_seguimiento = pd.merge(common, df_reporte, left_on='identificador', right_on='Matrícula Tec de Monterrey')





    st.write(df_reporte)
    st.write(common)
    st.write(df_seguimiento)