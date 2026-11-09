---
symbol: "WBP2"
type: "gene"
col: 5326
ensembl_id: "ENSG00000132471"
name: "WW domain binding protein 2"
location: "17q25.1"
module: 74
arm: "+"
pooled_cpm: 45.97
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 9
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# WBP2

*WW domain binding protein 2* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.67× (z +11.1, q 1e-25, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.538× (z -9.5, q 2e-18, down in 40 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.493× (z -5.6, q 5e-06, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D17]] (+0.72, fdr 7e-06), [[GABARAPL1]] (+0.67, fdr 8e-06), [[RB1CC1]] (+0.65, fdr 1e-05); moves opposite to [[RANBP1]] (-0.63, fdr 7e-06), [[COX10-DT]] (-0.58, fdr 3e-05), [[NDC1]] (-0.58, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[IFITM10]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5326.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +11.1 | 1e-25 | 31/47 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +8.2 | 1e-13 | 40/48 (KATO III, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +8.0 | 2e-13 | 36/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.68×** | +8.0 | 3e-13 | 41/48 (HOP62, A498, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.55×** | +6.4 | 2e-08 | 35/48 (HEC-1-A, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +6.0 | 1e-07 | 33/48 (KATO III, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +5.7 | 1e-06 | 26/47 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.9 | 5e-05 | 1/49 (HOP62) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.73×** | +4.4 | 8e-04 | 23/42 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.21×** | +4.2 | 0.001 | 21/48 (KATO III, A549, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.002 | 27/48 (LoVo, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.002 | 25/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **1.30×** | +4.0 | 0.002 | 22/45 (NCI-H2030, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +4.0 | 0.002 | 23/39 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.28×** | +3.8 | 0.006 | 25/48 (KATO III, A498, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.032 | 19/48 (H4, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.032 | 16/48 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.032 | 17/48 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.15× | +3.0 | 0.068 | 9/48 (A-172, HOP62, …) | rises with dose | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.24×** | +3.0 | 0.068 | 15/47 (KATO III, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.070 | 14/47 (A-427, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5326.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.538×** | -9.5 | 2e-18 | 40/48 (NCI-H460, A498, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.493×** | -5.6 | 5e-06 | 33/48 (A498, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.500×** | -5.5 | 6e-06 | 34/48 (MIA PaCa-2, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.809×** | -4.6 | 7e-04 | 25/48 (SW480, RKO, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.628×** | -4.5 | 7e-04 | 26/48 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.584×** | -4.3 | 0.002 | 28/47 (RKO, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.601×** | -4.1 | 0.004 | 19/48 (A498, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.772×** | -3.8 | 0.010 | 23/47 (RKO, SW480, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.665×** | -3.2 | 0.073 | 18/48 (SW 900, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.817× | -3.1 | 0.12 | 14/48 (NCI-H460, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5326. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 79.5 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +15.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.440× (z -9.2) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.220× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 36.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +13.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.336× (z -10.0) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 84.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +21.8) | — |
| [[HEC-1-A (line)]] | alt | 52.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +13.1) | — |
| [[HS-578T (line)]] | alt | 42.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.336× (z -8.9) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 47.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +15.9) | — |
| [[A-427 (line)]] | wt | 37.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.96× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 44.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +13.8) | — |
| [[HepG2_C3A (line)]] | wt | 42.1 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.262× (z -9.0) |
| [[HOP62 (line)]] | alt | 47.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 44.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.73× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 59.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.3) | — |
| [[J82 (line)]] | alt | 53.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +13.9) | — |
| [[KATO III (line)]] | alt | 75.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.22× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 52.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.350× (z -9.1) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 30.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.9) | — |
| [[RKO (line)]] | wt | 50.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 93.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +16.3) | — |
| [[SW1417 (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.363× (z -8.7) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 43.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5326), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D17]] | +0.72 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[GABARAPL1]] | +0.67 | +0.57 / +0.74 | both halves | 8e-06 |  |
| [[RB1CC1]] | +0.65 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[STX4]] | +0.64 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[DNAJB2]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[SQSTM1]] | +0.62 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[UBXN1]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[NKIRAS2]] | +0.59 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[UBE2B]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[ABHD4]] | +0.57 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[SHC2]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SLC31A2]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RANBP1]] | -0.63 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[COX10-DT]] | -0.58 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[NDC1]] | -0.58 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[MYO19]] | -0.58 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[SLC25A15]] | -0.56 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[MTERF3]] | -0.55 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[DHX15]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[CDCA7]] | -0.55 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[GMPS]] | -0.54 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[FANCC]] | -0.54 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[SYNCRIP]] | -0.54 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[DSCC1]] | -0.53 | -0.58 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFITM10]] | C | IFITM10 activity raises WBP2's level | lines that do not express IFITM10 (4) vs lines expressing it (46) | 1.61× lower at baseline in the lines without IFITM10 | 0.055 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CTSD, FLVCR2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.681). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.4, -46.4); signed map (-12.5, 11.3). **Vector** length 125, 35.5% of its response variance represented; |z| ≥ 3 in 852 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.7 | +6.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.9 | +8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +11.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.4 | +8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +8.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +4.2 | +4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.5 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.3 | +3.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.6 | -9.5 |
|  | [[EX229 (drug)]] 5 µM |  | -6.4 | -5.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.7 | -5.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.7 | -4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.7 | -4.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.3 | -3.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.2 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | WW domain binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,845,699-75,856,507 (-) |
| Ensembl biotype | protein_coding |
| Also known as | WBP-2, GRAMD6 |
| Gene groups (HGNC) | GRAM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969T9](https://www.uniprot.org/uniprotkb/Q969T9) (WW domain-binding protein 2):

> Acts as a transcriptional coactivator of estrogen and progesterone receptors (ESR1 and PGR) upon hormone activation. In presence of estrogen, binds to ESR1-responsive promoters. Synergizes with YAP1 to enhance PGR activity. Modulates expression of post-synaptic scaffolding proteins via regulation of ESR1, ESR2 and PGR (By similarity).

**Summary**, from NCBI Gene [23558](https://www.ncbi.nlm.nih.gov/gene/23558):

> The globular WW domain is composed of 38 to 40 semiconserved amino acids shared by proteins of diverse functions including structural, regulatory, and signaling proteins. The domain is involved in mediating protein-protein interactions through the binding of polyproline ligands. This gene encodes a WW domain binding protein that is a transcriptional coactivator of estrogen receptor alpha and progesterone receptor. Defects in this gene have been associated with hearing impairment. [provided by …

**Accessions** — [HGNC:12738](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12738) · Entrez [23558](https://www.ncbi.nlm.nih.gov/gene/23558) · UniProt [Q969T9](https://www.uniprot.org/uniprotkb/Q969T9) · Ensembl [ENSG00000132471](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132471)

## Data

Gene col 5326: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5326); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5326, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5326]; `tensor/DDL_lfc|DDL_z.npy` [5326]; `embed/gene_vectors.npy` [5326]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5326 or target_col == 5326). Every well: [[WBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
