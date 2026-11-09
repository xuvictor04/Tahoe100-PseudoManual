---
symbol: "PRICKLE1"
type: "gene"
col: 6271
ensembl_id: "ENSG00000139174"
name: "prickle planar cell polarity protein 1"
location: "12q12"
module: 19
arm: "+"
pooled_cpm: 28.17
n_lines_expressing: 24
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 10
direction_downstream: 6
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# PRICKLE1

*prickle planar cell polarity protein 1* — 12q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.17× (z +11.3, q 1e-26, up in 17 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.592× (z -5.4, q 4e-05, down in 12 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLITRK4]] (+0.66, fdr 1e-05), [[COL4A6]] (+0.61, fdr 1e-05), [[CNTN1]] (+0.61, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[CSF2RA]] → it (grade B ⚠); 6 go from it, the strongest it → [[SPINK13]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6271.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.17×** | +11.3 | 1e-26 | 17/22 (NCI-H2347, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.45×** | +9.2 | 6e-18 | 14/22 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.28×** | +8.5 | 4e-15 | 13/22 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.15×** | +7.9 | 4e-13 | 13/22 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.84×** | +6.3 | 3e-08 | 13/22 (NCI-H2347, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.81×** | +6.1 | 9e-08 | 15/22 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.5 | 3e-06 | 7/22 (A498, A549, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.59×** | +4.8 | 1e-04 | 3/21 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.00×** | +3.7 | 0.012 | 13/22 (NCI-H2347, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.63×** | +3.6 | 0.017 | 1/21 (RPMI-7951) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.40×** | +3.4 | 0.040 | 1/17 (NCI-H2347) | all doses, stronger at high dose | composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.057 | 11/22 (Hs 766T, C32, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.25×** | +3.2 | 0.060 | 5/22 (NCI-H2347, A-172, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6271.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.592×** | -5.4 | 4e-05 | 12/22 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.655×** | -4.4 | 0.004 | 9/21 (NCI-H460, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.685×** | -3.9 | 0.016 | 5/22 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.687×** | -3.9 | 0.016 | 15/22 (NCI-H460, Hs 766T, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.709×** | -3.5 | 0.044 | 10/22 (NCI-H460, C32, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.725×** | -3.3 | 0.086 | 15/22 (C32, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.741× | -3.1 | 0.16 | 12/22 (NCI-H460, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | 0.567× | -3.1 | 0.16 | 8/21 (NCI-H460, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6271. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 152 | 0 | 24 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -21.5) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0597× (z -18.8) |
| [[C-33 A (line)]] | alt | 657 | 0 | 12 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0209× (z -36.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -19.6) |
| [[HEC-1-A (line)]] | alt | 105 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H2347 (line)]] | alt | 8.30 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 5.95× (z +12.3) | — |
| [[C32 (line)]] | wt | 25.4 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0726× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 54.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A549 (line)]] | wt | 7.21 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0737× (z -10.9) |
| [[Hs 766T (line)]] | wt | 39.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.172× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 7.77 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.69× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 77.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.25 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.84 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.97 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.13 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.95 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.11 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.67 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.51 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.37 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.47 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.47 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.60 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.82 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6271), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLITRK4]] | +0.66 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[COL4A6]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[CNTN1]] | +0.61 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[KCNK2]] | +0.60 | +0.57 / +0.65 | both halves | 8e-06 |  |
| [[GREM2]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[TENM1]] | +0.59 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CDH7]] | +0.59 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[MEF2C]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[FENDRR]] | +0.58 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[LINC03000]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[PAK3]] | +0.58 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[ST8SIA4]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 1, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSF2RA]] | B | CSF2RA activity raises PRICKLE1's level | lines that do not express CSF2RA (28) vs lines expressing it (22) | 1.41× lower at baseline in the lines without CSF2RA | 0.091 | ⚠ within organs, on part of the lines; also absent: CPS1, KBTBD12, WNT7A |
| [[MARCOL]], [[SPINK13]] | C | MARCOL, SPINK13 activity raises PRICKLE1's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 2.63× lower at baseline in the lines without MARCOL, SPINK13 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[MN1]] | C | MN1 activity raises PRICKLE1's level | lines that do not express MN1 (21) vs lines expressing it (29) | 3.04× lower at baseline in the lines without MN1 | 0.030 | ⚠ within organs, on part of the lines; also absent: FHL1, COL7A1, ABI3BP; co-absent with the target |
| [[GLP2R]] | C | GLP2R activity raises PRICKLE1's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 3.98× lower at baseline in the lines without GLP2R | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054; co-absent with the target |
| [[LINC02742]] | C | LINC02742 activity raises PRICKLE1's level | lines that do not express LINC02742 (34) vs lines expressing it (16) | 2.58× lower at baseline in the lines without LINC02742 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000255029, ENSG00000254526, ENSG00000255227; co-absent with the target |
| [[C5orf46]] | C | C5orf46 activity raises PRICKLE1's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 1.89× lower at baseline in the lines without C5orf46 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[TBXT]] | C | TBXT activity raises PRICKLE1's level | lines that do not express TBXT (47) vs lines expressing it (3) | 5.23× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[NALCN]] | C | NALCN activity raises PRICKLE1's level | lines that do not express NALCN (22) vs lines expressing it (28) | 2.02× lower at baseline in the lines without NALCN | 0.078 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229; co-absent with the target |
| [[P3H2]] | C | P3H2 activity raises PRICKLE1's level | lines that do not express P3H2 (28) vs lines expressing it (22) | 1.40× lower at baseline in the lines without P3H2 | 0.095 | ⚠ within organs, on part of the lines; also absent: P3H2-AS1, SRGN, SPOCK1; co-absent with the target |
| [[FENDRR]] | C | FENDRR activity raises PRICKLE1's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 1.97× lower at baseline in the lines without FENDRR | 0.0996 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPINK13]] | C | PRICKLE1 activity raises SPINK13's level | lines that do not express PRICKLE1 (26) vs lines expressing it (24) | 1.52× lower at baseline in the lines without PRICKLE1 | 0.009 | ⚠ within organs, on part of the lines; also absent: COL4A2, NR0B1, THBD; co-absent with the target |
| [[MARCOL]] | C | PRICKLE1 activity raises MARCOL's level | lines that do not express PRICKLE1 (26) vs lines expressing it (24) | 1.45× lower at baseline in the lines without PRICKLE1 | 0.013 | ⚠ within organs, on part of the lines; also absent: COL4A2, NR0B1, THBD; co-absent with the target |
| [[DDIT4L]] | C | PRICKLE1 activity raises DDIT4L's level | lines that do not express PRICKLE1 (26) vs lines expressing it (24) | 1.71× lower at baseline in the lines without PRICKLE1 | 0.029 | ⚠ within organs, on part of the lines; also absent: COL4A2, NR0B1, THBD; co-absent with the target |
| [[P3H2]] | C | PRICKLE1 activity raises P3H2's level | lines that do not express PRICKLE1 (26) vs lines expressing it (24) | 2.73× lower at baseline in the lines without PRICKLE1 | 0.034 | ⚠ within organs, on part of the lines; also absent: COL4A2, NR0B1, THBD; co-absent with the target |
| [[NALCN]] | C | PRICKLE1 activity raises NALCN's level | lines that do not express PRICKLE1 (26) vs lines expressing it (24) | 3.48× lower at baseline in the lines without PRICKLE1 | 0.036 | ⚠ within organs, on part of the lines; also absent: COL4A2, NR0B1, THBD; co-absent with the target |
| [[TSPAN2]] | C | PRICKLE1 activity raises TSPAN2's level | lines that do not express PRICKLE1 (26) vs lines expressing it (24) | 1.55× lower at baseline in the lines without PRICKLE1 | 0.061 | ⚠ within organs, on part of the lines; also absent: COL4A2, NR0B1, THBD; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.2, 34.7); signed map (41.4, 44.7). **Vector** length 68.1, 18.2% of its response variance represented; |z| ≥ 3 in 631 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +11.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.2 | +4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +2.9 | +3.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +2.8 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.4 | +1.8 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.0 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | prickle planar cell polarity protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q12 — chr12:42,456,757-42,590,355 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31937, EPM1B, RILP |
| Gene groups (HGNC) | Prickle planar cell polarity proteins; LIM domain containing |
| Reactome | 4 pathways, smallest: Asymmetric localization of PCP proteins; PCP/CE pathway; Beta-catenin independent WNT signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MT3](https://www.uniprot.org/uniprotkb/Q96MT3) (Prickle-like protein 1):

> Involved in the planar cell polarity pathway that controls convergent extension during gastrulation and neural tube closure. Convergent extension is a complex morphogenetic process during which cells elongate, move mediolaterally, and intercalate between neighboring cells, leading to convergence toward the mediolateral axis and extension along the anteroposterior axis. Necessary for nuclear localization of REST. May serve as nuclear receptor.

**Summary**, from NCBI Gene [144165](https://www.ncbi.nlm.nih.gov/gene/144165):

> This gene encodes a nuclear receptor that may be a negative regulator of the Wnt/beta-catenin signaling pathway. The encoded protein localizes to the nuclear membrane and has been implicated in the nuclear trafficking of the transcription repressors REST/NRSF and REST4. Mutations in this gene have been linked to progressive myoclonus epilepsy. Alternate splicing results in multiple transcript variants. A pseudogene of this gene is found on chromosome 3. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:17019](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17019) · Entrez [144165](https://www.ncbi.nlm.nih.gov/gene/144165) · UniProt [Q96MT3](https://www.uniprot.org/uniprotkb/Q96MT3) · Ensembl [ENSG00000139174](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139174)

## Data

Gene col 6271: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6271); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6271, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6271]; `tensor/DDL_lfc|DDL_z.npy` [6271]; `embed/gene_vectors.npy` [6271]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6271 or target_col == 6271). Every well: [[PRICKLE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRICKLE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
