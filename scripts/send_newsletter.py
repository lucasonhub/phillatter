#!/usr/bin/env python3
"""Prévia por padrão; --send envia à lista privada de opt-in."""
import argparse
from datetime import date
from email.message import EmailMessage
from email.utils import parseaddr
import hashlib
import json
import os
from pathlib import Path
import smtplib
import ssl
from urllib.parse import urlparse
from collect import ROOT, read_note, write


def address(value):
    if parseaddr(value)[1] != value or '@' not in value or '\n' in value or '\r' in value:
        raise ValueError('Endereço de e-mail inválido')
    return value


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--edition', required=True, type=date.fromisoformat)
    p.add_argument('--send', action='store_true')
    args = p.parse_args()
    edition = json.loads((ROOT / f'data/editions/{args.edition}.json').read_text())
    base = os.environ.get('SITE_URL', '').rstrip('/') + '/'
    if urlparse(base).scheme != 'https' or not urlparse(base).netloc:
        raise SystemExit('Defina SITE_URL com a URL pública HTTPS.')
    text = [f'Mente Semanal — {args.edition}', base + f'editions/{args.edition}/', '']
    for uid in edition['ids']:
        r = read_note(ROOT / f'docs/publications/{uid}.md')
        text += [r['title'], '; '.join(r['authors']),
                 (r['abstract'] or 'Resumo indisponível na fonte.')[:700],
                 base + f'publications/{uid}/', '']
    if not args.send:
        print('\n'.join(text))
        return
    if not edition['ids']:
        print('Edição vazia; nenhum e-mail enviado.')
        return
    sender = address(os.environ['SMTP_FROM'])
    unsubscribe = address(os.environ['UNSUBSCRIBE_EMAIL'])
    path = Path(os.environ.get('SUBSCRIBERS_FILE', str(ROOT / 'private/subscribers.json')))
    recipients = sorted({address(v) for v in json.loads(path.read_text())})
    state_path = ROOT / 'private/sent.json'
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    mode = os.environ.get('SMTP_MODE', 'starttls')
    if mode not in ('ssl', 'starttls'):
        raise SystemExit('SMTP_MODE deve ser ssl ou starttls.')
    cls = smtplib.SMTP_SSL if mode == 'ssl' else smtplib.SMTP
    kwargs = dict(host=os.environ['SMTP_HOST'], port=int(os.environ.get('SMTP_PORT', '465' if mode == 'ssl' else '587')), timeout=45)
    if mode == 'ssl':
        kwargs['context'] = ssl.create_default_context()
    with cls(**kwargs) as smtp:
        if mode == 'starttls':
            smtp.ehlo()
            smtp.starttls(context=ssl.create_default_context())
            smtp.ehlo()
        if os.environ.get('SMTP_USER'):
            smtp.login(os.environ['SMTP_USER'], os.environ['SMTP_PASSWORD'])
        for recipient in recipients:
            token = hashlib.sha256(f'{args.edition}:{recipient}'.encode()).hexdigest()
            if token in state:
                continue
            message = EmailMessage()
            message['Subject'] = f'Mente Semanal — {args.edition}'
            message['From'], message['To'] = sender, recipient
            message['Message-ID'] = f'<{token}@{sender.split("@")[1]}>'
            message['List-Unsubscribe'] = f'<mailto:{unsubscribe}?subject=descadastrar>'
            message.set_content('\n'.join(text) + f'\nPara sair da lista, escreva para {unsubscribe}.\n')
            smtp.send_message(message)
            state[token] = True
            write(state_path, json.dumps(state, indent=2) + '\n')
    print('Envio concluído; estado salvo em private/sent.json.')


if __name__ == '__main__':
    main()
