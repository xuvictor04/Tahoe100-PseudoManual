---
symbol: "TTLL3"
type: "gene"
col: 13162
ensembl_id: "ENSG00000214021"
name: "tubulin tyrosine ligase like 3"
location: "3p25.3"
module: 38
arm: "+"
pooled_cpm: 49.87
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 24
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# TTLL3

*tubulin tyrosine ligase like 3* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +12.6, q 2e-33, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.482× (z -13.5, q 9e-39, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RABGEF1]] (+0.76, fdr 7e-06), [[SPRED3]] (+0.75, fdr 7e-06), [[SYCE1L]] (+0.74, fdr 7e-06); moves opposite to [[DLD]] (-0.62, fdr 1e-05), [[KCTD3]] (-0.61, fdr 1e-05), [[TRUB1]] (-0.61, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13162.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +12.6 | 2e-33 | 39/48 (AsPC-1, SW480, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +5.8 | 1e-06 | 28/48 (SW480, HT-29, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 0.002 | 20/48 (Panc 03.27, A-172, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.3 | 0.003 | 17/48 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.21×** | +3.4 | 0.067 | 19/48 (NCI-H460, SW480, …) | top dose only |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.067 | 16/48 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.12× | +3.1 | 0.17 | 9/48 (SNU-423, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 14 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13162.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.482×** | -13.5 | 9e-39 | 42/48 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.469×** | -13.2 | 2e-37 | 39/47 (Panc 03.27, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.501×** | -12.8 | 3e-35 | 41/49 (A-427, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.507×** | -11.9 | 3e-30 | 32/41 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.545×** | -10.4 | 3e-23 | 33/44 (H4, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.630×** | -8.5 | 1e-15 | 33/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.615×** | -8.5 | 2e-15 | 38/46 (hTERT-HPNE, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.679×** | -7.1 | 7e-11 | 28/47 (SW1417, CFPAC-1, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.484×** | -7.0 | 1e-10 | 33/47 (HepG2/C3A, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.685×** | -7.0 | 2e-10 | 33/48 (NCI-H2030, H4, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **0.688×** | -6.9 | 2e-10 | 29/48 (LoVo, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.691×** | -6.8 | 4e-10 | 32/48 (A549, HEC-1-A, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.696×** | -6.3 | 1e-08 | 32/48 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.790×** | -6.2 | 3e-08 | 28/47 (A498, HT-29, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.554×** | -5.7 | 4e-07 | 26/49 (RKO, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.590×** | -5.1 | 1e-05 | 23/47 (A-427, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.769×** | -4.8 | 4e-05 | 25/48 (LOX-IMVI, RPMI-7951, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.786×** | -4.4 | 3e-04 | 25/48 (RPMI-7951, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.844× | -4.4 | 3e-04 | 23/48 (RKO, A-427, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.652×** | -4.1 | 1e-03 | 25/48 (RKO, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.807×** | -4.0 | 0.002 | 21/48 (HepG2/C3A, A-427, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.804×** | -3.7 | 0.005 | 24/47 (SW 900, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.835× | -3.3 | 0.021 | 15/48 (NCI-H460, SNU-1, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.720×** | -3.2 | 0.032 | 14/48 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | 0.835× | -3.1 | 0.041 | 17/47 (KATO III, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13162. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 88.8 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.436× (z -8.5) |
| [[A-427 (line)]] | wt | 92.3 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0698× (z -28.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.378× (z -10.5) |
| [[SW480 (line)]] | alt | 58.0 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.438× (z -9.2) |
| [[LoVo (line)]] | wt | 88.4 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -18.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 42.2 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -13.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 37.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -13.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.273× (z -11.4) |
| [[A549 (line)]] | wt | 48.0 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.227× (z -12.8) |
| [[H4 (line)]] | wt | 75.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0676× (z -18.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 77.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -11.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.365× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 36.0 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -11.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 46.5 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +10.0) | [[Harringtonine (drug)]] 5 µM 0.200× (z -13.1) |
| [[SNU-423 (line)]] | alt | 60.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.283× (z -11.7) |
| [[SW1417 (line)]] | alt | 41.7 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -13.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.298× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 27.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +13.7) | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 23.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.232× (z -11.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.278× (z -9.8) |
| [[HOP62 (line)]] | alt | 72.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.366× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 40.0 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.321× (z -9.2) |
| [[PANC-1 (line)]] | alt | 39.4 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.385× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 59.2 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.266× (z -10.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 42.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.174× (z -9.8) |
| [[BT-474 (line)]] | alt | 40.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 43.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.205× (z -10.8) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 64.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0997× (z -15.7) ⚠ toxic |
| [[J82 (line)]] | alt | 38.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0374× (z -23.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 28.1 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.292× (z -9.0) |
| [[LS 180 (line)]] | wt | 52.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.296× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 38.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.262× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 30.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 38.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.281× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 63.2 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.227× (z -10.0) ⚠ toxic |
| [[C-33 A (line)]] | alt | 62.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -13.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 62.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -16.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 80.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0634× (z -21.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 71.2 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.298× (z -9.7) |
| [[Hs 766T (line)]] | wt | 27.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -13.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 29.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -13.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 36.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.9) | — |
| [[RKO (line)]] | wt | 97.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -20.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -14.7) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 74.6 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.112× (z -8.5) |
| [[SW 900 (line)]] | alt | 24.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13162), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGEF1]] | +0.76 | +0.63 / +0.79 | both halves | 7e-06 |  |
| [[SPRED3]] | +0.75 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[SYCE1L]] | +0.74 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[ATP2A1]] | +0.74 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[ORAI2]] | +0.72 | +0.66 / +0.75 | both halves | 7e-06 |  |
| [[SENP5]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[WNT2B]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[GOSR2]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[VWCE]] | +0.69 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.69 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[TPT1-AS1]] | +0.68 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[LINC01588]] | +0.68 | +0.66 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLD]] | -0.62 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[KCTD3]] | -0.61 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[TRUB1]] | -0.61 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[COX11]] | -0.60 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[CFL2]] | -0.59 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[PAIP1]] | -0.59 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[MBTPS2]] | -0.58 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[SCCPDH]] | -0.58 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[NBN]] | -0.57 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[COMMD8]] | -0.57 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[MDM1]] | -0.57 | -0.50 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.773). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.0, -20.2); signed map (11.2, 12.4). **Vector** length 119, 35.1% of its response variance represented; |z| ≥ 3 in 1,109 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +12.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.4 | +5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +4.2 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +4.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +3.4 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +1.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.8 | +2.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.3 | -13.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.1 | -13.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.7 | -6.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -5.4 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.7 | -4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.5 | -4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | tubulin tyrosine ligase like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:9,808,086-9,855,138 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434B103, HOTTL |
| Gene groups (HGNC) | Tubulin tyrosine ligase family |
| Reactome | 1 pathways, smallest: Carboxyterminal post-translational modifications of tubulin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4R7](https://www.uniprot.org/uniprotkb/Q9Y4R7) (Tubulin monoglycylase TTLL3):

> Monoglycylase which modifies alpha- and beta-tubulin, adding a single glycine on the gamma-carboxyl groups of specific glutamate residues to generate monoglycine side chains within the C-terminal tail of tubulin. Not involved in elongation step of the polyglycylation reaction (By similarity). Preferentially glycylates a beta-tail peptide over the alpha-tail, although shifts its preference toward alpha-tail as beta-tail glutamylation increases (By similarity). Competes with polyglutamylases for …

**Summary**, from NCBI Gene [26140](https://www.ncbi.nlm.nih.gov/gene/26140):

> Enables protein-glycine ligase activity. Predicted to be involved in axoneme assembly; flagellated sperm motility; and spermatogenesis. Predicted to be located in cilium. Predicted to be active in axoneme; microtubule cytoskeleton; and sperm flagellum. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24483](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24483) · Entrez [26140](https://www.ncbi.nlm.nih.gov/gene/26140) · UniProt [Q9Y4R7](https://www.uniprot.org/uniprotkb/Q9Y4R7) · Ensembl [ENSG00000214021](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214021)

## Data

Gene col 13162: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13162); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13162, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13162]; `tensor/DDL_lfc|DDL_z.npy` [13162]; `embed/gene_vectors.npy` [13162]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13162 or target_col == 13162). Every well: [[TTLL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTLL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
