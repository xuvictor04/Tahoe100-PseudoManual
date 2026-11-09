---
symbol: "ENOX2"
type: "gene"
col: 9164
ensembl_id: "ENSG00000165675"
name: "ecto-NOX disulfide-thiol exchanger 2"
location: "Xq26.1"
module: 5
arm: "+"
pooled_cpm: 50.47
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ENOX2

*ecto-NOX disulfide-thiol exchanger 2* — Xq26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.54× (z +7.4, q 9e-11, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.441× (z -9.9, q 3e-20, down in 38 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.213× (z -9.7, q 6e-20, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPOPL-DT]] (+0.78, fdr 7e-06), [[DPH5-DT]] (+0.75, fdr 1e-05), [[AVEN]] (+0.72, fdr 1e-05); moves opposite to [[RAB3A]] (-0.80, fdr 7e-06), [[AHDC1]] (-0.72, fdr 1e-05), [[FOXO6]] (-0.70, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[HMGA1P4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9164.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +7.4 | 9e-11 | 44/48 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +7.3 | 1e-10 | 36/47 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.1 | 3e-10 | 32/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.7 | 4e-04 | 28/48 (HT-29, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.48×** | +4.5 | 7e-04 | 30/48 (NCI-H2347, SW480, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.41×** | +4.2 | 0.003 | 24/47 (NCI-H460, SW 900, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.31×** | +3.3 | 0.084 | 21/47 (HOP62, CFPAC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.29× | +3.1 | 0.14 | 14/47 (MIA PaCa-2, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9164.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.441×** | -9.9 | 3e-20 | 38/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.213×** | -9.7 | 6e-20 | 38/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.453×** | -9.5 | 3e-19 | 38/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.227×** | -9.3 | 2e-18 | 46/49 (SW480, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.597×** | -6.2 | 6e-08 | 31/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.655×** | -5.1 | 3e-05 | 27/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.709×** | -4.1 | 0.003 | 27/48 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.523×** | -4.1 | 0.003 | 19/34 (HEC-1-A, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.704×** | -4.1 | 0.003 | 25/47 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.721×** | -3.8 | 0.009 | 28/48 (HT-29, LOX-IMVI, …) | top dose only | plate-row cell shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.740×** | -3.5 | 0.025 | 22/48 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.820×** | -3.4 | 0.033 | 23/47 (SW1417, A549, …) | top dose only | composition shift |
| [[Fumaric acid (drug)]] 5 µM |  | **0.751×** | -3.3 | 0.040 | 24/48 (C-33 A, HT-29, …) | top dose only | plate-row cell shift |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.742×** | -3.1 | 0.068 | 17/48 (A-172, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9164. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 113 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.103× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 63.2 | 0 | 8 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -13.0) |
| [[KATO III (line)]] | alt | 99.7 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -14.5) |
| [[SW480 (line)]] | alt | 96.4 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -17.7) |
| [[A-427 (line)]] | wt | 59.6 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -9.7) |
| [[LoVo (line)]] | wt | 53.2 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.188× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.290× (z -12.1) |
| [[PANC-1 (line)]] | alt | 66.9 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.110× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.120× (z -19.5) |
| [[C-33 A (line)]] | alt | 64.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0603× (z -10.3) |
| [[HT-29 (line)]] | alt | 66.2 | 2 | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.224× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.243× (z -12.2) |
| [[SW1417 (line)]] | alt | 71.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.315× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 52.9 | 0 | 3 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0680× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 49.5 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +12.6) | [[PH-797804 (drug)]] 5 µM 0.0990× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 57.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.158× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.299× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 45.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +8.6) | [[Lonafarnib (drug)]] 5 µM 0.0902× (z -10.8) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 35.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -9.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 32.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.221× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 56.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +8.8) | [[PH-797804 (drug)]] 5 µM 0.114× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 85.9 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.110× (z -9.1) |
| [[A-172 (line)]] | wt | 13.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.118× (z -10.9) |
| [[A498 (line)]] | wt | 50.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 50.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 21.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +9.3) | — |
| [[COLO 205 (line)]] | alt | 57.9 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0703× (z -10.1) |
| [[HCT15 (line)]] | alt | 44.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.168× (z -9.9) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 39.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0564× (z -10.0) |
| [[J82 (line)]] | alt | 61.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -11.3) |
| [[RKO (line)]] | wt | 59.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.136× (z -13.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 33.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -9.7) |
| [[AN3 CA (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9164), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPOPL-DT]] | +0.78 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[DPH5-DT]] | +0.75 | +0.82 / +0.51 | both halves | 1e-05 |  |
| [[AVEN]] | +0.72 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[PRDM5]] | +0.71 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[DOCK1]] | +0.70 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ATR]] | +0.68 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[PRMT3]] | +0.68 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[EPM2A]] | +0.67 | +0.72 / +0.36 | both halves | 1e-04 |  |
| [[CPSF2]] | +0.67 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[DNAJC11]] | +0.67 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[PTPRG]] | +0.67 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[ST7L]] | +0.66 | +0.73 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB3A]] | -0.80 | -0.73 / -0.61 | both halves | 7e-06 |  |
| [[AHDC1]] | -0.72 | -0.71 / -0.54 | both halves | 1e-05 |  |
| [[FOXO6]] | -0.70 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[SLC25A23]] | -0.68 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[MAST1]] | -0.67 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[PLCD1]] | -0.67 | -0.66 / -0.46 | both halves | 3e-05 |  |
| [[DBP]] | -0.67 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[PNKD]] | -0.66 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[TMEM14A]] | -0.66 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.66 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[CAT]] | -0.65 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[ABCB9]] | -0.65 | -0.61 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ENOX2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FAR2]] | B | FAR2 activity lowers ENOX2's level | lines that do not express FAR2 (19) vs lines expressing it (31) | 1.38× higher at baseline in the lines without FAR2 | 0.053 | ⚠ within organs, on part of the lines; also absent: CCN3, MIR155HG, LINC02605; maybe low, not absent |
| [[TOP2B]] | B | TOP2B activity lowers ENOX2's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGA1P4]] | C | ENOX2's natural level strengthens HMGA1P4's drug response | ENOX2's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.02; direction clear | 0.012 | ⚠ tissue can mimic it; precision caveat |
| cells under [[Procainamide (hydrochloride) (drug)]] 0.5 µM | C | ENOX2's natural level lowers the cells' numbers under Procainamide (hydrochloride) 0.5 µM (makes them more sensitive) | ENOX2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.71 | 0.250 over the table, 0.019 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Doxycycline (monohydrate) (drug)]] 5 µM | C | ENOX2's natural level lowers the cells' numbers under Doxycycline (monohydrate) 5 µM (makes them more sensitive) | ENOX2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.038 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Hydroxyurea (drug)]] 0.5 µM | C | ENOX2's natural level lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | ENOX2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63 | 0.417 over the table, 0.089 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | ENOX2's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | ENOX2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.61 | 0.437 over the table, 0.085 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | ENOX2's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | ENOX2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.57 | 0.510 over the table, 0.088 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.642). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (7.8, -7.1); signed map (22.3, -28.2). **Vector** length 103, 30.3% of its response variance represented; |z| ≥ 3 in 979 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.3 | +7.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.5 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.3 | +2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +7.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.7 | +4.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.2 | -0.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | -0.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.1 | +0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.8 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.5 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -9.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ecto-NOX disulfide-thiol exchanger 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.1 — chrX:130,622,325-130,903,234 (-) |
| Ensembl biotype | protein_coding |
| Also known as | APK1, tNOX; previously COVA1 |
| Gene groups (HGNC) | RNA binding motif containing; Ecto-NOX disulfide-thiol exchanger family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16206](https://www.uniprot.org/uniprotkb/Q16206) (Ecto-NOX disulfide-thiol exchanger 2):

> May be involved in cell growth. Probably acts as a terminal oxidase of plasma electron transport from cytosolic NAD(P)H via hydroquinones to acceptors at the cell surface. Hydroquinone oxidase activity alternates with a protein disulfide-thiol interchange/oxidoreductase activity which may control physical membrane displacements associated with vesicle budding or cell enlargement. The activities oscillate with a period length of 22 minutes and play a role in control of the ultradian cellular …

**Summary**, from NCBI Gene [10495](https://www.ncbi.nlm.nih.gov/gene/10495):

> This gene is a tumor-specific member of the ECTO-NOX family of genes that encode cell surface NADH oxidases. The encoded protein has two enzymatic activities: catalysis of hydroquinone or NADH oxidation, and protein disulfide interchange. The protein also displays prion-like properties. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:2259](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2259) · Entrez [10495](https://www.ncbi.nlm.nih.gov/gene/10495) · UniProt [Q16206](https://www.uniprot.org/uniprotkb/Q16206) · Ensembl [ENSG00000165675](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165675)

## Data

Gene col 9164: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9164); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9164, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9164]; `tensor/DDL_lfc|DDL_z.npy` [9164]; `embed/gene_vectors.npy` [9164]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9164 or target_col == 9164). Every well: [[ENOX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENOX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
