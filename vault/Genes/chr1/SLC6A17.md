---
symbol: "SLC6A17"
type: "gene"
col: 12342
ensembl_id: "ENSG00000197106"
name: "solute carrier family 6 member 17"
location: "1p13.3"
module: 82
arm: "+"
pooled_cpm: 2.37
n_lines_expressing: 22
n_dd_up: 31
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 9
direction_downstream: 12
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# SLC6A17

*solute carrier family 6 member 17* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.47× (z +12.2, q 2e-31, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.59× (z +10.0, q 4e-21, up in 4 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[crizotinib (drug)]] 5 µM: 0.588× (z -3.9, q 0.065, down in 3 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H2030 0.0734×, SHP-77 0.129×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.208×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JAKMIP1]] (+0.67, fdr 1e-05), [[TSPYL5]] (+0.61, fdr 1e-05), [[CHST8]] (+0.61, fdr 1e-05); moves opposite to [[USP49]] (-0.54, fdr 1e-04), [[LEPR]] (-0.46, fdr 9e-05), [[PMS2P4-1]] (-0.45, fdr 4e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[EPHA10]] → it (grade B ⚠); 12 go from it, the strongest it → [[FAM184A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12342.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.47×** | +12.2 | 2e-31 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.59×** | +10.0 | 4e-21 | 4/14 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +9.4 | 8e-19 | 1/11 (A549) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.53×** | +8.5 | 3e-15 | 1/4 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.94×** | +6.9 | 4e-10 | 13/19 (NCI-H23, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.41×** | +6.5 | 6e-09 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.43×** | +6.4 | 2e-08 | 4/9 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.63×** | +5.1 | 2e-05 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.95×** | +5.0 | 4e-05 | 7/13 (SK-MEL-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +4.8 | 9e-05 | 14/19 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.76×** | +4.2 | 0.001 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +4.2 | 0.002 | 2/10 (NCI-H1573, NCI-H2030) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.72×** | +4.0 | 0.002 | 0/10 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +4.0 | 0.002 | 12/18 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.10×** | +3.9 | 0.003 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +3.9 | 0.003 | 13/19 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.63×** | +3.6 | 0.011 | 8/17 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.014 | 6/15 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.66×** | +3.4 | 0.020 | 1/10 (PANC-1) | all doses, stronger at high dose | position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.57×** | +3.4 | 0.023 | 1/10 (NCI-H23) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.55×** | +3.2 | 0.031 | 2/9 (NCI-H1573, NCI-H2030) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.032 | 1/19 (NCI-H23) | top dose only | low cells (technical?); cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12342.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H2030 0.0734×, SHP-77 0.129×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.208×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[crizotinib (drug)]] 5 µM |  | **0.588×** | -3.9 | 0.065 | 3/16 (NCI-H1573, H4, …) | top dose only |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.627× | -3.5 | 0.11 | 6/19 (NCI-H1573, H4, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | 0.739× | -3.3 | 0.22 | 6/19 (SHP-77, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12342. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 33.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 7.14 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0734× (z -10.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.198 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.652 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.287 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.254 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.619 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.264 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.836 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.180 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.198 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.282 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.197 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.197 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.173 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.254 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.195 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.243 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.450 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.203 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.247 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12342), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JAKMIP1]] | +0.67 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[TSPYL5]] | +0.61 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[CHST8]] | +0.61 | +0.52 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[RET]] | +0.60 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[ADCY1]] | +0.60 | +0.45 / +0.72 | both halves | 3e-05 |  |
| [[DPYSL5]] | +0.59 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[GABRB3]] | +0.59 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[SULT4A1]] | +0.56 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[PDGFD]] | +0.56 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[LPAR3]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[SYN2]] | +0.55 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[ADD2]] | +0.54 | +0.53 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP49]] | -0.54 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[LEPR]] | -0.46 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[PMS2P4-1]] | -0.45 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA10]] | B | EPHA10 activity raises SLC6A17's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 1.56× lower at baseline in the lines without EPHA10 | 0.062 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |
| [[MAGEA4]] | C | MAGEA4 activity raises SLC6A17's level | lines that do not express MAGEA4 (41) vs lines expressing it (9) | 3.45× lower at baseline in the lines without MAGEA4 | 0.033 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG; co-absent with the target |
| [[MYT1]] | C | MYT1 activity raises SLC6A17's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 2.00× lower at baseline in the lines without MYT1 | 0.048 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2; co-absent with the target |
| [[GNAO1]] | C | GNAO1 activity raises SLC6A17's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 2.40× lower at baseline in the lines without GNAO1 | 0.049 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17; co-absent with the target |
| [[JPH3]] | C | JPH3 activity raises SLC6A17's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 2.44× lower at baseline in the lines without JPH3 | 0.057 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent; co-absent with the target |
| [[KIF1A]] | C | KIF1A activity raises SLC6A17's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 2.20× lower at baseline in the lines without KIF1A | 0.067 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7; co-absent with the target |
| [[CHGB]] | C | CHGB activity raises SLC6A17's level | lines that do not express CHGB (33) vs lines expressing it (17) | 2.18× lower at baseline in the lines without CHGB | 0.069 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2; co-absent with the target |
| [[CTNNA2]] | C | CTNNA2 activity raises SLC6A17's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.46× lower at baseline in the lines without CTNNA2 | 0.072 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7; co-absent with the target |
| [[RASGEF1A]] | C | RASGEF1A activity raises SLC6A17's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 2.03× lower at baseline in the lines without RASGEF1A | 0.072 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 3, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM184A]] | B | SLC6A17 activity raises FAM184A's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 2.29× lower at baseline in the lines without SLC6A17 | 0.030 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT |
| [[EBF2]] | B | SLC6A17 activity raises EBF2's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 1.97× lower at baseline in the lines without SLC6A17 | 0.058 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT |
| [[KCNK13]] | B | SLC6A17 activity raises KCNK13's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 1.47× lower at baseline in the lines without SLC6A17 | 0.091 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT |
| [[SCN8A]] | C | SLC6A17 activity raises SCN8A's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 3.41× lower at baseline in the lines without SLC6A17 | 0.003 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT; co-absent with the target |
| [[GNAO1]] | C | SLC6A17 activity raises GNAO1's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 3.89× lower at baseline in the lines without SLC6A17 | 0.009 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT; co-absent with the target |
| [[NFASC]] | C | SLC6A17 activity raises NFASC's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 3.93× lower at baseline in the lines without SLC6A17 | 0.011 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT; co-absent with the target |
| [[JPH3]] | C | SLC6A17 activity raises JPH3's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 3.09× lower at baseline in the lines without SLC6A17 | 0.014 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT; co-absent with the target |
| [[CTNNA2]] | C | SLC6A17 activity raises CTNNA2's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 3.85× lower at baseline in the lines without SLC6A17 | 0.039 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT; co-absent with the target |
| [[KIF1A]] | C | SLC6A17 activity raises KIF1A's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 4.31× lower at baseline in the lines without SLC6A17 | 0.040 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT; co-absent with the target |
| [[FMN2]] | C | SLC6A17 activity raises FMN2's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 3.22× lower at baseline in the lines without SLC6A17 | 0.051 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT; co-absent with the target |
| [[TMEM108]] | C | SLC6A17 activity raises TMEM108's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 3.01× lower at baseline in the lines without SLC6A17 | 0.062 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT; co-absent with the target |
| [[SYT9]] | C | SLC6A17 activity raises SYT9's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 1.69× lower at baseline in the lines without SLC6A17 | 0.094 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.677). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.0, 38.5); signed map (27.7, 27.2). **Vector** length 39.0, 9.43% of its response variance represented; |z| ≥ 3 in 429 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.5 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.6 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.3 | -3.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 6 member 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:110,150,494-110,202,202 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NTT4 |
| Gene groups (HGNC) | Solute carrier family 6 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1V8](https://www.uniprot.org/uniprotkb/Q9H1V8) (Sodium-dependent neutral amino acid transporter SLC6A17):

> Synaptic vesicle transporter with apparent selectivity for neutral amino acids. The transport is sodium-coupled but chloride-independent, likely driven by the proton electrochemical gradient generated by vacuolar H(+)-ATPase in an overall electrogenic mechanism. May contribute to the synaptic uptake of neurotransmitter precursors in a process coupled in part to vesicle exocytosis.

**Summary**, from NCBI Gene [388662](https://www.ncbi.nlm.nih.gov/gene/388662):

> The protein encoded by this gene is a member of the SLC6 family of transporters, which are responsible for the presynaptic uptake of most neurotransmitters. The encoded vesicular transporter is selective for proline, glycine, leucine and alanine. In mouse, the strongest expression of this gene was in cortical and hippocampal tissues where expression increased during embryonic brain development and peaked postnatally. Defects in this gene cause a form of autosomal recessive intellectual …

**Accessions** — [HGNC:31399](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31399) · Entrez [388662](https://www.ncbi.nlm.nih.gov/gene/388662) · UniProt [Q9H1V8](https://www.uniprot.org/uniprotkb/Q9H1V8) · Ensembl [ENSG00000197106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197106)

## Data

Gene col 12342: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12342); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12342, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12342]; `tensor/DDL_lfc|DDL_z.npy` [12342]; `embed/gene_vectors.npy` [12342]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12342 or target_col == 12342). Every well: [[SLC6A17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC6A17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
