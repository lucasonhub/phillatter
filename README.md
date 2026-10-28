# Phillater

O projeto publica **dez artigos por semana**, escolhidos pela relação com a pesquisa sobre teoria computacional da mente, representação simbólica, computação, intencionalidade e limites do computacionalismo. Artigos antigos são elegíveis: não há filtro por data de publicação.

O acervo gerado pela coleta ampla foi reiniciado em 28/10/2026. A remoção abrange as publicações Markdown, edições, manifests e o RSS ativos. O histórico Git não foi reescrito. A automação pessoal de três leituras na sexta-feira é uma tarefa independente e não foi alterada.

## Critérios da seleção

O perfil está em [`research_profile.yml`](research_profile.yml). Foi elaborado a partir das seis perguntas de pesquisa explicitamente fornecidas pelo usuário. As seis perguntas de pesquisa fornecidas pelo usuário estão registradas nesse arquivo e podem ser ajustadas.

A classificação é **lexical e determinística**, baseada em título e resumo. Não utiliza embeddings, LLM ou uma avaliação humana do texto integral. Ela aproxima a aderência ao recorte, mas não garante identificar os dez melhores artigos de toda a literatura. Cada nota registra a pontuação, os temas encontrados e a justificativa automática. A revisão crítica continua necessária.

- Definição e implementação de sistemas computacionais: peso 5.
- Computação e teoria computacional da mente: peso 5.
- Alcance da computação e explicação dos fenômenos mentais: peso 4.
- Computação e formalização em combinação com os demais temas: peso 3.
- Representação simbólica, linguagem do pensamento e fundamentação de símbolos: peso 4.
- Intencionalidade e conteúdo semântico: peso 4.
- Limites e alternativas, como sala chinesa e cognição incorporada: peso 3.

Uma correspondência no título recebe três vezes o peso de uma correspondência apenas no resumo. Repetição de palavras não acumula pontos. É exigido o grupo específico de teoria computacional, a combinação representação/intencionalidade um tema específico de individuação da computação, ou computação genérica acompanhada de representação, intencionalidade, críticas ou fenômenos mentais. A nota mínima padrão é 10. Entre os candidatos elegíveis, a seleção reserva primeiro uma contribuição para cada uma das seis perguntas de pesquisa, quando houver candidatos correspondentes, e preenche as vagas restantes por pontuação. Isso evita concentrar toda a semana em uma única frente. A cobertura é aproximada por termos do perfil; não é uma leitura dos argumentos dos artigos. Citações são usadas apenas para desempatar a pontuação; o ano não afeta a classificação.

São elegíveis `article` e `preprint`, identificados na página. Livros, dissertações e registros de tipo indeterminado não são publicados automaticamente. Descrições de feeds não são apresentadas como abstracts originais: a procedência é registrada. Registros do PhilPapers sem tipo confirmado só podem se tornar elegíveis quando combinados com metadados de um artigo/preprint identificado por outra fonte.

## Dez por semana e controle de repetição

A semana editorial vai de **segunda a domingo**, usando a data local de Fortaleza na execução. Uma edição normal contém exatamente dez artigos. O script rejeita configurações acima de dez e não publica uma lista parcial se faltarem candidatos inéditos com a pontuação mínima. Nesse caso, a execução explica a falta e exige revisar/ampliar as consultas; não preenche a lista com textos sem aderência.

A primeira execução bem-sucedida da semana fixa sua edição. Reexecutar na mesma semana não acrescenta, troca ou duplica artigos e dispensa novas consultas de rede. Na semana seguinte, os artigos publicados são excluídos da seleção por DOI, identificadores de origem e título/autor normalizados. Essa conciliação bibliográfica não é perfeita quando as fontes oferecem metadados incompletos ou divergentes.

O controle fica em `data/selection_state.json` e nos manifests `data/editions/AAAA-MM-DD.json`. Preserve esses arquivos para impedir repetições futuras. A reinicialização solicitada inicia um novo histórico editorial; artigos do acervo antigo podem voltar a ser selecionados se atenderem ao perfil atual.

