import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  vus: 1,
  duration: '10s',
};

export default function () {
  const url = 'http://localhost:4000/api/v1/load';
  const imgFile = open('./image.jpg', 'b');
  const imgData = imgFile.readAll();

  const params = {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
    tags: { name: 'test-upload' },
    data: {
      file: http.file(imgData, 'image.jpg'),
    },
  };

  http.post(url, params);
  imgFile.close();

  sleep(1);
}
