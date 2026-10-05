# Hermes Email Manager website

Static informational website for a personal Gmail assistant. No build step, JavaScript, forms, analytics, or OAuth implementation is included.

## Pages

- Homepage: https://mail.kent-huang.dev/
- Privacy policy: https://mail.kent-huang.dev/privacy.html
- Public contact: kentwelcome@gmail.com

## Hosting

Use GitHub Pages, deploying the `main` branch root. `CNAME` sets the intended custom domain.

The domain owner must create a DNS CNAME record: `mail` → `kentwelcome.github.io` (not a repository URL). Do not put an HTTP scheme or path in the DNS value. After DNS validation and certificate issuance, enable Enforce HTTPS in the repository Pages settings. Domain ownership verification using GitHub's supplied TXT record is recommended; obtain the exact value from GitHub rather than inventing one.

OAuth Branding homepage and privacy URLs should only be submitted once both HTTPS URLs load publicly. Add the authorized domain `kent-huang.dev` where Google requests it and complete ownership verification if required. This site does not guarantee OAuth publishing or verification approval. Match the OAuth app name to the site name.

## Local preview and validation

```sh
python3 -m http.server 8765 --bind 127.0.0.1
python3 tests/test_site.py
```

## Privacy copy maintenance

The policy intentionally does not claim fixed deletion periods, local-only processing, provider-wide no-training guarantees, or Google verification. It discloses configurable external AI and notification services without inventing a provider inventory. Review actual permissions, provider terms, retention, and Google API policy requirements before expanding beyond personal use. Do not commit mailbox content or credentials.
