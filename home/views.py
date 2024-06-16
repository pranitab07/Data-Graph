from django.shortcuts import render, HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
import os

def home(request):
    return render(request,'index.html')

def new(request):
    if request.method=='POST':
        file = request.FILES.get('file')
        extension = os.path.splitext(file.name)
        file_extension = extension[1].lower()
        x_axis=request.POST.get('X-axis')
        y_axis=request.POST.get('Y-axis')
        if (file_extension == '.xlsx'):
            data = pd.read_excel(file)
            #For Line Chart
            if type_new =='line':
                if file!=None:
                    data_1=pd.DataFrame(data)
                    x=list(data_1[x_axis])
                    y=list(data_1[y_axis])
                    plt.plot(x,y)
                    plt.xlabel(x_axis)
                    plt.ylabel(y_axis)
                    plt.title('Line Chart')
                    chart_path_1 = 'static/line/line_chart.png'
                    plt.savefig(chart_path_1)
                    context_1 = {'chart_path': chart_path_1}
                    plt.show()
                    return render(request,'line.html',context_1)
            
                else:
                    return render(request, 'index.html', {'error': 'Please select a file.'})
            #For Bar Chart
            elif type_new=='bar':
                if file!=None:
                    data_2=pd.DataFrame(data)   
                    x_1=list(data_2[x_axis])
                    y_1=list(data_2[y_axis])
                    plt.bar(x_1,y_1)
                    plt.xlabel(x_axis)
                    plt.ylabel(y_axis)
                    plt.title('Bar Chart')

                    chart_path_2 = 'static/bar/bar_chart.png'
                    plt.savefig(chart_path_2)
                    plt.show()

                    context_2 = {'chart':chart_path_2}
                    return render(request, 'bar.html',context_2)
                else:
                    return render(request, 'index.html', {'error': 'Please select a file.'})
            #for pie chart
            elif type_new=='pie':
                if file!=None:
                    data_3=pd.DataFrame(data)
                    var_pie=request.POST.get('pie_var')
                    print(var_pie)
                    X_2=list(data_3[var_pie])
                    total_75=0
                    total_no=0
                    total_ex=0
                    for X in X_2:
                        if (X>75):
                            total_75+=1
                        elif (X<75):
                            total_no+=1
                        else:
                            total_ex+=1
                    new_X=[total_75,total_no,total_ex]
                    Y=['greater than 75%','less then 75%','less than 50%']
                    plt.pie(new_X,labels=Y,shadow=True,autopct='%1.1f%%',startangle=90)
                    plt.legend(loc='upper left')
                    chart_path_3='static\pie\pie_3.png'
                    plt.savefig(chart_path_3)
                    plt.show()
                    context_3={'context':chart_path_3}
                    return render(request, 'pie.html',context_3)
                else:
                    return render(request, 'index.html', {'error': 'Please select a file.'})  
        else:
            data = pd.read_csv(file)
            #For Line Chart
            if type_new =='line':
                if file!=None:
                    data_1=pd.DataFrame(data)
                    x=list(data_1[x_axis])
                    y=list(data_1[y_axis])
                    plt.plot(sorted(x), sorted(y))
                    plt.xlabel(x_axis)
                    plt.ylabel(y_axis)
                    plt.title('Line Chart')
                    chart_path_1 = 'static/line/line_chart.png'
                    plt.savefig(chart_path_1)
                    context_1 = {'chart_path': chart_path_1}
                    plt.show()
                    return render(request,'line.html',context_1)
            
                else:
                    return render(request, 'index.html', {'error': 'Please select a file.'})
            #For Bar Chart
            elif type_new=='bar':
                if file!=None:
                    data_2=pd.DataFrame(data)   
                    x_1=list(data_2[x_axis])
                    y_1=list(data_2[y_axis])
                    plt.bar(x_1,y_1)
                    plt.xlabel(x_axis)
                    plt.ylabel(y_axis)
                    plt.title('Bar Chart')

                    chart_path_2 = 'static/bar/bar_chart.png'
                    plt.savefig(chart_path_2)
                    plt.show()

                    context_2 = {'chart':chart_path_2}
                    return render(request, 'bar.html',context_2)
                else:
                    return render(request, 'index.html', {'error': 'Please select a file.'})
            #for pie chart
            elif type_new=='pie':
                if file!=None:
                    data_3=pd.DataFrame(data)
                    var_pie=request.POST.get('pie_var')
                    print(var_pie)
                    X_2=list(data_3[var_pie])
                    total_75=0
                    total_no=0
                    total_ex=0
                    for X in X_2:
                        if (X>75):
                            total_75+=1
                        elif (X<75):
                            total_no+=1
                        else:
                            total_ex+=1
                    new_X=[total_75,total_no,total_ex]
                    Y=['greater than 75%','less then 75%','less than 50%']
                    plt.pie(new_X,labels=Y,shadow=True,autopct='%1.1f%%',startangle=90)
                    plt.legend(loc='upper left')
                    chart_path_3='static\pie\pie_3.png'
                    plt.savefig(chart_path_3)
                    plt.show()
                    context_3={'context':chart_path_3}
                    return render(request, 'pie.html',context_3)
                else:
                    return render(request, 'index.html', {'error': 'Please select a file.'})           
    else:
        return render(request,'index.html')
    
def selection(request):
    global type_new
    type_new=request.POST.get('graph_Type')
    type_1=type_new
    if (type_1 == 'line' or type_1=='bar'):
        return render(request,'selection.html')
    elif (type_1 == 'pie'):
        return render(request,'pei.html')
    else:
        return render(request,'index.html')
    

    


    