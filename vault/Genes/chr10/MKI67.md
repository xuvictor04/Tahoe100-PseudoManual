---
symbol: "MKI67"
type: "gene"
col: 7313
ensembl_id: "ENSG00000148773"
name: "marker of proliferation Ki-67"
location: "10q26.2"
module: 22
arm: "+"
pooled_cpm: 320.64
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 20
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# MKI67

*marker of proliferation Ki-67* — 10q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.88× (z +7.3, q 1e-10, up in 33 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.40× (z +3.9, q 0.005, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (13 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.475× (z -11.5, q 6e-28, down in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~78% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.618× (z -5.6, q 2e-06, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KNL1]] (+0.95, fdr 7e-06), [[KIF11]] (+0.94, fdr 7e-06), [[NCAPG]] (+0.94, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7313.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.88×** | +7.3 | 1e-10 | 33/49 (SW1417, J82, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.57×** | +7.0 | 7e-10 | 44/48 (NCI-H23, NCI-H1573, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.78×** | +6.7 | 3e-09 | 39/48 (HT-29, PANC-1, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | **1.82×** | +6.7 | 3e-09 | 34/44 (SW1417, J82, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.51×** | +6.3 | 3e-08 | 31/48 (NCI-H2030, PANC-1, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.73×** | +6.1 | 9e-08 | 38/48 (PANC-1, C32, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.53×** | +4.9 | 6e-05 | 34/48 (KATO III, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.45×** | +4.3 | 0.001 | 29/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.0 | 0.004 | 3/50 (RKO, SNU-1, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.40×** | +3.9 | 0.005 | 30/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.009 | 35/48 (NCI-H460, HT-29, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +3.7 | 0.010 | 26/47 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.014 | 32/48 (NCI-H23, HT-29, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.78×** | +3.5 | 0.017 | 25/47 (J82, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.35×** | +3.5 | 0.017 | 26/48 (RKO, KATO III, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.38×** | +3.5 | 0.019 | 25/48 (SW 900, NCI-H1792, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.022 | 25/48 (HT-29, NCI-H2030, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.042 | 22/47 (HOP62, H4, …) | all doses, flat |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.042 | 22/49 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.047 | 20/48 (H4, NCI-H460, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.29×** | +2.8 | 0.091 | 23/47 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Terfenadine (drug)]] 0.5 µM |  | **1.27×** | +2.8 | 0.091 | 18/48 (Hs 766T, NCI-H661, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.27×** | +2.8 | 0.098 | 20/49 (HT-29, HOP62, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7313.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.475×** | -11.5 | 6e-28 | 46/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.424×** | -10.0 | 3e-21 | 48/48 (H4, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.404×** | -8.3 | 2e-14 | 41/48 (SW48, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.290×** | -7.6 | 5e-12 | 41/45 (RKO, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.549×** | -7.0 | 3e-10 | 40/48 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.618×** | -5.6 | 2e-06 | 33/48 (COLO 205, NCI-H2030, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.621×** | -5.6 | 2e-06 | 42/49 (A549, Hs 766T, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.529×** | -5.3 | 7e-06 | 37/48 (HT-29, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.636×** | -5.1 | 2e-05 | 36/48 (NCI-H1573, H4, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.751×** | -4.5 | 3e-04 | 33/48 (HCT15, RKO, …) | rises with dose |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.716×** | -3.9 | 0.005 | 30/48 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.711×** | -3.8 | 0.006 | 26/47 (H4, A549, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.724×** | -3.8 | 0.007 | 30/48 (H4, CFPAC-1, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **0.789×** | -3.7 | 0.010 | 29/48 (HT-29, COLO 205, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.654×** | -3.5 | 0.015 | 33/49 (SHP-77, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.584×** | -3.3 | 0.032 | 28/48 (NCI-H1573, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.763×** | -3.2 | 0.045 | 25/48 (NCI-H1573, SW48, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.758×** | -3.0 | 0.075 | 24/48 (NCI-H1573, AN3 CA, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +1.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7313. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 407 | 0 | 11 (8 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0989× (z -14.0) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.219× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 260 | 1 (1 ⚠) | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.187× (z -15.7) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.310× (z -11.6) |
| [[SW48 (line)]] | wt | 443 | 0 | 9 (5 ⚠) | — | [[Amsacrine (drug)]] 5 µM 0.328× (z -11.9) |
| [[A549 (line)]] | wt | 316 | 1 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +14.6) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.329× (z -12.0) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.273× (z -10.7) |
| [[C32 (line)]] | wt | 225 | 4 (4 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +11.6) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.312× (z -11.0) ⚠ cell-cycle shift, explains ~78% of this change |
| [[A-172 (line)]] | wt | 240 | 0 | 6 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.217× (z -16.1) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 0.5 µM 0.304× (z -9.6) |
| [[A498 (line)]] | wt | 295 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.123× (z -22.3) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.359× (z -11.4) |
| [[HT-29 (line)]] | alt | 388 | 1 (1 ⚠) | 3 (3 ⚠) | [[Docetaxel (drug)]] 0.05 µM 3.10× (z +8.5) ⚠ transcription drop; cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.320× (z -11.3) ⚠ cell-cycle shift, explains ~78% of this change |
| [[LoVo (line)]] | wt | 302 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.260× (z -13.9) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.469× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 374 | 0 | 4 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.137× (z -13.9) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.233× (z -10.2) |
| [[PANC-1 (line)]] | alt | 382 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +17.6) ⚠ cell-cycle shift, would explain all of this change | [[Bortezomib (drug)]] 0.05 µM 0.294× (z -9.0) ⚠ cell-cycle shift, explains ~56% of this change |
| [[RKO (line)]] | wt | 377 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 0.5 µM 0.300× (z -11.0) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.386× (z -8.7) |
| [[SNU-1 (line)]] | wt | 364 | 0 | 4 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.159× (z -13.6) ⚠ cell-cycle shift, explains ~78% of this change |
| [[A-427 (line)]] | wt | 531 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.185× (z -17.7) ⚠ cell-cycle shift, explains ~78% of this change |
| [[J82 (line)]] | alt | 416 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 268 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.229× (z -15.7) ⚠ cell-cycle shift, explains ~78% of this change |
| [[Panc 03.27 (line)]] | alt | 386 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +13.5) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.431× (z -9.3) ⚠ cell-cycle shift, explains ~78% of this change |
| [[SW1417 (line)]] | alt | 397 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | — |
| [[HOP62 (line)]] | alt | 270 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.445× (z -8.5) ⚠ cell-cycle shift, explains ~78% of this change |
| [[HS-578T (line)]] | alt | 156 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +12.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[hTERT-HPNE (line)]] | wt | 150 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.255× (z -10.5) ⚠ cell-cycle shift, explains ~78% of this change |
| [[KATO III (line)]] | alt | 348 | 0 | 2 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.262× (z -10.2) ⚠ cell-cycle shift, explains ~54% of this change |
| [[LS 180 (line)]] | wt | 127 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.177× (z -14.2) ⚠ cell-cycle shift, explains ~78% of this change |
| [[NCI-H2030 (line)]] | alt | 278 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +18.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 280 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +14.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[COLO 205 (line)]] | alt | 163 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 597 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.301× (z -9.6) ⚠ cell-cycle shift, explains ~78% of this change |
| [[HEC-1-A (line)]] | alt | 617 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.358× (z -8.6) ⚠ cell-cycle shift, explains ~54% of this change |
| [[MIA PaCa-2 (line)]] | alt | 361 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -17.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 403 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.404× (z -10.8) ⚠ cell-cycle shift, explains ~78% of this change |
| [[SHP-77 (line)]] | alt | 375 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.387× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 319 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.410× (z -10.1) ⚠ cell-cycle shift, explains ~78% of this change |
| [[SNU-423 (line)]] | alt | 328 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 500 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 358 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 209 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 84.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 258 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 439 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 354 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 464 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7313), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KNL1]] | +0.95 | +0.94 / +0.95 | both halves | 7e-06 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 562 |
| [[KIF11]] | +0.94 | +0.92 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 931 |
| [[NCAPG]] | +0.94 | +0.94 / +0.93 | both halves | 7e-06 | STRING 908 |
| [[TPX2]] | +0.94 | +0.92 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 954 |
| [[KIF23]] | +0.94 | +0.94 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 880 |
| [[NDC80]] | +0.93 | +0.92 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 796 |
| [[KIF4A]] | +0.93 | +0.94 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 871 |
| [[BIRC5]] | +0.93 | +0.93 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 939 |
| [[ARHGAP11A]] | +0.92 | +0.93 / +0.90 | both halves | 7e-06 | STRING 812 |
| [[SGO1]] | +0.92 | +0.91 / +0.91 | both halves | 7e-06 | STRING 610 |
| [[DLGAP5]] | +0.92 | +0.90 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 902 |
| [[CENPF]] | +0.92 | +0.90 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 979 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises MKI67's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.04× lower at baseline in the lines without PIMREG | 0.059 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[HYLS1]] | B | HYLS1 activity raises MKI67's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 1.80× lower at baseline in the lines without HYLS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises MKI67's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.29× lower at baseline in the lines without NDC80 | 0.035 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[SKA3]] | C | SKA3 activity raises MKI67's level | lines that do not express SKA3 (3) vs lines expressing it (47) | 3.41× lower at baseline in the lines without SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p |
| [[SAPCD2]] | C | SAPCD2 activity raises MKI67's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.79× lower at baseline in the lines without SAPCD2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |
| [[CDC20]] | C | CDC20 activity raises MKI67's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.77× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises MKI67's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.73× lower at baseline in the lines without CDCA3, SPDL1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[AURKB]] | C | AURKB activity raises MKI67's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.36× lower at baseline in the lines without AURKB | 0.095 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.959). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.8, -55.4); signed map (-49.2, -43.7). **Vector** length 176, 75.4% of its response variance represented; |z| ≥ 3 in 1,640 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.85 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.74 to 48); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.75 to 41).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +8.1 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.7 | +6.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.9 | +6.1 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +6.9 | +7.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | +5.6 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +1.3 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.9 | +3.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.9 | +3.9 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +3.4 | +3.5 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +3.2 | +3.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | -11.0 | -11.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | -10.2 | -10.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | -10.0 | -8.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -8.4 | -7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.1 | -5.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -5.5 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.4 | -3.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.7 | -1.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.7 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | marker of proliferation Ki-67 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.2 — chr10:128,096,659-128,126,423 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MIB-1, PPP1R105, Ki-67 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [P46013](https://www.uniprot.org/uniprotkb/P46013) (Proliferation marker protein Ki-67):

> Protein that associates with the surface of mitotic chromosomes and acts both as a chromosome repellent during early mitosis and chromosome attractant during late mitosis. Required to maintain individual mitotic chromosomes dispersed in the cytoplasm following nuclear envelope disassembly. During early mitosis, relocalizes from nucleoli to the chromosome surface where it forms extended brush structures that cover a substantial fraction of the chromosome surface. The MKI67 brush structure …

**Summary**, from NCBI Gene [4288](https://www.ncbi.nlm.nih.gov/gene/4288):

> Enables RNA binding activity and molecular condensate scaffold activity. Involved in chromosome segregation and regulation of mitotic nuclear division. Located in chromosome; nucleolus; and nucleoplasm. Is active in condensed chromosome. Implicated in several diseases, including Crohn's disease; colorectal cancer; endocrine gland cancer (multiple); graft-versus-host disease; and human immunodeficiency virus infectious disease. Biomarker of several diseases, including Barrett's esophagus; …

**Accessions** — [HGNC:7107](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7107) · Entrez [4288](https://www.ncbi.nlm.nih.gov/gene/4288) · UniProt [P46013](https://www.uniprot.org/uniprotkb/P46013) · Ensembl [ENSG00000148773](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148773)

## Data

Gene col 7313: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7313); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7313, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7313]; `tensor/DDL_lfc|DDL_z.npy` [7313]; `embed/gene_vectors.npy` [7313]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7313 or target_col == 7313). Every well: [[MKI67 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MKI67.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
