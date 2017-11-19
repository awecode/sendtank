from django.db import IntegrityError
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


def prepare_array_field(val):
    if type(val) == str:
        return [item.strip() for item in val.split(',')]
    return [val]


def import_customers(request, list_pk):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data = request.FILES['file'].get_array()[1:]
            mapdict = ['id', 'full_name', 'first_name', 'middle_name', 'last_name', 'email', 'phone']
            new_customers = []
            customer_ids = []
            # existing_ids_in_import = []
            for datum in data:
                kgs = {}
                for index, val in enumerate(datum):
                    attr = mapdict[index]
                    if attr in ['email', 'phone']:
                        val = prepare_array_field(val)
                    kgs[attr] = val
                kgs['company_id'] = request.company.id
                customer = Customer(**kgs)
                if kgs.get('id'):
                    # existing_ids_in_import.append(kgs.get('id'))
                    cnt = Customer.objects.filter(company=request.company, id=kgs.get('id')).update(**kgs)
                    if not cnt:
                        new_customers.append(customer)
                    customer_ids.append(kgs.get('id'))
                else:
                    new_customers.append(customer)
            # id of existing customer of another company in import file would give error
            try:
                res = Customer.objects.bulk_create(new_customers)
                [customer_ids.append(cus.id) for cus in res]
            except IntegrityError:
                return HttpResponseBadRequest("ID mismatch.")
            list = get_object_or_404(List, pk=list_pk)
            list.customers.add(*customer_ids)
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
