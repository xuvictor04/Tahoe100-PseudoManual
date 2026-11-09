---
symbol: "NPAS1"
type: "gene"
col: 5116
ensembl_id: "ENSG00000130751"
name: "neuronal PAS domain protein 1"
location: "19q13.32"
module: 47
arm: "+"
pooled_cpm: 7.94
n_lines_expressing: 41
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 8
direction_downstream: 9
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# NPAS1

*neuronal PAS domain protein 1* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.24× (z +9.1, q 6e-17, up in 23 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.454× (z -8.9, q 3e-16, down in 24 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BMP8A]] (+0.66, fdr 1e-05), [[A3GALT2]] (+0.65, fdr 1e-05), [[DOK3]] (+0.65, fdr 7e-06); moves opposite to [[DECR1]] (-0.58, fdr 3e-05), [[RAB11FIP2]] (-0.53, fdr 2e-05), [[NIPSNAP3A]] (-0.52, fdr 4e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[MEIS3]] → it (grade B ⚠); 9 go from it, the strongest it → [[STON1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5116.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.24×** | +9.1 | 6e-17 | 23/39 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.21×** | +9.0 | 9e-17 | 21/37 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.75×** | +8.9 | 9e-17 | 22/38 (SW480, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.08×** | +8.2 | 2e-14 | 22/38 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +6.5 | 9e-09 | 18/38 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.78×** | +6.5 | 9e-09 | 19/36 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +5.5 | 3e-06 | 16/36 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.61×** | +5.1 | 2e-05 | 2/14 (SNU-423, LoVo) | inconsistent across doses | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +4.5 | 5e-04 | 12/33 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.23×** | +3.4 | 0.045 | 9/35 (A549, NCI-H23, …) | top dose only |  |
| [[Ritonavir (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.059 | 3/38 (NCI-H2030, LoVo, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.084 | 7/39 (SW 900, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5116.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.454×** | -8.9 | 3e-16 | 24/37 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.476×** | -8.4 | 2e-14 | 21/38 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.565×** | -6.4 | 2e-08 | 21/31 (LoVo, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.637×** | -5.1 | 5e-05 | 20/37 (SW 900, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.425×** | -5.0 | 5e-05 | 16/36 (A-427, H4, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM |  | **0.738×** | -4.8 | 1e-04 | 13/38 (HEC-1-A, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.655×** | -4.8 | 2e-04 | 17/36 (C-33 A, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.699×** | -4.0 | 0.004 | 19/37 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.542×** | -3.6 | 0.020 | 13/32 (RPMI-7951, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.718×** | -3.4 | 0.039 | 6/39 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.725×** | -3.3 | 0.043 | 9/37 (MIA PaCa-2, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.755×** | -3.2 | 0.075 | 14/38 (SW 900, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.587×** | -3.1 | 0.076 | 12/30 (RPMI-7951, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5116. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 39.1 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.116× (z -13.4) |
| [[MIA PaCa-2 (line)]] | alt | 29.2 | 1 | 4 (3 ⚠) | [[Auranofin (drug)]] 5 µM 4.23× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.105× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.257× (z -8.5) |
| [[LoVo (line)]] | wt | 17.3 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0968× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -9.4) |
| [[SW 900 (line)]] | alt | 31.4 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0912× (z -10.3) |
| [[A-427 (line)]] | wt | 14.9 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.107× (z -12.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 12.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0911× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H2030 (line)]] | alt | 7.88 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -9.7) |
| [[A549 (line)]] | wt | 5.68 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.19× (z +10.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[H4 (line)]] | wt | 13.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0518× (z -8.8) |
| [[J82 (line)]] | alt | 6.38 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0299× (z -11.8) |
| [[PANC-1 (line)]] | alt | 7.48 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.155× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0541× (z -11.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5116), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMP8A]] | +0.66 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[A3GALT2]] | +0.65 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[DOK3]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[SAMD14]] | +0.64 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[SH2B2]] | +0.62 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[GDF1]] | +0.61 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[CPNE9]] | +0.61 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[PARVG]] | +0.60 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[SNAI1]] | +0.60 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[SMIM41]] | +0.60 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[MIR9-1HG]] | +0.60 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[ASGR1]] | +0.59 | +0.58 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DECR1]] | -0.58 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[RAB11FIP2]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[NIPSNAP3A]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[NNT]] | -0.52 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[C5orf15]] | -0.50 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[RNF146]] | -0.50 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[SCYL3]] | -0.49 | -0.38 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEIS3]] | B | MEIS3 activity raises NPAS1's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 2.51× lower at baseline in the lines without MEIS3 | 0.013 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| [[FAM20C]] | B | FAM20C activity raises NPAS1's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 2.07× lower at baseline in the lines without FAM20C | 0.015 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |
| [[MRC2]] | B | MRC2 activity raises NPAS1's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 2.44× lower at baseline in the lines without MRC2 | 0.027 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |
| [[MMP17]] | B | MMP17 activity raises NPAS1's level | lines that do not express MMP17 (17) vs lines expressing it (33) | 2.37× lower at baseline in the lines without MMP17 | 0.028 | ⚠ within organs, on part of the lines; also absent: NOVA2, TUB, RIMKLB |
| [[PARVG]] | B | PARVG activity raises NPAS1's level | lines that do not express PARVG (15) vs lines expressing it (35) | 2.39× lower at baseline in the lines without PARVG | 0.036 | ⚠ within organs, on part of the lines; also absent: PARVB, DCLK2, RASSF8 |
| [[HCN2]] | B | HCN2 activity raises NPAS1's level | lines that do not express HCN2 (6) vs lines expressing it (44) | 2.70× lower at baseline in the lines without HCN2 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000267131, USP31, PRELID3A; maybe low, not absent |
| [[GBX1]] | B | GBX1 activity raises NPAS1's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 1.95× lower at baseline in the lines without GBX1 | 0.078 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[LINC02813]] | B | LINC02813 activity raises NPAS1's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 1.96× lower at baseline in the lines without LINC02813 | 0.081 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STON1]] | B | NPAS1 activity raises STON1's level | lines that do not express NPAS1 (9) vs lines expressing it (41) | 1.93× lower at baseline in the lines without NPAS1 | 0.011 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MRC2]] | B | NPAS1 activity raises MRC2's level | lines that do not express NPAS1 (9) vs lines expressing it (41) | 3.96× lower at baseline in the lines without NPAS1 | 0.024 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TSHZ3]] | B | NPAS1 activity raises TSHZ3's level | lines that do not express NPAS1 (9) vs lines expressing it (41) | 4.41× lower at baseline in the lines without NPAS1 | 0.033 | ⚠ within organs, on part of the lines; maybe low, not absent |
| cells under [[Ixazomib (drug)]] 5 µM | B | NPAS1 activity lowers the cells' numbers under Ixazomib 5 µM (makes them more sensitive) | lines that do not express NPAS1 (9) vs lines expressing it (39) | the lines without NPAS1: 1.28× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SIDT2]] | B | NPAS1 activity raises SIDT2's level | lines that do not express NPAS1 (9) vs lines expressing it (41) | 1.24× lower at baseline in the lines without NPAS1 | 0.053 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FHAD1]] | B | NPAS1 activity lowers FHAD1's level | lines that do not express NPAS1 (9) vs lines expressing it (41) | 1.94× higher at baseline in the lines without NPAS1 | 0.067 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CLIP2]] | B | NPAS1 activity raises CLIP2's level | lines that do not express NPAS1 (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without NPAS1 | 0.077 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CPNE9]] | B | NPAS1 activity raises CPNE9's level | lines that do not express NPAS1 (9) vs lines expressing it (41) | 1.45× lower at baseline in the lines without NPAS1 | 0.080 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[KIF17]] | B | NPAS1 activity raises KIF17's level | lines that do not express NPAS1 (9) vs lines expressing it (41) | 1.70× lower at baseline in the lines without NPAS1 | 0.099 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.547). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.2, -16.2); signed map (16.2, 16.1). **Vector** length 79.4, 15.7% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.6 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +6.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.1 | +6.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.8 | +9.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +3.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.7 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -3.4 | -5.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -8.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.8 | -4.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | +0.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | neuronal PAS domain protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:47,019,837-47,045,775 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MOP5, PASD5, bHLHe11 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; PAS domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99742](https://www.uniprot.org/uniprotkb/Q99742) (Neuronal PAS domain-containing protein 1):

> May control regulatory pathways relevant to schizophrenia and to psychotic illness. May play a role in late central nervous system development by modulating EPO expression in response to cellular oxygen level (By similarity). Forms a heterodimer that binds core DNA sequence 5'-TACGTG-3' within the hypoxia response element (HRE) leading to transcriptional repression on its target gene TH (By similarity).

**Summary**, from NCBI Gene [4861](https://www.ncbi.nlm.nih.gov/gene/4861):

> The protein encoded by this gene is a member of the basic helix-loop-helix (bHLH)-PAS family of transcription factors. Studies of a related mouse gene suggest that it functions in neurons. The exact function of this gene is unclear, but it may play protective or modulatory roles during late embryogenesis and postnatal development. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7894](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7894) · Entrez [4861](https://www.ncbi.nlm.nih.gov/gene/4861) · UniProt [Q99742](https://www.uniprot.org/uniprotkb/Q99742) · Ensembl [ENSG00000130751](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130751)

## Data

Gene col 5116: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5116); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5116, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5116]; `tensor/DDL_lfc|DDL_z.npy` [5116]; `embed/gene_vectors.npy` [5116]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5116 or target_col == 5116). Every well: [[NPAS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPAS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
