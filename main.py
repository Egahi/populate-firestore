import firebase_admin
from firebase_admin import credentials, firestore
import google.cloud
import xlrd

cred = credentials.Certificate('./firebasekey.json')
app = firebase_admin.initialize_app(cred)
store = firestore.client()

def get_documents(collection_name, state = None):
    doc_ref = store.collection(collection_name)

    try:
        if state:
            docs = doc_ref.where(u'State', u'==', state).stream()

            # the keys for entries in lagos state are in lower case
            if state == u'Lagos':
                docs = doc_ref.where(u'state', u'==', state).stream()
        else:
            docs = doc_ref.get()

        for doc in docs:
            print(f'Id: {doc.id}')

            for key, item in doc.to_dict().items():
                if key.lower() == 'coordinates':
                    print(f'{key}: ({item.latitude}, {item.longitude})')
                else:
                    print(f'{key}: {item}')

            print()

    except google.cloud.exceptions.NotFound:
        print(u'Missing data')


def batch_data(iterable, n = 1):
    length = len(iterable)

    for idx in range(0, length, n):
        yield iterable[idx : min(idx + n, length)]


def set_documents(collection_name, file_path):
    data = []
    headers = []

    work_book = xlrd.open_workbook(file_path)

    # Change 'Nort-west' to the name of the sheet in your excel work book
    # TODO: if you like advanture, and know your way around, 
    # you can modify this code block to loop over all sheets and aggregate the data
    sheet = work_book.sheet_by_name('North-West')
    sheet.cell_value(0, 0)

    for i in range(sheet.nrows):
        row_value = sheet.row_values(i)

        if i == 0:
            headers = row_value
        else:
            obj = {}

            for i in range(len(row_value) - 2):
                obj[headers[i]] = row_value[i]

            obj['Coordinates'] = firestore.GeoPoint(row_value[2], row_value[3])

            data.append(obj)
            print(obj)

    for batched_data in batch_data(data, 499):
        batch = store.batch()

        for data_item in batched_data:
            doc_ref = store.collection(collection_name).document()
            batch.set(doc_ref, data_item)

        batch.commit()

    print('Done')


def delete_documents(collection_name, state):
    doc_ref = store.collection(collection_name)

    docs = doc_ref.where(u'State', u'==', state).stream()

    batch = store.batch()

    for doc in docs:
        ref = store.collection(collection_name).document(doc.id)
        batch.delete(ref)

    batch.commit()

    print('done')

if __name__ == '__main__':
    collection_name = u'Clusters'

    # change 'data/Nort West.xlsx' to the location of your excel workbook
    # file_path = 'data/North West.xlsx'

    # set_documents(collection_name, file_path)

    # get all documents
    # get_documents(collection_name)

    # change 'Jigawa' to the name of the state 
    # whose documents you want to retrieve
    state = u'Jigawa'

    # get documents from a specific state
    get_documents(collection_name, state)

    # delete documents by states
    # delete_documents(collection_name, state)