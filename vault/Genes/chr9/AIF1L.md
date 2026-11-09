---
symbol: "AIF1L"
type: "gene"
col: 4776
ensembl_id: "ENSG00000126878"
name: "allograft inflammatory factor 1 like"
location: "9q34.12-q34.13"
module: 176
arm: "+"
pooled_cpm: 6.04
n_lines_expressing: 38
n_dd_up: 15
n_dd_down: 14
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 5
direction_downstream: 8
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# AIF1L

*allograft inflammatory factor 1 like* — 9q34.12-q34.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.60× (z +18.9, q 0e+00, up in 16 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.86× (z +15.5, q 0e+00, up in 30 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.545× (z -12.7, q 5e-34, down in 20 of 29 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PODXL2]] (+0.78, fdr 7e-06), [[SEPTIN3]] (+0.74, fdr 7e-06), [[GNAZ]] (+0.69, fdr 7e-06); moves opposite to [[ZBED5]] (-0.67, fdr 2e-05), [[DNAI4]] (-0.64, fdr 4e-05), [[CCAR1]] (-0.63, fdr 6e-05).
> It is in [[Module 176]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CELSR2]] → it (grade B ⚠); 8 go from it, the strongest it → [[PARD6G]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4776.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.60×** | +18.9 | 0e+00 | 16/18 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.51×** | +17.1 | 0e+00 | 5/6 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.86×** | +15.5 | 0e+00 | 30/36 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.74×** | +14.9 | 0e+00 | 31/33 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.58×** | +12.9 | 4e-36 | 8/11 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +12.3 | 8e-33 | 22/33 (J82, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.02×** | +10.4 | 3e-23 | 21/36 (PANC-1, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +8.4 | 5e-15 | 18/36 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +6.2 | 3e-08 | 10/34 (NCI-H460, SW480, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.13×** | +5.8 | 4e-07 | 8/32 (PANC-1, Hs 766T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +5.4 | 3e-06 | 6/30 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +5.3 | 4e-06 | 10/31 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +5.1 | 2e-05 | 3/22 (HEC-1-A, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +5.0 | 2e-05 | 6/22 (NCI-H1573, Hs 766T, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.4 | 0.023 | 0/36 | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.4 | 0.028 | 2/34 (SHP-77, NCI-H1573) | top dose only | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.067 | 0/33 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4776.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.545×** | -12.7 | 5e-34 | 20/29 (RKO, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.526×** | -8.8 | 4e-16 | 19/33 (HCT15, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.588×** | -7.8 | 8e-13 | 16/32 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.594×** | -7.7 | 2e-12 | 18/27 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.620×** | -7.1 | 2e-10 | 12/32 (RKO, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.646×** | -6.5 | 1e-08 | 16/34 (C32, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.648×** | -6.4 | 1e-08 | 17/36 (NCI-H23, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.692×** | -5.5 | 4e-06 | 10/34 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.726×** | -4.7 | 1e-04 | 12/27 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.744×** | -4.4 | 7e-04 | 7/33 (SK-MEL-2, RKO, …) | two highest doses | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.744×** | -4.1 | 0.002 | 14/33 (RKO, BT-474, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -3.8 | 0.008 | 14/28 (Hs 766T, SHP-77, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.622×** | -3.7 | 0.010 | 6/32 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.775×** | -3.5 | 0.019 | 7/31 (PANC-1, BT-474, …) | two highest doses |  |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.809×** | -3.1 | 0.065 | 4/35 (SW48, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4776. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 14.7 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 5.34× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -13.3) |
| [[Hs 766T (line)]] | wt | 17.8 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.26× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -13.3) |
| [[HEC-1-A (line)]] | alt | 23.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -13.6) |
| [[NCI-H460 (line)]] | wt | 4.48 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.73× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.145× (z -9.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 2.31 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 11.4× (z +9.7) | — |
| [[SW48 (line)]] | wt | 26.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0988× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.202× (z -11.3) |
| [[BT-474 (line)]] | alt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -9.4) |
| [[C-33 A (line)]] | alt | 10.4 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.114× (z -8.5) |
| [[HCT15 (line)]] | alt | 13.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.126× (z -8.5) |
| [[LoVo (line)]] | wt | 9.56 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +10.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 6.15 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0645× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 9.96 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.146× (z -8.8) ⚠ transcription drop |
| [[RKO (line)]] | wt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -14.5) |
| [[A-172 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.778 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.781 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.751 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4776), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PODXL2]] | +0.78 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[SEPTIN3]] | +0.74 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[GNAZ]] | +0.69 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[SMARCD3]] | +0.68 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[HPSE]] | +0.68 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[GLB1L2]] | +0.67 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[CDCA7L]] | +0.66 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[WASF3]] | +0.66 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[LRRC20]] | +0.65 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[SHANK3]] | +0.65 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[LHX6]] | +0.65 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ABCA2]] | +0.64 | +0.56 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBED5]] | -0.67 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[DNAI4]] | -0.64 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[CCAR1]] | -0.63 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[LINC01004]] | -0.63 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[ATE1OSP]] | -0.62 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[ERCC6L2-AS1]] | -0.62 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[ANKRD17-DT]] | -0.62 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[ASH1L]] | -0.61 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[RFX3-DT]] | -0.61 | -0.51 / -0.27 | both halves | 3e-04 |  |
| [[RNF146]] | -0.61 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[NAIF1]] | -0.60 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[ZNF407-AS1]] | -0.60 | -0.49 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CELSR2]] | B | CELSR2 activity raises AIF1L's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 2.63× lower at baseline in the lines without CELSR2 | 0.020 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |
| [[SEPTIN3]] | B | SEPTIN3 activity raises AIF1L's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 1.80× lower at baseline in the lines without SEPTIN3 | 0.031 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[MCF2L]] | B | MCF2L activity weakens AIF1L's drug response | lines that do not express MCF2L (7) vs lines expressing it (29) | the lines without MCF2L respond 1.55× as strongly (z diff -1.00); strongest at Panobinostat 5 µM: 5.77x vs 2.39x (z diff -2.6) | 0.063 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2; target measured in part of the lines; artifact flags |
| [[ADGRL1]] | B | ADGRL1 activity raises AIF1L's level | lines that do not express ADGRL1 (6) vs lines expressing it (44) | 2.14× lower at baseline in the lines without ADGRL1 | 0.074 | ⚠ within organs, on part of the lines; also absent: SH3BP5, DSCC1, NDC80; maybe low, not absent |
| [[HACE1]] | C | HACE1 activity raises AIF1L's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 2.41× lower at baseline in the lines without HACE1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARD6G]] | B | AIF1L activity raises PARD6G's level | lines that do not express AIF1L (12) vs lines expressing it (38) | 2.38× lower at baseline in the lines without AIF1L | 0.013 | ⚠ within organs, on part of the lines; also absent: FAM169A, NUP210, PRR36; maybe low, not absent |
| [[CELSR2]] | B | AIF1L activity raises CELSR2's level | lines that do not express AIF1L (12) vs lines expressing it (38) | 1.69× lower at baseline in the lines without AIF1L | 0.046 | ⚠ within organs, on part of the lines; also absent: FAM169A, NUP210, PRR36; maybe low, not absent |
| [[B4GALNT4]] | B | AIF1L activity raises B4GALNT4's level | lines that do not express AIF1L (12) vs lines expressing it (38) | 2.11× lower at baseline in the lines without AIF1L | 0.057 | ⚠ within organs, on part of the lines; also absent: FAM169A, NUP210, PRR36; maybe low, not absent |
| [[PRR5]] | B | AIF1L activity raises PRR5's level | lines that do not express AIF1L (12) vs lines expressing it (38) | 1.56× lower at baseline in the lines without AIF1L | 0.074 | ⚠ within organs, on part of the lines; also absent: FAM169A, NUP210, PRR36; maybe low, not absent |
| [[PRR5-ARHGAP8]] | B | AIF1L activity raises PRR5-ARHGAP8's level | lines that do not express AIF1L (12) vs lines expressing it (38) | 1.28× lower at baseline in the lines without AIF1L | 0.082 | ⚠ within organs, on part of the lines; also absent: FAM169A, NUP210, PRR36; maybe low, not absent |
| [[ADGRL1]] | B | AIF1L activity raises ADGRL1's level | lines that do not express AIF1L (12) vs lines expressing it (38) | 1.75× lower at baseline in the lines without AIF1L | 0.082 | ⚠ within organs, on part of the lines; also absent: FAM169A, NUP210, PRR36; maybe low, not absent |
| [[KRBOX5]] | B | AIF1L activity raises KRBOX5's level | lines that do not express AIF1L (12) vs lines expressing it (38) | 1.49× lower at baseline in the lines without AIF1L | 0.089 | ⚠ within organs, on part of the lines; also absent: FAM169A, NUP210, PRR36; maybe low, not absent |
| [[PODXL2]] | B | AIF1L activity raises PODXL2's level | lines that do not express AIF1L (12) vs lines expressing it (38) | 1.77× lower at baseline in the lines without AIF1L | 0.098 | ⚠ within organs, on part of the lines; also absent: FAM169A, NUP210, PRR36; maybe low, not absent |

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.844). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (2.2, 40.7); signed map (-23.2, 33.2). **Vector** length 55.0, 8.99% of its response variance represented; |z| ≥ 3 in 795 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +18.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +17.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +12.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.7 | +15.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.6 | +14.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.9 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -7.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.5 | -8.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.7 | -12.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -7.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | +3.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | allograft inflammatory factor 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.12-q34.13 — chr9:131,096,476-131,123,152 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IBA2, FLJ12783; previously C9orf58 |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQI0](https://www.uniprot.org/uniprotkb/Q9BQI0) (Allograft inflammatory factor 1-like):

> Actin-binding protein that promotes actin bundling. May neither bind calcium nor depend on calcium for function.

**Summary**, from NCBI Gene [83543](https://www.ncbi.nlm.nih.gov/gene/83543):

> Enables actin filament binding activity. Predicted to be involved in actin filament bundle assembly and ruffle assembly. Located in actin filament and focal adhesion. Biomarker of breast cancer. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28904](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28904) · Entrez [83543](https://www.ncbi.nlm.nih.gov/gene/83543) · UniProt [Q9BQI0](https://www.uniprot.org/uniprotkb/Q9BQI0) · Ensembl [ENSG00000126878](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126878)

## Data

Gene col 4776: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4776); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4776, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4776]; `tensor/DDL_lfc|DDL_z.npy` [4776]; `embed/gene_vectors.npy` [4776]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4776 or target_col == 4776). Every well: [[AIF1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AIF1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
