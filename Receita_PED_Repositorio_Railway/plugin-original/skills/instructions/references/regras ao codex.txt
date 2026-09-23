Implemente essa configuração de forma estrutural, global e definitiva, evitando correções pontuais, patches locais ou soluções específicas apenas para o exemplo relatado.

REQUISITOS DE EXECUÇÃO

1. ENTENDER O REQUISITO ANTES DE ALTERAR

* Identifique exatamente qual comportamento atual precisa mudar.
* Determine todos os componentes, arquivos, funções, estados, APIs, validações, cálculos, interfaces e dependências afetados.
* Trate os exemplos fornecidos apenas como casos de teste; a solução deve funcionar para toda a classe de situações equivalentes.

2. DEFINIR UMA ÚNICA FONTE DE VERDADE

* Sempre que o requisito envolver dados compartilhados, centralize a lógica em uma única fonte de verdade.
* Elimine parsers, cálculos, validações, estados ou regras duplicadas quando puderem produzir comportamentos divergentes.
* Todos os componentes dependentes devem consumir a mesma lógica centralizada.

3. FAZER BUSCA GLOBAL NO PROJETO

* Pesquise o projeto inteiro por todas as implementações relacionadas ao comportamento alterado.
* Procure nomes alternativos, funções equivalentes, regex, condicionais, validadores, parsers, estados locais, valores hardcoded e implementações legadas.
* Não presuma que o erro esteja apenas no arquivo ou componente onde ele apareceu.

4. FAZER ANÁLISE DE IMPACTO
   Antes de concluir, determine tudo que pode ser afetado direta ou indiretamente pela mudança:

* interface;
* estado;
* cálculos;
* validações;
* banco ou persistência;
* APIs;
* geração de resultados;
* exportações;
* responsividade;
* acessibilidade;
* segurança;
* desempenho;
* funcionalidades relacionadas.

5. PRESERVAR FUNCIONALIDADES EXISTENTES

* Não remover, alterar ou degradar comportamentos que não façam parte desta solicitação.
* Verifique explicitamente backward compatibility.
* Compare o comportamento antes e depois da alteração nas áreas não relacionadas.

6. COBRIR CASOS NORMAIS, LIMITES E INVÁLIDOS
   Crie testes para:

* valores típicos;
* valores mínimos;
* valores máximos;
* limites imediatamente abaixo e acima;
* valores vazios;
* valores inválidos;
* formatos alternativos válidos;
* entradas inesperadas;
* mudanças sucessivas de estado;
* seleção e desseleção;
* recarregamento;
* execução repetida;
* combinações entre diferentes parâmetros.

7. TESTAR O FLUXO COMPLETO
   Não teste apenas funções isoladas.

Teste obrigatoriamente o caminho completo:
entrada → normalização → estado → regra → cálculo/processamento → interface → resultado final.

Confirme que a informação não é perdida, reinterpretada ou alterada em nenhuma etapa.

8. CRIAR TESTES DE REGRESSÃO

* Todo erro encontrado deve gerar pelo menos um teste que falharia antes da correção e passe depois dela.
* Inclua testes para impedir que o mesmo problema reapareça futuramente.
* Acrescente também testes para problemas da mesma classe, mesmo que ainda não tenham sido relatados.

9. FAZER TESTES NEGATIVOS
   Tente deliberadamente quebrar a implementação:

* entradas inesperadas;
* estados inconsistentes;
* cliques rápidos;
* alterações consecutivas;
* valores extremos;
* campos ausentes;
* dados parcialmente preenchidos;
* combinações incomuns;
* chamadas repetidas;
* condições concorrentes, quando aplicável.

10. VERIFICAR ESTADO E REATIVIDADE
    Quando um dado for alterado:

* todos os componentes dependentes devem ser atualizados;
* nenhum componente pode permanecer utilizando valor antigo;
* não deve existir stale state;
* não deve haver duplicidade de estado representando a mesma informação.

11. PROIBIR FALHAS SILENCIOSAS

* Não mascarar exceções.
* Não utilizar catch genérico apenas para esconder erro.
* Não substituir erro de lógica por fallback que produza resultado aparentemente válido.
* Identifique e corrija a causa raiz.

12. VALIDAR TIPOS E CONTRATOS
    Execute, quando aplicável:

* type-check;
* linter;
* validação de schema;
* testes unitários;
* testes de integração;
* testes end-to-end;
* build de produção.

