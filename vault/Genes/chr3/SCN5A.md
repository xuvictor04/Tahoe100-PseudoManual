---
symbol: "SCN5A"
type: "gene"
col: 11469
ensembl_id: "ENSG00000183873"
name: "sodium voltage-gated channel alpha subunit 5"
location: "3p22.2"
module: 27
arm: "+"
pooled_cpm: 11.16
n_lines_expressing: 24
n_dd_up: 7
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 12
direction_downstream: 6
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# SCN5A

*sodium voltage-gated channel alpha subunit 5* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.10× (z +10.7, q 5e-24, up in 7 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.589× (z -5.2, q 6e-05, down in 11 of 20 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BLACAT1]] (+0.59, fdr 1e-05), [[FGF19]] (+0.59, fdr 1e-05), [[TMEM163]] (+0.58, fdr 1e-05); moves opposite to [[SLC16A14]] (-0.42, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[CACNA2D4]] → it (grade B ⚠); 6 go from it, the strongest it → [[IL17RD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11469.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +10.7 | 5e-24 | 7/18 (A-172, LoVo, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.40×** | +8.6 | 2e-15 | 2/7 (SW1417, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.19×** | +8.0 | 3e-13 | 6/14 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.04×** | +7.3 | 4e-11 | 11/21 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +6.5 | 8e-09 | 9/20 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +5.1 | 3e-05 | 6/20 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +3.5 | 0.037 | 2/8 (HEC-1-A, LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.54× | +3.1 | 0.12 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11469.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.589×** | -5.2 | 6e-05 | 11/20 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.603×** | -5.2 | 6e-05 | 14/17 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.707×** | -5.0 | 9e-05 | 16/18 (SW480, SW1417, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.650×** | -4.4 | 0.001 | 8/19 (A549, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.684×** | -3.9 | 0.011 | 17/21 (SW480, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); composition shift |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.690×** | -3.6 | 0.030 | 2/20 (MIA PaCa-2, Panc 03.27) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.706×** | -3.6 | 0.030 | 6/20 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.713×** | -3.3 | 0.056 | 3/20 (SW480, SNU-423, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **0.734×** | -3.3 | 0.056 | 4/21 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM |  | **0.797×** | -3.3 | 0.056 | 4/21 (SW480, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.550×** | -3.2 | 0.072 | 8/18 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.721×** | -3.2 | 0.074 | 12/20 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | **0.723×** | -3.1 | 0.091 | 2/20 (J82, A549) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.742×** | -3.1 | 0.091 | 8/21 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.746× | -3.0 | 0.10 | 7/21 (SW480, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11469. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 119 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -15.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.181× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 8.99 | 0 | 6 (4 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0502× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0740× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 23.6 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0482× (z -16.5) |
| [[C-33 A (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -8.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 8.67 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -10.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LoVo (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -10.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 5.19 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0767× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -10.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW1417 (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -13.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.890 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.877 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.37 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11469), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLACAT1]] | +0.59 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[FGF19]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[TMEM163]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[PADI1]] | +0.58 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[APCDD1]] | +0.57 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[VWA2]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[CACNA2D4]] | +0.55 | +0.46 / +0.50 | both halves | 3e-05 | STRING 414 |
| [[CARD11]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[IGFL4]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[B3GNT3]] | +0.55 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[PSG1]] | +0.54 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[ST6GALNAC5]] | +0.54 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC16A14]] | -0.42 | -0.41 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 3, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA2D4]] | B | CACNA2D4 activity raises SCN5A's level | lines that do not express CACNA2D4 (22) vs lines expressing it (28) | 1.66× lower at baseline in the lines without CACNA2D4 | 0.045 | ⚠ within organs, on part of the lines; also absent: ARHGDIB, NRP2, RFX8; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers SCN5A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[VWA2]] | B | VWA2 activity raises SCN5A's level | lines that do not express VWA2 (36) vs lines expressing it (14) | 1.79× lower at baseline in the lines without VWA2 | 0.078 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1 |
| [[SHISA9]] | C | SHISA9 activity raises SCN5A's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 2.82× lower at baseline in the lines without SHISA9 | 0.001 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent; co-absent with the target |
| [[PSG1]] | C | PSG1 activity raises SCN5A's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 3.26× lower at baseline in the lines without PSG1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |
| [[WNT7A]] | C | WNT7A activity raises SCN5A's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 2.91× lower at baseline in the lines without WNT7A | 0.015 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6; co-absent with the target |
| [[TMEM163]] | C | TMEM163 activity raises SCN5A's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 2.36× lower at baseline in the lines without TMEM163 | 0.021 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2; co-absent with the target |
| [[ANO4]] | C | ANO4 activity raises SCN5A's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 2.13× lower at baseline in the lines without ANO4 | 0.067 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent; co-absent with the target |
| [[CARD11]] | C | CARD11 activity raises SCN5A's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 1.99× lower at baseline in the lines without CARD11 | 0.069 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3; co-absent with the target |
| [[APCDD1]] | C | APCDD1 activity raises SCN5A's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 2.29× lower at baseline in the lines without APCDD1 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751; co-absent with the target |
| [[LAPTM5]] | C | LAPTM5 activity raises SCN5A's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 1.64× lower at baseline in the lines without LAPTM5 | 0.094 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2; co-absent with the target |
| [[JAKMIP2-AS1]] | C | JAKMIP2-AS1 activity raises SCN5A's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 2.28× lower at baseline in the lines without JAKMIP2-AS1 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL17RD]] | B | SCN5A activity raises IL17RD's level | lines that do not express SCN5A (26) vs lines expressing it (24) | 2.09× lower at baseline in the lines without SCN5A | 0.020 | ⚠ within organs, on part of the lines; also absent: ANKRD20A11P, OLFML2A, SHISA9 |
| [[CEP295NL]] | B | SCN5A activity raises CEP295NL's level | lines that do not express SCN5A (26) vs lines expressing it (24) | 1.46× lower at baseline in the lines without SCN5A | 0.034 | ⚠ within organs, on part of the lines; also absent: ANKRD20A11P, OLFML2A, SHISA9 |
| [[ATG9B]] | B | SCN5A activity raises ATG9B's level | lines that do not express SCN5A (26) vs lines expressing it (24) | 1.85× lower at baseline in the lines without SCN5A | 0.060 | ⚠ within organs, on part of the lines; also absent: ANKRD20A11P, OLFML2A, SHISA9 |
| [[BMP8B]] | B | SCN5A activity raises BMP8B's level | lines that do not express SCN5A (26) vs lines expressing it (24) | 1.41× lower at baseline in the lines without SCN5A | 0.087 | ⚠ within organs, on part of the lines; also absent: ANKRD20A11P, OLFML2A, SHISA9 |
| [[ST6GALNAC5]] | C | SCN5A activity raises ST6GALNAC5's level | lines that do not express SCN5A (26) vs lines expressing it (24) | 2.40× lower at baseline in the lines without SCN5A | 0.033 | ⚠ within organs, on part of the lines; also absent: ANKRD20A11P, OLFML2A, SHISA9; co-absent with the target |
| [[SHISA9]] | C | SCN5A activity raises SHISA9's level | lines that do not express SCN5A (26) vs lines expressing it (24) | 1.85× lower at baseline in the lines without SCN5A | 0.086 | ⚠ within organs, on part of the lines; also absent: ANKRD20A11P, OLFML2A, SHISA9; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.394). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.8, 43.1); signed map (64.7, 15.8). **Vector** length 56.6, 14.1% of its response variance represented; |z| ≥ 3 in 551 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +3.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.5 | +7.3 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.1 | +2.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.0 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +3.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.0 | +2.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.9 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.0 | -5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.4 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | sodium voltage-gated channel alpha subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.2 — chr3:38,548,057-38,649,743 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Nav1.5, LQT3, HB1, HBBD, PFHB1, IVF, HB2, HH1; previously CMD1E |
| Gene groups (HGNC) | Sodium voltage-gated channel alpha subunits |
| Reactome | 7 pathways, smallest: Interaction between L1 and Ankyrins; Phase 0 - rapid depolarisation; Cardiac conduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14524](https://www.uniprot.org/uniprotkb/Q14524) (Sodium channel protein type 5 subunit alpha):

> Pore-forming subunit of Nav1.5, a voltage-gated sodium (Nav) channel that directly mediates the depolarizing phase of action potentials in excitable membranes. Navs, also called VGSCs (voltage-gated sodium channels) or VDSCs (voltage-dependent sodium channels), operate by switching between closed and open conformations depending on the voltage difference across the membrane. In the open conformation they allow Na(+) ions to selectively pass through the pore, along their electrochemical …

**Summary**, from NCBI Gene [6331](https://www.ncbi.nlm.nih.gov/gene/6331):

> The protein encoded by this gene is an integral membrane protein and tetrodotoxin-resistant voltage-gated sodium channel subunit. This protein is found primarily in cardiac muscle and is responsible for the initial upstroke of the action potential in an electrocardiogram. Defects in this gene have been associated with long QT syndrome type 3 (LQT3), atrial fibrillation, cardiomyopathy, and Brugada syndrome 1, all autosomal dominant cardiac diseases. Alternative splicing results in several …

**Accessions** — [HGNC:10593](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10593) · Entrez [6331](https://www.ncbi.nlm.nih.gov/gene/6331) · UniProt [Q14524](https://www.uniprot.org/uniprotkb/Q14524) · Ensembl [ENSG00000183873](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183873)

## Data

Gene col 11469: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11469); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11469, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11469]; `tensor/DDL_lfc|DDL_z.npy` [11469]; `embed/gene_vectors.npy` [11469]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11469 or target_col == 11469). Every well: [[SCN5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCN5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
