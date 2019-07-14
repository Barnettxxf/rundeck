import os
import datetime


def save_zip(obj, path=None):
    if path is None:
        path = os.getcwd()

    if not os.path.exists(path):
        os.makedirs(path)

    if not os.path.isdir(path):
        if not path.endswith('.zip'):
            raise ValueError('Should be saved as a zip file')
        _path = path
    else:
        _path = os.path.join(path, '_'.join([obj.project_name, datetime.datetime.now().strftime('%Y%m%d%H%M%S'), '.zip']))

    with open(_path, 'wb') as f:
        f.write(obj.zip_stream)
