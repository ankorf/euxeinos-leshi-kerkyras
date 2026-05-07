#!/usr/bin/env python3
"""Generates Protasi_Istoselidas_Euxeinos_Leschi_v2.pdf"""

import base64
import os
import qrcode
import weasyprint
from io import BytesIO

PROJECT_DIR = "/Users/ankorf/Documents/HTMLS/euxeinos-leshi-pontiwn-kerkuras"
OUTPUT_PDF  = f"{PROJECT_DIR}/Protasi_Istoselidas_Euxeinos_Leschi_v2.pdf"
DEMO_URL    = "https://ankorf.github.io/euxeinos-leshi-kerkyras/"

# ── QR code ──────────────────────────────────────────────────────────────────
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=9,
    border=3,
)
qr.add_data(DEMO_URL)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="#1a1a1a", back_color="white")
buf = BytesIO()
qr_img.save(buf, format="PNG")
QR_B64 = base64.b64encode(buf.getvalue()).decode()

# ── Logo ─────────────────────────────────────────────────────────────────────
with open(f"{PROJECT_DIR}/images/logo.jpg", "rb") as f:
    LOGO_B64 = base64.b64encode(f.read()).decode()

# ── HTML ─────────────────────────────────────────────────────────────────────
HTML = f"""<!DOCTYPE html>
<html lang="el">
<head>
<meta charset="UTF-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

* {{ margin:0; padding:0; box-sizing:border-box; }}

body {{
    font-family: 'Inter', 'Liberation Sans', Arial, sans-serif;
    font-size: 9.5pt;
    color: #2c2c2c;
    background: #ffffff;
    line-height: 1.65;
}}

@page {{
    size: A4;
    margin: 18mm 18mm 22mm 18mm;
    @bottom-center {{
        content: "Ευξείνου Λέσχης Ποντίων Κέρκυρας  ·  Πρόταση Νέου Ιστοτόπου  ·  7 Μαΐου 2026";
        font-family: 'Inter', Arial, sans-serif;
        font-size: 7pt;
        color: #aaa;
    }}
}}

@page cover {{
    margin: 12mm 18mm 18mm 18mm;
    @bottom-center {{ content: none; }}
}}

.cover {{ page: cover; }}

/* ── Cover ── */
.cover-wrap {{
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding-top: 8mm;
}}
.cover-logo {{
    width: 88pt;
    height: auto;
    margin-bottom: 20pt;
}}
.cover-title {{
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 27pt;
    font-weight: 700;
    color: #1a1a1a;
    letter-spacing: -0.3pt;
    margin-bottom: 6pt;
}}
.cover-org {{
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 14pt;
    font-weight: 600;
    color: #b8880e;
    margin-bottom: 5pt;
}}
.cover-sub {{
    font-size: 9.5pt;
    color: #777;
    margin-bottom: 18pt;
}}
.cover-rule {{
    width: 55mm;
    height: 2pt;
    background: #b8880e;
    margin: 0 auto 18pt;
}}
.meta-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 9pt;
    margin-top: 4pt;
}}
.meta-table td {{ padding: 5pt 6pt; }}
.meta-table td.lbl {{
    width: 36%;
    font-weight: 600;
    color: #b8880e;
    text-transform: uppercase;
    letter-spacing: 0.6pt;
    font-size: 7.5pt;
    vertical-align: top;
    border-bottom: 0.5pt solid #ebebeb;
}}
.meta-table td.val {{
    border-bottom: 0.5pt solid #ebebeb;
    color: #2c2c2c;
}}

/* ── Intro box ── */
.intro-box {{
    background: #fffdf3;
    border: 1pt solid #d4a820;
    border-left: 5pt solid #d4a820;
    padding: 13pt 15pt;
    margin: 20pt 0 0;
    font-size: 9.5pt;
    line-height: 1.7;
}}
.intro-box .lbl {{
    font-size: 7.5pt;
    font-weight: 700;
    color: #b8880e;
    text-transform: uppercase;
    letter-spacing: 0.8pt;
    margin-bottom: 8pt;
}}

/* ── Section headings ── */
.section-label {{
    font-size: 7pt;
    font-weight: 700;
    color: #b8880e;
    text-transform: uppercase;
    letter-spacing: 1.8pt;
    margin-bottom: 3pt;
}}
.section-title {{
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 18pt;
    font-weight: 700;
    color: #1a1a1a;
    border-bottom: 2pt solid #b8880e;
    padding-bottom: 6pt;
    margin-bottom: 14pt;
}}
.sub-title {{
    font-size: 10.5pt;
    font-weight: 700;
    color: #1a1a1a;
    border-bottom: 1pt solid #e8d48a;
    padding-bottom: 3pt;
    margin: 14pt 0 8pt;
}}

/* ── Feature table ── */
.feat-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 8pt 0;
}}
.feat-table tr {{ border-bottom: 0.5pt solid #ebebeb; }}
.feat-table tr:first-child {{ border-top: 0.5pt solid #ebebeb; }}
.feat-table td {{ padding: 8pt 10pt; vertical-align: middle; font-size: 9.5pt; }}
.feat-table .num {{ width:26pt; font-weight:700; color:#b8880e; font-size:8.5pt; text-align:center; }}
.feat-table .name {{ width:108pt; font-weight:600; color:#1a1a1a; }}
.feat-table .desc {{ color:#444; }}

/* ── Highlight box ── */
.hl-box {{
    background: #f8f2e0;
    border: 1.5pt solid #c8960c;
    border-radius: 2pt;
    padding: 12pt 14pt;
    margin: 12pt 0;
}}
.hl-box .lbl {{
    font-size: 8pt;
    font-weight: 700;
    color: #9a6e00;
    text-transform: uppercase;
    letter-spacing: 0.8pt;
    margin-bottom: 8pt;
}}

/* ── Required section ── */
.req-box {{
    background: #fffdf3;
    border: 2pt solid #c8960c;
    border-left: 6pt solid #c8960c;
    padding: 13pt 15pt;
    margin: 10pt 0;
    font-size: 9.5pt;
    line-height: 1.7;
}}

/* ── Bullet lists ── */
ul.blist {{ margin: 6pt 0 6pt 16pt; padding:0; }}
ul.blist li {{ margin-bottom: 4pt; line-height:1.55; }}
ul.sub {{ margin: 3pt 0 3pt 20pt; list-style-type: circle; }}
ul.sub li {{ margin-bottom: 2pt; font-size:9pt; color:#444; }}

/* ── Tech note ── */
.tech-note {{
    font-size: 8pt;
    color: #666;
    padding: 6pt 10pt;
    border-top: 0.5pt solid #e5e5e5;
    margin-top: 10pt;
}}

/* ── Template structure table ── */
.struct-table {{ width:100%; border-collapse:collapse; margin:8pt 0; }}
.struct-table tr {{ border-bottom:0.5pt solid #ebebeb; }}
.struct-table tr:first-child {{ border-top:0.5pt solid #ebebeb; }}
.struct-table td {{ padding:7pt 10pt; vertical-align:middle; font-size:9.5pt; }}
.struct-table .num {{ width:24pt; font-weight:700; color:#b8880e; font-size:8.5pt; text-align:center; }}
.struct-table .name {{ width:90pt; font-weight:600; }}
.struct-table .desc {{ color:#444; font-size:9pt; }}

/* ── Color swatches ── */
.swatch-row {{ display:flex; align-items:center; gap:10pt; margin:5pt 0; }}
.swatch {{ width:20pt; height:20pt; border-radius:2pt; border:0.5pt solid #ccc; flex-shrink:0; }}

/* ── QR section ── */
.qr-wrap {{
    display: flex;
    align-items: flex-start;
    gap: 18pt;
    background: #f8f2e0;
    border: 1.5pt solid #c8960c;
    border-radius: 2pt;
    padding: 14pt 16pt;
    margin: 14pt 0;
}}
.qr-wrap img {{ width:88pt; height:88pt; flex-shrink:0; }}
.qr-text {{ font-size:9.5pt; line-height:1.65; }}
.qr-url {{ font-size:7.5pt; color:#888; margin-top:7pt; font-style:italic; word-break:break-all; }}

/* ── Steps table ── */
.steps-table {{ width:100%; border-collapse:collapse; margin:10pt 0; }}
.steps-table tr {{ border-bottom:0.5pt solid #ebebeb; }}
.steps-table tr:first-child {{ border-top:0.5pt solid #ebebeb; }}
.steps-table td {{ padding:8pt 10pt; vertical-align:middle; font-size:9.5pt; }}
.steps-table .snum {{ width:44pt; font-weight:700; color:#b8880e; font-size:8.5pt; }}
.steps-table .stitle {{ width:132pt; font-weight:600; color:#1a1a1a; }}
.steps-table .sdesc {{ color:#555; font-size:9pt; font-style:italic; }}

/* ── Disclaimer ── */
.disclaimer {{
    background: #f8f2e0;
    border: 1pt solid #c8960c;
    padding: 12pt 14pt;
    font-size: 9pt;
    line-height: 1.65;
    margin-top: 16pt;
}}
.disclaimer .lbl {{
    font-size: 8pt;
    font-weight: 700;
    color: #b8880e;
    text-transform: uppercase;
    letter-spacing: 0.8pt;
    margin-bottom: 6pt;
}}

/* ── Final note ── */
.final-note {{
    background: #f1f5f9;
    border: 1.5pt solid #9daec0;
    border-left: 5pt solid #6b82a0;
    padding: 13pt 15pt;
    margin-top: 18pt;
    font-size: 9.5pt;
    line-height: 1.7;
}}
.final-note .lbl {{
    font-size: 7.5pt;
    font-weight: 700;
    color: #4f6478;
    text-transform: uppercase;
    letter-spacing: 0.8pt;
    margin-bottom: 8pt;
}}

/* ── Utilities ── */
.page-break {{ page-break-before: always; }}
p {{ margin-bottom: 7pt; }}
.note {{ font-size:8pt; color:#777; font-style:italic; margin-top:7pt; }}
</style>
</head>
<body>

<!-- ═══════════════════ COVER ═══════════════════ -->
<div class="cover">
<div class="cover-wrap">
    <img class="cover-logo" src="data:image/jpeg;base64,{LOGO_B64}" alt="Λογότυπο">
    <div class="cover-title">Πρόταση Νέου Ιστοτόπου</div>
    <div class="cover-org">Ευξείνου Λέσχης Ποντίων Κέρκυρας</div>
    <div class="cover-sub">Πρόταση Σχεδιασμού &amp; Ανάπτυξης Ιστοτόπου</div>
    <div class="cover-rule"></div>

    <table class="meta-table">
        <tr><td class="lbl">Έκδοση</td>      <td class="val">v1.0 — Αρχική Πρόταση</td></tr>
        <tr><td class="lbl">Ημερομηνία</td>  <td class="val">7 Μαΐου 2026</td></tr>
        <tr><td class="lbl">Κατάσταση</td>   <td class="val">Προς Έγκριση</td></tr>
        <tr><td class="lbl">Προς</td>         <td class="val">κυρία Νόπη Κοτίδου — Αντιπρόεδρος</td></tr>
        <tr><td class="lbl">Υπόψιν</td>      <td class="val">κυρία Στέλλα Σοϊλεμετζίδου — Πρόεδρος</td></tr>
        <tr><td class="lbl">Από</td>           <td class="val">Ανάπτυξη Ιστοτόπου</td></tr>
    </table>

    <div class="intro-box" style="text-align:left;">
        <div class="lbl">Εισαγωγικό Κείμενο</div>
        <p><strong>Αξιότιμη κυρία Αντιπρόεδρε,</strong></p>
        <p>Σας αποστέλλω το παρόν έγγραφο στο πλαίσιο ανάπτυξης του νέου ιστοτόπου της Ευξείνου Λέσχης Ποντίων Κέρκυρας και περιλαμβάνει την προτεινόμενη δομή του site, τις αναβαθμίσεις του υφιστάμενου blog καθώς και τα στοιχεία που απαιτούνται για την ολοκλήρωσή του.</p>
    </div>
</div>
</div>

<!-- ═══════════════════ SECTION 1 ═══════════════════ -->
<div class="page-break"></div>

<div class="section-label">Ενότητα 1</div>
<div class="section-title">Σκοπός &amp; Αντικείμενο</div>

<p>Αντικείμενο της παρούσας πρότασης είναι η δημιουργία νέου, σύγχρονου ιστοτόπου για την Ευξείνου Λέσχης Ποντίων Κέρκυρας, που θα αντικαταστήσει ή θα συμπληρώσει την υπάρχουσα διαδικτυακή παρουσία (blog).</p>

<p>Ο νέος ιστότοπος θα παρουσιάζει τον Σύλλογο, την ιστορία του Πόντου, τα χορευτικά τμήματα και θα λειτουργεί ως βασικό σημείο επικοινωνίας.</p>

<div class="sub-title">Στόχοι</div>
<ul class="blist">
    <li>Σύγχρονη εμφάνιση που αντιπροσωπεύει τον Σύλλογο</li>
    <li>Ανάδειξη ποντιακής παράδοσης και ιστορίας</li>
    <li>Ενημέρωση για τμήματα και εκδηλώσεις</li>
    <li>Εύκολη πρόσβαση από κινητό τηλέφωνο (smartphone)</li>
    <li>Δυνατότητα επικοινωνίας μέσω φόρμας</li>
</ul>

<!-- ═══════════════════ SECTION 2 ═══════════════════ -->
<div class="section-label" style="margin-top:20pt;">Ενότητα 2</div>
<div class="section-title">Δυνατότητες &amp; Αναβαθμίσεις Ιστοτόπου</div>

<table class="feat-table">
    <tr>
        <td class="num">01</td>
        <td class="name">Responsive Design</td>
        <td class="desc">Λειτουργεί τέλεια σε υπολογιστή, tablet και κινητό.</td>
    </tr>
    <tr>
        <td class="num">02</td>
        <td class="name">Ο Σύλλογός μας</td>
        <td class="desc">Ιστορικό, αποστολή, αξίες. Κείμενο και εικόνα.</td>
    </tr>
    <tr>
        <td class="num">03</td>
        <td class="name">Ο Πόντος</td>
        <td class="desc">Ιστορία Πόντου, 19 Μαΐου — Ημέρα Μνήμης, χοροί.</td>
    </tr>
    <tr>
        <td class="num">04</td>
        <td class="name">Τμήματα</td>
        <td class="desc">Χορός αρχαρίων &amp; προχωρημένων, χορωδία, ταούλ — με ωράριο.</td>
    </tr>
    <tr>
        <td class="num">05</td>
        <td class="name">Gallery Φωτογραφιών</td>
        <td class="desc">Φωτογραφίες από εκδηλώσεις και παραστάσεις.</td>
    </tr>
    <tr>
        <td class="num">06</td>
        <td class="name">Πολυμέσα</td>
        <td class="desc">Βίντεο και οπτικοακουστικό υλικό από δραστηριότητες του Συλλόγου.</td>
    </tr>
    <tr>
        <td class="num">07</td>
        <td class="name">Φόρμα Επικοινωνίας</td>
        <td class="desc">Αποστολή μηνύματος απευθείας στο email.</td>
    </tr>
    <tr>
        <td class="num">08</td>
        <td class="name">Σύνδεση Social Media</td>
        <td class="desc">Facebook, Instagram, Blog.</td>
    </tr>
    <tr>
        <td class="num">09</td>
        <td class="name">Κωδικός QR</td>
        <td class="desc">Για γρήγορη πρόσβαση από κινητό — χρήσιμο σε αφίσες και έντυπο υλικό.</td>
    </tr>
    <tr>
        <td class="num">10</td>
        <td class="name">Animated Στοιχεία</td>
        <td class="desc">Ομαλές κινούμενες μεταβάσεις και εφέ για σύγχρονη αίσθηση πλοήγησης.</td>
    </tr>
    <tr>
        <td class="num">11</td>
        <td class="name">Εκτυπωμένο QR Πρόσβασης</td>
        <td class="desc">Έτοιμο QR code για εκτύπωση και χρήση σε αφίσες, φυλλάδια και πρόσκλησεις.</td>
    </tr>
</table>

<div class="hl-box">
    <div class="lbl">Πολύγλωσση Υποστήριξη</div>
    <p>Ο ιστότοπος θα υποστηρίζει πολλαπλές γλώσσες, παρέχοντας πρόσβαση στο ευρύτερο κοινό:</p>
    <ul class="blist" style="margin-top:6pt;">
        <li><strong>Ελληνικά</strong> — Κύρια γλώσσα του ιστοτόπου</li>
        <li><strong>Αγγλικά</strong> — Για διεθνείς επισκέπτες και ομογενείς</li>
        <li><strong>Δυνατότητα προσθήκης επιπλέον γλωσσών</strong> στο μέλλον, ανάλογα με τις ανάγκες του Συλλόγου</li>
    </ul>
</div>

<div class="tech-note">
    <strong>Τεχνολογία:</strong> HTML5 / CSS3 / JavaScript. Χωρίς CMS. Hosting: Επαγγελματική υπηρεσία φιλοξενίας ιστοτόπων.
</div>

<!-- ═══════════════════ SECTION 3 — REQUIRED ═══════════════════ -->
<div class="page-break"></div>

<div class="section-label">Ενότητα 3</div>
<div class="section-title">Στοιχεία που Απαιτούνται για την Ολοκλήρωση</div>

<div class="req-box">
    <p>Για την κατασκευή του προτεινόμενου ιστοτόπου έχουν ληφθεί ορισμένα στοιχεία από το ήδη υπάρχον Blogspot, τα οποία χρήζουν ενημέρωσης και εμπλουτισμού.</p>
    <p style="margin-top:8pt;"><strong>Ιδιαίτερα σημαντικά στοιχεία που απαιτούνται:</strong></p>
</div>

<div class="sub-title">Ενεργά Τμήματα της Λέσχης</div>
<ul class="blist">
    <li><strong>Τμήμα Χορού Αρχαρίων</strong> — Δευτέρα &amp; Τετάρτη, 19:00–20:00</li>
    <li><strong>Τμήμα Χορού Προχωρημένων</strong> — Δευτέρα &amp; Τετάρτη, 20:00–21:00</li>
    <li><strong>Τμήμα Χορωδίας</strong> — Τετάρτη, 18:00–19:00</li>
    <li><strong>Τμήμα Ταούλ</strong> — Παρασκευή, 19:00–20:00</li>
</ul>

<div class="sub-title">Εκδηλώσεις</div>
<ul class="blist">
    <li>Εκδηλώσεις προηγούμενων ετών</li>
    <li>Εκδηλώσεις που προγραμματίζονται για το τρέχον έτος</li>
</ul>

<div class="sub-title">Ιστορικό της Λέσχης</div>
<p>Επίσημο ιστορικό κείμενο του Συλλόγου — ιδρυτές, σκοπός, εξέλιξη (2–3 παράγραφοι).</p>

<div class="sub-title">Σήμα Ευξείνου Λέσχης Ποντίων</div>
<p>Ανάλυση και επεξήγηση του σήματος της Ευξείνου Λέσχης Ποντίων.</p>

<div class="hl-box" style="margin-top:16pt;">
    <div class="lbl">Διευκρίνιση σχετικά με τα Κείμενα</div>
    <p>Τα τελικά κείμενα του ιστοτόπου θα αντικατασταθούν και θα διαμορφωθούν βάσει του υλικού που θα αποσταλεί από την Ευξείνου Λέσχης Ποντίων Κέρκυρας.</p>
    <p style="margin-top:6pt;">Τα υπάρχοντα κείμενα στο demo είναι <strong>προσωρινά</strong> και χρησιμοποιούνται αποκλειστικά για σκοπούς παρουσίασης της δομής και του σχεδιασμού.</p>
</div>

<!-- ═══════════════════ SECTION 4 — TEMPLATE ═══════════════════ -->
<div class="page-break"></div>

<div class="section-label">Ενότητα 4</div>
<div class="section-title">Προτεινόμενο Template</div>

<div class="hl-box">
    <div class="lbl">Σημαντική Επισήμανση</div>
    <p>Το παρακάτω template είναι <strong>προτεινόμενο</strong> σχέδιο — ΟΧΙ τελικό. Όλα τα κείμενα είναι ενδεικτικά και θα αντικατασταθούν με βάση το υλικό που θα αποστείλει η Λέσχη.</p>
</div>

<p>Ο ιστότοπος είναι <strong>single-page</strong>: όλες οι ενότητες στην ίδια σελίδα, πλοήγηση με scroll ή μέσω μενού.</p>

<div class="sub-title">Δομή Ιστοτόπου</div>
<table class="struct-table">
    <tr><td class="num">01</td><td class="name">Hero</td><td class="desc">Κεντρική εικόνα, τίτλος, κουμπιά πλοήγησης</td></tr>
    <tr><td class="num">02</td><td class="name">Στατιστικά</td><td class="desc">Έτος ίδρυσης, μέλη, χρόνια, τμήματα</td></tr>
    <tr><td class="num">03</td><td class="name">Ο Σύλλογος</td><td class="desc">Ιστορικό, αποστολή, πυλώνες δράσης</td></tr>
    <tr><td class="num">04</td><td class="name">Ο Πόντος</td><td class="desc">Ιστορία, 19 Μαΐου — Ημέρα Μνήμης, χοροί</td></tr>
    <tr><td class="num">05</td><td class="name">Τμήματα</td><td class="desc">Χορός αρχαρίων, Χορός προχωρημένων, Χορωδία, Ταούλ</td></tr>
    <tr><td class="num">06</td><td class="name">Gallery</td><td class="desc">Φωτογραφίες και βίντεο εκδηλώσεων</td></tr>
    <tr><td class="num">07</td><td class="name">Επικοινωνία</td><td class="desc">Φόρμα, τηλέφωνο, κοινωνικά δίκτυα</td></tr>
</table>

<div class="sub-title">Χρωματικό Σχήμα</div>
<div class="swatch-row">
    <div class="swatch" style="background:#0a0a0a;"></div>
    <span>Κύριο Φόντο: <strong>#0a0a0a</strong> (σκούρο μαύρο)</span>
</div>
<div class="swatch-row">
    <div class="swatch" style="background:#D4AF37;"></div>
    <span>Accent: <strong>#D4AF37</strong> (χρυσό)</span>
</div>
<p class="note" style="margin-top:5pt;">Γραμματοσειρές: <strong>Playfair Display</strong> (τίτλοι) &nbsp;/&nbsp; <strong>Inter</strong> (κείμενο)</p>

<!-- QR -->
<div class="sub-title" style="margin-top:20pt;">Πρόσβαση στο Demo Ιστοτόπου</div>

<div class="qr-wrap">
    <img src="data:image/png;base64,{QR_B64}" alt="QR Code — Demo Ιστοτόπου">
    <div class="qr-text">
        <p>Μπορείτε να επισκεφθείτε το πρότυπο του ιστοτόπου μέσω του QR code και να αποστείλετε τυχόν παρατηρήσεις ή προτάσεις σχετικά με:</p>
        <ul class="blist" style="margin-top:7pt;">
            <li>το <strong>design</strong></li>
            <li>τη <strong>δομή</strong></li>
            <li>την <strong>εμφάνιση</strong></li>
            <li>και τη γενική <strong>αισθητική</strong> του site</li>
        </ul>
        <div class="qr-url">{DEMO_URL}</div>
    </div>
</div>

<!-- ═══════════════════ SECTION 5 ═══════════════════ -->
<div class="page-break"></div>

<div class="section-label">Ενότητα 5</div>
<div class="section-title">Σύνοψη &amp; Επόμενα Βήματα</div>

<p>Μετά την έγκριση και την αποστολή των απαιτούμενων στοιχείων, ακολουθεί το χρονοδιάγραμμα:</p>

<table class="steps-table">
    <tr>
        <td class="snum">Βήμα 1</td>
        <td class="stitle">Αποστολή στοιχείων</td>
        <td class="sdesc">Λέσχη — κείμενα, φωτογραφίες, πληροφορίες τμημάτων</td>
    </tr>
    <tr>
        <td class="snum">Βήμα 2</td>
        <td class="stitle">Ενημέρωση site με τελικά κείμενα &amp; εικόνες</td>
        <td class="sdesc">Αντικατάσταση προσωρινού περιεχομένου</td>
    </tr>
    <tr>
        <td class="snum">Βήμα 3</td>
        <td class="stitle">Έλεγχος &amp; παρατηρήσεις από Δ.Σ.</td>
        <td class="sdesc">Εξέταση, προτάσεις αλλαγών</td>
    </tr>
    <tr>
        <td class="snum">Βήμα 4</td>
        <td class="stitle">Ρύθμιση hosting &amp; domain</td>
        <td class="sdesc">Επαγγελματική υπηρεσία φιλοξενίας</td>
    </tr>
    <tr>
        <td class="snum">Βήμα 5</td>
        <td class="stitle">Ρύθμιση φόρμας επικοινωνίας</td>
        <td class="sdesc">Δοκιμή αποστολής μηνύματος</td>
    </tr>
    <tr>
        <td class="snum">Βήμα 6</td>
        <td class="stitle">Τελικός έλεγχος (mobile / tablet / desktop)</td>
        <td class="sdesc">Σε όλες τις συσκευές</td>
    </tr>
    <tr>
        <td class="snum">Βήμα 7</td>
        <td class="stitle">Go live — Δημοσίευση</td>
        <td class="sdesc">Ανακοίνωση στα κοινωνικά δίκτυα</td>
    </tr>
</table>

<div class="disclaimer">
    <div class="lbl">Σημείωση 1</div>
    <p>Το παρόν έγγραφο αποτελεί αρχική πρόταση. Το template χρησιμοποιεί ενδεικτικά κείμενα που θα αντικατασταθούν με βάση τα επίσημα κείμενα και το υλικό που θα αποστείλει η Λέσχη. Κάθε παρατήρηση από τα μέλη του Δ.Σ. είναι ευπρόσδεκτη.</p>
</div>

<div class="final-note">
    <div class="lbl">Σημείωση 2</div>
    <p>Οτιδήποτε υλοποιείται μέχρι στιγμής για την παρούσα εργασία δεν βασίζεται σε τεχνητή νοημοσύνη (AI), καθώς χρησιμοποιούνται τεχνολογίες HTML και CSS για την κατασκευή του ιστοτόπου, στις οποίες υπάρχει σχετική εμπειρία από προηγούμενη ενασχόληση με παρόμοια έργα.</p>
</div>

</body>
</html>"""

# ── Generate PDF ──────────────────────────────────────────────────────────────
print("Generating PDF…")
weasyprint.HTML(string=HTML, base_url=PROJECT_DIR).write_pdf(OUTPUT_PDF)
print(f"Done → {OUTPUT_PDF}")
