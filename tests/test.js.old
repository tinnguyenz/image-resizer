import http from 'k6/http';
import { sleep, check } from 'k6';

const binFile = open('test_img.jpeg', 'b');

export let options = {
  stages: [
    { duration: '30s', target: 10 },
    { duration: '30s', target: 0 },
  ],
  thresholds: {
    http_req_duration: ['p(99)<500'],
    http_req_failed: ['rate<0.1']
  },
};

export default function () {
  const data = {
    field: 'this is a standard form field',
    file: http.file(binFile, 'image.jpg'),
  };

  let res = http.batch([
    { method: 'POST', url: 'http://localhost:4000/api/v1/upload', body: data },
    { method: 'POST', url: 'http://localhost:4000/api/v1/upload', body: data },
    { method: 'POST', url: 'http://localhost:4000/api/v1/upload', body: data },
    { method: 'POST', url: 'http://localhost:4000/api/v1/upload', body: data },
    { method: 'POST', url: 'http://localhost:4000/api/v1/upload', body: data },
    { method: 'POST', url: 'http://localhost:4000/api/v1/upload', body: data },
    { method: 'POST', url: 'http://localhost:4000/api/v1/upload', body: data },
    { method: 'POST', url: 'http://localhost:4000/api/v1/upload', body: data },
    { method: 'POST', url: 'http://localhost:4000/api/v1/upload', body: data },
    { method: 'POST', url: 'http://localhost:4000/api/v1/upload', body: data },
  ]);

  check(res[0], {
    'status is 200': (r) => r.status === 200,
    'response body': (r) => r.body.indexOf('success') !== -1,
  });

  sleep(1);
}
