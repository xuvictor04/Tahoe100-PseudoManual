---
symbol: "KLHL25"
type: "gene"
col: 11430
ensembl_id: "ENSG00000183655"
name: "kelch like family member 25"
location: "15q25.3"
module: 72
arm: "+"
pooled_cpm: 9.76
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# KLHL25

*kelch like family member 25* — 15q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 4.02× (z +19.4, q 0e+00, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.545× (z -8.5, q 1e-14, down in 25 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Sulfatinib (drug)]] 5 µM: 0.766× (z -3.6, q 0.045, down in 10 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (LS 180 0.0586×, SW1417 0.148×, A549 0.110×, NCI-H1573 0.170×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H2347 0.0689×, A498 0.129×, LS 180 0.184×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LS 180 0.123×, NCI-H2030 0.167×; ⚠ toxic; transcription drop); [[BAY1125976 (drug)]] 0.05 µM in 1 line (Hs 766T 0.0555×); [[Ritonavir (drug)]] 0.5 µM in 1 line (NCI-H460 0.186×); [[Erlotinib (drug)]] 0.5 µM in 1 line (HCT15 0.0473×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MBOAT7]] (+0.67, fdr 8e-06), [[SPINDOC]] (+0.66, fdr 1e-05), [[SS18L1]] (+0.66, fdr 1e-05); moves opposite to [[GOPC]] (-0.66, fdr 1e-05), [[RAD50]] (-0.64, fdr 1e-05), [[CHURC1]] (-0.63, fdr 1e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP3K9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11430.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **4.02×** | +19.4 | 0e+00 | 42/46 (LoVo, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.99×** | +19.3 | 0e+00 | 46/47 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **3.59×** | +17.8 | 0e+00 | 44/47 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **3.58×** | +17.8 | 0e+00 | 45/47 (LoVo, SW1417, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.41×** | +17.3 | 0e+00 | 35/43 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.60×** | +13.3 | 2e-38 | 36/47 (SW1417, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.34×** | +11.9 | 2e-30 | 41/47 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.25×** | +10.7 | 7e-25 | 34/45 (SW1417, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.04×** | +9.9 | 2e-21 | 32/45 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.51×** | +9.2 | 3e-18 | 24/30 (SW1417, A498, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.87×** | +8.4 | 3e-15 | 22/41 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.30×** | +8.3 | 6e-15 | 29/46 (A498, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.77×** | +8.0 | 7e-14 | 28/47 (SW1417, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.76×** | +7.6 | 2e-12 | 24/39 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +7.0 | 7e-11 | 19/41 (CFPAC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +6.1 | 3e-08 | 20/47 (HT-29, SW1417, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.15×** | +5.6 | 7e-07 | 16/47 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +5.4 | 2e-06 | 20/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Infigratinib (drug)]] 5 µM |  | **2.04×** | +5.2 | 5e-06 | 10/43 (A549, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +5.1 | 1e-05 | 19/47 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.007 | 6/47 (NCI-H460, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11430.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (LS 180 0.0586×, SW1417 0.148×, A549 0.110×, NCI-H1573 0.170×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H2347 0.0689×, A498 0.129×, LS 180 0.184×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LS 180 0.123×, NCI-H2030 0.167×; ⚠ toxic; transcription drop); [[BAY1125976 (drug)]] 0.05 µM in 1 line (Hs 766T 0.0555×); [[Ritonavir (drug)]] 0.5 µM in 1 line (NCI-H460 0.186×); [[Erlotinib (drug)]] 0.5 µM in 1 line (HCT15 0.0473×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.545×** | -8.5 | 1e-14 | 25/34 (LS 180, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.657×** | -5.4 | 1e-05 | 15/26 (LS 180, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.733×** | -4.2 | 0.005 | 6/17 (NCI-H2347, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Sulfatinib (drug)]] 5 µM |  | **0.766×** | -3.6 | 0.045 | 10/46 (AN3 CA, PANC-1, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.855× | -3.1 | 0.18 | 12/46 (hTERT-HPNE, NCI-H1792, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.856× | -3.1 | 0.18 | 9/48 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.805× | -3.0 | 0.19 | 5/47 (A-172, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.66 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11430. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 13.3 | 4 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.57× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.129× (z -10.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 17.5 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 6.49× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -11.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 15.3 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.62× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 19.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0586× (z -15.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 8.72 | 1 (1 ⚠) | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 5.06× (z +8.5) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 5 µM 0.0689× (z -13.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 7.65 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.98× (z +10.6) | — |
| [[A549 (line)]] | wt | 10.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -11.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 12.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.64× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 11.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 5.66 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.66× (z +11.6) | [[Ritonavir (drug)]] 0.5 µM 0.186× (z -9.1) |
| [[A-172 (line)]] | wt | 7.19 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.59× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 9.18 | 1 | 0 | [[Auranofin (drug)]] 5 µM 12.1× (z +9.9) | — |
| [[C32 (line)]] | wt | 6.84 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0864× (z -8.9) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 5.40 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.83× (z +8.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[COLO 205 (line)]] | alt | 6.98 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 15.3× (z +9.3) ⚠ toxic; cell-cycle shift, explains ~31% of this change | — |
| [[HCT15 (line)]] | alt | 5.81 | 0 | 1 | — | [[Erlotinib (drug)]] 0.5 µM 0.0473× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 8.27 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.65× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 13.3 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.109× (z -8.6) |
| [[Hs 766T (line)]] | wt | 4.48 | 0 | 1 | — | [[BAY1125976 (drug)]] 0.05 µM 0.0555× (z -9.3) |
| [[HT-29 (line)]] | alt | 15.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.85× (z +11.5) | — |
| [[LOX-IMVI (line)]] | wt | 8.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -10.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11430), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBOAT7]] | +0.67 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[SPINDOC]] | +0.66 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[SS18L1]] | +0.66 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[INPP5A]] | +0.66 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[NFATC3]] | +0.65 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[ABHD3]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[ANKRD39]] | +0.59 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[CACYBP]] | +0.59 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[SLC27A4]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CCDC134]] | +0.58 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[TSPAN9]] | +0.57 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[PACC1]] | +0.57 | +0.63 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOPC]] | -0.66 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[RAD50]] | -0.64 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[CHURC1]] | -0.63 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[TRMT13]] | -0.59 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[SLC25A46]] | -0.58 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[ZNF252P-1]] | -0.57 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[DARS1]] | -0.57 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[METTL25B]] | -0.56 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[TIMM9]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[USP40]] | -0.55 | -0.57 / -0.37 | both halves | 7e-05 |  |
| [[RIPK2-DT]] | -0.55 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[CHMP4A]] | -0.55 | -0.45 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP3K9]] | B | MAP3K9 activity raises KLHL25's level | lines that do not express MAP3K9 (8) vs lines expressing it (42) | 1.59× lower at baseline in the lines without MAP3K9 | 0.031 | ⚠ within organs, on part of the lines; also absent: CDKN1C, DAPK2, PRKCZ; maybe low, not absent |
| [[MFAP3L]] | B | MFAP3L activity raises KLHL25's level | lines that do not express MFAP3L (9) vs lines expressing it (41) | 1.44× lower at baseline in the lines without MFAP3L | 0.054 | ⚠ within organs, on part of the lines; also absent: CRACD, FILIP1, TSPAN33; maybe low, not absent |
| [[RBMS3]] | B | RBMS3 activity lowers KLHL25's level | lines that do not express RBMS3 (19) vs lines expressing it (31) | 1.53× higher at baseline in the lines without RBMS3 | 0.057 | ⚠ within organs, on part of the lines; also absent: RFTN1, PYGO1, LINC00472 |
| [[B4GALNT1]] | B | B4GALNT1 activity weakens KLHL25's drug response | lines that do not express B4GALNT1 (16) vs lines expressing it (32) | the lines without B4GALNT1 respond 1.34× as strongly (z diff -0.95); strongest at Ixazomib citrate 5 µM: 3.53x vs 1.91x (z diff -2.6) | 0.094 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.534). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.3, -6.7); signed map (-43.4, 3.3). **Vector** length 72.0, 13.3% of its response variance represented; |z| ≥ 3 in 1,241 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.3 | +19.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.3 | +9.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.2 | +13.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.8 | +10.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +6.1 |
|  | [[Infigratinib (drug)]] 5 µM |  | +1.5 | +5.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | +2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.7 | +7.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -0.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | +1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.4 | -3.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.3 — chr15:85,759,326-85,794,925 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12587, ENC2, ENC-2 |
| Gene groups (HGNC) | Kelch like; BTB domain containing; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0H3](https://www.uniprot.org/uniprotkb/Q9H0H3) (Kelch-like protein 25):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin ligase complex involved in various processes, such as translation homeostasis and lipid synthesis. The BCR(KLHL25) ubiquitin ligase complex acts by mediating ubiquitination of hypophosphorylated EIF4EBP1 (4E-BP1): ubiquitination and subsequent degradation of hypophosphorylated EIF4EBP1 (4E-BP1) probably serves as a homeostatic mechanism to maintain translation and prevent eIF4E inhibition when eIF4E levels are low. The BCR(KLHL25) …

**Summary**, from NCBI Gene [64410](https://www.ncbi.nlm.nih.gov/gene/64410):

> Enables ubiquitin-like ligase-substrate adaptor activity. Involved in several processes, including positive regulation of CD4-positive, CD25-positive, alpha-beta regulatory T cell differentiation; protein ubiquitination; and regulation of fatty acid metabolic process. Located in cytoplasm. Part of Cul3-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25732](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25732) · Entrez [64410](https://www.ncbi.nlm.nih.gov/gene/64410) · UniProt [Q9H0H3](https://www.uniprot.org/uniprotkb/Q9H0H3) · Ensembl [ENSG00000183655](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183655)

## Data

Gene col 11430: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11430); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11430, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11430]; `tensor/DDL_lfc|DDL_z.npy` [11430]; `embed/gene_vectors.npy` [11430]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11430 or target_col == 11430). Every well: [[KLHL25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
