from odoo import http
from odoo.http import request


class blog(http.Controller):
    @http.route('/blog', type='http', auth='public', website=True)
    def blog_page(self):
        BlogPost = request.env['blog.post']
        posts = BlogPost.search([], limit=10)
        
        values = {
            'posts': posts,
        }
        return request.render('web_simpasar.blog_page_template', values)
    
    @http.route('/blog/<model("blog.post"):post>', type='http', auth='public', website=True)
    def blog_post(self, post):
        values = {
            'post': post,
        }
        return request.render('web_simpasar.blog_post_template', values)