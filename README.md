# Paris Metro Mapping
Paris Metro Mapping. Code/Idea started in the Graph Theory Project.

- graph 19 = Paris metro interchange graph.

# Technicalities about the metro interchange graph :
- The vertices are the different correspondences of Paris's metro wether it is with another metro line or anything else.
- The values of the arcs is the distance from one correspondence to the next in terms of number of station.
- When they were 2 metro lines that contained the same arc, we only kept 1.
- When they were 2 metro lines that contained the same arc but with different values, we kept the smallest value ignoring the time to change line.
- We did not include the correspondence between Carrefour - Pleyel and Saint-Denis - Pleyel since we have to walk outside between the 2 but kept the vertex in case we changed our minds.
- We did not include the correspondence between Saint-Augustin and Saint-Lazare since they are linked by an underground corridor, and it is weird on the metro plan but kept the vertex in case we changed our minds.


folium display :
Show the metro graph in browser with an HTML file. 
also possible: with all stations.

nodes bleues = seulement les stations des 16 (1à14+3bis+7bis) métros qui ont des connexions à d'autres lignes + les terminus.
nodes violets = all others stations (n'inclut pas les bus) - si vous cliquez dessus vous verrez le nom des stations.