Todos devem terminar sem erros.

13. REVISAR O DIFF COMPLETO
    Após implementar:

* releia todas as alterações realizadas;
* procure código morto;
* duplicações;
* condicionais redundantes;
* inconsistências de nomes;
* problemas de tipos;
* valores hardcoded desnecessários;
* alterações acidentais;
* riscos de regressão.

Faça uma segunda revisão do diff como se estivesse revisando o código produzido por outro desenvolvedor.

14. EXECUTAR UMA REVISÃO INDEPENDENTE
    Depois que considerar a tarefa concluída, descarte mentalmente a hipótese inicial do problema e investigue novamente o comportamento a partir dos requisitos originais.

Pergunte:
“Existe alguma situação válida em que esta configuração ainda não funcionaria?”

Se encontrar alguma, corrija antes de concluir.

15. VALIDAR OS CRITÉRIOS DE ACEITE UM A UM
    Transforme cada requisito desta solicitação em um critério verificável.

Ao final, confira individualmente:
REQUISITO 1 → aprovado/reprovado
REQUISITO 2 → aprovado/reprovado
REQUISITO 3 → aprovado/reprovado
...

Nenhum requisito pode ser considerado atendido por inferência.

16. NÃO CONSIDERAR “TESTE PASSOU” COMO SINÔNIMO DE “REQUISITO ATENDIDO”
    Além dos testes automatizados, confirme semanticamente que o comportamento implementado corresponde exatamente ao solicitado.

17. VERIFICAR A INTERFACE FINAL
    Quando houver interface:

* testar desktop e mobile;
* diferentes larguras de tela;
* textos longos;
* campos vazios e preenchidos;
* seleção/desseleção;
* contraste e legibilidade;
* overflow;
* alinhamento;
* estados disabled/enabled;
* loading;
* erro;
* resultado.

18. EXECUTAR BUILD LIMPO
    Quando possível:

* remover artefatos de build anteriores;
* executar instalação/compilação limpa;
* executar novamente todos os testes relevantes;
* confirmar que o funcionamento não depende de cache ou estado residual.

19. VALIDAR APÓS A IMPLEMENTAÇÃO
    Após todas as alterações, repita do zero os cenários que originalmente apresentavam erro e também cenários diferentes da mesma classe.

20. CORRIGIR QUALQUER NOVO ERRO ENCONTRADO
    Caso os testes revelem outro problema relacionado ou uma regressão introduzida pela alteração:

* investigue;
* corrija;
* adicione teste correspondente;
* execute novamente toda a bateria relevante.

Repita o ciclo até que os testes estejam estáveis.

21. NÃO FAZER CORREÇÃO SUPERFICIAL
    Evite:

* exceção específica para determinado valor;
* if criado apenas para o exemplo relatado;
* duplicação da regra;
* hardcode;
* workaround que não elimine a causa raiz.

Prefira uma solução arquitetural que cubra a regra geral.

22. CRITÉRIO DE CONCLUSÃO
    Somente considere a implementação concluída quando:

* todos os requisitos estiverem implementados;
* todos os critérios de aceite tiverem sido verificados;
* testes antigos continuarem passando;
* novos testes passarem;
* testes de regressão passarem;
* testes negativos relevantes passarem;
* linter passar;
* type-check passar;
* build passar;
* revisão independente não encontrar lacunas;
* não houver erro conhecido relacionado à alteração.

23. EVIDÊNCIAS
    Ao finalizar, informe objetivamente:

* causa raiz encontrada;
* arquivos/componentes alterados;
* solução estrutural adotada;
* testes novos adicionados;
* testes executados;
* quantidade de testes aprovados/reprovados;
* resultado de linter;
* resultado de type-check;
* resultado do build;
* casos-limite verificados;
* possíveis limitações que realmente permaneçam.

Não declare que algo foi testado se não tiver sido efetivamente executado.

24. PRINCÍPIO FINAL
    Não otimize para “fazer o exemplo funcionar”.
    Otimize para tornar impossível, dentro das regras definidas pelo sistema, que a mesma classe de erro volte a ocorrer em outro componente, entrada ou fluxo.
O exemplo que forneci demonstra o problema, mas NÃO delimita o escopo da correção. Procure sistematicamente todas as ocorrências da mesma classe de erro em todo o projeto e corrija a causa raiz global.

