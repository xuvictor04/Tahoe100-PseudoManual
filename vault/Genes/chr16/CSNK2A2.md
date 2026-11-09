---
symbol: "CSNK2A2"
type: "gene"
col: 965
ensembl_id: "ENSG00000070770"
name: "casein kinase 2 alpha 2"
location: "16q21"
module: 2
arm: "+"
pooled_cpm: 86.7
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CSNK2A2

*casein kinase 2 alpha 2* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.28× (z +26.3, q 0e+00, up in 45 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.44× (z +11.3, q 6e-27, up in 36 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.197×, SK-MEL-2 0.402×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-1 0.459×, AN3 CA 0.340×; ⚠ cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW48 0.179×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VTI1B]] (+0.61, fdr 1e-05), [[UBE2F]] (+0.59, fdr 1e-05), [[EIF3L]] (+0.58, fdr 3e-05); moves opposite to [[HCP5]] (-0.52, fdr 3e-05), [[HEXIM1]] (-0.50, fdr 3e-05), [[CCNL1]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 965.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.28×** | +26.3 | 0e+00 | 45/50 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +11.3 | 6e-27 | 36/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +10.6 | 4e-24 | 37/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +9.3 | 1e-18 | 35/48 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.76×** | +9.1 | 1e-17 | 33/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +8.5 | 1e-15 | 34/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +8.4 | 5e-15 | 35/45 (MIA PaCa-2, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +7.9 | 2e-13 | 26/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +7.8 | 3e-13 | 30/48 (HOP62, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +7.8 | 3e-13 | 34/48 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +7.3 | 1e-11 | 32/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.26×** | +7.0 | 2e-10 | 25/48 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.25×** | +6.9 | 2e-10 | 28/48 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Rimonabant (Hydrochloride) (drug)]] 0.05 µM | ⚠ unreliable plate only; position correction uncertain | **1.25×** | +6.8 | 4e-10 | 36/49 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.25×** | +6.8 | 5e-10 | 25/48 (HEC-1-A, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.22×** | +6.1 | 4e-08 | 24/48 (HEC-1-A, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +6.1 | 5e-08 | 25/48 (A498, HOP62, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.30×** | +4.2 | 7e-04 | 17/48 (A498, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.002 | 15/48 (SW 900, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.002 | 16/48 (NCI-H460, NCI-H2030, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 965.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.197×, SK-MEL-2 0.402×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-1 0.459×, AN3 CA 0.340×; ⚠ cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW48 0.179×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.869× | -6.2 | 3e-07 | 13/48 (SHP-77, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.854× | -4.9 | 2e-04 | 20/49 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.898× | -3.3 | 0.11 | 4/48 (HEC-1-A, Panc 03.27, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.891× | -3.3 | 0.11 | 13/47 (A-427, C-33 A, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.896× | -3.3 | 0.11 | 10/47 (HepG2/C3A, A549, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.930× | -3.2 | 0.12 | 13/49 (AsPC-1, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 965. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 120 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 3.53× (z +12.2) | — |
| [[HOP62 (line)]] | alt | 89.1 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.74× (z +8.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.73× (z +8.8) | — |
| [[LoVo (line)]] | wt | 94.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.13× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.75× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 127 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.65× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 131 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +9.4) | — |
| [[A-427 (line)]] | wt | 80.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.461× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 89.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +11.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[AN3 CA (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -11.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[AsPC-1 (line)]] | alt | 58.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -8.9) ⚠ cell-cycle shift, explains ~8% of this change |
| [[NCI-H2030 (line)]] | alt | 124 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.52× (z +8.8) ⚠ cell-cycle shift, explains ~8% of this change | — |
| [[NCI-H23 (line)]] | alt | 71.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 55.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.76× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 88.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.402× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -11.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW48 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change |
| [[A-172 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 99.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 66.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 73.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 111 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 115 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 96.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 81.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 139 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 96.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 965), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VTI1B]] | +0.61 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[UBE2F]] | +0.59 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[EIF3L]] | +0.58 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[GLB1]] | +0.58 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[HSF1]] | +0.55 | +0.54 / +0.56 | both halves | 1e-05 | pathway: Autophagy |
| [[COMMD9]] | +0.55 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[VPS13D]] | +0.55 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[ZNF496]] | +0.55 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[RAB5C]] | +0.54 | +0.49 / +0.46 | both halves | 3e-05 | pathway: Respiratory Syncytial Virus Infection Pathway |
| [[AP3M1]] | +0.53 | +0.49 / +0.59 | both halves | 1e-05 | pathway: Chaperonin-mediated protein folding |
| [[AP2A2]] | +0.53 | +0.56 / +0.41 | both halves | 4e-05 | pathway: L1CAM interactions |
| [[KIF1C]] | +0.53 | +0.51 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCP5]] | -0.52 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[HEXIM1]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 | STRING 462 |
| [[CCNL1]] | -0.49 | -0.46 / -0.40 | both halves | 4e-05 | STRING 476 |
| [[NSUN6]] | -0.48 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[PAN2]] | -0.47 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[LPXN]] | -0.47 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[NR1D1]] | -0.47 | -0.30 / -0.47 | both halves | 2e-04 | pathway: Circadian clock |
| [[PLEKHA8P1]] | -0.47 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[IRF1]] | -0.47 | -0.42 / -0.45 | both halves | 4e-05 | pathway: Co-inhibition by PD-1 |
| [[SLC6A7]] | -0.47 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[LINC02362]] | -0.46 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[MAFF]] | -0.46 | -0.31 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.412). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-7.5, -26.4); signed map (-46.1, -13.5). **Vector** length 86.7, 18.4% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.5 | +9.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.4 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.4 | +4.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +7.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +6.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.5 | +3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +6.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.4 | +2.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.3 | -4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -3.3 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | -1.5 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | casein kinase 2 alpha 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:58,157,907-58,198,106 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CSNK2A1, CK2alpha' |
| Gene groups (HGNC) | Casein kinase 2 alpha family |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 57 pathways, smallest: WNT mediated activation of DVL; Condensation of Prometaphase Chromosomes; Receptor Mediated Mitophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [P19784](https://www.uniprot.org/uniprotkb/P19784) (Casein kinase II subunit alpha'):

> Catalytic subunit of a constitutively active serine/threonine-protein kinase complex that phosphorylates a large number of substrates containing acidic residues C-terminal to the phosphorylated serine or threonine. Regulates numerous cellular processes, such as cell cycle progression, apoptosis and transcription, as well as viral infection. May act as a regulatory node which integrates and coordinates numerous signals leading to an appropriate cellular response. During mitosis, functions as a …

**Summary**, from NCBI Gene [1459](https://www.ncbi.nlm.nih.gov/gene/1459):

> This gene encodes the alpha', or alpha 2, catalytic subunit of the protein kinase enzyme, casein kinase 2 (CK2). Casein kinase 2 is a serine/threonine protein kinase that phosphorylates acidic proteins such as casein. It is involved in various cellular processes, including cell cycle control, apoptosis, and circadian rhythms. This heterotetrameric kinase includes two catalytic subunits, either alpha or alpha', and two regulatory beta subunits. The closely related gene paralog encoding the …

**Accessions** — [HGNC:2459](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2459) · Entrez [1459](https://www.ncbi.nlm.nih.gov/gene/1459) · UniProt [P19784](https://www.uniprot.org/uniprotkb/P19784) · Ensembl [ENSG00000070770](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070770)

## Data

Gene col 965: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 965); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 965, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 965]; `tensor/DDL_lfc|DDL_z.npy` [965]; `embed/gene_vectors.npy` [965]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 965 or target_col == 965). Every well: [[CSNK2A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSNK2A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
