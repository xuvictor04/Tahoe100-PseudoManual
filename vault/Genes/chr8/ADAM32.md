---
symbol: "ADAM32"
type: "gene"
col: 12352
ensembl_id: "ENSG00000197140"
name: "ADAM metallopeptidase domain 32"
location: "8p11.22"
module: 39
arm: "+"
pooled_cpm: 45.31
n_lines_expressing: 48
n_dd_up: 44
n_dd_down: 10
n_dd_up_clean: 37
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# ADAM32

*ADAM metallopeptidase domain 32* — 8p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.47× (z +17.6, q 0e+00, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.581× (z -7.6, q 2e-11, down in 28 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 0.784× (z -4.8, q 2e-04, down in 22 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALDH8A1]] (+0.79, fdr 7e-06), [[LINC01031]] (+0.78, fdr 7e-06), [[SLC22A14]] (+0.71, fdr 7e-06); moves opposite to [[TERF1]] (-0.58, fdr 1e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SLCO1B3-SLCO1B7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12352.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.47×** | +17.6 | 0e+00 | 38/45 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.37×** | +11.8 | 6e-30 | 41/45 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.10×** | +10.2 | 3e-22 | 31/46 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +9.3 | 1e-18 | 42/46 (A549, LS 180, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.23×** | +8.4 | 4e-15 | 33/47 (NCI-H23, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.83×** | +8.3 | 1e-14 | 30/46 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.67×** | +7.0 | 2e-10 | 29/46 (A549, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +6.9 | 4e-10 | 26/46 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +6.0 | 1e-07 | 26/46 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +6.0 | 1e-07 | 30/45 (LoVo, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +5.9 | 2e-07 | 25/45 (C-33 A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.9 | 2e-07 | 25/46 (HS-578T, Hs 766T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +5.7 | 6e-07 | 17/38 (LoVo, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.15×** | +5.5 | 2e-06 | 27/45 (HOP62, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +5.4 | 2e-06 | 30/47 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.50×** | +5.3 | 4e-06 | 26/45 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +5.2 | 7e-06 | 23/46 (SNU-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12352.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.581×** | -7.6 | 2e-11 | 28/42 (HEC-1-A, KATO III, …) | two highest doses | cell-cycle shift (explains ~11% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.619×** | -6.4 | 3e-08 | 26/43 (KATO III, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.692×** | -5.0 | 1e-04 | 21/36 (NCI-H1573, KATO III, …) | two highest doses | cell-cycle shift (explains ~14% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | **0.784×** | -4.8 | 2e-04 | 22/46 (HEC-1-A, AsPC-1, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.550×** | -4.4 | 0.001 | 24/47 (LOX-IMVI, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.761×** | -3.9 | 0.011 | 21/44 (KATO III, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.775×** | -3.6 | 0.026 | 20/46 (HEC-1-A, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.626×** | -3.4 | 0.045 | 10/45 (AsPC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.788×** | -3.4 | 0.045 | 17/45 (LOX-IMVI, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Bexarotene (drug)]] 5 µM |  | **0.788×** | -3.4 | 0.045 | 13/46 (LOX-IMVI, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12352. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 59.5 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +20.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 113 | 0 | 9 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.101× (z -18.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.325× (z -9.6) |
| [[LoVo (line)]] | wt | 23.8 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +14.1) | — |
| [[HEC-1-A (line)]] | alt | 142 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.353× (z -11.6) |
| [[A498 (line)]] | wt | 27.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +14.5) | — |
| [[C-33 A (line)]] | alt | 68.6 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -9.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 18.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +17.4) | — |
| [[NCI-H23 (line)]] | alt | 35.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.18× (z +19.5) | [[Docetaxel (drug)]] 0.05 µM 0.253× (z -9.1) ⚠ transcription drop |
| [[PANC-1 (line)]] | alt | 25.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +21.4) | — |
| [[HCT15 (line)]] | alt | 64.6 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.195× (z -10.7) ⚠ toxic · without an alert: [[Isocorydine (drug)]] 0.5 µM 0.285× (z -8.6) |
| [[LS 180 (line)]] | wt | 26.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +15.0) | — |
| [[NCI-H1573 (line)]] | alt | 156 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0642× (z -23.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 88.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -15.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 77.4 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.87× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.214× (z -11.8) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 39.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.166× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 109 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -13.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 105 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 48.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +14.8) | — |
| [[NCI-H460 (line)]] | wt | 27.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.25× (z +13.0) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 23.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +10.9) | — |
| [[SW480 (line)]] | alt | 24.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 43.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 48.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 37.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 58.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +11.0) | — |
| [[HT-29 (line)]] | alt | 19.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.96× (z +10.1) | — |
| [[J82 (line)]] | alt | 70.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 28.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.51× (z +10.4) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 20.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.50× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 15.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +10.0) | — |
| [[A-427 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.39 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.91 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12352), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH8A1]] | +0.79 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[LINC01031]] | +0.78 | +0.76 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[SLC22A14]] | +0.71 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[TMEM236]] | +0.70 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.69 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[RAPSN]] | +0.68 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[FRZB]] | +0.68 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[IMPA1P1]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[CMYA5]] | +0.66 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[PHEX]] | +0.66 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[SCUBE2]] | +0.66 | +0.61 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERF1]] | -0.58 | -0.52 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLCO1B3-SLCO1B7]] | B | SLCO1B3-SLCO1B7 activity raises ADAM32's level | lines that do not express SLCO1B3-SLCO1B7 (27) vs lines expressing it (23) | 1.53× lower at baseline in the lines without SLCO1B3-SLCO1B7 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000257062, SLCO1B3, SLCO1B1 |
| [[LMO7DN]] | B | LMO7DN activity raises ADAM32's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.50× lower at baseline in the lines without LMO7DN | 0.056 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[SH2D4B]] | C | SH2D4B activity raises ADAM32's level | lines that do not express SH2D4B (3) vs lines expressing it (47) | 2.06× lower at baseline in the lines without SH2D4B | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000249951, ARHGAP15, B4GALT1; maybe low, not absent; its own permutation p |
| [[TRIM72]] | C | TRIM72 activity raises ADAM32's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 2.42× lower at baseline in the lines without TRIM72 | 0.080 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |
| [[LINC02133]] | C | LINC02133 activity raises ADAM32's level | lines that do not express LINC02133 (4) vs lines expressing it (46) | 2.96× lower at baseline in the lines without LINC02133 | 0.087 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LYG1, RBM44, TRIM72; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.7, -12.7); signed map (17.6, 7.4). **Vector** length 122, 35.5% of its response variance represented; |z| ≥ 3 in 1,316 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.6 | +10.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +9.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.8 | +4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +5.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +5.7 | +4.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.9 | +5.3 |
| fall | [[NG25 (drug)]] 5 µM |  | -4.0 | -3.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.7 | -2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.6 | -3.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.5 | -3.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.3 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.3 | -4.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -3.1 | -4.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase domain 32 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.22 — chr8:39,106,990-39,284,917 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ADAM metallopeptidase domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TC27](https://www.uniprot.org/uniprotkb/Q8TC27) (Disintegrin and metalloproteinase domain-containing protein 32):

> May play a role in sperm development and fertilization This is a non-catalytic metalloprotease-like protein.

**Summary**, from NCBI Gene [203102](https://www.ncbi.nlm.nih.gov/gene/203102):

> This gene encodes a member of the disintegrin family of membrane-anchored proteins that play a role in diverse biological processes such as brain development, fertilization, tumor development and inflammation. This gene is predominantly expressed in the testis. The encoded protein undergoes proteolytic processing to generate a mature polypeptide comprised of an metalloprotease, disintegrin and epidermal growth factor-like domains. This gene is located in a cluster of other disintegrin and …

**Accessions** — [HGNC:15479](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15479) · Entrez [203102](https://www.ncbi.nlm.nih.gov/gene/203102) · UniProt [Q8TC27](https://www.uniprot.org/uniprotkb/Q8TC27) · Ensembl [ENSG00000197140](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197140)

## Data

Gene col 12352: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12352); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12352, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12352]; `tensor/DDL_lfc|DDL_z.npy` [12352]; `embed/gene_vectors.npy` [12352]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12352 or target_col == 12352). Every well: [[ADAM32 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAM32.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
