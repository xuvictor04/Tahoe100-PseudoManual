---
symbol: "ZNF736P9Y"
type: "gene"
col: 14217
ensembl_id: "ENSG00000239893"
name: "zinc finger protein 736 pseudogene 9, Y-linked"
location: "Yp11.2"
module: 73
arm: "+"
pooled_cpm: 6.76
n_lines_expressing: 10
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 12
direction_downstream: 18
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# ZNF736P9Y

*zinc finger protein 736 pseudogene 9, Y-linked* — Yp11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.04× (z +10.9, q 5e-25, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 2.01× (z +3.5, q 0.038, up in 0 of 7 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.560× (z -4.1, q 0.024, down in 7 of 8 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (LoVo 0.109×, A-172 0.134×, CFPAC-1 0.109×, NCI-H460 0.204×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (NCI-H460 0.114×, H4 0.105×, A-172 0.183×); [[Panobinostat (drug)]] 5 µM in 3 lines (A-172 0.157×, NCI-H460 0.155×, LoVo 0.161×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.171×, H4 0.179×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPINB5]] (+0.58, fdr 1e-05), [[LINC02582]] (+0.58, fdr 2e-05), [[COL4A6]] (+0.55, fdr 3e-05); moves opposite to [[PIK3IP1]] (-0.42, fdr 1e-04), [[SLC4A8]] (-0.42, fdr 2e-04), [[JMY]] (-0.40, fdr 6e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[SCARA5]] → it (grade C ⚠); 18 go from it, the strongest it → [[NCF2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14217.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.04×** | +10.9 | 5e-25 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.10×** | +9.9 | 1e-20 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.67×** | +8.4 | 6e-15 | 1/6 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +5.6 | 4e-06 | 3/7 (J82, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.9 | 0.013 | 0/7 | top dose only | cell-cycle shift (explains ~1% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.12×** | +3.8 | 0.016 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.01×** | +3.5 | 0.038 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.62×** | +3.4 | 0.046 | 1/7 (J82) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +3.4 | 0.046 | 0/7 | top dose only | cell-cycle shift (explains ~2% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.60×** | +3.3 | 0.053 | 6/7 (NCI-H460, H4, …) | two highest doses | low cells (technical?) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.2 | 0.068 | 1/7 (NCI-H460) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +3.2 | 0.068 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.87×** | +3.1 | 0.068 | 0/8 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.068 | 3/8 (J82, H4, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.34×** | +3.1 | 0.068 | 1/6 (NCI-H460) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.84×** | +3.1 | 0.081 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.54×** | +3.0 | 0.082 | 1/7 (HCT15) | inconsistent across doses | low cells (technical?) |
| [[Belzutifan (drug)]] 5 µM |  | **2.27×** | +3.0 | 0.082 | 4/6 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.57×** | +2.9 | 0.098 | 0/7 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14217.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (LoVo 0.109×, A-172 0.134×, CFPAC-1 0.109×, NCI-H460 0.204×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (NCI-H460 0.114×, H4 0.105×, A-172 0.183×); [[Panobinostat (drug)]] 5 µM in 3 lines (A-172 0.157×, NCI-H460 0.155×, LoVo 0.161×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.171×, H4 0.179×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.560×** | -4.1 | 0.024 | 7/8 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.603× | -3.3 | 0.20 | 0/8 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.636× | -3.2 | 0.20 | 6/8 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Diphenhydramine (drug)]] 5 µM |  | 0.632× | -3.1 | 0.20 | 0/8 | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.621× | -3.1 | 0.20 | 0/7 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14217. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 22.5 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.114× (z -11.9) |
| [[LoVo (line)]] | wt | 60.1 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -16.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.171× (z -13.5) |
| [[A-172 (line)]] | wt | 66.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -16.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.157× (z -10.5) |
| [[H4 (line)]] | wt | 40.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.651 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.716 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.640 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.758 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.735 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.628 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.432 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.516 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.744 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.665 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.543 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.646 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.578 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.541 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.797 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.732 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.494 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14217), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINB5]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[LINC02582]] | +0.58 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[COL4A6]] | +0.55 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[SLCO1B3]] | +0.54 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[DSG4]] | +0.54 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[DSG3]] | +0.53 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[TPTEP1-1]] | +0.53 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[CALB1]] | +0.50 | +0.38 / +0.47 | both halves | 7e-05 |  |
| [[PRSS3]] | +0.49 | +0.35 / +0.42 | both halves | 1e-04 |  |
| [[PSD3]] | +0.48 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[CTSE]] | +0.48 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[F3]] | +0.48 | +0.49 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIK3IP1]] | -0.42 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[SLC4A8]] | -0.42 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[JMY]] | -0.40 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[ANAPC1P2]] | -0.40 | -0.37 / -0.38 | both halves | 7e-05 |  |
| [[TNRC6B]] | -0.40 | -0.32 / -0.42 | both halves | 1e-04 |  |
| [[DHRS3]] | -0.38 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[ZBTB44]] | -0.37 | -0.34 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCARA5]] | C | SCARA5 activity raises ZNF736P9Y's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 4.25× lower at baseline in the lines without SCARA5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[SUCNR1]] | C | SUCNR1 activity raises ZNF736P9Y's level | lines that do not express SUCNR1 (44) vs lines expressing it (6) | 5.46× lower at baseline in the lines without SUCNR1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, TBXT, ENSG00000230258; co-absent with the target |
| [[GSG1L2]] | C | GSG1L2 activity raises ZNF736P9Y's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 3.91× lower at baseline in the lines without GSG1L2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises ZNF736P9Y's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 2.95× lower at baseline in the lines without LINC03000 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[GDA]] | C | GDA activity raises ZNF736P9Y's level | lines that do not express GDA (35) vs lines expressing it (15) | 1.79× lower at baseline in the lines without GDA | 0.035 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4; co-absent with the target |
| [[MYOM3]] | C | MYOM3 activity raises ZNF736P9Y's level | lines that do not express MYOM3 (27) vs lines expressing it (23) | 2.05× lower at baseline in the lines without MYOM3 | 0.049 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, USH1C; co-absent with the target |
| [[TBXT]] | C | TBXT activity raises ZNF736P9Y's level | lines that do not express TBXT (47) vs lines expressing it (3) | 3.85× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[C5orf46]] | C | C5orf46 activity raises ZNF736P9Y's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 2.52× lower at baseline in the lines without C5orf46 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[CTNND2]] | C | CTNND2 activity raises ZNF736P9Y's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 2.69× lower at baseline in the lines without CTNND2 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |
| [[LINC00824]] | C | LINC00824 activity raises ZNF736P9Y's level | lines that do not express LINC00824 (46) vs lines expressing it (4) | 2.38× lower at baseline in the lines without LINC00824 | 0.086 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SUCNR1, ENSG00000289530; co-absent with the target |
| [[GLP2R]] | C | GLP2R activity raises ZNF736P9Y's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 2.30× lower at baseline in the lines without GLP2R | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054; co-absent with the target |
| [[MMP28]] | C | MMP28 activity raises ZNF736P9Y's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without MMP28 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 1, C 17. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCF2]] | B | ZNF736P9Y activity raises NCF2's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 2.08× lower at baseline in the lines without ZNF736P9Y | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364 |
| [[SUCNR1]] | C | ZNF736P9Y activity raises SUCNR1's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 2.55× lower at baseline in the lines without ZNF736P9Y | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[SCARA5]] | C | ZNF736P9Y activity raises SCARA5's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 2.33× lower at baseline in the lines without ZNF736P9Y | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[CTNND2]] | C | ZNF736P9Y activity raises CTNND2's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 3.04× lower at baseline in the lines without ZNF736P9Y | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[TBXT]] | C | ZNF736P9Y activity raises TBXT's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 2.53× lower at baseline in the lines without ZNF736P9Y | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[LINC03000]] | C | ZNF736P9Y activity raises LINC03000's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 2.62× lower at baseline in the lines without ZNF736P9Y | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[GDA]] | C | ZNF736P9Y activity raises GDA's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 2.58× lower at baseline in the lines without ZNF736P9Y | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[GSG1L2]] | C | ZNF736P9Y activity raises GSG1L2's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 1.75× lower at baseline in the lines without ZNF736P9Y | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[GLP2R]] | C | ZNF736P9Y activity raises GLP2R's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 1.96× lower at baseline in the lines without ZNF736P9Y | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[GREM2]] | C | ZNF736P9Y activity raises GREM2's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 2.34× lower at baseline in the lines without ZNF736P9Y | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[LINC00589]] | C | ZNF736P9Y activity raises LINC00589's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 1.87× lower at baseline in the lines without ZNF736P9Y | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[C5orf46]] | C | ZNF736P9Y activity raises C5orf46's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 1.61× lower at baseline in the lines without ZNF736P9Y | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.515). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.9, 50.8); signed map (66.7, 8.1). **Vector** length 35.2, 13.0% of its response variance represented; |z| ≥ 3 in 241 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +10.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | -1.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +0.8 | +1.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.7 | +2.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.7 | +1.5 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -1.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -2.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.8 | +0.4 |
|  | [[Encorafenib (drug)]] 5 µM |  | -0.8 | -2.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.7 | -1.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -0.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 736 pseudogene 9, Y-linked |
| Locus type | pseudogene |
| Location | Yp11.2 — chrY:8,068,896-8,070,723 (-) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:38408](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:38408) · Entrez [100419726](https://www.ncbi.nlm.nih.gov/gene/100419726) · Ensembl [ENSG00000239893](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239893)

## Data

Gene col 14217: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14217); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14217, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14217]; `tensor/DDL_lfc|DDL_z.npy` [14217]; `embed/gene_vectors.npy` [14217]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14217 or target_col == 14217). Every well: [[ZNF736P9Y — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF736P9Y.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
