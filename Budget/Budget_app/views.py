from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.db.models import Sum

from Budget_app.forms import RegisterUserForm, CreateCategoryForm, CreateCountForm, CreateCountValueForm, \
    CreateTransferToCard, UserLoginForm, PasswordResetForm, PasswordResetDoneForm
from Budget_app.models import CategoriesList, CountsList, CurrencyList
from Budget_app.utils import set_remainder, set_transfer_utils, get_currency_values, get_data_from_monobank, \
    email_sender


@login_required
def home(request):
    context = {
        'count_list': CountsList.objects.filter(user_id=request.user.pk),
        'amount_count': CountsList.objects.filter(user_id=request.user.pk).aggregate(Sum('balance')),
        'category_list_income': CategoriesList.objects.filter(user_id=request.user.pk, transaction_type=True),
        'category_list_expense': CategoriesList.objects.filter(user_id=request.user.pk, transaction_type=False),
        'currency_list': CurrencyList.objects.all(),
        'currency_values': get_currency_values()
    }
    # get_data_from_monobank()
    return render(request, 'Budget_app/base.html', context)


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'Budget_app/register.html'
    success_url = reverse_lazy('b_app:login')


class AuthUserView(LoginView):
    form_class = UserLoginForm
    template_name = 'Budget_app/login.html'

    def get_success_url(self):
        return reverse_lazy('b_app:home')


@login_required
def user_logout(request):
    logout(request)
    return redirect('b_app:login')


@login_required
def create_category(request):
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user_id = request.user
            category.save()
            return redirect('b_app:home')
    return redirect('b_app:home')


@login_required
def create_count(request):
    if request.method == 'POST':
        form = CreateCountForm(request.POST)
        if form.is_valid():
            count = form.save(commit=False)
            count.user_id = request.user
            count.save()
            return redirect('b_app:home')
    return redirect('b_app:home')


@login_required
def create_transaction(request):
    if request.method == 'POST':
        form = CreateCountValueForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.remainder = set_remainder(request)
            transaction.save()
            return redirect('b_app:home')
    return redirect('b_app:home')


@login_required
def set_transfer_to_card(request):
    if request.method == 'POST':
        form = CreateTransferToCard(request.POST)
        if form.is_valid():
            set_transfer_utils(request)
            return redirect('b_app:home')
    return redirect('b_app:home')


def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email_sender(request)
            return render(request, 'Budget_app/messages_page.html', {'message': 'Лист відправлено на пошту.'})
    else:
        form = PasswordResetForm()
    return render(request, 'Budget_app/password_reset.html', {'form': form})


def password_reset_done(request, pk):
    if request.method == 'POST':
        form = PasswordResetDoneForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=pk)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('b_app:login')
    return render(request, 'Budget_app/password_reset_done.html')
