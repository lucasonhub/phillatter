# Mente Semanal

Agregador acadêmico em Python + MkDocs Material. Reúne Filosofia da Mente, Inteligência Artificial, Ciências Cognitivas e Neurociência. Markdown é a fonte do site e pode ser aberto no Obsidian. Não usa LLM nem serviços pagos de geração de texto.

## Estrutura

```text
.
├── .github/workflows/update_publications.yml
├── .gitignore
├── requirements.txt             # versões principais testadas
├── requirements.lock.txt        # ambiente completo testado
├── topics.yml                  # buscas e limite por consulta
├── mkdocs.yml                  # tema, busca, navegação e hook
├── scripts/
│   ├── collect.py              # coletor completo OpenAlex + arXiv + PhilPapers
│   ├── render_site.py          # páginas, edições e RSS
│   ├── site_hook.py            # atualiza índices antes de cada build
│   └── send_newsletter.py      # prévia e envio SMTP opcional
├── docs/                       # pode ser aberto como cofre Obsidian
│   ├── index.md                # gerado; filtro por tema
│   ├── categories.md           # gerado; índice por tags
│   ├── feed.xml                # gerado; RSS de edições
│   ├── publications/<id>.md    # gerados; uma nota por publicação
│   ├── editions/
│   │   ├── index.md            # gerado; arquivo de edições
│   │   └── AAAA-MM-DD.md       # gerados; edições semanais
│   ├── javascripts/filter.js
│   └── stylesheets/newsletter.css
├── data/editions/AAAA-MM-DD.json  # IDs incluídos em cada edição
├── private/                    # criar localmente; ignorado pelo Git
│   ├── subscribers.json        # destinatários opt-in
│   └── sent.json               # controle de envio por edição/destinatário
└── tests/test_pipeline.py
```

Os diretórios de publicações e manifests começam vazios. O site vazio funciona e não contém dados acadêmicos fictícios. `mkdocs build` cria `site/`, que não deve ser versionado.

## Rodar localmente

Requer Python 3.12. Execute na raiz do projeto:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.lock.txt
export CONTACT_EMAIL='seu-email@example.org'
export SITE_URL='https://lucasonhub.github.io/phillatter/'
read -rsp 'Chave OpenAlex: ' OPENALEX_API_KEY
export OPENALEX_API_KEY
python scripts/collect.py
mkdocs build --strict
mkdocs serve
```

No Windows, ative com `.venv\Scripts\Activate.ps1` e configure variáveis com `$env:NOME='valor'`. Não armazene a chave no Git. O script não carrega `.env` automaticamente.

Obtenha uma chave gratuita na conta do [OpenAlex](https://openalex.org/). Este projeto exige `OPENALEX_API_KEY`; não depende do acesso anônimo. Consulte a [documentação da API](https://developers.openalex.org/) para os limites vigentes da conta. O arXiv não exige chave: veja o [manual da API](https://info.arxiv.org/help/api/user-manual.html).

A rede do ambiente em que este pacote foi preparado não permitiu consultas ao vivo a essas duas APIs nem aos feeds do PhilPapers. O tratamento dos formatos foi testado com fixtures; autenticação, cotas e disponibilidade devem ser conferidas na primeira coleta real.

## GitHub Pages e automação

1. Este projeto está preparado para o repositório público `lucasonhub/phillatter`, na branch `main`. Os arquivos incluem o diretório `.github/`. Para usá-lo em outro repositório, copie os arquivos e ajuste a URL pública.
2. Em **Settings → Secrets and variables → Actions**, adicione o secret `OPENALEX_API_KEY`. Em **Variables**, configure `CONTACT_EMAIL` e `SITE_URL` (por exemplo, `https://lucasonhub.github.io/phillatter/`). Se `SITE_URL` não estiver definida no Actions, o workflow usa automaticamente `https://lucasonhub.github.io/phillatter/` neste repositório. A URL deve incluir o subdiretório do repositório e terminar com `/`; para repositório `usuario.github.io`, use a raiz.
3. Em **Settings → Pages → Build and deployment → Source**, selecione **GitHub Actions**. Depois, crie a variável de Actions `ENABLE_PAGES` com valor `true`. Sem essa variável, os testes e o build rodam, mas o deploy é ignorado; isso permite adicionar os arquivos antes de configurar a hospedagem.
4. Verifique que a política de Actions permite gravar conteúdo. O job declara `contents: write` para salvar Markdown na `main`; regras de proteção que proíbam push do bot precisam permitir esse fluxo. Não altere uma branch protegida sem revisar a política do repositório.
5. Abra **Actions → Atualizar publicações e GitHub Pages → Run workflow** com `collect` marcado. Para reconstruir sem consultar as APIs, desmarque esse campo.

