---
symbol: "PFN1"
type: "gene"
col: 2960
ensembl_id: "ENSG00000108518"
name: "profilin 1"
location: "17p13.2"
module: 171
arm: "-"
pooled_cpm: 209.48
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# PFN1

*profilin 1* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.03× (z +9.4, q 2e-18, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 15 lines (HT-29 6.35×, NCI-H460 6.07×, COLO 205 8.54×, NCI-H1792 7.09×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.567× (z -3.8, q 0.080, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYL12A]] (+0.66, fdr 1e-05), [[POLR2L]] (+0.63, fdr 1e-05), [[GOLT1A]] (+0.61, fdr 5e-05); moves opposite to [[RTCA]] (-0.63, fdr 2e-05), [[ALDH2]] (-0.60, fdr 3e-05), [[ABHD4]] (-0.60, fdr 3e-05).
> It sits in the **-** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ALDH2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2960.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 15 lines (HT-29 6.35×, NCI-H460 6.07×, COLO 205 8.54×, NCI-H1792 7.09×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **4.03×** | +9.4 | 2e-18 | 49/49 (HT-29, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **3.44×** | +7.8 | 2e-12 | 42/44 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **2.32×** | +5.7 | 2e-06 | 46/48 (PANC-1, NCI-H1573, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.47×** | +5.7 | 2e-06 | 40/45 (CHP-212, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~92% of this change | **1.68×** | +3.5 | 0.050 | 42/48 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.67× | +3.2 | 0.11 | 34/48 (A549, NCI-H1573, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.63× | +3.1 | 0.17 | 26/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2960.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.567×** | -3.8 | 0.080 | 41/48 (AsPC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.341×** | -3.6 | 0.080 | 44/49 (BT-474, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.598× | -3.5 | 0.10 | 38/48 (AsPC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.378× | -3.3 | 0.13 | 44/49 (HOP62, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 0.382× | -3.2 | 0.13 | 43/50 (AsPC-1, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.552× | -3.2 | 0.13 | 38/50 (NCI-H23, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | 0.630× | -3.1 | 0.16 | 35/48 (AsPC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~86% of this change | 0.617× | -3.1 | 0.16 | 37/48 (RKO, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.94 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2960. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 244 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A498 (line)]] | wt | 377 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A549 (line)]] | wt | 346 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H460 (line)]] | wt | 171 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.07× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SW 900 (line)]] | alt | 143 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A-172 (line)]] | wt | 280 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[C32 (line)]] | wt | 133 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[CFPAC-1 (line)]] | alt | 138 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[COLO 205 (line)]] | alt | 68.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.54× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[H4 (line)]] | wt | 162 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[HOP62 (line)]] | alt | 169 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[HS-578T (line)]] | alt | 237 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[HT-29 (line)]] | alt | 135 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.35× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[J82 (line)]] | alt | 307 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[KATO III (line)]] | alt | 202 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.58× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[LoVo (line)]] | wt | 134 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[LOX-IMVI (line)]] | wt | 231 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[LS 180 (line)]] | wt | 181 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 204 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H1792 (line)]] | alt | 147 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.09× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[RKO (line)]] | wt | 290 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[RPMI-7951 (line)]] | alt | 167 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SNU-423 (line)]] | alt | 143 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SW480 (line)]] | alt | 236 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A-427 (line)]] | wt | 387 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 136 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 202 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 194 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 141 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 180 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 228 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 369 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 362 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 386 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 97.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 393 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 153 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2960), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*34 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYL12A]] | +0.66 | +0.71 / +0.57 | both halves | 1e-05 | STRING 402 |
| [[POLR2L]] | +0.63 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[GOLT1A]] | +0.61 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[S100A6]] | +0.59 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[MICOS10]] | +0.57 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[TUBB4B]] | +0.56 | +0.62 / +0.50 | both halves | 1e-05 | pathway: RHO GTPase Effectors |
| [[PHLDA2]] | +0.55 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[TNFRSF12A]] | +0.54 | +0.66 / +0.39 | both halves | 5e-05 |  |
| [[CFL1]] | +0.53 | +0.61 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_PI3K_AKT_MTOR_SIGNALING; STRING 994 |
| [[DCBLD1]] | +0.53 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[EXOC6]] | +0.53 | +0.51 / +0.36 | both halves | 1e-04 |  |
| [[DRAP1]] | +0.53 | +0.62 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*66 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTCA]] | -0.63 | -0.69 / -0.47 | both halves | 2e-05 |  |
| [[ALDH2]] | -0.60 | -0.67 / -0.46 | both halves | 3e-05 |  |
| [[ABHD4]] | -0.60 | -0.68 / -0.45 | both halves | 3e-05 |  |
| [[DCAF12]] | -0.59 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[SAMM50]] | -0.59 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[SLC25A38]] | -0.58 | -0.65 / -0.36 | both halves | 9e-05 |  |
| [[CIZ1]] | -0.58 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[OTULIN]] | -0.57 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[BABAM1]] | -0.57 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[DFFB]] | -0.56 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[TMEM183A]] | -0.56 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[SUDS3]] | -0.55 | -0.58 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALDH2]] | B | ALDH2 activity lowers PFN1's level | lines that do not express ALDH2 (9) vs lines expressing it (41) | 1.33× higher at baseline in the lines without ALDH2 | 0.048 | ⚠ within organs, on part of the lines; also absent: MTARC2, SLC12A7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **-** arm (projection on the module's main direction -0.713). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (38.6, 3.6); signed map (9.2, 41.2). **Vector** length 71.0, 35.2% of its response variance represented; |z| ≥ 3 in 811 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +1.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.5 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +3.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | +3.2 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | -1.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.0 | +1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.9 | +0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.9 | +0.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~86% of this change | -5.6 | -3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -5.0 | +9.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.0 | -0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -4.8 | +7.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.6 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | profilin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:4,945,652-4,949,061 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Profilins |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, COMPLEMENT, APICAL_JUNCTION |
| Reactome | 14 pathways, smallest: PCP/CE pathway; Platelet degranulation; Response to elevated platelet cytosolic Ca2+ |
| Matched by | ensembl_id |

**Function**, from UniProt [P07737](https://www.uniprot.org/uniprotkb/P07737) (Profilin-1):

> Binds to actin and affects the structure of the cytoskeleton. At high concentrations, profilin prevents the polymerization of actin, whereas it enhances it at low concentrations. By binding to PIP2, it inhibits the formation of IP3 and DG. Inhibits androgen receptor (AR) and HTT aggregation and binding of G-actin is essential for its inhibition of AR. Acts as a host antiviral restriction factor against Kaposi sarcoma-associated herpesvirus through SQSTM1/p62-mediated selective autophagy …

**Summary**, from NCBI Gene [5216](https://www.ncbi.nlm.nih.gov/gene/5216):

> This gene encodes a member of the profilin family of small actin-binding proteins. The encoded protein plays an important role in actin dynamics by regulating actin polymerization in response to extracellular signals. Deletion of this gene is associated with Miller-Dieker syndrome, and the encoded protein may also play a role in Huntington disease. Multiple pseudogenes of this gene are located on chromosome 1. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:8881](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8881) · Entrez [5216](https://www.ncbi.nlm.nih.gov/gene/5216) · UniProt [P07737](https://www.uniprot.org/uniprotkb/P07737) · Ensembl [ENSG00000108518](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108518)

## Data

Gene col 2960: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2960); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2960, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2960]; `tensor/DDL_lfc|DDL_z.npy` [2960]; `embed/gene_vectors.npy` [2960]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2960 or target_col == 2960). Every well: [[PFN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PFN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
