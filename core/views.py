from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView,ListView,DeleteView,FormView,CreateView,UpdateView
from .models import  Post
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .form import PostForm 
# Create your views here.
def index(request):
    return render(request,'core/index.html')


class HomeView(ListView):
    model = Post
    template_name = 'core/index.html'
    context_object_name = 'posts'
    paginate_by = 3
    paginate_orphans =  2
    
    # def get_queryset(self):
    #     query = super().get_queryset()
    #     return query.filter(title__contains = 'dasturlash')
    
    def get_queryset(self):
        search = self.request.GET.get('search')
        if search :
            return super().get_queryset().filter(Q(title__contains = search) | Q(content__contains = search))
        else:
            return super().get_queryset()
        
    def get_context_data(self, **kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)
        query = self.request.GET.copy()
        if "page" in query:
            query.pop('page')
        context['query_param'] = query.urlencode()
        
        return context
class PostDetailView(DeleteView):
    model = Post
    template_name = 'core/detail_post.html'


    def get_objet(self,query_set=None):
        query_set = Post.objects.filter(title__contains = 'Dasturlash ')
        return get_object_or_404(query_set,pk=2 )
    
    
    
    
class PostFormView(FormView):
    form_class = PostForm
    template_name = 'core/create_post.html'
    success_url = "/"
    
    

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']
    success_url = '/'
    template_name = 'core/create_post.html'
    
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'core/confirm.html'