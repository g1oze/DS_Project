import folium
import geopandas as gpd
import branca.colormap as cm


regions_pools = gpd.read_file('regions_pools.json')
regions_swimming = gpd.read_file('regions_swimming.json')


def make_interactive_map_1(m):
    max_count = regions_pools['total'].max()
    min_count = regions_pools['total'].min()
    colormap = cm.linear.YlGnBu_09.scale(min_count, max_count)
    colormap.add_to(m)

    def style_function(feature):
        regions_pools = feature['properties']['total']
        return {
            'fillColor': colormap(regions_pools),
            'color': 'black',
            'weight': 1,
            'fillOpacity': 0.7
        }

    folium.GeoJson(
        regions_pools,
        style_function=style_function,
        tooltip=folium.GeoJsonTooltip(
            fields=['region', 'total', '50m'],
            aliases=['Регион:', 'Количество бассейнов:',
                     'Количество "полтинников":'],
            localize=True
        )
    ).add_to(m)


def make_interactive_map_2(m):
    max_count = regions_swimming['ms_density'].max()
    min_count = regions_swimming['ms_density'].min()
    colormap = cm.linear.PuBuGn_09.scale(min_count, max_count)
    colormap.add_to(m)

    def style_function(feature):
        regions_swimming = feature['properties']['ms_density']
        return {
            'fillColor': colormap(regions_swimming),
            'color': 'black',
            'weight': 1,
            'fillOpacity': 0.7
        }

    folium.GeoJson(
        regions_swimming,
        style_function=style_function,
        tooltip=folium.GeoJsonTooltip(
            fields=['region', 'ms_quant', 'ms_density'],
            aliases=['Регион:', 'Количество МС по плаванию:',
                     'Число МС по плаванию на 100 тыс. жителей:'],
            localize=True,
        )
    ).add_to(m)
