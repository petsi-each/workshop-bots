# Programa do Workshop: Criando um Bot Básico para o Telegram com python-telegram-bot 21.3

## Visão Geral do Workshop
Este workshop foi criado para guiar os participantes no processo de criação de um bot básico para o Telegram usando a biblioteca `python-telegram-bot`, versão 21.3. Ao final do workshop, os participantes terão um bot funcional para o Telegram capaz de responder a comandos e mensagens.

## Público-Alvo
- Desenvolvedores Python iniciantes a intermediários
- Indivíduos interessados em construir bots para o Telegram
- Não é necessário ter experiência prévia com o desenvolvimento de bots para o Telegram

## Duração
- Total: 2 horas
- Dividido em três sessões

## Sessão 1: Introdução e Configuração

**Duração: 1 hora**

**Objetivos:**
- Entender os conceitos básicos dos bots do Telegram
- Configurar o ambiente de desenvolvimento

**Agenda:**
1. **Introdução aos Bots do Telegram (15 minutos)**
   - O que são bots do Telegram?
   - Casos de uso e exemplos
   - Visão geral da biblioteca `python-telegram-bot`

2. **Criando um Bot no Telegram (15 minutos)**
   - Interagindo com o BotFather
   - Criando um novo bot
   - Obtendo o token do bot

3. **Configurando o Ambiente de Desenvolvimento (30 minutos)**
   - Instalando Python e pip
   - Configurando um ambiente virtual
   - Instalando `python-telegram-bot` versão 21.3
     ```bash
     pip install python-telegram-bot==21.3
     ```

## Sessão 2: Desenvolvimento Básico do Bot

**Duração: 1 hora**

**Objetivos:**
- Criar um bot básico para o Telegram
- Implementar manipuladores de comandos simples

**Agenda:**
1. **Escrevendo o Script do Bot (20 minutos)**
   - Configurando a estrutura do projeto
   - Escrevendo o script básico do bot
   - Explicação da função principal e dos manipuladores

   ```python
   from telegram import Update
   from telegram.ext import Application, CommandHandler

   BOT_TOKEN = 'SEU_TOKEN_DO_BOT'

   async def start(update: Update, context):
       await update.message.reply_text('Olá!')

   async def help_command(update: Update, context):
       await update.message.reply_text('Ajuda!')

   def main():
       application = Application.builder().token(BOT_TOKEN).build()
       application.add_handler(CommandHandler("start", start))
       application.add_handler(CommandHandler("help", help_command))
       application.run_polling()

   if __name__ == '__main__':
       main()
    ```

2. **Executando o Bot (20 minutos)**
    - Executando o script
    - Testando o bot com os comandos /start e /help

3. **Perguntas e Respostas e Solução de Problemas (20 minutos)**
    - Problemas comuns e soluções
    - Solução interativa de problemas

## Sessão 3: Aprimorando a Funcionalidade do Bot

**Duração: 1 hora**

**Objetivos:**
- Adicionar manipuladores de mensagens ao bot
- Implementar recursos mais interativos

**Agenda:**
1. **Adicionando Manipuladores de Mensagens (20 minutos)**
   - Introdução aos manipuladores de mensagens
   - Escrevendo um manipulador de eco para responder a mensagens de texto

   ```python
   from telegram.ext import MessageHandler, filters

   async def echo(update: Update, context):
       await update.message.reply_text(update.message.text)

   # Em main()
   application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    ```

2. **Implementando Comandos Adicionais (20 minutos)**
    - Adicionando mais comandos como /sobre, /contato, etc.
    - Melhores práticas para nomeação e manipulação de comandos

3. **Recursos Interativos (20 minutos)**
    - Adicionando botões e menus
    - Utilizando teclados inline