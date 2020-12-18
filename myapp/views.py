from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
from .scoring import scoring1, scoring2, runScoring
from django.db.models import Max


def renderPage(request, message='Upload as many files as you want. Only the best score will be shown on the leaderboard at the end of the competition.', form=DocumentForm()):
    documents = Document.objects.values(
        'team').annotate(max_score1=Max('score1'), max_score2=Max('score2'), last_date=Max('date')).order_by('-max_score2', '-max_score1')

    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'list.html', context)


def my_view(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            teamname = form.cleaned_data["team"]
            if teamname == '_':
                return renderPage(
                    request, message='Select a correct team', form=form)

            newdoc = Document(docfile=request.FILES['docfile'])

            if request.FILES['docfile'].size > 1024 * 1000:
                message = f"file size is too large ! {request.FILES['docfile'].size}"
                return renderPage(request, message)

            newdoc.team = teamname

            ret, score = False, 0.
            dres = "---"
            if form.cleaned_data["challenge_id"] == "d1":
                dres = "1 (small)"
                ret, score = runScoring(scoring1, newdoc.docfile)
                if ret:
                    newdoc.score1 = score

            elif form.cleaned_data["challenge_id"] == "d2":
                dres = "2 (large)"
                ret, score = runScoring(scoring2, newdoc.docfile)
                if ret:
                    newdoc.score2 = score

            if ret:
                message = f"The file has been received correctly for dataset {dres}; your score is {score:.4f} and is now stored on the database. "
                newdoc.save()
            else:
                message = "A problem occurred with the scoring. Check the sanity of your csv file!"

            # Redirect to the document list after POST
            return renderPage(request, message)
        else:
            renderPage(
                request, message='The form is not valid. Fix the following error:', form=form)

    return renderPage(request)
