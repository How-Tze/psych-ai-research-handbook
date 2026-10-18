"""Keep private reading copies offline; authorize only generated reader scripts."""
from urllib.parse import urlsplit

from bs4 import BeautifulSoup

NONCE_MARKER = "AW_RUNTIME_NONCE"


def seal_preview(soup: BeautifulSoup) -> None:
    # Raw scripts and event handlers from prose are not reader functionality.
    for tag in soup.find_all(True):
        for key in list(tag.attrs):
            if key.lower().startswith("on") or key in {"nonce", "srcdoc"}:
                del tag.attrs[key]
        for key in ("href", "src", "action", "xlink:href"):
            value = str(tag.get(key, "")).strip()
            if value.lower().startswith(("javascript:", "vbscript:", "data:text/html")):
                del tag.attrs[key]
    for tag in soup.select('iframe,object,embed,base,meta[http-equiv],link[rel="preconnect"],link[rel="dns-prefetch"]'):
        tag.decompose()
    for script in list(soup.find_all("script")):
        src = urlsplit(script.get("src", ""))
        local_reader = not src.scheme and not src.netloc and "/site_libs/" in "/" + src.path and not script.find_parent("main")
        quarto_init = script.get("id") == "quarto-html-after-body" and not script.find_parent("main")
        if local_reader or quarto_init:
            script["nonce"] = NONCE_MARKER
        elif script.get("type") in {"application/json", "application/ld+json"}:
            continue
        else:
            script.decompose()
    bridge = soup.new_tag("script", src="/bridge.js", nonce=NONCE_MARKER)
    soup.body.append(bridge)


def preview_policy(app_origin: str, nonce: str) -> str:
    return (f"default-src 'self'; script-src 'nonce-{nonce}' 'self'; "
            "style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self' data:; "
            "connect-src 'self'; frame-src 'none'; object-src 'none'; base-uri 'none'; "
            f"form-action 'none'; frame-ancestors {app_origin}")
