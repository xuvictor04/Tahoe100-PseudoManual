---
symbol: "RFLNA"
type: "gene"
col: 10968
ensembl_id: "ENSG00000178882"
name: "refilin A"
location: "12q24.31"
module: 232
arm: "+"
pooled_cpm: 96.42
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/232"]
generated_by: "tahoemap"
---

# RFLNA

*refilin A* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.33× (z +22.0, q 0e+00, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.63× (z +12.8, q 6e-35, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.741× (z -7.8, q 4e-12, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM199X]] (+0.51, fdr 5e-05), [[FOXO4]] (+0.51, fdr 3e-05), [[WDTC1]] (+0.50, fdr 3e-05); moves opposite to [[LINC01169]] (-0.53, fdr 5e-05), [[FAAP24]] (-0.51, fdr 6e-05), [[LARS2]] (-0.49, fdr 7e-05).
> It is in [[Module 232]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10968.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.33×** | +22.0 | 0e+00 | 47/49 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.25×** | +20.3 | 0e+00 | 41/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +12.8 | 6e-35 | 42/48 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +11.3 | 3e-27 | 39/45 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +10.6 | 5e-24 | 38/48 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +8.9 | 4e-17 | 37/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +8.0 | 7e-14 | 37/48 (C32, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +6.6 | 4e-09 | 19/49 (BT-474, NCI-H2347, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +6.3 | 2e-08 | 30/48 (C-33 A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.39×** | +6.1 | 4e-08 | 36/48 (HS-578T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +6.1 | 4e-08 | 23/48 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **1.25×** | +5.8 | 3e-07 | 24/48 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +5.7 | 4e-07 | 25/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.34×** | +5.5 | 2e-06 | 27/47 (H4, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 1.15× | +5.1 | 1e-05 | 18/48 (HOP62, HCT15, …) | inconsistent across doses | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.20× | +4.7 | 9e-05 | 20/49 (HOP62, SW 900, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.24×** | +4.1 | 0.002 | 22/48 (SHP-77, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.16× | +3.8 | 0.004 | 10/47 (A-427, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.005 | 20/49 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.006 | 14/48 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.14× | +3.5 | 0.013 | 10/48 (A-427, BT-474, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10968.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.741×** | -7.8 | 4e-12 | 36/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.771×** | -6.4 | 4e-08 | 30/48 (SW480, KATO III, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.822×** | -5.1 | 6e-05 | 24/48 (KATO III, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.671×** | -4.4 | 0.001 | 24/45 (SNU-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.815×** | -3.8 | 0.016 | 17/49 (HT-29, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10968. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 103 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +17.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.00× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 47.6 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +14.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.80× (z +10.2) | — |
| [[SW480 (line)]] | alt | 138 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +18.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 74.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +12.2) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 148 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +11.5) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.514× (z -9.1) |
| [[LoVo (line)]] | wt | 197 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.21× (z +12.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 89.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.02× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 101 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +16.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 87.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +13.8) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 65.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +14.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 1.95× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 95.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +18.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 79.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +13.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 112 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +11.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 83.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +12.5) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 136 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 58.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +10.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 60.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +13.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 158 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.93× (z +9.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 92.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +11.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 68.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +12.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 61.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +14.1) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 51.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 151 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.05× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 143 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.97× (z +10.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.265× (z -9.8) ⚠ cell-cycle shift, explains ~22% of this change |
| [[AsPC-1 (line)]] | alt | 82.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.38× (z +9.1) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 74.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +10.9) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 74.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 144 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.0) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[Hs 766T (line)]] | wt | 51.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.481× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 150 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.94× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 32.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 120 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H596 (line)]] | alt | 95.8 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.112× (z -10.8) |
| [[RKO (line)]] | wt | 91.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +12.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 82.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.29× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 85.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 214 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 96.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 91.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 123 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10968), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM199X]] | +0.51 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[FOXO4]] | +0.51 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[WDTC1]] | +0.50 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[RMND5A]] | +0.50 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[ZNF664]] | +0.50 | +0.53 / +0.42 | both halves | 4e-05 | STRING 543; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SUN1]] | +0.48 | +0.36 / +0.50 | both halves | 9e-05 |  |
| [[SLC25A23]] | +0.47 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[PLCD3]] | +0.46 | +0.39 / +0.43 | both halves | 5e-05 |  |
| [[CACUL1]] | +0.46 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[GET4]] | +0.46 | +0.35 / +0.46 | both halves | 1e-04 |  |
| [[ZDHHC2]] | +0.45 | +0.34 / +0.49 | both halves | 1e-04 |  |
| [[CTDSP2]] | +0.45 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[RNF187]] | +0.45 | +0.35 / +0.42 | both halves | 1e-04 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01169]] | -0.53 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[FAAP24]] | -0.51 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[LARS2]] | -0.49 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[PSMB5]] | -0.46 | -0.44 / -0.43 | both halves | 4e-05 |  |
| [[COX10]] | -0.46 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[AASDH]] | -0.45 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[TTC4]] | -0.45 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[C12orf43]] | -0.45 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[SPATS2]] | -0.45 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[METTL16]] | -0.44 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[LINC02985]] | -0.44 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[NR2C2AP]] | -0.43 | -0.26 / -0.54 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises RFLNA's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 232]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (4.5, -49.6); signed map (-17.2, 9.1). **Vector** length 99.9, 25.8% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +8.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +22.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.8 | +6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +3.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +2.5 | +0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +2.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -6.6 | -7.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.2 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.2 | -5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | -6.0 | -6.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.5 | -4.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.7 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | +3.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.0 | -0.9 |
|  | [[Thymol (drug)]] 5 µM |  | -1.9 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | refilin A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:123,973,241-124,316,024 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ44614, Cfm2, RefilinA; previously FAM101A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZTI6](https://www.uniprot.org/uniprotkb/Q6ZTI6) (Refilin-A):

> Involved in the regulation of the perinuclear actin network and nuclear shape through interaction with filamins. Plays an essential role in actin cytoskeleton formation in developing cartilaginous cells.

**Summary**, from NCBI Gene [144347](https://www.ncbi.nlm.nih.gov/gene/144347):

> Predicted to enable filamin binding activity. Predicted to be involved in several processes, including actin filament bundle organization; negative regulation of bone mineralization involved in bone maturation; and negative regulation of chondrocyte development. Predicted to be located in cytoskeleton. Predicted to be active in actin filament bundle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27051](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27051) · Entrez [144347](https://www.ncbi.nlm.nih.gov/gene/144347) · UniProt [Q6ZTI6](https://www.uniprot.org/uniprotkb/Q6ZTI6) · Ensembl [ENSG00000178882](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178882)

## Data

Gene col 10968: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10968); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10968, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10968]; `tensor/DDL_lfc|DDL_z.npy` [10968]; `embed/gene_vectors.npy` [10968]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10968 or target_col == 10968). Every well: [[RFLNA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFLNA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
