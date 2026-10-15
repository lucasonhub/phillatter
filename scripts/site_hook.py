import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_site import render


def on_pre_build(config):
    render(site_url=config['site_url'])
