from flask import render_template, request, Blueprint, flash, url_for
from web.test.TestFunctions import get_book, word_list, check_word
from web.main.forms import PostForm, ButtonForm, ChoiceForm

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')


@main.route('/about')
def about():
	return render_template('about.html', title='About')
    

@main.route('/test', methods=['GET', 'POST'])
def test():
    global words
    global points
    global started
    button = ButtonForm()
    choice = ChoiceForm()
    form = PostForm()
    if form.validate_on_submit():
        if check_word(list(words)[0],form.content.data):
            points += 1
            flash('Správne!', 'success')
        else:
            flash('Nesprávne. Správny preklad je: ' + list(words)[0], 'danger')
        words.pop(list(words)[0])
        return render_template('test_between.html',form=button)
    if choice.is_submitted():
        if started == 0:
            book = get_book(int(request.args.get('book')))
            words = word_list(int(choice.number.data), book[int(choice.unit.data)])
            points = 0
            started = 1
            return render_template('test.html',form=form, words=words, listed=list(words))
        else:
            if len(list(words)) == 0:
                words = None
                return render_template('test_results.html',points=points)
            else:
                return render_template('test.html',form=form, words=words, listed=list(words))
    else:
        started = 0
    try:
        if words is not None:
            if len(list(words)) == 0:
                words = None
                return render_template('test_results.html',points=points)
    except NameError:
        pass
    return render_template('test_settings.html',form=choice)
    

@main.route('/test_settings', methods=['GET', 'POST'])
def test_settings():
    form = ButtonForm()
    if form.is_submitted():
        book = get_book(0)
        words = word_list(10, book[7])
        points = 0
        return render_template('test.html',form=PostForm(), words=words, listed=list(words))
    return render_template('test_settings.html', form=form)