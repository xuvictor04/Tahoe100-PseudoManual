---
symbol: "PEG10"
type: "gene"
col: 14310
ensembl_id: "ENSG00000242265"
name: "paternally expressed 10"
location: "7q21.3"
module: 9
arm: "+"
pooled_cpm: 74.66
n_lines_expressing: 33
n_dd_up: 49
n_dd_down: 7
n_dd_up_clean: 28
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PEG10

*paternally expressed 10* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 49 drug-doses (21 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.91× (z +34.9, q 0e+00, up in 24 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Temsirolimus (drug)]] 5 µM: 0.793× (z -4.6, q 0.002, down in 17 of 32 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLEU1]] (+0.60, fdr 3e-05), [[PCDH10]] (+0.59, fdr 1e-05), [[FREM2]] (+0.58, fdr 7e-06); moves opposite to [[C19orf25]] (-0.60, fdr 1e-05), [[ZNF500]] (-0.53, fdr 2e-05), [[PEX16]] (-0.53, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MBNL3]] → it (grade B ⚠); 2 go from it, the strongest it → [[ZBTB49]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 22 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 49 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14310.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.91×** | +34.9 | 0e+00 | 24/31 (hTERT-HPNE, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.32×** | +28.7 | 0e+00 | 27/32 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.01×** | +24.9 | 0e+00 | 30/31 (SK-MEL-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM |  | **5.60×** | +23.9 | 0e+00 | 30/31 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **5.10×** | +22.6 | 0e+00 | 29/31 (SW 900, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **4.62×** | +20.4 | 0e+00 | 25/26 (A498, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.89×** | +17.4 | 0e+00 | 26/28 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **3.42×** | +17.0 | 0e+00 | 29/31 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.18×** | +16.0 | 0e+00 | 24/31 (hTERT-HPNE, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.18×** | +15.3 | 0e+00 | 30/31 (SW 900, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **3.00×** | +14.7 | 0e+00 | 24/31 (hTERT-HPNE, C32, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.43×** | +12.3 | 5e-33 | 27/31 (SW 900, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **2.10×** | +10.3 | 4e-23 | 28/32 (LOX-IMVI, SW 900, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **3.96×** | +10.0 | 8e-22 | 28/31 (LOX-IMVI, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.02×** | +9.7 | 9e-21 | 22/31 (LOX-IMVI, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +9.0 | 7e-18 | 21/31 (HOP62, J82, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **2.75×** | +7.3 | 7e-12 | 26/30 (Panc 03.27, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +7.3 | 1e-11 | 25/32 (SW 900, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.56×** | +6.8 | 2e-10 | 23/32 (SW 900, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +6.3 | 5e-09 | 19/31 (J82, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +5.8 | 1e-07 | 19/31 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14310.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Temsirolimus (drug)]] 5 µM |  | **0.793×** | -4.6 | 0.002 | 17/32 (SHP-77, AN3 CA, …) | all doses, stronger at high dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.803×** | -4.3 | 0.004 | 16/32 (A-427, SHP-77, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.749×** | -3.8 | 0.022 | 15/31 (SHP-77, HepG2/C3A, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.755×** | -3.8 | 0.022 | 9/31 (CFPAC-1, NCI-H2347, …) | rises with dose | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | 0.834× | -3.6 | 0.035 | 13/31 (SHP-77, AN3 CA, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.777×** | -3.5 | 0.037 | 12/31 (SW 1088, SHP-77, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.779×** | -3.5 | 0.037 | 13/31 (A-427, NCI-H23, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -3.5 | 0.037 | 1/33 (SW 1088) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.774×** | -3.4 | 0.046 | 11/32 (AN3 CA, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.61 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14310. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 174 | 21 (12 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +22.6) | — |
| [[C32 (line)]] | wt | 47.5 | 18 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 28.6× (z +25.7) | — |
| [[SW 900 (line)]] | alt | 97.8 | 16 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.22× (z +24.0) | — |
| [[J82 (line)]] | alt | 57.5 | 14 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.08× (z +22.4) | — |
| [[NCI-H1573 (line)]] | alt | 19.3 | 12 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 25.7× (z +23.1) | — |
| [[PANC-1 (line)]] | alt | 46.4 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +21.7) | — |
| [[A498 (line)]] | wt | 84.3 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.84× (z +21.0) | — |
| [[hTERT-HPNE (line)]] | wt | 68.0 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.0× (z +31.7) | — |
| [[NCI-H1792 (line)]] | alt | 22.6 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 23.3× (z +23.1) | — |
| [[CFPAC-1 (line)]] | alt | 137 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +22.1) | — |
| [[HOP62 (line)]] | alt | 19.1 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.70× (z +18.0) | — |
| [[SK-MEL-2 (line)]] | alt | 28.0 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +18.5) | — |
| [[A549 (line)]] | wt | 29.8 | 8 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.36× (z +15.4) | — |
| [[HepG2_C3A (line)]] | wt | 308 | 6 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.66× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 3.57× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 34.4 | 8 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.95× (z +18.1) | — |
| [[SW480 (line)]] | alt | 53.3 | 8 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.24× (z +16.0) | — |
| [[Panc 03.27 (line)]] | alt | 80.7 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.33× (z +16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.05× (z +12.2) | — |
| [[SNU-423 (line)]] | alt | 36.7 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +18.2) | — |
| [[SHP-77 (line)]] | alt | 904 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -12.4) |
| [[A-427 (line)]] | wt | 256 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.95× (z +11.0) | [[Daptomycin (drug)]] 5 µM 0.396× (z -9.5) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.527× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 20.7 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 25.6× (z +16.7) | — |
| [[BT-474 (line)]] | alt | 19.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.6× (z +16.5) | — |
| [[C-33 A (line)]] | alt | 178 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.30× (z +13.9) | — |
| [[H4 (line)]] | wt | 105 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +13.1) | — |
| [[HS-578T (line)]] | alt | 79.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +18.3) | — |
| [[NCI-H2347 (line)]] | alt | 199 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +12.8) | — |
| [[AN3 CA (line)]] | alt | 1,373 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -15.9) |
| [[A-172 (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 62.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.15 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.86 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.29 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.98 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.98 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.42 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.46 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.57 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.87 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.60 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1,164 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.44 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.45 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.52 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.08 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14310), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLEU1]] | +0.60 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[PCDH10]] | +0.59 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[FREM2]] | +0.58 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[PCDH9]] | +0.58 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[CCN3]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[PCDH17]] | +0.56 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[COL12A1]] | +0.55 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[FAT1]] | +0.55 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[CDH2]] | +0.54 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[NCAM2]] | +0.54 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[EPHA5]] | +0.54 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[ABLIM1]] | +0.54 | +0.51 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C19orf25]] | -0.60 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ZNF500]] | -0.53 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[PEX16]] | -0.53 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[MEF2B]] | -0.53 | -0.28 / -0.55 | both halves | 3e-04 |  |
| [[DNAAF9]] | -0.52 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[VRK3]] | -0.51 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[RHBDF2]] | -0.51 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[NOXRED1]] | -0.50 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[TMEM92-AS1]] | -0.50 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[RAB43]] | -0.49 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ZBTB49]] | -0.49 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[ZNF549]] | -0.49 | -0.48 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MBNL3]] | B | MBNL3 activity raises PEG10's level | lines that do not express MBNL3 (16) vs lines expressing it (34) | 1.60× lower at baseline in the lines without MBNL3 | 0.073 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| [[TOP2A]] | B | TOP2A activity lowers PEG10's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EPHA7]] | C | EPHA7 activity raises PEG10's level | lines that do not express EPHA7 (30) vs lines expressing it (20) | 3.94× lower at baseline in the lines without EPHA7 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000287683, GRIA2, NTNG1; co-absent with the target |
| [[TMEM47]] | C | TMEM47 activity raises PEG10's level | lines that do not express TMEM47 (27) vs lines expressing it (23) | 3.68× lower at baseline in the lines without TMEM47 | 0.089 | ⚠ within organs, on part of the lines; also absent: KCNE4, ENSG00000280241, ENSG00000225649; co-absent with the target |
| [[CDH2]] | C | CDH2 activity raises PEG10's level | lines that do not express CDH2 (22) vs lines expressing it (28) | 4.18× lower at baseline in the lines without CDH2 | 0.092 | ⚠ within organs, on part of the lines; also absent: ARMCX1, DKK3, RFTN1; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZBTB49]] | B | PEG10 activity raises ZBTB49's level | lines that do not express PEG10 (17) vs lines expressing it (33) | 1.24× lower at baseline in the lines without PEG10 | 0.029 | ⚠ within organs, on part of the lines; also absent: ZNF569, ZNF570, MAP1B |
| [[TMEM47]] | C | PEG10 activity raises TMEM47's level | lines that do not express PEG10 (17) vs lines expressing it (33) | 3.31× lower at baseline in the lines without PEG10 | 0.099 | ⚠ within organs, on part of the lines; also absent: ZNF569, ZNF570, MAP1B; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.483). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.1, 30.2); signed map (44.1, 30.0). **Vector** length 102, 28.2% of its response variance represented; |z| ≥ 3 in 1,215 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +6.5 | +22.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +5.2 | +20.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.9 | +17.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +5.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +2.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~74% of this change | -3.4 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.8 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -1.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -3.5 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.8 | -3.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.6 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | paternally expressed 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.3 — chr7:94,656,325-94,669,695 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1051, HB-1, MEF3L, RGAG3, Mar2, Mart2, SIRH1, RTL2 |
| Gene groups (HGNC) | Retrotransposon Gag like family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86TG7](https://www.uniprot.org/uniprotkb/Q86TG7) (Retrotransposon-derived protein PEG10):

> Retrotransposon-derived protein that binds its own mRNA and self-assembles into virion-like capsids. Forms virion-like extracellular vesicles that encapsulate their own mRNA and are released from cells, enabling intercellular transfer of PEG10 mRNA. Binds its own mRNA in the 5'-UTR region, in the region near the boundary between the nucleocapsid (NC) and protease (PRO) coding sequences and in the beginning of the 3'-UTR region. Involved in placenta formation: required for trophoblast stem cells …

**Summary**, from NCBI Gene [23089](https://www.ncbi.nlm.nih.gov/gene/23089):

> This is a paternally expressed imprinted gene that is thought to have been derived from the Ty3/Gypsy family of retrotransposons. It contains two overlapping open reading frames, RF1 and RF2, and expresses two proteins: a shorter, gag-like protein (with a CCHC-type zinc finger domain) from RF1; and a longer, gag/pol-like fusion protein (with an additional aspartic protease motif) from RF1/RF2 by -1 translational frameshifting (-1 FS). While -1 FS has been observed in RNA viruses and transposons …

**Accessions** — [HGNC:14005](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14005) · Entrez [23089](https://www.ncbi.nlm.nih.gov/gene/23089) · UniProt [Q86TG7](https://www.uniprot.org/uniprotkb/Q86TG7) · Ensembl [ENSG00000242265](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242265)

## Data

Gene col 14310: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14310); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14310, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14310]; `tensor/DDL_lfc|DDL_z.npy` [14310]; `embed/gene_vectors.npy` [14310]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14310 or target_col == 14310). Every well: [[PEG10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEG10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
