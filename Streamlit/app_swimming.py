import streamlit as st
import folium
from streamlit_folium import folium_static
from maps import make_interactive_map_1, make_interactive_map_2

map_1 = folium.Map(location=[64.6863136, 97.7453061], zoom_start=3)
map_2 = folium.Map(location=[64.6863136, 97.7453061], zoom_start=3)


def predict_ms(population, pools):
    ms_quant = population * 0.00003 + pools * 0.76279
    if pools != 0 and population != 0:
        return round(ms_quant)
    else:
        return 0


st.title('Приложение к проекту')
st.caption("Здесь предлагаю просто посмотреть на те вещи, которые в должной мере не оценить в самом ноутбуке")

st.header("Предсказательная модель.", divider='blue')
st.subheader(
    "Количество МС по плаванию, исходя из данных по населению и числу бассейнов.")
population = st.slider("Число жителей в регионе:", 0,
                       15000000, 2000000)
pools = st.slider("Число бассейнов в регионе:", 0, 300, 50)
st.write('Предполагаемое число Мастеров Спорта по плаванию в регионе:',
         predict_ms(population, pools))


st.header("Интерактивная карта 1.", divider='blue')
st.subheader("Количество бассейнов в регионах России")
make_interactive_map_1(map_1)
folium_static(map_1)


st.header("Интерактивная карта 2.", divider='blue')
st.subheader('Количество МС по плаванию и их "плотность".')
make_interactive_map_2(map_2)
folium_static(map_2)

st.caption(
    'Спасибо тебе, грейдер, что посмотрел мой проект! Надеюсь, было интересно.')
