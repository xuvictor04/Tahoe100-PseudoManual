---
symbol: "TAF1A"
type: "gene"
col: 6757
ensembl_id: "ENSG00000143498"
name: "TATA-box binding protein associated factor, RNA polymerase I subunit A"
location: "1q41"
module: 1
arm: "+"
pooled_cpm: 17.35
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 9
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TAF1A

*TATA-box binding protein associated factor, RNA polymerase I subunit A* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.99× (z +15.6, q 0e+00, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.702× (z -8.0, q 6e-13, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR3A]] (+0.67, fdr 7e-06), [[NLE1]] (+0.67, fdr 1e-05), [[DDX55]] (+0.64, fdr 1e-05); moves opposite to [[BMPR2]] (-0.61, fdr 1e-05), [[YPEL5]] (-0.60, fdr 1e-05), [[GNAS]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6757.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +15.6 | 0e+00 | 38/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.26×** | +13.1 | 2e-36 | 40/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.94×** | +10.6 | 6e-24 | 40/48 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.21×** | +9.8 | 2e-20 | 40/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.81×** | +9.5 | 2e-19 | 39/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.77×** | +9.2 | 5e-18 | 36/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.66×** | +8.2 | 2e-14 | 33/45 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +7.8 | 3e-13 | 34/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +5.4 | 4e-06 | 21/48 (NCI-H2347, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +4.9 | 4e-05 | 18/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.35×** | +4.8 | 8e-05 | 19/48 (NCI-H2030, HT-29, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +4.8 | 9e-05 | 20/47 (LoVo, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +4.4 | 4e-04 | 15/48 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.31×** | +4.4 | 5e-04 | 14/48 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.29×** | +4.1 | 0.001 | 16/47 (NCI-H1573, HCT15, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +4.0 | 0.002 | 12/48 (SW 900, A498, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.54×** | +3.6 | 0.009 | 6/47 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.013 | 15/47 (PANC-1, LS 180, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6757.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -8.0 | 6e-13 | 31/47 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.608×** | -7.4 | 4e-11 | 21/32 (RPMI-7951, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.637×** | -7.2 | 8e-11 | 23/40 (SHP-77, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.667×** | -6.3 | 5e-08 | 17/28 (A498, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.761×** | -4.9 | 9e-05 | 22/48 (SW480, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.753×** | -4.4 | 0.001 | 20/46 (RKO, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.773×** | -4.0 | 0.005 | 16/46 (LOX-IMVI, HepG2/C3A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.793×** | -4.0 | 0.006 | 13/48 (LoVo, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.801×** | -3.6 | 0.023 | 13/48 (SW480, KATO III, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.834× | -3.4 | 0.032 | 13/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.822× | -3.0 | 0.12 | 17/47 (NCI-H23, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6757. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 14.2 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -9.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 19.2 | 0 | 2 (1 ⚠) | — | [[Ixazomib (drug)]] 5 µM 0.0584× (z -10.0) |
| [[A498 (line)]] | wt | 23.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -10.4) |
| [[PANC-1 (line)]] | alt | 21.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +11.6) | — |
| [[SHP-77 (line)]] | alt | 38.9 | 0 | 2 (2 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0503× (z -11.8) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 18.2 | 0 | 2 | — | [[Temsirolimus (drug)]] 0.5 µM 0.127× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -9.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 9.30 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0891× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 17.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 18.6 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.125× (z -9.2) ⚠ toxic |
| [[J82 (line)]] | alt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 17.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -14.5) |
| [[NCI-H460 (line)]] | wt | 22.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.99× (z +8.7) | — |
| [[RKO (line)]] | wt | 18.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0950× (z -13.8) |
| [[RPMI-7951 (line)]] | alt | 19.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -11.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6757), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR3A]] | +0.67 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[NLE1]] | +0.67 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[DDX55]] | +0.64 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ZNHIT6]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[MPHOSPH6]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[RIOK1]] | +0.61 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[PAK1IP1]] | +0.60 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[RBM28]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[AGK]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[BRIX1]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[TAMM41]] | +0.59 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[ZNF283]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMPR2]] | -0.61 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[YPEL5]] | -0.60 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[GNAS]] | -0.59 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[C2]] | -0.58 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[PPM1B]] | -0.58 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[CDK19]] | -0.57 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[MKLN1]] | -0.54 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[CASTOR3P-1]] | -0.54 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[LINC02615]] | -0.53 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[ITM2B]] | -0.53 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[RC3H1]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[KDM6A]] | -0.53 | -0.40 / -0.51 | both halves | 5e-05 | pathway: Epigenetic regulation of gene expression |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises TAF1A's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds |
| [[MAP2K2]] | B | MAP2K2 activity raises TAF1A's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.476). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.5, -42.4); signed map (-8.9, -50.4). **Vector** length 75.0, 14.0% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +13.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.4 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | +3.4 | +4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.5 | +10.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +2.3 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +8.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +1.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -8.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -4.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -3.0 | +4.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -2.8 | +4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -4.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor, RNA polymerase I subunit A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:222,557,902-222,589,933 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TAFI48, SL1 |
| Reactome | 10 pathways, smallest: SIRT1 negatively regulates rRNA expression; RNA Polymerase I Transcription Termination; B-WICH complex positively regulates rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15573](https://www.uniprot.org/uniprotkb/Q15573) (TATA box-binding protein-associated factor RNA polymerase I subunit A):

> Component of the transcription factor SL1/TIF-IB complex, which is involved in the assembly of the PIC (pre-initiation complex) during RNA polymerase I-dependent transcription. The rate of PIC formation probably is primarily dependent on the rate of association of SL1/TIF-IB with the rDNA promoter. SL1/TIF-IB is involved in stabilization of nucleolar transcription factor 1/UBTF on rDNA. Formation of SL1/TIF-IB excludes the association of TBP with TFIID subunits.

**Summary**, from NCBI Gene [9015](https://www.ncbi.nlm.nih.gov/gene/9015):

> This gene encodes a subunit of the RNA polymerase I complex, Selectivity Factor I (SLI). The encoded protein is a TATA box-binding protein-associated factor that plays a role in the assembly of the RNA polymerase I preinitiation complex. Alternate splicing results in multiple transcript variants encoding multiple isoforms.[provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:11532](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11532) · Entrez [9015](https://www.ncbi.nlm.nih.gov/gene/9015) · UniProt [Q15573](https://www.uniprot.org/uniprotkb/Q15573) · Ensembl [ENSG00000143498](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143498)

## Data

Gene col 6757: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6757); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6757, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6757]; `tensor/DDL_lfc|DDL_z.npy` [6757]; `embed/gene_vectors.npy` [6757]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6757 or target_col == 6757). Every well: [[TAF1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