O workflow completo está em `.github/workflows/update_publications.yml`. Executa às **segundas-feiras, 09:17 UTC / 06:17 em Fortaleza** (`17 9 * * 1`). Horários de Actions são aproximados, sujeitos a fila. Em repositórios públicos sem atividade, agendamentos podem ser desativados após 60 dias; reative em Actions se necessário.

O fluxo é: testes → coleta (schedule/manual) → build estrito → commit dos Markdown/manifests → upload do site → deploy Pages. Push na `main` só reconstrói, sem nova coleta. Commits feitos pelo `GITHUB_TOKEN` não disparam outro workflow de push. A concorrência não cancela execuções em andamento.

O feed ficará em `https://lucasonhub.github.io/phillatter/feed.xml`. Contém uma entrada por edição e as 52 edições mais recentes; o arquivo completo permanece no site.

## Como o coletor funciona

- Janela padrão: sete dias **completos em UTC**, do início de `hoje - 7 dias` até o início de hoje, fim exclusivo. Na execução de segunda-feira, cobre segunda a domingo anteriores. `--end 2026-10-12` usa `[2026-10-05, 2026-10-12)`.
- OpenAlex usa `publication_date`, pesquisa textual configurável e filtro `type:article|book|dissertation`. Reconstrói o abstract a partir de `abstract_inverted_index`; campo ausente fica vazio no YAML e indicado na página.
- arXiv usa `submittedDate`, ordenação e paginação. Registros são `type: preprint`: eles não são classificados como artigos revisados por pares. Versões `v1`, `v2` etc. compartilham o mesmo ID de origem.
- Respeita intervalo mínimo de 3,2 segundos entre chamadas arXiv; timeouts, retry com backoff e `Retry-After` em 429/5xx. OpenAlex usa cursores; arXiv usa offsets.
- Todas as consultas terminam antes da gravação. HTTP inválido, XML inválido e limite excedido falham, sem publicar uma edição parcial. O workflow só faz commit após build bem-sucedido.
- No OpenAlex, consultas com mais de 5.000 resultados são divididas automaticamente em intervalos menores de dias, sem sobreposição e sem truncar resultados. O limite de segurança vale para cada intervalo; se um único dia ultrapassá-lo, refine `topics.yml` ou ajuste `max_results_per_query`. O arXiv também limita esta implementação a 10.000 por consulta. Não há truncamento silencioso nem seleção artificial dos “melhores” resultados.
- Deduplica por DOI normalizado, ID de origem e título normalizado + primeiro autor. Combina categorias e fontes; não é uma resolução bibliográfica perfeita. Correspondências ambíguas entre notas existentes interrompem a gravação para revisão. Notas mantêm IDs e URLs estáveis.
- Uma edição inclui somente novas notas descobertas na execução, podendo receber novos itens numa repetição da mesma data. Repetir a mesma coleta não duplica notas nem substitui a edição por uma lista vazia. Não execute dois coletores simultâneos no homelab; o workflow já serializa execuções.
- Categorias são atribuídas pela busca que encontrou o trabalho, não por classificação semântica. Trabalhos podem ter várias categorias. Ajuste os termos para equilibrar abrangência e ruído. As buscas em inglês não garantem cobertura de literatura em português.
- Atrasos de indexação podem fazer trabalhos escaparem à janela. Para recuperação, rode `python scripts/collect.py --days 30`; os recuperados entram na edição dessa execução com a data original preservada. Isso não reconstitui automaticamente edições antigas. Agendamentos perdidos também exigem aumentar a janela.
- Não baixa PDFs nem inventa resumos ausentes. Metadados são preservados no frontmatter; o corpo e o HTML escapam conteúdo vindo das APIs. Os resumos e descrições RSS continuam no idioma original.

