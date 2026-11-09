---
symbol: "NEFM"
type: "gene"
col: 2487
ensembl_id: "ENSG00000104722"
name: "neurofilament medium chain"
location: "8p21.2"
module: 19
arm: "+"
pooled_cpm: 4.24
n_lines_expressing: 15
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# NEFM

*neurofilament medium chain* — 8p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.67× (z +13.7, q 7e-40, up in 6 of 8 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0985×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPP10]] (+0.58, fdr 3e-05), [[NEFL]] (+0.57, fdr 4e-05, ⚠ same locus), [[LINC01257]] (+0.55, fdr 4e-05), [[SERPINB11]] (+0.54, fdr 4e-05); moves opposite to [[ADAMTS10]] (-0.52, fdr 2e-05), [[PREX2]] (-0.48, fdr 9e-05), [[TIMD4]] (-0.41, fdr 3e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EPHA4]] → it (grade B ⚠); 3 go from it, the strongest it → [[SCUBE1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2487.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.67×** | +13.7 | 7e-40 | 6/8 (A498, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.48×** | +12.2 | 2e-31 | 4/4 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.70×** | +10.9 | 2e-25 | 4/5 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.83×** | +9.2 | 5e-18 | 4/8 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.72×** | +7.6 | 3e-12 | 3/5 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.99×** | +6.9 | 6e-10 | 5/8 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.38×** | +5.4 | 5e-06 | 6/10 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.36×** | +4.8 | 1e-04 | 0/4 | top dose only | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.08×** | +4.6 | 3e-04 | 10/11 (A498, HOP62, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.78×** | +4.6 | 3e-04 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.64×** | +4.4 | 6e-04 | 1/10 (A498) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.61×** | +4.2 | 0.001 | 3/5 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.44×** | +4.0 | 0.003 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.89×** | +4.0 | 0.003 | 4/5 (NCI-H1792, SHP-77, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.87×** | +3.9 | 0.003 | 0/7 | two highest doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.39×** | +3.9 | 0.003 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.004 | 8/11 (HOP62, RPMI-7951, …) | rises with dose | position effect removed |
| [[NVP-BHG712 (drug)]] 0.5 µM |  | **2.35×** | +3.8 | 0.004 | 0/10 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.012 | 4/11 (A498, HOP62, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.00×** | +3.1 | 0.043 | 3/10 (A498, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.40×** | +3.0 | 0.057 | 2/8 (NCI-H460, SHP-77) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2487.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0985×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pimozide (drug)]] 5 µM |  | 0.581× | -3.5 | 0.28 | 1/11 (NCI-H23) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.577× | -3.2 | 0.28 | 1/11 (NCI-H460) | inconsistent across doses |  |
| [[Oxaliplatin (drug)]] 0.5 µM |  | 0.505× | -3.1 | 0.28 | 0/12 | inconsistent across doses | noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.600× | -3.0 | 0.28 | 0/11 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2487. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 12.1 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 38.7× (z +22.4) | — |
| [[HOP62 (line)]] | alt | 8.53 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +14.4) | — |
| [[NCI-H1792 (line)]] | alt | 64.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.64× (z +14.8) | — |
| [[NCI-H460 (line)]] | wt | 4.61 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0985× (z -8.6) |
| [[A-172 (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.433 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.643 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.594 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.633 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.671 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.562 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.657 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.643 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.750 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.516 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.521 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.656 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.573 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.647 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.716 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.982 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.782 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.750 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.693 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.562 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2487), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPP10]] | +0.58 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[NEFL]] | +0.57 | +0.42 / +0.67 | both halves | 4e-05 | same gene group; STRING 999; ⚠ same locus (31.9 kb: neighbours can correlate without regulation) |
| [[LINC01257]] | +0.55 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[SERPINB11]] | +0.54 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[SCARA5]] | +0.53 | +0.48 / +0.38 | both halves | 6e-05 |  |
| [[CTNND2]] | +0.52 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[PLAC4]] | +0.52 | +0.38 / +0.45 | both halves | 7e-05 |  |
| [[UNC13A]] | +0.51 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[KCNK2]] | +0.51 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[RAB3C]] | +0.51 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[FENDRR]] | +0.50 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[PCDH10]] | +0.50 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[KCNMB4]] | +0.50 | +0.46 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS10]] | -0.52 | -0.51 / -0.46 | both halves | 2e-05 | **novel candidate** |
| [[PREX2]] | -0.48 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[TIMD4]] | -0.41 | -0.32 / -0.29 | both halves | 3e-04 |  |
| [[LRRK1]] | -0.39 | -0.27 / -0.29 | both halves | 3e-04 |  |
| [[ATP10A]] | -0.39 | -0.36 / -0.28 | both halves | 3e-04 |  |
| [[TSHZ3-AS1]] | -0.38 | -0.37 / -0.21 | both halves | 7e-04 |  |
| [[SLC25A28]] | -0.38 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[SCO2]] | -0.38 | -0.30 / -0.37 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA4]] | B | EPHA4 activity raises NEFM's level | lines that do not express EPHA4 (19) vs lines expressing it (31) | 1.69× lower at baseline in the lines without EPHA4 | 0.089 | ⚠ within organs, on part of the lines; also absent: SNAI2, GNG2, TNFSF10 |
| [[TMEM144]] | C | TMEM144 activity lowers NEFM's level | lines that do not express TMEM144 (3) vs lines expressing it (47) | 2.65× higher at baseline in the lines without TMEM144 | 0.083 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: WNK4, RNF103-CHMP3, RBMS2; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCUBE1]] | C | NEFM activity raises SCUBE1's level | lines that do not express NEFM (35) vs lines expressing it (15) | 3.72× lower at baseline in the lines without NEFM | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, GTF2I-AS1, LINC03000; co-absent with the target |
| [[NEFL]] | C | NEFM activity raises NEFL's level | lines that do not express NEFM (35) vs lines expressing it (15) | 4.56× lower at baseline in the lines without NEFM | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, GTF2I-AS1, LINC03000; co-absent with the target |
| [[COL4A6]] | C | NEFM activity raises COL4A6's level | lines that do not express NEFM (35) vs lines expressing it (15) | 3.43× lower at baseline in the lines without NEFM | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, GTF2I-AS1, LINC03000; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.465). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.7, 36.2); signed map (40.7, 40.6). **Vector** length 35.3, 11.0% of its response variance represented; |z| ≥ 3 in 277 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +7.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +1.6 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +5.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.0 | +0.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.9 | +0.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.7 | +2.4 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | +0.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -1.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -0.7 | -1.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -0.7 | -1.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.7 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | neurofilament medium chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.2 — chr8:24,913,758-24,919,098 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NFM, NF-M; previously NEF3 |
| Gene groups (HGNC) | Intermediate filaments Type IV |
| Matched by | ensembl_id |

