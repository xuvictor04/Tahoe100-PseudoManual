---
symbol: "ROBO4"
type: "gene"
col: 7775
ensembl_id: "ENSG00000154133"
name: "roundabout guidance receptor 4"
location: "11q24.2"
module: 116
arm: "+"
pooled_cpm: 2.52
n_lines_expressing: 22
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 20
direction_downstream: 44
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# ROBO4

*roundabout guidance receptor 4* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.37× (z +10.1, q 2e-21, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.76× (z +8.1, q 7e-14, up in 8 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.391× (z -5.0, q 3e-04, down in 11 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADTRP]] (+0.74, fdr 7e-06), [[RDUR]] (+0.72, fdr 7e-06), [[MARCHF4]] (+0.68, fdr 1e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[ADAMTSL1]] → it (grade B ⚠); 44 go from it, the strongest it → [[ROBO3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7775.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.37×** | +10.1 | 2e-21 | 1/5 (Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.17×** | +9.3 | 3e-18 | 3/5 (A-172, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.76×** | +8.1 | 7e-14 | 8/14 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.09×** | +7.4 | 2e-11 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.30×** | +4.8 | 2e-04 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.04×** | +4.0 | 0.005 | 1/8 (A-172) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +3.9 | 0.008 | 1/5 (SNU-423) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.43×** | +3.7 | 0.018 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.90×** | +3.6 | 0.018 | 2/6 (Hs 766T, MIA PaCa-2) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.5 | 0.029 | 0/8 | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +3.3 | 0.042 | 2/14 (RPMI-7951, HOP62) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.77×** | +3.2 | 0.061 | 1/15 (NCI-H1573) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +3.2 | 0.061 | 0/7 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.1 | 0.082 | 2/10 (SNU-423, SK-MEL-2) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7775.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.391×** | -5.0 | 3e-04 | 11/18 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.492×** | -4.1 | 0.011 | 12/19 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.505×** | -4.0 | 0.011 | 7/19 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.512×** | -3.9 | 0.016 | 14/18 (LOX-IMVI, RKO, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.524×** | -3.7 | 0.022 | 11/18 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.532×** | -3.6 | 0.025 | 12/17 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **0.549×** | -3.5 | 0.043 | 6/19 (NCI-H2030, NCI-H1573, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.325×** | -3.4 | 0.051 | 4/18 (A-172, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7775. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 36.7 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0198× (z -17.6) |
| [[A-172 (line)]] | wt | 14.8 | 3 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +18.3) | [[Simotinib (drug)]] 5 µM 0.0716× (z -12.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0866× (z -11.9) |
| [[SNU-423 (line)]] | alt | 8.26 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 20.4× (z +14.1) | [[Panobinostat (drug)]] 0.5 µM 0.0362× (z -11.0) |
| [[RKO (line)]] | wt | 5.42 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0229× (z -10.2) |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.467× (z -9.7) ⚠ position not correctable |
| [[A-427 (line)]] | wt | 0.148 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.226 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.229 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.189 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.137 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.191 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.659 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.210 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.132 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.994 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.790 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.250 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.730 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.178 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.175 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.173 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.147 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.744 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.149 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.148 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.179 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.710 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.230 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.356 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7775), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADTRP]] | +0.74 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[RDUR]] | +0.72 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[MARCHF4]] | +0.68 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[LINC01204]] | +0.66 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[KBTBD8]] | +0.65 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[FGF1]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[LTBP2]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[LINC02454]] | +0.63 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[LINC00702]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[CCDC190]] | +0.63 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[LINC01776]] | +0.63 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[LNCOG]] | +0.62 | +0.53 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 3, C 17. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAMTSL1]] | B | ADAMTSL1 activity raises ROBO4's level | lines that do not express ADAMTSL1 (18) vs lines expressing it (32) | 1.95× lower at baseline in the lines without ADAMTSL1 | 0.048 | ⚠ within organs, on part of the lines; also absent: SHOX2, ACTN2, AK5; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises ROBO4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FJX1]] | B | FJX1 activity raises ROBO4's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 1.86× lower at baseline in the lines without FJX1 | 0.098 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[ESM1]] | C | ESM1 activity raises ROBO4's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 2.80× lower at baseline in the lines without ESM1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865; co-absent with the target |
| [[BNC1]] | C | BNC1 activity raises ROBO4's level | lines that do not express BNC1 (36) vs lines expressing it (14) | 2.58× lower at baseline in the lines without BNC1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SIM1, AJAP1, ENSG00000254337; co-absent with the target |
| [[CCDC190]] | C | CCDC190 activity raises ROBO4's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 2.52× lower at baseline in the lines without CCDC190 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337; co-absent with the target |
| [[PSG5]] | C | PSG5 activity raises ROBO4's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 3.25× lower at baseline in the lines without PSG5 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486; co-absent with the target |
| [[RGS4]] | C | RGS4 activity raises ROBO4's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 2.68× lower at baseline in the lines without RGS4 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486; co-absent with the target |
| [[VEPH1]] | C | VEPH1 activity raises ROBO4's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 2.19× lower at baseline in the lines without VEPH1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC; co-absent with the target |
| [[ADTRP]] | C | ADTRP activity raises ROBO4's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 2.58× lower at baseline in the lines without ADTRP | 0.016 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2; co-absent with the target |
| [[LINC01435]] | C | LINC01435 activity raises ROBO4's level | lines that do not express LINC01435 (37) vs lines expressing it (13) | 2.76× lower at baseline in the lines without LINC01435 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000203434, TMPRSS15, ENSG00000224865; co-absent with the target |
| [[LINC02509]] | C | LINC02509 activity raises ROBO4's level | lines that do not express LINC02509 (35) vs lines expressing it (15) | 2.13× lower at baseline in the lines without LINC02509 | 0.032 | ⚠ within organs, on part of the lines; also absent: POSTN, ITGA11, IRAG2; co-absent with the target |

### Downstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 24, C 20. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ROBO3]] | B | ROBO4 activity raises ROBO3's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.37× lower at baseline in the lines without ROBO4 | 0.005 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[RGMB]] | B | ROBO4 activity raises RGMB's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 1.99× lower at baseline in the lines without ROBO4 | 0.005 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[ARHGAP31]] | B | ROBO4 activity raises ARHGAP31's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 3.48× lower at baseline in the lines without ROBO4 | 0.006 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[RCAN1]] | B | ROBO4 activity raises RCAN1's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.30× lower at baseline in the lines without ROBO4 | 0.006 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[IQCJ-SCHIP1]] | B | ROBO4 activity raises IQCJ-SCHIP1's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.63× lower at baseline in the lines without ROBO4 | 0.013 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[ERCC1]] | B | ROBO4 activity raises ERCC1's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 1.46× lower at baseline in the lines without ROBO4 | 0.015 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[SPHK1]] | B | ROBO4 activity raises SPHK1's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 3.00× lower at baseline in the lines without ROBO4 | 0.016 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[FGF1]] | B | ROBO4 activity raises FGF1's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 1.78× lower at baseline in the lines without ROBO4 | 0.025 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[DELEC1]] | B | ROBO4 activity raises DELEC1's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 1.62× lower at baseline in the lines without ROBO4 | 0.028 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[SHANK1]] | B | ROBO4 activity raises SHANK1's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.74× lower at baseline in the lines without ROBO4 | 0.033 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[CORO2B]] | B | ROBO4 activity raises CORO2B's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.16× lower at baseline in the lines without ROBO4 | 0.042 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[MSANTD3]] | B | ROBO4 activity raises MSANTD3's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.34× lower at baseline in the lines without ROBO4 | 0.047 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.790). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.6, 11.2); signed map (15.0, 45.5). **Vector** length 49.7, 13.7% of its response variance represented; |z| ≥ 3 in 462 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.3 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.2 | +1.4 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.9 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -5.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.6 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -3.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.3 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | roundabout guidance receptor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:124,883,691-124,898,500 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20798, MRB, ECSM4 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Roundabout guidance receptor family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WZ75](https://www.uniprot.org/uniprotkb/Q8WZ75) (Roundabout homolog 4):

> Receptor for Slit proteins, at least for SLIT2, and seems to be involved in angiogenesis and vascular patterning. May mediate the inhibition of primary endothelial cell migration by Slit proteins (By similarity). Involved in the maintenance of endothelial barrier organization and function.

**Summary**, from NCBI Gene [54538](https://www.ncbi.nlm.nih.gov/gene/54538):

> Predicted to enable cell-cell adhesion mediator activity. Involved in angiogenesis and establishment of endothelial barrier. Located in extracellular exosome. Implicated in aortic valve disease 3. Biomarker of pre-eclampsia and thyroid gland carcinoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17985](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17985) · Entrez [54538](https://www.ncbi.nlm.nih.gov/gene/54538) · UniProt [Q8WZ75](https://www.uniprot.org/uniprotkb/Q8WZ75) · Ensembl [ENSG00000154133](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154133)

## Data

Gene col 7775: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7775); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7775, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7775]; `tensor/DDL_lfc|DDL_z.npy` [7775]; `embed/gene_vectors.npy` [7775]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7775 or target_col == 7775). Every well: [[ROBO4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ROBO4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
