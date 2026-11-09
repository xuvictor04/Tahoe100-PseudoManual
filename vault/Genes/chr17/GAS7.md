---
symbol: "GAS7"
type: "gene"
col: 140
ensembl_id: "ENSG00000007237"
name: "growth arrest specific 7"
location: "17p13.1"
module: 87
arm: "+"
pooled_cpm: 11.72
n_lines_expressing: 26
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 9
direction_downstream: 3
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# GAS7

*growth arrest specific 7* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.75× (z +14.7, q 0e+00, up in 2 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.30× (z +13.6, q 2e-39, up in 18 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Futibatinib (drug)]] 0.05 µM: 0.696× (z -4.0, q 0.040, down in 3 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EDNRB]] (+0.63, fdr 1e-05), [[C10orf90]] (+0.62, fdr 1e-05), [[TYR]] (+0.62, fdr 1e-05).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[LINC02941]] → it (grade C ⚠); 3 go from it, the strongest it → [[SPOCK3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 140.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.75×** | +14.7 | 0e+00 | 2/7 (HOP62, SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.30×** | +13.6 | 2e-39 | 18/22 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.99×** | +12.6 | 3e-34 | 2/12 (SW 900, RPMI-7951) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +10.1 | 7e-22 | 9/22 (A549, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.46×** | +9.6 | 1e-19 | 3/7 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +8.4 | 5e-15 | 6/20 (LoVo, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.94×** | +7.6 | 2e-12 | 16/22 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +5.6 | 1e-06 | 11/22 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.62×** | +5.6 | 2e-06 | 12/23 (NCI-H2030, HOP62, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.1 | 2e-05 | 6/23 (A-172, LoVo, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +4.0 | 0.003 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.37×** | +3.5 | 0.023 | 4/13 (A549, LS 180, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.023 | 7/22 (COLO 205, AN3 CA, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.4 | 0.023 | 0/8 | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.034 | 12/23 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.36×** | +3.3 | 0.037 | 6/21 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.081 | 8/22 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 140.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Futibatinib (drug)]] 0.05 µM |  | **0.696×** | -4.0 | 0.040 | 3/22 (AN3 CA, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.701×** | -3.8 | 0.040 | 2/23 (NCI-H1573, COLO 205) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.727×** | -3.7 | 0.042 | 6/21 (C32, SK-MEL-2, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.733×** | -3.6 | 0.044 | 11/22 (C32, NCI-H460, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.738×** | -3.5 | 0.044 | 5/21 (LoVo, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.564×** | -3.5 | 0.044 | 8/22 (C32, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.742×** | -3.5 | 0.044 | 7/22 (C-33 A, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Asciminib (drug)]] 0.05 µM |  | 0.766× | -3.1 | 0.13 | 2/22 (NCI-H23, SK-MEL-2) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.766× | -3.1 | 0.13 | 7/23 (C32, SK-MEL-2, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.831× | -3.0 | 0.13 | 6/22 (C32, SK-MEL-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 140. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 267 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -12.9) |
| [[A-427 (line)]] | wt | 23.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -10.6) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.300× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 83.7 | 0 | 3 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.323× (z -9.7) |
| [[CHP-212 (line)]] | wt | 89.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0491× (z -18.4) |
| [[LoVo (line)]] | wt | 3.43 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +13.6) | [[Belinostat (drug)]] 0.5 µM 0.0852× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 38.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.272× (z -8.7) |
| [[BT-474 (line)]] | alt | 30.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.94× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 6.10 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.197× (z -9.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.83 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 140), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDNRB]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[C10orf90]] | +0.62 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[TYR]] | +0.62 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[A2M]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[EFR3B]] | +0.61 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[LDLRAD4]] | +0.61 | +0.58 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[SOX10]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[MIR3681HG]] | +0.59 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[LINC01205]] | +0.59 | +0.40 / +0.56 | both halves | 4e-05 |  |
| [[COL9A3]] | +0.58 | +0.39 / +0.45 | both halves | 6e-05 |  |
| [[TRPM8]] | +0.58 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[PI15]] | +0.58 | +0.37 / +0.57 | both halves | 9e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02941]] | C | LINC02941 activity raises GAS7's level | lines that do not express LINC02941 (34) vs lines expressing it (16) | 4.59× lower at baseline in the lines without LINC02941 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, CHL1, COL19A1; co-absent with the target |
| [[LEF1-AS1]] | C | LEF1-AS1 activity raises GAS7's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 3.56× lower at baseline in the lines without LEF1-AS1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent; co-absent with the target |
| [[A2M]] | C | A2M activity raises GAS7's level | lines that do not express A2M (42) vs lines expressing it (8) | 4.95× lower at baseline in the lines without A2M | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |
| [[SDC2]] | C | SDC2 activity raises GAS7's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 2.54× lower at baseline in the lines without SDC2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH; co-absent with the target |
| [[ASXL3]] | C | ASXL3 activity raises GAS7's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 2.12× lower at baseline in the lines without ASXL3 | 0.060 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent; co-absent with the target |
| [[TYR]] | C | TYR activity raises GAS7's level | lines that do not express TYR (43) vs lines expressing it (7) | 6.74× lower at baseline in the lines without TYR | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[LHFPL3-AS1]] | C | LHFPL3-AS1 activity raises GAS7's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 6.64× lower at baseline in the lines without LHFPL3-AS1 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[CHRNA7]] | C | CHRNA7 activity raises GAS7's level | lines that do not express CHRNA7 (19) vs lines expressing it (31) | 2.59× lower at baseline in the lines without CHRNA7 | 0.091 | ⚠ within organs, on part of the lines; also absent: LRRC4B, NKD2, IGFL4; maybe low, not absent; co-absent with the target |
| [[TF]] | C | TF activity raises GAS7's level | lines that do not express TF (41) vs lines expressing it (9) | 4.19× lower at baseline in the lines without TF | 0.097 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPOCK3]] | B | GAS7 activity lowers SPOCK3's level | lines that do not express GAS7 (24) vs lines expressing it (26) | 1.26× higher at baseline in the lines without GAS7 | 0.047 | ⚠ within organs, on part of the lines; also absent: COLEC12, ADCY1, MAPK4 |
| cells under [[GSK1059615 (drug)]] 0.5 µM | B | GAS7 activity lowers the cells' numbers under GSK1059615 0.5 µM (makes them more sensitive) | lines that do not express GAS7 (24) vs lines expressing it (24) | the lines without GAS7: 1.20× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: COLEC12, ADCY1, MAPK4 |
| [[NHSL2]] | C | GAS7 activity raises NHSL2's level | lines that do not express GAS7 (24) vs lines expressing it (26) | 1.59× lower at baseline in the lines without GAS7 | 0.082 | ⚠ within organs, on part of the lines; also absent: COLEC12, ADCY1, MAPK4; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.708). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.2, 28.8); signed map (29.5, 39.2). **Vector** length 53.6, 11.3% of its response variance represented; |z| ≥ 3 in 624 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +14.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +9.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +4.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +3.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.3 | -0.1 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -3.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -3.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | growth arrest specific 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:9,910,606-10,198,606 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0394, MGC1348 |
| Gene groups (HGNC) | F-BAR domain containing; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O60861](https://www.uniprot.org/uniprotkb/O60861) (Growth arrest-specific protein 7):

> May play a role in promoting maturation and morphological differentiation of cerebellar neurons.

**Summary**, from NCBI Gene [8522](https://www.ncbi.nlm.nih.gov/gene/8522):

> Growth arrest-specific 7 is expressed primarily in terminally differentiated brain cells and predominantly in mature cerebellar Purkinje neurons. GAS7 plays a putative role in neuronal development. Several transcript variants encoding proteins which vary in the N-terminus have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4169](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4169) · Entrez [8522](https://www.ncbi.nlm.nih.gov/gene/8522) · UniProt [O60861](https://www.uniprot.org/uniprotkb/O60861) · Ensembl [ENSG00000007237](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007237)

## Data

Gene col 140: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 140); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 140, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 140]; `tensor/DDL_lfc|DDL_z.npy` [140]; `embed/gene_vectors.npy` [140]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 140 or target_col == 140). Every well: [[GAS7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAS7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
