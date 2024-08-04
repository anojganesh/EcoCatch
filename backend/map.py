import folium 
import requests  

def make_map_with_pointer(zone, cordx, cordy, city, town, district):

    api_key = 'at_Xf1Aa1xUWfHerdvOBw08rUCX7sTUo' 

    ip_address =  requests.get('https://api.ipify.org').text 
    response = requests.get(f'https://geo.ipify.org/api/v2/country,city?apiKey={api_key}&ipAddress={ip_address}').json() 

    response['location']['lat'],response['location']['lng'] 
    lati = response['location']['lat']
    long = response['location']['lng'] 
    location_me=[cordx, cordy]
    map = folium.Map(location=location_me, zoom_start=10)

    #fishing zones on map
    folium.GeoJson("Fisheries_Management_Zone.geojson", name="Fishing Zones").add_to(map)

    file_path = "map.html" 
    # Check if the file exists 

        # Save the map to an HTML file if it doesn't exist 
    
    # Open the map in the default web browser 
    #webbrowser.open(file_path)

    #marker on map for user location

    query_coord = [cordx, cordy]
   
    if zone in ["1","2","3"]:
        folium.Marker(location=query_coord,
            popup= '<a href="https://www.ontario.ca/page/fisheries-management-zones-fmzs-1-2-and-3">Zone 1, 2, and 3 Regulations</a>', 
            tooltip= "" + city + ", " + town + ", " + district).add_to(map)

    

    if zone == "4":
        folium.Marker(location=query_coord,
            popup='<a href="https://www.ontario.ca/page/fisheries-management-zone-4-fmz-4">Zone 4 Regulations</a>', 
            tooltip= "" + city + ", " + town + ", " + district).add_to(map)


    if zone == "5":
        folium.Marker(location=query_coord,
            popup='<a href="https://www.ontario.ca/page/fisheries-management-zone-5-fmz-5">Zone 5 Regulations</a>', 
            tooltip= "" + city + ", " + town + ", " + district).add_to(map)


    if zone == "6":
        folium.Marker(location=query_coord,
            popup='<a href="https://www.ontario.ca/page/fisheries-management-zone-6-fmz-6">Zone 6 Regulations</a>', 
            tooltip= "" + city + ", " + town + ", " + district).add_to(map)


    if zone == "7":
        folium.Marker(location=query_coord,
            popup='<a href="https://www.ontario.ca/page/fisheries-management-zone-7-fmz-7">Zone 7 Regulations</a>', 
            tooltip= "" + city + ", " + town + ", " + district).add_to(map)


    if zone == "8":
        folium.Marker(location=query_coord,
            popup='<a href="https://www.ontario.ca/page/fisheries-management-zone-8-fmz-8">Zone 8 Regulations</a>', 
            tooltip= "" + city + ", " + town + ", " + district).add_to(map)
       

    if zone == "9":
        folium.Marker(location=query_coord,
            popup='<a href="https://www.ontario.ca/page/fisheries-management-zone-9-fmz-9">Zone 9 Regulations</a>', 
            tooltip= "" + city + ", " + town + ", " + district).add_to(map)


    if zone == "10":
        folium.Marker(location=query_coord,
            popup='<a href="https://www.ontario.ca/page/fisheries-management-zone-10-fmz-10">Zone 10 Regulations</a>', 
            tooltip= "" + city + ", " + town + ", " + district).add_to(map)


    if zone == "11":
        folium.Marker(location=query_coord,
            popup='<a href="https://www.ontario.ca/page/fisheries-management-zone-11-fmz-11">Zone 11 Regulations</a>', 
            tooltip= "" + city + ", " + town + ", " + district).add_to(map)
    if zone == "12":
            folium.Marker(location=query_coord,
                popup='<a href="https://www.ontario.ca/page/fisheries-management-zone-12-fmz-12">Zone 12 Regulations</a>', 
                tooltip= "" + city + ", " + town + ", " + district).add_to(map)
    if zone == "13":
            folium.Marker(location=query_coord,
                popup='<a href="https://www.ontario.ca/page/fisheries-management-zone-13-fmz-13">Zone 13 Regulations</a>', 
                tooltip= "" + city + ", " + town + ", " + district).add_to(map)


    if zone == "14":
        folium.Marker(location=query_coord,
            popup='<a href="https://www.ontario.ca/page/fisheries-management-zone-14-fmz-14">Zone 14 Regulations</a>', 
            tooltip= "" + city + ", " + town + ", " + district).add_to(map)


    if zone == "15":
        folium.Marker(location=query_coord,
            popup='<a href="https://www.ontario.ca/page/fisheries-management-zone-15-fmz-15">Zone 15 Regulations</a>', 
            tooltip= "" + city + ", " + town + ", " + district).add_to(map)


    if zone == "16":
        folium.Marker(location=query_coord,
            popup='<a href="https://www.ontario.ca/page/fisheries-management-zone-16-fmz-16">Zone 16 Regulations</a>', 
            tooltip= "" + city + ", " + town + ", " + district).add_to(map)

    if zone == "17":
        folium.Marker(location=query_coord,
            popup='<a href="https://www.ontario.ca/page/fisheries-management-zone-17-fmz-17">Zone 17 Regulations</a>', 
            tooltip= "" + city + ", " + town + ", " + district).add_to(map)

    if zone == "18":
        folium.Marker(location=query_coord,
            popup='<a href="https://www.ontario.ca/page/fisheries-management-zone-18-fmz-18">Zone 18 Regulations</a>', 
            tooltip= "" + city + ", " + town + ", " + district).add_to(map)
    if zone == "19":
        folium.Marker(location=query_coord,
            popup='<a href="https://www.ontario.ca/page/fisheries-management-zone-19-fmz-19">Zone 19 Regulations</a>', 
            tooltip= "" + city + ", " + town + ", " + district).add_to(map)

    if zone == "20":
        folium.Marker(location=query_coord,
            popup='<a href="https://www.ontario.ca/page/fisheries-management-zone-20-fmz-20">Zone 20 Regulations</a>', 
            tooltip= "" + city + ", " + town + ", " + district).add_to(map)
   # folium.PolyLine((location_me,query_coord)).add_to(map)

    print("Saving map..")  
    map.save(file_path)