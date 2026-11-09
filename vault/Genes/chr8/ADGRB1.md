---
symbol: "ADGRB1"
type: "gene"
col: 11213
ensembl_id: "ENSG00000181790"
name: "adhesion G protein-coupled receptor B1"
location: "8q24.3"
module: 128
arm: "+"
pooled_cpm: 5.6
n_lines_expressing: 32
n_dd_up: 7
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 8
direction_downstream: 13
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# ADGRB1

*adhesion G protein-coupled receptor B1* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.68× (z +6.9, q 3e-09, up in 10 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.446× (z -7.6, q 2e-11, down in 14 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JPH3]] (+0.63, fdr 1e-05), [[LRRC36]] (+0.61, fdr 1e-05), [[ELFN1]] (+0.61, fdr 1e-05); moves opposite to [[KIAA0319L]] (-0.43, fdr 5e-05), [[MORN2]] (-0.42, fdr 9e-05), [[ACOT8]] (-0.42, fdr 7e-05).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CHD5]] → it (grade B ⚠); 13 go from it, the strongest it → [[SYT9-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11213.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +6.9 | 3e-09 | 10/26 (NCI-H1573, BT-474, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +5.8 | 2e-06 | 2/11 (LS 180, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +5.3 | 2e-05 | 1/9 (HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +4.2 | 0.004 | 8/24 (HOP62, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +3.8 | 0.016 | 2/15 (MIA PaCa-2, A-427) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.53×** | +3.7 | 0.020 | 3/20 (NCI-H23, LoVo, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.70×** | +3.6 | 0.028 | 1/14 (LS 180) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Canagliflozin (drug)]] 5 µM |  | 1.40× | +3.0 | 0.16 | 0/21 | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 1.41× | +3.0 | 0.16 | 2/18 (CFPAC-1, NCI-H23) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11213.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.446×** | -7.6 | 2e-11 | 14/28 (AN3 CA, A549, …) | two highest doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.472×** | -7.1 | 4e-10 | 17/29 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.476×** | -7.0 | 5e-10 | 16/19 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.485×** | -6.8 | 1e-09 | 15/21 (NCI-H23, A549, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.486×** | -6.5 | 7e-09 | 17/26 (A549, NCI-H2030, …) | two highest doses | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.541×** | -5.8 | 7e-07 | 16/26 (SW480, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.561×** | -5.4 | 4e-06 | 14/26 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.641×** | -4.2 | 0.002 | 14/28 (AN3 CA, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.674×** | -3.7 | 0.013 | 10/29 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Hesperidin (drug)]] 0.5 µM |  | **0.682×** | -3.6 | 0.018 | 9/26 (LoVo, SW 900, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.685×** | -3.6 | 0.019 | 6/25 (HOP62, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.700×** | -3.4 | 0.038 | 5/27 (RKO, SW 900, …) | inconsistent across doses | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.719×** | -3.1 | 0.084 | 5/26 (A549, NCI-H23, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.712×** | -3.1 | 0.085 | 11/22 (SW480, A-427, …) | top dose only |  |
| [[Malotilate (drug)]] 0.5 µM |  | **0.726×** | -3.0 | 0.098 | 5/25 (CFPAC-1, SHP-77, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11213. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 17.0 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0963× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 40.3 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -15.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -10.0) |
| [[A549 (line)]] | wt | 6.08 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0565× (z -10.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Entecavir (monohydrate) (drug)]] 0.05 µM 0.0730× (z -8.8) |
| [[AN3 CA (line)]] | alt | 34.8 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0749× (z -9.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0891× (z -8.9) |
| [[A-427 (line)]] | wt | 18.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0931× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 41.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -10.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 6.71 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.151× (z -8.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.884 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.869 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.580 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.867 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.597 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11213), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JPH3]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[LRRC36]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[ELFN1]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[MYT1]] | +0.59 | +0.49 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[SCN8A]] | +0.59 | +0.62 / +0.47 | both halves | 2e-05 | **novel candidate** |
| [[LAMC3]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[RASGEF1A]] | +0.57 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[SLC6A11]] | +0.57 | +0.50 / +0.39 | both halves | 6e-05 |  |
| [[ARHGEF25]] | +0.56 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[RFPL1S]] | +0.56 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[SLC4A3]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[DANT1]] | +0.56 | +0.45 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA0319L]] | -0.43 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[MORN2]] | -0.42 | -0.38 / -0.37 | both halves | 9e-05 |  |
| [[ACOT8]] | -0.42 | -0.43 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHD5]] | B | CHD5 activity raises ADGRB1's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.94× lower at baseline in the lines without CHD5 | 0.008 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[IQGAP2]] | B | IQGAP2 activity raises ADGRB1's level | lines that do not express IQGAP2 (25) vs lines expressing it (25) | 1.73× lower at baseline in the lines without IQGAP2 | 0.018 | ⚠ within organs, on part of the lines; also absent: KLHL13, KCNQ2, CHD5; maybe low, not absent |
| [[KIF1A]] | B | KIF1A activity raises ADGRB1's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 2.29× lower at baseline in the lines without KIF1A | 0.053 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[KCNQ2]] | B | KCNQ2 activity raises ADGRB1's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 2.05× lower at baseline in the lines without KCNQ2 | 0.053 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P |
| [[GRID1]] | B | GRID1 activity raises ADGRB1's level | lines that do not express GRID1 (27) vs lines expressing it (23) | 1.71× lower at baseline in the lines without GRID1 | 0.063 | ⚠ within organs, on part of the lines; also absent: LINC02643, EPGN, MSI1; maybe low, not absent |
| [[PAX2]] | B | PAX2 activity raises ADGRB1's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.20× lower at baseline in the lines without PAX2 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[CACNA1H]] | C | CACNA1H activity raises ADGRB1's level | lines that do not express CACNA1H (23) vs lines expressing it (27) | 2.52× lower at baseline in the lines without CACNA1H | 0.015 | ⚠ within organs, on part of the lines; also absent: LHX2, LMX1B, JPH3; co-absent with the target |
| [[LMX1B]] | C | LMX1B activity raises ADGRB1's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 2.64× lower at baseline in the lines without LMX1B | 0.039 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 10, C 3. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYT9-AS1]] | B | ADGRB1 activity raises SYT9-AS1's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 1.50× lower at baseline in the lines without ADGRB1 | 0.065 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent |
| [[KIF1A]] | B | ADGRB1 activity raises KIF1A's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 4.15× lower at baseline in the lines without ADGRB1 | 0.070 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent |
| [[SBK1]] | B | ADGRB1 activity raises SBK1's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 2.35× lower at baseline in the lines without ADGRB1 | 0.071 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent |
| [[PTP4A3]] | B | ADGRB1 activity raises PTP4A3's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 1.73× lower at baseline in the lines without ADGRB1 | 0.074 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent |
| [[KCNQ2]] | B | ADGRB1 activity raises KCNQ2's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 2.34× lower at baseline in the lines without ADGRB1 | 0.074 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent |
| [[PHF21B]] | B | ADGRB1 activity raises PHF21B's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 3.33× lower at baseline in the lines without ADGRB1 | 0.074 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent |
| [[PLCXD1]] | B | ADGRB1 activity raises PLCXD1's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 2.02× lower at baseline in the lines without ADGRB1 | 0.088 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent |
| [[SEPTIN3]] | B | ADGRB1 activity raises SEPTIN3's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 2.11× lower at baseline in the lines without ADGRB1 | 0.089 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent |
| [[CBFA2T3]] | B | ADGRB1 activity raises CBFA2T3's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 1.95× lower at baseline in the lines without ADGRB1 | 0.097 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent |
| [[FBXO27]] | B | ADGRB1 activity raises FBXO27's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 2.47× lower at baseline in the lines without ADGRB1 | 0.098 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent |
| [[B4GALNT4]] | C | ADGRB1 activity raises B4GALNT4's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 2.58× lower at baseline in the lines without ADGRB1 | 0.038 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent; co-absent with the target |
| [[LMX1B]] | C | ADGRB1 activity raises LMX1B's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 2.45× lower at baseline in the lines without ADGRB1 | 0.097 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.8, 37.6); signed map (24.7, 25.2). **Vector** length 56.7, 11.7% of its response variance represented; |z| ≥ 3 in 721 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +1.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.4 | +3.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.6 | -5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.0 | -3.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | -1.8 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -1.7 | -7.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -0.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | +0.3 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:142,449,430-142,545,009 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously BAI1 |
| Gene groups (HGNC) | Adhesion G protein-coupled receptors, subfamily B |
| Matched by | ensembl_id |

