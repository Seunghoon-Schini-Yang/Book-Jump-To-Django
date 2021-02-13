from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from ..models import Question

def index(request) :
    # 페이지
    page = request.GET.get('page', '1')

    # pybo 목록 출력
    question_list = Question.objects.order_by('-create_date')  # '-' : 역순

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list':page_obj}

    # return HttpResponse("안녕하세요, pybo에 온 것을 환영합니다.")

    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id) :
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)