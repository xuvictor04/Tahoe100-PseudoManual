---
symbol: "SULF1"
type: "gene"
col: 6037
ensembl_id: "ENSG00000137573"
name: "sulfatase 1"
location: "8q13.2-q13.3"
module: 66
arm: "+"
pooled_cpm: 37.08
n_lines_expressing: 15
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 16
direction_downstream: 9
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# SULF1

*sulfatase 1* — 8q13.2-q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.51× (z +13.8, q 2e-40, up in 7 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.51× (z +5.3, q 1e-05, up in 5 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.599× (z -4.7, q 0.002, down in 5 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH6]] (+0.66, fdr 7e-06), [[ANGPT1]] (+0.61, fdr 3e-05), [[ANXA8]] (+0.60, fdr 3e-05); moves opposite to [[SHANK2]] (-0.43, fdr 3e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 9 go from it, the strongest it → [[NCKAP5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6037.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.51×** | +13.8 | 2e-40 | 7/10 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.17×** | +10.1 | 1e-21 | 7/9 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.64×** | +8.2 | 4e-14 | 4/10 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +5.3 | 1e-05 | 5/13 (J82, SHP-77, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.62×** | +5.0 | 7e-05 | 7/13 (J82, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.69×** | +4.6 | 4e-04 | 8/12 (J82, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.004 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.010 | 6/13 (J82, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.033 | 1/13 (NCI-H460) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.038 | 1/12 (J82) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **1.98×** | +3.3 | 0.057 | 2/11 (HOP62, Hs 766T) | inconsistent across doses | noisy plate (z scaled) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.065 | 1/12 (SW 900) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.28×** | +3.2 | 0.067 | 1/13 (SHP-77) | top dose only | composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.080 | 7/13 (J82, Hs 766T, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.080 | 5/13 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6037.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.599×** | -4.7 | 0.002 | 5/12 (HS-578T, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.625×** | -4.3 | 0.005 | 9/13 (C32, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.658×** | -3.8 | 0.025 | 11/13 (Hs 766T, HS-578T, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.662×** | -3.8 | 0.025 | 6/13 (J82, NCI-H460, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.656×** | -3.5 | 0.044 | 1/13 (SW 900) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.672×** | -3.5 | 0.047 | 3/13 (Hs 766T, SW 900, …) | top dose only |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.677×** | -3.3 | 0.084 | 0/13 | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.716× | -3.0 | 0.17 | 2/13 (Hs 766T, NCI-H460) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.792× | -3.0 | 0.17 | 9/13 (NCI-H460, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6037. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 990 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -17.5) |
| [[A-172 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 9.87 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.88 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.59 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.81 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.79 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.51 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 97.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.30 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 324 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.86 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.60 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.66 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.03 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.14 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6037), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH6]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[ANGPT1]] | +0.61 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[ANXA8]] | +0.60 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[C5orf46]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[COL1A1]] | +0.58 | +0.45 / +0.57 | both halves | 3e-05 | STRING 621 |
| [[PALLD]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[FBN1]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 | STRING 408 |
| [[TEX41]] | +0.57 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[COL5A2]] | +0.57 | +0.45 / +0.66 | both halves | 3e-05 | STRING 630 |
| [[PCDH18]] | +0.57 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[MXRA5]] | +0.56 | +0.49 / +0.60 | both halves | 1e-05 | STRING 496 |
| [[LUM]] | +0.56 | +0.41 / +0.56 | both halves | 4e-05 | STRING 529 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHANK2]] | -0.43 | -0.50 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 2, C 14. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers SULF1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[HDAC6]] | B | HDAC6 activity raises SULF1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TEK]] | C | TEK activity raises SULF1's level | lines that do not express TEK (27) vs lines expressing it (23) | 2.75× lower at baseline in the lines without TEK | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: THY1, LINC01036, FCRLA; maybe low, not absent; co-absent with the target |
| [[KRT14]] | C | KRT14 activity raises SULF1's level | lines that do not express KRT14 (43) vs lines expressing it (7) | 4.71× lower at baseline in the lines without KRT14 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13; co-absent with the target |
| [[SIM1]] | C | SIM1 activity raises SULF1's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 5.03× lower at baseline in the lines without SIM1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; co-absent with the target |
| [[CHRDL1]] | C | CHRDL1 activity raises SULF1's level | lines that do not express CHRDL1 (37) vs lines expressing it (13) | 3.26× lower at baseline in the lines without CHRDL1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01592, PAX3, LINC01035; co-absent with the target |
| [[LINC01592]] | C | LINC01592 activity raises SULF1's level | lines that do not express LINC01592 (35) vs lines expressing it (15) | 3.93× lower at baseline in the lines without LINC01592 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHRDL1, ESM1, CCL3; maybe low, not absent; co-absent with the target |
| [[DOK5]] | C | DOK5 activity raises SULF1's level | lines that do not express DOK5 (40) vs lines expressing it (10) | 3.49× lower at baseline in the lines without DOK5 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230258, IGFBP5; co-absent with the target |
| [[IGFBP5]] | C | IGFBP5 activity raises SULF1's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 3.21× lower at baseline in the lines without IGFBP5 | 0.041 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2; co-absent with the target |
| [[MGP]] | C | MGP activity raises SULF1's level | lines that do not express MGP (35) vs lines expressing it (15) | 3.12× lower at baseline in the lines without MGP | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TIMP3, HTR1F, AEBP1; co-absent with the target |
| [[CCDC190]] | C | CCDC190 activity raises SULF1's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 3.73× lower at baseline in the lines without CCDC190 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337; co-absent with the target |
| [[CDH6]] | C | CDH6 activity raises SULF1's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 3.19× lower at baseline in the lines without CDH6 | 0.048 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCKAP5]] | B | SULF1 activity raises NCKAP5's level | lines that do not express SULF1 (35) vs lines expressing it (15) | 2.74× lower at baseline in the lines without SULF1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00958, LINC01592, TBXT |
| [[CCDC144A]] | B | SULF1 activity raises CCDC144A's level | lines that do not express SULF1 (35) vs lines expressing it (15) | 1.89× lower at baseline in the lines without SULF1 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00958, LINC01592, TBXT |
| [[PPP2R2B]] | C | SULF1 activity raises PPP2R2B's level | lines that do not express SULF1 (35) vs lines expressing it (15) | 3.05× lower at baseline in the lines without SULF1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00958, LINC01592, TBXT; co-absent with the target |
| [[ANXA8]] | C | SULF1 activity raises ANXA8's level | lines that do not express SULF1 (35) vs lines expressing it (15) | 2.01× lower at baseline in the lines without SULF1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00958, LINC01592, TBXT; co-absent with the target |
| [[KRT14]] | C | SULF1 activity raises KRT14's level | lines that do not express SULF1 (35) vs lines expressing it (15) | 2.01× lower at baseline in the lines without SULF1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00958, LINC01592, TBXT; co-absent with the target |
| [[TEK]] | C | SULF1 activity raises TEK's level | lines that do not express SULF1 (35) vs lines expressing it (15) | 1.82× lower at baseline in the lines without SULF1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00958, LINC01592, TBXT; co-absent with the target |
| [[DOK5]] | C | SULF1 activity raises DOK5's level | lines that do not express SULF1 (35) vs lines expressing it (15) | 1.98× lower at baseline in the lines without SULF1 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00958, LINC01592, TBXT; co-absent with the target |
| [[SPOCK3]] | C | SULF1 activity raises SPOCK3's level | lines that do not express SULF1 (35) vs lines expressing it (15) | 1.95× lower at baseline in the lines without SULF1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00958, LINC01592, TBXT; co-absent with the target |
| [[CDH11]] | C | SULF1 activity raises CDH11's level | lines that do not express SULF1 (35) vs lines expressing it (15) | 2.99× lower at baseline in the lines without SULF1 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00958, LINC01592, TBXT; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.697). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.7, 21.1); signed map (36.0, 31.1). **Vector** length 39.5, 12.3% of its response variance represented; |z| ≥ 3 in 279 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Syndecan interactions* (reactome, mean cos +0.51 to 5); *Developmental Lineage of Pancreatic Ductal Cells* (reactome, mean cos +0.54 to 4); *Developmental Lineage of Pancreatic Endocrine Mid Progenitor Cells* (reactome, mean cos +0.54 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +13.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.9 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +4.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +3.8 |
| fall | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.0 | -3.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -3.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -3.5 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -1.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | sulfatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.2-q13.3 — chr8:69,466,624-69,660,915 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1077, SULF-1, hSulf-1 |
| Gene groups (HGNC) | Sulfatases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWU6](https://www.uniprot.org/uniprotkb/Q8IWU6) (Extracellular sulfatase Sulf-1):

> Exhibits arylsulfatase activity and highly specific endoglucosamine-6-sulfatase activity. It can remove sulfate from the C-6 position of glucosamine within specific subregions of intact heparin. Diminishes HSPG (heparan sulfate proteoglycans) sulfation, inhibits signaling by heparin-dependent growth factors, diminishes proliferation, and facilitates apoptosis in response to exogenous stimulation.

**Summary**, from NCBI Gene [23213](https://www.ncbi.nlm.nih.gov/gene/23213):

> This gene encodes an extracellular heparan sulfate endosulfatase. The encoded enzyme selectively removes 6-O-sulfate groups from heparan sulfate chains of heparan sulfate proteoglycans (HSPGs). The enzyme is secreted through the Golgi and is subsequently localized to the cell surface. The expression of this gene may be down-regulated in several types of cancer, including hepatocellular (HCC), ovarian and breast cancers. Alternative splicing results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:20391](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20391) · Entrez [23213](https://www.ncbi.nlm.nih.gov/gene/23213) · UniProt [Q8IWU6](https://www.uniprot.org/uniprotkb/Q8IWU6) · Ensembl [ENSG00000137573](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137573)

## Data

Gene col 6037: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6037); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6037, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6037]; `tensor/DDL_lfc|DDL_z.npy` [6037]; `embed/gene_vectors.npy` [6037]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6037 or target_col == 6037). Every well: [[SULF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SULF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
