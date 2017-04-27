from django.views.generic.edit import FormView
from feedback.forms import FeedbackForm,UploadFileform

#from feedback.tasks import amazon_uploader,create_thumb

def UploadFile(request):
    if request.method=='post':
        form = UploadFileForm(request.POST,request.files)
        if form.is_valid():
            # how request.FILES does it's work?
            
            handle_uploaded_file(request.FILES['file']):
            return HttpResponseRedirect('/success/url/')
        else:
            form = UploadFileForm()
        return render(request,'feedback/contact.html',{'form': form})
    
class FeedbackView(FormView):
    template_name = 'feedback/contact.html'
    form_class = FeedbackForm
    success_url = '/'

    def form_valid(self, form):
  #      amazon_uploader.delay()
   #     create_thumb.delay()
        return super(FeedbackView, self).form_valid(form)

