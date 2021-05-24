%Script to send request to HERE server
%Import required packages for http interface
import matlab.net.http.*
import matlab.net.http.field.*
import matlab.net.http.io.*

%choose file to send
[fName, fPath] = uigetfile('.kml');
kFile = fopen([fPath, fName]);

%Build POST request 
kProvider = FileProvider(kFile);
request = RequestMessage( 'POST', ContentTypeField('application/binary'), kProvider);
response = send(request, 'https://m.fleet.ls.hereapi.com/2/matchroute.json?...routemode=car&apiKey=LOgrzoNNKqlKKiQGi7AnbinsfKs8KRNYocxrcvp88bU&attributes=LINK_ATTRIBUTE_FCn(*),ADAS_ATTRIB_FCn(*),SPEED_LIMITS_FCn(*),LINK_ATTRIBUTE_FCn(*)');

%close file
fclose(kFile);
