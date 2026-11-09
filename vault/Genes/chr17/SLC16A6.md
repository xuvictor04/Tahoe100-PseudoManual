---
symbol: "SLC16A6"
type: "gene"
col: 3010
ensembl_id: "ENSG00000108932"
name: "solute carrier family 16 member 6"
location: "17q24.2"
module: 92
arm: "+"
pooled_cpm: 18.83
n_lines_expressing: 23
n_dd_up: 18
n_dd_down: 13
n_dd_up_clean: 15
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 22
direction_downstream: 16
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# SLC16A6

*solute carrier family 16 member 6* — 17q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.82× (z +13.4, q 2e-38, up in 10 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.404× (z -8.2, q 1e-13, down in 17 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARSG]] (+0.76, fdr 7e-06, ⚠ same locus), [[STEAP1B-AS1]] (+0.61, fdr 1e-05), [[SGIP1]] (+0.60, fdr 1e-05), [[GPR68]] (+0.56, fdr 1e-05); moves opposite to [[ENAH]] (-0.47, fdr 7e-05), [[PDLIM1]] (-0.46, fdr 9e-05), [[NXPE3]] (-0.46, fdr 6e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[CYGB]] → it (grade B ⚠); 16 go from it, the strongest it → [[ARSG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3010.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.82×** | +13.4 | 2e-38 | 10/19 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **2.61×** | +12.4 | 6e-33 | 17/21 (NCI-H460, SW1417, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **2.87×** | +9.6 | 1e-19 | 18/20 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **2.64×** | +8.9 | 9e-17 | 18/21 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +7.9 | 2e-13 | 7/20 (J82, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.32×** | +7.7 | 1e-12 | 2/16 (BT-474, HepG2/C3A) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **2.22×** | +7.3 | 2e-11 | 16/20 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.1 | 2e-05 | 10/20 (BT-474, hTERT-HPNE, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +5.1 | 2e-05 | 1/11 (J82) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.72×** | +5.0 | 4e-05 | 13/19 (HOP62, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +4.7 | 1e-04 | 0/10 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +4.4 | 5e-04 | 7/18 (BT-474, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.63×** | +4.3 | 6e-04 | 7/18 (SW480, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +4.2 | 1e-03 | 3/18 (SW1417, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[4EGI-1 (drug)]] 5 µM |  | **2.20×** | +3.4 | 0.022 | 8/16 (NCI-H460, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.039 | 6/21 (NCI-H460, RPMI-7951, …) | top dose only | plate-row cell shift |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.41×** | +3.2 | 0.051 | 1/21 (NCI-H1792) | inconsistent across doses |  |
| [[Meloxicam (drug)]] 0.05 µM |  | **1.39×** | +3.0 | 0.083 | 3/21 (RPMI-7951, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3010.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.404×** | -8.2 | 1e-13 | 17/20 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.434×** | -7.6 | 9e-12 | 18/20 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.451×** | -7.2 | 8e-11 | 16/21 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.569×** | -4.9 | 1e-04 | 15/19 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.587×** | -4.8 | 2e-04 | 14/21 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.613×** | -4.4 | 9e-04 | 12/20 (NCI-H460, SW 900, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.728×** | -4.0 | 0.006 | 9/20 (SW480, CHP-212, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.647×** | -3.9 | 0.006 | 12/20 (SW 900, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.711×** | -3.9 | 0.007 | 11/20 (SW480, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.645×** | -3.7 | 0.011 | 10/21 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.667×** | -3.7 | 0.013 | 5/21 (SW 900, SW480, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.682×** | -3.5 | 0.026 | 15/21 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.665×** | -3.4 | 0.028 | 10/20 (SW480, HOP62, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3010. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 184 | 0 | 16 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0221× (z -27.4) |
| [[SW 900 (line)]] | alt | 68.0 | 0 | 14 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0383× (z -16.5) |
| [[HOP62 (line)]] | alt | 38.2 | 0 | 12 (3 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0469× (z -14.4) |
| [[SW480 (line)]] | alt | 25.1 | 0 | 11 | — | [[Panobinostat (drug)]] 5 µM 0.131× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 64.6 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -15.4) |
| [[NCI-H1792 (line)]] | alt | 28.4 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0195× (z -18.2) |
| [[SNU-423 (line)]] | alt | 20.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0372× (z -13.4) |
| [[SW1417 (line)]] | alt | 30.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.126× (z -10.1) |
| [[BT-474 (line)]] | alt | 4.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.45× (z +9.2) | — |
| [[A-172 (line)]] | wt | 2.80 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.16 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.14 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.06 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3010), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARSG]] | +0.76 | +0.67 / +0.79 | both halves | 7e-06 | STRING 574; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[STEAP1B-AS1]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SGIP1]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[GPR68]] | +0.56 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[LINC02813]] | +0.55 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[IL1B]] | +0.55 | +0.56 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CNIH3]] | +0.55 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[ADAMTS9-AS2]] | +0.53 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[ANGPTL2]] | +0.52 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[CDH13]] | +0.52 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[LIF-AS2]] | +0.51 | +0.37 / +0.52 | both halves | 7e-05 |  |
| [[GNG11]] | +0.51 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[PAEP]] | +0.51 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENAH]] | -0.47 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[PDLIM1]] | -0.46 | -0.37 / -0.41 | both halves | 9e-05 |  |
| [[NXPE3]] | -0.46 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[SORT1]] | -0.45 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[CMKLR2]] | -0.44 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ABCC4]] | -0.43 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[MAP4]] | -0.42 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[PLCE1]] | -0.42 | -0.43 / -0.44 | both halves | 4e-05 |  |
| [[JDP2]] | -0.41 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[TBC1D1]] | -0.40 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[LARP1]] | -0.40 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[KPNA3]] | -0.40 | -0.35 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 8, C 14. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYGB]] | B | CYGB activity raises SLC16A6's level | lines that do not express CYGB (20) vs lines expressing it (30) | 2.43× lower at baseline in the lines without CYGB | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SLC16A6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TWIST2]] | B | TWIST2 activity raises SLC16A6's level | lines that do not express TWIST2 (26) vs lines expressing it (24) | 2.24× lower at baseline in the lines without TWIST2 | 0.052 | ⚠ within organs, on part of the lines; also absent: TSHZ3, STAC, SALL1 |
| [[ETV1]] | B | ETV1 activity raises SLC16A6's level | lines that do not express ETV1 (11) vs lines expressing it (39) | 2.36× lower at baseline in the lines without ETV1 | 0.059 | ⚠ within organs, on part of the lines; also absent: LINC02454, KATNAL1, CCDC136 |
| [[HDAC6]] | B | HDAC6 activity raises SLC16A6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ITGA1]] | B | ITGA1 activity raises SLC16A6's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 2.60× lower at baseline in the lines without ITGA1 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[SLC35G2]] | B | SLC35G2 activity raises SLC16A6's level | lines that do not express SLC35G2 (12) vs lines expressing it (38) | 2.23× lower at baseline in the lines without SLC35G2 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SMARCA1, LARP6, ZSCAN12 |
| [[LINC02454]] | B | LINC02454 activity raises SLC16A6's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 2.37× lower at baseline in the lines without LINC02454 | 0.097 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[WNT5A]] | C | WNT5A activity raises SLC16A6's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 3.37× lower at baseline in the lines without WNT5A | 0.003 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[IL6]] | C | IL6 activity raises SLC16A6's level | lines that do not express IL6 (32) vs lines expressing it (18) | 2.93× lower at baseline in the lines without IL6 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises SLC16A6's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 3.53× lower at baseline in the lines without CDH13 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[GNG11]] | C | GNG11 activity raises SLC16A6's level | lines that do not express GNG11 (21) vs lines expressing it (29) | 2.73× lower at baseline in the lines without GNG11 | 0.012 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 8, C 8. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARSG]] | B | SLC16A6 activity raises ARSG's level | lines that do not express SLC16A6 (27) vs lines expressing it (23) | 2.57× lower at baseline in the lines without SLC16A6 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENPP2, TMEM47, IGFBP7 |
| [[IL19]] | B | SLC16A6 activity raises IL19's level | lines that do not express SLC16A6 (27) vs lines expressing it (23) | 1.98× lower at baseline in the lines without SLC16A6 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENPP2, TMEM47, IGFBP7 |
| [[ETV1]] | B | SLC16A6 activity raises ETV1's level | lines that do not express SLC16A6 (27) vs lines expressing it (23) | 2.52× lower at baseline in the lines without SLC16A6 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENPP2, TMEM47, IGFBP7 |
| [[CYGB]] | B | SLC16A6 activity raises CYGB's level | lines that do not express SLC16A6 (27) vs lines expressing it (23) | 2.44× lower at baseline in the lines without SLC16A6 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENPP2, TMEM47, IGFBP7 |
| [[CMKLR2]] | B | SLC16A6 activity raises CMKLR2's level | lines that do not express SLC16A6 (27) vs lines expressing it (23) | 1.57× lower at baseline in the lines without SLC16A6 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENPP2, TMEM47, IGFBP7 |
| [[LINC02813]] | B | SLC16A6 activity raises LINC02813's level | lines that do not express SLC16A6 (27) vs lines expressing it (23) | 1.80× lower at baseline in the lines without SLC16A6 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENPP2, TMEM47, IGFBP7 |
| [[ABCC4]] | B | SLC16A6 activity lowers ABCC4's level | lines that do not express SLC16A6 (27) vs lines expressing it (23) | 1.51× higher at baseline in the lines without SLC16A6 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENPP2, TMEM47, IGFBP7 |
| cells under [[Pralsetinib (drug)]] 5 µM | B | SLC16A6 activity raises the cells' numbers under Pralsetinib 5 µM (protects the cells) | lines that do not express SLC16A6 (27) vs lines expressing it (21) | the lines without SLC16A6: 0.71× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENPP2, TMEM47, IGFBP7 |
| [[SHC4]] | C | SLC16A6 activity raises SHC4's level | lines that do not express SLC16A6 (27) vs lines expressing it (23) | 3.68× lower at baseline in the lines without SLC16A6 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENPP2, TMEM47, IGFBP7; co-absent with the target |
| [[SLC43A3]] | C | SLC16A6 activity raises SLC43A3's level | lines that do not express SLC16A6 (27) vs lines expressing it (23) | 3.89× lower at baseline in the lines without SLC16A6 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENPP2, TMEM47, IGFBP7; co-absent with the target |
| [[TMEM163]] | C | SLC16A6 activity raises TMEM163's level | lines that do not express SLC16A6 (27) vs lines expressing it (23) | 2.17× lower at baseline in the lines without SLC16A6 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENPP2, TMEM47, IGFBP7; co-absent with the target |
| [[ADAMTS9-AS2]] | C | SLC16A6 activity raises ADAMTS9-AS2's level | lines that do not express SLC16A6 (27) vs lines expressing it (23) | 3.38× lower at baseline in the lines without SLC16A6 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENPP2, TMEM47, IGFBP7; co-absent with the target |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.473). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.5, 16.3); signed map (20.2, 52.4). **Vector** length 85.2, 26.3% of its response variance represented; |z| ≥ 3 in 761 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +13.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.0 | +12.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +5.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.2 | +9.6 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +2.5 | +8.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.2 | +7.3 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +1.6 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +4.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +2.7 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.1 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -3.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.7 | -4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 16 member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.2 — chr17:68,267,026-68,291,267 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MCT6, MCT7 |
| Gene groups (HGNC) | Solute carrier family 16 |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [O15403](https://www.uniprot.org/uniprotkb/O15403) (Monocarboxylate transporter 7):

> Monocarboxylate transporter selective for taurine. May associate with BSG/CD147 or EMB/GP70 ancillary proteins to mediate facilitative efflux or influx of taurine across the plasma membrane. The transport is pH- and sodium-independent. Rather low-affinity, is likely effective for taurine transport in tissues where taurine is present at high concentrations.

**Summary**, from NCBI Gene [9120](https://www.ncbi.nlm.nih.gov/gene/9120):

> Predicted to enable monocarboxylic acid transmembrane transporter activity. Predicted to be involved in monocarboxylic acid transport. Predicted to be located in basolateral plasma membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10927](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10927) · Entrez [9120](https://www.ncbi.nlm.nih.gov/gene/9120) · UniProt [O15403](https://www.uniprot.org/uniprotkb/O15403) · Ensembl [ENSG00000108932](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108932)

## Data

Gene col 3010: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3010); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3010, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3010]; `tensor/DDL_lfc|DDL_z.npy` [3010]; `embed/gene_vectors.npy` [3010]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3010 or target_col == 3010). Every well: [[SLC16A6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC16A6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
