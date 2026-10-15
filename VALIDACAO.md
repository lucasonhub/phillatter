# Validação da entrega

- Python 3.12: dez testes unitários passaram.
- `mkdocs build --strict`: passou com acervo vazio.
- Build adicional com uma publicação e edição simuladas: passou; confirmados arquivo de publicação, links com subdiretório, marcação do filtro, índice de busca e RSS.
- Prévia SMTP com edição simulada: passou, sem enviar mensagem.
- Dependências efetivamente usadas registradas em `requirements.lock.txt`.
- Sem consultas reais ao OpenAlex/arXiv/PhilPapers, sem envio SMTP real e sem publicação no GitHub Pages.
- Não houve validação visual em navegador. O filtro foi verificado no código e na marcação gerada, sem teste de interação em navegador.

A amostra simulada foi criada em diretório temporário e não integra o acervo entregue.

A extensão PhilPapers verifica limites de data, entradas sem data, Atom com atualização, remoção de HTML, rejeição de feed inválido, descoberta do link RSS, URL explícita, duas categorias, integração no coletor, deduplicação entre fontes e preferência por abstract/tipo conhecidos.
