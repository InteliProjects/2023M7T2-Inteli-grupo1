const AWS = require('aws-sdk');
const s3 = new AWS.S3();

async function uploadToS3(file, bucketName, folderName, fileName) {
  const params = {
    Bucket: bucketName,
    Key: `${folderName}/${fileName}`,
    Body: file.buffer, // Use file.buffer para obter o conteúdo do arquivo
  };

  try {
    const result = await s3.upload(params).promise();
    return result.Location; // Retorna o URL do arquivo no S3
  } catch (error) {
    throw error;
  }
}

module.exports = { uploadToS3 };
