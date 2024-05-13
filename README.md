# Monitoramento de Temperatura e Fluxostato

Este é um projeto de medidor de dados IoT que lê a temperatura de dois sensores DS18B20 e o estado de um fluxostato, e publica esses dados em um servidor MQTT. O projeto é escrito em MicroPython e foi projetado para ser executado em um microcontrolador compatível, como o ESP32.

## Funcionalidades

- **Conexão Wi-Fi**: O dispositivo se conecta a uma rede Wi-Fi para comunicação com o servidor MQTT.
- **Leitura de Temperatura**: Utilizando sensores DS18B20, o dispositivo mede a temperatura em dois pontos distintos.
- **Leitura do Estado do Fluxostato**: O estado do fluxostato, indicando a presença de fluxo de água, é lido.
- **Publicação via MQTT**: Os dados de temperatura e o estado do fluxostato são publicados em um servidor MQTT para monitoramento remoto.

## Pré-requisitos

- Microcontrolador ESP32 ou similar compatível com MicroPython.
- Sensores DS18B20 para medição de temperatura.
- Fluxostato para detecção de fluxo de água.
- Acesso à rede Wi-Fi.
- Configurações do servidor MQTT, incluindo endereço, porta, usuário e senha.

## Instalação e Configuração

1. Conecte os sensores DS18B20 e o fluxostato ao microcontrolador de acordo com as especificações do hardware.
2. Configure as variáveis de configuração no arquivo `config.py`, incluindo SSID e senha da rede Wi-Fi, detalhes do servidor MQTT e pinos de conexão dos sensores.
3. Carregue o código Python para o microcontrolador.
4. Certifique-se de que o servidor MQTT está configurado e acessível na rede.

## Uso

Ao ligar o dispositivo, ele se conectará à rede Wi-Fi especificada e começará a publicar os dados de temperatura e estado do fluxostato no servidor MQTT. Esses dados podem ser monitorados e utilizados para automação ou visualização em aplicativos IoT.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar este projeto.
