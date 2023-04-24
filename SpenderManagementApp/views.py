from django.shortcuts import render,redirect
from . models import User,Expense,Income
# Create your views here.
def openDashboard(request):
    if 'userid' in request.session:
        userid=request.session['userid']
        user=User.objects.get(id=userid)
        expenses=user.expense_set.all()
        incomes=user.income_set.all()
        totalExpense=0  
        totalIncome=0
        for expense in expenses:
            totalExpense+=expense.amount
        for income in incomes:
            totalIncome+=income.amount
        netBalance=totalIncome-totalExpense
        return render(request,'Dashboard.html',{'net_balance':netBalance,'user':User,'total_expenses':totalExpense,'total_incomes':totalIncome})

    else:
        return redirect('/')
   
def recordExpense(request):
    if 'userid' in request.session:
        userid=request.session['userid']
        user=User.objects.get(id=userid)
        exp=Expense()
        exp.amount=request.POST['amount']
        exp.date=request.POST['date']
        exp.remarks=request.POST['remarks']
        exp.category=request.POST['category']
        exp.time=request.POST['time']
        exp.user=user
        exp.save()
        return redirect('/dashboard')
    else:
        return redirect('/')

def recordIncome(request):
    if 'userid' in request.session:
        userid=request.session['userid']
        user=User.objects.get(id=userid)
        inc=Income()
        inc.amount=request.POST['amount']
        inc.date=request.POST['date']
        inc.remarks=request.POST['remarks']
        inc.category=request.POST['category']
        inc.time=request.POST['time']
        inc.user=user
        inc.save()
        return redirect('/dashboard')
    else:
        return redirect('/')
    
    
def fetchAllExpenses(request):
    userid=request.session['userid']
    user=User.objects.get(id=userid)
    expenses=user.expense_set.all()
    return render(request,'ExpensesList.html',{'expenses':expenses})


def deleteExpense(request,id):
    delExp=Expense.objects.get(id=id)
    delExp.delete()
    return redirect('/fetchallexpenses')

def fetchAllIncomes(request):
    userid=request.session['userid']
    user=User.objects.get(id=userid)
    incomes=user.income_set.all()
    return render(request,'IncomesList.html',{'incomes':incomes})

def deleteIncome(request,id):
    delInc=Income.objects.get(id=id)
    delInc.delete()
    return redirect('/fetchallincomes')

def openEditForm(request,id):
    upInc=Income.objects.get(id=id)
    return render(request,"updateForm.html",{"updateinc":upInc})

def updateIncome(request,id):
    upInc=Income.objects.get(id=id)
    upInc.amount=request.POST['amount']
    upInc.date=request.POST['date']
    upInc.remarks=request.POST['remarks']
    upInc.category=request.POST['category']
    upInc.time=request.POST['time']
    upInc.user=User
    upInc.save()
    return redirect('/fetchallincomes')


def openLoginForm(request):
    if 'userid' in request.session:
        return redirect('/dashboard')
    return render(request,'Login.html')

def perFormLogin(request):
    email=request.POST['email']
    password=request.POST['password']
    user=User.objects.filter(email=email,password=password)
    if user:
        list=user.values()
        request.session['userid']=list[0]['id']
        return redirect('/dashboard')
    else:
        return render(request,'Login.html',{'error':'Invalid email or password!!!'})

def logout(request):
    del request.session['userid']
    return redirect('/')


def OpenExpenseForm(request):
    if 'userid' in request.session:
        userid=request.session['userid']
        return render(request,'ExpenseForm.html')
    else:
        return redirect('/')

def openIncomeForm(request):
    if 'userid' in request.session:
        userid=request.session['userid']
        return render(request,'IncomeForm.html')
    else:
        return redirect('/')

def openUserForm(request):
    return render(request,'UserForm.html')

def registerUser(request):
    user=User()
    user.name=request.POST['name']
    user.email=request.POST['email']
    user.phone=request.POST['phone']
    user.password=request.POST['password']
    user.save()
    return redirect('/dashboard')