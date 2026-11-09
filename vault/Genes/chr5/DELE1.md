---
symbol: "DELE1"
type: "gene"
col: 1324
ensembl_id: "ENSG00000081791"
name: "DAP3 binding cell death enhancer 1"
location: "5q31.3"
module: 144
arm: "+"
pooled_cpm: 30.78
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# DELE1

*DAP3 binding cell death enhancer 1* — 5q31.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 2.53×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.616× (z -13.6, q 3e-39, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SARS2]] (+0.61, fdr 1e-05), [[MIER2]] (+0.58, fdr 1e-05), [[ATXN7L2]] (+0.58, fdr 2e-05); moves opposite to [[IPMK]] (-0.61, fdr 1e-05), [[CERT1]] (-0.60, fdr 3e-05), [[RSBN1]] (-0.56, fdr 1e-05).
> It is in [[Module 144]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1324.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 2.53×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.2 | 0.015 | 0/48 | inconsistent across doses |  |
| [[Arbutin (drug)]] 0.05 µM |  | 1.20× | +3.3 | 0.24 | 4/47 (SW480, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.26 | 3/48 (Panc 03.27, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1324.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.616×** | -13.6 | 3e-39 | 45/47 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.621×** | -13.4 | 3e-38 | 42/48 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.552×** | -11.8 | 9e-30 | 43/48 (HS-578T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.582×** | -10.7 | 1e-24 | 41/48 (NCI-H23, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.590×** | -10.5 | 1e-23 | 37/47 (BT-474, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.623×** | -9.4 | 5e-19 | 42/48 (NCI-H2030, SW1417, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.611×** | -9.2 | 4e-18 | 40/48 (NCI-H2030, H4, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.614×** | -8.8 | 1e-16 | 36/47 (H4, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.433×** | -8.7 | 3e-16 | 39/48 (NCI-H23, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.674×** | -7.1 | 7e-11 | 30/48 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.706×** | -6.9 | 2e-10 | 30/48 (PANC-1, SHP-77, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.726×** | -6.4 | 1e-08 | 24/47 (A-427, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.758×** | -5.5 | 2e-06 | 23/47 (SW48, KATO III, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.614×** | -5.1 | 2e-05 | 22/48 (HS-578T, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.624×** | -4.9 | 4e-05 | 15/48 (SK-MEL-2, SNU-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.795×** | -4.1 | 0.001 | 17/47 (HepG2/C3A, J82, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.817×** | -4.0 | 0.002 | 14/48 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1324. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 31.3 | 0 | 4 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0902× (z -14.7) |
| [[NCI-H23 (line)]] | alt | 39.2 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -14.4) |
| [[A-427 (line)]] | wt | 42.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -14.1) |
| [[AsPC-1 (line)]] | alt | 28.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -10.6) |
| [[HOP62 (line)]] | alt | 32.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 35.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -15.6) |
| [[A498 (line)]] | wt | 21.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -11.5) |
| [[AN3 CA (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.120× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~46% of this change |
| [[BT-474 (line)]] | alt | 23.1 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.249× (z -9.3) |
| [[C-33 A (line)]] | alt | 37.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 34.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -10.7) |
| [[CHP-212 (line)]] | wt | 25.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -9.6) |
| [[HS-578T (line)]] | alt | 34.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -11.0) |
| [[KATO III (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.266× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[LoVo (line)]] | wt | 44.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.606× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 31.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 34.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -9.8) |
| [[RKO (line)]] | wt | 33.0 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.303× (z -8.8) |
| [[SHP-77 (line)]] | alt | 30.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 26.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-172 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 36.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1324), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SARS2]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[MIER2]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ATXN7L2]] | +0.58 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[AP4B1]] | +0.57 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[SLC35C2]] | +0.56 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[GCN1]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[NCDN]] | +0.54 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[MAN2C1]] | +0.54 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[ARMC6]] | +0.53 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[TXLNA]] | +0.53 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[NECAB3]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[ZNF587B]] | +0.52 | +0.57 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPMK]] | -0.61 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[CERT1]] | -0.60 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[RSBN1]] | -0.56 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[ZNF654]] | -0.55 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[YY1]] | -0.54 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[ARL6IP5]] | -0.53 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[NR2F2]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[DCAF5]] | -0.52 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[TBC1D12]] | -0.51 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[PPP2R5A]] | -0.50 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[SNAPC1]] | -0.50 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[RRAGC]] | -0.49 | -0.54 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction -0.512). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.7, -32.3); signed map (-30.6, -31.8). **Vector** length 78.6, 15.3% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +2.7 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | -1.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.8 | +2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +0.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.3 | -8.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -13.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.4 | -10.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | -2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | DAP3 binding cell death enhancer 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:141,923,855-141,942,047 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DELE; previously KIAA0141 |
| Reactome | 3 pathways, smallest: Cellular response to mitochondrial stress; Cellular responses to stress; Cellular responses to stimuli |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14154](https://www.uniprot.org/uniprotkb/Q14154) (DAP3-binding cell death enhancer 1):

> Protein kinase activator that acts as a key activator of the integrated stress response (ISR) following various stresses, such as iron deficiency, mitochondrial stress or mitochondrial DNA breaks. Detects impaired protein import and processing in mitochondria, activating the ISR. May also required for the induction of death receptor-mediated apoptosis through the regulation of caspase activation.; [DAP3-binding cell death enhancer 1]: Protein kinase activator that activates the ISR in response …

**Summary**, from NCBI Gene [9812](https://www.ncbi.nlm.nih.gov/gene/9812):

> Enables protein kinase binding activity and protein serine/threonine kinase activator activity. Involved in several processes, including HRI-mediated signaling; positive regulation of mitophagy; and response to iron ion starvation. Located in mitochondrial inner membrane. Is active in cytosol and mitochondrial outer membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28969](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28969) · Entrez [9812](https://www.ncbi.nlm.nih.gov/gene/9812) · UniProt [Q14154](https://www.uniprot.org/uniprotkb/Q14154) · Ensembl [ENSG00000081791](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081791)

## Data

Gene col 1324: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1324); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1324, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1324]; `tensor/DDL_lfc|DDL_z.npy` [1324]; `embed/gene_vectors.npy` [1324]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1324 or target_col == 1324). Every well: [[DELE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DELE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
