from django.urls import path
from .views import (
    income_view, expenditure_view, reports_view, manage_budgets, update_budget,
    manage_debts, add_edit_debt, delete_debt, add_investment, update_investment, delete_investment, investment_view  # Import investment-related views
)
from . import views
from .views import download_report
urlpatterns = [
    path('income/', income_view, name='income'),
    path('expenditure/', expenditure_view, name='expenditure'),
    path('reports/', reports_view, name='reports'),
    path('manage_budgets/', views.manage_budgets, name='manage_budgets'),
    path('expenses/update/<int:expense_id>/',
         views.update_expense, name='update_expense'),
    path('expenses/delete/<int:expense_id>/',
         views.delete_expense, name='delete_expense'),
    path('incomes/update/<int:income_id>/',
         views.update_income, name='update_income'),
    path('incomes/delete/<int:income_id>/',
         views.delete_income, name='delete_income'),
    path('budgets/update/<int:budget_id>/<str:budget_type>/',
         update_budget, name='update_budget'),
    path('debts/', manage_debts, name='manage_debts'),
    path('debts/add/', add_edit_debt, name='add_debt'),
    path('debts/edit/<int:debt_id>/', add_edit_debt, name='edit_debt'),
    path('debts/delete/<int:debt_id>/', delete_debt, name='delete_debt'),
    path('download-report/', download_report, name='download_report'),
    path('investments/', investment_view, name='investment_view'),
    path('investments/add/', add_investment, name='add_investment'),
    path('investments/update/<int:pk>/', update_investment, name='update_investment'),
    path('investments/delete/<int:pk>/', views.delete_investment, name='delete_investment'),
]

