---
symbol: "ZNF17"
type: "gene"
col: 11798
ensembl_id: "ENSG00000186272"
name: "zinc finger protein 17"
location: "19q13.43"
module: 143
arm: "+"
pooled_cpm: 5.27
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# ZNF17

*zinc finger protein 17* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.90× (z +6.5, q 4e-08, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.652× (z -4.4, q 0.007, down in 20 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Azithromycin (hydrate) (drug)]] 5 µM: 0.785× (z -3.5, q 0.077, down in 15 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H460 0.145×, HEC-1-A 0.191×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (KATO III 0.0749×; ⚠ cell-cycle shift, explains ~30% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (NCI-H460 0.106×); [[Tetracycline (hydrochloride) (drug)]] 0.05 µM in 1 line (A549 0.0576×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (A549 0.0736×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF256]] (+0.67, fdr 1e-05), [[TSFM]] (+0.64, fdr 1e-05), [[ZNF70]] (+0.63, fdr 3e-05); moves opposite to [[MEMO1]] (-0.59, fdr 3e-05), [[ARL15]] (-0.59, fdr 1e-05), [[RALGAPA1]] (-0.57, fdr 3e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF256]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11798.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +6.5 | 4e-08 | 28/48 (NCI-H23, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.06×** | +6.0 | 7e-07 | 24/44 (KATO III, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +5.0 | 1e-04 | 20/46 (C-33 A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.50×** | +4.9 | 1e-04 | 12/39 (KATO III, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +4.4 | 0.001 | 14/46 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +4.2 | 0.003 | 3/17 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.30×** | +3.8 | 0.010 | 9/48 (HS-578T, LoVo, …) | top dose only | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.23× | +3.0 | 0.18 | 11/42 (BT-474, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11798.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H460 0.145×, HEC-1-A 0.191×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (KATO III 0.0749×; ⚠ cell-cycle shift, explains ~30% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (NCI-H460 0.106×); [[Tetracycline (hydrochloride) (drug)]] 0.05 µM in 1 line (A549 0.0576×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (A549 0.0736×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.652×** | -4.4 | 0.007 | 20/43 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.691×** | -3.8 | 0.047 | 13/45 (KATO III, H4, …) | all doses, flat |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **0.785×** | -3.5 | 0.077 | 15/46 (HepG2/C3A, HEC-1-A, …) | top dose only | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **0.703×** | -3.5 | 0.077 | 10/43 (NCI-H1573, HT-29, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | 0.726× | -3.1 | 0.19 | 12/34 (SHP-77, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11798. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 4.92 | 0 | 2 | — | [[Tetracycline (hydrochloride) (drug)]] 0.05 µM 0.0576× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 4.58 | 0 | 2 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.106× (z -10.3) |
| [[A-172 (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 8.94 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.191× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[KATO III (line)]] | alt | 6.35 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0749× (z -10.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 2.54 | 0 | 1 | — | [[Tolcapone (drug)]] 0.05 µM 0.0531× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 7.47 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -8.5) |
| [[A-427 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11798), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF256]] | +0.67 | +0.54 / +0.66 | both halves | 1e-05 | same gene group |
| [[TSFM]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[ZNF70]] | +0.63 | +0.64 / +0.44 | both halves | 3e-05 | same gene group |
| [[ZNF266]] | +0.62 | +0.64 / +0.58 | both halves | 7e-06 | same gene group |
| [[PRPF8]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[SNRNP200]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[RNF25]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ZNF408]] | +0.59 | +0.62 / +0.50 | both halves | 1e-05 | same gene group |
| [[PLXNB3]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[C1D]] | +0.58 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[CDK9]] | +0.58 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[ZNF527]] | +0.58 | +0.57 / +0.60 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEMO1]] | -0.59 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[ARL15]] | -0.59 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[RALGAPA1]] | -0.57 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[DTNB]] | -0.56 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[AHCYL2]] | -0.55 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[ERVK3-1]] | -0.53 | -0.36 / -0.56 | both halves | 9e-05 |  |
| [[LARGE1]] | -0.53 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[SLMAP]] | -0.52 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[PARD3]] | -0.51 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[PEAK1]] | -0.51 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[PLEKHA5]] | -0.50 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[MSX1]] | -0.50 | -0.42 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF256]] | B | ZNF256 activity raises ZNF17's level | lines that do not express ZNF256 (14) vs lines expressing it (36) | 1.41× lower at baseline in the lines without ZNF256 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ZNF331, GAMT, ZNF625 |
| [[HDAC6]] | B | HDAC6 activity lowers ZNF17's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF304]] | B | ZNF304 activity raises ZNF17's level | lines that do not express ZNF304 (10) vs lines expressing it (40) | 1.42× lower at baseline in the lines without ZNF304 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000286964, ZNF256, RTL8C |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction -0.508). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.1, -14.4); signed map (-43.5, -27.4). **Vector** length 45.5, 4.94% of its response variance represented; |z| ≥ 3 in 990 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +4.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +2.0 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +4.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.7 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +1.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +0.8 | +1.9 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | +0.7 | +1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +0.6 | +1.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | -2.2 | -3.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -1.9 | -4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.6 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | +0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.1 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.0 | +0.2 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | -0.9 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.43 — chr19:57,411,161-57,421,934 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HPF3, KOX10, KIAA1947, FLJ40864, FLJ46058, FLJ46615 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P17021](https://www.uniprot.org/uniprotkb/P17021) (Zinc finger protein 17):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7565](https://www.ncbi.nlm.nih.gov/gene/7565):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:12958](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12958) · Entrez [7565](https://www.ncbi.nlm.nih.gov/gene/7565) · UniProt [P17021](https://www.uniprot.org/uniprotkb/P17021) · Ensembl [ENSG00000186272](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186272)

## Data

Gene col 11798: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11798); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11798, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11798]; `tensor/DDL_lfc|DDL_z.npy` [11798]; `embed/gene_vectors.npy` [11798]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11798 or target_col == 11798). Every well: [[ZNF17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
