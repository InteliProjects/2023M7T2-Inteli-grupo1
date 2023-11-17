import { Card, Form, Input, DatePicker, Button, Upload, message } from 'antd';
import { UploadOutlined } from '@ant-design/icons';
import AWS from 'aws-sdk';

AWS.config.update({
  accessKeyId: 'AKIAU5TL4RBKDREQT5U5',
  secretAccessKey: '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',
  region: 'us-east-1', // Substitua pela região desejada
});

const s3 = new AWS.S3();

function FlightDataForm() {
  const onFinish = async (values) => {
    try {
      const { entryDate, aircraft, flightData } = values;

      // Verifique se um arquivo foi selecionado
      if (!flightData || flightData.length === 0) {
        message.error('Por favor, selecione um arquivo para fazer o upload.');
        return;
      }

      const file = flightData[0].originFileObj; // Obtenha o arquivo do objeto fileList
      const fileName = flightData[0].name;

      const params = {
        Bucket: 'blueskai-g1',
        Key: `files/${fileName}`,
        Body: file,
      };

      // Faça o upload diretamente para o Amazon S3
      const result = await s3.upload(params).promise();

      // Os dados do formulário, incluindo o URL do arquivo no S3, podem ser usados conforme necessário
      console.log('Valores do formulário:', { entryDate, aircraft, fileUrl: result.Location });
      message.success('Dados de voo enviados com sucesso!');
    } catch (error) {
      console.error('Falha no envio do formulário:', error);
      message.error('Falha no envio do formulário.');
    }
  };

  const onFinishFailed = (errorInfo) => {
    console.log('Falha no envio do formulário:', errorInfo);
  };

  // Configurações de upload
  const uploadProps = {
    name: 'file',
    accept: '.parquet', // Defina os tipos de arquivo permitidos
    customRequest: async ({ file, onSuccess, onError }) => {
      try {
        const fileName = file.name;

        const params = {
          Bucket: 'blueskai-g1',
          Key: `files/${fileName}`,
          Body: file,
        };

        // Faça o upload diretamente para o Amazon S3
        const result = await s3.upload(params).promise();

        // Chame onSuccess para indicar que o upload foi bem-sucedido
        onSuccess(result);

        message.success(`${fileName} arquivo enviado com sucesso.`);
      } catch (error) {
        console.error('Falha no envio do arquivo:', error);
        message.error(`${file.name} falha ao enviar o arquivo.`);
        onError(error);
      }
    },
  };

  return (
    <Card style={{ width: "80%" }}>
      <h1 style={{ color: '#0F5FC2' }}>Dados de Voo</h1>
      <p>Por favor, realize o input dos dados:</p>
      <Form
        name="flightDataForm"
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
        labelCol={{ span: 24 }}
        wrapperCol={{ span: 24 }}
      >
        <Form.Item
          label="Data de Entrada dos Dados"
          name="entryDate"
          labelAlign="top"
        >
          <DatePicker style={{ width: '100%', backgroundColor: '#F2EFFF' }} />
        </Form.Item>
        <Form.Item
          label="Aeronave"
          name="aircraft"
          labelAlign="top"
        >
          <Input style={{ backgroundColor: '#F2EFFF' }} />
        </Form.Item>
        <Form.Item
          label="Upload de Dados de Voo"
          name="flightData"
          valuePropName="fileList"
          getValueFromEvent={(e) => e.fileList}
          labelAlign="top"
        >
          <Upload {...uploadProps}>
            <Button icon={<UploadOutlined />} style={{ backgroundColor: '#F2EFFF', color: '#0F5FC2' }}>
              Selecione o arquivo
            </Button>
          </Upload>
        </Form.Item>

        <Form.Item wrapperCol={{ span: 24 }} style={{ marginTop: '16px' }}>
          <Button type="primary" htmlType="submit" style={{ backgroundColor: '#0F5FC2' }}>
            Enviar Dados
          </Button>
        </Form.Item>
      </Form>
    </Card>
  );
}

export default FlightDataForm;