Exemplo do esquema de uma nota (apenas ilustração; não incluída no conteúdo):

```yaml
---
title: Título retornado pela fonte
authors:
  - Nome do autor
date: '2026-10-14'
type: article
category:
  - Filosofia da Mente
doi: null
abstract: Texto original do resumo, ou string vazia.
source:
  - OpenAlex
source_ids:
  - https://openalex.org/W0000000000
url: https://openalex.org/W0000000000
discovered_at: '2026-10-15'
tags:
  - Filosofia da Mente
---
```

`category` e `tags` são listas para permitir classificação múltipla. `doi` é uma string sem o prefixo `https://doi.org/`, ou `null`. Os campos pedidos estão em todas as notas de publicação; notas de índice e de edição usam metadados próprios. `date` indica publicação/submissão nas APIs. Para PhilPapers, consulte `date_basis` conforme a seção abaixo. `discovered_at` indica quando a nota entrou no acervo.

## Alertas PhilPapers (RSS/Atom)

O coletor usa **feedparser** para cinco categorias do PhilPapers:

| Categoria no PhilPapers | Categoria no site |
| --- | --- |
| Philosophy of Mind | Filosofia da Mente |
| Philosophy of Cognitive Science | Filosofia da Ciência Cognitiva |
| Theory of Computation | Teoria da Computação |
| Computationalism | Computacionalismo |
| Philosophy of Consciousness | Filosofia da Consciência |

As três últimas foram adicionadas às duas originais. Os filtros e as tags do site são gerados automaticamente quando houver publicações coletadas nessas categorias. A configuração das páginas não confirma que os feeds estejam acessíveis: a descoberta do RSS no GitHub Actions continua pendente.

Em `topics.yml`, cada fonte tem `page_url`, `category` e `feed_url`. Com `feed_url: null`, o script abre a página oficial e procura o formulário `allparams` usado pelo botão RSS que chama `/utils/feed.pl`. Ele lê os campos da própria página e reproduz as alterações `noheader=1`, `__action` e `format` vazio na URL de consulta, sem executar JavaScript. Também aceita um único link RSS/Atom tradicional anunciado na página. Isso evita inventar IDs numéricos de categorias. Se não houver um único link identificável, a coleta falha com uma instrução para copiar o endereço do RSS oferecido pela categoria para `feed_url`. O suporte ao formulário foi testado com HTML simulado baseado no botão RSS observado no site. A confirmação ao vivo continua necessária: a política de rede deste ambiente não permite `philpapers.org`. O parser e a integração foram testados com feeds simulados.

Você pode fixar os endereços reais em `feed_url`, copiados do link de RSS em cada categoria:

- https://philpapers.org/browse/philosophy-of-mind
- https://philpapers.org/browse/philosophy-of-cognitive-science
- https://philpapers.org/browse/theory-of-computation
- https://philpapers.org/browse/computationalism
- https://philpapers.org/browse/philosophy-of-consciousness

A busca das páginas só é necessária enquanto `feed_url` estiver vazio. O trecho `/utils/feed.pl` sozinho não identifica a categoria: são necessários os campos do formulário. Os feeds são verificados antes das APIs, para falhar cedo se a descoberta não funcionar. O download usa a mesma sessão HTTP, timeouts e retries das APIs; `feedparser` recebe os bytes baixados, sem abrir conexões por conta própria. Feeds inválidos ou respostas HTML interrompem a execução antes da gravação. Não há alteração necessária no workflow: ele instala o arquivo de dependências atualizado e executa o mesmo coletor.

