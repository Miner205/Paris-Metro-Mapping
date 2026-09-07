import folium_display
import graph as g

if __name__ == '__main__':
    current_graph = g.Graph("graph 19")
    print(current_graph)
    print()
    folium_display.draw_metro_graph(current_graph, with_all_stations=False)