**Function**, from UniProt [P07197](https://www.uniprot.org/uniprotkb/P07197) (Neurofilament medium polypeptide):

> Neurofilaments usually contain three intermediate filament proteins: NEFL, NEFM, and NEFH which are involved in the maintenance of neuronal caliber. May additionally cooperate with the neuronal intermediate filament proteins PRPH and INA to form neuronal filamentous networks (By similarity).

**Summary**, from NCBI Gene [4741](https://www.ncbi.nlm.nih.gov/gene/4741):

> Neurofilaments are type IV intermediate filament heteropolymers composed of light, medium, and heavy chains. Neurofilaments comprise the axoskeleton and functionally maintain neuronal caliber. They may also play a role in intracellular transport to axons and dendrites. This gene encodes the medium neurofilament protein. This protein is commonly used as a biomarker of neuronal damage. Alternative splicing results in multiple transcript variants encoding distinct isoforms. [provided by RefSeq, …

**Accessions** — [HGNC:7734](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7734) · Entrez [4741](https://www.ncbi.nlm.nih.gov/gene/4741) · UniProt [P07197](https://www.uniprot.org/uniprotkb/P07197) · Ensembl [ENSG00000104722](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104722)

## Data

Gene col 2487: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2487); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2487, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2487]; `tensor/DDL_lfc|DDL_z.npy` [2487]; `embed/gene_vectors.npy` [2487]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2487 or target_col == 2487). Every well: [[NEFM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEFM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
