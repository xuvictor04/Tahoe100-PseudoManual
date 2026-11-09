---
symbol: "SANBR"
type: "gene"
col: 8602
ensembl_id: "ENSG00000162929"
name: "SANT and BTB domain regulator of CSR"
location: "2p15"
module: 72
arm: "+"
pooled_cpm: 28.21
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 21
n_dd_up_clean: 17
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# SANBR

*SANT and BTB domain regulator of CSR* — 2p15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.51× (z +10.2, q 1e-21, up in 35 of 47 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.54× (z +7.6, q 3e-12, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.426× (z -15.0, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPNE2]] (+0.62, fdr 7e-06), [[KIF1B]] (+0.60, fdr 7e-06), [[SFXN5]] (+0.59, fdr 1e-05); moves opposite to [[LINC01473]] (-0.55, fdr 4e-05), [[TXNIP]] (-0.51, fdr 3e-05), [[PPP1R3B]] (-0.50, fdr 2e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 16 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8602.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.51×** | +10.2 | 1e-21 | 35/47 (RKO, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +9.8 | 4e-20 | 31/41 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +9.2 | 4e-18 | 29/37 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.68×** | +9.1 | 1e-17 | 37/48 (LoVo, A498, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.65×** | +8.5 | 3e-15 | 29/47 (NCI-H460, A549, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.59×** | +8.2 | 3e-14 | 33/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +7.6 | 3e-12 | 31/48 (C-33 A, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.61×** | +7.5 | 5e-12 | 30/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.50×** | +6.9 | 4e-10 | 27/48 (LS 180, LoVo, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.47×** | +6.4 | 8e-09 | 22/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.43×** | +6.2 | 2e-08 | 26/47 (HepG2/C3A, NCI-H1792, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.41×** | +5.8 | 2e-07 | 22/47 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~60% of this change | **1.41×** | +5.8 | 2e-07 | 25/44 (SW480, HCT15, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +5.8 | 2e-07 | 23/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +5.8 | 3e-07 | 24/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.80×** | +5.4 | 3e-06 | 20/48 (LoVo, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.0 | 2e-05 | 19/48 (A549, SW480, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +4.7 | 6e-05 | 16/46 (Hs 766T, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +4.5 | 2e-04 | 18/48 (A-427, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.001 | 15/47 (hTERT-HPNE, H4, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.26×** | +4.0 | 0.001 | 16/47 (Hs 766T, RPMI-7951, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.002 | 13/47 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.002 | 11/48 (A498, KATO III, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.005 | 15/48 (NCI-H1573, A-427, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.18× | +3.4 | 0.012 | 13/48 (A-427, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.013 | 9/48 (SW480, A-427, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8602.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.426×** | -15.0 | 0e+00 | 42/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.552×** | -14.7 | 0e+00 | 34/48 (A-172, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.465×** | -12.1 | 1e-31 | 36/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.506×** | -11.9 | 1e-30 | 33/46 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.284×** | -11.5 | 1e-28 | 41/48 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.544×** | -10.3 | 9e-23 | 33/48 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.343×** | -9.8 | 9e-21 | 35/48 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.547×** | -9.6 | 9e-20 | 36/47 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.591×** | -9.2 | 2e-18 | 30/48 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.608×** | -8.7 | 1e-16 | 27/47 (A-427, A-172, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.550×** | -5.5 | 2e-06 | 21/45 (A-172, H4, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.769×** | -4.6 | 2e-04 | 22/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.768×** | -4.0 | 0.003 | 16/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **0.791×** | -4.0 | 0.003 | 19/46 (SW480, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.783×** | -4.0 | 0.003 | 15/46 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | **0.798×** | -3.8 | 0.006 | 11/48 (HS-578T, SW480, …) | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.678×** | -3.6 | 0.011 | 12/46 (MIA PaCa-2, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.813×** | -3.5 | 0.014 | 13/48 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.815×** | -3.5 | 0.015 | 11/47 (HOP62, HS-578T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.887× | -3.0 | 0.071 | 10/48 (KATO III, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 0.848× | -2.9 | 0.092 | 9/48 (SW 1271, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8602. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 33.1 | 1 (1 ⚠) | 7 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.57× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -15.8) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -13.9) |
| [[A549 (line)]] | wt | 43.8 | 2 (2 ⚠) | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +9.4) ⚠ cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -18.7) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.345× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 25.1 | 2 (2 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +11.4) ⚠ cell-cycle shift, explains ~27% of this change | [[Harringtonine (drug)]] 0.5 µM 0.240× (z -12.0) |
| [[A-172 (line)]] | wt | 62.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -24.8) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.326× (z -10.3) |
| [[A-427 (line)]] | wt | 78.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0523× (z -32.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0640× (z -15.9) |
| [[LOX-IMVI (line)]] | wt | 24.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -11.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.274× (z -9.1) |
| [[A498 (line)]] | wt | 24.5 | 2 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +9.9) ⚠ cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -10.1) ⚠ cell-cycle shift, explains ~55% of this change |
| [[AsPC-1 (line)]] | alt | 23.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -14.3) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.263× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 20.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.54× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.234× (z -9.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SW480 (line)]] | alt | 23.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.284× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 48.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -14.2) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.151× (z -9.6) |
| [[HOP62 (line)]] | alt | 28.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.287× (z -9.2) |
| [[J82 (line)]] | alt | 32.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -11.4) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.291× (z -9.8) |
| [[RKO (line)]] | wt | 25.0 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +11.4) ⚠ cell-cycle shift, explains ~27% of this change | [[Harringtonine (drug)]] 0.5 µM 0.117× (z -14.2) |
| [[AN3 CA (line)]] | alt | 45.7 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.114× (z -9.4) |
| [[C-33 A (line)]] | alt | 81.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -12.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -8.8) ⚠ cell-cycle shift, explains ~55% of this change |
| [[HT-29 (line)]] | alt | 22.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.205× (z -11.7) |
| [[hTERT-HPNE (line)]] | wt | 15.3 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.120× (z -9.0) |
| [[SNU-1 (line)]] | wt | 32.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0540× (z -16.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -10.5) ⚠ cell-cycle shift, explains ~55% of this change |
| [[SW 900 (line)]] | alt | 16.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +9.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[BT-474 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8602), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPNE2]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[KIF1B]] | +0.60 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SFXN5]] | +0.59 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[MAP4]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[B4GALNT1]] | +0.57 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[KLC1]] | +0.57 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[UFD1]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[DIP2A]] | +0.56 | +0.37 / +0.64 | both halves | 7e-05 |  |
| [[ANKRD23]] | +0.55 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[MAPK9]] | +0.54 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[TANGO2]] | +0.54 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[DONSON]] | +0.53 | +0.50 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01473]] | -0.55 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[TXNIP]] | -0.51 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[PPP1R3B]] | -0.50 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[ELP3]] | -0.50 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[HMG20A]] | -0.50 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[METTL25B]] | -0.49 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[NSMCE1]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[CAAP1]] | -0.48 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[TUT1]] | -0.48 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[TIPARP]] | -0.48 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[TMEM251]] | -0.47 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[SNAPC1]] | -0.47 | -0.36 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SANBR's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TXNIP]] | B | TXNIP activity lowers SANBR's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 1.78× higher at baseline in the lines without TXNIP | 0.080 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.543). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.3, -0.4); signed map (-13.0, 18.7). **Vector** length 93.0, 24.3% of its response variance represented; |z| ≥ 3 in 1,238 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +8.4 | +6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.4 | +5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | +6.4 | +6.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +4.3 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +9.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.3 | +0.5 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +7.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +4.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -5.7 | -10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -4.7 | -14.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.6 | -9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -4.2 | -8.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.6 | -11.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -4.6 |
|  | [[palbociclib (drug)]] 5 µM |  | -1.6 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | SANT and BTB domain regulator of CSR |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p15 — chr2:61,065,871-61,138,034 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1841 |
| Gene groups (HGNC) | Tubulin polyglutamylase complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NSI8](https://www.uniprot.org/uniprotkb/Q6NSI8) (SANT and BTB domain regulator of class switch recombination):

> Negatively regulates class switch recombination or isotype switching in splenic B-cells.

**Summary**, from NCBI Gene [84542](https://www.ncbi.nlm.nih.gov/gene/84542):

> Predicted to enable identical protein binding activity. Predicted to be involved in isotype switching. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29387](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29387) · Entrez [84542](https://www.ncbi.nlm.nih.gov/gene/84542) · UniProt [Q6NSI8](https://www.uniprot.org/uniprotkb/Q6NSI8) · Ensembl [ENSG00000162929](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162929)

## Data

Gene col 8602: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8602); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8602, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8602]; `tensor/DDL_lfc|DDL_z.npy` [8602]; `embed/gene_vectors.npy` [8602]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8602 or target_col == 8602). Every well: [[SANBR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SANBR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
