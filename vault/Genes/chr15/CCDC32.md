---
symbol: "CCDC32"
type: "gene"
col: 4929
ensembl_id: "ENSG00000128891"
name: "coiled-coil domain containing 32"
location: "15q15.1"
module: 72
arm: "+"
pooled_cpm: 37.7
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 18
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# CCDC32

*coiled-coil domain containing 32* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.94× (z +14.3, q 1e-43, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.695× (z -11.2, q 3e-26, down in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~85% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.426× (z -9.7, q 4e-20, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED31]] (+0.75, fdr 7e-06), [[SLC30A6]] (+0.69, fdr 7e-06), [[GPR89A]] (+0.66, fdr 9e-06); moves opposite to [[NAB1]] (-0.62, fdr 1e-05), [[PLCB4]] (-0.60, fdr 1e-05), [[VEZF1]] (-0.59, fdr 1e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4929.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.94×** | +14.3 | 1e-43 | 43/48 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.01×** | +14.2 | 2e-43 | 44/48 (COLO 205, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +12.4 | 6e-33 | 38/48 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.76×** | +12.3 | 2e-32 | 41/48 (C-33 A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +12.1 | 1e-31 | 40/48 (HT-29, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.67×** | +11.1 | 2e-26 | 40/48 (COLO 205, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +8.4 | 3e-15 | 33/48 (HT-29, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.38×** | +6.7 | 1e-09 | 26/48 (NCI-H460, A498, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.23×** | +6.3 | 2e-08 | 24/48 (AsPC-1, HT-29, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.45×** | +5.8 | 4e-07 | 30/48 (A-172, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **1.27×** | +5.0 | 3e-05 | 24/47 (AsPC-1, Panc 03.27, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.46×** | +4.3 | 8e-04 | 22/43 (PANC-1, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.20× | +3.9 | 0.005 | 17/48 (A-427, HT-29, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.20×** | +3.8 | 0.006 | 16/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +3.5 | 0.016 | 21/48 (HT-29, NCI-H2030, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.073 | 15/48 (C-33 A, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.0 | 0.080 | 5/48 (PANC-1, SNU-423, …) | inconsistent across doses | plate-row cell shift |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.16× | +2.9 | 0.100 | 8/48 (HT-29, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4929.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.695×** | -11.2 | 3e-26 | 33/48 (H4, A498, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.589×** | -11.1 | 6e-26 | 34/47 (SNU-423, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.591×** | -11.0 | 8e-26 | 34/48 (A498, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.607×** | -10.0 | 2e-21 | 32/43 (NCI-H460, A-172, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.426×** | -9.7 | 4e-20 | 41/49 (SNU-423, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.650×** | -9.4 | 8e-19 | 30/47 (LS 180, HT-29, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.668×** | -8.4 | 3e-15 | 27/38 (A498, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.497×** | -7.9 | 2e-13 | 32/48 (SNU-1, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.697×** | -7.8 | 3e-13 | 31/48 (A498, H4, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.711×** | -7.4 | 7e-12 | 25/48 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.791×** | -4.9 | 5e-05 | 19/47 (HT-29, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.819×** | -4.3 | 7e-04 | 16/48 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.771×** | -4.0 | 0.002 | 18/48 (CFPAC-1, HT-29, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.831×** | -4.0 | 0.002 | 19/47 (NCI-H661, H4, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.832×** | -4.0 | 0.002 | 15/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.832×** | -3.8 | 0.004 | 12/48 (CFPAC-1, HOP62, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **0.725×** | -3.6 | 0.008 | 13/46 (NCI-H460, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.809×** | -3.3 | 0.029 | 15/47 (HCT15, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.866× | -3.0 | 0.069 | 15/48 (SNU-423, C32, …) | top dose only |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.871× | -2.9 | 0.094 | 4/48 (LOX-IMVI, J82, …) | top dose only | plate-row cell shift |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.876× | -2.9 | 0.094 | 11/47 (CFPAC-1, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4929. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 97.7 | 3 | 5 (5 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.49× (z +11.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.285× (z -11.8) ⚠ toxic |
| [[A498 (line)]] | wt | 50.3 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -19.6) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.335× (z -13.6) |
| [[NCI-H460 (line)]] | wt | 25.3 | 5 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -14.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 33.0 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -12.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 71.4 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.57× (z +10.2) | [[Lonafarnib (drug)]] 5 µM 0.0814× (z -14.3) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 57.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Verteporfin (drug)]] 5 µM 0.185× (z -8.9) |
| [[H4 (line)]] | wt | 49.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0943× (z -22.0) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.249× (z -9.2) |
| [[LS 180 (line)]] | wt | 33.1 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.91× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -19.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 31.9 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.50× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 48.0 | 2 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.09× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -13.3) ⚠ cell-cycle shift, explains ~85% of this change |
| [[PANC-1 (line)]] | alt | 61.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -11.4) ⚠ cell-cycle shift, explains ~85% of this change |
| [[SNU-423 (line)]] | alt | 39.7 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.171× (z -14.6) ⚠ toxic |
| [[C-33 A (line)]] | alt | 40.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.25× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 33.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -16.9) ⚠ cell-cycle shift, explains ~85% of this change |
| [[Panc 03.27 (line)]] | alt | 27.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -10.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 34.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.43× (z +9.4) | — |
| [[A-427 (line)]] | wt | 26.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -12.0) ⚠ cell-cycle shift, explains ~85% of this change |
| [[A549 (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -9.1) ⚠ cell-cycle shift, explains ~48% of this change |
| [[CFPAC-1 (line)]] | alt | 34.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 48.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -10.5) ⚠ cell-cycle shift, explains ~85% of this change |
| [[HepG2_C3A (line)]] | wt | 51.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.218× (z -10.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -9.0) ⚠ cell-cycle shift, explains ~85% of this change |
| [[J82 (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.310× (z -9.2) ⚠ toxic |
| [[KATO III (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 48.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.303× (z -10.7) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 30.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +10.8) | — |
| [[NCI-H661 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0717× (z -8.5) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 51.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -15.9) ⚠ cell-cycle shift, explains ~85% of this change |
| [[RPMI-7951 (line)]] | alt | 49.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.163× (z -13.4) ⚠ toxic |
| [[SW48 (line)]] | wt | 27.5 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.182× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4929), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED31]] | +0.75 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[SLC30A6]] | +0.69 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[GPR89A]] | +0.66 | +0.57 / +0.71 | both halves | 9e-06 |  |
| [[SDF2]] | +0.65 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[VRK3]] | +0.65 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[TM2D1]] | +0.65 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[PSMB5]] | +0.64 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[ANKRD39]] | +0.64 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[NDUFAF7]] | +0.64 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[MBOAT7]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[BABAM1]] | +0.63 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[GPR89B]] | +0.62 | +0.56 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAB1]] | -0.62 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[PLCB4]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[VEZF1]] | -0.59 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[HNRNPD]] | -0.57 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[CDK6]] | -0.56 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[SRSF3]] | -0.55 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[FAT1]] | -0.55 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[ISOC1]] | -0.54 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[CDH2]] | -0.54 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[LCOR]] | -0.54 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[CEP41]] | -0.54 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[BBS10]] | -0.54 | -0.51 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCDC32's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CEP41]] | C | CEP41 activity raises CCDC32's level | lines that do not express CEP41 (4) vs lines expressing it (46) | 1.31× lower at baseline in the lines without CEP41 | 0.083 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LRRIQ3, LINC02175, WDR35 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.7, -5.6); signed map (-44.5, 4.0). **Vector** length 108, 28.3% of its response variance represented; |z| ≥ 3 in 1,237 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +11.8 | +14.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +11.3 | +14.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.0 | +11.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.2 | +5.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | +4.8 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +3.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.2 | +2.9 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | -8.2 | -11.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -6.8 | -11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.3 | -9.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.3 | -11.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -6.0 | -7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -7.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.1 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -4.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 32 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,528,683-40,565,054 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC20481; previously C15orf57 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BV29](https://www.uniprot.org/uniprotkb/Q9BV29) (Coiled-coil domain-containing protein 32):

> Regulates clathrin-mediated endocytsois of cargos such as transferrin probably through the association and modulation of adaptor protein complex 2 (AP-2). Has a role in ciliogenesis (By similarity). Required for proper cephalic and left/right axis development.

**Summary**, from NCBI Gene [90416](https://www.ncbi.nlm.nih.gov/gene/90416):

> Involved in head development and regulation of clathrin-dependent endocytosis. Part of clathrin-coated pit. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28295](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28295) · Entrez [90416](https://www.ncbi.nlm.nih.gov/gene/90416) · UniProt [Q9BV29](https://www.uniprot.org/uniprotkb/Q9BV29) · Ensembl [ENSG00000128891](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128891)

## Data

Gene col 4929: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4929); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4929, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4929]; `tensor/DDL_lfc|DDL_z.npy` [4929]; `embed/gene_vectors.npy` [4929]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4929 or target_col == 4929). Every well: [[CCDC32 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC32.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
