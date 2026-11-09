---
symbol: "CBR3-AS1"
type: "gene"
col: 14105
ensembl_id: "ENSG00000236830"
name: "CBR3 antisense RNA 1"
location: "21q22.12"
module: 4
arm: "-"
pooled_cpm: 10.78
n_lines_expressing: 49
n_dd_up: 32
n_dd_down: 8
n_dd_up_clean: 24
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CBR3-AS1

*CBR3 antisense RNA 1* — 21q22.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.52× (z +28.5, q 0e+00, up in 42 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.405× (z -6.3, q 2e-07, down in 24 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRPV3]] (+0.55, fdr 1e-05), [[ZNF165]] (+0.53, fdr 3e-05), [[CFAP20DC-AS1]] (+0.53, fdr 5e-05); moves opposite to [[AIFM1]] (-0.54, fdr 5e-05), [[PRKDC]] (-0.53, fdr 2e-05), [[RHOBTB2]] (-0.53, fdr 1e-04).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MYO5B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14105.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.52×** | +28.5 | 0e+00 | 42/42 (CFPAC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.74×** | +20.8 | 0e+00 | 44/46 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.68×** | +17.4 | 0e+00 | 41/45 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.29×** | +15.9 | 0e+00 | 40/46 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +11.9 | 1e-30 | 21/39 (COLO 205, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +8.8 | 1e-16 | 26/37 (CFPAC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +7.6 | 3e-12 | 23/46 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.71×** | +7.2 | 6e-11 | 21/46 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +6.9 | 4e-10 | 5/16 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +6.7 | 1e-09 | 22/46 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.5 | 4e-09 | 20/38 (CFPAC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.54×** | +5.7 | 5e-07 | 17/45 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.20×** | +5.5 | 2e-06 | 15/44 (A-172, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.52×** | +5.4 | 3e-06 | 13/32 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +5.3 | 4e-06 | 16/38 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.41×** | +4.6 | 2e-04 | 18/46 (SW1417, LoVo, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.38×** | +4.3 | 5e-04 | 14/46 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +4.2 | 9e-04 | 14/45 (COLO 205, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14105.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.405×** | -6.3 | 2e-07 | 24/43 (SW1417, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.433×** | -5.8 | 2e-06 | 20/39 (A-172, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.671×** | -5.3 | 2e-05 | 19/41 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.722×** | -4.3 | 0.002 | 11/45 (A549, C32, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.728×** | -4.2 | 0.003 | 17/46 (COLO 205, LS 180, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.757×** | -3.7 | 0.020 | 11/44 (COLO 205, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.760×** | -3.6 | 0.021 | 9/44 (AsPC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.625×** | -3.3 | 0.076 | 10/39 (SW48, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.846× | -3.1 | 0.10 | 10/46 (SW 1271, Hs 766T, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.784× | -3.1 | 0.10 | 15/42 (LoVo, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.793× | -3.1 | 0.10 | 15/44 (SNU-423, LS 180, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14105. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 51.9 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +14.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.218× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~47% of this change |
| [[SW480 (line)]] | alt | 8.24 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +14.2) | — |
| [[AsPC-1 (line)]] | alt | 7.32 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +13.3) | — |
| [[CFPAC-1 (line)]] | alt | 19.4 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.94× (z +18.0) | — |
| [[HT-29 (line)]] | alt | 25.7 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.12× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.0760× (z -16.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 24.8 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.170× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 7.51 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 6.49× (z +9.3) | [[PH-797804 (drug)]] 5 µM 0.0378× (z -8.5) |
| [[A498 (line)]] | wt | 5.26 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.93× (z +10.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.61 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.98× (z +13.3) | — |
| [[NCI-H460 (line)]] | wt | 4.72 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.54× (z +10.5) | [[Digitoxin (drug)]] 5 µM 0.117× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[PANC-1 (line)]] | alt | 4.99 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.24× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 15.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +9.8) | [[Docetaxel (drug)]] 0.05 µM 0.0964× (z -9.1) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 4.68 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.08× (z +11.8) | — |
| [[LoVo (line)]] | wt | 17.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +15.0) | — |
| [[NCI-H1573 (line)]] | alt | 17.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.98× (z +14.6) | — |
| [[SW1417 (line)]] | alt | 33.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 3.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.16× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 39.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +10.6) | — |
| [[HEC-1-A (line)]] | alt | 10.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.79× (z +17.7) | — |
| [[HepG2_C3A (line)]] | wt | 14.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.98× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 4.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.69× (z +8.6) | — |
| [[J82 (line)]] | alt | 3.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +10.5) | — |
| [[KATO III (line)]] | alt | 12.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.12× (z +15.0) | — |
| [[Panc 03.27 (line)]] | alt | 16.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.88× (z +14.5) | — |
| [[SNU-423 (line)]] | alt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +9.7) | — |
| [[A-427 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14105), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRPV3]] | +0.55 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[ZNF165]] | +0.53 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[CFAP20DC-AS1]] | +0.53 | +0.40 / +0.49 | both halves | 5e-05 | same gene group |
| [[KPNA7]] | +0.52 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[PCF11-AS1]] | +0.52 | +0.47 / +0.49 | both halves | 2e-05 | same gene group |
| [[RABGEF1]] | +0.51 | +0.26 / +0.52 | both halves | 3e-04 |  |
| [[USP34-DT]] | +0.51 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ULBP2]] | +0.51 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[OSER1-DT]] | +0.50 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[BTG1-DT]] | +0.50 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[HNRNPD-DT]] | +0.50 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[TMEM106A]] | +0.50 | +0.47 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AIFM1]] | -0.54 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[PRKDC]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[RHOBTB2]] | -0.53 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[MTHFD1]] | -0.52 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[PPP5C]] | -0.52 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[HNRNPF]] | -0.51 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[TUBGCP3]] | -0.50 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[NUP155]] | -0.49 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[ATIC]] | -0.49 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[IGFBP4]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[WDR36]] | -0.48 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[RUVBL1]] | -0.47 | -0.34 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO5B]] | B | MYO5B activity raises CBR3-AS1's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 2.46× lower at baseline in the lines without MYO5B | 0.001 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[RNF223]] | B | RNF223 activity raises CBR3-AS1's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 2.59× lower at baseline in the lines without RNF223 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2 |
| [[MPZL3]] | B | MPZL3 activity raises CBR3-AS1's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 2.47× lower at baseline in the lines without MPZL3 | 0.002 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[KPNA7]] | B | KPNA7 activity raises CBR3-AS1's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 2.24× lower at baseline in the lines without KPNA7 | 0.025 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[ZNF165]] | B | ZNF165 activity raises CBR3-AS1's level | lines that do not express ZNF165 (19) vs lines expressing it (31) | 2.17× lower at baseline in the lines without ZNF165 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ENSG00000224621, ESRP2, CNKSR1 |
| [[TOP2A]] | B | TOP2A activity lowers CBR3-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RND1]] | B | RND1 activity raises CBR3-AS1's level | lines that do not express RND1 (9) vs lines expressing it (41) | 1.86× lower at baseline in the lines without RND1 | 0.065 | ⚠ within organs, on part of the lines; also absent: EPS15-AS1; maybe low, not absent |
| [[ARHGDIB]] | B | ARHGDIB activity raises CBR3-AS1's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.56× lower at baseline in the lines without ARHGDIB | 0.077 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[TNS4]] | B | TNS4 activity raises CBR3-AS1's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 1.96× lower at baseline in the lines without TNS4 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.459). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (21.5, 17.7); signed map (7.7, 19.5). **Vector** length 82.8, 16.8% of its response variance represented; |z| ≥ 3 in 1,177 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +28.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.7 | +3.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.0 | +1.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.8 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +4.3 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -5.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.6 | -6.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.1 | -4.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | -2.0 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.0 | -0.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -1.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.7 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | CBR3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 21q22.12 — chr21:36,131,767-36,175,815 (-) |
| Ensembl biotype | lncRNA |
| Also known as | PlncRNA-1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43664](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43664) · Entrez [100506428](https://www.ncbi.nlm.nih.gov/gene/100506428) · Ensembl [ENSG00000236830](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236830)

## Data

Gene col 14105: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14105); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14105, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14105]; `tensor/DDL_lfc|DDL_z.npy` [14105]; `embed/gene_vectors.npy` [14105]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14105 or target_col == 14105). Every well: [[CBR3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CBR3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
