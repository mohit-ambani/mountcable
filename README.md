# Mount Cable India

Marketing website for **Mount Cable India** — authorized distributors of **Finolex, Polycab & Wipro** and dealers for leading electrical brands in Bengaluru. Showrooms in **Jayanagar** and **Chickpete**.

## Stack
Plain static HTML/CSS/JS. Brand pages are generated from a single data table in `build.py`.

## Edit content
All copy, contact details and the brand list live in `build.py`:
- `PHONE`, `EMAIL`, `WHATSAPP` — **update these with real details**
- `OFFICES` — showroom addresses
- `BRANDS` — each brand's name, colour, tier, categories and blurb

After editing, regenerate the pages:

```bash
python3 build.py
```

This rewrites `index.html` and `brands/*.html`.

## Brands covered
**Authorized Distributors:** Finolex · Polycab · Wipro
**Dealers:** Havells · Legrand · Schneider Electric · GM Modular · Goldmedal · Cona · Lisha · Hifi · Norisys · Indo Asian

## Deploy
Hosted on Vercel (static). Pushing to `main` triggers a deploy. Custom domain: **mountcable.com**.

> Note: brand names and logos are the property of their respective owners and are shown to indicate products available for sale.
