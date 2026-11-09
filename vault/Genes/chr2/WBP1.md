---
symbol: "WBP1"
type: "gene"
col: 14210
ensembl_id: "ENSG00000239779"
name: "WW domain binding protein 1"
location: "2p13.1"
module: 69
arm: "+"
pooled_cpm: 14.93
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# WBP1

*WW domain binding protein 1* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.19× (z +11.4, q 2e-27, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.465× (z -7.9, q 2e-12, down in 38 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.507× (z -7.0, q 8e-10, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC115]] (+0.78, fdr 7e-06), [[DNAJC4]] (+0.68, fdr 1e-05), [[HBP1]] (+0.67, fdr 1e-05); moves opposite to [[TMEM33]] (-0.66, fdr 1e-05), [[CCT5]] (-0.66, fdr 1e-05), [[C1QBP]] (-0.65, fdr 8e-06).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14210.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +11.4 | 2e-27 | 44/45 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +8.9 | 1e-16 | 33/37 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +8.2 | 7e-14 | 18/28 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.72×** | +5.6 | 3e-06 | 28/44 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.72×** | +5.6 | 3e-06 | 29/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +5.1 | 3e-05 | 25/46 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +5.0 | 4e-05 | 29/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.61×** | +4.9 | 7e-05 | 23/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +4.4 | 6e-04 | 16/33 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.023 | 20/48 (NCI-H23, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.4 | 0.030 | 3/48 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.96×** | +3.4 | 0.030 | 11/45 (HOP62, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.059 | 12/47 (HOP62, NCI-H460, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.85×** | +3.1 | 0.077 | 10/44 (NCI-H23, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.100 | 12/47 (SW480, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14210.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.465×** | -7.9 | 2e-12 | 38/47 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.507×** | -7.0 | 8e-10 | 39/47 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.643×** | -4.5 | 0.001 | 27/46 (HS-578T, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.414×** | -4.0 | 0.007 | 23/46 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.690×** | -3.8 | 0.014 | 22/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.694×** | -3.8 | 0.014 | 23/47 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.679×** | -3.7 | 0.014 | 20/47 (SW 900, MIA PaCa-2, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.510× | -3.1 | 0.14 | 15/43 (NCI-H460, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Pentagastrin (drug)]] 5 µM |  | 0.811× | -3.0 | 0.15 | 9/48 (AsPC-1, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14210. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 10.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.44× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 14.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.277× (z -8.6) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0714× (z -13.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 12.5 | 0 | 1 | — | [[EX229 (drug)]] 0.05 µM 0.0670× (z -9.3) |
| [[SW480 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.254× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14210), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC115]] | +0.78 | +0.75 / +0.78 | both halves | 7e-06 |  |
| [[DNAJC4]] | +0.68 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[HBP1]] | +0.67 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[ARID4A]] | +0.66 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[CIR1]] | +0.66 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[OSER1-DT]] | +0.66 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[KDM5B]] | +0.65 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[ATOSA]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[IFT20]] | +0.65 | +0.46 / +0.72 | both halves | 2e-05 |  |
| [[FBXL20]] | +0.64 | +0.32 / +0.73 | both halves | 2e-04 |  |
| [[BSDC1]] | +0.64 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[RAB24]] | +0.64 | +0.65 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM33]] | -0.66 | -0.54 / -0.68 | both halves | 1e-05 |  |
| [[CCT5]] | -0.66 | -0.57 / -0.71 | both halves | 1e-05 |  |
| [[C1QBP]] | -0.65 | -0.58 / -0.66 | both halves | 8e-06 |  |
| [[ATIC]] | -0.64 | -0.48 / -0.70 | both halves | 2e-05 |  |
| [[NAA15]] | -0.64 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[URB2]] | -0.64 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[TFDP1]] | -0.64 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[NUP155]] | -0.63 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[CTPS1]] | -0.63 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[TCOF1]] | -0.63 | -0.70 / -0.62 | both halves | 7e-06 |  |
| [[TUBGCP4]] | -0.63 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[POLR1A]] | -0.63 | -0.54 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers WBP1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CLIP3]] | C | CLIP3 activity raises WBP1's level | lines that do not express CLIP3 (4) vs lines expressing it (46) | 1.25× lower at baseline in the lines without CLIP3 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RAPGEF4, MEGF11, TMEM170B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.738). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.6, -43.1); signed map (-13.0, 8.2). **Vector** length 69.6, 15.0% of its response variance represented; |z| ≥ 3 in 653 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +11.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.4 | +2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +5.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +3.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.2 | +3.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.2 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.2 | -7.9 |
|  | [[EX229 (drug)]] 5 µM |  | -3.5 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.2 | -2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.1 | -3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.7 | -2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | WW domain binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:74,458,400-74,460,891 (+) |
| Ensembl biotype | protein_coding |
| Also known as | WBP-1 |
| Gene groups (HGNC) | WBP1/VOPP1 family |
| Matched by | ensembl_id |

UniProt [Q96G27](https://www.uniprot.org/uniprotkb/Q96G27) carries no function annotation.

**Summary**, from NCBI Gene [23559](https://www.ncbi.nlm.nih.gov/gene/23559):

> The globular WW domain, named for the conserved tryptophan residues in the protein motif present in various structural and regulatory proteins, is known to play a role in the mediation of protein-protein interactions. This gene encodes a ligand of the WW domain of the Yes kinase-associated protein. Readthrough transcription of the neighboring upstream gene, which encodes INO80 complex subunit B, into this gene generates a non-coding transcript. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:12737](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12737) · Entrez [23559](https://www.ncbi.nlm.nih.gov/gene/23559) · UniProt [Q96G27](https://www.uniprot.org/uniprotkb/Q96G27) · Ensembl [ENSG00000239779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239779)

## Data

Gene col 14210: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14210); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14210, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14210]; `tensor/DDL_lfc|DDL_z.npy` [14210]; `embed/gene_vectors.npy` [14210]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14210 or target_col == 14210). Every well: [[WBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
