---
symbol: "CNPY3"
type: "gene"
col: 5976
ensembl_id: "ENSG00000137161"
name: "canopy FGF signaling regulator 3"
location: "6p21.1"
module: 50
arm: "+"
pooled_cpm: 17.64
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# CNPY3

*canopy FGF signaling regulator 3* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.42× (z +23.0, q 0e+00, up in 48 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.32× (z +3.8, q 0.009, up in 11 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 9 lines (PANC-1 1.48×, NCI-H23 1.52×, SW480 1.42×, A498 1.45×, …; ⚠ position not correctable); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 3.37×, PANC-1 2.42×, HEC-1-A 2.92×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (HEC-1-A 3.40×, PANC-1 2.53×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.475× (z -20.3, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SELENON]] (+0.73, fdr 7e-06), [[PPT1]] (+0.71, fdr 7e-06), [[NAGA]] (+0.70, fdr 7e-06); moves opposite to [[NSRP1]] (-0.70, fdr 1e-05), [[ATF4]] (-0.62, fdr 1e-05), [[ZNF503]] (-0.61, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MYL9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5976.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 9 lines (PANC-1 1.48×, NCI-H23 1.52×, SW480 1.42×, A498 1.45×, …; ⚠ position not correctable); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 3.37×, PANC-1 2.42×, HEC-1-A 2.92×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (HEC-1-A 3.40×, PANC-1 2.53×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.42×** | +23.0 | 0e+00 | 48/48 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +16.6 | 0e+00 | 35/39 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +13.8 | 5e-41 | 26/31 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +10.2 | 4e-22 | 25/36 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +6.7 | 2e-09 | 24/44 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Rimonabant (Hydrochloride) (drug)]] 0.05 µM | ⚠ unreliable plate only; position correction uncertain | **1.33×** | +5.5 | 5e-06 | 17/48 (HEC-1-A, J82, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.9 | 6e-05 | 18/48 (SNU-423, HOP62, …) | top dose only | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.8 | 0.009 | 8/26 (HS-578T, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.009 | 11/44 (HCT15, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.25× | +3.0 | 0.13 | 10/48 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5976.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.475×** | -20.3 | 0e+00 | 42/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.406×** | -17.4 | 0e+00 | 42/47 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.552×** | -11.0 | 6e-26 | 37/48 (H4, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.693×** | -7.0 | 3e-10 | 25/48 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.720×** | -6.3 | 3e-08 | 22/48 (NCI-H23, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.729×** | -6.1 | 1e-07 | 20/47 (KATO III, SNU-423, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.721×** | -6.0 | 1e-07 | 25/47 (J82, AN3 CA, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.740×** | -5.8 | 5e-07 | 21/46 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.740×** | -5.8 | 5e-07 | 20/48 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.785×** | -4.6 | 2e-04 | 18/47 (BT-474, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.786×** | -4.6 | 2e-04 | 15/47 (Hs 766T, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.795×** | -4.4 | 5e-04 | 16/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.809×** | -4.1 | 0.002 | 16/48 (HS-578T, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.696×** | -3.6 | 0.011 | 12/46 (SW480, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.875× | -3.6 | 0.011 | 13/48 (SW 1088, A-427, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.700×** | -3.6 | 0.013 | 12/47 (SK-MEL-2, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.879× | -3.5 | 0.015 | 12/48 (A-427, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5976. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 24.8 | 1 (1 ⚠) | 3 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.52× (z +10.5) ⚠ position not correctable | [[Harringtonine (drug)]] 5 µM 0.166× (z -12.6) |
| [[PANC-1 (line)]] | alt | 23.3 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -11.4) |
| [[A-427 (line)]] | wt | 24.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -15.5) |
| [[HEC-1-A (line)]] | alt | 21.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.40× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 19.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 16.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -18.1) |
| [[NCI-H460 (line)]] | wt | 11.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -13.8) |
| [[SW480 (line)]] | alt | 11.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -15.0) |
| [[H4 (line)]] | wt | 26.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0698× (z -13.1) |
| [[HS-578T (line)]] | alt | 24.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -12.2) |
| [[KATO III (line)]] | alt | 27.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.2) |
| [[LoVo (line)]] | wt | 14.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 5.01× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -11.3) |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.160× (z -8.8) |
| [[C-33 A (line)]] | alt | 19.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -10.6) |
| [[COLO 205 (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -9.0) |
| [[HCT15 (line)]] | alt | 12.1 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.122× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 14.1 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.142× (z -8.5) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -8.9) |
| [[HT-29 (line)]] | alt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -9.8) |
| [[J82 (line)]] | alt | 26.1 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.289× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 18.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -8.5) |
| [[LS 180 (line)]] | wt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 30.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.236× (z -8.5) |
| [[SNU-1 (line)]] | wt | 21.6 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0505× (z -14.3) |
| [[A-172 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5976), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENON]] | +0.73 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[PPT1]] | +0.71 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[NAGA]] | +0.70 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[FKBP9]] | +0.68 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[CRTAP]] | +0.68 | +0.79 / +0.51 | both halves | 1e-05 |  |
| [[ITM2C]] | +0.68 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[RNPEP]] | +0.67 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[AGO1]] | +0.67 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[MAN2B2]] | +0.67 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[PRDX3]] | +0.66 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[MRE11]] | +0.66 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[COPS7B]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSRP1]] | -0.70 | -0.74 / -0.56 | both halves | 1e-05 |  |
| [[ATF4]] | -0.62 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[ZNF503]] | -0.61 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[NBPF10]] | -0.61 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[CCDC174]] | -0.59 | -0.65 / -0.41 | both halves | 4e-05 |  |
| [[TRIP11]] | -0.59 | -0.70 / -0.42 | both halves | 4e-05 |  |
| [[ZKSCAN1]] | -0.58 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[ESF1]] | -0.57 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[EID2]] | -0.57 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[EIF5B]] | -0.57 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[FOXD1]] | -0.57 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[METTL23]] | -0.56 | -0.65 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYL9]] | B | MYL9 activity raises CNPY3's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.19× lower at baseline in the lines without MYL9 | 0.098 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[CRTAP]] | C | CRTAP activity raises CNPY3's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.70× lower at baseline in the lines without CRTAP | 0.042 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.759). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.3, -23.7); signed map (-27.0, -36.2). **Vector** length 63.7, 9.92% of its response variance represented; |z| ≥ 3 in 843 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +16.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +10.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +4.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.4 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.1 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.0 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -17.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -20.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.7 | -11.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -4.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | canopy FGF signaling regulator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:42,929,480-42,939,294 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAG4A; previously TNRC5 |
| Gene groups (HGNC) | Canopy FGF signaling regulators |
| Reactome | 3 pathways, smallest: Trafficking and processing of endosomal TLR; Toll-like Receptor Cascades; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BT09](https://www.uniprot.org/uniprotkb/Q9BT09) (Protein canopy homolog 3):

> Toll-like receptor (TLR)-specific co-chaperone for HSP90B1. Required for proper TLR folding, except that of TLR3, and hence controls TLR exit from the endoplasmic reticulum. Consequently, required for both innate and adaptive immune responses (By similarity).

**Summary**, from NCBI Gene [10695](https://www.ncbi.nlm.nih.gov/gene/10695):

> This gene encodes a protein that binds members of the toll-like receptor protein family and functions as a chaperone to aid in folding and export of these proteins. Alternative splicing results in multiple transcript variants. Naturally occuring readthrough transcription occurs between this locus and the downstream GNMT (glycine N-methyltransferase) gene and is represented with GeneID:107080644. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:11968](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11968) · Entrez [10695](https://www.ncbi.nlm.nih.gov/gene/10695) · UniProt [Q9BT09](https://www.uniprot.org/uniprotkb/Q9BT09) · Ensembl [ENSG00000137161](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137161)

## Data

Gene col 5976: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5976); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5976, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5976]; `tensor/DDL_lfc|DDL_z.npy` [5976]; `embed/gene_vectors.npy` [5976]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5976 or target_col == 5976). Every well: [[CNPY3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNPY3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