O objetivo não é obter sucesso nos testes que você próprio decidiu executar. O objetivo é tentar falsificar a implementação: procure ativamente cenários nos quais ela falharia e expanda os testes até cobrir essas hipóteses. Quero que trabalhe sistematicamente com milhares de testes internos e corrija cada erro encontrado. Continue com milhares de novos testes, em looping, até que 100% do programa/scrit/projeto/site esteja funcionando corretamente, sem nenhuma falha, mínima que seja.


25. DEFINIR INVARIANTES DO SISTEMA

Antes de testar casos específicos, identifique propriedades que devem ser verdadeiras em qualquer cenário válido.

Exemplos:

* o mesmo dado não pode produzir resultados diferentes em componentes distintos;
* alterar uma entrada deve atualizar todos os resultados dependentes;
* dados válidos nunca devem ser descartados silenciosamente;
* dados inválidos nunca devem produzir resultado aparentemente válido;
* nenhuma ação repetida deve gerar duplicação indevida;
* nenhuma navegação deve causar perda inesperada de estado.

Crie testes específicos para cada invariante identificado.

26. UTILIZAR TESTES BASEADOS EM PROPRIEDADES

Quando aplicável, não teste apenas exemplos manualmente escolhidos.

Use property-based testing para gerar automaticamente grande quantidade de combinações válidas e inválidas e verificar invariantes do sistema.

Inclua:

* valores aleatórios dentro da faixa válida;
* valores próximos aos limites;
* combinações inesperadas;
* diferentes ordens de interação;
* sequências repetidas de alterações.

A implementação deve se comportar corretamente para a classe inteira de entradas, e não somente para fixtures predeterminadas.

27. REALIZAR FUZZ TESTING

Submeta entradas e fluxos a dados inesperados e malformados para procurar falhas não previstas.

Testar, quando aplicável:

* strings muito longas;
* espaços;
* caracteres Unicode;
* caracteres especiais;
* separadores decimais diferentes;
* números extremamente grandes ou pequenos;
* null;
* undefined;
* NaN;
* Infinity;
* arrays vazios;
* objetos incompletos;
* dados duplicados;
* formatos antigos ainda aceitos pelo sistema.

Nenhum desses testes deve provocar corrupção de estado, erro não tratado ou resultado incorreto silencioso.

28. REALIZAR MUTATION TESTING QUANDO VIÁVEL

Quando houver infraestrutura compatível, execute mutation testing nos módulos críticos alterados.

Objetivo:
confirmar que os testes realmente detectariam uma implementação errada, e não apenas passam porque exercitam superficialmente o código.

Mutações sobreviventes em regras críticas devem ser analisadas e, quando necessário, gerar novos testes.

29. TESTAR CONCORRÊNCIA E RACE CONDITIONS

Quando houver operações assíncronas, efeitos, chamadas de API, persistência, uploads ou cálculos concorrentes, teste:

* respostas fora de ordem;
* duas ações executadas rapidamente;
* múltiplos cliques;
* alteração de estado enquanto uma operação está em andamento;
* requisições duplicadas;
* respostas lentas;
* cancelamentos;
* timeouts;
* reexecução após falha.

Uma resposta antiga nunca pode sobrescrever um estado mais recente.

30. GARANTIR IDEMPOTÊNCIA

A mesma operação executada mais de uma vez não deve causar:

* duplicação;
* corrupção;
* incremento indevido;
* alteração inesperada;
* criação múltipla do mesmo registro;
* resultados divergentes.

Testar explicitamente execução repetida dos fluxos críticos.

31. VALIDAR PERSISTÊNCIA E RECARREGAMENTO

Quando houver armazenamento local, banco, cache, sessão ou persistência:

* salvar;
* recarregar;
* fechar e abrir;
* navegar para outra tela e retornar;
* restaurar sessão;
* atualizar a página.

O estado restaurado deve continuar semanticamente equivalente ao estado original.

32. TESTAR MIGRAÇÃO E COMPATIBILIDADE COM DADOS ANTIGOS

Se houver dados persistidos ou formatos anteriores:

* testar dados criados por versões antigas;
* verificar migrações;
* garantir que novos campos não quebrem registros antigos;
* garantir valores default seguros;
* impedir perda de dados durante atualização.

33. VALIDAR CONTRATOS ENTRE CAMADAS

Verifique explicitamente contratos entre:

