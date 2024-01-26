from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from django.db.models import Sum
import datetime

# Create your views here.
def index(request):

    if request.method == "POST":
        expense = ExpenseForm(request.POST)

        if expense.is_valid:
            expense.save()
            return redirect('index')

    else:
        expenses = Expense.objects.all()

        # calculating total expenses
        total_expenses = expenses.aggregate(Sum('amount'))
        
        # calculating 365 day expenses
        last_year = datetime.date.today() - datetime.timedelta(days=365)
        data = Expense.objects.filter(date__gt=last_year) 
        yearly_sum = data.aggregate(Sum('amount'))

        # / last months expensese
        last_month = datetime.date.today() - datetime.timedelta(days=30)
        data = Expense.objects.filter(date__gt=last_month)
        monthly_sum = data.aggregate(Sum('amount'))

        # / last weeks expensese
        last_week = datetime.date.today() - datetime.timedelta(days=7)
        data = Expense.objects.filter(date__gt=last_week)
        weekly_sum = data.aggregate(Sum('amount'))


        daily_sums = Expense.objects.filter().values('date').order_by('date').annotate(sum=Sum('amount'))
        
        categorical_sums = Expense.objects.filter().values('category').order_by('category').annotate(sum=Sum('amount'))
        print(categorical_sums)

        expense_form = ExpenseForm()

    return render(request, 'myapp/index.html', {'expense_form': expense_form, 'expenses': expenses, 'total_expenses': total_expenses, 'yearly_sum': yearly_sum, 'monthly_sum': monthly_sum, 'weekly_sum': weekly_sum, 'daily_sums': daily_sums, 'categorical_sums': categorical_sums})


# edit view
def edit(request, id):
    expense = Expense.objects.get(id=id)
    expense_form = ExpenseForm(instance=expense)

    if request.method =="POST":
        expense = Expense.objects.get(id=id)
        form = ExpenseForm(request.POST,instance=expense)

        if form.is_valid():
            form.save()
            return redirect('index')
        
    return render(request, 'myapp/edit.html', {'expense_form': expense_form})


# delete view
def delete(request, id):
    if request.method == "POST" and 'delete' in request.POST:
        expense = Expense.objects.get(id=id)
        expense.delete()
    return redirect('index')
