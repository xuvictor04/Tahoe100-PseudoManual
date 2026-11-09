---
symbol: "CTTNBP2"
type: "gene"
col: 1171
ensembl_id: "ENSG00000077063"
name: "cortactin binding protein 2"
location: "7q31.31"
module: 87
arm: "+"
pooled_cpm: 19.53
n_lines_expressing: 19
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 21
direction_downstream: 15
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# CTTNBP2

*cortactin binding protein 2* — 7q31.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.44× (z +13.8, q 2e-40, up in 11 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.507× (z -3.9, q 0.042, down in 6 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 11 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C32 0.0579×, hTERT-HPNE 0.0479×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 5 µM in 2 lines (C32 0.116×, SK-MEL-2 0.0497×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.0605×; ⚠ cell-cycle shift, explains ~47% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.224×); [[Auranofin (drug)]] 5 µM in 1 line (C32 0.146×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[A2M]] (+0.73, fdr 7e-06), [[SOX10]] (+0.72, fdr 7e-06), [[LHFPL3-AS1]] (+0.72, fdr 7e-06).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 15 go from it, the strongest it → [[DIRC3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1171.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.44×** | +13.8 | 2e-40 | 11/16 (NCI-H1573, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.08×** | +11.3 | 2e-27 | 11/17 (NCI-H1573, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +6.6 | 9e-09 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.79×** | +6.3 | 3e-08 | 11/16 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +5.8 | 7e-07 | 1/13 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.70×** | +4.1 | 0.003 | 3/15 (NCI-H1573, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.003 | 2/15 (COLO 205, LoVo) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.003 | 4/16 (C32, LoVo, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.007 | 2/15 (LoVo, A549) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +3.8 | 0.008 | 4/15 (COLO 205, C32, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.8 | 0.008 | 2/15 (SW 900, J82) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.7 | 0.008 | 4/15 (hTERT-HPNE, RKO, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +3.7 | 0.009 | 1/12 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.010 | 4/17 (LoVo, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.40×** | +3.4 | 0.025 | 2/15 (SK-MEL-2, RPMI-7951) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.025 | 4/15 (LoVo, J82, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.052 | 7/17 (LoVo, C32, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1171.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 11 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C32 0.0579×, hTERT-HPNE 0.0479×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 5 µM in 2 lines (C32 0.116×, SK-MEL-2 0.0497×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.0605×; ⚠ cell-cycle shift, explains ~47% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.224×); [[Auranofin (drug)]] 5 µM in 1 line (C32 0.146×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.507×** | -3.9 | 0.042 | 6/15 (RKO, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.707×** | -3.8 | 0.042 | 13/16 (RKO, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.726×** | -3.5 | 0.088 | 8/16 (C32, RKO, …) | rises with dose |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM |  | 0.735× | -3.2 | 0.14 | 3/16 (LoVo, AN3 CA, …) | rises with dose |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.727× | -3.2 | 0.14 | 0/16 | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.753× | -3.1 | 0.18 | 4/16 (LoVo, SHP-77, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.756× | -3.1 | 0.18 | 7/16 (C32, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1171. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 776 | 0 | 19 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0605× (z -31.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -16.6) |
| [[RKO (line)]] | wt | 51.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 28.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0479× (z -15.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 23.7 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.33× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -10.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 24.7 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.189× (z -8.7) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0497× (z -8.5) |
| [[HT-29 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -8.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H1573 (line)]] | alt | 5.41 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.91× (z +11.5) | — |
| [[A-172 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.87 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.12 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.66 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1171), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[A2M]] | +0.73 | +0.60 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SOX10]] | +0.72 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[LHFPL3-AS1]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[LINC02941]] | +0.70 | +0.63 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[LEF1]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[PI15]] | +0.64 | +0.46 / +0.69 | both halves | 3e-05 | **novel candidate** |
| [[PLEKHS1]] | +0.63 | +0.61 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[TF]] | +0.62 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[LEF1-AS1]] | +0.61 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[MDGA2]] | +0.60 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[TYR]] | +0.58 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[SAMMSON]] | +0.58 | +0.58 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 2, C 19. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers CTTNBP2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[PLA2G4A]] | B | PLA2G4A activity raises CTTNBP2's level | lines that do not express PLA2G4A (22) vs lines expressing it (28) | 2.17× lower at baseline in the lines without PLA2G4A | 0.098 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3 |
| [[LINC01812]] | C | LINC01812 activity raises CTTNBP2's level | lines that do not express LINC01812 (35) vs lines expressing it (15) | 2.93× lower at baseline in the lines without LINC01812 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622; co-absent with the target |
| [[LHFPL3-AS1]] | C | LHFPL3-AS1 activity raises CTTNBP2's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 6.39× lower at baseline in the lines without LHFPL3-AS1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[APOD]] | C | APOD activity raises CTTNBP2's level | lines that do not express APOD (43) vs lines expressing it (7) | 6.19× lower at baseline in the lines without APOD | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LHFPL3-AS1, SOX10, CALCA; co-absent with the target |
| [[TYR]] | C | TYR activity raises CTTNBP2's level | lines that do not express TYR (43) vs lines expressing it (7) | 5.41× lower at baseline in the lines without TYR | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[RHOJ]] | C | RHOJ activity raises CTTNBP2's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 1.82× lower at baseline in the lines without RHOJ | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[TDRD9]] | C | TDRD9 activity raises CTTNBP2's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 2.98× lower at baseline in the lines without TDRD9 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT; co-absent with the target |
| [[LEF1]] | C | LEF1 activity raises CTTNBP2's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 3.01× lower at baseline in the lines without LEF1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1; co-absent with the target |
| [[IHO1]] | C | IHO1 activity raises CTTNBP2's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 2.91× lower at baseline in the lines without IHO1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent; co-absent with the target |
| [[COL19A1]] | C | COL19A1 activity raises CTTNBP2's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 2.48× lower at baseline in the lines without COL19A1 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[A2M]] | C | A2M activity raises CTTNBP2's level | lines that do not express A2M (42) vs lines expressing it (8) | 4.07× lower at baseline in the lines without A2M | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 7, C 8. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DIRC3]] | B | CTTNBP2 activity raises DIRC3's level | lines that do not express CTTNBP2 (31) vs lines expressing it (19) | 2.58× lower at baseline in the lines without CTTNBP2 | 0.011 | ⚠ within organs, on part of the lines; also absent: DCT, ENSG00000266976, TYR |
| [[LINC00276]] | B | CTTNBP2 activity raises LINC00276's level | lines that do not express CTTNBP2 (31) vs lines expressing it (19) | 1.72× lower at baseline in the lines without CTTNBP2 | 0.018 | ⚠ within organs, on part of the lines; also absent: DCT, ENSG00000266976, TYR |
| [[ESR1]] | B | CTTNBP2 activity raises ESR1's level | lines that do not express CTTNBP2 (31) vs lines expressing it (19) | 1.39× lower at baseline in the lines without CTTNBP2 | 0.048 | ⚠ within organs, on part of the lines; also absent: DCT, ENSG00000266976, TYR |
| [[MIR3681HG]] | B | CTTNBP2 activity raises MIR3681HG's level | lines that do not express CTTNBP2 (31) vs lines expressing it (19) | 2.33× lower at baseline in the lines without CTTNBP2 | 0.054 | ⚠ within organs, on part of the lines; also absent: DCT, ENSG00000266976, TYR |
| [[DAAM2]] | B | CTTNBP2 activity raises DAAM2's level | lines that do not express CTTNBP2 (31) vs lines expressing it (19) | 1.83× lower at baseline in the lines without CTTNBP2 | 0.054 | ⚠ within organs, on part of the lines; also absent: DCT, ENSG00000266976, TYR |
| [[LOXL3]] | B | CTTNBP2 activity raises LOXL3's level | lines that do not express CTTNBP2 (31) vs lines expressing it (19) | 1.85× lower at baseline in the lines without CTTNBP2 | 0.059 | ⚠ within organs, on part of the lines; also absent: DCT, ENSG00000266976, TYR |
| [[NELL1]] | B | CTTNBP2 activity raises NELL1's level | lines that do not express CTTNBP2 (31) vs lines expressing it (19) | 1.90× lower at baseline in the lines without CTTNBP2 | 0.098 | ⚠ within organs, on part of the lines; also absent: DCT, ENSG00000266976, TYR |
| [[APOD]] | C | CTTNBP2 activity raises APOD's level | lines that do not express CTTNBP2 (31) vs lines expressing it (19) | 2.00× lower at baseline in the lines without CTTNBP2 | 0.023 | ⚠ within organs, on part of the lines; also absent: DCT, ENSG00000266976, TYR; co-absent with the target |
| [[AEBP1]] | C | CTTNBP2 activity raises AEBP1's level | lines that do not express CTTNBP2 (31) vs lines expressing it (19) | 2.41× lower at baseline in the lines without CTTNBP2 | 0.029 | ⚠ within organs, on part of the lines; also absent: DCT, ENSG00000266976, TYR; co-absent with the target |
| [[ATP10B]] | C | CTTNBP2 activity raises ATP10B's level | lines that do not express CTTNBP2 (31) vs lines expressing it (19) | 2.76× lower at baseline in the lines without CTTNBP2 | 0.036 | ⚠ within organs, on part of the lines; also absent: DCT, ENSG00000266976, TYR; co-absent with the target |
| [[TDRD9]] | C | CTTNBP2 activity raises TDRD9's level | lines that do not express CTTNBP2 (31) vs lines expressing it (19) | 1.38× lower at baseline in the lines without CTTNBP2 | 0.039 | ⚠ within organs, on part of the lines; also absent: DCT, ENSG00000266976, TYR; co-absent with the target |
| [[A2M]] | C | CTTNBP2 activity raises A2M's level | lines that do not express CTTNBP2 (31) vs lines expressing it (19) | 2.16× lower at baseline in the lines without CTTNBP2 | 0.086 | ⚠ within organs, on part of the lines; also absent: DCT, ENSG00000266976, TYR; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.759). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.0, 29.1); signed map (29.9, 39.3). **Vector** length 46.5, 12.6% of its response variance represented; |z| ≥ 3 in 359 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +13.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +11.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.6 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +5.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +3.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +4.1 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -2.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -2.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -2.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.7 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | cortactin binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.31 — chr7:117,710,651-117,874,139 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1758, Orf4; previously CORTBP2, C7orf8 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; STRIPAK complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WZ74](https://www.uniprot.org/uniprotkb/Q8WZ74) (Cortactin-binding protein 2):

> Regulates the dendritic spine distribution of CTTN/cortactin in hippocampal neurons, and thus controls dendritic spinogenesis and dendritic spine maintenance. Associates with the striatin-interacting phosphatase and kinase (STRIPAK) core complex to regulate dendritic spine distribution of the STRIPAK complex in hippocampal neurons.

**Summary**, from NCBI Gene [83992](https://www.ncbi.nlm.nih.gov/gene/83992):

> This gene encodes a protein with six ankyrin repeats and several proline-rich regions. A similar gene in rat interacts with a central regulator of the actin cytoskeleton. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15679](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15679) · Entrez [83992](https://www.ncbi.nlm.nih.gov/gene/83992) · UniProt [Q8WZ74](https://www.uniprot.org/uniprotkb/Q8WZ74) · Ensembl [ENSG00000077063](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077063)

## Data

Gene col 1171: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1171); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1171, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1171]; `tensor/DDL_lfc|DDL_z.npy` [1171]; `embed/gene_vectors.npy` [1171]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1171 or target_col == 1171). Every well: [[CTTNBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTTNBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
