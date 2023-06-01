import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
import boto3
from PIL import Image

def process_image(event, context):
    #Recupere o nome do arquivo de imagem do evento
    image_name = event['image_name']
    
    #Baixe a imagem S3
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('seu-bucket')
    obj = bucket.Object(image_name)
    image_data = obj.get()['Body'].read()
    
    #Abra a imagem usando a biblioteca Pillow
    image_data = Image.open(image_data)
    
    #Realize o processamento da imagem
    #(por exemplo, redimensionamento, aplicação de filtro, detecção de objeto, etc.)
    
    #Salve a imagem processada em um novo arquivo
    processed_image_path = '/tmp/processed_image_jpg'
    image.save(processed_image_path)
    
    #Faça upload da imagem processada para o S3
    bucket.upload_file(processed_image_path, 'caminho/para/processed_image_jpg')
    
    #Retorne a URL da imagem processada
    processed_image_url = f'https://seu-bucket.s3.amazonaws.com/caminho/para/processed_image_jpg'
    return {
        'processed_image_url': processed_image_url
        }
    
    #Documentação da função Lambda de Processamento de Imagem
    
    Esta função Lambda é responsavel por processar uma imagem, realizar operações especificar e fazer upload da imagem processada para o Amazon S3.
    
    ##Função
    
    A função Lambda 'process_image' recebe um evento contendo o nome do arquivo de imagem a ser processado. A função realiza as seguintes tarefas:
        1. Baixa a imagem do Amazon S3.
        2. Abre a imagem utilizando a biblioteca Pillow.
        3. Realiza o processamento de imagem desejado (por exemplo , redimensionamento, aplicação de filtro, detecção de objeto).
        4. Salva a imagem processada em um novo arquivo.
        5. Faz upload da imagem processada novamente para o Amazon S3.
        6. Retorna a URL da imagem processada.
        
    ##Entrada e Saída
    
    
    A função Lambda é acionada por um evento que contém o seguinte formato:
        '''json
        {
            "image_name": "nome_da_imagem.jpg"
        }
        {
            "processed_image_url": "https://seu-bucket.s3.amazonaws.com/caminho/para/processed_image_url"
        }
        
        '''
    ##Dependências Externas

    A função Lambda depende das seguintes bibliotecas Python:
    1. Pillow: biblioteca para manipulação de imagens.
    2. Boto3: SDK da AWS para Python, usado para interagir com o Amazon S3.
    
    ##Certifique-se de que essas dependências estejam instaladas no ambiente de execução da Lambda.
    
    ##Instruções de Execução
    1. Faça o upload do código da função Lambda para o AWS Lambda Console ou utilize o AWS CLI para criar a função Lambda com o código fornecido.
    2. Configure as permissões adequadas para a função Lambda, permitindo o acesso ao Amazon S3.
    3. Ajuste as configurações avançadas, como recursos de memória e limite de tempo de execução, de acordo com as necessidades do seu processamento de imagem.
    4. Salve a função Lambda.
    
    ##Teste e Depuração
    1. No AWS Lambda Console, crie um evento de teste com o seguinte formato:
        {
            "image_name": "nome_da_imagem.jpg"
        }
    2. Execute o teste para verificar se a função é acionada corretamente e se a imagem processada é enviada para o Amazon S3 com sucesso.
    3. Verifique os logs de execução no console do AWS Lambda para depurar eventuais erros ou problemas.