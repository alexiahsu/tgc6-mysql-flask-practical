from flask import Flask, render_template, request, redirect, url_for
import pymysql
from dotenv import load_dotenv
import os

# 1. Load in the environment variables
load_dotenv()

# 2. Create the connection
conn = pymysql.connect(host="localhost",
                       user=os.environ.get("DB_USER"),
                       password=os.environ.get("DB_PASSWORD"),
                       database="Chinook"
                       )

# 3. Create the cursor
cursor = conn.cursor(pymysql.cursors.DictCursor)

app = Flask(__name__)

# Begin CRUD


@app.route('/mediatype')
def show_mediatype():
    sql = f"select * from MediaType"
    cursor.execute(sql)
    return render_template("show_mediatype.template.html", all_mediatype=cursor)

##Update form
@app.route('/mediatype/update/<mediatype_id>')
def display_update_mediatype_form(mediatype_id):
    sql = f"select * from MediaType where MediaTypeId={mediatype_id}"
    cursor.execute(sql)
    mediatype = cursor.fetchone()
    return render_template("update_mediatype_form.template.html", mediatype=mediatype)


@app.route('/mediatype/update/<mediatype_id>', methods=["POST"])
def process_update_mediatype(mediatype_id):
    sql = f"""
    UPDATE MediaType SET Name='{request.form.get('mediatype_name')}'
    WHERE MediaTypeId={mediatype_id}
    """
    cursor.execute(sql)
    conn.commit()
    return redirect(url_for('show_mediatype'))

##Create new mediatype
@app.route('/mediatype/create')
def show_create_mediatype():
    return render_template('create_mediatype.template.html')



@app.route('/mediatype/create', methods=["POST"])
def process_create_mediatype():
    mediatype_name = request.form.get("mediatype_name")

    sql = f"""
    insert into MediaType (Name) values ("{mediatype_name}")
    """
    cursor.execute(sql)
    new_mediatype_id = cursor.lastrowid
    conn.commit()
    return redirect(url_for('show_mediatype'))
    
##Delete MediaType
@app.route('/mediatype/delete/<mediatype_id>')
def show_delete_mediatype(mediatype_id):
    sql = f"select * from MediaType where MediaTypeId={mediatype_id}"
    cursor.execute(sql)
    mediatype = cursor.fetchone()
    return render_template('confirm_delete_mediatype.template.html', mediatype=mediatype)

@app.route('/mediatype/delete/<mediatype_id>', methods=["POST"])
def process_delete_mediatype(mediatype_id):
    sql = f"delete from MediaType where MediaTypeId={mediatype_id}"
    cursor.execute(sql)
    conn.commit()
    return redirect(url_for('show_mediatype'))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
