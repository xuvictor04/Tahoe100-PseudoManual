---
symbol: "SULT1C2"
type: "gene"
col: 12552
ensembl_id: "ENSG00000198203"
name: "sulfotransferase family 1C member 2"
location: "2q12.3"
module: 55
arm: "+"
pooled_cpm: 4.99
n_lines_expressing: 20
n_dd_up: 22
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 32
direction_downstream: 51
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# SULT1C2

*sulfotransferase family 1C member 2* — 2q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 3.45× (z +15.0, q 0e+00, up in 17 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.425× (z -7.3, q 2e-10, down in 13 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFRSF14-AS1]] (+0.70, fdr 1e-05), [[KCTD14]] (+0.65, fdr 7e-06), [[FGD3]] (+0.64, fdr 7e-06); moves opposite to [[SRGAP2C]] (-0.54, fdr 3e-05), [[RSKR]] (-0.51, fdr 4e-05), [[PGP]] (-0.49, fdr 4e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[NOD2]] → it (grade B ⚠); 51 go from it, the strongest it → [[FUT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12552.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **3.45×** | +15.0 | 0e+00 | 17/17 (LS 180, LoVo, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **3.38×** | +10.4 | 5e-23 | 17/17 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **3.03×** | +9.5 | 5e-19 | 16/16 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **2.91×** | +9.2 | 8e-18 | 17/17 (LS 180, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.62×** | +7.9 | 2e-13 | 1/7 (KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +7.8 | 5e-13 | 2/11 (HEC-1-A, AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +6.2 | 4e-08 | 7/16 (A-172, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +6.2 | 5e-08 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +4.3 | 0.001 | 2/11 (SK-MEL-2, SW 900) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +3.9 | 0.006 | 9/17 (SW 900, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.62×** | +3.8 | 0.007 | 0/13 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +3.4 | 0.028 | 0/11 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.50×** | +3.3 | 0.038 | 7/17 (COLO 205, LS 180, …) | top dose only | plate-row cell shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.043 | 7/17 (SK-MEL-2, SNU-423, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.044 | 4/16 (SW 900, LoVo, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.48×** | +3.2 | 0.044 | 4/16 (COLO 205, SW480, …) | top dose only | position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.45×** | +3.2 | 0.048 | 0/13 | inconsistent across doses | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.062 | 4/17 (SW480, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +3.0 | 0.070 | 5/17 (SW480, NCI-H2347, …) | all doses, flat |  |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.41×** | +2.9 | 0.085 | 0/15 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12552.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.425×** | -7.3 | 2e-10 | 13/16 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.590×** | -4.5 | 0.002 | 12/17 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.601×** | -4.3 | 0.003 | 14/16 (LoVo, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.635×** | -3.9 | 0.016 | 11/16 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.642×** | -3.8 | 0.018 | 12/17 (LoVo, LS 180, …) | all doses, flat | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | **0.676×** | -3.3 | 0.082 | 3/16 (HCT15, SW 900, …) | rises with dose |  |
| [[Flumatinib (mesylate) (drug)]] 0.5 µM |  | **0.683×** | -3.2 | 0.094 | 2/17 (H4, SNU-423) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.768× | -3.2 | 0.11 | 4/17 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.694× | -3.1 | 0.12 | 6/17 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~25% here); position effect removed |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.701× | -3.0 | 0.14 | 0/17 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12552. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 24.0 | 2 | 9 (6 ⚠) | [[Selinexor (drug)]] 5 µM 3.89× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -16.1) |
| [[LS 180 (line)]] | wt | 20.9 | 4 | 7 (6 ⚠) | [[Selinexor (drug)]] 5 µM 7.61× (z +16.0) | [[Panobinostat (drug)]] 5 µM 0.158× (z -10.4) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.170× (z -10.0) |
| [[SW480 (line)]] | alt | 9.91 | 3 | 8 (7 ⚠) | [[Selinexor (drug)]] 5 µM 4.36× (z +10.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0430× (z -16.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0696× (z -13.7) |
| [[SNU-423 (line)]] | alt | 38.9 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0854× (z -11.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 22.4 | 1 | 4 (2 ⚠) | [[Selinexor (drug)]] 5 µM 4.78× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.0513× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.100× (z -9.4) |
| [[SW1417 (line)]] | alt | 5.64 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0340× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 2.98 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0707× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 6.71 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0530× (z -9.2) ⚠ cell-cycle shift, explains ~84% of this change |
| [[A-172 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.479 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.935 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.840 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.872 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.645 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.674 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.973 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.944 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.611 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.579 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.819 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.622 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.658 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12552), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF14-AS1]] | +0.70 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[KCTD14]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[FGD3]] | +0.64 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[PLCH1]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[LPAR5]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[A1CF]] | +0.62 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[TNFRSF14]] | +0.61 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[STK32A]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[TPRXL]] | +0.61 | +0.66 / +0.46 | both halves | 3e-05 |  |
| [[ABO]] | +0.60 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[FUT2]] | +0.60 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[ARHGEF38]] | +0.59 | +0.66 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGAP2C]] | -0.54 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[RSKR]] | -0.51 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[PGP]] | -0.49 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[SLC27A4]] | -0.49 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 6, C 26. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOD2]] | B | NOD2 activity raises SULT1C2's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 1.89× lower at baseline in the lines without NOD2 | 0.019 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[FUT2]] | B | FUT2 activity raises SULT1C2's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 2.37× lower at baseline in the lines without FUT2 | 0.044 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises SULT1C2's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.21× lower at baseline in the lines without ELF3-AS1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[PSTPIP2]] | B | PSTPIP2 activity raises SULT1C2's level | lines that do not express PSTPIP2 (20) vs lines expressing it (30) | 1.67× lower at baseline in the lines without PSTPIP2 | 0.054 | ⚠ within organs, on part of the lines; also absent: NEDD9, CARD11, BCAT1 |
| [[SEC16B]] | B | SEC16B activity raises SULT1C2's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 2.06× lower at baseline in the lines without SEC16B | 0.082 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |
| [[HDAC6]] | B | HDAC6 activity raises SULT1C2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HKDC1]] | C | HKDC1 activity raises SULT1C2's level | lines that do not express HKDC1 (30) vs lines expressing it (20) | 2.94× lower at baseline in the lines without HKDC1 | 0.008 | ⚠ within organs, on part of the lines; also absent: HHLA2, GCNT3, HNF4A; co-absent with the target |
| [[TNFRSF14-AS1]] | C | TNFRSF14-AS1 activity raises SULT1C2's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 2.72× lower at baseline in the lines without TNFRSF14-AS1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises SULT1C2's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.74× lower at baseline in the lines without TMPRSS2 | 0.013 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[C11orf52]] | C | C11orf52 activity raises SULT1C2's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 2.48× lower at baseline in the lines without C11orf52 | 0.018 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39; co-absent with the target |
| [[ANO9]] | C | ANO9 activity raises SULT1C2's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 2.41× lower at baseline in the lines without ANO9 | 0.019 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29; co-absent with the target |
| [[ILDR1]] | C | ILDR1 activity raises SULT1C2's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 2.18× lower at baseline in the lines without ILDR1 | 0.023 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1; co-absent with the target |

