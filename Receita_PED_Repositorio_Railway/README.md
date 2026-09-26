# Receita PED — serviço documental

## Estado do código

O servidor publica instruções originais autenticadas. A integração NEXO de pesquisa bibliográfica e rascunho de revisão foi mesclada em main em 23/09/2026.
Não há motor clínico, geração de receitas, cálculo de soro ou ajuste ventilatório.
Os documentos não são carregados automaticamente como regras de um modelo.
Código mesclado e /health não comprovam implantação, integração funcional nem validação clínica.

Os 18 arquivos originais estão em `plugin-original/`, com hashes em
`original-sha256.json`. 
O manifesto original foi preservado. Os testes de integridade conferem todos os arquivos.

## Diretório canônico e execução local

A partir da raiz deste repositório:

```bash
cd 'Receita_PED_Repositorio_Railway'
python -m unittest -v test_server.py test_nexo_adapter.py
# Configure SERVICE_API_TOKEN no ambiente antes de iniciar:
python server.py
```

O servidor usa somente a biblioteca padrão do Python (Python 3.12 no Dockerfile).
`SERVICE_API_TOKEN` deve ser um segredo URL-safe aleatório de 32–256 caracteres.
Não preencher arquivos versionados com credenciais.

## Configuração de deploy

- Root Directory: `/Receita_PED_Repositorio_Railway`.
- Railway Config File: `/Receita_PED_Repositorio_Railway/railway.json`, caminho absoluto no repositório.
- Dockerfile dentro da pasta canônica; comando `python server.py`.
- Porta `PORT` fornecida pela plataforma, padrão local 8080.
- Healthcheck `/health`, timeout de 100 segundos, reinício ON_FAILURE até 3 vezes.
- O caminho do arquivo Railway Config File é configurado separadamente do Root Directory.

O código não confirma o domínio, variáveis ou SHA implantado. Não há comando de
deploy automático nestes testes. O servidor http.server é uma implementação
documental com limitações para produção; ver a documentação oficial do Python.

## Rotas

| Método | Caminho | Autenticação | Resultado |
|---|---|---|---|
| GET | / | Pública | Identificação documental |
| GET | /health | Pública | Saúde técnica, clinical_engine=false |
| GET | /v1/capabilities | Bearer | Capacidades reais |
| GET | /v1/instructions | Bearer | Instruções originais |
| POST | /v1/evidence/search | Bearer | Proxy de pesquisa NEXO |
| POST | /v1/clinical/review | Bearer | Proxy de rascunho NEXO |
| POST | outros caminhos | Bearer | 501: motor clínico não implementado |

## Integração NEXO

Configure no ambiente do servidor:
- `NEXO_API_URL=https://nexo-clinical-api-production.up.railway.app`;
- `NEXO_INTEGRATION_TOKEN`, independente do token de acesso deste serviço.

O domínio enviado ao NEXO é `prescription`. O cliente canônico está em
`nexo-clinical/integrations/nexo_client.py`; regras clínicas permanecem centralizadas.
`nexo_configured` informa presença/formato da configuração, sem testar o upstream.
A indisponibilidade ou resposta truncada do upstream retorna erro sanitizado 503.
Rascunho nunca é aprovação clínica. Aceitar somente conteúdo desidentificado,
sem nome, prontuário ou data de nascimento.

`verify_production.py` é opt-in e depende de `RAILWAY_PUBLIC_DOMAIN` e credenciais
já presentes no ambiente confiável. Não é executado pela suíte local e pode chamar
provedores externos; use-o somente na etapa de verificação de produção autorizada.

## Evidência e limites

Os testes locais usam sockets loopback, tokens sintéticos e mocks de provedores.
Verificam autenticação, contratos, integridade e tratamento de falhas; não validam
condutas, doses ou fontes médicas. Não existem dados reais de pacientes nos testes.

Referências técnicas:
- [Railway — configuração de build](https://docs.railway.com/builds/build-configuration)
- [Python — http.server](https://docs.python.org/3.12/library/http.server.html)
