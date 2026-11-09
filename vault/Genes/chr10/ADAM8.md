---
symbol: "ADAM8"
type: "gene"
col: 7545
ensembl_id: "ENSG00000151651"
name: "ADAM metallopeptidase domain 8"
location: "10q26.3"
module: 34
arm: "+"
pooled_cpm: 15.81
n_lines_expressing: 22
n_dd_up: 6
n_dd_down: 26
n_dd_up_clean: 3
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 19
direction_downstream: 45
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# ADAM8

*ADAM metallopeptidase domain 8* — 10q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.34× (z +8.2, q 1e-13, up in 1 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 2.33× (z +4.5, q 0.002, up in 6 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.499× (z -6.7, q 5e-09, down in 15 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDE2A]] (+0.70, fdr 7e-06), [[RAC2]] (+0.69, fdr 7e-06), [[WNT7B]] (+0.66, fdr 1e-05); moves opposite to [[MGST1]] (-0.59, fdr 1e-05), [[ABCC4]] (-0.54, fdr 1e-05), [[PCGF5]] (-0.52, fdr 5e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[EPHB6]] → it (grade B ⚠); 45 go from it, the strongest it → [[SH3BP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7545.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +8.2 | 1e-13 | 1/10 (NCI-H1792) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.33×** | +4.5 | 0.002 | 6/17 (AsPC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.30×** | +3.6 | 0.050 | 5/13 (Panc 03.27, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.42×** | +3.5 | 0.050 | 8/19 (AsPC-1, NCI-H2347, …) | top dose only | position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.050 | 6/20 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose | position effect removed |
| [[Pimitespib (drug)]] 5 µM |  | **2.16×** | +3.3 | 0.086 | 5/14 (SNU-423, SW 900, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.37× | +3.2 | 0.12 | 5/19 (A-172, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.77× | +3.0 | 0.17 | 4/18 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7545.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.499×** | -6.7 | 5e-09 | 15/19 (SW 900, AsPC-1, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.512×** | -6.7 | 5e-09 | 14/19 (NCI-H1573, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.516×** | -6.1 | 2e-07 | 12/19 (AsPC-1, Panc 03.27, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.548×** | -6.0 | 2e-07 | 14/19 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.619×** | -4.8 | 1e-04 | 14/19 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.608×** | -4.8 | 1e-04 | 15/19 (RPMI-7951, HT-29, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.632×** | -4.6 | 3e-04 | 14/19 (HT-29, SW 900, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.633×** | -4.4 | 7e-04 | 8/19 (CHP-212, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.618×** | -4.1 | 0.002 | 11/20 (AsPC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.685×** | -3.9 | 0.006 | 10/20 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.689×** | -3.7 | 0.010 | 8/19 (HT-29, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.693×** | -3.7 | 0.010 | 10/19 (AsPC-1, SW 900, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.693×** | -3.7 | 0.010 | 13/19 (HT-29, RPMI-7951, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.677×** | -3.7 | 0.010 | 13/20 (AsPC-1, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.685×** | -3.6 | 0.010 | 8/19 (SW 900, Panc 03.27, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.715×** | -3.4 | 0.028 | 11/19 (HT-29, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7545. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 151 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -11.1) ⚠ cell-cycle shift, explains ~90% of this change |
| [[HT-29 (line)]] | alt | 28.9 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -10.7) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.130× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 226 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -11.1) ⚠ cell-cycle shift, explains ~22% of this change |
| [[NCI-H1573 (line)]] | alt | 9.85 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -9.2) |
| [[CHP-212 (line)]] | wt | 19.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0334× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 85.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -10.9) ⚠ cell-cycle shift, explains ~22% of this change |
| [[A-172 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.83 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.74 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.91 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.81 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7545), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE2A]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[RAC2]] | +0.69 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[WNT7B]] | +0.66 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[NLRP1]] | +0.64 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[GNA15]] | +0.61 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[ARAP1]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[TMCC3]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[PDGFB]] | +0.60 | +0.63 / +0.53 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[TNFRSF6B]] | +0.60 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[LINC02813]] | +0.60 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[PLCH2]] | +0.60 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[RIN1]] | +0.60 | +0.57 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGST1]] | -0.59 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[ABCC4]] | -0.54 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[PCGF5]] | -0.52 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[LARP1]] | -0.51 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[USP46]] | -0.51 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[PDS5A]] | -0.50 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[KPNA3]] | -0.50 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[USP25]] | -0.50 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[CHPT1]] | -0.50 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[BLTP3A]] | -0.49 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[AKAP7]] | -0.49 | -0.49 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 10, C 9. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHB6]] | B | EPHB6 activity raises ADAM8's level | lines that do not express EPHB6 (27) vs lines expressing it (23) | 2.14× lower at baseline in the lines without EPHB6 | 0.032 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000213981, ARHGEF38 |
| [[PTPRE]] | B | PTPRE activity raises ADAM8's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 2.41× lower at baseline in the lines without PTPRE | 0.034 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[WFDC3]] | B | WFDC3 activity raises ADAM8's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 2.19× lower at baseline in the lines without WFDC3 | 0.057 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[MAPK13]] | B | MAPK13 activity raises ADAM8's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 2.02× lower at baseline in the lines without MAPK13 | 0.060 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |
| [[TGFA]] | B | TGFA activity raises ADAM8's level | lines that do not express TGFA (17) vs lines expressing it (33) | 2.38× lower at baseline in the lines without TGFA | 0.065 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[SH3BP2]] | B | SH3BP2 activity raises ADAM8's level | lines that do not express SH3BP2 (8) vs lines expressing it (42) | 2.26× lower at baseline in the lines without SH3BP2 | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CDCP1]] | B | CDCP1 activity raises ADAM8's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 2.01× lower at baseline in the lines without CDCP1 | 0.079 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[DCLK2]] | B | DCLK2 activity lowers ADAM8's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 1.86× higher at baseline in the lines without DCLK2 | 0.082 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[MAP2K1]] | B | MAP2K1 activity raises ADAM8's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[GNA15]] | B | GNA15 activity raises ADAM8's level | lines that do not express GNA15 (25) vs lines expressing it (25) | 2.23× lower at baseline in the lines without GNA15 | 0.0998 | ⚠ within organs, on part of the lines; also absent: GDPD4, LINC02725, RDUR; maybe low, not absent |
| [[ADAM28]] | C | ADAM28 activity raises ADAM8's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 3.32× lower at baseline in the lines without ADAM28 | 0.002 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5; co-absent with the target |
| [[CARD11]] | C | CARD11 activity raises ADAM8's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.52× lower at baseline in the lines without CARD11 | 0.004 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3; co-absent with the target |

