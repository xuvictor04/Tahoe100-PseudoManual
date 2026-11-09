---
symbol: "TRNT1"
type: "gene"
col: 1028
ensembl_id: "ENSG00000072756"
name: "tRNA nucleotidyl transferase 1"
location: "3p26.2"
module: 5
arm: "+"
pooled_cpm: 34.16
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TRNT1

*tRNA nucleotidyl transferase 1* — 3p26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.79× (z +12.2, q 1e-31, up in 35 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +11.1, q 5e-26, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.786× (z -7.4, q 6e-11, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALG8]] (+0.79, fdr 7e-06), [[RNASEH1]] (+0.76, fdr 7e-06), [[WDR4]] (+0.75, fdr 7e-06); moves opposite to [[KBTBD3]] (-0.65, fdr 1e-05), [[TTBK2]] (-0.64, fdr 1e-05), [[PLEKHH3]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1028.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +12.2 | 1e-31 | 35/47 (RKO, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +11.1 | 5e-26 | 39/48 (AsPC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +8.8 | 3e-16 | 38/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +7.5 | 1e-11 | 30/48 (SW480, BT-474, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +7.4 | 1e-11 | 28/43 (NCI-H1792, RKO, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +7.4 | 1e-11 | 29/47 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +6.5 | 6e-09 | 26/48 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.30×** | +5.6 | 2e-06 | 22/48 (SW480, CFPAC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.30×** | +5.6 | 2e-06 | 22/38 (LS 180, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +5.3 | 7e-06 | 24/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +5.0 | 3e-05 | 24/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.8 | 8e-05 | 18/48 (HOP62, NCI-H2030, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.7 | 1e-04 | 16/34 (SW 900, A549, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.22×** | +4.3 | 6e-04 | 21/46 (NCI-H23, AsPC-1, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.004 | 15/47 (MIA PaCa-2, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.008 | 16/47 (NCI-H460, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.014 | 13/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.018 | 9/48 (NCI-H1792, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1028.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.786×** | -7.4 | 6e-11 | 27/48 (HEC-1-A, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.777×** | -5.5 | 1e-05 | 20/48 (RKO, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.806×** | -4.7 | 5e-04 | 22/48 (HEC-1-A, BT-474, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.846× | -4.3 | 0.002 | 17/48 (LoVo, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.824×** | -4.2 | 0.003 | 18/48 (SW 1088, NCI-H460, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.825×** | -4.1 | 0.005 | 18/47 (J82, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -3.8 | 0.013 | 13/48 (RKO, PANC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.870× | -3.7 | 0.013 | 8/48 (HEC-1-A, C-33 A, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.853× | -3.6 | 0.017 | 16/48 (LOX-IMVI, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.893× | -3.5 | 0.028 | 9/48 (RKO, A-427, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.857× | -3.4 | 0.038 | 13/48 (PANC-1, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1028. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 60.6 | 1 (1 ⚠) | 3 (2 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.60× (z +9.3) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.395× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 26.4 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +12.8) | — |
| [[A-427 (line)]] | wt | 44.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 30.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HepG2_C3A (line)]] | wt | 27.6 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0710× (z -14.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 23.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 28.6 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +8.9) | — |
| [[LoVo (line)]] | wt | 38.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.382× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[NCI-H1792 (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -15.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 47.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H2347 (line)]] | alt | 30.3 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.82× (z +8.5) ⚠ cell-cycle shift, explains ~72% of this change | — |
| [[NCI-H460 (line)]] | wt | 27.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 51.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.232× (z -9.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 40.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.246× (z -9.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW480 (line)]] | alt | 44.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1028), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG8]] | +0.79 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[RNASEH1]] | +0.76 | +0.65 / +0.73 | both halves | 7e-06 | STRING 521 |
| [[WDR4]] | +0.75 | +0.77 / +0.73 | both halves | 7e-06 | pathway: tRNA processing |
| [[ARMC6]] | +0.74 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[PIGW]] | +0.73 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[HCG18]] | +0.71 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[MSANTD2]] | +0.71 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[PUS1]] | +0.71 | +0.75 / +0.69 | both halves | 7e-06 | pathway: tRNA processing; STRING 653 |
| [[GNL3L]] | +0.71 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[TIMM23B-AGAP6]] | +0.69 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[NAF1]] | +0.68 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[ZNF587B]] | +0.68 | +0.55 / +0.72 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD3]] | -0.65 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[TTBK2]] | -0.64 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.62 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ALAD]] | -0.62 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[KMT2A]] | -0.61 | -0.56 / -0.69 | both halves | 1e-05 |  |
| [[HDAC5]] | -0.60 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[DBP]] | -0.60 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[RNF114]] | -0.59 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[KMT2C]] | -0.59 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[UBE2B]] | -0.59 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[TBC1D17]] | -0.59 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[OSBPL9]] | -0.59 | -0.44 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises TRNT1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[TOP2A]] | B | TOP2A activity lowers TRNT1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.771). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.7, -33.8); signed map (-0.9, -47.6). **Vector** length 105, 24.2% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.52 to 13); *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.59 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +11.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +8.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.4 | +12.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.3 | +3.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +3.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -7.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.2 | -5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.9 | -1.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -3.6 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | tRNA nucleotidyl transferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p26.2 — chr3:3,126,933-3,153,435 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MtCCA, CGI-47, CCA1 |
| Reactome | 4 pathways, smallest: tRNA processing in the mitochondrion; tRNA processing in the nucleus; tRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96Q11](https://www.uniprot.org/uniprotkb/Q96Q11) (CCA tRNA nucleotidyltransferase 1, mitochondrial):

> Nucleotidyltransferase that catalyzes the addition and repair of the essential 3'-terminal CCA sequence in tRNAs, which is necessary for the attachment of amino acids to the 3' terminus of tRNA molecules, using CTP and ATP as substrates. tRNA 3'-terminal CCA addition is required both for tRNA processing and repair. Promotes tRNA repair and recycling downstream of the ribosome-associated quality control (RQC) pathway by mediating addition of the tRNA 3'-terminal CCA following cleavage by ANKZF1 …

**Summary**, from NCBI Gene [51095](https://www.ncbi.nlm.nih.gov/gene/51095):

> The protein encoded by this gene is a CCA-adding enzyme which belongs to the tRNA nucleotidyltransferase/poly(A) polymerase family. This essential enzyme functions by catalyzing the addition of the conserved nucleotide triplet CCA to the 3' terminus of tRNA molecules. Mutations in this gene result in sideroblastic anemia with B-cell immunodeficiency, periodic fevers, and developmental delay. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:17341](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17341) · Entrez [51095](https://www.ncbi.nlm.nih.gov/gene/51095) · UniProt [Q96Q11](https://www.uniprot.org/uniprotkb/Q96Q11) · Ensembl [ENSG00000072756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072756)

## Data

Gene col 1028: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1028); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1028, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1028]; `tensor/DDL_lfc|DDL_z.npy` [1028]; `embed/gene_vectors.npy` [1028]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1028 or target_col == 1028). Every well: [[TRNT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRNT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