interface → estado;
estado → domínio;
domínio → API;
API → persistência;
persistência → leitura;
resultado → renderização.

Cada camada deve receber e devolver dados no formato esperado.

Não depender implicitamente de coerção automática de tipos.

34. VERIFICAR PRECISÃO NUMÉRICA

Quando houver cálculos:

* definir unidade canônica;
* testar arredondamentos;
* testar casas decimais;
* evitar erros de ponto flutuante quando clinicamente ou financeiramente relevantes;
* testar conversões entre unidades;
* testar limites inclusivos e exclusivos;
* verificar overflow e underflow quando aplicável.

A mesma regra matemática deve ser implementada uma única vez.

35. EXECUTAR ANÁLISE ESTÁTICA ADICIONAL

Quando houver ferramentas disponíveis, executar também:

* análise de dependências;
* código não utilizado;
* imports não utilizados;
* ciclos entre módulos;
* complexidade excessiva;
* duplicação de código;
* vulnerabilidades conhecidas;
* padrões inseguros;
* secrets acidentalmente versionados.

36. VERIFICAR DEPENDÊNCIAS

Analise se a alteração depende de bibliotecas externas.

Verifique:

* versão utilizada;
* breaking changes;
* APIs obsoletas;
* dependências duplicadas;
* peer dependencies;
* vulnerabilidades conhecidas;
* comportamento diferente entre versões.

Não atualizar dependências não relacionadas sem necessidade.

37. TESTAR DIFERENTES AMBIENTES

Quando aplicável, verificar:

* ambiente de desenvolvimento;
* ambiente de teste;
* build de produção.

Evitar solução que funcione somente em modo development.

Confirmar que variáveis de ambiente, caminhos, URLs, feature flags e configurações de produção permanecem corretos.

38. TESTAR COMPATIBILIDADE DE NAVEGADORES

Quando houver aplicação web, testar pelo menos motores representativos suportados pelo projeto:

* Chromium;
* Safari/WebKit;
* Firefox, quando suportado.

Verificar especialmente:

* inputs;
* clipboard;
* uploads;
* downloads;
* seleção;
* modais;
* scroll;
* CSS;
* eventos;
* APIs do navegador.

39. TESTAR RESPONSIVIDADE POR BREAKPOINT

Não testar apenas “desktop” e “mobile”.

Verifique diferentes larguras reais, incluindo:

* telas estreitas;
* smartphones;
* tablets;
* notebooks;
* monitores largos.

Procurar:

* overflow;
* elementos cortados;
* sobreposição;
* campos inacessíveis;
* botões fora da viewport;
* textos truncados.

40. VALIDAR ACESSIBILIDADE

Quando aplicável:

* navegação por teclado;
* foco visível;
* ordem de tabulação;
* labels;
* contraste;
* aria;
* leitores de tela;
* mensagens de erro associadas ao campo correto.

Nenhuma alteração visual deve tornar uma função inacessível.

41. VERIFICAR PERFORMANCE

Compare antes e depois da alteração.

Investigue regressões em:

* tempo de carregamento;
* renderizações desnecessárias;
* chamadas de API duplicadas;
* loops;
* cálculos repetidos;
* consumo de memória;
* tamanho do bundle;
* processamento de grandes volumes de dados.

Não aceitar uma correção funcional que introduza degradação grave de desempenho.

42. DETECTAR MEMORY LEAKS E EFEITOS RESIDUAIS

Quando aplicável, procurar:

* event listeners não removidos;
* timers;
* subscriptions;
* observers;
* requisições pendentes;
* objetos mantidos em memória sem necessidade.

Montar e desmontar repetidamente o componente não deve aumentar continuamente uso de recursos.

43. TESTAR RECUPERAÇÃO DE ERROS

Simule falhas reais:

* API indisponível;
* timeout;
* erro 4xx;
* erro 5xx;
* conexão interrompida;
* resposta incompleta;
* armazenamento indisponível;
* arquivo inválido.

O sistema deve:

* manter integridade do estado;
* informar adequadamente o erro;
* permitir recuperação;
* nunca apresentar dado fictício como resultado válido.

44. VALIDAR SEGURANÇA

Quando houver superfície relevante, revisar:

* validação de entrada;
* sanitização;
* XSS;
* injection;
* manipulação de parâmetros;
* exposição de dados;
* autorização;
* autenticação;
* CSRF;
* uploads;
* acesso indevido a recursos;
* logs contendo dados sensíveis;
* secrets.

