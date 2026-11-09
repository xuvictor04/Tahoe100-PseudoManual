---
symbol: "LTB"
type: "gene"
col: 13596
ensembl_id: "ENSG00000227507"
name: "lymphotoxin beta"
location: "6p21.33"
module: 14
arm: "+"
pooled_cpm: 2.48
n_lines_expressing: 22
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# LTB

*lymphotoxin beta* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.85× (z +12.2, q 2e-31, up in 13 of 14 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 6.52× (z +7.5, q 1e-11, up in 14 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0115×); [[Auranofin (drug)]] 5 µM in 1 line (HEC-1-A 0.0302×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STAP2]] (+0.74, fdr 7e-06), [[IL23A]] (+0.73, fdr 7e-06), [[NEURL3]] (+0.71, fdr 7e-06); moves opposite to [[AHSA1]] (-0.55, fdr 1e-05), [[NIPA2]] (-0.55, fdr 3e-05), [[BLTP2]] (-0.54, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[CD83]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13596.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **7.85×** | +12.2 | 2e-31 | 13/14 (HOP62, A-172, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **6.52×** | +7.5 | 1e-11 | 14/14 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.15×** | +6.9 | 1e-09 | 7/10 (NCI-H2347, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.42×** | +6.0 | 3e-07 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **2.89×** | +4.4 | 0.001 | 2/6 (PANC-1, Panc 03.27) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.75×** | +4.2 | 0.002 | 9/17 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.54×** | +3.9 | 0.007 | 10/17 (NCI-H2347, BT-474, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.53×** | +3.9 | 0.007 | 8/12 (A-172, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.56×** | +3.8 | 0.010 | 1/6 (Panc 03.27) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.90×** | +3.8 | 0.010 | 0/17 | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.60×** | +3.7 | 0.012 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.39×** | +3.6 | 0.013 | 0/9 | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +3.6 | 0.014 | 4/11 (A549, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.13×** | +3.4 | 0.027 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.20×** | +3.3 | 0.039 | 1/9 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.11×** | +3.1 | 0.063 | 5/14 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~22% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13596.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0115×); [[Auranofin (drug)]] 5 µM in 1 line (HEC-1-A 0.0302×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | 0.433× | -3.6 | 0.14 | 12/15 (HEC-1-A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | 0.439× | -3.5 | 0.14 | 13/16 (HEC-1-A, SW1417, …) | all doses, flat | cell-cycle shift (explains ~22% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | 0.452× | -3.4 | 0.14 | 14/15 (HEC-1-A, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.484× | -3.1 | 0.28 | 12/17 (Panc 03.27, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.54 per unit of S-phase module lfc, +0.96 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13596. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 7.60 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0115× (z -13.7) |
| [[A-172 (line)]] | wt | 0.681 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 38.0× (z +8.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[CFPAC-1 (line)]] | alt | 3.69 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +8.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HOP62 (line)]] | alt | 0.645 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 43.7× (z +8.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-427 (line)]] | wt | 0.284 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.697 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.239 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.243 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.523 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.289 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.308 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.825 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.319 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.210 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.985 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.225 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.236 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.266 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.277 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.752 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.265 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.451 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13596), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAP2]] | +0.74 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[IL23A]] | +0.73 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[NEURL3]] | +0.71 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[STARD10]] | +0.66 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[PLAU]] | +0.63 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[RASGRP1]] | +0.62 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[POLR1H]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[NINJ1]] | +0.61 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[IL32]] | +0.61 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[CX3CL1]] | +0.61 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[PIK3IP1]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[STAT5A]] | +0.60 | +0.49 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHSA1]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[NIPA2]] | -0.55 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[BLTP2]] | -0.54 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[STRAP]] | -0.54 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[DROSHA]] | -0.52 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[ADAM15]] | -0.52 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[CDC42BPB]] | -0.51 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[HERC2P3]] | -0.51 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[FBXW2]] | -0.51 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[NAPG]] | -0.51 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[OPA1]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[EIF3H]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD83]] | B | LTB activity raises CD83's level | lines that do not express LTB (28) vs lines expressing it (22) | 1.72× lower at baseline in the lines without LTB | 0.072 | ⚠ within organs, on part of the lines; also absent: HAVCR1, TIMD4, RHEX |
| [[TMEM265]] | B | LTB activity raises TMEM265's level | lines that do not express LTB (28) vs lines expressing it (22) | 1.85× lower at baseline in the lines without LTB | 0.078 | ⚠ within organs, on part of the lines; also absent: HAVCR1, TIMD4, RHEX |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.2, 2.6); signed map (42.4, 10.4). **Vector** length 42.3, 12.0% of its response variance represented; |z| ≥ 3 in 398 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.1 | +12.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.9 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +2.4 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +1.4 | +4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.1 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.7 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.6 | +0.6 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | +0.6 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.6 | +2.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -0.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.3 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -1.3 | +3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -1.0 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | lymphotoxin beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,580,525-31,582,522 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p33, TNFSF3; previously TNFC |
| Gene groups (HGNC) | Tumor necrosis factor superfamily |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, ALLOGRAFT_REJECTION, IL2_STAT5_SIGNALING |
| Reactome | 3 pathways, smallest: TNF receptor superfamily (TNFSF) members mediating non-canonical NF-kB pathway; TNFR2 non-canonical NF-kB pathway; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06643](https://www.uniprot.org/uniprotkb/Q06643) (Lymphotoxin-beta):

> Cytokine that binds to LTBR/TNFRSF3. May play a specific role in immune response regulation. Provides the membrane anchor for the attachment of the heterotrimeric complex to the cell surface. Isoform 2 is probably non-functional.

**Summary**, from NCBI Gene [4050](https://www.ncbi.nlm.nih.gov/gene/4050):

> Lymphotoxin beta is a type II membrane protein of the TNF family. It anchors lymphotoxin-alpha to the cell surface through heterotrimer formation. The predominant form on the lymphocyte surface is the lymphotoxin-alpha 1/beta 2 complex (e.g. 1 molecule alpha/2 molecules beta) and this complex is the primary ligand for the lymphotoxin-beta receptor. The minor complex is lymphotoxin-alpha 2/beta 1. LTB is an inducer of the inflammatory response system and involved in normal development of …

**Accessions** — [HGNC:6711](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6711) · Entrez [4050](https://www.ncbi.nlm.nih.gov/gene/4050) · UniProt [Q06643](https://www.uniprot.org/uniprotkb/Q06643) · Ensembl [ENSG00000227507](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227507)

## Data

Gene col 13596: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13596); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13596, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13596]; `tensor/DDL_lfc|DDL_z.npy` [13596]; `embed/gene_vectors.npy` [13596]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13596 or target_col == 13596). Every well: [[LTB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LTB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
