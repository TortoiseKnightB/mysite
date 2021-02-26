from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from comment.models import Comment
from comment.forms import CommentForm
from django.http import JsonResponse
from django.core.mail import send_mail
from mysite import settings


# Create your views here.
def update_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    comment_form = CommentForm(request.POST, user=request.user)  # user 参数实现判断用户是否登录，具体见 CommentForm 的 init
    data = {}

    if comment_form.is_valid():
        # 检查通过，保存数据
        comment = Comment()
        comment.user = comment_form.cleaned_data['user']
        comment.text = comment_form.cleaned_data['text']
        comment.content_object = comment_form.cleaned_data['content_object']

        parent = comment_form.cleaned_data['parent']
        if parent:
            comment.root = parent.root if parent.root else parent
            comment.parent = parent
            comment.reply_to = parent.user
        comment.save()

        # 发送邮件通知
        comment.send_mail()

        # 返回数据
        data['status'] = 'SUCCESS'
        data['username'] = comment.user.get_nickname_or_username()
        data['comment_time'] = comment.comment_time.timestamp()
        data['text'] = comment.text
        data['content_type'] = ContentType.objects.get_for_model(comment).model
        if parent:
            data['reply_to'] = comment.reply_to.get_nickname_or_username()
        else:
            data['reply_to'] = ''
        data['pk'] = comment.pk
        data['root_pk'] = comment.root.pk if comment.root else ''
        # return redirect(referer)
    else:
        # return render(request, 'error.html', {'message': comment_form.errors, 'redirect_to': referer})
        data['status'] = 'ERROR'
        data['message'] = list(comment_form.errors.values())[0][0]
    return JsonResponse(data)

    # referer = request.META.get('HTTP_REFERER', reverse('home'))
    #
    # # 数据检查
    # if not request.user.is_authenticated:
    #     return render(request, 'error.html', {'message': '用户未登录', 'redirect_to': referer})
    # text = request.POST.get('text', '').strip()
    # if text == '':
    #     return render(request, 'error.html', {'message': '评论内容为空', 'redirect_to': referer})
    # try:
    #     content_type = request.POST.get('content_type', '')
    #     object_id = int(request.POST.get('object_id', ''))
    #     model_class = ContentType.objects.get(model=content_type).model_class()
    #     model_object = model_class.objects.get(pk=object_id)
    # except Exception as e:
    #     return render(request, 'error.html', {'message': '评论对象不存在', 'redirect_to': referer})
    #
    # # 检查通过，保存数据
    # comment = Comment()
    # comment.user = request.user
    # comment.text = text
    # comment.content_object =model_object
    # comment.save()
    # return redirect(referer)