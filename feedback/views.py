from django.views.generic.edit import FormView
from feedback.forms import FeedbackForm
#from feedback.tasks import amazon_uploader,create_thumb


class FeedbackView(FormView):
    template_name = 'feedback/contact.html'
    form_class = FeedbackForm
    success_url = '/'

    def form_valid(self, form):
  #      amazon_uploader.delay()
   #     create_thumb.delay()
        return super(FeedbackView, self).form_valid(form)

