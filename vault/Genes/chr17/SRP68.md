---
symbol: "SRP68"
type: "gene"
col: 9554
ensembl_id: "ENSG00000167881"
name: "signal recognition particle 68"
location: "17q25.1"
module: 7
arm: "+"
pooled_cpm: 57.84
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# SRP68

*signal recognition particle 68* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.89× (z +17.5, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.824× (z -5.4, q 5e-05, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PABIR1]] (+0.71, fdr 7e-06), [[SF3A1]] (+0.69, fdr 7e-06), [[PES1]] (+0.68, fdr 7e-06); moves opposite to [[PALS2]] (-0.57, fdr 1e-05), [[MEMO1]] (-0.55, fdr 1e-04), [[ATP1B3]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9554.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +17.5 | 0e+00 | 45/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.12×** | +16.7 | 0e+00 | 47/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.11×** | +14.5 | 1e-45 | 42/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.91×** | +12.2 | 6e-32 | 43/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.92×** | +10.9 | 8e-26 | 41/48 (A-172, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.74×** | +10.7 | 6e-25 | 44/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +8.1 | 3e-14 | 38/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +7.8 | 4e-13 | 0/49 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +6.3 | 2e-08 | 35/48 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +5.4 | 5e-06 | 29/48 (SW48, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +5.3 | 6e-06 | 31/47 (RPMI-7951, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +5.3 | 6e-06 | 28/48 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +5.2 | 7e-06 | 30/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.29×** | +5.0 | 2e-05 | 23/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +5.0 | 2e-05 | 29/48 (PANC-1, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +4.6 | 1e-04 | 24/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.036 | 15/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.042 | 8/48 (SW480, NCI-H2030, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9554.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.824×** | -5.4 | 5e-05 | 28/48 (H4, CHP-212, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.777×** | -4.9 | 2e-04 | 29/48 (NCI-H460, CHP-212, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.781×** | -4.8 | 2e-04 | 24/48 (SW1417, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.840× | -4.8 | 2e-04 | 21/48 (A498, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.795×** | -4.5 | 8e-04 | 28/48 (H4, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.813×** | -4.1 | 0.005 | 26/49 (LS 180, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.829×** | -3.5 | 0.032 | 20/41 (SW48, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9554. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 75.2 | 7 | 0 | [[TAK-901 (drug)]] 5 µM 6.57× (z +13.3) | — |
| [[HOP62 (line)]] | alt | 61.7 | 5 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.84× (z +12.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 54.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +13.7) | — |
| [[PANC-1 (line)]] | alt | 53.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +22.6) | — |
| [[COLO 205 (line)]] | alt | 71.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 56.3 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 7.61× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 49.5 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.45× (z +16.8) | — |
| [[LS 180 (line)]] | wt | 57.6 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.88× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 48.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +15.6) | — |
| [[A-172 (line)]] | wt | 58.7 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.23× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.427× (z -9.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 65.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.4) | — |
| [[A549 (line)]] | wt | 66.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +14.7) | — |
| [[HEC-1-A (line)]] | alt | 79.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 36.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +11.9) | — |
| [[LOX-IMVI (line)]] | wt | 43.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +11.1) | — |
| [[NCI-H23 (line)]] | alt | 59.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.378× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 55.9 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 7.57× (z +10.2) | — |
| [[SW48 (line)]] | wt | 70.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.91× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.118× (z -16.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 51.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.3) | — |
| [[Panc 03.27 (line)]] | alt | 64.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +11.0) | — |
| [[RPMI-7951 (line)]] | alt | 44.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.195× (z -13.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 59.7 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.27× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.395× (z -8.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 46.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.77× (z +8.8) | — |
| [[H4 (line)]] | wt | 72.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 52.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 49.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.1) | — |
| [[hTERT-HPNE (line)]] | wt | 54.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.53× (z +8.9) | — |
| [[KATO III (line)]] | alt | 84.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 49.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.9) | — |
| [[SNU-1 (line)]] | wt | 53.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 57.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +11.9) | — |
| [[SW1417 (line)]] | alt | 57.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.414× (z -8.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 67.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9554), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PABIR1]] | +0.71 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[SF3A1]] | +0.69 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[PES1]] | +0.68 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[ABCF3]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[RNF40]] | +0.67 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[ZNF543]] | +0.67 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[ACTR8]] | +0.66 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[ERAL1]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ZNF548]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[RBM18]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[VPS72]] | +0.65 | +0.47 / +0.74 | both halves | 2e-05 |  |
| [[ZNF414]] | +0.63 | +0.60 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PALS2]] | -0.57 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[MEMO1]] | -0.55 | -0.74 / -0.33 | both halves | 1e-04 |  |
| [[ATP1B3]] | -0.54 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[TRIM33]] | -0.54 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[AGAP3]] | -0.54 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.54 | -0.44 / -0.61 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises SRP68's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises SRP68's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-33.5, -2.6); signed map (-2.8, -32.0). **Vector** length 92.5, 23.2% of its response variance represented; |z| ≥ 3 in 1,158 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.7 | +10.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +14.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +5.6 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +10.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | -0.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.2 | -4.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | -3.9 | +4.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.6 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | +4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | +1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | +0.4 |
|  | [[Auranofin (drug)]] 0.5 µM |  | -1.7 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | signal recognition particle 68 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:76,038,775-76,072,517 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Signal recognition particle |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHB9](https://www.uniprot.org/uniprotkb/Q9UHB9) (Signal recognition particle subunit SRP68):

> Component of the signal recognition particle (SRP) complex, a ribonucleoprotein complex that mediates the cotranslational targeting of secretory and membrane proteins to the endoplasmic reticulum (ER). The SRP complex interacts with the signal sequence in nascent secretory and membrane proteins and directs them to the membrane of the ER. The SRP complex targets the ribosome-nascent chain complex to the SRP receptor (SR), which is anchored in the ER, where SR compaction and GTPase rearrangement …

**Summary**, from NCBI Gene [6730](https://www.ncbi.nlm.nih.gov/gene/6730):

> This gene encodes a subunit of the signal recognition particle (SRP). The SRP is a ribonucleoprotein complex that transports secreted and membrane proteins to the endoplasmic reticulum for processing. The complex includes a 7S RNA and six protein subunits. The encoded protein is the 68kDa component of the SRP, and forms a heterodimer with the 72kDa subunit that is required for SRP function. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene, …

**Accessions** — [HGNC:11302](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11302) · Entrez [6730](https://www.ncbi.nlm.nih.gov/gene/6730) · UniProt [Q9UHB9](https://www.uniprot.org/uniprotkb/Q9UHB9) · Ensembl [ENSG00000167881](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167881)

## Data

Gene col 9554: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9554); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9554, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9554]; `tensor/DDL_lfc|DDL_z.npy` [9554]; `embed/gene_vectors.npy` [9554]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9554 or target_col == 9554). Every well: [[SRP68 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRP68.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
