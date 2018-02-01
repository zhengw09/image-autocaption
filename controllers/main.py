from flask import *
from werkzeug.utils import secure_filename
import os
import sys
import shutil
# from extensions import connect_to_database
#sys.path.append('../ImageCaptionGenerator')
#import predict

main = Blueprint('main', __name__, template_folder='templates')


def allowed_file(filename):
    allowed_extensions = set(['png', 'jpg', 'bmp', 'gif'])
    return '.' in filename and \
           filename.split('.')[-1].lower() in allowed_extensions


def get_caption(filename):
    os.chdir('../ImageCaptionGenerator')
    src = os.path.join('../image-autocaption/static/images', filename)
    dst = os.path.join('image/pred', filename)
    shutil.copyfile(src, dst)
    caption = predict.main()
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    return caption
    # return "test caption"


@main.route('/', methods=['GET', 'POST'])
def main_route():
    options = {}
    # username = request.args.get('username')
    # db = connect_to_database()
    # cur = db.cursor()
    # # get the users
    # query = 'select username from User;'
    # cur.execute(query)
    # requests = cur.fetchall()
    # user_list = []
    # for result in requests:
    #     user_list.append(result['username'])
    # options['user_list'] = user_list
    
    if request.method == 'POST':
        form = request.form
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('static/images', filename))
            options['post'] = True
            options['filename'] = filename
            options['caption'] = get_caption(filename)
            return render_template("index.html", **options)

    else:  # 'GET'
        options['post'] = False
        return render_template("index.html", **options)
