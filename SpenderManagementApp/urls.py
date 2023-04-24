from django.urls import path
from . import views

urlpatterns=[
    path('',views.openLoginForm),
    path('signup',views.openUserForm),
    path('register',views.registerUser),
    path('dashboard',views.openDashboard),
    path('ExpenseForm',views.OpenExpenseForm),
    path('IncomeForm',views.openIncomeForm),
    path('recordexpense',views.recordExpense),
    path('recordincome',views.recordIncome),
    path('fetchallexpenses',views.fetchAllExpenses),
    path('fetchallincomes',views.fetchAllIncomes),
    path('login',views.perFormLogin),
    path('logout',views.logout),
    path('delete/<int:id>',views.deleteExpense),
    path('remove/<int:id>',views.deleteIncome),
    path('edit/<int:id>',views.openEditForm),
    path('update/<int:id>',views.updateIncome)
]