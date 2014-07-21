from django.shortcuts import render
# core django imports
from django.views.generic import TemplateView

#from blog.models import Entry


class HomeView(TemplateView):

	template_name = 'index.html'

	def get_context_data(self):
		return { 'title': 'Tic Tac Toe' }

home = HomeView.as_view()