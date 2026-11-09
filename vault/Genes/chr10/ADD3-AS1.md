---
symbol: "ADD3-AS1"
type: "gene"
col: 12797
ensembl_id: "ENSG00000203876"
name: "ADD3 antisense RNA 1"
location: "10q25.1"
module: 44
arm: "+"
pooled_cpm: 3.01
n_lines_expressing: 41
n_dd_up: 25
n_dd_down: 22
n_dd_up_clean: 20
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 8
direction_downstream: 5
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# ADD3-AS1

*ADD3 antisense RNA 1* — 10q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.52× (z +16.6, q 0e+00, up in 18 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.467× (z -7.1, q 6e-10, down in 21 of 34 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP8B4]] (+0.63, fdr 1e-05), [[MGST2]] (+0.57, fdr 3e-05), [[ST6GALNAC1]] (+0.51, fdr 1e-04); moves opposite to [[RAD23A]] (-0.45, fdr 3e-04), [[R3HDM4]] (-0.44, fdr 1e-04), [[GGA1]] (-0.41, fdr 1e-03, ⚠ not reproduced), [[ST3GAL3]] (-0.41, fdr 1e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CA9]] → it (grade B ⚠); 5 go from it, the strongest it → [[CA9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12797.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.52×** | +16.6 | 0e+00 | 18/27 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.61×** | +11.5 | 4e-28 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.64×** | +7.9 | 5e-13 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +7.8 | 9e-13 | 5/16 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +7.8 | 9e-13 | 19/35 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.62×** | +6.3 | 2e-08 | 10/34 (A-427, HepG2/C3A, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.96×** | +6.3 | 3e-08 | 17/35 (HepG2/C3A, AsPC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.95×** | +6.2 | 4e-08 | 10/34 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.93×** | +6.1 | 6e-08 | 14/31 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.7 | 2e-04 | 8/36 (SW480, SW1417, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.61×** | +4.4 | 5e-04 | 9/34 (AsPC-1, HepG2/C3A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.006 | 5/21 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +3.7 | 0.011 | 9/36 (HepG2/C3A, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.016 | 7/25 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.038 | 6/35 (AsPC-1, LS 180, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.046 | 6/34 (HS-578T, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.046 | 2/25 (SW480, PANC-1) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.053 | 5/33 (AsPC-1, NCI-H460, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.053 | 2/37 (AsPC-1, LS 180) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12797.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.467×** | -7.1 | 6e-10 | 21/34 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.487×** | -6.7 | 5e-09 | 21/37 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.550×** | -5.6 | 4e-06 | 13/34 (NCI-H460, NCI-H661, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.598×** | -4.8 | 2e-04 | 16/32 (LS 180, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.601×** | -4.8 | 2e-04 | 15/33 (NCI-H460, hTERT-HPNE, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.590×** | -4.7 | 2e-04 | 14/31 (KATO III, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.622×** | -4.4 | 7e-04 | 17/24 (LS 180, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.642×** | -4.2 | 0.002 | 14/35 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.646×** | -4.1 | 0.003 | 8/37 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.653×** | -4.0 | 0.004 | 15/26 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.654×** | -4.0 | 0.004 | 6/38 (NCI-H460, AN3 CA, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.660×** | -3.9 | 0.005 | 17/33 (NCI-H460, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.751×** | -3.8 | 0.006 | 15/27 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.697×** | -3.4 | 0.029 | 10/36 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.504×** | -3.3 | 0.031 | 7/26 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.616×** | -3.2 | 0.043 | 3/37 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.703×** | -3.2 | 0.049 | 7/35 (SW1417, NCI-H23, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.788×** | -3.2 | 0.049 | 9/33 (KATO III, LS 180, …) | all doses, flat |  |
| [[Fluvoxamine (drug)]] 0.05 µM |  | **0.689×** | -3.0 | 0.065 | 3/34 (Panc 03.27, A-427, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.720×** | -2.9 | 0.093 | 10/30 (COLO 205, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12797. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.60 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0416× (z -12.7) |
| [[LS 180 (line)]] | wt | 19.6 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0976× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H1792 (line)]] | alt | 9.93 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0581× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.101× (z -8.7) |
| [[KATO III (line)]] | alt | 7.74 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0318× (z -12.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H1573 (line)]] | alt | 3.40 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 2.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +8.7) | — |
| [[A-172 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.710 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.739 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.980 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.496 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.451 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.943 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12797), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 7 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP8B4]] | +0.63 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[MGST2]] | +0.57 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[ST6GALNAC1]] | +0.51 | +0.45 / +0.33 | both halves | 1e-04 |  |
| [[ENPEP]] | +0.51 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[UGT1A6]] | +0.51 | +0.55 / +0.37 | both halves | 8e-05 |  |
| [[UGT1A9]] | +0.50 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[CARD14]] | +0.50 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[TSPAN8]] | +0.49 | +0.50 / +0.33 | both halves | 1e-04 |  |
| [[ALDH1A1]] | +0.49 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[UGT1A8]] | +0.49 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[LINC00534]] | +0.49 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[NXPH1]] | +0.48 | +0.41 / +0.44 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD23A]] | -0.45 | -0.28 / -0.31 | both halves | 3e-04 |  |
| [[R3HDM4]] | -0.44 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[GGA1]] | -0.41 | -0.18 / -0.43 | ⚠ not reproduced | 1e-03 |  |
| [[ST3GAL3]] | -0.41 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[DTNBP1]] | -0.41 | -0.28 / -0.30 | both halves | 3e-04 |  |
| [[DVL1]] | -0.41 | -0.22 / -0.45 | both halves | 6e-04 |  |
| [[METTL2B]] | -0.40 | -0.27 / -0.36 | both halves | 3e-04 |  |
| [[SUPT3H]] | -0.40 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[SAMD4B]] | -0.40 | -0.36 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA9]] | B | CA9 activity raises ADD3-AS1's level | lines that do not express CA9 (19) vs lines expressing it (31) | 1.64× lower at baseline in the lines without CA9 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |
| [[UGT1A1]] | B | UGT1A1 activity raises ADD3-AS1's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 1.95× lower at baseline in the lines without UGT1A1 | 0.046 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1 |
| [[UGT1A8]], [[UGT1A9]] | B | UGT1A8, UGT1A9 activity raises ADD3-AS1's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 1.80× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.064 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent genes |
| [[PAPSS2]] | B | PAPSS2 activity raises ADD3-AS1's level | lines that do not express PAPSS2 (15) vs lines expressing it (35) | 1.40× lower at baseline in the lines without PAPSS2 | 0.072 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, A4GALT, NT5E |
| [[UGT1A6]] | B | UGT1A6 activity raises ADD3-AS1's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 1.78× lower at baseline in the lines without UGT1A6 | 0.082 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1 |
| [[GASK1B]] | B | GASK1B activity raises ADD3-AS1's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 1.68× lower at baseline in the lines without GASK1B | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054 |
| [[MAP2K1]] | B | MAP2K1 activity lowers ADD3-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[ADD3]] | C | ADD3 activity raises ADD3-AS1's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 2.34× lower at baseline in the lines without ADD3 | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA9]] | B | ADD3-AS1 activity raises CA9's level | lines that do not express ADD3-AS1 (9) vs lines expressing it (41) | 4.21× lower at baseline in the lines without ADD3-AS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ADD3, ARHGAP23, ENSG00000286830; maybe low, not absent |
| [[WDR72]] | B | ADD3-AS1 activity raises WDR72's level | lines that do not express ADD3-AS1 (9) vs lines expressing it (41) | 2.54× lower at baseline in the lines without ADD3-AS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: ADD3, ARHGAP23, ENSG00000286830; maybe low, not absent |
| [[PTPN22]] | B | ADD3-AS1 activity raises PTPN22's level | lines that do not express ADD3-AS1 (9) vs lines expressing it (41) | 1.89× lower at baseline in the lines without ADD3-AS1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ADD3, ARHGAP23, ENSG00000286830; maybe low, not absent |
| [[BCL2L15]] | B | ADD3-AS1 activity raises BCL2L15's level | lines that do not express ADD3-AS1 (9) vs lines expressing it (41) | 1.74× lower at baseline in the lines without ADD3-AS1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ADD3, ARHGAP23, ENSG00000286830; maybe low, not absent |
| [[ADD3]] | C | ADD3-AS1 activity raises ADD3's level | lines that do not express ADD3-AS1 (9) vs lines expressing it (41) | 4.13× lower at baseline in the lines without ADD3-AS1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: ADD3, ARHGAP23, ENSG00000286830; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.503). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.5, 50.3); signed map (65.1, -0.7). **Vector** length 45.3, 6.31% of its response variance represented; |z| ≥ 3 in 944 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +16.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | -0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +6.3 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -5.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -3.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -0.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -3.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ADD3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10q25.1 — chr10:109,940,104-110,008,381 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48682](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48682) · Entrez [100505933](https://www.ncbi.nlm.nih.gov/gene/100505933) · Ensembl [ENSG00000203876](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203876)

## Data

Gene col 12797: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12797); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12797, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12797]; `tensor/DDL_lfc|DDL_z.npy` [12797]; `embed/gene_vectors.npy` [12797]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12797 or target_col == 12797). Every well: [[ADD3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADD3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
