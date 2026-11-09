---
symbol: "PIEZO1"
type: "gene"
col: 2354
ensembl_id: "ENSG00000103335"
name: "piezo type mechanosensitive ion channel component 1 (Er blood group)"
location: "16q24.3"
module: 54
arm: "-"
pooled_cpm: 51.84
n_lines_expressing: 49
n_dd_up: 22
n_dd_down: 10
n_dd_up_clean: 16
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# PIEZO1

*piezo type mechanosensitive ion channel component 1 (Er blood group)* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.58× (z +30.6, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.505× (z -11.6, q 2e-28, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THOC6]] (+0.71, fdr 7e-06), [[CROCC]] (+0.67, fdr 2e-05), [[WDR1]] (+0.66, fdr 1e-05); moves opposite to [[MRPL55]] (-0.66, fdr 4e-05), [[MPG]] (-0.65, fdr 2e-05), [[CNOT8]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[FSTL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2354.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.58×** | +30.6 | 0e+00 | 43/46 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.38×** | +14.2 | 5e-43 | 40/47 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.21×** | +13.5 | 4e-39 | 38/46 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +11.8 | 1e-29 | 29/38 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +11.4 | 7e-28 | 33/45 (NCI-H1792, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +10.5 | 5e-24 | 30/43 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.82×** | +10.2 | 2e-22 | 36/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +8.6 | 4e-16 | 30/47 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +6.1 | 5e-08 | 30/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +6.0 | 9e-08 | 26/47 (SW480, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +5.7 | 8e-07 | 29/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.39×** | +5.6 | 1e-06 | 27/46 (NCI-H460, HT-29, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.33×** | +4.8 | 6e-05 | 26/47 (NCI-H1573, NCI-H460, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +4.7 | 9e-05 | 22/47 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +4.6 | 1e-04 | 26/47 (LoVo, NCI-H1792, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +4.3 | 6e-04 | 24/48 (HEC-1-A, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +3.9 | 0.004 | 18/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.004 | 22/47 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +3.7 | 0.006 | 18/47 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.013 | 22/46 (LS 180, C32, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.028 | 11/47 (PANC-1, HEC-1-A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2354.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.505×** | -11.6 | 2e-28 | 38/47 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.523×** | -11.0 | 7e-26 | 38/47 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.536×** | -10.6 | 4e-24 | 41/47 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.672×** | -6.8 | 2e-09 | 34/47 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.706×** | -5.9 | 3e-07 | 37/47 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.794×** | -4.0 | 0.007 | 22/47 (LoVo, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.654×** | -3.8 | 0.012 | 20/47 (SNU-1, BT-474, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.866× | -3.5 | 0.030 | 17/47 (LoVo, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **0.809×** | -3.5 | 0.030 | 19/45 (A-172, PANC-1, …) | top dose only | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.813×** | -3.4 | 0.036 | 19/47 (A-427, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.708×** | -3.1 | 0.095 | 13/44 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.882× | -3.1 | 0.095 | 16/47 (RKO, KATO III, …) | rises with dose | low cells (technical?) |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.882× | -3.1 | 0.095 | 6/48 (NCI-H460, MIA PaCa-2, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2354. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.8 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +23.3) | — |
| [[A-172 (line)]] | wt | 171 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.353× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 50.4 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +16.3) | [[Belinostat (drug)]] 5 µM 0.212× (z -14.3) |
| [[KATO III (line)]] | alt | 43.8 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +19.7) | — |
| [[NCI-H1573 (line)]] | alt | 41.0 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +19.6) | [[Belinostat (drug)]] 5 µM 0.324× (z -8.5) |
| [[SW480 (line)]] | alt | 49.9 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +11.7) | — |
| [[BT-474 (line)]] | alt | 60.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +17.4) | — |
| [[C32 (line)]] | wt | 26.2 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +13.0) | — |
| [[J82 (line)]] | alt | 76.6 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +13.6) | [[Belinostat (drug)]] 5 µM 0.344× (z -10.7) |
| [[LoVo (line)]] | wt | 36.7 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +14.9) | [[Belinostat (drug)]] 5 µM 0.230× (z -12.1) |
| [[NCI-H1792 (line)]] | alt | 39.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +13.4) | — |
| [[NCI-H2347 (line)]] | alt | 25.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +18.9) | — |
| [[RPMI-7951 (line)]] | alt | 40.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +20.0) | — |
| [[A498 (line)]] | wt | 63.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +17.9) | — |
| [[A549 (line)]] | wt | 27.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.65× (z +17.7) | — |
| [[HepG2_C3A (line)]] | wt | 59.3 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.16× (z +19.5) | [[Belinostat (drug)]] 5 µM 0.201× (z -11.2) |
| [[HOP62 (line)]] | alt | 86.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.86× (z +25.5) | — |
| [[HS-578T (line)]] | alt | 50.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.77× (z +22.9) | — |
| [[hTERT-HPNE (line)]] | wt | 50.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.65× (z +18.7) | — |
| [[A-427 (line)]] | wt | 40.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +9.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -9.2) ⚠ cell-cycle shift, explains ~91% of this change |
| [[AsPC-1 (line)]] | alt | 42.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +20.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 98.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +15.1) | — |
| [[RKO (line)]] | wt | 94.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.330× (z -9.3) |
| [[SNU-423 (line)]] | alt | 30.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.76× (z +23.8) | — |
| [[SW 900 (line)]] | alt | 28.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.18× (z +19.2) | — |
| [[CFPAC-1 (line)]] | alt | 66.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.22× (z +22.2) | — |
| [[COLO 205 (line)]] | alt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.76× (z +15.1) | — |
| [[H4 (line)]] | wt | 114 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 34.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +14.1) | — |
| [[HT-29 (line)]] | alt | 59.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +14.5) | — |
| [[LOX-IMVI (line)]] | wt | 47.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 51.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 59.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +12.6) | — |
| [[Panc 03.27 (line)]] | alt | 41.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.55× (z +18.7) | — |
| [[PANC-1 (line)]] | alt | 44.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.5) | — |
| [[SK-MEL-2 (line)]] | alt | 45.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +15.1) | — |
| [[SNU-1 (line)]] | wt | 61.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 48.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +17.3) | — |
| [[AN3 CA (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.95 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2354), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC6]] | +0.71 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[CROCC]] | +0.67 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[WDR1]] | +0.66 | +0.52 / +0.71 | both halves | 1e-05 | same gene group |
| [[PRRC2B]] | +0.65 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ZNF655]] | +0.65 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[DLG5]] | +0.64 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[FKRP]] | +0.64 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[FLII]] | +0.63 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[NPIPB4]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SDCBP2-AS1]] | +0.62 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[CELSR3]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 | same gene group |
| [[MYO1C]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL55]] | -0.66 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[MPG]] | -0.65 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[CNOT8]] | -0.65 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[ATP5MJ]] | -0.64 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[ATG4C]] | -0.63 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[CAMLG]] | -0.63 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[MALSU1]] | -0.63 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[SDHAF1]] | -0.62 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[MED23]] | -0.62 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[COX14]] | -0.62 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.62 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[KLHDC10]] | -0.62 | -0.55 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSTL3]] | B | FSTL3 activity raises PIEZO1's level | lines that do not express FSTL3 (7) vs lines expressing it (43) | 1.59× lower at baseline in the lines without FSTL3 | 0.008 | ⚠ within organs, on part of the lines; also absent: PDLIM2, TAGLN2, CCND1 |
| [[C1RL-AS1]] | B | C1RL-AS1 activity raises PIEZO1's level | lines that do not express C1RL-AS1 (7) vs lines expressing it (43) | 1.92× lower at baseline in the lines without C1RL-AS1 | 0.059 | ⚠ within organs, on part of the lines; also absent: EGFR, HFE, SH2D4A |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PIEZO1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises PIEZO1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ARHGEF17]] | C | ARHGEF17 activity raises PIEZO1's level | lines that do not express ARHGEF17 (4) vs lines expressing it (46) | 1.89× lower at baseline in the lines without ARHGEF17 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RGS10; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.723). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (1.6, -15.9); signed map (20.0, -27.2). **Vector** length 125, 36.8% of its response variance represented; |z| ≥ 3 in 1,183 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +12.4 | +30.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.0 | +11.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.8 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +6.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +4.6 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.7 | +1.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.4 | -5.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.0 | -11.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.5 | -6.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.2 | -10.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.0 | -11.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | -3.0 | -1.5 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.6 | -1.9 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | -2.5 | -1.9 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | piezo type mechanosensitive ion channel component 1 (Er blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:88,715,338-88,785,220 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0233; previously FAM38A |
| Gene groups (HGNC) | Blood group antigens; MicroRNA protein coding host genes; Piezo type mechanosensitive ion channel components |
| Reactome | 6 pathways, smallest: Mechanical load activates signaling by PIEZO1 and integrins in osteocytes; Turbulent (oscillatory, disturbed) flow shear stress activates signaling by PIEZO1 and integrins in endothelial cells; High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92508](https://www.uniprot.org/uniprotkb/Q92508) (Piezo-type mechanosensitive ion channel component 1):

> Pore-forming subunit of the mechanosensitive non-specific cation Piezo channel required for rapidly adapting mechanically activated (MA) currents and has a key role in sensing touch and tactile pain. Piezo channels are homotrimeric three-blade propeller-shaped structures that utilize a cap-motion and plug-and-latch mechanism to gate their ion-conducting pathways. Generates currents characterized by a linear current-voltage relationship that are sensitive to ruthenium red and gadolinium (By …

**Summary**, from NCBI Gene [9780](https://www.ncbi.nlm.nih.gov/gene/9780):

> The protein encoded by this gene is a mechanically-activated ion channel that links mechanical forces to biological signals. The encoded protein contains 36 transmembrane domains and functions as a homotetramer. Defects in this gene have been associated with dehydrated hereditary stomatocytosis. [provided by RefSeq, Jul 2015]

**Accessions** — [HGNC:28993](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28993) · Entrez [9780](https://www.ncbi.nlm.nih.gov/gene/9780) · UniProt [Q92508](https://www.uniprot.org/uniprotkb/Q92508) · Ensembl [ENSG00000103335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103335)

## Data

Gene col 2354: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2354); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2354, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2354]; `tensor/DDL_lfc|DDL_z.npy` [2354]; `embed/gene_vectors.npy` [2354]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2354 or target_col == 2354). Every well: [[PIEZO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIEZO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
