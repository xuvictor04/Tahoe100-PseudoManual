---
symbol: "ST8SIA4"
type: "gene"
col: 3470
ensembl_id: "ENSG00000113532"
name: "ST8 alpha-N-acetyl-neuraminide alpha-2,8-sialyltransferase 4"
location: "5q21.1"
module: 19
arm: "+"
pooled_cpm: 10.03
n_lines_expressing: 23
n_dd_up: 16
n_dd_down: 19
n_dd_up_clean: 11
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 13
direction_downstream: 5
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# ST8SIA4

*ST8 alpha-N-acetyl-neuraminide alpha-2,8-sialyltransferase 4* — 5q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.76× (z +10.8, q 2e-24, up in 2 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.76× (z +8.5, q 4e-15, up in 14 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.388× (z -10.1, q 5e-21, down in 19 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAK3]] (+0.70, fdr 7e-06), [[SFMBT2]] (+0.68, fdr 7e-06), [[TENM1]] (+0.64, fdr 1e-05); moves opposite to [[TMBIM1]] (-0.48, fdr 5e-05), [[HMGA1P4]] (-0.47, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[LIMCH1]] → it (grade B ⚠); 5 go from it, the strongest it → [[LIMCH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3470.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.76×** | +10.8 | 2e-24 | 2/16 (NCI-H1573, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.76×** | +8.5 | 4e-15 | 14/19 (PANC-1, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.22×** | +8.5 | 4e-15 | 16/19 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +8.1 | 9e-14 | 1/12 (LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.88×** | +6.7 | 2e-09 | 11/19 (SK-MEL-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +5.8 | 7e-07 | 1/13 (NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.69×** | +5.6 | 2e-06 | 13/19 (NCI-H1792, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +5.6 | 2e-06 | 13/19 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.002 | 2/18 (SNU-423, HOP62) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.003 | 11/19 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +3.8 | 0.009 | 7/19 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.91×** | +3.6 | 0.015 | 10/19 (PANC-1, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.3 | 0.039 | 0/18 | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.54×** | +3.3 | 0.045 | 0/16 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.049 | 0/19 | inconsistent across doses |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.050 | 2/18 (PANC-1, NCI-H1792) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3470.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.388×** | -10.1 | 5e-21 | 19/19 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.534×** | -6.7 | 8e-09 | 14/19 (NCI-H460, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.579×** | -5.8 | 1e-06 | 16/19 (Panc 03.27, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.583×** | -5.7 | 1e-06 | 12/19 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.722×** | -4.9 | 1e-04 | 14/19 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.636×** | -4.8 | 1e-04 | 11/19 (NCI-H460, SW 900, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.655×** | -4.5 | 5e-04 | 16/20 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.666×** | -4.3 | 0.001 | 10/19 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.672×** | -4.2 | 0.001 | 12/19 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.694×** | -3.9 | 0.005 | 9/19 (SNU-423, NCI-H460, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.684×** | -3.9 | 0.005 | 8/19 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mebendazole (drug)]] 5 µM |  | **0.688×** | -3.8 | 0.006 | 5/19 (SHP-77, SK-MEL-2, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **0.708×** | -3.7 | 0.010 | 8/19 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.712×** | -3.6 | 0.012 | 8/19 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.708×** | -3.4 | 0.025 | 2/20 (NCI-H460, SNU-423) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.726×** | -3.3 | 0.035 | 10/19 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.748×** | -3.1 | 0.064 | 4/19 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3470. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 61.2 | 0 | 16 (8 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0901× (z -13.9) |
| [[SHP-77 (line)]] | alt | 64.3 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0380× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.111× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 20.5 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.119× (z -12.7) |
| [[C32 (line)]] | wt | 10.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0634× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0726× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 45.7 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.182× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 15.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0524× (z -13.6) |
| [[H4 (line)]] | wt | 34.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0984× (z -10.2) ⚠ cell-cycle shift, explains ~19% of this change |
| [[LS 180 (line)]] | wt | 17.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.202× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~16% of this change |
| [[Panc 03.27 (line)]] | alt | 6.28 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0595× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 17.6 | 0 | 1 | — | [[vincristine (drug)]] 0.5 µM 0.0544× (z -9.6) |
| [[A-172 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.805 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.832 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.796 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.756 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.810 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.855 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.924 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.794 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3470), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAK3]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[SFMBT2]] | +0.68 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[TENM1]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[EPHA3]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[GPRIN3]] | +0.63 | +0.57 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[SLITRK4]] | +0.62 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[SLITRK5]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[GRAMD1B]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[TCF4]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ACSS3]] | +0.61 | +0.42 / +0.61 | both halves | 4e-05 | same gene group |
| [[UNC5D]] | +0.60 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[PTPRD]] | +0.59 | +0.61 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMBIM1]] | -0.48 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[HMGA1P4]] | -0.47 | -0.35 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 3, C 10. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LIMCH1]] | B | LIMCH1 activity raises ST8SIA4's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without LIMCH1 | 0.037 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[PLAC4]] | B | PLAC4 activity raises ST8SIA4's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 1.87× lower at baseline in the lines without PLAC4 | 0.093 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |
| [[UNC13A]] | B | UNC13A activity lowers ST8SIA4's level | lines that do not express UNC13A (29) vs lines expressing it (21) | 1.05× higher at baseline in the lines without UNC13A | 0.095 | ⚠ within organs, on part of the lines; also absent: CDH19, LINC02864, SCG3; maybe low, not absent |
| [[ADGRB3]] | C | ADGRB3 activity raises ST8SIA4's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 5.03× lower at baseline in the lines without ADGRB3 | 0.001 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4; co-absent with the target |
| [[NCAM2]] | C | NCAM2 activity raises ST8SIA4's level | lines that do not express NCAM2 (24) vs lines expressing it (26) | 3.28× lower at baseline in the lines without NCAM2 | 0.028 | ⚠ within organs, on part of the lines; also absent: MMP16, ADGRB3, FAP; co-absent with the target |
| [[TCF4]] | C | TCF4 activity raises ST8SIA4's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 3.51× lower at baseline in the lines without TCF4 | 0.035 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[TRPA1]] | C | TRPA1 activity raises ST8SIA4's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 3.79× lower at baseline in the lines without TRPA1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises ST8SIA4's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 3.88× lower at baseline in the lines without DPP10 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[CLDN10-AS1]] | C | CLDN10-AS1 activity raises ST8SIA4's level | lines that do not express CLDN10-AS1 (31) vs lines expressing it (19) | 2.17× lower at baseline in the lines without CLDN10-AS1 | 0.063 | ⚠ within organs, on part of the lines; also absent: ADGRD1, AMBP, NPSR1-AS1; co-absent with the target |
| [[EPHA3]] | C | EPHA3 activity raises ST8SIA4's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 3.06× lower at baseline in the lines without EPHA3 | 0.066 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491; co-absent with the target |
| [[LINC00461]] | C | LINC00461 activity raises ST8SIA4's level | lines that do not express LINC00461 (22) vs lines expressing it (28) | 3.32× lower at baseline in the lines without LINC00461 | 0.069 | ⚠ within organs, on part of the lines; also absent: NPTX2, EYA1, CELF4; maybe low, not absent; co-absent with the target |
| [[ADGRD1]] | C | ADGRD1 activity raises ST8SIA4's level | lines that do not express ADGRD1 (37) vs lines expressing it (13) | 2.76× lower at baseline in the lines without ADGRD1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, SLC15A5; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LIMCH1]] | B | ST8SIA4 activity raises LIMCH1's level | lines that do not express ST8SIA4 (27) vs lines expressing it (23) | 2.23× lower at baseline in the lines without ST8SIA4 | 0.054 | ⚠ within organs, on part of the lines; also absent: ADGRB3, SEMA3E, TRPA1 |
| [[ADGRB3]] | C | ST8SIA4 activity raises ADGRB3's level | lines that do not express ST8SIA4 (27) vs lines expressing it (23) | 6.04× lower at baseline in the lines without ST8SIA4 | 0.018 | ⚠ within organs, on part of the lines; also absent: ADGRB3, SEMA3E, TRPA1; co-absent with the target |
| [[EYA1]] | C | ST8SIA4 activity raises EYA1's level | lines that do not express ST8SIA4 (27) vs lines expressing it (23) | 5.01× lower at baseline in the lines without ST8SIA4 | 0.039 | ⚠ within organs, on part of the lines; also absent: ADGRB3, SEMA3E, TRPA1; co-absent with the target |
| [[EPHA3]] | C | ST8SIA4 activity raises EPHA3's level | lines that do not express ST8SIA4 (27) vs lines expressing it (23) | 4.23× lower at baseline in the lines without ST8SIA4 | 0.060 | ⚠ within organs, on part of the lines; also absent: ADGRB3, SEMA3E, TRPA1; co-absent with the target |
| [[EDNRB]] | C | ST8SIA4 activity raises EDNRB's level | lines that do not express ST8SIA4 (27) vs lines expressing it (23) | 2.13× lower at baseline in the lines without ST8SIA4 | 0.078 | ⚠ within organs, on part of the lines; also absent: ADGRB3, SEMA3E, TRPA1; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.8, 33.7); signed map (39.1, 39.8). **Vector** length 72.5, 22.4% of its response variance represented; |z| ≥ 3 in 634 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +10.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +0.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +1.2 |
|  | [[Glycyrrhizic acid (drug)]] 0.05 µM |  | +1.4 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +3.6 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | -10.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.2 | -2.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ST8 alpha-N-acetyl-neuraminide alpha-2,8-sialyltransferase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q21.1 — chr5:100,806,933-100,903,282 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PST, PST1; previously SIAT8D |
| Gene groups (HGNC) | Sialyltransferases; MicroRNA protein coding host genes |
| Hallmark sets | ALLOGRAFT_REJECTION, INTERFERON_GAMMA_RESPONSE |
| Reactome | 8 pathways, smallest: NCAM1 interactions; Sialic acid metabolism; NCAM signaling for neurite out-growth |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92187](https://www.uniprot.org/uniprotkb/Q92187) (CMP-N-acetylneuraminate-poly-alpha-2,8-sialyltransferase):

> Catalyzes the transfer of a sialic acid from a CMP-linked sialic acid donor onto a terminal alpha-2,3-, alpha-2,6-, or alpha-2,8-linked sialic acid of an N-linked glycan protein acceptor through alpha-2,8-linkages. Therefore, participates in polysialic acid synthesis on various sialylated N-acetyllactosaminyl oligosaccharides, including NCAM1 N-glycans, FETUB N-glycans and AHSG. It is noteworthy that alpha-2,3-linked sialic acid is apparently a better acceptor than alpha-2,6-linked sialic acid.

**Summary**, from NCBI Gene [7903](https://www.ncbi.nlm.nih.gov/gene/7903):

> The protein encoded by this gene catalyzes the polycondensation of alpha-2,8-linked sialic acid required for the synthesis of polysialic acid, a modulator of the adhesive properties of neural cell adhesion molecule (NCAM1). The encoded protein, which is a member of glycosyltransferase family 29, is a type II membrane protein that may be present in the Golgi apparatus. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10871](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10871) · Entrez [7903](https://www.ncbi.nlm.nih.gov/gene/7903) · UniProt [Q92187](https://www.uniprot.org/uniprotkb/Q92187) · Ensembl [ENSG00000113532](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113532)

## Data

Gene col 3470: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3470); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3470, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3470]; `tensor/DDL_lfc|DDL_z.npy` [3470]; `embed/gene_vectors.npy` [3470]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3470 or target_col == 3470). Every well: [[ST8SIA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST8SIA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
