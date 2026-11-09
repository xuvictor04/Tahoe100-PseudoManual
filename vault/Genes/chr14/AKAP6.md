---
symbol: "AKAP6"
type: "gene"
col: 7505
ensembl_id: "ENSG00000151320"
name: "A-kinase anchoring protein 6"
location: "14q12"
module: 9
arm: "+"
pooled_cpm: 20.21
n_lines_expressing: 38
n_dd_up: 30
n_dd_down: 14
n_dd_up_clean: 26
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# AKAP6

*A-kinase anchoring protein 6* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.44× (z +14.4, q 5e-44, up in 27 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.445× (z -9.2, q 1e-17, down in 28 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGBL4]] (+0.61, fdr 7e-06), [[SOX5]] (+0.61, fdr 1e-05), [[GRIA2]] (+0.60, fdr 1e-05); moves opposite to [[GLE1]] (-0.52, fdr 2e-05), [[TAF12]] (-0.49, fdr 2e-04), [[IKZF4]] (-0.46, fdr 3e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PTPRZ1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7505.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.44×** | +14.4 | 5e-44 | 27/36 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.63×** | +11.0 | 1e-25 | 26/35 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.45×** | +10.2 | 3e-22 | 24/35 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.37×** | +9.8 | 1e-20 | 26/35 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +9.7 | 3e-20 | 17/35 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.44×** | +9.2 | 3e-18 | 24/35 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.97×** | +7.7 | 1e-12 | 20/35 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +5.6 | 2e-06 | 7/22 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.45×** | +5.0 | 5e-05 | 13/36 (SHP-77, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.56×** | +4.9 | 7e-05 | 19/35 (NCI-H23, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +4.8 | 8e-05 | 10/31 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.23×** | +4.8 | 9e-05 | 18/36 (NCI-H2347, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.49×** | +4.5 | 3e-04 | 11/35 (LoVo, A498, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.52×** | +4.3 | 7e-04 | 13/35 (NCI-H1573, NCI-H2030, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +4.2 | 0.001 | 8/25 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.44×** | +4.2 | 0.001 | 17/35 (C32, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.44×** | +4.1 | 0.001 | 12/35 (COLO 205, NCI-H1792, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.002 | 14/36 (A-172, C32, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.003 | 13/35 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7505.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.445×** | -9.2 | 1e-17 | 28/35 (SHP-77, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.496×** | -8.0 | 3e-13 | 24/35 (COLO 205, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.523×** | -7.4 | 2e-11 | 24/34 (SHP-77, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.580×** | -6.2 | 7e-08 | 24/35 (SHP-77, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.634×** | -5.2 | 2e-05 | 20/34 (H4, C32, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.641×** | -4.9 | 9e-05 | 19/33 (HEC-1-A, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.643×** | -4.6 | 4e-04 | 16/36 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.679×** | -4.3 | 0.001 | 18/34 (Hs 766T, NCI-H2030, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.796×** | -3.7 | 0.013 | 22/35 (Hs 766T, COLO 205, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.708×** | -3.6 | 0.019 | 14/35 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.805×** | -3.5 | 0.022 | 11/36 (H4, SW480, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.758×** | -3.2 | 0.072 | 12/35 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.757×** | -3.1 | 0.094 | 8/36 (Hs 766T, SW480, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.830×** | -3.0 | 0.098 | 14/36 (SW480, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7505. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 147 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0942× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.147× (z -12.2) |
| [[C32 (line)]] | wt | 211 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -11.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -9.7) |
| [[Hs 766T (line)]] | wt | 68.5 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -19.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -10.6) |
| [[SHP-77 (line)]] | alt | 50.2 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.139× (z -13.7) |
| [[NCI-H23 (line)]] | alt | 21.8 | 0 | 4 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.108× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~73% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.147× (z -10.9) |
| [[SW480 (line)]] | alt | 15.3 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -10.1) |
| [[A-172 (line)]] | wt | 95.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -9.7) |
| [[COLO 205 (line)]] | alt | 23.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -15.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.117× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 10.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 8.03 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.27× (z +11.8) | — |
| [[SK-MEL-2 (line)]] | alt | 95.1 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -10.4) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A498 (line)]] | wt | 9.63 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.27× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0852× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 27.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.58× (z +8.5) | — |
| [[A-427 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.71 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.93 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.95 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7505), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGBL4]] | +0.61 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[SOX5]] | +0.61 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[GRIA2]] | +0.60 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[NELL2]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[PDGFD]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[MAGEA10]] | +0.57 | +0.47 / +0.38 | both halves | 6e-05 |  |
| [[DGKB]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[KCNH7]] | +0.56 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[ADGRL3]] | +0.55 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[LINC01205]] | +0.55 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[TMEM108]] | +0.55 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[ATRNL1]] | +0.55 | +0.45 / +0.64 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLE1]] | -0.52 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[TAF12]] | -0.49 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[IKZF4]] | -0.46 | -0.29 / -0.43 | both halves | 3e-04 |  |
| [[USP20]] | -0.46 | -0.39 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRZ1]] | B | PTPRZ1 activity raises AKAP6's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 2.54× lower at baseline in the lines without PTPRZ1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[MAP2K1]] | B | MAP2K1 activity lowers AKAP6's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[AGBL4]] | B | AGBL4 activity raises AKAP6's level | lines that do not express AGBL4 (11) vs lines expressing it (39) | 2.23× lower at baseline in the lines without AGBL4 | 0.090 | ⚠ within organs, on part of the lines; also absent: RBFOX1, ENSG00000248347; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.3, 35.2); signed map (42.6, 36.1). **Vector** length 68.4, 13.5% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.2 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.0 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.7 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +14.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +4.9 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.3 | -3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -1.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -0.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -0.1 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.5 | -0.9 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | A-kinase anchoring protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:32,329,298-32,837,684 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0311, mAKAP, AKAP100, PRKA6, ADAP6 |
| Gene groups (HGNC) | A-kinase anchoring proteins; Spectrin repeat containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13023](https://www.uniprot.org/uniprotkb/Q13023) (A-kinase anchor protein 6):

> Binds to type II regulatory subunits of protein kinase A and anchors/targets them to the nuclear membrane or sarcoplasmic reticulum. May act as an adapter for assembling multiprotein complexes.

**Summary**, from NCBI Gene [9472](https://www.ncbi.nlm.nih.gov/gene/9472):

> The A-kinase anchor proteins (AKAPs) are a group of structurally diverse proteins, which have the common function of binding to the regulatory subunit of protein kinase A (PKA) and confining the holoenzyme to discrete locations within the cell. This gene encodes a member of the AKAP family. The encoded protein is highly expressed in various brain regions and cardiac and skeletal muscle. It is specifically localized to the sarcoplasmic reticulum and nuclear membrane, and is involved in anchoring …

**Accessions** — [HGNC:376](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:376) · Entrez [9472](https://www.ncbi.nlm.nih.gov/gene/9472) · UniProt [Q13023](https://www.uniprot.org/uniprotkb/Q13023) · Ensembl [ENSG00000151320](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151320)

## Data

Gene col 7505: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7505); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7505, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7505]; `tensor/DDL_lfc|DDL_z.npy` [7505]; `embed/gene_vectors.npy` [7505]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7505 or target_col == 7505). Every well: [[AKAP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKAP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
