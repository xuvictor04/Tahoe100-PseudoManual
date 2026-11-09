---
symbol: "ANKMY2"
type: "gene"
col: 2769
ensembl_id: "ENSG00000106524"
name: "ankyrin repeat and MYND domain containing 2"
location: "7p21.1"
module: 30
arm: "+"
pooled_cpm: 57.21
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 19
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# ANKMY2

*ankyrin repeat and MYND domain containing 2* — 7p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.70× (z +9.9, q 2e-20, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.384× (z -16.4, q 0e+00, down in 38 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.635× (z -8.4, q 4e-15, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPB11]] (+0.70, fdr 7e-06), [[PLCD1]] (+0.69, fdr 1e-05), [[SEPTIN6]] (+0.67, fdr 1e-05); moves opposite to [[MSRA]] (-0.61, fdr 1e-05), [[GNL3L]] (-0.60, fdr 1e-05), [[ENOX2]] (-0.59, fdr 4e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ABL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2769.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.70×** | +9.9 | 2e-20 | 36/48 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +9.2 | 1e-17 | 40/48 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +7.8 | 1e-12 | 29/48 (SW1417, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.9 | 1e-04 | 28/48 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.20×** | +4.8 | 2e-04 | 22/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +4.5 | 8e-04 | 23/48 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +4.4 | 8e-04 | 22/49 (HT-29, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.55×** | +4.3 | 0.001 | 23/47 (H4, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.25×** | +3.9 | 0.005 | 21/48 (SW480, RKO, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.025 | 14/48 (LS 180, SW 900, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.031 | 19/48 (RKO, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +3.4 | 0.031 | 21/48 (RKO, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.3 | 0.038 | 14/48 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.3 | 0.043 | 19/45 (PANC-1, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2769.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.384×** | -16.4 | 0e+00 | 38/40 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.402×** | -16.3 | 0e+00 | 36/38 (SNU-1, A549, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.470×** | -14.0 | 3e-42 | 38/48 (AsPC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.623×** | -8.4 | 4e-15 | 33/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.635×** | -8.4 | 4e-15 | 37/48 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.674×** | -7.0 | 2e-10 | 33/48 (NCI-H2347, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.769×** | -4.9 | 1e-04 | 24/48 (A-172, A549, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.785×** | -4.5 | 5e-04 | 19/47 (H4, PANC-1, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.784×** | -4.3 | 1e-03 | 24/48 (A498, A-172, …) | all doses, flat | composition shift |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.793×** | -4.3 | 0.001 | 25/49 (SW480, HS-578T, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.791×** | -4.2 | 0.001 | 24/48 (H4, A498, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.799×** | -4.2 | 0.002 | 22/48 (Hs 766T, SNU-423, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.659×** | -4.0 | 0.002 | 22/49 (A-172, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.795×** | -3.9 | 0.003 | 21/47 (LoVo, NCI-H460, …) | all doses, flat | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.870× | -3.6 | 0.011 | 18/48 (A498, H4, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.870× | -3.6 | 0.012 | 11/48 (A-427, SW1417, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.834× | -3.4 | 0.022 | 15/48 (HEC-1-A, HT-29, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.829×** | -3.3 | 0.023 | 18/47 (BT-474, H4, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.839× | -3.2 | 0.030 | 17/48 (COLO 205, Panc 03.27, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.843× | -3.2 | 0.036 | 17/48 (SW1417, HEC-1-A, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.756×** | -3.1 | 0.043 | 14/48 (Hs 766T, NCI-H2347, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2769. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 62.6 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.235× (z -14.2) |
| [[A498 (line)]] | wt | 107 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.349× (z -12.7) |
| [[KATO III (line)]] | alt | 94.8 | 3 (1 ⚠) | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.67× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -11.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 69.3 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.373× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 66.4 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.274× (z -12.4) ⚠ toxic |
| [[SW1417 (line)]] | alt | 74.4 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.03× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -11.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 62.7 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.04× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -14.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 51.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.415× (z -9.1) |
| [[H4 (line)]] | wt | 131 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -12.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 44.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.416× (z -9.0) |
| [[HT-29 (line)]] | alt | 40.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.86× (z +11.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 47.5 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 33.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.28× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -9.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 89.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -17.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 106 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -14.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 54.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 53.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 52.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 55.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -16.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 40.5 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.47× (z +11.2) | — |
| [[SNU-1 (line)]] | wt | 124 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0993× (z -18.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 34.2 | 0 | 2 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0827× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 52.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -14.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 57.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 21.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.10× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 55.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -13.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 85.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -9.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 63.1 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.72× (z +8.8) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.132× (z -9.2) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 37.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.41× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 70.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 46.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HEC-1-A (line)]] | alt | 61.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -14.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 53.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.423× (z -10.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 42.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.266× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0703× (z -10.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 70.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -11.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2769), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPB11]] | +0.70 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[PLCD1]] | +0.69 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[SEPTIN6]] | +0.67 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[MGST3]] | +0.67 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[AZIN2]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[CAT]] | +0.65 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[PRRC1]] | +0.65 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[SNAPC3]] | +0.65 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[RAB3A]] | +0.64 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[VDAC3]] | +0.64 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[GMCL1]] | +0.64 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[PLEKHH3]] | +0.64 | +0.50 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSRA]] | -0.61 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[GNL3L]] | -0.60 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[ENOX2]] | -0.59 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[REXO1]] | -0.59 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[SLC20A2]] | -0.59 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[ITPA]] | -0.59 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[ST7L]] | -0.59 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[MAPKAP1]] | -0.59 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[TBCEL]] | -0.59 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[ZC3H4]] | -0.59 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.58 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[E2F3]] | -0.58 | -0.58 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABL1]] | B | ABL1 activity lowers ANKMY2's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 2.8% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SNHG18]] | B | SNHG18 activity raises ANKMY2's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.40× lower at baseline in the lines without SNHG18 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.686). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (5.7, -6.4); signed map (-31.6, 20.0). **Vector** length 122, 36.4% of its response variance represented; |z| ≥ 3 in 1,254 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +5.8 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.1 | +4.9 |
|  | [[NG25 (drug)]] 5 µM |  | +4.9 | +4.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +9.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +3.4 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +3.0 | +3.5 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +3.0 | +2.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.2 | -8.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.1 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -4.5 | -3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.3 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.0 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and MYND domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.1 — chr7:16,599,779-16,645,817 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564O043, ZMYND20 |
| Gene groups (HGNC) | Zinc fingers MYND-type; Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IV38](https://www.uniprot.org/uniprotkb/Q8IV38) (Ankyrin repeat and MYND domain-containing protein 2):

> May be involved in the trafficking of signaling proteins to the cilia.

**Summary**, from NCBI Gene [57037](https://www.ncbi.nlm.nih.gov/gene/57037):

> Predicted to enable enzyme binding activity and zinc ion binding activity. Predicted to be located in cilium. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25370) · Entrez [57037](https://www.ncbi.nlm.nih.gov/gene/57037) · UniProt [Q8IV38](https://www.uniprot.org/uniprotkb/Q8IV38) · Ensembl [ENSG00000106524](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106524)

## Data

Gene col 2769: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2769); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2769, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2769]; `tensor/DDL_lfc|DDL_z.npy` [2769]; `embed/gene_vectors.npy` [2769]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2769 or target_col == 2769). Every well: [[ANKMY2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKMY2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