### Downstream of this gene

*51 arrows, 51 of them with an alert ⚠; grade A 0, B 10, C 41. Shown: the 12 strongest; 39 more arrows (39 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FUT2]] | B | SULT1C2 activity raises FUT2's level | lines that do not express SULT1C2 (30) vs lines expressing it (20) | 2.20× lower at baseline in the lines without SULT1C2 | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC03040, EPS8L3, TMEM139 |
| [[LPAR5]] | B | SULT1C2 activity raises LPAR5's level | lines that do not express SULT1C2 (30) vs lines expressing it (20) | 2.20× lower at baseline in the lines without SULT1C2 | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC03040, EPS8L3, TMEM139 |
| [[ABCC6]] | B | SULT1C2 activity raises ABCC6's level | lines that do not express SULT1C2 (30) vs lines expressing it (20) | 1.62× lower at baseline in the lines without SULT1C2 | 0.015 | ⚠ within organs, on part of the lines; also absent: LINC03040, EPS8L3, TMEM139 |
| [[SLC44A3]] | B | SULT1C2 activity raises SLC44A3's level | lines that do not express SULT1C2 (30) vs lines expressing it (20) | 2.11× lower at baseline in the lines without SULT1C2 | 0.017 | ⚠ within organs, on part of the lines; also absent: LINC03040, EPS8L3, TMEM139 |
| [[VILL]] | B | SULT1C2 activity raises VILL's level | lines that do not express SULT1C2 (30) vs lines expressing it (20) | 1.82× lower at baseline in the lines without SULT1C2 | 0.029 | ⚠ within organs, on part of the lines; also absent: LINC03040, EPS8L3, TMEM139 |
| [[PRRG4]] | B | SULT1C2 activity raises PRRG4's level | lines that do not express SULT1C2 (30) vs lines expressing it (20) | 2.43× lower at baseline in the lines without SULT1C2 | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC03040, EPS8L3, TMEM139 |
| [[NUDT4]] | B | SULT1C2 activity raises NUDT4's level | lines that do not express SULT1C2 (30) vs lines expressing it (20) | 1.68× lower at baseline in the lines without SULT1C2 | 0.037 | ⚠ within organs, on part of the lines; also absent: LINC03040, EPS8L3, TMEM139 |
| [[DNAJC15]] | B | SULT1C2 activity raises DNAJC15's level | lines that do not express SULT1C2 (30) vs lines expressing it (20) | 2.60× lower at baseline in the lines without SULT1C2 | 0.042 | ⚠ within organs, on part of the lines; also absent: LINC03040, EPS8L3, TMEM139 |
| [[ELF3-AS1]] | B | SULT1C2 activity raises ELF3-AS1's level | lines that do not express SULT1C2 (30) vs lines expressing it (20) | 2.20× lower at baseline in the lines without SULT1C2 | 0.044 | ⚠ within organs, on part of the lines; also absent: LINC03040, EPS8L3, TMEM139 |
| [[ZNF503-AS1]] | B | SULT1C2 activity raises ZNF503-AS1's level | lines that do not express SULT1C2 (30) vs lines expressing it (20) | 1.92× lower at baseline in the lines without SULT1C2 | 0.077 | ⚠ within organs, on part of the lines; also absent: LINC03040, EPS8L3, TMEM139 |
| [[TNFRSF14-AS1]] | C | SULT1C2 activity raises TNFRSF14-AS1's level | lines that do not express SULT1C2 (30) vs lines expressing it (20) | 2.30× lower at baseline in the lines without SULT1C2 | 0.003 | ⚠ within organs, on part of the lines; also absent: LINC03040, EPS8L3, TMEM139; co-absent with the target |
| [[ANO9]] | C | SULT1C2 activity raises ANO9's level | lines that do not express SULT1C2 (30) vs lines expressing it (20) | 2.97× lower at baseline in the lines without SULT1C2 | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC03040, EPS8L3, TMEM139; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.7, 47.6); signed map (59.5, 12.2). **Vector** length 57.9, 16.6% of its response variance represented; |z| ≥ 3 in 524 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.5 | +15.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.3 | +9.5 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +3.3 | +10.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +6.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.8 | +9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -7.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | -1.8 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.6 | -3.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -1.5 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -1.3 | -4.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.9 | -2.3 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.9 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | sulfotransferase family 1C member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q12.3 — chr2:108,288,639-108,309,915 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ST1C1; previously SULT1C1 |
| Gene groups (HGNC) | Sulfotransferases, cytosolic |
| Reactome | 3 pathways, smallest: Cytosolic sulfonation of small molecules; Phase II - Conjugation of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [O00338](https://www.uniprot.org/uniprotkb/O00338) (Sulfotransferase 1C2):

> Sulfotransferase that utilizes 3'-phospho-5'-adenylyl sulfate (PAPS) to catalyze the sulfate conjugation of phenolic compounds. Does not transfer sulfate to steroids, dopamine, acetaminophen, or alpha-naphthol. Except in mitochondria, where it can add sulfate to cholesterol producing cholesterol sulfate, which alters mitochondrial membrane organization, and impacts protein complex mobility increasing state-III respiration, thereby modulating mitochondrial respiration (By similarity). Catalyzes …

**Summary**, from NCBI Gene [6819](https://www.ncbi.nlm.nih.gov/gene/6819):

> Sulfotransferase enzymes catalyze the sulfate conjugation of many hormones, neurotransmitters, drugs, and xenobiotic compounds. These cytosolic enzymes are different in their tissue distributions and substrate specificities. The gene structure (number and length of exons) is similar among family members. This gene encodes a protein that belongs to the SULT1 subfamily, responsible for transferring a sulfo moiety from PAPS to phenol-containing compounds. Two alternatively spliced transcript …

**Accessions** — [HGNC:11456](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11456) · Entrez [6819](https://www.ncbi.nlm.nih.gov/gene/6819) · UniProt [O00338](https://www.uniprot.org/uniprotkb/O00338) · Ensembl [ENSG00000198203](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198203)

## Data

Gene col 12552: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12552); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12552, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12552]; `tensor/DDL_lfc|DDL_z.npy` [12552]; `embed/gene_vectors.npy` [12552]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12552 or target_col == 12552). Every well: [[SULT1C2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SULT1C2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
