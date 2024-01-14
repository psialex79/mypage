from django.shortcuts import render

def eduhelperlogpage(request):
    return render(request, 'eduhelperlog/eduhelperlog.html')
