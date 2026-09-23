# Receita PED — pacote para repositório e Railway

## O que está incluído

Arquivos originais do plugin `gpt-e99bb653b839b267957d2919ff50fadd`, versão `0.31.1+bundle.d311ca7717a78f9e6936609e886457ea`, copiados sem alteração para `plugin-original/`. O arquivo `original-sha256.json` permite conferir a integridade de todos os 18 arquivos originais.

O servidor adicional usa somente a biblioteca padrão do Python. Ele disponibiliza saúde do serviço e leitura autenticada das instruções originais. **Não há motor clínico, cálculo de doses, geração de receitas, ajuste ventilatório, pesquisa médica em tempo real nem processamento de pacientes.** As instruções e documentos arquivados não foram submetidos a validação clínica nesta entrega. Não envie dados de pacientes.

## Como anexar ao seu repositório

1. Extraia este ZIP no computador.
2. Envie o CONTEÚDO extraído para a raiz do repositório correspondente. `Dockerfile`, `server.py` e `railway.json` devem ficar diretamente na raiz, junto da pasta `plugin-original`.
3. Não envie apenas o ZIP: o Railway precisa dos arquivos extraídos. Prefira Git para preservar arquivos ocultos, incluindo o manifesto original em `plugin-original/.codex-plugin/plugin.json`.
4. Faça commit dos arquivos. Nenhuma senha ou token está incluído neste pacote.

## Configurar no Railway

1. Conecte este repositório ao serviço do Railway.
2. Em Variables, defina `SERVICE_API_TOKEN` com um segredo aleatório de pelo menos 32 caracteres. Gere localmente com `python -c "import secrets; print(secrets.token_urlsafe(48))"`. Não coloque o segredo em arquivos ou commits.
3. O serviço utiliza `PORT` fornecida pelo Railway; localmente usa 8080. O Dockerfile inicia `python server.py`.
4. Implante e confira os logs. Gere o domínio público nas configurações de rede do serviço. O HTTPS será terminado pela plataforma; o processo interno atende HTTP.
5. Abra `/health` no domínio gerado e confirme resposta 200. Isso comprova somente a disponibilidade técnica do serviço documental.

## Rotas

| Método | Caminho | Autenticação | Resultado |
|---|---|---|---|
| GET | / | Pública | Identificação e limitações |
| GET | /health | Pública | Saúde técnica |
| GET | /v1/capabilities | Bearer token | Capacidades documentais |
| GET | /v1/instructions | Bearer token | Texto original da skill |
| POST | qualquer caminho | Bearer token | 501: motor clínico não implementado |

Rotas protegidas exigem cabeçalho `Authorization: Bearer SEU_TOKEN`. Os documentos de referência permanecem no pacote; o servidor não os publica como arquivos estáticos. Não há integração automática com GPTs, (M) ou outros sites.

## Verificação local

Execute `python -m unittest -v test_server.py` com Python 3.12 ou compatível. Os testes verificam autenticação, leitura de instruções, saúde, bloqueio de leitura arbitrária e resposta explícita de função clínica não implementada. Foram executados localmente na preparação; build Docker, domínio HTTPS e implantação Railway ainda precisam ser verificados no destino.

## Pendências para aplicação clínica

Implementar e validar o motor clínico e suas fontes, revisar instruções e referências com responsável clínico, implementar proteção de dados apropriada e integrar a API ao consumidor. A publicação deste serviço documental não conclui essas etapas nem confirma migração funcional clínica. Não foi criada uma URL HTTPS nesta entrega.
