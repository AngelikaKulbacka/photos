from flask import Blueprint, jsonify, request

import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-E73EMHE9;DATABASE=CMS;')
cursor = conn.cursor()

gallery_bp = Blueprint('gallery', __name__, url_prefix='/gallery')


@gallery_bp.route('/gallery_get_list/<int:site_id>', methods=['GET'])
def gallery_get_list(site_id):
    data = request.json
    page = data['pagination']['page']
    per_page = data['pagination']['per_page']
    cursor.execute(f'SELECT name, description FROM album WHERE gallery_id={site_id} ORDER BY id OFFSET ({(page-1)*per_page}) ROWS FETCH NEXT {per_page} ROWS ONLY')
    result = cursor.fetchall()
    albums = [{'name': row[0], 'description': row[1]} for row in result]
    return jsonify({'message': f'Albums list for site_id={site_id}', 'albums': albums})


@gallery_bp.route('/gallery_add/<int:site_id>', methods=['POST'])
def gallery_add(site_id):
    data = request.json
    name = data['name']
    description = data['description']
    cursor.execute('INSERT INTO album (name, description, gallery_id) VALUES (?, ?, ?)', name, description, site_id)
    conn.commit()
    return jsonify({'message': f'Album {name} has been added to site_id={site_id}.'})