Tratamento dos campos:

- `source: [PhilPapers]`, ID estável da ficha e deduplicação com as outras fontes por DOI/ID/título + primeiro autor.
- `date_basis: feed_published` para data publicada no RSS; `feed_updated` quando só houver data de atualização. O filtro de sete dias usa essa data UTC do **alerta**, que pode diferir da data bibliográfica da obra.
- Sem data utilizável, a entrada ainda disponível no feed entra por descoberta, com `date_basis: discovered` e `date` igual à data UTC real da execução. Não é apresentada como publicação comprovadamente lançada nos sete dias. O ID impede repetição nas próximas coletas.
- `type: unknown` quando o feed não informa tipo confiável, sem presumir que toda ficha é artigo. Um registro correspondente do OpenAlex pode preencher o tipo conhecido.
- Descrição HTML é convertida em texto e armazenada em `abstract` com `abstract_basis: feed_summary`. A página a identifica como **Descrição do feed**; não há alegação de que seja um abstract. Descrição ausente fica vazia. Um abstract real obtido no OpenAlex tem preferência sobre a descrição RSS na união de registros.
- Autores e DOI só são preenchidos quando disponíveis nos campos do feed. Não são inferidos de referências citadas na descrição.

RSS é uma lista finita de itens recentes, não uma API histórica paginada: uma coleta semanal pode perder alertas que saiam do feed entre execuções. `--days 30` amplia o filtro temporal, mas não recupera itens que o feed já deixou de fornecer. Para aumentar cobertura, é necessário coletar com maior frequência ou complementar pela API OpenAlex.

## Obsidian

Abra `docs/` como cofre, ou copie essa pasta para um cofre existente. Links entre edições e publicações são Markdown padrão, sem depender de wikilinks. As propriedades YAML são acessíveis no Obsidian; nenhuma extensão é necessária. `tags` preserva os nomes legíveis com espaços e acentos como propriedades YAML; para usar as hashtags nativas do Obsidian, você pode adaptar para slugs sem espaços.

Trate `publications/`, `editions/`, `index.md`, `categories.md` e `feed.xml` como arquivos gerados. Mantenha anotações pessoais em outra pasta ou cofre, pois as notas geradas são reescritas. Não publique um cofre que contenha notas privadas por engano.

## Busca, filtros e RSS

MkDocs Material indexa títulos, autores, abstracts e edições com suporte a português e inglês. A busca roda no navegador, sem banco de dados. O seletor na página inicial filtra por tema usando o mesmo conteúdo de `category`/`tags`. O índice Temas oferece navegação sem JavaScript. O hook gera índices e RSS em todo `mkdocs build`, inclusive no homelab.

O visual usa tipografia serifada nos títulos, cartões discretos, modo escuro e fontes locais do sistema. Nenhuma requisição a Google Fonts. O volume cresce com o acervo: grandes coleções podem precisar de paginação e de um índice de busca menor no futuro.

## Newsletter por SMTP (opcional)

O site e RSS funcionam sem provedor de e-mail. Buttondown e outros serviços RSS-to-email têm preços e limites próprios; não presuma que Substack ou Buttondown ofereçam importação automática e gratuita de qualquer RSS. Para manter a integração independente, há um script SMTP completo.

Use uma conta SMTP existente. Crie `private/subscribers.json` com endereços que consentiram em receber a newsletter:

```json
["pessoa1@example.org", "pessoa2@example.org"]
```

Configure o ambiente (as credenciais ficam fora do repositório):

