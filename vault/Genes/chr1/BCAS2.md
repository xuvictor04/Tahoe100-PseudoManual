---
symbol: "BCAS2"
type: "gene"
col: 3834
ensembl_id: "ENSG00000116752"
name: "BCAS2 pre-mRNA processing factor"
location: "1p13.2"
module: 12
arm: "+"
pooled_cpm: 32.57
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# BCAS2

*BCAS2 pre-mRNA processing factor* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.28× (z +12.0, q 1e-30, up in 43 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.200×, HCT15 0.154×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (MIA PaCa-2 0.294×); [[Digitoxin (drug)]] 0.5 µM in 1 line (KATO III 0.257×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNRPB2]] (+0.69, fdr 7e-06), [[VIRMA]] (+0.68, fdr 1e-05), [[CIR1]] (+0.64, fdr 7e-06); moves opposite to [[UBE2G2]] (-0.59, fdr 1e-05), [[CTSC]] (-0.58, fdr 1e-05), [[EIF5A]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MED6]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3834.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.28×** | +12.0 | 1e-30 | 43/49 (LoVo, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +11.3 | 3e-27 | 40/47 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +8.2 | 3e-14 | 37/48 (LoVo, HT-29, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.66×** | +8.0 | 1e-13 | 38/48 (A498, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +8.0 | 1e-13 | 35/48 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +8.0 | 1e-13 | 36/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +7.7 | 1e-12 | 35/47 (LS 180, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +6.6 | 2e-09 | 30/48 (RKO, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +6.6 | 2e-09 | 35/48 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.18×** | +6.5 | 5e-09 | 30/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +6.4 | 7e-09 | 35/48 (A498, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +6.3 | 2e-08 | 25/48 (J82, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +5.9 | 2e-07 | 28/46 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.6 | 7e-07 | 27/47 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.39×** | +5.2 | 8e-06 | 28/48 (SK-MEL-2, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.5 | 2e-04 | 22/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.49×** | +4.5 | 2e-04 | 19/48 (MIA PaCa-2, A498, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.004 | 15/48 (J82, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3834.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.200×, HCT15 0.154×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (MIA PaCa-2 0.294×); [[Digitoxin (drug)]] 0.5 µM in 1 line (KATO III 0.257×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -4.0 | 0.033 | 1/49 (SW 1088) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3834. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 26.3 | 5 (4 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.03× (z +10.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.40× (z +9.9) | — |
| [[LoVo (line)]] | wt | 36.1 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 7.84× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 73.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 19.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +12.8) | — |
| [[A498 (line)]] | wt | 44.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.89× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 48.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 42.6 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.60× (z +11.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.74× (z +11.3) | — |
| [[A549 (line)]] | wt | 18.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 41.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 39.7 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.103× (z -10.0) ⚠ toxic |
| [[HT-29 (line)]] | alt | 23.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.37× (z +9.3) | — |
| [[KATO III (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.257× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 24.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.5 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.294× (z -13.3) |
| [[RKO (line)]] | wt | 30.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.22× (z +8.8) | — |
| [[SW480 (line)]] | alt | 29.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.10× (z +8.8) | — |
| [[A-427 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3834), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPB2]] | +0.69 | +0.60 / +0.66 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 991 |
| [[VIRMA]] | +0.68 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[CIR1]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[OSER1]] | +0.63 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[SCNM1]] | +0.63 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[PPIL4]] | +0.62 | +0.61 / +0.55 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions |
| [[TCEAL8]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[HAX1]] | +0.61 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[TRIM23]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[CWC15]] | +0.61 | +0.62 / +0.58 | both halves | 8e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 999 |
| [[IK]] | +0.61 | +0.57 / +0.64 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 488 |
| [[FRG1]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 | STRING 842 |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2G2]] | -0.59 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[CTSC]] | -0.58 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[EIF5A]] | -0.58 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[PKP4]] | -0.57 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[IGF2BP3]] | -0.57 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[SUGP2]] | -0.56 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[PRPS2]] | -0.56 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[NSD2]] | -0.56 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[NUP188]] | -0.55 | -0.37 / -0.56 | both halves | 8e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[CFL1]] | -0.52 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[QSOX2]] | -0.52 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[TBC1D4]] | -0.51 | -0.51 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MED6]] | C | MED6's natural level weakens BCAS2's drug response | MED6's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.16; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[VIRMA]] | C | VIRMA's natural level weakens BCAS2's drug response | VIRMA's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.61, reverse -0.13; direction not clear | 0.099 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.640). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-38.2, -7.2); signed map (-13.3, -9.9). **Vector** length 86.1, 19.7% of its response variance represented; |z| ≥ 3 in 955 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.9 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +8.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +5.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.2 | +12.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.2 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +8.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | -0.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.3 | +0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | +2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | +1.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -5.6 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -2.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -0.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -0.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.8 | -0.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | BCAS2 pre-mRNA processing factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:114,567,557-114,581,629 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DAM1, SPF27, Snt309 |
| Gene groups (HGNC) | NineTeen complex; Spliceosomal C complex |
| Reactome | 7 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Dengue Virus-Host Interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [O75934](https://www.uniprot.org/uniprotkb/O75934) (Pre-mRNA-splicing factor SPF27):

> Required for pre-mRNA splicing as component of the activated spliceosome. Component of the PRP19-CDC5L complex that forms an integral part of the spliceosome and is required for activating pre-mRNA splicing. May have a scaffolding role in the spliceosome assembly as it contacts all other components of the core complex. The PRP19-CDC5L complex may also play a role in the response to DNA damage (DDR).

**Summary**, from NCBI Gene [10286](https://www.ncbi.nlm.nih.gov/gene/10286):

> Involved in mRNA splicing, via spliceosome. Located in DNA replication factor A complex and nuclear speck. Part of U2-type catalytic step 2 spliceosome. Implicated in breast cancer. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:975](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:975) · Entrez [10286](https://www.ncbi.nlm.nih.gov/gene/10286) · UniProt [O75934](https://www.uniprot.org/uniprotkb/O75934) · Ensembl [ENSG00000116752](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116752)

## Data

Gene col 3834: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3834); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3834, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3834]; `tensor/DDL_lfc|DDL_z.npy` [3834]; `embed/gene_vectors.npy` [3834]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3834 or target_col == 3834). Every well: [[BCAS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCAS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
