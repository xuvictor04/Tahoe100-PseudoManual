---
symbol: "HDGF"
type: "gene"
col: 6713
ensembl_id: "ENSG00000143321"
name: "heparin binding growth factor"
location: "1q23.1"
module: 184
arm: "-"
pooled_cpm: 162.4
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/184"]
generated_by: "tahoemap"
---

# HDGF

*heparin binding growth factor* — 1q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.32× (z +16.0, q 0e+00, up in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 1.37× (z +3.4, q 0.045, up in 26 of 50 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 13 lines (LoVo 8.24×, KATO III 6.99×, SW480 5.66×, Panc 03.27 5.66×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 4.23×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 7.77×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.324× (z -12.8, q 9e-35, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALNT7-DT]] (+0.65, fdr 1e-04), [[STAT5A]] (+0.64, fdr 4e-05), [[JADE2]] (+0.63, fdr 1e-05); moves opposite to [[ABTB3]] (-0.61, fdr 3e-05), [[ARID3B]] (-0.59, fdr 7e-05), [[GIPR]] (-0.59, fdr 6e-05).
> It sits in the **-** arm of [[Module 184]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6713.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 13 lines (LoVo 8.24×, KATO III 6.99×, SW480 5.66×, Panc 03.27 5.66×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 4.23×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 7.77×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.32×** | +16.0 | 0e+00 | 43/44 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.57×** | +11.2 | 2e-26 | 49/49 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.82×** | +10.9 | 3e-25 | 44/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.21×** | +7.2 | 1e-10 | 30/50 (Panc 03.27, HEC-1-A, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **1.72×** | +6.2 | 8e-08 | 46/48 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.68×** | +5.7 | 1e-06 | 39/47 (LoVo, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.58×** | +5.2 | 2e-05 | 38/48 (KATO III, NCI-H460, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.045 | 26/50 (MIA PaCa-2, A-172, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.085 | 29/48 (C32, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +3.2 | 0.085 | 27/48 (HOP62, SNU-423, …) | rises with dose | composition shift; position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.22×** | +3.1 | 0.085 | 28/48 (HOP62, NCI-H2030, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.31×** | +3.1 | 0.089 | 24/48 (A549, SNU-423, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.30× | +3.0 | 0.11 | 28/48 (KATO III, SNU-423, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6713.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.324×** | -12.8 | 9e-35 | 48/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.374×** | -11.2 | 2e-26 | 47/48 (SW 900, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.448×** | -9.1 | 1e-17 | 47/48 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.658×** | -6.7 | 3e-09 | 45/48 (SW1417, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.558×** | -6.6 | 4e-09 | 45/48 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.438×** | -4.9 | 9e-05 | 42/49 (NCI-H2030, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.703×** | -4.0 | 0.005 | 32/49 (CHP-212, SW 900, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.745×** | -3.3 | 0.059 | 30/49 (SW 900, RKO, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.753×** | -3.2 | 0.084 | 26/48 (HepG2/C3A, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.587×** | -3.2 | 0.089 | 30/49 (LoVo, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6713. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 208 | 5 (5 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 5.07× (z +13.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -12.1) |
| [[SW480 (line)]] | alt | 136 | 3 (3 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.66× (z +16.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.256× (z -13.4) |
| [[LoVo (line)]] | wt | 122 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 8.24× (z +17.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -11.4) |
| [[HOP62 (line)]] | alt | 89.3 | 5 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.76× (z +15.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.348× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 311 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.27× (z +12.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.413× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 259 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.23× (z +12.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.243× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 170 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 5.19× (z +14.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.234× (z -13.5) |
| [[SW 900 (line)]] | alt | 260 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +9.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.192× (z -16.0) |
| [[AsPC-1 (line)]] | alt | 155 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +17.4) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -15.5) |
| [[C-33 A (line)]] | alt | 109 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 5.86× (z +13.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.230× (z -11.2) |
| [[J82 (line)]] | alt | 155 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.40× (z +13.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.332× (z -10.7) |
| [[KATO III (line)]] | alt | 117 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 6.99× (z +17.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.367× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 155 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.42× (z +12.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 151 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.29× (z +10.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.189× (z -15.7) |
| [[Panc 03.27 (line)]] | alt | 172 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.66× (z +16.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -12.5) |
| [[PANC-1 (line)]] | alt | 97.3 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.50× (z +14.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.345× (z -9.2) |
| [[SW1417 (line)]] | alt | 161 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +10.8) ⚠ toxic; transcription drop | [[Tucidinostat (drug)]] 5 µM 0.480× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 171 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +12.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -11.7) |
| [[HepG2_C3A (line)]] | wt | 124 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | [[Belinostat (drug)]] 5 µM 0.310× (z -9.6) |
| [[LS 180 (line)]] | wt | 156 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.52× (z +15.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.340× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 192 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.81× (z +12.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -11.0) |
| [[SK-MEL-2 (line)]] | alt | 109 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -12.5) |
| [[SW48 (line)]] | wt | 160 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +9.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -11.2) |
| [[A-427 (line)]] | wt | 252 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.37× (z +12.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.279× (z -10.9) |
| [[C32 (line)]] | wt | 136 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.31× (z +13.6) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 140 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.27× (z +9.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.219× (z -10.1) |
| [[HT-29 (line)]] | alt | 154 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.92× (z +13.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 118 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.62× (z +14.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 158 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +10.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.405× (z -8.7) |
| [[A-172 (line)]] | wt | 119 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.30× (z +10.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 217 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -12.4) |
| [[CHP-212 (line)]] | wt | 176 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.03× (z +9.8) ⚠ toxic; transcription drop | [[Tucidinostat (drug)]] 0.5 µM 0.191× (z -10.3) |
| [[Hs 766T (line)]] | wt | 175 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.27× (z +11.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 111 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +9.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.282× (z -9.3) |
| [[SNU-1 (line)]] | wt | 215 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.235× (z -12.0) |
| [[SNU-423 (line)]] | alt | 98.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.64× (z +11.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 270 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.36× (z +11.3) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 108 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.01× (z +10.8) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 130 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.283× (z -11.3) |
| [[COLO 205 (line)]] | alt | 101 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -10.3) |
| [[HCT15 (line)]] | alt | 97.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.07× (z +12.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 100 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.10× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 239 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.387× (z -8.8) |
| [[RKO (line)]] | wt | 148 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.373× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 149 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6713), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNT7-DT]] | +0.65 | +0.58 / +0.33 | both halves | 1e-04 |  |
| [[STAT5A]] | +0.64 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[JADE2]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[USP13]] | +0.62 | +0.65 / +0.32 | both halves | 2e-04 |  |
| [[MCCC2]] | +0.62 | +0.63 / +0.39 | both halves | 5e-05 |  |
| [[HNRNPU]] | +0.62 | +0.53 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[IQCH-AS1]] | +0.62 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[HNRNPH3]] | +0.59 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[HMGN2]] | +0.59 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[SAFB]] | +0.58 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[MLLT6]] | +0.58 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[HMGB2]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABTB3]] | -0.61 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[ARID3B]] | -0.59 | -0.55 / -0.38 | both halves | 7e-05 |  |
| [[GIPR]] | -0.59 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[YIF1B]] | -0.59 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[GP6-AS1]] | -0.59 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[LYPD3]] | -0.57 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[PIGH]] | -0.56 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[KIF21B]] | -0.56 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[TMEM92]] | -0.55 | -0.51 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[SH3BGRL3]] | -0.55 | -0.44 / -0.24 | both halves | 5e-04 |  |
| [[GPRIN1]] | -0.55 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[AP2S1]] | -0.54 | -0.45 / -0.22 | both halves | 6e-04 |  |
| [[MYO9B]] | -0.54 | -0.50 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises HDGF's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises HDGF's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 184]]; 20 genes; this gene is in the **-** arm (projection on the module's main direction -0.577). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (14.3, 5.7); signed map (32.1, -24.9). **Vector** length 86.5, 35.5% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.5 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +4.2 | +3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.3 | +3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +0.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.9 | -1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | -0.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.8 | +0.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | -0.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.1 | -12.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.4 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -6.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | heparin binding growth factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.1 — chr1:156,742,109-156,766,925 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HMG1L2 |
| Gene groups (HGNC) | Heparin binding growth factor family |
| Hallmark sets | HEME_METABOLISM, MYC_TARGETS_V1 |
| Reactome | 5 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Unfolded Protein Response (UPR) |
| Matched by | ensembl_id |

**Function**, from UniProt [P51858](https://www.uniprot.org/uniprotkb/P51858) (Hepatoma-derived growth factor):

> [Isoform 1]: Acts as a transcriptional repressor. Has mitogenic activity for fibroblasts. Heparin-binding protein.; [Isoform 2]: Does not have mitogenic activity for fibroblasts. Does not bind heparin.; [Isoform 3]: Has mitogenic activity for fibroblasts. Heparin-binding protein.

**Summary**, from NCBI Gene [3068](https://www.ncbi.nlm.nih.gov/gene/3068):

> This gene encodes a member of the hepatoma-derived growth factor family. The encoded protein has mitogenic and DNA-binding activity and may play a role in cellular proliferation and differentiation. High levels of expression of this gene enhance the growth of many tumors. This gene was thought initially to be located on chromosome X; however, that location has been determined to correspond to a related pseudogene. Alternatively spliced transcript variants encoding distinct isoforms have been …

**Accessions** — [HGNC:4856](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4856) · Entrez [3068](https://www.ncbi.nlm.nih.gov/gene/3068) · UniProt [P51858](https://www.uniprot.org/uniprotkb/P51858) · Ensembl [ENSG00000143321](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143321)

## Data

Gene col 6713: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6713); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6713, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6713]; `tensor/DDL_lfc|DDL_z.npy` [6713]; `embed/gene_vectors.npy` [6713]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6713 or target_col == 6713). Every well: [[HDGF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDGF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
