---
symbol: "NXPH4"
type: "gene"
col: 11282
ensembl_id: "ENSG00000182379"
name: "neurexophilin 4"
location: "12q13.3"
module: 99
arm: "+"
pooled_cpm: 7.1
n_lines_expressing: 37
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 15
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# NXPH4

*neurexophilin 4* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.01× (z +10.8, q 1e-24, up in 24 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.315× (z -11.0, q 3e-25, down in 21 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IGSF8]] (+0.70, fdr 1e-05), [[GPI]] (+0.68, fdr 1e-05), [[QSOX1]] (+0.67, fdr 2e-05); moves opposite to [[ITPA]] (-0.69, fdr 1e-05), [[DNAJC11]] (-0.66, fdr 1e-05), [[CFLAR]] (-0.65, fdr 1e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CA9]] → it (grade B ⚠); 15 go from it, the strongest it → [[TNFRSF11A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11282.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.01×** | +10.8 | 1e-24 | 24/32 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.81×** | +10.1 | 1e-21 | 24/32 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.71×** | +9.8 | 3e-20 | 21/34 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.23×** | +7.8 | 6e-13 | 11/20 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.73×** | +7.6 | 5e-12 | 19/32 (SW480, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.04×** | +7.0 | 2e-10 | 14/33 (J82, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.84×** | +6.0 | 2e-07 | 13/29 (HT-29, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.73×** | +5.2 | 2e-05 | 2/10 (H4, HS-578T) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +5.1 | 2e-05 | 11/32 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.56×** | +4.0 | 0.003 | 2/10 (LoVo, HS-578T) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.10×** | +3.8 | 0.008 | 2/31 (SW480, SHP-77) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.6 | 0.018 | 3/35 (NCI-H460, HepG2/C3A, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.43×** | +3.5 | 0.020 | 6/33 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.89×** | +3.2 | 0.047 | 0/9 | top dose only | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +3.2 | 0.059 | 4/23 (LoVo, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11282.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.315×** | -11.0 | 3e-25 | 21/31 (HT-29, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.521×** | -9.1 | 2e-17 | 20/26 (HT-29, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.420×** | -8.6 | 2e-15 | 17/27 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.568×** | -5.6 | 3e-06 | 17/32 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.512×** | -3.5 | 0.060 | 6/32 (SW480, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.713×** | -3.4 | 0.070 | 7/31 (NCI-H1573, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.725× | -3.2 | 0.11 | 8/32 (KATO III, C-33 A, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11282. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 28.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0244× (z -32.6) |
| [[KATO III (line)]] | alt | 54.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.00798× (z -32.5) |
| [[NCI-H460 (line)]] | wt | 29.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0416× (z -21.3) |
| [[A549 (line)]] | wt | 4.41 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0219× (z -11.5) |
| [[COLO 205 (line)]] | alt | 8.07 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -9.9) |
| [[HCT15 (line)]] | alt | 20.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0448× (z -20.7) |
| [[SW480 (line)]] | alt | 7.08 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -10.1) |
| [[H4 (line)]] | wt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 3.48 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0558× (z -8.6) |
| [[SNU-423 (line)]] | alt | 3.59 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -8.5) |
| [[A-172 (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.886 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.705 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.851 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11282), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGSF8]] | +0.70 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[GPI]] | +0.68 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[QSOX1]] | +0.67 | +0.69 / +0.46 | both halves | 2e-05 |  |
| [[CDON]] | +0.67 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[WDR45B]] | +0.67 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[PDK3]] | +0.66 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[ANKRD37]] | +0.66 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[ALDOA]] | +0.66 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[P4HB]] | +0.65 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[AHDC1]] | +0.65 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[INSIG2]] | +0.65 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[HK2]] | +0.65 | +0.65 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITPA]] | -0.69 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[DNAJC11]] | -0.66 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[CFLAR]] | -0.65 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[FAIM]] | -0.63 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[EFCAB2]] | -0.63 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[ST7L]] | -0.63 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[DPH5-DT]] | -0.62 | -0.61 / -0.35 | both halves | 1e-04 |  |
| [[MTHFSD]] | -0.62 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[RNF115]] | -0.62 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[ZNF181]] | -0.61 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[PPP3CB-AS1]] | -0.61 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[ZMYND11]] | -0.61 | -0.47 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA9]] | B | CA9 activity strengthens NXPH4's drug response | lines that do not express CA9 (15) vs lines expressing it (19) | the lines without CA9 respond 0.75× as strongly (z diff +0.58); strongest at Homoharringtonine 5 µM: 0.70x vs 0.20x (z diff +5.7) | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF11A]] | B | NXPH4 activity lowers TNFRSF11A's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 2.18× higher at baseline in the lines without NXPH4 | 0.020 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |
| [[ANOS1]] | B | NXPH4 activity lowers ANOS1's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 1.84× higher at baseline in the lines without NXPH4 | 0.027 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |
| [[LRP1]] | B | NXPH4 activity raises LRP1's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 2.21× lower at baseline in the lines without NXPH4 | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |
| [[ALKBH5]] | B | NXPH4 activity raises ALKBH5's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without NXPH4 | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |
| [[SLC17A7]] | B | NXPH4 activity raises SLC17A7's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 1.61× lower at baseline in the lines without NXPH4 | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |
| [[RHPN2]] | B | NXPH4 activity lowers RHPN2's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 2.14× higher at baseline in the lines without NXPH4 | 0.037 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |
| [[ARRB2]] | B | NXPH4 activity raises ARRB2's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 1.70× lower at baseline in the lines without NXPH4 | 0.043 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |
| [[MCF2L]] | B | NXPH4 activity strengthens MCF2L's drug response | lines that do not express NXPH4 (9) vs lines expressing it (25) | the lines without NXPH4 respond 0.74× as strongly (z diff +1.76); strongest at Harringtonine 5 µM: 0.53x vs 0.29x (z diff +3.6) | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[STK32C]] | B | NXPH4 activity raises STK32C's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 1.60× lower at baseline in the lines without NXPH4 | 0.074 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |
| [[QSOX1]] | B | NXPH4 activity lowers QSOX1's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 1.50× higher at baseline in the lines without NXPH4 | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |
| [[DPH5-DT]] | B | NXPH4 activity raises DPH5-DT's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 1.32× lower at baseline in the lines without NXPH4 | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |
| [[SREBF1]] | B | NXPH4 activity raises SREBF1's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 1.43× lower at baseline in the lines without NXPH4 | 0.090 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.757). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.0, -11.0); signed map (-30.8, 22.0). **Vector** length 58.6, 10.7% of its response variance represented; |z| ≥ 3 in 725 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (hallmark, mean cos +0.51 to 17); *Glycolysis* (reactome, mean cos +0.52 to 10); *Glucose metabolism* (reactome, mean cos +0.52 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +5.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.6 | +9.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +10.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +7.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -8.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.0 | -11.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -2.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.7 | -9.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -0.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | neurexophilin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:57,216,794-57,226,449 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NPH4 |
| Gene groups (HGNC) | Neurexophilins |
| Matched by | ensembl_id |

**Function**, from UniProt [O95158](https://www.uniprot.org/uniprotkb/O95158) (Neurexophilin-4):

> May be signaling molecules that resemble neuropeptides and that act by binding to alpha-neurexins and possibly other receptors.

**Summary**, from NCBI Gene [11247](https://www.ncbi.nlm.nih.gov/gene/11247):

> Predicted to enable signaling receptor binding activity. Predicted to be involved in neuropeptide signaling pathway. Predicted to be located in extracellular region. Predicted to be active in GABA-ergic synapse. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:8078](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8078) · Entrez [11247](https://www.ncbi.nlm.nih.gov/gene/11247) · UniProt [O95158](https://www.uniprot.org/uniprotkb/O95158) · Ensembl [ENSG00000182379](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182379)

## Data

Gene col 11282: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11282); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11282, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11282]; `tensor/DDL_lfc|DDL_z.npy` [11282]; `embed/gene_vectors.npy` [11282]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11282 or target_col == 11282). Every well: [[NXPH4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NXPH4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
