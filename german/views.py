from django.shortcuts import render
from django.core.cache import cache
from . import terms_work


def index(request):
    return render(request, "index.html")


def terms_list(request):
    terms = terms_work.get_terms_for_table()
    return render(request, "term_list.html", context={"terms": terms})
    

def examples_list(request):
    examples = terms_work.get_examples()
    return render(request, "examples_list.html", context={"examples": examples})


def add_term(request):
    return render(request, "term_add.html")


def add_example(request):
    return render(request, "example_add.html")


def send_term(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_term = request.POST.get("new_term", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif len(new_term) == 0:
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
        add_term(request)

def send_example(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_example = request.POST.get("new_example", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif len(new_example) == 0:
            context["success"] = False
            context["comment"] = "Предложение должно быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваше предложение принято"
            terms_work.write_example(new_example, new_definition)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "example_request.html", context)
    else:
        add_example(request)


def show_stats(request):
    stats = terms_work.get_terms_stats()
    return render(request, "stats.html", stats)