### Downstream of this gene

*45 arrows, 45 of them with an alert ⚠; grade A 0, B 33, C 12. Shown: the 12 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH3BP2]] | B | ADAM8 activity raises SH3BP2's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 2.42× lower at baseline in the lines without ADAM8 | 6e-04 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[GIPR]] | B | ADAM8 activity raises GIPR's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 2.39× lower at baseline in the lines without ADAM8 | 7e-04 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[CDCP1]] | B | ADAM8 activity raises CDCP1's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 2.45× lower at baseline in the lines without ADAM8 | 0.006 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[EHD1]] | B | ADAM8 activity raises EHD1's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 1.56× lower at baseline in the lines without ADAM8 | 0.007 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[PLAUR]] | B | ADAM8 activity raises PLAUR's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 2.51× lower at baseline in the lines without ADAM8 | 0.009 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[TUBGCP2]] | B | ADAM8 activity raises TUBGCP2's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 1.56× lower at baseline in the lines without ADAM8 | 0.009 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[KPNA3]] | B | ADAM8 activity lowers KPNA3's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 1.58× higher at baseline in the lines without ADAM8 | 0.015 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[PTPRE]] | B | ADAM8 activity raises PTPRE's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 2.58× lower at baseline in the lines without ADAM8 | 0.015 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[PTK6]] | B | ADAM8 activity raises PTK6's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 1.82× lower at baseline in the lines without ADAM8 | 0.018 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[WFDC3]] | B | ADAM8 activity raises WFDC3's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 2.39× lower at baseline in the lines without ADAM8 | 0.019 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[GNA15]] | B | ADAM8 activity raises GNA15's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 2.38× lower at baseline in the lines without ADAM8 | 0.020 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[USP46]] | B | ADAM8 activity lowers USP46's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 1.38× higher at baseline in the lines without ADAM8 | 0.022 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.3, -0.6); signed map (0.6, 47.4). **Vector** length 65.1, 20.3% of its response variance represented; |z| ≥ 3 in 557 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | +2.6 | -1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +2.0 | -2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +1.9 | -1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.8 | -2.6 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +1.4 | +2.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +3.0 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.3 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | -0.8 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.0 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -6.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -2.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.5 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -6.7 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase domain 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.3 — chr10:133,262,420-133,276,868 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD156, MS2, CD156A |
| Gene groups (HGNC) | ADAM metallopeptidase domain containing; CD molecules |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 4 pathways, smallest: Degradation of the extracellular matrix; Extracellular matrix organization; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P78325](https://www.uniprot.org/uniprotkb/P78325) (Disintegrin and metalloproteinase domain-containing protein 8):

> Possible involvement in extravasation of leukocytes.

**Summary**, from NCBI Gene [101](https://www.ncbi.nlm.nih.gov/gene/101):

> This gene encodes a member of the ADAM (a disintegrin and metalloprotease domain) family. Members of this family are membrane-anchored proteins structurally related to snake venom disintegrins, and have been implicated in a variety of biological processes involving cell-cell and cell-matrix interactions, including fertilization, muscle development, and neurogenesis. The protein encoded by this gene may be involved in cell adhesion during neurodegeneration, and it is thought to be a target for …

**Accessions** — [HGNC:215](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:215) · Entrez [101](https://www.ncbi.nlm.nih.gov/gene/101) · UniProt [P78325](https://www.uniprot.org/uniprotkb/P78325) · Ensembl [ENSG00000151651](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151651)

## Data

Gene col 7545: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7545); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7545, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7545]; `tensor/DDL_lfc|DDL_z.npy` [7545]; `embed/gene_vectors.npy` [7545]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7545 or target_col == 7545). Every well: [[ADAM8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAM8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
