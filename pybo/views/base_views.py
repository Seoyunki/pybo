from django.core.paginator import Paginator 
from django.shortcuts import render, get_object_or_404
import logging

logger = logging.getLogger('pybo')

from ..models import Question

def index(request):
    logger.info("INFO 레벨로 출력")
    ## pybo 목록 출력
    # 입력인자
    page = request.GET.get('page', '1')
    # 조회
    question_list = Question.objects.order_by('-create_date')
    # 페이징 처리
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list' : page_obj}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    ## 내용 출력
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)