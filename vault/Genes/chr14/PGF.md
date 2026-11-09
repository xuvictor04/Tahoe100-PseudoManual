---
symbol: "PGF"
type: "gene"
col: 4085
ensembl_id: "ENSG00000119630"
name: "placental growth factor"
location: "14q24.3"
module: 13
arm: "+"
pooled_cpm: 6.56
n_lines_expressing: 38
n_dd_up: 21
n_dd_down: 16
n_dd_up_clean: 12
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 9
direction_downstream: 4
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# PGF

*placental growth factor* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.71× (z +11.2, q 1e-26, up in 27 of 35 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 3.10× (z +9.7, q 5e-20, up in 24 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.588× (z -4.4, q 0.003, down in 12 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL6A2]] (+0.62, fdr 3e-05), [[RAC2]] (+0.62, fdr 1e-05), [[SLC22A17]] (+0.61, fdr 1e-05); moves opposite to [[ROS1]] (-0.55, fdr 4e-05), [[TGFB2]] (-0.54, fdr 3e-05), [[MYO16-AS1]] (-0.54, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CSPG4]] → it (grade B ⚠); 4 go from it, the strongest it → [[FAM167A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4085.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **3.71×** | +11.2 | 1e-26 | 27/35 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.69×** | +11.2 | 1e-26 | 25/34 (NCI-H2030, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **3.10×** | +9.7 | 5e-20 | 24/30 (SK-MEL-2, MIA PaCa-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.15×** | +9.3 | 3e-18 | 23/33 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.76×** | +8.7 | 4e-16 | 22/35 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **2.41×** | +7.5 | 4e-12 | 2/17 (A549, J82) | two highest doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.30×** | +6.9 | 6e-10 | 7/18 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.18×** | +6.7 | 1e-09 | 18/35 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **4.44×** | +6.7 | 1e-09 | 9/16 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.71×** | +6.5 | 5e-09 | 13/28 (CFPAC-1, SW1417, …) | top dose only | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.62×** | +5.9 | 2e-07 | 12/35 (NCI-H460, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.22×** | +4.9 | 5e-05 | 12/32 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +4.7 | 1e-04 | 14/34 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +4.3 | 7e-04 | 11/32 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +3.8 | 0.006 | 10/33 (KATO III, SW1417, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +3.7 | 0.007 | 12/31 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.71×** | +3.3 | 0.036 | 4/26 (RKO, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.46×** | +3.2 | 0.038 | 4/27 (SNU-423, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.61×** | +2.9 | 0.096 | 2/22 (Hs 766T, A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4085.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.588×** | -4.4 | 0.003 | 12/30 (A-172, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.600×** | -4.4 | 0.003 | 19/34 (NCI-H2030, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.646×** | -3.6 | 0.035 | 10/30 (CHP-212, SK-MEL-2, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.717×** | -3.6 | 0.035 | 14/33 (A-172, HS-578T, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.638×** | -3.6 | 0.035 | 13/35 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.601×** | -3.5 | 0.035 | 12/35 (A-172, HS-578T, …) | all doses, flat | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.664×** | -3.5 | 0.035 | 5/33 (Hs 766T, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.668×** | -3.5 | 0.035 | 12/34 (hTERT-HPNE, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.671×** | -3.4 | 0.035 | 11/35 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.572×** | -3.4 | 0.035 | 5/36 (HS-578T, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.757×** | -3.4 | 0.036 | 12/35 (hTERT-HPNE, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.676×** | -3.4 | 0.036 | 9/34 (A-172, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.686×** | -3.3 | 0.039 | 11/35 (A-172, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.497×** | -3.1 | 0.069 | 8/35 (HS-578T, A-172, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.501×** | -3.1 | 0.073 | 9/33 (HOP62, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.683×** | -3.0 | 0.086 | 5/34 (SW48, H4, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4085. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 28.7 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0215× (z -14.8) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0615× (z -10.8) |
| [[HOP62 (line)]] | alt | 36.9 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0824× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 39.3 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[hTERT-HPNE (line)]] | wt | 38.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0254× (z -12.5) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0581× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 1.72 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +10.0) ⚠ cell-cycle shift, explains ~80% of this change | — |
| [[SHP-77 (line)]] | alt | 10.0 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0523× (z -10.3) |
| [[A549 (line)]] | wt | 3.20 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +9.5) ⚠ cell-cycle shift, explains ~80% of this change | — |
| [[Hs 766T (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 4.59 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0873× (z -8.7) |
| [[SNU-423 (line)]] | alt | 7.59 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -9.7) ⚠ cell-cycle shift, explains ~80% of this change |
| [[A-427 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.488 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.911 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.963 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.539 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.468 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4085), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL6A2]] | +0.62 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[RAC2]] | +0.62 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[SLC22A17]] | +0.61 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[TSHZ3]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[INSYN2B]] | +0.59 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[MIR493HG]] | +0.58 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[METRNL]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[SHANK1]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[ARMCX2]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[DIRAS3]] | +0.57 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[RFX8]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[MEG3]] | +0.57 | +0.51 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROS1]] | -0.55 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[TGFB2]] | -0.54 | -0.45 / -0.52 | both halves | 3e-05 | STRING 558 |
| [[MYO16-AS1]] | -0.54 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[NFIB]] | -0.48 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[SLC12A2-DT]] | -0.47 | -0.45 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSPG4]] | B | CSPG4 activity raises PGF's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 2.26× lower at baseline in the lines without CSPG4 | 0.025 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1 |
| [[LINC01615]] | B | LINC01615 activity raises PGF's level | lines that do not express LINC01615 (36) vs lines expressing it (14) | 2.59× lower at baseline in the lines without LINC01615 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ENSG00000222032, GYPC |
| [[TNS1]] | B | TNS1 activity raises PGF's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 1.94× lower at baseline in the lines without TNS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[SHANK1]] | B | SHANK1 activity raises PGF's level | lines that do not express SHANK1 (22) vs lines expressing it (28) | 1.47× lower at baseline in the lines without SHANK1 | 0.045 | ⚠ within organs, on part of the lines; also absent: TRIML2, HOXD8, ENSG00000242880 |
| [[MAP2K1]] | B | MAP2K1 activity raises PGF's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[LINC03047]] | B | LINC03047 activity raises PGF's level | lines that do not express LINC03047 (28) vs lines expressing it (22) | 1.94× lower at baseline in the lines without LINC03047 | 0.082 | ⚠ within organs, on part of the lines; also absent: CNRIP1, ITGA4, INSYN2B |
| [[FLT1]] | B | FLT1 activity weakens PGF's drug response | lines that do not express FLT1 (20) vs lines expressing it (15) | the lines without FLT1 respond 5.67× as strongly (z diff -2.37); strongest at Dinaciclib 0.5 µM: 0.91x vs 0.20x (z diff -6.4) | 0.092 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB; target measured in part of the lines; artifact flags |
| [[DENND2A]] | B | DENND2A activity weakens PGF's drug response | lines that do not express DENND2A (18) vs lines expressing it (17) | the lines without DENND2A respond 6.86× as strongly (z diff -2.70); strongest at Homoharringtonine 5 µM: 1.77x vs 0.65x (z diff -5.0) | 0.093 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[GPR173]] | B | GPR173 activity raises PGF's level | lines that do not express GPR173 (30) vs lines expressing it (20) | 2.42× lower at baseline in the lines without GPR173 | 0.097 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM167A]] | B | PGF activity raises FAM167A's level | lines that do not express PGF (12) vs lines expressing it (38) | 2.03× lower at baseline in the lines without PGF | 0.067 | ⚠ within organs, on part of the lines; also absent: ZSCAN12, LOXL1, REEP2; maybe low, not absent |
| [[TNS1]] | B | PGF activity raises TNS1's level | lines that do not express PGF (12) vs lines expressing it (38) | 2.32× lower at baseline in the lines without PGF | 0.078 | ⚠ within organs, on part of the lines; also absent: ZSCAN12, LOXL1, REEP2; maybe low, not absent |
| [[SERPINE1]] | B | PGF activity raises SERPINE1's level | lines that do not express PGF (12) vs lines expressing it (38) | 4.14× lower at baseline in the lines without PGF | 0.079 | ⚠ within organs, on part of the lines; also absent: ZSCAN12, LOXL1, REEP2; maybe low, not absent |
| [[SARDH]] | B | PGF activity raises SARDH's level | lines that do not express PGF (12) vs lines expressing it (38) | 1.96× lower at baseline in the lines without PGF | 0.085 | ⚠ within organs, on part of the lines; also absent: ZSCAN12, LOXL1, REEP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.622). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.8, 14.2); signed map (23.2, 45.9). **Vector** length 90.7, 21.8% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.2 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +9.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.8 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +4.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.8 | +11.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +4.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +1.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.3 | +1.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.4 | -4.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.3 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -3.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.5 | -2.9 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | placental growth factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:74,941,834-74,955,626 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PlGF-2, SHGC-10760, D12S1900, PIGF, PLGF, PlGF; previously PGFL |
| Gene groups (HGNC) | VEGF family |
| Hallmark sets | HYPOXIA |
| Reactome | 4 pathways, smallest: VEGF binds to VEGFR leading to receptor dimerization; VEGF ligand-receptor interactions; Signaling by VEGF |
| Matched by | ensembl_id |

**Function**, from UniProt [P49763](https://www.uniprot.org/uniprotkb/P49763) (Placenta growth factor):

> Growth factor active in angiogenesis and endothelial cell growth, stimulating their proliferation and migration. It binds to the receptor FLT1/VEGFR-1. Isoform PlGF-2 binds NRP1/neuropilin-1 and NRP2/neuropilin-2 in a heparin-dependent manner. Also promotes cell tumor growth.

**Summary**, from NCBI Gene [5228](https://www.ncbi.nlm.nih.gov/gene/5228):

> Enables growth factor activity. Involved in positive regulation of cell population proliferation. Predicted to be located in extracellular region. Predicted to be active in obsolete extracellular space. Implicated in several diseases, including brain ischemia; diabetic neuropathy; glioblastoma; myocardial infarction; and pancreatic endocrine carcinoma. Biomarker of several diseases, including artery disease (multiple); arthritis (multiple); epilepsy (multiple); limited scleroderma; and …

**Accessions** — [HGNC:8893](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8893) · Entrez [5228](https://www.ncbi.nlm.nih.gov/gene/5228) · UniProt [P49763](https://www.uniprot.org/uniprotkb/P49763) · Ensembl [ENSG00000119630](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119630)

## Data

Gene col 4085: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4085); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4085, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4085]; `tensor/DDL_lfc|DDL_z.npy` [4085]; `embed/gene_vectors.npy` [4085]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4085 or target_col == 4085). Every well: [[PGF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
