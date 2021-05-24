%process response data
data = response.Body.Data;

%initialize
No_Of_Links = length(data.RouteLinks);
start_link = 1;
end_link = No_Of_Links;

length_of_longitudes = 1;
length_of_latitudes = 1;
loopnumber = 0;
%
for i = 1:No_Of_Links
   intesectioncategory(i) = str2num(data.RouteLinks(i).attributes.LINK_ATTRIBUTE_FCN.INTERSECTION_CATEGORY);
end


%% extract data
for link_To_Investigate=start_link:end_link
loopnumber = loopnumber+1;
    % Link Latitudes
    link_latitudes_cell = split(data.RouteLinks(link_To_Investigate).attributes.ADAS_ATTRIB_FCN.HPY);
        for linksubpoint = 1: length(link_latitudes_cell)
        b = cell2mat(link_latitudes_cell(linksubpoint));
        c = strip(b,'left','[');
        c = strip(c,'right',',');
        c = strip(c,'right',']');
        d = str2double(c);
            if linksubpoint>1
                d = link_latitude(linksubpoint-1) + d;
            end
        link_latitude(linksubpoint) = d;
        end
    
    % Link Longitudes
    link_longitudes_cell = split(data.RouteLinks(link_To_Investigate).attributes.ADAS_ATTRIB_FCN.HPX);
        for linksubpoint = 1: length(link_longitudes_cell)
        b = cell2mat(link_longitudes_cell(linksubpoint));
        c = strip(b,'left','[');
        c = strip(c,'right',',');
        c = strip(c,'right',']');
        d = str2double(c);
            if linksubpoint>1
                d = link_longitude(linksubpoint-1) + d;
            end
        link_longitude(linksubpoint) = d;
        end
end

%% extract data
for link_To_Investigate=start_link:end_link
    link_latitudes_cell = split(data.RouteLinks(link_To_Investigate).attributes.ADAS_ATTRIB_FCN.HPY);
    latitudes(link_To_Investigate)=link_latitudes_cell(1);
end