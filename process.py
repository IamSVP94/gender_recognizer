import sys,os,io,torch,cv2,numpy,json
from tqdm import tqdm


def gender_recognizer(img_file):
    def img_for_net(path):
        x = cv2.imread(path)
        x = cv2.resize(x, (134, 178))
        return torch.from_numpy(x).float().reshape(1, 3, 134, 178)
    net.eval()
    with torch.no_grad():
        out = net(img_for_net(img_file))
        if torch.argmax(out):
            return 'male'
        else:
            return 'female'


if __name__ == "__main__":
    path_dir = sys.argv[1]
    if not os.path.exists(path_dir):
        print(f'Папка не найдена! Проверьте наличие папки по адресу {path_dir}')
        raise SystemExit
    else:
        file_list = os.listdir(path_dir)
        model_path =  os.path.abspath(os.curdir)+'/net.pt'
        if not os.path.exists(model_path):
            print('Проверьте наличие модели net.pt в папке с исполняемым скриптом!')
        with open(model_path, 'rb') as model:
            buffer = io.BytesIO(model.read())
        net = torch.load(buffer, map_location=torch.device('cpu'))

        results = {file: gender_recognizer(path_dir + file) for file in tqdm(file_list) if isinstance(cv2.imread(path_dir+file), numpy.ndarray)}
        with open('process_results.json', "w", encoding="utf-8") as json_file:
            json.dump(results, json_file)