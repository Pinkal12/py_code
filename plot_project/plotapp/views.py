from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import numpy as np
import io
import urllib, base64
from .models import Anomaly
import xlwt



def home(request):
    # set width of bar
    barWidth = 0.25
    fig = plt.subplots(figsize =(12, 8))
 
# set of bar
    POTHOLE = [12, 40, 1, 8, 22]        
    PATCH = [28, 6, 16, 5, 10]
    WEBCRACK = [29, 3, 24, 25, 17]
    
    # Set position of bar on X axis
    br1 = np.arange(len(POTHOLE))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    
    # Make the plot
    plt.bar(br1, POTHOLE, color ='r', width = barWidth,
            edgecolor ='grey', label ='POTHOLE')
    plt.bar(br2, PATCH, color ='g', width = barWidth,
            edgecolor ='grey', label ='PATCH')
    plt.bar(br3, WEBCRACK, color ='b', width = barWidth,
            edgecolor ='grey', label ='WEBCRACK')
    
    # Adding Xticks
    plt.xlabel('Distance in meter', fontweight ='bold', fontsize = 12)
    plt.ylabel('Number of Anomalies', fontweight ='bold', fontsize = 12)
    plt.xticks([r + barWidth for r in range(len(POTHOLE))],
            ['200', '400', '600', '800', '1000'])
    
    plt.legend()
    
    fig = plt.gcf()
    #convert graph into dtring buffer and then convert 64 bit code into image
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    anomalies = Anomaly.objects.all()
    return render(request,'home.html',{'data':uri,'anomalies': anomalies})

# download_excel
def download_excel(request):
    # Create a new workbook and add a worksheet
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Anomaly Report')

    # Add column headings to the worksheet
    row_num = 0
    columns = ['Anomaly Number', 'Anomaly Type', 'Latitude', 'Longitude', 'Length', 'Width', 'Area', 'Size', 'Distance', 'Location']
    for col_num, column_title in enumerate(columns):
        print(row_num,col_num,column_title)
        ws.write(row_num, col_num, column_title)

    # Add data to the worksheet
    anomalies = Anomaly.objects.all()
    for anomaly in anomalies:
        row_num += 1
        row = [anomaly.anomaly_number, anomaly.anomaly_type, anomaly.lat, anomaly.lng, anomaly.length, anomaly.width, anomaly.area, anomaly.size, anomaly.distance, anomaly.location]
        for col_num, cell_value in enumerate(row):
            ws.write(row_num, col_num, cell_value)

    # Create a response object with the appropriate content type and content disposition headers
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="anomaly_report.xls"'

    # Write the workbook to the response object
    wb.save(response)
    return response
