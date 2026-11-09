---
symbol: "SYCE2"
type: "gene"
col: 8456
ensembl_id: "ENSG00000161860"
name: "synaptonemal complex central element protein 2"
location: "19p13.13"
module: 38
arm: "+"
pooled_cpm: 7.78
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# SYCE2

*synaptonemal complex central element protein 2* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.61× (z +16.0, q 0e+00, up in 39 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.693× (z -6.1, q 6e-07, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL9]] (+0.77, fdr 7e-06), [[ISY1-RAB43]] (+0.73, fdr 7e-06), [[IDI2-AS1]] (+0.72, fdr 7e-06); moves opposite to [[DLD]] (-0.60, fdr 4e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8456.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +16.0 | 0e+00 | 39/44 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +9.5 | 4e-19 | 25/34 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.5 | 0.001 | 16/46 (A-172, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +4.5 | 0.001 | 17/41 (LoVo, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +4.2 | 0.003 | 13/46 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.42×** | +4.0 | 0.005 | 13/41 (SW480, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.012 | 18/44 (NCI-H460, HCT15, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.018 | 7/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.36×** | +3.5 | 0.030 | 13/42 (SW480, HT-29, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.063 | 2/47 (HOP62, SW48) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.67×** | +3.2 | 0.077 | 4/41 (C32, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.085 | 10/44 (A-427, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8456.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.693×** | -6.1 | 6e-07 | 24/47 (RPMI-7951, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.670×** | -4.7 | 7e-04 | 19/45 (PANC-1, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.690×** | -4.2 | 0.004 | 18/44 (C32, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.691×** | -4.2 | 0.004 | 18/40 (A-427, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.710×** | -4.0 | 0.007 | 14/46 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.528×** | -3.9 | 0.008 | 13/44 (HEC-1-A, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.715×** | -3.8 | 0.012 | 16/45 (BT-474, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.746×** | -3.4 | 0.042 | 15/41 (H4, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.606× | -3.1 | 0.13 | 9/41 (HEC-1-A, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8456. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 45.8 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.112× (z -12.9) |
| [[A-427 (line)]] | wt | 14.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0394× (z -18.1) ⚠ cell-cycle shift, explains ~3% of this change |
| [[H4 (line)]] | wt | 20.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0559× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.112× (z -9.2) |
| [[HOP62 (line)]] | alt | 4.66 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0811× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0912× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 17.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0767× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 3.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.97× (z +9.3) | — |
| [[HepG2_C3A (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0805× (z -9.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 6.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.09× (z +8.5) | — |
| [[J82 (line)]] | alt | 8.93 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 7.01 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0897× (z -10.9) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 4.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 5.57 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.178× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0931× (z -9.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 8.38 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8456), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL9]] | +0.77 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.73 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | +0.72 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[PYGM]] | +0.71 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[PILRA]] | +0.71 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[ATP2A1]] | +0.71 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[PYY]] | +0.71 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[KCNJ14]] | +0.71 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[CHRNE]] | +0.69 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[VWCE]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[KLRA1P]] | +0.68 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[TFAP2E]] | +0.68 | +0.68 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLD]] | -0.60 | -0.42 / -0.61 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SYCE2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RUNDC3A-AS1]] | B | RUNDC3A-AS1 activity raises SYCE2's level | lines that do not express RUNDC3A-AS1 (5) vs lines expressing it (45) | 1.99× lower at baseline in the lines without RUNDC3A-AS1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ERO1B, TEX14, TCTN1; maybe low, not absent |
| [[LINC02609]] | B | LINC02609 activity raises SYCE2's level | lines that do not express LINC02609 (6) vs lines expressing it (44) | 1.86× lower at baseline in the lines without LINC02609 | 0.095 | ⚠ within organs, on part of the lines; also absent: TPST1, HLTF, FERMT2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.810). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.3, -19.4); signed map (12.6, 11.4). **Vector** length 82.8, 15.2% of its response variance represented; |z| ≥ 3 in 979 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +16.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.5 | +9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | +3.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +2.9 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.7 | +4.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.9 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.7 | +2.0 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -4.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.3 | -6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -0.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.9 | -4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.1 | -2.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | synaptonemal complex central element protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,898,786-12,919,293 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CESC1 |
| Reactome | 4 pathways, smallest: Meiotic synapsis; Meiosis; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PIF2](https://www.uniprot.org/uniprotkb/Q6PIF2) (Synaptonemal complex central element protein 2):

> Major component of the transverse central element of synaptonemal complexes (SCS), formed between homologous chromosomes during meiotic prophase. Requires SYCP1 in order to be incorporated into the central element. May have a role in the synaptonemal complex assembly, stabilization and recombination (By similarity).

**Summary**, from NCBI Gene [256126](https://www.ncbi.nlm.nih.gov/gene/256126):

> The protein encoded by this gene is part of the synaptonemal complex formed between homologous chromosomes during meiotic prophase. The encoded protein associates with SYCP1 and SYCE1 and is found only where chromosome cores are synapsed. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:27411](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27411) · Entrez [256126](https://www.ncbi.nlm.nih.gov/gene/256126) · UniProt [Q6PIF2](https://www.uniprot.org/uniprotkb/Q6PIF2) · Ensembl [ENSG00000161860](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161860)

## Data

Gene col 8456: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8456); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8456, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8456]; `tensor/DDL_lfc|DDL_z.npy` [8456]; `embed/gene_vectors.npy` [8456]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8456 or target_col == 8456). Every well: [[SYCE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYCE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