```bash
export SITE_URL='https://lucasonhub.github.io/phillatter/'
export SMTP_HOST='smtp.seu-provedor.example'
export SMTP_PORT='587'
export SMTP_MODE='starttls'
export SMTP_FROM='newsletter@seu-dominio.example'
export SMTP_USER='seu-usuario'
export UNSUBSCRIBE_EMAIL='descadastro@seu-dominio.example'
read -rsp 'Senha SMTP: ' SMTP_PASSWORD
export SMTP_PASSWORD
python scripts/send_newsletter.py --edition 2026-10-12
# Após revisar a prévia e publicar a edição:
python scripts/send_newsletter.py --edition 2026-10-12 --send
```

Use uma data que exista em `data/editions/`. Para TLS direto, configure `SMTP_MODE=ssl`, porta `465`. Um servidor local pode dispensar login, mas o script sempre exige TLS válido. Cada destinatário recebe mensagem individual, sem expor a lista. Uma edição vazia não é enviada.

O script grava confirmações em `private/sent.json`, ignorado pelo Git. Preserve essa pasta em volume privado no homelab. O controle evita reenvios comuns, mas uma falha entre a aceitação SMTP e a gravação local pode duplicar uma mensagem; Message-ID determinístico não garante deduplicação no provedor. Após o envio, não altere uma edição esperando reenviar aos mesmos destinatários automaticamente. Descadastro é manual: monitore a caixa indicada e remova quem pedir da lista. Não há formulário público de inscrição neste site estático.

O workflow não envia e-mails automaticamente. Para isso no homelab, acrescente o comando de envio depois de publicar com sucesso. Se adaptar ao Actions, injete a lista por secret e armazene o estado em armazenamento privado persistente; `private/` local ao runner é efêmero. Nunca versione a lista em repositório público.

## Homelab e cron

Sirva a pasta `site/` com Nginx, Caddy ou outro servidor estático existente. Defina `SITE_URL` como o endereço público real antes do build para gerar links RSS corretos. O acesso aos conteúdos publicados continua estático.

Exemplo de cron de segunda-feira, **09:17 no fuso configurado no host**:

```cron
17 9 * * 1 /usr/bin/flock -n /tmp/mente-semanal.lock /srv/mente-semanal/update.sh >> /srv/mente-semanal/update.log 2>&1
```

Crie `update.sh` executável, contendo:

```sh
#!/bin/sh
set -eu
cd /srv/mente-semanal
# Arquivo privado do servidor: export CONTACT_EMAIL=..., OPENALEX_API_KEY=..., SITE_URL=...
. /srv/mente-semanal/private/environment.sh
.venv/bin/python scripts/collect.py
.venv/bin/mkdocs build --strict --site-dir site-next
# Copie somente após build completo; aponte o servidor para /var/www/mente-semanal.
rsync -a --delete site-next/ /var/www/mente-semanal/
# Opcional, se SMTP já estiver configurado no arquivo privado e o site estiver publicado:
# .venv/bin/python scripts/send_newsletter.py --edition "$(date -u +%F)" --send
```

Instale `flock`/`rsync` se necessário e use permissões mínimas para o processo. O cron usa o fuso do host; a janela de coleta continua UTC.

## Custos e validação

GitHub Pages e runners padrão de Actions em repositório público permitem esta arquitetura sem custo de hospedagem nas condições dos planos gratuitos. Em repositório privado ou com limites/políticas diferentes, verifique a franquia. Um domínio próprio, energia do homelab e envio SMTP podem ter custo; não são necessários para servir o site no domínio gratuito do Pages. A conta OpenAlex tem cotas de uso; não configure faturamento pago se a intenção for permanecer no nível gratuito.

Validação local:

```bash
python -m unittest discover -s tests -v
mkdocs build --strict
```

Os testes verificam reconstrução de abstract, parser arXiv e versões, paginação e intervalo OpenAlex, limite de segurança, deduplicação, escaping de conteúdo e RSS com subdiretório. O site vazio e um site com registros simulados são construídos na validação de entrega. Nenhum envio real de e-mail ou deploy foi realizado.
