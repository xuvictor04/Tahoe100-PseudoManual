---
symbol: "LHFPL6"
type: "gene"
col: 11442
ensembl_id: "ENSG00000183722"
name: "LHFPL tetraspan subfamily member 6"
location: "13q13.3-q14.11"
module: 14
arm: "+"
pooled_cpm: 75.53
n_lines_expressing: 39
n_dd_up: 23
n_dd_down: 11
n_dd_up_clean: 15
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 8
direction_downstream: 14
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# LHFPL6

*LHFPL tetraspan subfamily member 6* — 13q13.3-q14.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.70× (z +41.0, q 0e+00, up in 37 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.494× (z -15.7, q 0e+00, down in 29 of 37 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC14A]] (+0.63, fdr 1e-05), [[TIFA]] (+0.60, fdr 2e-05), [[WAKMAR2]] (+0.58, fdr 7e-05); moves opposite to [[SAMD4B]] (-0.56, fdr 3e-05), [[SIN3B]] (-0.56, fdr 2e-05), [[HERC2P3]] (-0.55, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 14 go from it, the strongest it → [[ERI3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11442.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.70×** | +41.0 | 0e+00 | 37/37 (Panc 03.27, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +28.8 | 0e+00 | 35/38 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.10×** | +24.2 | 0e+00 | 35/37 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.17×** | +17.2 | 0e+00 | 30/37 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +14.5 | 0e+00 | 31/37 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.82×** | +12.0 | 2e-31 | 28/38 (HS-578T, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +11.8 | 4e-30 | 31/39 (SK-MEL-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +10.3 | 6e-23 | 27/37 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.43×** | +7.9 | 2e-13 | 22/37 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +7.6 | 2e-12 | 28/37 (J82, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +7.4 | 8e-12 | 22/37 (Hs 766T, HEC-1-A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.34×** | +6.4 | 6e-09 | 21/37 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.33×** | +6.1 | 4e-08 | 19/36 (J82, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.9 | 2e-07 | 14/37 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +5.1 | 1e-05 | 17/37 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.38×** | +5.1 | 1e-05 | 12/37 (Hs 766T, NCI-H2030, …) | two highest doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.001 | 11/37 (Hs 766T, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.18× | +3.5 | 0.010 | 8/38 (SK-MEL-2, CFPAC-1, …) | top dose only |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.11× | +3.1 | 0.044 | 6/37 (SK-MEL-2, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11442.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.494×** | -15.7 | 0e+00 | 29/37 (J82, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.531×** | -14.1 | 1e-42 | 28/38 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.593×** | -11.6 | 7e-29 | 26/37 (SW480, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.619×** | -10.2 | 2e-22 | 24/35 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.718×** | -7.4 | 2e-11 | 27/37 (J82, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.749×** | -6.4 | 1e-08 | 22/37 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.737×** | -6.4 | 1e-08 | 21/37 (A-172, C32, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.759×** | -6.1 | 6e-08 | 20/37 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.770×** | -5.8 | 4e-07 | 16/37 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.817×** | -4.5 | 4e-04 | 16/37 (J82, A-172, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.950× | -4.2 | 0.001 | 2/39 (MIA PaCa-2, SW48) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.837× | -4.0 | 0.003 | 14/37 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.840× | -3.9 | 0.005 | 15/38 (HOP62, J82, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.798×** | -3.6 | 0.014 | 15/37 (CHP-212, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.857× | -3.3 | 0.037 | 5/37 (hTERT-HPNE, NCI-H1573, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.865× | -3.2 | 0.043 | 9/37 (A498, SW48, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.874× | -3.0 | 0.085 | 9/37 (A-172, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11442. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 220 | 7 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.460× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 87.9 | 10 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +20.6) | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -9.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 86.8 | 8 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +24.5) | [[Panobinostat (drug)]] 5 µM 0.309× (z -12.3) |
| [[J82 (line)]] | alt | 264 | 5 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +26.3) | [[Panobinostat (drug)]] 0.5 µM 0.360× (z -16.7) |
| [[A-172 (line)]] | wt | 205 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.261× (z -13.3) |
| [[Hs 766T (line)]] | wt | 152 | 4 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +21.0) | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -14.1) |
| [[SW480 (line)]] | alt | 53.9 | 4 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +20.6) | [[Dinaciclib (drug)]] 5 µM 0.214× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.289× (z -14.4) |
| [[CFPAC-1 (line)]] | alt | 110 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +27.1) | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.336× (z -8.7) |
| [[HOP62 (line)]] | alt | 56.4 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +21.6) | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 89.1 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +32.1) | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 75.5 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +31.8) | — |
| [[SNU-423 (line)]] | alt | 92.2 | 5 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +27.1) | [[Panobinostat (drug)]] 0.5 µM 0.294× (z -13.5) |
| [[A498 (line)]] | wt | 134 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +24.2) | — |
| [[HEC-1-A (line)]] | alt | 78.1 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +17.0) | [[Dinaciclib (drug)]] 0.5 µM 0.464× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.495× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 128 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +22.5) | — |
| [[SK-MEL-2 (line)]] | alt | 50.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +16.5) | — |
| [[A-427 (line)]] | wt | 70.8 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.149× (z -14.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 176 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +23.3) | — |
| [[LOX-IMVI (line)]] | wt | 126 | 2 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.440× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 40.9 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +14.4) | [[Ixazomib citrate (drug)]] 5 µM 0.355× (z -8.6) |
| [[SW 900 (line)]] | alt | 77.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.54× (z +23.4) | — |
| [[A549 (line)]] | wt | 35.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.52× (z +18.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.59× (z +18.7) | — |
| [[NCI-H2030 (line)]] | alt | 79.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -8.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 77.0 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +20.5) | — |
| [[NCI-H23 (line)]] | alt | 77.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -12.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 51.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.74× (z +18.7) | — |
| [[NCI-H1792 (line)]] | alt | 58.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -11.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 67.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -10.2) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 117 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.44× (z +10.9) | — |
| [[SW 1271 (line)]] | alt | 131 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.49 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.77 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.44 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.42 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.34 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.24 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 347 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.89 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.74 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 30.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11442), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC14A]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[TIFA]] | +0.60 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[WAKMAR2]] | +0.58 | +0.44 / +0.38 | both halves | 7e-05 |  |
| [[MEIS2]] | +0.57 | +0.33 / +0.57 | both halves | 1e-04 |  |
| [[FAS]] | +0.57 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[MICOS10]] | +0.57 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[NFKBID]] | +0.56 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[QKI]] | +0.56 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[CDK6-AS1]] | +0.56 | +0.45 / +0.35 | both halves | 1e-04 |  |
| [[ZNF827]] | +0.56 | +0.29 / +0.42 | both halves | 2e-04 |  |
| [[MB21D2]] | +0.56 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[SEPTIN8]] | +0.54 | +0.46 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD4B]] | -0.56 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[SIN3B]] | -0.56 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[HERC2P3]] | -0.55 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[KCTD20]] | -0.55 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[ZNF875]] | -0.55 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[PRKCZ]] | -0.55 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[RNF216]] | -0.54 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[KCTD21]] | -0.53 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[PSMD3]] | -0.53 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[HERC2P2]] | -0.53 | -0.45 / -0.32 | both halves | 1e-04 |  |
| [[CALCOCO2]] | -0.53 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[ERI3]] | -0.53 | -0.46 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LHFPL6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FMNL3]] | B | FMNL3 activity raises LHFPL6's level | lines that do not express FMNL3 (8) vs lines expressing it (42) | 4.01× lower at baseline in the lines without FMNL3 | 0.059 | ⚠ within organs, on part of the lines; also absent: STARD9, CERCAM, ASAP3 |
| [[IL7R]] | B | IL7R activity raises LHFPL6's level | lines that do not express IL7R (30) vs lines expressing it (20) | 3.21× lower at baseline in the lines without IL7R | 0.079 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1 |
| [[HECTD2]] | B | HECTD2 activity raises LHFPL6's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 7.05× lower at baseline in the lines without HECTD2 | 0.079 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[CAMK4]] | C | CAMK4 activity raises LHFPL6's level | lines that do not express CAMK4 (21) vs lines expressing it (29) | 3.83× lower at baseline in the lines without CAMK4 | 0.024 | ⚠ within organs, on part of the lines; also absent: SNAP25, PRR16, ADAM12; co-absent with the target |
| [[CAV1]] | C | CAV1 activity raises LHFPL6's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 4.56× lower at baseline in the lines without CAV1 | 0.037 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6; co-absent with the target |
| [[OGFRL1]] | C | OGFRL1 activity raises LHFPL6's level | lines that do not express OGFRL1 (10) vs lines expressing it (40) | 4.42× lower at baseline in the lines without OGFRL1 | 0.061 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, HDGFL3, CYP46A1; co-absent with the target |
| [[GASAL1]] | C | GASAL1 activity raises LHFPL6's level | lines that do not express GASAL1 (3) vs lines expressing it (47) | 4.13× lower at baseline in the lines without GASAL1 | 0.073 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NECAB2, DLG4, CEP112; maybe low, not absent |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 12, C 2. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERI3]] | B | LHFPL6 activity raises ERI3's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.55× lower at baseline in the lines without LHFPL6 | 0.007 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |
| [[REV3L]] | B | LHFPL6 activity raises REV3L's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.76× lower at baseline in the lines without LHFPL6 | 0.027 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |
| [[ATP23]] | B | LHFPL6 activity raises ATP23's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without LHFPL6 | 0.035 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |
| [[SNHG31]] | B | LHFPL6 activity raises SNHG31's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 2.01× lower at baseline in the lines without LHFPL6 | 0.040 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |
| [[DNAJC16]] | B | LHFPL6 activity raises DNAJC16's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.08× lower at baseline in the lines without LHFPL6 | 0.061 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |
| [[WDR59]] | B | LHFPL6 activity raises WDR59's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.32× lower at baseline in the lines without LHFPL6 | 0.068 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |
| [[ENO3]] | B | LHFPL6 activity raises ENO3's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.46× lower at baseline in the lines without LHFPL6 | 0.079 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |
| [[CMC4]] | B | LHFPL6 activity raises CMC4's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.46× lower at baseline in the lines without LHFPL6 | 0.079 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |
| [[RWDD2B]] | B | LHFPL6 activity raises RWDD2B's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.20× lower at baseline in the lines without LHFPL6 | 0.087 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |
| [[GALNS]] | B | LHFPL6 activity raises GALNS's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.45× lower at baseline in the lines without LHFPL6 | 0.091 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |
| [[STARD4-AS1]] | B | LHFPL6 activity raises STARD4-AS1's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.79× lower at baseline in the lines without LHFPL6 | 0.092 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |
| [[HSF1]] | B | LHFPL6 activity lowers HSF1's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.17× higher at baseline in the lines without LHFPL6 | 0.0998 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.482). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.7, 5.8); signed map (44.3, 0.1). **Vector** length 118, 32.3% of its response variance represented; |z| ≥ 3 in 1,170 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.1 | +28.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +41.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +14.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.1 | +5.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +4.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.7 | +1.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -6.7 | -6.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.7 | -15.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.1 | -6.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.0 | -11.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.7 | -5.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.4 | -3.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.3 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | LHFPL tetraspan subfamily member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.3-q14.11 — chr13:39,209,116-39,603,528 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC22429; previously LHFP |
| Gene groups (HGNC) | LHFPL tetraspan proteins |
| Matched by | ensembl_id |

UniProt [Q9Y693](https://www.uniprot.org/uniprotkb/Q9Y693) carries no function annotation.

**Summary**, from NCBI Gene [10186](https://www.ncbi.nlm.nih.gov/gene/10186):

> This gene is a member of the lipoma HMGIC fusion partner (LHFP) gene family, which is a subset of the superfamily of tetraspan transmembrane protein encoding genes. This gene is fused to a high-mobility group gene in a translocation-associated lipoma. Mutations in another LHFP-like gene result in deafness in humans and mice. Alternatively spliced transcript variants have been found; however, their full-length nature is not known. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6586](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6586) · Entrez [10186](https://www.ncbi.nlm.nih.gov/gene/10186) · UniProt [Q9Y693](https://www.uniprot.org/uniprotkb/Q9Y693) · Ensembl [ENSG00000183722](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183722)

## Data

Gene col 11442: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11442); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11442, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11442]; `tensor/DDL_lfc|DDL_z.npy` [11442]; `embed/gene_vectors.npy` [11442]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11442 or target_col == 11442). Every well: [[LHFPL6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LHFPL6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
