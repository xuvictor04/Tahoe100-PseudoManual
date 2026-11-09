---
symbol: "ALG13"
type: "gene"
col: 2187
ensembl_id: "ENSG00000101901"
name: "ALG13 UDP-N-acetylglucosaminyltransferase subunit"
location: "Xq23"
module: 30
arm: "-"
pooled_cpm: 109.61
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# ALG13

*ALG13 UDP-N-acetylglucosaminyltransferase subunit* — Xq23

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 1.97×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 2.35×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 2.25×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.511× (z -10.8, q 2e-24, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC30A9]] (+0.64, fdr 1e-05), [[DELEC1]] (+0.63, fdr 2e-05), [[ERCC6L2]] (+0.63, fdr 3e-05); moves opposite to [[SUFU]] (-0.64, fdr 3e-05), [[TMEM185A]] (-0.63, fdr 3e-05), [[SLC9A6]] (-0.61, fdr 4e-05).
> It sits in the **-** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2187.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 1.97×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 2.35×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 2.25×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Demeclocycline (drug)]] 5 µM |  | 1.15× | +3.1 | 0.95 | 9/48 (HT-29, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2187.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.511×** | -10.8 | 2e-24 | 47/48 (LOX-IMVI, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.529×** | -10.3 | 3e-22 | 48/48 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.559×** | -9.4 | 1e-18 | 48/48 (RKO, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.652×** | -6.6 | 4e-09 | 34/47 (MIA PaCa-2, HCT15, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.673×** | -6.4 | 2e-08 | 42/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.695×** | -5.9 | 4e-07 | 40/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **0.724×** | -5.2 | 1e-05 | 34/48 (AsPC-1, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **0.803×** | -5.0 | 4e-05 | 27/48 (SK-MEL-2, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.738×** | -4.9 | 5e-05 | 35/48 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.728×** | -4.7 | 1e-04 | 25/45 (HCT15, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **0.738×** | -4.7 | 1e-04 | 29/49 (NCI-H23, CHP-212, …) | all doses, flat | composition shift |
| [[Radotinib (drug)]] 5 µM |  | **0.827×** | -4.3 | 7e-04 | 27/48 (NCI-H23, RKO, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.611×** | -4.2 | 0.001 | 29/49 (hTERT-HPNE, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.844× | -3.9 | 0.004 | 18/48 (SNU-1, SHP-77, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.794×** | -3.5 | 0.016 | 23/48 (CFPAC-1, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2187. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 164 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.367× (z -8.9) |
| [[LoVo (line)]] | wt | 105 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.385× (z -11.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.429× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 135 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.348× (z -12.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.378× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 202 | 1 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.254× (z -14.1) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 159 | 2 (2 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.433× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.455× (z -8.8) |
| [[H4 (line)]] | wt | 169 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.327× (z -10.1) |
| [[A549 (line)]] | wt | 129 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.438× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 111 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 145 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.391× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H460 (line)]] | wt | 135 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.444× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.497× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 76.9 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -11.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.359× (z -10.0) |
| [[RKO (line)]] | wt | 111 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.342× (z -10.2) |
| [[SNU-1 (line)]] | wt | 155 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.408× (z -8.6) |
| [[SW480 (line)]] | alt | 145 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.423× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 82.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.567× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 82.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.418× (z -9.0) ⚠ transcription drop; cell-cycle shift, explains ~34% of this change |
| [[CFPAC-1 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.427× (z -8.7) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 94.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[COLO 205 (line)]] | alt | 65.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.336× (z -9.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 136 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.383× (z -9.5) |
| [[LS 180 (line)]] | wt | 98.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.404× (z -8.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 88.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.399× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 188 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[PANC-1 (line)]] | alt | 165 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.502× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 116 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 67.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 94.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 94.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 111 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2187), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC30A9]] | +0.64 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[DELEC1]] | +0.63 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[ERCC6L2]] | +0.63 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[SECISBP2]] | +0.61 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[HOMER1]] | +0.60 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[MSRA]] | +0.60 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[GLIPR1-AS1]] | +0.57 | +0.38 / +0.43 | both halves | 6e-05 |  |
| [[KRR1]] | +0.57 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[CSTF3]] | +0.57 | +0.40 / +0.39 | both halves | 5e-05 |  |
| [[DESI1]] | +0.57 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[MIATNB]] | +0.57 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[CCDC200]] | +0.57 | +0.34 / +0.51 | both halves | 1e-04 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUFU]] | -0.64 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[TMEM185A]] | -0.63 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[SLC9A6]] | -0.61 | -0.47 / -0.42 | both halves | 4e-05 | STRING 428 |
| [[PHAF1]] | -0.60 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[TSPAN33]] | -0.60 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[GNPTAB]] | -0.60 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[CDC14B]] | -0.59 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[XKR8]] | -0.58 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[TLE1]] | -0.58 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[SAC3D1]] | -0.58 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[OTX1]] | -0.57 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[THRA]] | -0.57 | -0.43 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **-** arm (projection on the module's main direction -0.629). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.8, -5.7); signed map (18.1, -2.2). **Vector** length 100, 29.2% of its response variance represented; |z| ≥ 3 in 969 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | +6.4 | -4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.4 | -2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | -1.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | -1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.6 | +0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | -1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.3 | +0.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.1 | +1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +2.3 |
| fall | [[Radotinib (drug)]] 5 µM |  | -4.8 | -4.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.6 | -6.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.0 | -10.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.6 | -4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.4 | -5.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -1.7 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.3 | -2.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | ALG13 UDP-N-acetylglucosaminyltransferase subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq23 — chrX:111,665,811-111,760,649 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MDS031, YGL047W, FLJ23018, TDRD13, CDG1S; previously GLT28D1, CXorf45 |
| Gene groups (HGNC) | UDP-N-acetylglucosaminyltransferase subunits; OTU domain containing; Tudor domain containing |
| Reactome | 5 pathways, smallest: Diseases associated with N-glycosylation of proteins; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein; Diseases of glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP73](https://www.uniprot.org/uniprotkb/Q9NP73) (UDP-N-acetylglucosamine transferase subunit ALG13):

> Catalytic subunit of the UDP-N-acetylglucosamine transferase complex that operates in the biosynthetic pathway of dolichol-linked oligosaccharides, the glycan precursors employed in protein asparagine (N)-glycosylation. The assembly of dolichol-linked oligosaccharides begins on the cytosolic side of the endoplasmic reticulum membrane and finishes in its lumen. The sequential addition of sugars to dolichol pyrophosphate produces dolichol-linked oligosaccharides containing fourteen sugars, …

**Summary**, from NCBI Gene [79868](https://www.ncbi.nlm.nih.gov/gene/79868):

> The protein encoded by this gene is a subunit of a bipartite UDP-N-acetylglucosamine transferase. It heterodimerizes with asparagine-linked glycosylation 14 homolog to form a functional UDP-GlcNAc glycosyltransferase that catalyzes the second sugar addition of the highly conserved oligosaccharide precursor in endoplasmic reticulum N-linked glycosylation. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2009]

**Accessions** — [HGNC:30881](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30881) · Entrez [79868](https://www.ncbi.nlm.nih.gov/gene/79868) · UniProt [Q9NP73](https://www.uniprot.org/uniprotkb/Q9NP73) · Ensembl [ENSG00000101901](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101901)

## Data

Gene col 2187: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2187); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2187, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2187]; `tensor/DDL_lfc|DDL_z.npy` [2187]; `embed/gene_vectors.npy` [2187]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2187 or target_col == 2187). Every well: [[ALG13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALG13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
