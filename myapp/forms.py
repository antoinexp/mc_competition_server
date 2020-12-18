from django import forms

TEAM_CHOICES = [
    ("_", "Select a team"),
    ("Markov Unchained", "Markov Unchained"),
    ("Hunyuan Taichi", "Hunyuan Taichi"),
    ("VSL", "VSL"),
    ("X/IEb", "X/IEb"),
    ("Even and Odd", "Even and Odd"),
    ("Random Walkers", "Random Walkers"),
    ("ComeOnMCAA", "ComeOnMCAA"),
    ("EPFL Bruins", "EPFL Bruins"),
    ("Life is a transient state", "Life is a transient state"),
    ("Aquarium", "Aquarium"),
    ("ThE raNDom WALkERS", "ThE raNDom WALkERS"),
    ("Metropolis Unchained", "Metropolis Unchained"),
    ("DHA", "DHA"),
    ("The Wise Birds", "The Wise Birds"),
    ("MarkovMiracle", "MarkovMiracle"),
    ("Markov Polo", "Markov Polo"),
    ("Aleandro & the Aleandroz", "Aleandro & the Aleandroz"),
    ("M(Ch)a(ins)rkov", "M(Ch)a(ins)rkov"),
    ("Lost in Metropolis", "Lost in Metropolis"),
    ("The Unchained", "The Unchained"),
    ("OMN", "OMN"),
    ("Corentin & Khalil", "Corentin & Khalil"),
    ("TA Team", "TA Team")
]

CHOICES = [('d1', 'dataset 1 (small) with λ=1.00'),
           ('d2', 'dataset 2 (large) with λ=1.25')]


class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')
    team = forms.CharField(label='Team name', max_length=100,
                           widget=forms.Select(choices=TEAM_CHOICES))

    challenge_id = forms.ChoiceField(
        choices=CHOICES, widget=forms.RadioSelect)
