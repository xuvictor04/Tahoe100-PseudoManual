---
symbol: "SLC14A1"
type: "gene"
col: 6527
ensembl_id: "ENSG00000141469"
name: "solute carrier family 14 member 1 (Kidd blood group)"
location: "18q12.3"
module: 34
arm: "+"
pooled_cpm: 4.83
n_lines_expressing: 13
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 16
direction_downstream: 16
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# SLC14A1

*solute carrier family 14 member 1 (Kidd blood group)* — 18q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.09× (z +11.1, q 4e-26, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.87× (z +6.3, q 5e-08, up in 0 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.516× (z -4.6, q 0.002, down in 7 of 11 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (Hs 766T 0.0197×, CFPAC-1 0.0865×; ⚠ cell-cycle shift, explains ~51% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (Hs 766T 0.0327×, LoVo 0.0368×; ⚠ cell-cycle shift, explains ~25% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (Hs 766T 0.133×, H4 0.157×); [[Dexamethasone (drug)]] 5 µM in 2 lines (H4 0.0916×, Hs 766T 0.133×); [[Budesonide (drug)]] 0.05 µM in 2 lines (H4 0.115×, Hs 766T 0.143×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYTL5]] (+0.66, fdr 7e-06), [[DOK5]] (+0.64, fdr 7e-06), [[PTHLH]] (+0.62, fdr 1e-05); moves opposite to [[BATF]] (-0.51, fdr 3e-05), [[KRT5]] (-0.46, fdr 1e-04), [[MT1M]] (-0.46, fdr 1e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[PKIA]] → it (grade B ⚠); 16 go from it, the strongest it → [[PLEKHM1P1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6527.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.09×** | +11.1 | 4e-26 | 1/4 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.28×** | +8.4 | 9e-15 | 3/7 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.41×** | +8.1 | 1e-13 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +6.3 | 5e-08 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.93×** | +4.6 | 4e-04 | 0/9 | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.16×** | +4.3 | 0.002 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.51×** | +4.2 | 0.003 | 2/10 (H4, SW 1088) | top dose only | composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.01×** | +3.5 | 0.028 | 1/8 (AsPC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Silodosin (drug)]] 5 µM |  | 1.57× | +3.1 | 0.13 | 0/7 | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | 1.54× | +3.1 | 0.13 | 0/8 | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6527.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (Hs 766T 0.0197×, CFPAC-1 0.0865×; ⚠ cell-cycle shift, explains ~51% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (Hs 766T 0.0327×, LoVo 0.0368×; ⚠ cell-cycle shift, explains ~25% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (Hs 766T 0.133×, H4 0.157×); [[Dexamethasone (drug)]] 5 µM in 2 lines (H4 0.0916×, Hs 766T 0.133×); [[Budesonide (drug)]] 0.05 µM in 2 lines (H4 0.115×, Hs 766T 0.143×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.516×** | -4.6 | 0.002 | 7/11 (LoVo, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.569×** | -3.7 | 0.050 | 2/11 (CFPAC-1, LoVo) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.734× | -3.2 | 0.18 | 7/11 (Hs 766T, CFPAC-1, …) | top dose only |  |
| [[Quinestrol (drug)]] 5 µM |  | 0.734× | -3.2 | 0.18 | 2/11 (SK-MEL-2, AsPC-1) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.647× | -3.1 | 0.18 | 6/10 (CFPAC-1, AsPC-1, …) | all doses, flat | position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | 0.650× | -3.1 | 0.18 | 7/11 (H4, Hs 766T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.659× | -3.0 | 0.22 | 5/11 (Hs 766T, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6527. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 83.0 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0197× (z -28.7) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -14.7) |
| [[H4 (line)]] | wt | 161 | 0 | 15 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0434× (z -15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -13.7) |
| [[LoVo (line)]] | wt | 6.06 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0368× (z -12.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.0885× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 6.21 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -8.9) ⚠ cell-cycle shift, explains ~51% of this change |
| [[CFPAC-1 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0865× (z -12.5) ⚠ cell-cycle shift, explains ~51% of this change |
| [[A-172 (line)]] | wt | 0.882 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.501 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.675 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.714 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.975 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.716 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.782 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.768 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.852 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.800 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.704 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.747 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.732 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.922 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.613 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.811 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.868 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.887 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.732 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.666 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.742 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.872 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.610 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.713 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 93.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.750 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.688 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6527), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYTL5]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[DOK5]] | +0.64 | +0.60 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[PTHLH]] | +0.62 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[WNT7B]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[KISS1]] | +0.60 | +0.63 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[LAMA4]] | +0.59 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[IL33]] | +0.59 | +0.62 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[ADAM19]] | +0.58 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[IL1RAPL1]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[CDH6]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[SIGLEC15]] | +0.56 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ECSCR]] | +0.55 | +0.59 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BATF]] | -0.51 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[KRT5]] | -0.46 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[MT1M]] | -0.46 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[SAA1]] | -0.46 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[PID1]] | -0.43 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[STXBP5]] | -0.42 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[NNMT]] | -0.42 | -0.32 / -0.50 | both halves | 1e-04 |  |
| [[ADGRG2]] | -0.42 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[CHPT1]] | -0.42 | -0.34 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 1, C 15. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKIA]] | B | PKIA activity raises SLC14A1's level | lines that do not express PKIA (22) vs lines expressing it (28) | 1.42× lower at baseline in the lines without PKIA | 0.098 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4 |
| [[PAK3]] | C | PAK3 activity raises SLC14A1's level | lines that do not express PAK3 (32) vs lines expressing it (18) | 2.70× lower at baseline in the lines without PAK3 | 0.005 | ⚠ within organs, on part of the lines; also absent: CRLF2, SLC14A1, ENTHD1; co-absent with the target |
| [[SIM1]] | C | SIM1 activity raises SLC14A1's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 1.86× lower at baseline in the lines without SIM1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; co-absent with the target |
| [[KRT5]] | C | KRT5 activity raises SLC14A1's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 3.09× lower at baseline in the lines without KRT5 | 0.027 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[B3GALT5]] | C | B3GALT5 activity raises SLC14A1's level | lines that do not express B3GALT5 (26) vs lines expressing it (24) | 2.40× lower at baseline in the lines without B3GALT5 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000225330, IGFL2-AS1, PADI1; co-absent with the target |
| [[CDH6]] | C | CDH6 activity raises SLC14A1's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 2.52× lower at baseline in the lines without CDH6 | 0.048 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC; co-absent with the target |
| [[HTR1F]] | C | HTR1F activity raises SLC14A1's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 2.49× lower at baseline in the lines without HTR1F | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent; co-absent with the target |
| [[COL22A1]] | C | COL22A1 activity raises SLC14A1's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 2.35× lower at baseline in the lines without COL22A1 | 0.070 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2; co-absent with the target |
| [[ERG]] | C | ERG activity raises SLC14A1's level | lines that do not express ERG (30) vs lines expressing it (20) | 2.11× lower at baseline in the lines without ERG | 0.074 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent; co-absent with the target |
| [[NLRP1]] | C | NLRP1 activity raises SLC14A1's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 2.23× lower at baseline in the lines without NLRP1 | 0.075 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12; co-absent with the target |
| [[CSMD2]] | C | CSMD2 activity raises SLC14A1's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 2.17× lower at baseline in the lines without CSMD2 | 0.077 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent; co-absent with the target |
| [[GALNT5]] | C | GALNT5 activity raises SLC14A1's level | lines that do not express GALNT5 (27) vs lines expressing it (23) | 1.30× lower at baseline in the lines without GALNT5 | 0.080 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 4, C 12. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHM1P1]] | B | SLC14A1 activity raises PLEKHM1P1's level | lines that do not express SLC14A1 (37) vs lines expressing it (13) | 1.39× lower at baseline in the lines without SLC14A1 | 0.026 | ⚠ within organs, on part of the lines; also absent: APOD, ZNF208, GRIN2A; maybe low, not absent |
| [[TGFA]] | B | SLC14A1 activity raises TGFA's level | lines that do not express SLC14A1 (37) vs lines expressing it (13) | 2.56× lower at baseline in the lines without SLC14A1 | 0.043 | ⚠ within organs, on part of the lines; also absent: APOD, ZNF208, GRIN2A; maybe low, not absent |
| [[YOD1]] | B | SLC14A1 activity raises YOD1's level | lines that do not express SLC14A1 (37) vs lines expressing it (13) | 1.49× lower at baseline in the lines without SLC14A1 | 0.072 | ⚠ within organs, on part of the lines; also absent: APOD, ZNF208, GRIN2A; maybe low, not absent |
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | B | SLC14A1 activity strengthens ARHGAP27P1-BPTFP1-KPNA2P3's drug response | lines that do not express SLC14A1 (37) vs lines expressing it (11) | the lines without SLC14A1 respond 0.61× as strongly (z diff +1.68); strongest at Ouabain (Octahydrate) 5 µM: 0.55x vs 0.26x (z diff +3.0) | 0.096 | ⚠ within organs, on part of the lines; also absent: APOD, ZNF208, GRIN2A; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SYTL5]] | C | SLC14A1 activity raises SYTL5's level | lines that do not express SLC14A1 (37) vs lines expressing it (13) | 2.89× lower at baseline in the lines without SLC14A1 | 0.006 | ⚠ within organs, on part of the lines; also absent: APOD, ZNF208, GRIN2A; maybe low, not absent; co-absent with the target |
| [[B3GALT5]] | C | SLC14A1 activity raises B3GALT5's level | lines that do not express SLC14A1 (37) vs lines expressing it (13) | 3.20× lower at baseline in the lines without SLC14A1 | 0.013 | ⚠ within organs, on part of the lines; also absent: APOD, ZNF208, GRIN2A; maybe low, not absent; co-absent with the target |
| [[COL22A1]] | C | SLC14A1 activity raises COL22A1's level | lines that do not express SLC14A1 (37) vs lines expressing it (13) | 3.44× lower at baseline in the lines without SLC14A1 | 0.013 | ⚠ within organs, on part of the lines; also absent: APOD, ZNF208, GRIN2A; maybe low, not absent; co-absent with the target |
| [[PAK3]] | C | SLC14A1 activity raises PAK3's level | lines that do not express SLC14A1 (37) vs lines expressing it (13) | 3.92× lower at baseline in the lines without SLC14A1 | 0.019 | ⚠ within organs, on part of the lines; also absent: APOD, ZNF208, GRIN2A; maybe low, not absent; co-absent with the target |
| [[TFF2]] | C | SLC14A1 activity raises TFF2's level | lines that do not express SLC14A1 (37) vs lines expressing it (13) | 2.12× lower at baseline in the lines without SLC14A1 | 0.024 | ⚠ within organs, on part of the lines; also absent: APOD, ZNF208, GRIN2A; maybe low, not absent; co-absent with the target |
| [[GALNT5]] | C | SLC14A1 activity raises GALNT5's level | lines that do not express SLC14A1 (37) vs lines expressing it (13) | 2.39× lower at baseline in the lines without SLC14A1 | 0.029 | ⚠ within organs, on part of the lines; also absent: APOD, ZNF208, GRIN2A; maybe low, not absent; co-absent with the target |
| [[DHRS9]] | C | SLC14A1 activity raises DHRS9's level | lines that do not express SLC14A1 (37) vs lines expressing it (13) | 3.17× lower at baseline in the lines without SLC14A1 | 0.035 | ⚠ within organs, on part of the lines; also absent: APOD, ZNF208, GRIN2A; maybe low, not absent; co-absent with the target |
| [[NLRP1]] | C | SLC14A1 activity raises NLRP1's level | lines that do not express SLC14A1 (37) vs lines expressing it (13) | 3.72× lower at baseline in the lines without SLC14A1 | 0.052 | ⚠ within organs, on part of the lines; also absent: APOD, ZNF208, GRIN2A; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.540). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.9, 19.1); signed map (16.9, 50.9). **Vector** length 49.5, 16.1% of its response variance represented; |z| ≥ 3 in 436 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +8.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.1 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.8 | +1.1 |
|  | [[Vilanterol (drug)]] 5 µM |  | +0.7 | +0.9 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -2.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.9 | -0.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.8 | -3.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 14 member 1 (Kidd blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.3 — chr18:45,687,025-45,752,520 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HsT1341, RACH1, RACH2; previously JK |
| Gene groups (HGNC) | Blood group antigens; Solute carrier family 14 |
| Reactome | 3 pathways, smallest: SLC-mediated transport of organic cations; SLC-mediated transmembrane transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13336](https://www.uniprot.org/uniprotkb/Q13336) (Urea transporter 1):

> Mediates the transport of urea driven by a concentration gradient across the cell membrane of erythrocytes. Also mediates the transport of urea across the cell membrane of the renal inner medullary collecting duct which is critical to the urinary concentrating mechanism (By similarity). Facilitates water transport in erythrocytes (By similarity).

**Summary**, from NCBI Gene [6563](https://www.ncbi.nlm.nih.gov/gene/6563):

> The protein encoded by this gene is a membrane transporter that mediates urea transport in erythrocytes. This gene forms the basis for the Kidd blood group system. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:10918](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10918) · Entrez [6563](https://www.ncbi.nlm.nih.gov/gene/6563) · UniProt [Q13336](https://www.uniprot.org/uniprotkb/Q13336) · Ensembl [ENSG00000141469](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141469)

## Data

Gene col 6527: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6527); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6527, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6527]; `tensor/DDL_lfc|DDL_z.npy` [6527]; `embed/gene_vectors.npy` [6527]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6527 or target_col == 6527). Every well: [[SLC14A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC14A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
