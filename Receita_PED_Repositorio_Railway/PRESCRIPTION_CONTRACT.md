# Contrato reservado — receita-prescription/1

Inspeção do código em 06/10/2026: RECEITA 8a465464cdcb74e1b287f58294f749564e438440; receita-ped 5d3e360ab6fafdbb8c3924f42beadbde290534a5; NEXO 85be261acf9f0682cc9a31c099cbb7a9a740f00e, diretório canônico indicado em seu README.

NEXO expõe pesquisa bibliográfica e revisão em rascunho, roteamento, regras técnicas de segurança, metadados ECG/imagem e cálculos derivados laboratório/QTc. Nenhuma dessas operações aprova regimes. POST /v1/pediatric/prescription existe no código canônico, mas declara clinical_validated=false, prescribing_authorization=false e requires_human_review=true. O token de integração só acessa capabilities, evidence/search e clinical/review. Não há saída prescritiva autorizada verificada. Não houve consulta autenticada de produção nem confirmação do SHA implantado.

## Contrato implementado

GET /v1/capabilities autenticado adiciona prescription_integration:
```json
{"contract_version":"receita-prescription/1","endpoint":"/v1/pediatric/prescription","available":false,"validated_regimes":[],"reason_code":"validated_prescription_dependency_unavailable"}
```
POST /v1/pediatric/prescription e alias /v1/prescribe autenticados retornam HTTP 501, no-store:
```json
{"contract_version":"receita-prescription/1","status":"unavailable","error":"validated_prescription_dependency_unavailable","message":"Nenhum regime prescritivo validado disponível nesta integração.","clinical_validated":false,"prescribing_authorization":false,"requires_human_review":true,"prescription":null,"regime_id":null,"audit":null}
```
Enquanto indisponível, o corpo não é interpretado nem encaminhado ao NEXO. Nenhuma configuração habilita prescrição. Outras rotas preservam os contratos. Frontend bloqueado inclusive sem JavaScript; não consulta capacidades, não armazena pacientes, não recebe tokens e não promove drafts. Submit e ações copiar/imprimir são interceptados; resultados residuais apagados; impressão nativa oculta formulário/resultados.

## Contrato futuro proposto — não implementado nem validado

BFF autenticado no mesmo origin; tokens somente no servidor. Não conectar GitHub Pages diretamente ao serviço Bearer. Auth, timeout, redirect, 429, 5xx, JSON inválido/truncado ou contrato incompatível limpam resultado e desabilitam exports. Sem retry automático do POST.

Entrada estrita desidentificada: contract_version, request_id, regime_id/version da allowlist, diagnosis_id canônico, weight_kg positivo/finito, age={years,months,days} com inteiros não negativos/calendário validado, visit_date ISO, allergies/comorbidities/current_medications como listas explícitas, renal_function/hepatic_function explícitas. Ausente não equivale a vazio/normal. Gravidade, indicação e apresentação precisam de campos específicos do regime selecionado. Rejeitar desconhecidos e dados identificáveis. Elegibilidade e cálculos exclusivamente centrais.

Sucesso: vincular request_id/hash da entrada ao regime/version e SHA implantado. prescription estruturada: indication, presentation, concentration, dose={value,unit}, volume_ml, route, interval, duration, per_dose_max, daily_max, warnings; infusion/preparation quando aplicáveis. Texto copiável derivado dos mesmos campos. Exigir clinical_validated=true, prescribing_authorization=true e audit verificável contra artefato confiável no servidor, nunca apenas flags upstream.

Audit: regime_id/version, content_sha256, deployment_sha, fontes primárias/URLs/data de revisão, aprovações clínica/farmacêutica identificáveis, checagem matemática independente/reversa, elegibilidade, evidência/regulação BR, contraindicações/interações/ajustes, limites e testes. Todos os gates PASS com evidência/responsável real. Não inventar aprovação humana. Allowlist inicial vazia. Pesquisa/review nunca são fallback prescritivo.

Ativar exatamente um regime só após auditoria do artefato e contrato/SHA em produção. Regressões necessárias: elegibilidade, idade/peso extremos, máximos, unidades, cálculo reverso, apresentações, alergias/ajustes, dados ausentes, regime desconhecido, conexão perdida, resposta fora de ordem, entrada alterada, versão divergente/expiração. Copiar/imprimir apenas resultado atual permitido; textContent e impressão isolada sem HTML upstream. Restante default-deny.

## Testes locais

RECEITA: node --test tests/prescription-integration.test.cjs.
Receita PED: python -m unittest -v test_server.py test_nexo_adapter.py test_prescription_contract.py.
Entradas sintéticas/mocks testam software; não validam condutas ou produção.
