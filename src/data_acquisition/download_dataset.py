import urllib.request
import zipfile

def download_dataset(url, output_zip, extract_to):
    print("Descărcare dataset...")
    urllib.request.urlretrieve(url, output_zip)
    with zipfile.ZipFile(output_zip, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print("Dataset descărcat și extras cu succes!")
