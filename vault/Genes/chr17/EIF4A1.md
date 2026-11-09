---
symbol: "EIF4A1"
type: "gene"
col: 8465
ensembl_id: "ENSG00000161960"
name: "eukaryotic translation initiation factor 4A1"
location: "17p13.1"
module: 134
arm: "+"
pooled_cpm: 255.57
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# EIF4A1

*eukaryotic translation initiation factor 4A1* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.84× (z +6.6, q 3e-08, up in 43 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.69× (z +5.6, q 5e-06, up in 42 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (C-33 A 0.347×, RKO 0.467×, CHP-212 0.424×, NCI-H2347 0.531×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GAPDH]] (+0.64, fdr 1e-05), [[GRPEL1]] (+0.59, fdr 1e-05), [[SLC25A6]] (+0.58, fdr 1e-05); moves opposite to [[XPA]] (-0.56, fdr 1e-05), [[LGALSL-DT]] (-0.54, fdr 3e-05), [[HACD2]] (-0.52, fdr 3e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC00869-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8465.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.84×** | +6.6 | 3e-08 | 43/49 (KATO III, A549, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +5.6 | 5e-06 | 42/48 (SW480, Panc 03.27, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.37×** | +4.9 | 2e-04 | 44/49 (COLO 205, SHP-77, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.25×** | +4.6 | 6e-04 | 34/48 (C32, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **1.55×** | +4.5 | 6e-04 | 33/44 (HT-29, A498, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.52×** | +4.5 | 8e-04 | 37/48 (NCI-H1573, PANC-1, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.53×** | +4.4 | 8e-04 | 36/47 (COLO 205, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.50×** | +4.3 | 0.001 | 37/48 (KATO III, AsPC-1, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.2 | 0.002 | 1/50 (C-33 A) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +4.2 | 0.002 | 40/48 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +4.2 | 0.002 | 41/48 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.42×** | +3.7 | 0.009 | 31/48 (KATO III, SW480, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.59×** | +3.5 | 0.017 | 41/47 (RPMI-7951, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~75% of this change | **1.38×** | +3.5 | 0.021 | 37/48 (SW1417, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.54×** | +3.3 | 0.034 | 43/48 (H4, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8465.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (C-33 A 0.347×, RKO 0.467×, CHP-212 0.424×, NCI-H2347 0.531×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 0.705× | -3.6 | 0.11 | 33/47 (AsPC-1, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.720× | -3.6 | 0.11 | 37/48 (NCI-H23, HCT15, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.709× | -3.3 | 0.21 | 29/50 (SW480, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8465. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 155 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.9) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[AsPC-1 (line)]] | alt | 214 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.81× (z +9.5) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[COLO 205 (line)]] | alt | 167 | 2 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 12.4× (z +9.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A498 (line)]] | wt | 340 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | — |
| [[A549 (line)]] | wt | 429 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | — |
| [[C-33 A (line)]] | alt | 269 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 322 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 156 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | — |
| [[NCI-H2347 (line)]] | alt | 185 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 392 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 3.47× (z +10.2) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[RKO (line)]] | wt | 328 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 365 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.27× (z +8.6) ⚠ toxic; cell-cycle shift, explains ~48% of this change | — |
| [[SW480 (line)]] | alt | 318 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.45× (z +8.5) | — |
| [[A-172 (line)]] | wt | 202 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 232 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 267 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 235 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 236 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 299 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 176 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 212 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 203 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 266 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 305 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 176 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 374 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 225 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 361 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 364 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 427 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 301 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 260 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 304 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 269 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8465), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GAPDH]] | +0.64 | +0.50 / +0.66 | both halves | 1e-05 | STRING 689 |
| [[GRPEL1]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[SLC25A6]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[HK1]] | +0.57 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[SLC2A3]] | +0.55 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[PDCD6]] | +0.55 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[MYO9B]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[GNAI3]] | +0.54 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[EIF4A3]] | +0.54 | +0.41 / +0.49 | both halves | 4e-05 | same gene group; pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 979 |
| [[CHSY1]] | +0.53 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[BUD23]] | +0.53 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[ATG101]] | +0.52 | +0.44 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPA]] | -0.56 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[LGALSL-DT]] | -0.54 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[HACD2]] | -0.52 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[UBXN2A]] | -0.52 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[SREK1]] | -0.52 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[NHLRC2]] | -0.52 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[DIS3L]] | -0.51 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[MTARC2]] | -0.50 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[TSR2]] | -0.50 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[TIA1]] | -0.50 | -0.41 / -0.34 | both halves | 1e-04 | STRING 818 |
| [[ZNF280D]] | -0.49 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[MARVELD2]] | -0.48 | -0.45 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00869-1]] | B | LINC00869-1 activity lowers EIF4A1's level | lines that do not express LINC00869-1 (7) vs lines expressing it (43) | 1.22× higher at baseline in the lines without LINC00869-1 | 0.085 | ⚠ within organs, on part of the lines; also absent: OSBPL10, STPG2, EIF4E3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.562). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.7, -18.2); signed map (-42.3, 26.7). **Vector** length 91.0, 37.1% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +4.6 | +3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +4.6 | +4.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.2 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +5.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.7 | +2.0 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +1.6 | +0.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +3.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -0.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.5 | +1.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | -4.1 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.7 | -3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 4A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,572,824-7,579,006 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DDX2A, EIF-4A; previously EIF4A |
| Gene groups (HGNC) | DEAD-box helicases; Small nucleolar RNA protein coding host genes |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, MYC_TARGETS_V1 |
| Reactome | 21 pathways, smallest: Z-decay: degradation of maternal mRNAs by zygotically expressed factors; Deadenylation of mRNA; M-decay: degradation of maternal mRNAs by maternally stored factors |
| Matched by | ensembl_id |

**Function**, from UniProt [P60842](https://www.uniprot.org/uniprotkb/P60842) (Eukaryotic initiation factor 4A-I):

> ATP-dependent RNA helicase which is a subunit of the eIF4F complex involved in cap recognition and is required for mRNA binding to ribosome. In the current model of translation initiation, eIF4A unwinds RNA secondary structures in the 5'-UTR of mRNAs which is necessary to allow efficient binding of the small ribosomal subunit, and subsequent scanning for the initiator codon. As a result, promotes cell proliferation and growth.

**Summary**, from NCBI Gene [1973](https://www.ncbi.nlm.nih.gov/gene/1973):

> Enables double-stranded RNA binding activity and translation initiation factor activity. Involved in cytoplasmic translational initiation and positive regulation of transcription by RNA polymerase II. Located in nuclear stress granule; perinuclear region of cytoplasm; and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3282](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3282) · Entrez [1973](https://www.ncbi.nlm.nih.gov/gene/1973) · UniProt [P60842](https://www.uniprot.org/uniprotkb/P60842) · Ensembl [ENSG00000161960](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161960)

## Data

Gene col 8465: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8465); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8465, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8465]; `tensor/DDL_lfc|DDL_z.npy` [8465]; `embed/gene_vectors.npy` [8465]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8465 or target_col == 8465). Every well: [[EIF4A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF4A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
