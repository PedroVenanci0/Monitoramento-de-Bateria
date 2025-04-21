# Monitor de Bateria com Notificação

Este projeto contém um script em Python que monitora o nível de carga da bateria do seu computador e envia notificações automaticamente quando a bateria atinge certos limites críticos. O objetivo é alertar o usuário para a necessidade de conectar ou desconectar o carregador com base nos níveis de carga da bateria.

## Objetivo

O script foi desenvolvido para ser executado em segundo plano, sem a necessidade de interação constante do usuário. Ele fornece notificações de forma prática e eficiente para que o usuário saiba quando a bateria está cheia ou precisa ser carregada, ajudando a manter a saúde da bateria do dispositivo.

## Funcionalidades

- **Notificação de Bateria Cheia**: Envia um alerta quando a bateria atinge 80% ou mais enquanto está carregando.
- **Notificação de Bateria Baixa**: Envia um alerta quando a bateria atinge 20% ou menos e não está carregando.
- **Execução Automática**: O script é configurado para ser executado automaticamente ao iniciar o computador, sem a necessidade de abrir o terminal.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para escrever o script.
- **psutil**: Biblioteca para acessar informações do sistema, como o status da bateria.
- **plyer**: Biblioteca para enviar notificações nativas no sistema operacional.

## Como Funciona

O script verifica periodicamente o status da bateria (a cada 60 segundos). Quando a bateria atinge o limite de 80% enquanto está carregando ou 20% enquanto está descarregando, ele envia uma notificação para alertar o usuário. O script continuará funcionando em segundo plano até que o computador seja desligado ou reiniciado.

## Instalação e Uso

1. **Instalar as dependências**: 
   Execute o comando `pip install psutil plyer` para instalar as bibliotecas necessárias.
   
2. **Salvar o Script**:
   Salve o código Python fornecido como `monitor_bateria.pyw` (a extensão `.pyw` é usada para impedir que o terminal seja aberto durante a execução).

3. **Configurar Execução Automática**:
   Coloque um atalho do script na pasta de inicialização do Windows, para que ele seja executado automaticamente ao iniciar o sistema.

Esse repositório foi desenvolvido para ajudar usuários a manter o controle sobre a saúde de suas baterias, garantindo que o carregador seja desconectado quando a carga atingir um nível seguro e que a bateria seja carregada a tempo de evitar falhas.
