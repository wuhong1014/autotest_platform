from django.core.paginator import Paginator
from django.http import StreamingHttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Report
# Create your views here.
@login_required(login_url='/login/')
def report_manage(request,type):
    username = request.session.get('user', '')
    search_reportname = request.GET.get('reportname', '')
    report_search_result = Report.objects.filter(name__icontains=search_reportname,type=type).order_by('-id')
    paginator = Paginator(report_search_result, 10)
    currentPage = int(request.GET.get('page', 1))
    try:
        report_list = paginator.page(currentPage)
    except Exception:
        report_list = paginator.page(1)
    return render(request, 'report_manage.html',
                  {'user': username, 'reports': report_list, 'currentPage': currentPage,
                   'search_reportname': search_reportname,'type':type})
def report_del(request):
    report_id = request.GET.get('report_id', '')
    report_type=request.GET.get('report_type','')
    report = Report.objects.filter(id=report_id)
    report.delete()
    return redirect(reverse('report_manage',args=[report_type]))

def report_download(request):
    from django.conf import settings
    import os
    full_path=os.path.join(settings.BASE_DIR,'result')
    print(full_path)
    name=os.path.basename(request.GET['url'])
    file_name= os.path.join(full_path,name)

    def file_iterator(file_name, chunk_size=512):
        try:
            with open(file_name ,encoding='utf-8') as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break
        except FileNotFoundError as e:
            return False
    response = StreamingHttpResponse(file_iterator(file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Encoding'] = 'utf-8'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(name)
    return response



