import os
import zipfile
from os.path import basename


def zip(in_path):
    """
        create zip from path of directory or file
    :param in_path: path of the file/dir to zip
    :return: output file path
    """
    base = os.path.splitext(in_path)[0]
    out_path = '%s.zip' % (base)

    if os.path.isfile(in_path):
        zip_file(in_path, out_path)
    else:
        zip_directory(in_path, out_path)

    return out_path


def unzip(in_path, clean=False):
    """
        unzip file in the directory of the file
    :param in_path: path of file
    :return: output file path
    """
    # out_path = os.path.dirname(in_path)
    out_path = os.path.splitext(in_path)[0]

    zip_ref = zipfile.ZipFile(in_path, 'r')
    zip_ref.extractall(out_path)
    zip_ref.close()

    if clean:
        os.remove(in_path)

    return out_path


def zip_directory(in_path, out_path):
    """
        zip directory
    :param in_path: path of the directory to zip
    :param out_path: path of the output, it must be zip file.
    :return: None
    """
    zf = zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(in_path)
    for dirname, subdirs, files in os.walk(in_path):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            # print ('zipping %s as %s' % (os.path.join(dirname, filename),
            #                            arcname))
            zf.write(absname, arcname)
    zf.close()
    return True


def zip_file(in_path, out_path):
    """
        zip single file
    :param in_path: path of file to zip
    :param out_path: path of the output, it must be zip file.
    :return: None
    """
    zipfile.ZipFile(out_path, mode='w').write(in_path, basename(in_path))
    return True


if __name__ == '__main__':
    pass
