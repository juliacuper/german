from django.shortcuts import render, redirect
from django.core.cache import cache
from . import terms_work


def index(request):
    return render(request, "index.html")


def terms_list(request):
    terms = terms_work.get_terms_for_table()
    return render(request, "term_list.html", context={"terms": terms})


def add_term(request):
    return render(request, "term_add.html")


def send_term(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_term = request.POST.get("new_term", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}

        if not new_definition:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif not new_term:
            context["success"] = False
            context["comment"] = "Термин должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            terms_work.write_term(new_term, new_definition)

        if context["success"]:
            context["success-title"] = ""

        return render(request, "term_request.html", context)
    else:
        return redirect('add_term')  # предполагается, что у вас есть URL с именем 'add_term'


def show_stats(request):
    stats = terms_work.get_terms_stats()
    return render(request, "stats.html", context={"stats": stats})  # добавлен контекст для stats
