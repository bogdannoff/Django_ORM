from django.views.generic import ListView

from main.models import Blog


class BlogAuthorsView(ListView):
    model = Blog
    template_name = 'main/blog_authors.html'
    context_object_name = 'authors'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Authors'
        return context

    def get_queryset(self):
        return Blog.objects.raw(
            """
            SELECT 
                b.id AS id,
                b.name AS blog,
                COUNT(DISTINCT ea.author_id) AS authors
            FROM main_blog AS b 
                LEFT JOIN main_entry AS e 
                    ON b.id=e.blog_id
                LEFT JOIN main_entry_authors AS ea 
                    ON e.id=ea.entry_id
            GROUP BY 
                b.id,
                b.name
            ORDER BY 
                b.name ASC 
            """
        )