Os candidatos não selecionados são avaliados em memória e não geram notas nem páginas. Só os dez selecionados entram em `docs/publications/`. Os manifests das edições determinam o conteúdo do site; o build remove arquivos órfãos das pastas geradas para evitar que conteúdo antigo reapareça no índice de busca.

## Fontes e limites da busca

`topics.yml` contém as fontes e os limites de candidatos, separados da quantidade publicada:

- **OpenAlex:** dez consultas direcionadas pelo perfil, até 100 candidatos por consulta. Pesquisa em todos os anos, com `type:article`, ordenação padrão por relevância da API e sem filtro de data.
- **arXiv:** até 100 candidatos por relevância, usando a expressão do perfil e sem filtro de submissão recente. Publicações selecionadas dessa fonte são rotuladas como preprints.
- **PhilPapers:** quatro feeds explícitos existentes foram mantidos: Filosofia da Inteligência Artificial (`349`), Filosofia da Ciência Cognitiva, Miscelânea (`387`), Filosofia da Consciência (`130`) e Filosofia da Consciência, Miscelânea (`131`). O coletor segue a página intermediária até o RSS oficial. Itens com data antiga não são excluídos. Os feeds são finitos e não equivalem ao catálogo histórico completo do PhilPapers.

Não se tenta indexar a totalidade das bases. A cobertura depende dessas amostras e dos termos escolhidos. Quando uma consulta/fonte falha, a seleção pode prosseguir com as fontes disponíveis, desde que ainda obtenha dez candidatos elegíveis. O manifest informa quais fontes responderam e quantos candidatos foram avaliados. Se faltarem dez, nada novo é publicado.

A chave OpenAlex é usada quando `OPENALEX_API_KEY` está configurada. A ausência é registrada no relatório das fontes e poderá impedir chegar aos dez artigos, sobretudo porque muitos feeds do PhilPapers não informam o tipo bibliográfico. `CONTACT_EMAIL` é obrigatório para identificar o coletor.

## Estrutura

```text
research_profile.yml              perfil, pesos e consultas acadêmicas
topics.yml                        fontes e limites de candidatos
scripts/collect.py                parsers e entrada compatível da CLI
scripts/curate.py                 seleção histórica, quota e controle semanal
scripts/render_site.py            páginas, índice de temas e RSS
scripts/site_hook.py              atualiza conteúdo antes do build
scripts/send_newsletter.py        prévia e envio SMTP opcional
.github/workflows/update_publications.yml
mkdocs.yml
requirements.txt
requirements.lock.txt
docs/publications/                somente artigos selecionados
docs/editions/                    somente edições atuais
docs/index.md                     página inicial gerada
docs/categories.md                índice de temas gerado
docs/feed.xml                     feed de edições semanais
data/editions/                    composição de cada edição
data/selection_state.json         identidades já utilizadas após a reinicialização
tests/                            parsers, curadoria, quota e renderização
```

Cada artigo conserva `title`, `authors`, `date`, `type`, `category`, `doi` e `abstract`, além da origem dos dados. O YAML também inclui `selected_at`, `selection_week`, `selection_score`, `selection_reasons` e `selection_basis`. A data editorial de seleção é separada da data bibliográfica; um artigo de 1950 pode ser recomendado em uma edição atual.

## GitHub Actions e publicação

O workflow segue às **segundas-feiras, às 06:17 em Fortaleza / 09:17 UTC**. A execução seleciona os dez artigos, constrói o site, salva os arquivos gerados e publica no Pages. Os horários do Actions são aproximados. Um push na `main` apenas reconstrói e publica o conteúdo já selecionado; não cria uma edição extra.

Configure em **Settings → Secrets and variables → Actions**:

- Secret `OPENALEX_API_KEY`, obtido gratuitamente na conta OpenAlex.
- Variável `CONTACT_EMAIL`, com um endereço válido de contato.
- Variável `ENABLE_PAGES=true` para habilitar publicação.
- Opcionalmente `SITE_URL=https://lucasonhub.github.io/phillatter/`; o workflow calcula esse endereço quando a variável não está definida.

