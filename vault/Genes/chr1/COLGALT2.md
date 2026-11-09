---
symbol: "COLGALT2"
type: "gene"
col: 12669
ensembl_id: "ENSG00000198756"
name: "collagen beta(1-O)galactosyltransferase 2"
location: "1q25.3"
module: 27
arm: "+"
pooled_cpm: 10.06
n_lines_expressing: 27
n_dd_up: 10
n_dd_down: 26
n_dd_up_clean: 6
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 12
direction_downstream: 10
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# COLGALT2

*collagen beta(1-O)galactosyltransferase 2* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.05× (z +11.2, q 2e-26, up in 10 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.480× (z -8.1, q 3e-13, down in 15 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APCDD1]] (+0.68, fdr 7e-06), [[SLC30A10]] (+0.66, fdr 8e-06), [[FGF19]] (+0.63, fdr 1e-05); moves opposite to [[SCG3]] (-0.43, fdr 2e-04), [[MYH14]] (-0.43, fdr 1e-04), [[TAOK3]] (-0.41, fdr 2e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[OPRD1]] → it (grade B ⚠); 10 go from it, the strongest it → [[ZNRF3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12669.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +11.2 | 2e-26 | 10/21 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.85×** | +11.1 | 5e-26 | 2/7 (NCI-H1792, HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.43×** | +9.8 | 3e-20 | 1/15 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +8.3 | 1e-14 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.63×** | +3.8 | 0.015 | 0/21 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.017 | 1/19 (hTERT-HPNE) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.021 | 1/24 (MIA PaCa-2) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.025 | 5/23 (C32, PANC-1, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.54×** | +3.4 | 0.040 | 1/16 (LOX-IMVI) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.24×** | +3.3 | 0.048 | 5/24 (C32, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.34× | +3.1 | 0.11 | 2/16 (SW 900, SW1417) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12669.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.480×** | -8.1 | 3e-13 | 15/23 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.548×** | -6.6 | 9e-09 | 17/24 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.561×** | -6.4 | 4e-08 | 15/23 (HepG2/C3A, SW480, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.591×** | -5.8 | 9e-07 | 14/21 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.595×** | -5.7 | 1e-06 | 13/23 (SW480, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.608×** | -5.5 | 4e-06 | 14/23 (C32, SW480, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.616×** | -5.3 | 8e-06 | 11/23 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.631×** | -5.1 | 3e-05 | 12/23 (SW480, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.625×** | -5.0 | 4e-05 | 13/23 (J82, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.626×** | -5.0 | 4e-05 | 14/23 (HepG2/C3A, NCI-H1792, …) | two highest doses | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.639×** | -4.9 | 4e-05 | 13/23 (SW480, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.747×** | -4.5 | 3e-04 | 16/21 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.684×** | -4.2 | 0.001 | 14/23 (SK-MEL-2, SW48, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.685×** | -4.2 | 0.001 | 5/23 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.688×** | -4.0 | 0.003 | 5/23 (COLO 205, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.700×** | -3.9 | 0.003 | 9/24 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.717×** | -3.7 | 0.008 | 8/23 (J82, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.730×** | -3.5 | 0.015 | 6/23 (C32, LOX-IMVI, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12669. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 113 | 0 | 15 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0254× (z -23.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0361× (z -21.7) |
| [[PANC-1 (line)]] | alt | 6.68 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.125× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 24.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -11.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0642× (z -11.3) |
| [[C32 (line)]] | wt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0641× (z -11.8) |
| [[J82 (line)]] | alt | 4.01 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0806× (z -9.0) |
| [[SW1417 (line)]] | alt | 6.07 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -8.5) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12669), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APCDD1]] | +0.68 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[SLC30A10]] | +0.66 | +0.66 / +0.58 | both halves | 8e-06 | **novel candidate** |
| [[FGF19]] | +0.63 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[IGFL4]] | +0.63 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[JAKMIP2-AS1]] | +0.60 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[NKD1]] | +0.59 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[ST18]] | +0.58 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[PSG1]] | +0.58 | +0.50 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[NMNAT3]] | +0.57 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[VWA2]] | +0.57 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[PTPRZ1]] | +0.56 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[GJB1]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCG3]] | -0.43 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[MYH14]] | -0.43 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[TAOK3]] | -0.41 | -0.29 / -0.45 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 6, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OPRD1]] | B | OPRD1 activity strengthens COLGALT2's drug response | lines that do not express OPRD1 (12) vs lines expressing it (12) | the lines without OPRD1 respond 0.86× as strongly (z diff +0.83); strongest at Homoharringtonine 0.5 µM: 0.49x vs 0.29x (z diff +3.5) | 0.033 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[OPRD1]] | B | OPRD1 activity raises COLGALT2's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 2.35× lower at baseline in the lines without OPRD1 | 0.055 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent |
| [[LINC01169]] | B | LINC01169 activity raises COLGALT2's level | lines that do not express LINC01169 (36) vs lines expressing it (14) | 2.40× lower at baseline in the lines without LINC01169 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, AFP, AK4P3 |
| [[LAMC3]] | B | LAMC3 activity raises COLGALT2's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.78× lower at baseline in the lines without LAMC3 | 0.083 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[PEG3]] | B | PEG3 activity raises COLGALT2's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 1.91× lower at baseline in the lines without PEG3 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1 |
| [[CDK15]] | B | CDK15 activity raises COLGALT2's level | lines that do not express CDK15 (28) vs lines expressing it (22) | 1.65× lower at baseline in the lines without CDK15 | 0.098 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent |
| [[JAKMIP2-AS1]] | C | JAKMIP2-AS1 activity raises COLGALT2's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 2.79× lower at baseline in the lines without JAKMIP2-AS1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[LGR5]] | C | LGR5 activity raises COLGALT2's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 3.93× lower at baseline in the lines without LGR5 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573; co-absent with the target |
| [[ROBO2]] | C | ROBO2 activity raises COLGALT2's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 2.94× lower at baseline in the lines without ROBO2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205; co-absent with the target |
| [[SLC25A24P1]] | C | SLC25A24P1 activity raises COLGALT2's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 3.04× lower at baseline in the lines without SLC25A24P1 | 0.037 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2; co-absent with the target |
| [[SCG3]] | C | SCG3 activity raises COLGALT2's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 2.76× lower at baseline in the lines without SCG3 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA; co-absent with the target |
| [[NOTUM]] | C | NOTUM activity raises COLGALT2's level | lines that do not express NOTUM (31) vs lines expressing it (19) | 2.36× lower at baseline in the lines without NOTUM | 0.078 | ⚠ within organs, on part of the lines; also absent: FGF20, AXIN2, XKR7; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNRF3]] | B | COLGALT2 activity raises ZNRF3's level | lines that do not express COLGALT2 (23) vs lines expressing it (27) | 1.57× lower at baseline in the lines without COLGALT2 | 0.017 | ⚠ within organs, on part of the lines; also absent: PRRX1, SYT11, GNAT3 |
| [[PSD2]] | B | COLGALT2 activity raises PSD2's level | lines that do not express COLGALT2 (23) vs lines expressing it (27) | 1.53× lower at baseline in the lines without COLGALT2 | 0.029 | ⚠ within organs, on part of the lines; also absent: PRRX1, SYT11, GNAT3 |
| [[TRAF5]] | B | COLGALT2 activity raises TRAF5's level | lines that do not express COLGALT2 (23) vs lines expressing it (27) | 1.62× lower at baseline in the lines without COLGALT2 | 0.054 | ⚠ within organs, on part of the lines; also absent: PRRX1, SYT11, GNAT3 |
| [[AXIN2]] | B | COLGALT2 activity raises AXIN2's level | lines that do not express COLGALT2 (23) vs lines expressing it (27) | 1.98× lower at baseline in the lines without COLGALT2 | 0.065 | ⚠ within organs, on part of the lines; also absent: PRRX1, SYT11, GNAT3 |
| [[PALD1]] | B | COLGALT2 activity raises PALD1's level | lines that do not express COLGALT2 (23) vs lines expressing it (27) | 1.90× lower at baseline in the lines without COLGALT2 | 0.092 | ⚠ within organs, on part of the lines; also absent: PRRX1, SYT11, GNAT3 |
| [[ASB4]] | B | COLGALT2 activity raises ASB4's level | lines that do not express COLGALT2 (23) vs lines expressing it (27) | 1.72× lower at baseline in the lines without COLGALT2 | 0.097 | ⚠ within organs, on part of the lines; also absent: PRRX1, SYT11, GNAT3 |
| [[NKD1]] | C | COLGALT2 activity raises NKD1's level | lines that do not express COLGALT2 (23) vs lines expressing it (27) | 2.53× lower at baseline in the lines without COLGALT2 | 0.021 | ⚠ within organs, on part of the lines; also absent: PRRX1, SYT11, GNAT3; co-absent with the target |
| [[NOTUM]] | C | COLGALT2 activity raises NOTUM's level | lines that do not express COLGALT2 (23) vs lines expressing it (27) | 2.36× lower at baseline in the lines without COLGALT2 | 0.022 | ⚠ within organs, on part of the lines; also absent: PRRX1, SYT11, GNAT3; co-absent with the target |
| [[CSMD3]] | C | COLGALT2 activity raises CSMD3's level | lines that do not express COLGALT2 (23) vs lines expressing it (27) | 2.99× lower at baseline in the lines without COLGALT2 | 0.025 | ⚠ within organs, on part of the lines; also absent: PRRX1, SYT11, GNAT3; co-absent with the target |
| [[ROBO2]] | C | COLGALT2 activity raises ROBO2's level | lines that do not express COLGALT2 (23) vs lines expressing it (27) | 2.45× lower at baseline in the lines without COLGALT2 | 0.095 | ⚠ within organs, on part of the lines; also absent: PRRX1, SYT11, GNAT3; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.6, 43.4); signed map (63.5, 16.1). **Vector** length 56.1, 12.9% of its response variance represented; |z| ≥ 3 in 548 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +9.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +2.0 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +8.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +3.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.1 | +3.6 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -6.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -1.5 | -5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.4 | -5.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | collagen beta(1-O)galactosyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:183,929,854-184,037,729 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0584; previously C1orf17, GLT25D2 |
| Gene groups (HGNC) | Collagen beta(1-O)galactosyltransferases |
| Reactome | 3 pathways, smallest: Collagen biosynthesis and modifying enzymes; Collagen formation; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYK4](https://www.uniprot.org/uniprotkb/Q8IYK4) (Procollagen galactosyltransferase 2):

> Beta-galactosyltransferase that transfers beta-galactose to hydroxylysine residues of collagen.

**Summary**, from NCBI Gene [23127](https://www.ncbi.nlm.nih.gov/gene/23127):

> Predicted to enable procollagen galactosyltransferase activity. Predicted to be involved in collagen fibril organization. Predicted to act upstream of or within T cell apoptotic process. Predicted to be located in endoplasmic reticulum lumen. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16790](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16790) · Entrez [23127](https://www.ncbi.nlm.nih.gov/gene/23127) · UniProt [Q8IYK4](https://www.uniprot.org/uniprotkb/Q8IYK4) · Ensembl [ENSG00000198756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198756)

## Data

Gene col 12669: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12669); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12669, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12669]; `tensor/DDL_lfc|DDL_z.npy` [12669]; `embed/gene_vectors.npy` [12669]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12669 or target_col == 12669). Every well: [[COLGALT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COLGALT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
