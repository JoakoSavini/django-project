from datetime import date

""" para obtener el año """
def get_current_year(request):
    return{
        'current_year' : date.today().year
    }

""" para obtener el dia """
def get_current_hour(request):
    return{
        'current_hour' : date.today().today          
    }   
