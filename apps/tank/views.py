from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django import forms
import django_excel as excel
from pyexcel import get_sheet

from .models import Customer, List


class UploadFileForm(forms.Form):
    file = forms.FileField()


def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv",
                                       file_name="download")
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {
            'form': form,
            'title': 'Excel file upload and download example',
            'header': ('Please choose any excel file ' +
                       'from your cloned repository:')
        })


def import_customers(request):
    # todo check all ids are for request.company
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
                name_columns_by_row=2,
                model=Customer,
                mapdict=['id', 'full_name', 'first_name', 'middle_name', 'last_name', 'email', 'phone'])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()


def export_customers(request, list_pk):
    lst = get_object_or_404(List, pk=list_pk, company=request.company)
    qs = Customer.objects.filter(lists=list_pk).distinct()
    columns = ['id', 'full_name', 'first_name', 'middle_name', 'last_name']
    sheet = get_sheet(query_sets=qs, column_names=columns)
    emails = ['email']
    phones = ['phone']
    for obj in qs:
        emails.append(', '.join(obj.email))
        phones.append(', '.join(obj.phone))
    sheet.column += emails
    sheet.column += phones
    response = excel.make_response(sheet, 'xls', file_name='sheet')
    response['Content-Disposition'] = 'attachment; filename="%s_customers.xls"' % lst.name.lower().replace(' ', '_')
    return response