**Function**, from UniProt [O14514](https://www.uniprot.org/uniprotkb/O14514) (Adhesion G protein-coupled receptor B1):

> Phosphatidylserine receptor which enhances the engulfment of apoptotic cells. Also mediates the binding and engulfment of Gram-negative bacteria. Stimulates production of reactive oxygen species by macrophages in response to Gram-negative bacteria, resulting in enhanced microbicidal macrophage activity. In the gastric mucosa, required for recognition and engulfment of apoptotic gastric epithelial cells. Promotes myoblast fusion (By similarity). Activates the Rho pathway in a G protein-dependent …

**Summary**, from NCBI Gene [575](https://www.ncbi.nlm.nih.gov/gene/575):

> Angiogenesis is controlled by a local balance between stimulators and inhibitors of new vessel growth and is suppressed under normal physiologic conditions. Angiogenesis has been shown to be essential for growth and metastasis of solid tumors. In order to obtain blood supply for their growth, tumor cells are potently angiogenic and attract new vessels as results of increased secretion of inducers and decreased production of endogenous negative regulators. BAI1 contains at least one 'functional' …

**Accessions** — [HGNC:943](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:943) · Entrez [575](https://www.ncbi.nlm.nih.gov/gene/575) · UniProt [O14514](https://www.uniprot.org/uniprotkb/O14514) · Ensembl [ENSG00000181790](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181790)

## Data

Gene col 11213: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11213); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11213, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11213]; `tensor/DDL_lfc|DDL_z.npy` [11213]; `embed/gene_vectors.npy` [11213]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11213 or target_col == 11213). Every well: [[ADGRB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
