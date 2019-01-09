from django.urls.conf import path

from qanda import views

app_name = 'qanda'
urlpatterns = [
    path('', views.TodayQuestionList.as_view(), name='index'),
    path('ask', views.AskQuestionView.as_view(), name='ask'),
    path('q/<int:pk>', views.QuestionDetailView.as_view(), name='question_detail'),
    path('q/<int:pk>/answer', views.CreateAnswerView.as_view(), name='answer_question'),
    path('q/search', views.SearchView.as_view(), name='question_search'),
    path('a/<int:pk>/accept', views.UpdateAnswerAcceptance.as_view(), name='update_answer_acceptance'),
    path('daily/<int:year>/<int:month>/<int:day>/',
         views.DailyQuestionList.as_view(), name='daily_questions'),
]
