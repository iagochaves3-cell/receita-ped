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


## Incremento de integração — 23/09/2026 — NÃO PUBLICADO

Branch local `feat/nexo-evidence-integration`. Publicação e PR bloqueados pelo
conector GitHub: HTTP 403 `Resource not accessible by integration`.

Foram acrescentadas duas rotas POST autenticadas: `/v1/evidence/search` e
`/v1/clinical/review`, como proxy de servidor para o NEXO, domínio `prescription`.
O cliente canônico está em `nexo-clinical/integrations/nexo_client.py`. A pesquisa
e revisão ficam centralizadas no NEXO, sem duplicar o motor clínico. O servidor
continua sem gerar prescrição ou parâmetros terapêuticos. O serviço documental
e suas rotas anteriores foram preservados. As instruções originais não são
injetadas automaticamente no modelo; esta etapa não conclui migração funcional clínica.

Configure somente pelo cofre/Variables do Railway: `SERVICE_API_TOKEN` próprio,
`NEXO_API_URL=https://nexo-clinical-api-production.up.railway.app` e
`NEXO_INTEGRATION_TOKEN` compartilhado com o novo endpoint restrito do NEXO.
Não configure antes da publicação do incremento NEXO. Não enviar chaves pelo
chat, frontend, URL ou arquivos versionados. Valores vazios em `.env.example`.

O diretório raiz do serviço Railway deve ser `/Receita_PED_Repositorio_Railway` nesta estrutura
atual do repositório. Não mover/recriar o pacote para fazê-lo parecer na raiz.

Testes: `python -m unittest -v test_server.py test_nexo_adapter.py`.
16 testes passaram, incluindo verificação de integridade dos arquivos originais.
Teste autenticado em produção e domínio HTTPS ainda não confirmados.
`nexo_configured` indica somente presença de configuração, não teste remoto.
Falha do NEXO produz 503; rascunho nunca é aprovação clínica. Sem nome,
prontuário ou data de nascimento no payload. Usar apenas conteúdo desidentificado.

Arquivos originais ausentes foram restaurados apenas quando o hash coincidiu
com `original-sha256.json`; conteúdo existente preservado.
