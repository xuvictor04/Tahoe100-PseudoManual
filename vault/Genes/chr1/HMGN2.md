---
symbol: "HMGN2"
type: "gene"
col: 12696
ensembl_id: "ENSG00000198830"
name: "high mobility group nucleosomal binding domain 2"
location: "1p36.11"
module: 173
arm: "+"
pooled_cpm: 68.22
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# HMGN2

*high mobility group nucleosomal binding domain 2* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.40× (z +22.3, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +6.8, q 1e-09, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.568× (z -6.3, q 1e-07, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGN2P5]] (+0.74, fdr 1e-05), [[HMGN1]] (+0.70, fdr 7e-06), [[STAG2]] (+0.70, fdr 1e-05); moves opposite to [[RBAK-RBAKDN]] (-0.69, fdr 1e-05), [[HMOX2]] (-0.68, fdr 1e-05), [[EIF3M]] (-0.66, fdr 1e-05).
> It is in [[Module 173]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12696.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.40×** | +22.3 | 0e+00 | 49/49 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.48×** | +20.1 | 0e+00 | 43/43 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.96×** | +16.5 | 0e+00 | 44/44 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **2.16×** | +8.6 | 1e-15 | 46/48 (HT-29, HOP62, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.78×** | +7.9 | 4e-13 | 37/48 (AsPC-1, NCI-H2030, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **2.00×** | +7.4 | 9e-12 | 38/48 (NCI-H2030, AsPC-1, …) | rises with dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +6.8 | 1e-09 | 43/48 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.82×** | +6.4 | 1e-08 | 42/47 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.64×** | +5.5 | 2e-06 | 37/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +5.4 | 5e-06 | 40/48 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +5.3 | 6e-06 | 36/50 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **1.60×** | +5.3 | 7e-06 | 36/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.56×** | +5.0 | 3e-05 | 35/48 (NCI-H2030, PANC-1, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +4.9 | 5e-05 | 30/48 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.49×** | +4.5 | 3e-04 | 38/48 (HT-29, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.3 | 7e-04 | 33/48 (A-172, HOP62, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.014 | 23/48 (HT-29, RKO, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.36×** | +3.4 | 0.018 | 23/48 (HT-29, HOP62, …) | inconsistent across doses | position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.020 | 28/48 (hTERT-HPNE, HepG2/C3A, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.022 | 27/48 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.042 | 22/48 (NCI-H1792, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.042 | 22/48 (HT-29, C32, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.067 | 20/48 (SK-MEL-2, HCT15, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12696.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.568×** | -6.3 | 1e-07 | 42/48 (BT-474, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.640×** | -5.0 | 2e-04 | 37/48 (HOP62, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.657×** | -4.7 | 5e-04 | 37/48 (HOP62, HCT15, …) | all doses, flat | cell-cycle shift (explains ~13% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.649×** | -4.6 | 7e-04 | 32/48 (NCI-H23, KATO III, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.692×** | -4.1 | 0.004 | 37/48 (SK-MEL-2, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.754× | -3.2 | 0.15 | 25/48 (SW480, SK-MEL-2, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.70 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12696. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 87.1 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.0× (z +17.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 49.3 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.1× (z +15.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 5.14× (z +9.9) | — |
| [[A549 (line)]] | wt | 31.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.9× (z +16.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 31.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.93× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 69.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.41× (z +17.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 86.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.3× (z +17.3) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 102 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.63× (z +17.3) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 127 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.86× (z +16.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 52.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.69× (z +14.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 124 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +9.9) | — |
| [[PANC-1 (line)]] | alt | 77.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.7× (z +18.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 34.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.50× (z +15.3) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 42.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +15.6) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 91.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +9.8) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 0.5 µM 0.265× (z -10.1) |
| [[C-33 A (line)]] | alt | 103 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.55× (z +12.9) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 45.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.88× (z +13.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 60.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +12.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 99.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.39× (z +11.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 79.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.12× (z +14.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 77.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.87× (z +14.7) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 69.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.27× (z +13.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 38.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.6× (z +18.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 66.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.09× (z +13.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 61.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.97× (z +13.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 32.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.83× (z +15.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 26.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 18.8× (z +18.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 45.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.1× (z +17.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 69.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.36× (z +15.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 81.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.10× (z +13.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 119 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +11.4) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 0.5 µM 0.371× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 59.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.05× (z +13.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 82.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.65× (z +15.4) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 55.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.72× (z +16.2) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 95.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +13.5) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 48.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.48× (z +12.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 80.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.51× (z +18.4) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 75.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +12.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 74.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.76× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 106 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.85× (z +14.2) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 61.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.58× (z +16.3) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 71.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.63× (z +14.1) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 34.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.9× (z +8.5) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 62.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.18× (z +14.9) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 34.1 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.110× (z -11.7) |
| [[RKO (line)]] | wt | 52.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.76× (z +12.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2122 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 84.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12696), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGN2P5]] | +0.74 | +0.88 / +0.51 | both halves | 1e-05 |  |
| [[HMGN1]] | +0.70 | +0.67 / +0.72 | both halves | 7e-06 | same gene group; STRING 994 |
| [[STAG2]] | +0.70 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[NUCKS1]] | +0.69 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[HNRNPU]] | +0.68 | +0.65 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[HNRNPH3]] | +0.67 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[FAM111A]] | +0.66 | +0.71 / +0.43 | both halves | 3e-05 |  |
| [[SUCLG2-DT]] | +0.65 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[ZNF532]] | +0.65 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[CGGBP1]] | +0.65 | +0.66 / +0.46 | both halves | 2e-05 |  |
| [[EIF4G2]] | +0.64 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[STMN1]] | +0.64 | +0.72 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBAK-RBAKDN]] | -0.69 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[HMOX2]] | -0.68 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[EIF3M]] | -0.66 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[ST6GALNAC6]] | -0.64 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[EIF3K]] | -0.63 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[ST6GALNAC6-1]] | -0.63 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[TMEM120B]] | -0.63 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[SNU13]] | -0.63 | -0.56 / -0.49 | both halves | 1e-05 | STRING 628 |
| [[NAT9]] | -0.62 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[RGS10]] | -0.62 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[TECPR1]] | -0.62 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[HM13]] | -0.61 | -0.55 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HMGN2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises HMGN2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises HMGN2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[POGLUT3]] | B | POGLUT3 activity raises HMGN2's level | lines that do not express POGLUT3 (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without POGLUT3 | 0.060 | ⚠ within organs, on part of the lines; also absent: DENND2B, MEX3A, CAMKK1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.601). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.8, 0.8); signed map (16.1, -35.6). **Vector** length 111, 38.8% of its response variance represented; |z| ≥ 3 in 1,085 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.7 | +4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | +6.7 | +7.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +0.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.2 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.0 | +0.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +1.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -7.4 | -6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.2 | -5.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | -6.0 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -1.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.8 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | +0.4 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -2.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.2 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | high mobility group nucleosomal binding domain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:26,472,440-26,476,642 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HMG17 |
| Gene groups (HGNC) | Canonical high mobility group |
| Hallmark sets | G2M_CHECKPOINT |
| Matched by | ensembl_id |

**Function**, from UniProt [P05204](https://www.uniprot.org/uniprotkb/P05204) (Non-histone chromosomal protein HMG-17):

> Binds to the inner side of the nucleosomal DNA thus altering the interaction between the DNA and the histone octamer. May be involved in the process which maintains transcribable genes in a unique chromatin conformation (By similarity).

**Summary**, from NCBI Gene [3151](https://www.ncbi.nlm.nih.gov/gene/3151):

> The protein encoded by this gene binds nucleosomal DNA and is associated with transcriptionally active chromatin. Along with a similar protein, HMGN1, the encoded protein may help maintain an open chromatin configuration around transcribable genes. The protein has also been found to have antimicrobial activity against bacteria, viruses and fungi. [provided by RefSeq, Oct 2014]

**Accessions** — [HGNC:4986](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4986) · Entrez [3151](https://www.ncbi.nlm.nih.gov/gene/3151) · UniProt [P05204](https://www.uniprot.org/uniprotkb/P05204) · Ensembl [ENSG00000198830](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198830)

## Data

Gene col 12696: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12696); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12696, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12696]; `tensor/DDL_lfc|DDL_z.npy` [12696]; `embed/gene_vectors.npy` [12696]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12696 or target_col == 12696). Every well: [[HMGN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMGN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