Em **Settings → Pages**, selecione **GitHub Actions** como origem. O bot precisa de permissão para gravar os manifests e Markdown na `main`; regras de proteção da branch devem ser compatíveis com esse fluxo.

Para gerar uma edição agora, abra **Actions → Atualizar publicações e GitHub Pages → Run workflow**, com `collect` marcado. Para reconstruir sem nova seleção, desmarque. A quota vale para a semana editorial, mesmo em execuções manuais. O commit de reinicialização publica inicialmente um site sem artigos; a primeira execução de seleção cria o novo acervo.

O RSS continua em `https://lucasonhub.github.io/phillatter/feed.xml`. Cada entrada corresponde a uma edição com dez artigos; mantém as 52 edições mais recentes. O site conserva o arquivo das edições do novo ciclo. O plugin de busca indexa somente as páginas do novo acervo a cada build.

## Execução local e homelab

Requer Python 3.12:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.lock.txt
export CONTACT_EMAIL='seu-contato@example.org'
export SITE_URL='https://lucasonhub.github.io/phillatter/'
read -rsp 'Chave OpenAlex: ' OPENALEX_API_KEY
export OPENALEX_API_KEY
python scripts/collect.py
mkdocs build --strict
mkdocs serve
```

No PowerShell, ative `.venv\Scripts\Activate.ps1` e use `$env:NOME='valor'`. O script não lê `.env` automaticamente. Guarde segredos fora do Git.

`python scripts/collect.py --date 2026-10-28` escolhe a semana editorial de 26/10/2026. Esse argumento serve a recuperação/backfill editorial: não restringe a data dos artigos. O uso normal dispensa `--date`. As opções antigas `--days` e `--end` foram removidas da CLI para impedir confusão com recência.

Para cron, execute a coleta e o build semanalmente com `flock` para impedir processos simultâneos. Preserve `data/`, publique a pasta `site/` somente depois de um build bem-sucedido e mantenha credenciais privadas no ambiente. Não execute dois coletores ao mesmo tempo. O workflow do Actions já serializa execuções.

## Obsidian e SMTP

Abra `docs/` como cofre Obsidian ou copie suas notas para um cofre pessoal. Guarde anotações particulares fora das pastas geradas: `docs/publications/`, `docs/editions/`, os índices e o RSS são reconstruídos pelo projeto.

O envio SMTP continua opcional. A lista `private/subscribers.json`, o estado `private/sent.json` e credenciais não são publicados nem alterados pela reinicialização do acervo. O script exige TLS e envia uma mensagem individual por destinatário, com prévia por padrão. Use a data de segunda-feira que identifica o manifest da edição:

```bash
python scripts/send_newsletter.py --edition 2026-10-26
# Depois de configurar SMTP e revisar a prévia:
python scripts/send_newsletter.py --edition 2026-10-26 --send
```

Configure `SITE_URL`, `SMTP_HOST`, `SMTP_MODE` (`starttls`/`ssl`), `SMTP_PORT`, `SMTP_FROM`, `SMTP_USER`, `SMTP_PASSWORD` e `UNSUBSCRIBE_EMAIL`. A lista deve conter destinatários opt-in; pedidos de saída são atendidos manualmente. Preserve o estado de envio no homelab. Uma falha entre a aceitação SMTP e a gravação local pode duplicar uma mensagem. O workflow não envia e-mails automaticamente.

## Verificação e limites

```bash
python -m unittest discover -s tests -v
mkdocs build --strict
```

Os testes cobrem fontes, respostas intermediárias do PhilPapers, classificação, inclusão de artigos antigos, exclusão de livros/tipos não confirmados, deduplicação, dez por semana, reexecução na mesma semana, não repetição entre semanas, falta de candidatos e limpeza do conteúdo anterior.

O projeto continua sem infraestrutura paga obrigatória: Python, MkDocs e busca no navegador. GitHub Pages/Actions e OpenAlex estão sujeitos às condições e cotas dos planos gratuitos. SMTP, domínio próprio e energia do homelab podem ter custos próprios. A seleção automática não lê os textos integrais nem traduz os abstracts; seus resultados devem ser avaliados em função da pergunta efetiva da dissertação.
