from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Mentor
from .forms import MentorForm
from .serializers import MentorSerializer

def mentor_list(request):
    mentors = Mentor.objects.filter(is_available=True)
    return render(request, 'mentor/mentor_list.html', {'mentors': mentors})

@login_required
def mentor_create(request):
    if request.method == 'POST':
        form = MentorForm(request.POST)
        if form.is_valid():
            mentor = form.save(commit=False)
            mentor.user = request.user
            mentor.save()
            messages.success(request, 'Mentor profile created successfully!')
            return redirect('mentor:mentor_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = MentorForm()
    return render(request, 'mentor/mentor_create.html', {'form': form})

def mentor_detail(request, pk):
    mentor = get_object_or_404(Mentor, pk=pk)
    return render(request, 'mentor/mentor_detail.html', {'mentor': mentor})

# API views
class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['get'])
    def available(self, request, pk=None):
        mentor = self.get_object()
        return Response({
            'is_available': mentor.is_available,
            'hourly_rate': mentor.hourly_rate
        }) 