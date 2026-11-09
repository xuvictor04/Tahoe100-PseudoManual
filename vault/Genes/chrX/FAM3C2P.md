---
symbol: "FAM3C2P"
type: "gene"
col: 10456
ensembl_id: "ENSG00000174028"
name: "family with sequence similarity 3 member C2, pseudogene"
location: "Xp22.11"
module: 34
arm: "+"
pooled_cpm: 2.63
n_lines_expressing: 44
n_dd_up: 7
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 8
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# FAM3C2P

*family with sequence similarity 3 member C2, pseudogene* — Xp22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.48× (z +9.1, q 4e-17, up in 5 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +3.8, q 0.015, up in 1 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.821× (z -5.3, q 8e-05, down in 23 of 40 measured lines) ⚠ position not correctable. The strongest without an alert is [[Trametinib (drug)]] 5 µM: 0.590× (z -4.0, q 0.021, down in 12 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (Panc 03.27 0.0850×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (HEC-1-A 0.0419×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (PANC-1 0.181×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM3C]] (+0.67, fdr 1e-05), [[ITGA6]] (+0.59, fdr 1e-05), [[ITPRID2]] (+0.58, fdr 2e-05); moves opposite to [[BATF]] (-0.52, fdr 4e-05), [[WTAP]] (-0.50, fdr 5e-05), [[RAF1]] (-0.49, fdr 7e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[AMOTL1]] → it (grade B ⚠); 8 go from it, the strongest it → [[FAM3C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10456.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.48×** | +9.1 | 4e-17 | 5/5 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.51×** | +6.5 | 3e-08 | 5/7 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.24×** | +6.1 | 2e-07 | 8/13 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.65×** | +3.8 | 0.015 | 8/36 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.8 | 0.015 | 1/24 (NCI-H460) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.8 | 0.015 | 3/20 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.92×** | +3.5 | 0.033 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | 1.51× | +3.0 | 0.15 | 1/20 (HS-578T) | top dose only | position effect removed |
| [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | 1.49× | +3.0 | 0.15 | 2/29 (HCT15, NCI-H2030) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10456.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (Panc 03.27 0.0850×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (HEC-1-A 0.0419×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (PANC-1 0.181×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.821×** | -5.3 | 8e-05 | 23/40 (MIA PaCa-2, SW1417, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.590×** | -4.0 | 0.021 | 12/39 (AsPC-1, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.614×** | -3.7 | 0.036 | 9/37 (HOP62, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.657× | -3.2 | 0.18 | 8/38 (NCI-H23, SW48, …) | rises with dose | position effect removed |
| [[Baicalin (drug)]] 5 µM |  | 0.746× | -3.1 | 0.19 | 2/40 (HOP62, LoVo) | top dose only | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.657× | -3.1 | 0.19 | 8/29 (NCI-H1792, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Tadalafil (drug)]] 5 µM |  | 0.665× | -3.0 | 0.19 | 0/28 | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10456. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 2.92 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0419× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0850× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 2.55 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -9.1) |
| [[A-172 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.725 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.953 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.912 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.473 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.560 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.915 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.893 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10456), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM3C]] | +0.67 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[ITGA6]] | +0.59 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[ITPRID2]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[CDCP1]] | +0.58 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[ITGA2]] | +0.57 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[OSBPL8]] | +0.56 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[ITGB1]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[WNT7A]] | +0.54 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[VSIG1]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[S100A16]] | +0.52 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[WNT7B]] | +0.51 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[BZW1]] | +0.51 | +0.46 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BATF]] | -0.52 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[WTAP]] | -0.50 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[RAF1]] | -0.49 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[AZI2]] | -0.48 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[DHX58]] | -0.47 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[IL4I1]] | -0.47 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[GALT]] | -0.45 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[CNTNAP1]] | -0.45 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[HEIH]] | -0.45 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[CEBPD]] | -0.45 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[INTS12]] | -0.45 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[UBE2E1]] | -0.44 | -0.37 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AMOTL1]] | B | AMOTL1 activity raises FAM3C2P's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 1.35× lower at baseline in the lines without AMOTL1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN |
| [[LEMD1]] | B | LEMD1 activity raises FAM3C2P's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 1.46× lower at baseline in the lines without LEMD1 | 0.073 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[WNT7B]] | B | WNT7B activity raises FAM3C2P's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 1.40× lower at baseline in the lines without WNT7B | 0.082 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[TINAGL1]] | B | TINAGL1 activity raises FAM3C2P's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.41× lower at baseline in the lines without TINAGL1 | 0.087 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM3C]] | B | FAM3C2P activity raises FAM3C's level | lines that do not express FAM3C2P (6) vs lines expressing it (44) | 2.82× lower at baseline in the lines without FAM3C2P | 0.012 | ⚠ within organs, on part of the lines; also absent: CMTM7, ARHGAP10, IQSEC2; maybe low, not absent |
| [[ENDOD1]] | B | FAM3C2P activity strengthens ENDOD1's drug response | lines that do not express FAM3C2P (6) vs lines expressing it (40) | the lines without FAM3C2P respond 0.50× as strongly (z diff +1.50); strongest at Harringtonine 5 µM: 1.28x vs 0.34x (z diff +5.7) | 0.033 | ⚠ within organs, on part of the lines; also absent: CMTM7, ARHGAP10, IQSEC2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[DENND5A]] | B | FAM3C2P activity raises DENND5A's level | lines that do not express FAM3C2P (6) vs lines expressing it (44) | 1.63× lower at baseline in the lines without FAM3C2P | 0.039 | ⚠ within organs, on part of the lines; also absent: CMTM7, ARHGAP10, IQSEC2; maybe low, not absent |
| [[DCBLD2]] | B | FAM3C2P activity raises DCBLD2's level | lines that do not express FAM3C2P (6) vs lines expressing it (44) | 1.82× lower at baseline in the lines without FAM3C2P | 0.051 | ⚠ within organs, on part of the lines; also absent: CMTM7, ARHGAP10, IQSEC2; maybe low, not absent |
| [[C14orf93]] | B | FAM3C2P activity lowers C14orf93's level | lines that do not express FAM3C2P (6) vs lines expressing it (44) | 1.33× higher at baseline in the lines without FAM3C2P | 0.057 | ⚠ within organs, on part of the lines; also absent: CMTM7, ARHGAP10, IQSEC2; maybe low, not absent |
| [[SYT13]] | B | FAM3C2P activity lowers SYT13's level | lines that do not express FAM3C2P (6) vs lines expressing it (44) | 1.91× higher at baseline in the lines without FAM3C2P | 0.062 | ⚠ within organs, on part of the lines; also absent: CMTM7, ARHGAP10, IQSEC2; maybe low, not absent |
| [[MFNG]] | B | FAM3C2P activity lowers MFNG's level | lines that do not express FAM3C2P (6) vs lines expressing it (44) | 1.85× higher at baseline in the lines without FAM3C2P | 0.074 | ⚠ within organs, on part of the lines; also absent: CMTM7, ARHGAP10, IQSEC2; maybe low, not absent |
| [[MGAT4A]] | B | FAM3C2P activity lowers MGAT4A's level | lines that do not express FAM3C2P (6) vs lines expressing it (44) | 2.21× higher at baseline in the lines without FAM3C2P | 0.091 | ⚠ within organs, on part of the lines; also absent: CMTM7, ARHGAP10, IQSEC2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.583). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.9, 4.3); signed map (3.7, 42.5). **Vector** length 38.6, 4.66% of its response variance represented; |z| ≥ 3 in 823 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.5 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +0.8 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.7 | +1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +0.7 | +1.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.9 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.5 | -3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.5 | -0.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -2.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.4 | +1.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 3 member C2, pseudogene |
| Locus type | pseudogene |
| Location | Xp22.11 — chrX:23,075,758-23,076,767 (+) |
| Ensembl biotype | processed_pseudogene |
| Also known as | ; previously FAM3C2 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:34501](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34501) · Entrez [286460](https://www.ncbi.nlm.nih.gov/gene/286460) · Ensembl [ENSG00000174028](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174028)

## Data

Gene col 10456: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10456); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10456, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10456]; `tensor/DDL_lfc|DDL_z.npy` [10456]; `embed/gene_vectors.npy` [10456]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10456 or target_col == 10456). Every well: [[FAM3C2P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM3C2P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