Não enfraquecer controles de segurança para resolver problema funcional.

45. VERIFICAR DUPLICIDADE SEMÂNTICA

Não procurar apenas código textualmente duplicado.

Procure duas ou mais funções diferentes que implementem semanticamente a mesma regra.

Se duas partes do sistema responderem à mesma pergunta de negócio, verificar se deveriam consumir a mesma implementação centralizada.

46. VERIFICAR CÓDIGO LEGADO E ROTAS ALTERNATIVAS

Identifique caminhos antigos que ainda possam ser utilizados:

* componentes legados;
* funções não removidas;
* páginas antigas;
* APIs antigas;
* aliases;
* rotas secundárias;
* feature flags;
* código condicional por ambiente.

A correção deve alcançar qualquer caminho ainda acessível ao usuário.

47. CRIAR MATRIZ DE COBERTURA DE REQUISITOS

Para cada requisito, documente:

REQUISITO
→ implementação responsável
→ arquivos afetados
→ teste unitário
→ teste de integração
→ teste end-to-end
→ evidência de aprovação.

Nenhum requisito pode ficar sem implementação identificável e sem método de validação.

48. EXIGIR COBERTURA DOS RAMOS CRÍTICOS

Não usar cobertura percentual global como única medida.

Identifique explicitamente os branches críticos da funcionalidade e confirme que cada um foi exercitado.

Especialmente:

* true/false de condicionais;
* limites;
* estados de erro;
* estados vazios;
* caminhos alternativos;
* permissões;
* fallbacks legítimos.

49. VERIFICAR TESTES QUE PASSAM PELO MOTIVO ERRADO

Revise os testes criados e confirme:

* que cada assert verifica realmente o comportamento solicitado;
* que nenhum teste é excessivamente permissivo;
* que mocks não eliminam justamente a lógica que deveria ser validada;
* que snapshots não escondem erro semântico;
* que o teste falharia se a implementação estivesse incorreta.

50. MINIMIZAR MOCKS EM FLUXOS CRÍTICOS

Mocks são permitidos quando necessários, mas os fluxos críticos devem possuir testes com o máximo possível de componentes reais integrados.

Não considere uma API ou integração validada apenas porque um mock respondeu como esperado.

51. TESTAR ORDEM DAS OPERAÇÕES

Execute as mesmas ações em ordens diferentes quando a ordem não deveria alterar o resultado.

Exemplo:
A → B → C

e também:
B → A → C

Quando semanticamente equivalentes, devem produzir resultado equivalente.

52. TESTAR TRANSIÇÕES DE ESTADO

Não valide apenas estados finais.

Teste cada transição importante:

vazio → preenchido;
preenchido → alterado;
alterado → apagado;
válido → inválido;
inválido → válido;
selecionado → desselecionado → selecionado novamente.

53. VERIFICAR DETERMINISMO

Executando o mesmo cenário com as mesmas entradas e mesmo estado inicial, o resultado deve ser reproduzível.

Se houver comportamento não determinístico legítimo, documentá-lo explicitamente.

54. GARANTIR REPRODUTIBILIDADE DOS TESTES

Informe comandos exatos necessários para reproduzir:

* instalação;
* lint;
* type-check;
* testes;
* E2E;
* build.

Evite testes que dependam de estado local não documentado.

55. NÃO MODIFICAR TESTES PARA ESCONDER REGRESSÃO

É proibido resolver teste quebrado simplesmente:

* removendo o teste;
* relaxando assert;
* aumentando timeout indiscriminadamente;
* ignorando teste;
* marcando como flaky;
* atualizando snapshot sem verificar semanticamente a diferença.

Se um teste antigo deixar de fazer sentido por alteração intencional de requisito, documentar explicitamente a razão.

56. NÃO DEIXAR TODO, FIXME OU WORKAROUND

Antes da conclusão, procurar no código alterado:
TODO
FIXME
HACK
TEMP
WORKAROUND

Nenhum item relacionado à implementação solicitada pode permanecer sem justificativa explícita.

57. NÃO DEIXAR CÓDIGO INACESSÍVEL OU DESATIVADO

Não considerar funcionalidade implementada se estiver:

