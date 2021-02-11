from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from .models import Photo
@login_required
def photo_list(request): # 함수형뷰의 처음 인자는 request
    # 보여줄 사진 데이터
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos}) #템플릿은 앱폴더로부터가아닌 템플릿폴더부터 쭊쭊찾아들어감

from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.shortcuts import redirect



class PhotoUploadView(LoginRequiredMixin , CreateView):
    model = Photo
    fields = ['photo', 'text'] # 작성자(author), 작성시간(created)
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            # 데이터가 올바르다면
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})


class PhotoDeleteView(DeleteView):
    model = Photo 
    success_url = '/' # << 메인으로가겠다
    template_name = 'photo/delete.html'

class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/update.html'


    
