---
symbol: "KLHL13"
type: "gene"
col: 28
ensembl_id: "ENSG00000003096"
name: "kelch like family member 13"
location: "Xq24"
module: 9
arm: "+"
pooled_cpm: 14.29
n_lines_expressing: 27
n_dd_up: 17
n_dd_down: 11
n_dd_up_clean: 14
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 11
direction_downstream: 13
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# KLHL13

*kelch like family member 13* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.49× (z +19.3, q 0e+00, up in 18 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.609× (z -7.4, q 6e-11, down in 15 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERBB4]] (+0.66, fdr 7e-06), [[SNCA]] (+0.62, fdr 1e-05), [[LINC00937]] (+0.62, fdr 1e-05); moves opposite to [[ERVK13-1]] (-0.51, fdr 4e-04), [[RABL2B]] (-0.48, fdr 3e-04), [[RABL2A]] (-0.47, fdr 5e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[SNCA]] → it (grade B ⚠); 13 go from it, the strongest it → [[NRXN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 28.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.49×** | +19.3 | 0e+00 | 18/24 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.90×** | +13.6 | 8e-40 | 10/23 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.06×** | +10.9 | 4e-25 | 16/24 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +7.5 | 1e-11 | 13/24 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +7.4 | 2e-11 | 9/24 (SHP-77, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +7.2 | 6e-11 | 2/15 (BT-474, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +5.1 | 3e-05 | 3/22 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.23×** | +4.2 | 0.002 | 8/24 (LoVo, NCI-H1792, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +3.8 | 0.008 | 6/25 (SHP-77, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | 1.19× | +3.6 | 0.018 | 8/24 (SW 900, A549, …) | top dose only | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.025 | 5/24 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.036 | 2/24 (MIA PaCa-2, NCI-H460) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.3 | 0.042 | 0/25 | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.2 | 0.051 | 3/19 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.053 | 3/24 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.053 | 3/24 (A498, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.057 | 5/23 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.058 | 8/24 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.079 | 9/24 (BT-474, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.085 | 0/24 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 28.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.609×** | -7.4 | 6e-11 | 15/24 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.618×** | -7.2 | 1e-10 | 19/24 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.650×** | -6.5 | 2e-08 | 16/24 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.678×** | -5.8 | 7e-07 | 14/24 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **0.746×** | -4.4 | 0.001 | 6/24 (SK-MEL-2, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.774×** | -3.9 | 0.011 | 4/24 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.777×** | -3.8 | 0.012 | 6/24 (H4, SHP-77, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.788×** | -3.6 | 0.024 | 2/24 (CHP-212, LS 180) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.787×** | -3.5 | 0.034 | 7/24 (NCI-H23, LoVo, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.799×** | -3.2 | 0.067 | 5/24 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.860× | -3.2 | 0.070 | 4/24 (SHP-77, H4, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.673×** | -3.1 | 0.087 | 7/25 (C-33 A, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 28. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 715 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0590× (z -26.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.134× (z -13.2) |
| [[LoVo (line)]] | wt | 25.6 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.243× (z -11.2) |
| [[A-427 (line)]] | wt | 21.3 | 0 | 6 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0852× (z -16.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.184× (z -11.5) |
| [[AN3 CA (line)]] | alt | 94.0 | 0 | 6 (3 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0586× (z -14.8) |
| [[LS 180 (line)]] | wt | 53.3 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -17.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.360× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 21.3 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.129× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 10.9 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 4.67× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.216× (z -8.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 8.75 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 35.7× (z +11.1) | — |
| [[A498 (line)]] | wt | 36.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.320× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 9.78 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0693× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.0666× (z -10.7) |
| [[PANC-1 (line)]] | alt | 11.9 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.34× (z +11.4) | — |
| [[C-33 A (line)]] | alt | 47.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 20.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -15.4) |
| [[SK-MEL-2 (line)]] | alt | 54.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0923× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.47 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 28), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERBB4]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[SNCA]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[LINC00937]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[ZFHX4]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[FUT9]] | +0.60 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[FAM184A]] | +0.59 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[MMRN1]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[NCAM2]] | +0.59 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[EPHA5]] | +0.59 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[CTNNA2]] | +0.58 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[SLC5A4-AS1]] | +0.58 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[VAV3]] | +0.57 | +0.46 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERVK13-1]] | -0.51 | -0.25 / -0.49 | both halves | 4e-04 |  |
| [[RABL2B]] | -0.48 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[RABL2A]] | -0.47 | -0.24 / -0.50 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 3, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNCA]] | B | SNCA activity raises KLHL13's level | lines that do not express SNCA (29) vs lines expressing it (21) | 2.39× lower at baseline in the lines without SNCA | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CNKSR2, CDH10 |
| [[BRINP3]] | B | BRINP3 activity raises KLHL13's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 2.35× lower at baseline in the lines without BRINP3 | 0.038 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent |
| [[NRXN3]] | B | NRXN3 activity raises KLHL13's level | lines that do not express NRXN3 (23) vs lines expressing it (27) | 1.46× lower at baseline in the lines without NRXN3 | 0.044 | ⚠ within organs, on part of the lines; also absent: RGS7, FGF13, ENSG00000255983 |
| [[IQGAP2]] | C | IQGAP2 activity raises KLHL13's level | lines that do not express IQGAP2 (25) vs lines expressing it (25) | 2.88× lower at baseline in the lines without IQGAP2 | 0.001 | ⚠ within organs, on part of the lines; also absent: KLHL13, KCNQ2, CHD5; maybe low, not absent; co-absent with the target |
| [[FAM110B]] | C | FAM110B activity raises KLHL13's level | lines that do not express FAM110B (27) vs lines expressing it (23) | 2.16× lower at baseline in the lines without FAM110B | 0.044 | ⚠ within organs, on part of the lines; also absent: LRRK2, PIEZO2, GFRA1; co-absent with the target |
| [[ANO5]] | C | ANO5 activity raises KLHL13's level | lines that do not express ANO5 (25) vs lines expressing it (25) | 2.09× lower at baseline in the lines without ANO5 | 0.049 | ⚠ within organs, on part of the lines; also absent: CNKSR2, SLC6A15, CNTN1; maybe low, not absent; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises KLHL13's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 3.44× lower at baseline in the lines without KCNH7 | 0.078 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[SLITRK6]] | C | SLITRK6 activity raises KLHL13's level | lines that do not express SLITRK6 (28) vs lines expressing it (22) | 2.25× lower at baseline in the lines without SLITRK6 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4; co-absent with the target |
| [[LINC02864]] | C | LINC02864 activity raises KLHL13's level | lines that do not express LINC02864 (36) vs lines expressing it (14) | 1.72× lower at baseline in the lines without LINC02864 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC00824, LINC01205; co-absent with the target |
| [[KSR2]] | C | KSR2 activity raises KLHL13's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 2.25× lower at baseline in the lines without KSR2 | 0.089 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent; co-absent with the target |
| [[LRRN2]] | C | LRRN2 activity raises KLHL13's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 2.00× lower at baseline in the lines without LRRN2 | 0.093 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 5, C 8. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRXN3]] | B | KLHL13 activity raises NRXN3's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 2.45× lower at baseline in the lines without KLHL13 | 0.013 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4 |
| [[PTPN4]] | B | KLHL13 activity raises PTPN4's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 1.53× lower at baseline in the lines without KLHL13 | 0.027 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4 |
| [[MID1]] | B | KLHL13 activity strengthens MID1's drug response | lines that do not express KLHL13 (19) vs lines expressing it (25) | the lines without KLHL13 respond 0.62× as strongly (z diff +1.34); strongest at Trametinib 5 µM: 1.21x vs 1.63x (z diff +2.4) | 0.059 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4; target measured in part of the lines; artifact flags |
| [[AUTS2]] | B | KLHL13 activity raises AUTS2's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 2.47× lower at baseline in the lines without KLHL13 | 0.083 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4 |
| [[PPM1H]] | B | KLHL13 activity raises PPM1H's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 1.15× lower at baseline in the lines without KLHL13 | 0.089 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4 |
| [[IQGAP2]] | C | KLHL13 activity raises IQGAP2's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 2.04× lower at baseline in the lines without KLHL13 | 0.010 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4; co-absent with the target |
| [[FAM110B]] | C | KLHL13 activity raises FAM110B's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 2.21× lower at baseline in the lines without KLHL13 | 0.039 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4; co-absent with the target |
| [[LGSN]] | C | KLHL13 activity raises LGSN's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 2.62× lower at baseline in the lines without KLHL13 | 0.050 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4; co-absent with the target |
| [[SLITRK6]] | C | KLHL13 activity raises SLITRK6's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 2.18× lower at baseline in the lines without KLHL13 | 0.069 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4; co-absent with the target |
| [[LONRF2]] | C | KLHL13 activity raises LONRF2's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 2.43× lower at baseline in the lines without KLHL13 | 0.078 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4; co-absent with the target |
| [[VAV3]] | C | KLHL13 activity raises VAV3's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 2.56× lower at baseline in the lines without KLHL13 | 0.084 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4; co-absent with the target |
| [[WIPF3]] | C | KLHL13 activity raises WIPF3's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 1.85× lower at baseline in the lines without KLHL13 | 0.090 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.8, 34.3); signed map (39.3, 36.2). **Vector** length 61.5, 14.0% of its response variance represented; |z| ≥ 3 in 621 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +19.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.1 | +2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.8 | +2.0 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -7.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.6 | -3.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -3.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:117,897,813-118,117,340 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10262; previously BKLHD2, KIAA1309 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2N7](https://www.uniprot.org/uniprotkb/Q9P2N7) (Kelch-like protein 13):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complex required for mitotic progression and cytokinesis. The BCR(KLHL9-KLHL13) E3 ubiquitin ligase complex mediates the ubiquitination of AURKB and controls the dynamic behavior of AURKB on mitotic chromosomes and thereby coordinates faithful mitotic progression and completion of cytokinesis.

**Summary**, from NCBI Gene [90293](https://www.ncbi.nlm.nih.gov/gene/90293):

> This gene encodes a BTB and kelch domain containing protein and belongs to the kelch repeat domain containing superfamily of proteins. The encoded protein functions as an adaptor protein that complexes with Cullin 3 and other proteins to form the Cullin 3-based E3 ubiquitin-protein ligase complex. This complex is necessary for proper chromosome segregation and completion of cytokinesis. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:22931](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22931) · Entrez [90293](https://www.ncbi.nlm.nih.gov/gene/90293) · UniProt [Q9P2N7](https://www.uniprot.org/uniprotkb/Q9P2N7) · Ensembl [ENSG00000003096](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000003096)

## Data

Gene col 28: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 28); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 28, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 28]; `tensor/DDL_lfc|DDL_z.npy` [28]; `embed/gene_vectors.npy` [28]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 28 or target_col == 28). Every well: [[KLHL13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