* atrás de feature flag não habilitada;
* comentada;
* sem rota acessível;
* sem import;
* sem integração real com a interface;
* presente no código mas não utilizada pelo fluxo real.

58. VALIDAR A FUNCIONALIDADE NO ARTEFATO FINAL

Não confiar apenas em testes do código fonte.

Quando possível, testar também o build final efetivamente produzido e o mesmo fluxo que o usuário utilizará.

59. COMPARAR ANTES E DEPOIS

Para funcionalidades não relacionadas à mudança, executar smoke tests equivalentes antes e depois.

Qualquer diferença inesperada deve ser investigada.

60. CRIAR CHECKLIST DE REGRESSÃO PERMANENTE

Transforme os cenários críticos desta correção em testes permanentes do projeto para serem executados automaticamente em alterações futuras.

61. PRIORIZAR CAUSA RAIZ SOBRE NÚMERO DE ALTERAÇÕES

Não tente minimizar quantidade de arquivos alterados se isso mantiver arquitetura incorreta.

Por outro lado, não faça refatorações desnecessárias fora do escopo.

Modificar exatamente o que for necessário para eliminar estruturalmente a classe do problema.

62. REGISTRAR DECISÕES ARQUITETURAIS IMPORTANTES

Quando uma mudança estrutural significativa for necessária, documente brevemente:

* problema;
* alternativas consideradas;
* solução escolhida;
* razão da escolha;
* impactos;
* trade-offs.

63. REALIZAR REVISÃO ADVERSARIAL FINAL

Após todos os testes, faça uma última revisão assumindo que a implementação contém algum erro ainda não encontrado.

Procure ativamente uma forma de fazê-la falhar.

Pergunte:

* Qual entrada eu ainda não testei?
* Qual estado poderia ficar desatualizado?
* Qual caminho alternativo não utiliza a nova lógica?
* Qual condição de corrida pode existir?
* Qual comportamento funciona apenas por coincidência?
* Qual componente ainda poderia manter implementação própria?
* Qual dado válido poderia ser rejeitado?
* Qual dado inválido poderia ser aceito?
* Qual regressão não seria detectada pela suíte atual?

Somente depois desta revisão considere a implementação tecnicamente concluída.

64. DECLARAR INCERTEZAS E LACUNAS REMANESCENTES

Se algum ponto não puder ser comprovado, não declarar “sem erros”.

Informar exatamente:

* o que não pôde ser testado;
* por que não pôde ser testado;
* risco residual;
* como deveria ser validado.

Diferenciar claramente:
COMPROVADO POR TESTE
VALIDADO POR INSPEÇÃO
INFERIDO
NÃO VALIDADO.

65. NÃO UTILIZAR LINGUAGEM DE CERTEZA SEM EVIDÊNCIA

Não informar:
“tudo funcionando”,
“100% corrigido”,
“sem bugs”,
“sem lacunas”

sem evidência objetiva compatível.

Relatar somente aquilo que foi efetivamente verificado.

66. ACEITAÇÃO BASEADA EM EVIDÊNCIA

A tarefa somente deve ser considerada concluída quando cada requisito possuir pelo menos uma evidência verificável de que foi atendido.

Quando uma evidência automatizada for tecnicamente possível, prefira evidência automatizada à mera inspeção visual.

67. SEPARAR IMPLEMENTAÇÃO E REVISÃO

Quando possível, executar duas fases distintas:

FASE A — IMPLEMENTAÇÃO
Corrigir e implementar os requisitos.

FASE B — REVISÃO ADVERSARIAL
Reexaminar a alteração sem assumir que a implementação da Fase A está correta.

Na Fase B, não utilizar o sucesso dos testes anteriores como prova suficiente. Reavaliar requisitos, código, fluxos e casos-limite independentemente.

68. CRITÉRIO DE FALHA

Se qualquer requisito permanecer sem validação, qualquer teste crítico falhar ou houver regressão conhecida, a tarefa deve ser classificada como NÃO CONCLUÍDA, e não como parcialmente aprovada.

Corrigir e repetir o ciclo de validação sempre que tecnicamente possível.

69. PRINCÍPIO DE RASTREABILIDADE TOTAL

Deve ser possível responder, para cada requisito:

“Qual código implementa isso?”

“Qual teste prova isso?”

“Qual resultado demonstra que o teste passou?”

Se alguma dessas três perguntas não tiver resposta, considere o requisito ainda não suficientemente validado.
