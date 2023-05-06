const request = require('supertest');
const app = require('../../front-api/index.js');
const { expect } = require('@jest/globals');
const FormData = require('form-data');
const fs = require('fs');

test('should upload a file and return a filename', async () => {
  const form = new FormData();
  const fileStream = fs.createReadStream('tests/frontend/test-image.jpg');
  form.append('file', fileStream);

  const response = await request('http://localhost:4000')
    .post('/api/v1/upload')
    .set('Content-Type', 'multipart/form-data')
    .send(form);
  
  expect(response.status).toBe(200);
  expect(response.body).toHaveProperty('filename');
});