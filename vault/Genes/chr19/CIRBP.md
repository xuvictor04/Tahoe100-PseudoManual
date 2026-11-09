---
symbol: "CIRBP"
type: "gene"
col: 1805
ensembl_id: "ENSG00000099622"
name: "cold inducible RNA binding protein"
location: "19p13.3"
module: 12
arm: "+"
pooled_cpm: 35.52
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# CIRBP

*cold inducible RNA binding protein* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.31× (z +12.2, q 1e-31, up in 42 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.73× (z +11.1, q 6e-26, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.598× (z -7.5, q 4e-11, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASHC1]] (+0.70, fdr 1e-05), [[CHMP4A]] (+0.68, fdr 1e-05), [[DXO]] (+0.68, fdr 1e-05); moves opposite to [[C1GALT1C1]] (-0.66, fdr 1e-05), [[ATP5MC3]] (-0.62, fdr 3e-05, ⚠ ATP5MC3 in the vector space only through flagged drug-doses), [[BRI3BP]] (-0.62, fdr 2e-05), [[AP1S1]] (-0.61, fdr 4e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1805.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +12.2 | 1e-31 | 42/46 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +11.1 | 6e-26 | 42/47 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +9.8 | 3e-20 | 34/40 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +8.8 | 2e-16 | 43/47 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +7.6 | 4e-12 | 38/48 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +5.7 | 1e-06 | 31/45 (A498, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +5.4 | 5e-06 | 31/43 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +4.8 | 1e-04 | 30/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.68×** | +4.6 | 3e-04 | 29/47 (HOP62, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.3 | 0.001 | 21/48 (NCI-H2347, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.58×** | +4.0 | 0.003 | 27/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.54×** | +3.8 | 0.006 | 19/47 (SW480, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.8 | 0.006 | 2/49 (MIA PaCa-2, COLO 205) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.53×** | +3.8 | 0.006 | 19/48 (C32, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.53×** | +3.8 | 0.006 | 21/48 (HOP62, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.011 | 22/48 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.022 | 18/48 (HOP62, C32, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.039 | 17/48 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.043 | 14/48 (LS 180, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.057 | 16/47 (hTERT-HPNE, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1805.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.598×** | -7.5 | 4e-11 | 36/48 (BT-474, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.655×** | -6.2 | 2e-07 | 35/48 (HT-29, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.656×** | -6.1 | 2e-07 | 37/48 (SW 900, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.748×** | -5.9 | 7e-07 | 30/48 (A-427, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.484×** | -4.7 | 3e-04 | 29/48 (NCI-H1573, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.504×** | -4.4 | 8e-04 | 25/49 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.738×** | -4.4 | 8e-04 | 24/47 (COLO 205, SW480, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.752×** | -4.2 | 0.002 | 25/47 (PANC-1, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.769×** | -3.8 | 0.008 | 24/48 (CHP-212, SNU-423, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Pyridoxine (drug)]] 5 µM |  | 0.853× | -3.2 | 0.072 | 9/48 (H4, C32, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.795×** | -3.2 | 0.081 | 21/47 (BT-474, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1805. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 30.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +11.6) | — |
| [[C32 (line)]] | wt | 44.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +8.8) | — |
| [[LoVo (line)]] | wt | 43.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +12.2) | — |
| [[SW480 (line)]] | alt | 42.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.1) | — |
| [[A498 (line)]] | wt | 26.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +13.6) | — |
| [[A-427 (line)]] | wt | 37.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.471× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 28.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 41.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.223× (z -10.7) |
| [[COLO 205 (line)]] | alt | 29.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -11.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 40.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.103× (z -13.5) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 39.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +9.3) | — |
| [[KATO III (line)]] | alt | 34.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 47.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +8.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 46.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.80× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 23.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 38.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 31.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.88× (z +12.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 34.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +9.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 24.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.17× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 38.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.0) | — |
| [[A-172 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 72.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1805), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASHC1]] | +0.70 | +0.79 / +0.53 | both halves | 1e-05 |  |
| [[CHMP4A]] | +0.68 | +0.78 / +0.57 | both halves | 1e-05 |  |
| [[DXO]] | +0.68 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[PQBP1]] | +0.67 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[CCT6P3]] | +0.66 | +0.73 / +0.39 | both halves | 5e-05 |  |
| [[ZNF213]] | +0.66 | +0.74 / +0.50 | both halves | 1e-05 |  |
| [[BRD4]] | +0.66 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ENO3]] | +0.65 | +0.75 / +0.46 | both halves | 2e-05 |  |
| [[CYP20A1]] | +0.65 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[STK16]] | +0.64 | +0.81 / +0.37 | both halves | 7e-05 |  |
| [[HNRNPH1]] | +0.64 | +0.69 / +0.55 | both halves | 1e-05 | same gene group |
| [[PAN2]] | +0.63 | +0.72 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1GALT1C1]] | -0.66 | -0.70 / -0.52 | both halves | 1e-05 |  |
| [[ATP5MC3]] ⚠ | -0.62 | -0.62 / -0.44 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[BRI3BP]] | -0.62 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[AP1S1]] | -0.61 | -0.67 / -0.42 | both halves | 4e-05 |  |
| [[DCAF16]] | -0.59 | -0.70 / -0.39 | both halves | 5e-05 |  |
| [[RNGTT]] | -0.59 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[TMEM97]] | -0.58 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[PRIM2]] | -0.56 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[HACD3]] | -0.56 | -0.63 / -0.35 | both halves | 1e-04 |  |
| [[AP3M2]] | -0.56 | -0.67 / -0.38 | both halves | 6e-05 |  |
| [[SNHG30]] | -0.56 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[MYCBP]] | -0.56 | -0.65 / -0.31 | both halves | 2e-04 |  |
| [[NUTF2]] | -0.55 | -0.65 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.461). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-13.0, 6.5); signed map (11.0, -20.0). **Vector** length 104, 28.0% of its response variance represented; |z| ≥ 3 in 793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.6 | +11.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.8 | +8.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.4 | +7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.8 | +4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +3.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.7 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.5 | +4.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.5 | +3.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.4 | -5.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.1 | -6.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.1 | -7.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -4.7 |
|  | [[vincristine (drug)]] 0.05 µM |  | -2.0 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.7 | -1.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.6 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | cold inducible RNA binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,259,384-1,274,880 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CIRP |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14011](https://www.uniprot.org/uniprotkb/Q14011) (Cold-inducible RNA-binding protein):

> Cold-inducible mRNA binding protein that plays a protective role in the genotoxic stress response by stabilizing transcripts of genes involved in cell survival. Acts as a translational activator. Seems to play an essential role in cold-induced suppression of cell proliferation. Binds specifically to the 3'-untranslated regions (3'-UTRs) of stress-responsive transcripts RPA2 and TXN. Acts as a translational repressor (By similarity). Promotes assembly of stress granules (SGs), when overexpressed.

**Summary**, from NCBI Gene [1153](https://www.ncbi.nlm.nih.gov/gene/1153):

> Enables mRNA 3'-UTR binding activity and small ribosomal subunit rRNA binding activity. Involved in mRNA stabilization; positive regulation of translation; and response to UV. Located in cytoplasm and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1982](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1982) · Entrez [1153](https://www.ncbi.nlm.nih.gov/gene/1153) · UniProt [Q14011](https://www.uniprot.org/uniprotkb/Q14011) · Ensembl [ENSG00000099622](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099622)

## Data

Gene col 1805: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1805); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1805, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1805]; `tensor/DDL_lfc|DDL_z.npy` [1805]; `embed/gene_vectors.npy` [1805]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1805 or target_col == 1805). Every well: [[CIRBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CIRBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
