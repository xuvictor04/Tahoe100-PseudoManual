---
symbol: "LPIN1"
type: "gene"
col: 5547
ensembl_id: "ENSG00000134324"
name: "lipin 1"
location: "2p25.1"
module: 86
arm: "+"
pooled_cpm: 63.67
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 15
n_dd_up_clean: 32
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# LPIN1

*lipin 1* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.52× (z +28.3, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.734× (z -9.9, q 3e-20, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGCS1]] (+0.72, fdr 7e-06), [[HMGCR]] (+0.64, fdr 1e-05), [[FDFT1]] (+0.64, fdr 7e-06); moves opposite to [[NAF1]] (-0.44, fdr 1e-04), [[ZBTB26]] (-0.44, fdr 3e-04), [[DYNLT2]] (-0.41, fdr 2e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 9 with an alert ⚠; shown: the 15 strongest. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5547.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.52×** | +28.3 | 0e+00 | 46/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.25×** | +26.5 | 0e+00 | 46/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.70×** | +22.4 | 0e+00 | 47/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.88×** | +20.0 | 0e+00 | 44/48 (A549, NCI-H23, …) | rises with dose |  |
| [[Berbamine (drug)]] 5 µM |  | **1.71×** | +17.1 | 0e+00 | 43/49 (LoVo, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +16.8 | 0e+00 | 41/48 (AsPC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.66×** | +11.5 | 2e-28 | 38/48 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +9.7 | 2e-20 | 30/48 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.53×** | +9.1 | 4e-18 | 35/47 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +9.1 | 5e-18 | 35/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +8.8 | 9e-17 | 31/48 (HT-29, RKO, …) | rises with dose |  |
| [[Posaconazole (drug)]] 5 µM |  | **1.47×** | +8.3 | 5e-15 | 30/48 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +8.3 | 6e-15 | 29/48 (NCI-H460, HEC-1-A, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +8.1 | 2e-14 | 29/48 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.98×** | +8.0 | 3e-14 | 37/49 (A498, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5547.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.734×** | -9.9 | 3e-20 | 32/48 (CFPAC-1, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.718×** | -7.5 | 2e-11 | 29/48 (SW1417, NCI-H2347, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.742×** | -6.7 | 4e-09 | 31/48 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.773×** | -5.6 | 3e-06 | 25/47 (HepG2/C3A, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.763×** | -5.5 | 3e-06 | 24/45 (KATO III, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.648×** | -5.1 | 3e-05 | 20/47 (SW48, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.817×** | -4.6 | 4e-04 | 20/49 (KATO III, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.690×** | -4.4 | 9e-04 | 20/48 (NCI-H2347, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.707×** | -4.1 | 0.003 | 15/48 (NCI-H23, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.886× | -3.9 | 0.007 | 14/48 (Hs 766T, LS 180, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.725×** | -3.8 | 0.008 | 17/48 (SW 1271, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Asciminib (drug)]] 5 µM |  | 0.850× | -3.7 | 0.011 | 9/48 (KATO III, PANC-1, …) | top dose only |  |
| [[MK-3903 (drug)]] 5 µM |  | **0.739×** | -3.6 | 0.015 | 11/48 (LS 180, SW 1088, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.859× | -3.4 | 0.024 | 15/48 (KATO III, Panc 03.27, …) | top dose only |  |
| [[Riluzole hydrochloride (drug)]] 5 µM |  | 0.902× | -3.3 | 0.037 | 4/49 (NCI-H2122, J82, …) | top dose only | position effect removed |
| [[Megestrol (drug)]] 5 µM |  | 0.906× | -3.2 | 0.055 | 6/49 (A549, NCI-H1792, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.767×** | -3.1 | 0.058 | 15/48 (H4, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[IQ 1 (drug)]] 5 µM |  | **0.770×** | -3.1 | 0.058 | 13/48 (NCI-H460, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.826×** | -3.1 | 0.058 | 9/48 (J82, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 0.872× | -3.1 | 0.058 | 14/48 (NCI-H1573, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5547. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 37.3 | 9 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.28× (z +15.9) | — |
| [[KATO III (line)]] | alt | 239 | 1 | 7 (3 ⚠) | [[Cepharanthine (drug)]] 5 µM 1.87× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -15.6) |
| [[NCI-H23 (line)]] | alt | 84.3 | 6 | 1 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 4.64× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -9.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 50.1 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 3.31× (z +12.9) | — |
| [[A549 (line)]] | wt | 47.2 | 6 | 0 | [[Cepharanthine (drug)]] 5 µM 4.85× (z +18.2) | — |
| [[HS-578T (line)]] | alt | 34.5 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 5.70× (z +13.1) | — |
| [[HT-29 (line)]] | alt | 34.0 | 6 | 0 | [[Cepharanthine (drug)]] 5 µM 3.90× (z +13.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 150 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 3.22× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 75.8 | 6 | 0 | [[Cepharanthine (drug)]] 5 µM 2.68× (z +14.0) | — |
| [[PANC-1 (line)]] | alt | 70.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +14.5) | — |
| [[RKO (line)]] | wt | 130 | 5 | 1 | [[Panobinostat (drug)]] 5 µM 3.70× (z +12.4) | [[Selinexor (drug)]] 5 µM 0.497× (z -9.5) |
| [[A-172 (line)]] | wt | 54.6 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.46× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 101 | 4 | 1 | [[Cepharanthine (drug)]] 5 µM 2.28× (z +9.1) | [[Selinexor (drug)]] 5 µM 0.428× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 64.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +16.6) | — |
| [[LS 180 (line)]] | wt | 104 | 2 | 3 (2 ⚠) | [[Cepharanthine (drug)]] 5 µM 2.51× (z +10.4) | [[Selinexor (drug)]] 5 µM 0.409× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 38.5 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.40× (z +16.5) | — |
| [[SW 900 (line)]] | alt | 40.3 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.91× (z +10.7) | — |
| [[A-427 (line)]] | wt | 39.7 | 4 | 0 | [[Belinostat (drug)]] 5 µM 3.71× (z +12.0) | — |
| [[AsPC-1 (line)]] | alt | 40.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +17.6) | — |
| [[HEC-1-A (line)]] | alt | 59.5 | 4 | 0 | [[Berbamine (drug)]] 5 µM 2.08× (z +10.7) | — |
| [[LoVo (line)]] | wt | 52.4 | 4 | 0 | [[Cepharanthine (drug)]] 5 µM 3.28× (z +16.7) | — |
| [[NCI-H1573 (line)]] | alt | 88.8 | 3 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.27× (z +9.1) | [[Budesonide (drug)]] 0.5 µM 0.326× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 59.5 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.21× (z +11.3) | [[Selinexor (drug)]] 5 µM 0.537× (z -8.7) |
| [[SW1417 (line)]] | alt | 41.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.29× (z +13.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.345× (z -9.6) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 36.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.10× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 34.5 | 3 | 0 | [[Cepharanthine (drug)]] 5 µM 2.74× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 48.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 11.0× (z +14.2) | — |
| [[HepG2_C3A (line)]] | wt | 73.8 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.58× (z +10.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.221× (z -12.5) ⚠ toxic |
| [[J82 (line)]] | alt | 32.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.77× (z +12.1) | — |
| [[RPMI-7951 (line)]] | alt | 57.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.82× (z +10.4) | — |
| [[SK-MEL-2 (line)]] | alt | 38.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.21× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 30.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.50× (z +10.4) | — |
| [[SW480 (line)]] | alt | 31.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.11× (z +13.3) | — |
| [[BT-474 (line)]] | alt | 62.2 | 1 | 1 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 2.27× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 84.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +8.8) | [[Selinexor (drug)]] 5 µM 0.386× (z -12.4) |
| [[hTERT-HPNE (line)]] | wt | 32.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.81× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 45.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.48× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 28.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.50× (z +9.8) | — |
| [[SNU-1 (line)]] | wt | 97.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -14.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 89.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 972 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 2.75× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 27.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.77× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 86.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.420× (z -8.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 92.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5547), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGCS1]] | +0.72 | +0.81 / +0.61 | both halves | 7e-06 | STRING 513 |
| [[HMGCR]] | +0.64 | +0.66 / +0.54 | both halves | 1e-05 | STRING 472 |
| [[FDFT1]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[LIPG]] | +0.63 | +0.60 / +0.54 | both halves | 1e-05 | STRING 749 |
| [[LDLR]] | +0.63 | +0.62 / +0.57 | both halves | 1e-05 | same gene group |
| [[ACSS2]] | +0.63 | +0.65 / +0.52 | both halves | 1e-05 | STRING 561 |
| [[DHCR7]] | +0.63 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[IDI1]] | +0.62 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[INSIG1]] | +0.61 | +0.63 / +0.48 | both halves | 2e-05 | STRING 610 |
| [[SREBF2]] | +0.58 | +0.42 / +0.56 | both halves | 4e-05 | same gene group; STRING 557 |
| [[STARD4]] | +0.58 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[PCYT2]] | +0.57 | +0.59 / +0.42 | both halves | 4e-05 | pathway: Glycerophospholipid biosynthesis |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAF1]] | -0.44 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[ZBTB26]] | -0.44 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[DYNLT2]] | -0.41 | -0.31 / -0.32 | both halves | 2e-04 |  |
| [[PAAF1]] | -0.41 | -0.22 / -0.45 | both halves | 6e-04 |  |
| [[COX10-DT]] | -0.41 | -0.36 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.682). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.1, -48.7); signed map (-52.2, 33.1). **Vector** length 129, 40.1% of its response variance represented; |z| ≥ 3 in 1,750 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *cholesterol synthesis* (control, mean cos +0.55 to 22); *Cholesterol biosynthesis* (reactome, mean cos +0.53 to 20); *cholesterol homeostasis* (hallmark, mean cos +0.54 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +9.5 | +20.0 |
|  | [[Berbamine (drug)]] 5 µM |  | +8.8 | +17.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +7.3 | +8.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +6.9 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.8 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +8.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.1 | -9.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.4 | -6.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | -0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | +0.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.2 | -7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.3 | -4.1 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.0 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | lipin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:11,677,595-11,827,409 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0188 |
| Gene groups (HGNC) | Lipins; MicroRNA protein coding host genes |
| Hallmark sets | SPERMATOGENESIS, MYOGENESIS |
| Reactome | 18 pathways, smallest: Triglyceride biosynthesis; Synthesis of PE; Depolymerization of the Nuclear Lamina |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14693](https://www.uniprot.org/uniprotkb/Q14693) (Phosphatidate phosphatase LPIN1):

> Acts as a magnesium-dependent phosphatidate phosphatase enzyme which catalyzes the conversion of phosphatidic acid to diacylglycerol during triglyceride, phosphatidylcholine and phosphatidylethanolamine biosynthesis and therefore controls the metabolism of fatty acids at different levels. Is involved in adipocyte differentiation (By similarity). Recruited at the mitochondrion outer membrane and is involved in mitochondrial fission by converting phosphatidic acid to diacylglycerol (By …

**Summary**, from NCBI Gene [23175](https://www.ncbi.nlm.nih.gov/gene/23175):

> This gene encodes a magnesium-ion-dependent phosphatidic acid phosphohydrolase enzyme that catalyzes the penultimate step in triglyceride synthesis including the dephosphorylation of phosphatidic acid to yield diacylglycerol. Expression of this gene is required for adipocyte differentiation and it also functions as a nuclear transcriptional coactivator with some peroxisome proliferator-activated receptors to modulate expression of other genes involved in lipid metabolism. Mutations in this gene …

**Accessions** — [HGNC:13345](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13345) · Entrez [23175](https://www.ncbi.nlm.nih.gov/gene/23175) · UniProt [Q14693](https://www.uniprot.org/uniprotkb/Q14693) · Ensembl [ENSG00000134324](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134324)

## Data

Gene col 5547: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5547); `tables/drug_effects.parquet` (80 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5547, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5547]; `tensor/DDL_lfc|DDL_z.npy` [5547]; `embed/gene_vectors.npy` [5547]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5547 or target_col == 5547). Every well: [[LPIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LPIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
