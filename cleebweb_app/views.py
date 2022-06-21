from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from cleebweb_app.models import MatchLog
from cleebweb_app.forms import LogForm

# Create your views here.
def testv(request):
    return render(request, 'cleebweb_app/base.html')


def region_list(request):
    list = MatchLog.objects.all().order_by('id')
    return render(request, 'cleebweb_app/matchlog.html', {'list': list})


def add(request, id=None):
    if id:
        log = get_object_or_404(MatchLog, pk=id)
    else:
        log = MatchLog()
    if request.method == 'POST':
        form = LogForm(request.POST, instance=log)
        if form.is_valid():
            log = form.save(commit=False)
            log.save()
            return redirect('list')
    else:
        form = LogForm(instance=log)
    return render(request, 'cleebweb_app/matchlog_add.html', dict(form=form, id=id))


def delete(request, id):
    return HttpResponse('dell')
