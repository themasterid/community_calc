from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Bb
from django.views.generic.edit import CreateView
from .forms import BbForm
from django.urls import reverse_lazy

import datetime as dt

limit = 1000
USD_RATE = 72.0
EURO_RATE = 86.0
RUB_RATE = 1.0
CALC_ACCURACY = 2


def get_today_stats():
    today = dt.date.today()
    return sum(
        day.ammount for day in Bb.objects.all()
        if day.published == today)


def get_week_stats():
    today = dt.date.today()
    offset_week = today - dt.timedelta(days=7)
    return sum(
        day.ammount for day in Bb.objects.all()
        if offset_week <= day.published <= today)


def get_limit_today():
    return limit - get_today_stats()


def get_today_cash_remained(currency='rub'):
    money: dict = {
        'rub': (RUB_RATE, 'руб'),
        'usd': (USD_RATE, 'USD'),
        'eur': (EURO_RATE, 'Euro')
    }
    if currency not in money:
        return '<выбрана неверная валюта>'
    limit_today = get_limit_today()
    if limit_today == 0:
        return 'Денег нет, держись'
    rate_m, name_money = money[currency]
    cash_today = round(abs(limit_today) / rate_m, CALC_ACCURACY)
    if limit_today > 0:
        return f'На сегодня осталось {cash_today} {name_money}'
    return f'Денег нет, держись: твой долг - {cash_today} {name_money}'


def get_calories_remained():
    limit_today = get_limit_today()
    if limit_today > 0:
        return ('Сегодня можно съесть что-нибудь ещё, но с общей '
                f'калорийностью не более {limit_today} кКал')
    return 'Хватит есть!'


def calc(request):
    massege_money = get_today_cash_remained()
    massege_calories = get_calories_remained()

    today_stat = get_today_stats()
    week_stat = get_week_stats()
    template = 'calc/calc.html'
    posts = Bb.objects.order_by('-published')
    text = 'Тут будет калькулятор'
    context = {
        'text': text,
        'posts': posts,
        'today_stat': today_stat,
        'week_stat': week_stat,
        'limit': limit,
        'massege_money': massege_money,
        'massege_calories': massege_calories,
    }
    return render(request, template, context)


class BbCreateView(CreateView):
    template_name = 'calc/create.html'
    form_class = BbForm
    success_url = reverse_lazy('calc:calc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['published'] = Bb.objects.all()
        return context
