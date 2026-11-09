---
symbol: "AGGF1"
type: "gene"
col: 8912
ensembl_id: "ENSG00000164252"
name: "angiogenic factor with G-patch and FHA domains 1"
location: "5q13.3"
module: 11
arm: "+"
pooled_cpm: 44.5
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# AGGF1

*angiogenic factor with G-patch and FHA domains 1* — 5q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 1.50× (z +6.6, q 2e-08, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.315× (z -18.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHAX]] (+0.78, fdr 7e-06), [[KLHL9]] (+0.78, fdr 7e-06), [[EBAG9]] (+0.78, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8912.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +6.6 | 2e-08 | 36/48 (NCI-H2347, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +5.2 | 7e-05 | 24/48 (NCI-H1573, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.9 | 2e-04 | 29/48 (NCI-H1792, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.2 | 0.004 | 20/48 (CFPAC-1, A549, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.022 | 19/48 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.061 | 16/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.16× | +3.3 | 0.068 | 8/48 (PANC-1, HS-578T, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 1.15× | +3.3 | 0.068 | 12/48 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.070 | 15/48 (NCI-H2347, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.070 | 17/47 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.071 | 19/48 (KATO III, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Busulfan (drug)]] 0.05 µM |  | 1.21× | +3.1 | 0.11 | 12/48 (NCI-H2347, NCI-H1573, …) | inconsistent across doses |  |
| [[Lapatinib ditosylate (drug)]] 0.05 µM |  | 1.22× | +3.0 | 0.11 | 15/48 (SW480, HOP62, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8912.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.315×** | -18.6 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.332×** | -17.7 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.355×** | -16.7 | 0e+00 | 45/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.459×** | -12.5 | 9e-34 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.635×** | -10.3 | 1e-22 | 41/48 (SW 900, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.646×** | -6.7 | 2e-09 | 29/47 (C-33 A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.663×** | -6.6 | 4e-09 | 35/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.687×** | -6.0 | 1e-07 | 31/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.758×** | -4.4 | 6e-04 | 25/48 (HCT15, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.759×** | -4.2 | 0.002 | 22/48 (PANC-1, NCI-H661, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.620×** | -4.0 | 0.003 | 24/49 (PANC-1, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.782×** | -3.9 | 0.004 | 22/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.650×** | -3.6 | 0.013 | 21/48 (C32, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.811×** | -3.3 | 0.034 | 18/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Folic acid (drug)]] 5 µM |  | 0.872× | -3.1 | 0.084 | 14/48 (SW 1271, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8912. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 50.7 | 0 | 10 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.202× (z -17.6) |
| [[LoVo (line)]] | wt | 48.6 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.299× (z -12.6) |
| [[PANC-1 (line)]] | alt | 54.4 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.166× (z -22.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -21.0) |
| [[J82 (line)]] | alt | 48.1 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -14.6) |
| [[KATO III (line)]] | alt | 50.5 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -16.0) |
| [[SW 900 (line)]] | alt | 36.6 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -11.0) |
| [[SW480 (line)]] | alt | 41.8 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.173× (z -19.2) |
| [[A-427 (line)]] | wt | 67.9 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.292× (z -12.9) |
| [[MIA PaCa-2 (line)]] | alt | 72.0 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.295× (z -12.9) |
| [[NCI-H1573 (line)]] | alt | 62.0 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.339× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 49.9 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.307× (z -10.5) |
| [[SNU-423 (line)]] | alt | 47.7 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.304× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -10.3) |
| [[A-172 (line)]] | wt | 58.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.350× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -10.7) |
| [[COLO 205 (line)]] | alt | 45.6 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.269× (z -9.8) |
| [[HCT15 (line)]] | alt | 49.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -12.3) |
| [[HOP62 (line)]] | alt | 39.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.282× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.305× (z -10.1) |
| [[C-33 A (line)]] | alt | 49.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -15.7) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 36.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.308× (z -8.9) |
| [[HS-578T (line)]] | alt | 35.2 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.288× (z -9.7) |
| [[HT-29 (line)]] | alt | 31.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 40.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.234× (z -12.2) |
| [[LS 180 (line)]] | wt | 40.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.307× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 35.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -10.6) |
| [[SW1417 (line)]] | alt | 26.8 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.274× (z -9.6) |
| [[AN3 CA (line)]] | alt | 59.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 21.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.197× (z -10.1) |
| [[BT-474 (line)]] | alt | 20.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.206× (z -8.5) |
| [[C32 (line)]] | wt | 40.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.314× (z -9.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 37.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0916× (z -10.1) ⚠ toxic |
| [[H4 (line)]] | wt | 47.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.189× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 35.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 32.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.326× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 30.9 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.302× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 42.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.293× (z -10.3) |
| [[RKO (line)]] | wt | 36.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.199× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~1% of this change |
| [[A498 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8912), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHAX]] | +0.78 | +0.80 / +0.79 | both halves | 7e-06 |  |
| [[KLHL9]] | +0.78 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.78 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[REXO4]] | +0.76 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[ASNSD1]] | +0.74 | +0.82 / +0.69 | both halves | 7e-06 |  |
| [[RBAK]] | +0.73 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[MRPS18B]] | +0.72 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.72 | +0.72 / +0.79 | both halves | 7e-06 |  |
| [[ZNF510]] | +0.71 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[GSPT2]] | +0.71 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[ZNF23]] | +0.71 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.71 | +0.78 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.698). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-32.2, 3.7); signed map (-0.5, -22.0). **Vector** length 96.1, 25.7% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.0 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.0 | +6.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | +2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.8 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | -3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +0.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.4 | +0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.4 | -10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.9 | +0.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.6 | -1.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.4 | +1.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.2 | -16.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | +0.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.9 | +0.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.6 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | angiogenic factor with G-patch and FHA domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.3 — chr5:77,029,251-77,065,234 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VG5Q, HSU84971, FLJ10283, GPATC7, GPATCH7 |
| Gene groups (HGNC) | G-patch domain containing |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 3 pathways, smallest: Signaling by BRAF and RAF1 fusions; Oncogenic MAPK signaling; Diseases of signal transduction by growth factor receptors and second messengers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N302](https://www.uniprot.org/uniprotkb/Q8N302) (Angiogenic factor with G patch and FHA domains 1):

> Promotes angiogenesis and the proliferation of endothelial cells. Able to bind to endothelial cells and promote cell proliferation, suggesting that it may act in an autocrine fashion.

**Summary**, from NCBI Gene [55109](https://www.ncbi.nlm.nih.gov/gene/55109):

> This gene encodes an angiogenic factor that promotes proliferation of endothelial cells. Mutations in this gene are associated with a susceptibility to Klippel-Trenaunay syndrome. Pseudogenes of this gene are found on chromosomes 3, 4, 10 and 16.[provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:24684](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24684) · Entrez [55109](https://www.ncbi.nlm.nih.gov/gene/55109) · UniProt [Q8N302](https://www.uniprot.org/uniprotkb/Q8N302) · Ensembl [ENSG00000164252](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164252)

## Data

Gene col 8912: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8912); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8912, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8912]; `tensor/DDL_lfc|DDL_z.npy` [8912]; `embed/gene_vectors.npy` [8912]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8912 or target_col == 8912). Every well: [[AGGF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGGF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
