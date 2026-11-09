---
symbol: "ATF7IP"
type: "gene"
col: 10147
ensembl_id: "ENSG00000171681"
name: "activating transcription factor 7 interacting protein"
location: "12p13.1"
module: 143
arm: "+"
pooled_cpm: 89.78
n_lines_expressing: 49
n_dd_up: 27
n_dd_down: 6
n_dd_up_clean: 21
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# ATF7IP

*activating transcription factor 7 interacting protein* — 12p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.41× (z +25.1, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[PF-06260933 (drug)]] 5 µM: 0.467× (z -6.0, q 6e-07, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HYLS1]] (+0.68, fdr 7e-06), [[ZNF280D]] (+0.67, fdr 1e-05), [[STAG1]] (+0.67, fdr 1e-05); moves opposite to [[BET1L]] (-0.67, fdr 8e-06), [[LCMT1]] (-0.67, fdr 1e-05), [[RARS2]] (-0.66, fdr 1e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MBNL1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10147.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.41×** | +25.1 | 0e+00 | 46/47 (NCI-H2030, RKO, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.83×** | +15.2 | 0e+00 | 46/47 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.44×** | +13.5 | 4e-39 | 42/47 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.99×** | +10.4 | 2e-23 | 43/47 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +9.9 | 5e-21 | 41/47 (Panc 03.27, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.81×** | +9.0 | 2e-17 | 37/47 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +8.0 | 1e-13 | 33/47 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +7.5 | 5e-12 | 37/47 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +5.9 | 2e-07 | 38/48 (Panc 03.27, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +5.5 | 2e-06 | 31/47 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.91×** | +5.1 | 2e-05 | 38/46 (RKO, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +5.1 | 2e-05 | 26/47 (HOP62, Panc 03.27, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.74×** | +4.4 | 5e-04 | 27/48 (NCI-H2030, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.3 | 8e-04 | 22/47 (A-172, HEC-1-A, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.001 | 27/46 (C-33 A, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.32×** | +4.0 | 0.002 | 24/46 (Panc 03.27, SK-MEL-2, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.003 | 27/47 (LoVo, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10147.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PF-06260933 (drug)]] 5 µM |  | **0.467×** | -6.0 | 6e-07 | 36/47 (A549, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.674×** | -6.0 | 6e-07 | 33/47 (SNU-423, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.696×** | -5.5 | 7e-06 | 28/47 (SK-MEL-2, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.752×** | -4.3 | 0.002 | 26/47 (SK-MEL-2, SNU-423, …) | rises with dose |  |
| [[Ciclopirox (drug)]] 5 µM |  | 0.837× | -3.8 | 0.015 | 20/47 (LOX-IMVI, C-33 A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.777×** | -3.7 | 0.022 | 25/49 (LS 180, SK-MEL-2, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.741×** | -3.3 | 0.091 | 20/47 (HEC-1-A, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10147. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 56.5 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +18.5) | — |
| [[LOX-IMVI (line)]] | wt | 148 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +18.1) | [[Lonafarnib (drug)]] 5 µM 0.0364× (z -18.9) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 166 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -12.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.463× (z -8.8) |
| [[SW 900 (line)]] | alt | 97.4 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +18.9) | — |
| [[BT-474 (line)]] | alt | 90.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +15.8) | — |
| [[HEC-1-A (line)]] | alt | 157 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +19.4) | — |
| [[hTERT-HPNE (line)]] | wt | 86.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +14.3) | — |
| [[LS 180 (line)]] | wt | 114 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.2) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -9.7) ⚠ cell-cycle shift, explains ~24% of this change |
| [[KATO III (line)]] | alt | 125 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +13.8) | — |
| [[NCI-H2030 (line)]] | alt | 93.2 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +23.5) | [[Panobinostat (drug)]] 5 µM 0.418× (z -9.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H2347 (line)]] | alt | 115 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +17.5) | [[Panobinostat (drug)]] 0.5 µM 0.414× (z -9.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H460 (line)]] | wt | 82.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +19.8) | — |
| [[RKO (line)]] | wt | 106 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.68× (z +22.1) | — |
| [[A-427 (line)]] | wt | 74.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[COLO 205 (line)]] | alt | 97.2 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.25× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0924× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change |
| [[HepG2_C3A (line)]] | wt | 55.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +11.0) | — |
| [[LoVo (line)]] | wt | 81.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +16.4) | — |
| [[Panc 03.27 (line)]] | alt | 191 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +16.7) | — |
| [[SW48 (line)]] | wt | 112 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +13.0) | — |
| [[A-172 (line)]] | wt | 47.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +18.0) | — |
| [[A549 (line)]] | wt | 40.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +21.9) | — |
| [[C32 (line)]] | wt | 93.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[HT-29 (line)]] | alt | 58.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +12.8) | — |
| [[J82 (line)]] | alt | 99.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +18.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 126 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.27× (z +10.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.243× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~66% of this change |
| [[PANC-1 (line)]] | alt | 41.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +18.0) | — |
| [[SNU-1 (line)]] | wt | 51.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +11.8) | — |
| [[SNU-423 (line)]] | alt | 121 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +15.9) | [[Panobinostat (drug)]] 0.5 µM 0.406× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.438× (z -8.9) |
| [[SW1417 (line)]] | alt | 129 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +16.1) | — |
| [[A498 (line)]] | wt | 66.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +14.7) | — |
| [[CFPAC-1 (line)]] | alt | 40.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +13.1) | — |
| [[HS-578T (line)]] | alt | 71.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +13.8) | — |
| [[NCI-H1792 (line)]] | alt | 71.3 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 3.72× (z +11.5) | — |
| [[NCI-H661 (line)]] | alt | 178 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0959× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[RPMI-7951 (line)]] | alt | 119 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[SW480 (line)]] | alt | 146 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 40.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +12.5) | — |
| [[HCT15 (line)]] | alt | 43.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 61.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +15.9) | — |
| [[NCI-H23 (line)]] | alt | 64.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +14.2) | — |
| [[AN3 CA (line)]] | alt | 166 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 246 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10147), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HYLS1]] | +0.68 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[ZNF280D]] | +0.67 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[STAG1]] | +0.67 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[ZNF644]] | +0.66 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[USP13]] | +0.66 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[TCF12]] | +0.65 | +0.68 / +0.46 | both halves | 3e-05 |  |
| [[VEZF1]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[HNRNPH2]] | +0.65 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ZNF776]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[HNRNPK]] | +0.64 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[ZNF260]] | +0.63 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[FAM111A]] | +0.63 | +0.68 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BET1L]] | -0.67 | -0.68 / -0.57 | both halves | 8e-06 |  |
| [[LCMT1]] | -0.67 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[RARS2]] | -0.66 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[DNAJC5]] | -0.65 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[MPG]] | -0.64 | -0.69 / -0.48 | both halves | 2e-05 |  |
| [[EEF1AKMT4]] | -0.64 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[PDIA5]] | -0.63 | -0.72 / -0.42 | both halves | 4e-05 |  |
| [[ZCCHC17]] | -0.63 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[TMEM120B]] | -0.62 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[TXNDC11]] | -0.62 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[FBH1]] | -0.62 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[GUK1]] | -0.62 | -0.61 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ATF7IP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MBNL1]] | C | ATF7IP's natural level strengthens MBNL1's drug response | ATF7IP's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.03; direction not clear | 0.094 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.662). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.4, 2.7); signed map (13.5, -32.7). **Vector** length 143, 45.9% of its response variance represented; |z| ≥ 3 in 1,174 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.1 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.8 | +25.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.7 | +15.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.8 | +5.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +8.5 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.6 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +5.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +5.0 | +3.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -6.0 | -6.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.0 | -5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.9 | -4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.2 | -2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -4.2 | -6.0 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -2.9 | -2.3 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.8 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | activating transcription factor 7 interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.1 — chr12:14,365,676-14,502,931 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10688, p621, ATF7IP1, MCAF1, MCAF, AM |
| Gene groups (HGNC) | Fibronectin type III domain containing |
| Reactome | 7 pathways, smallest: Regulation of endogenous retroelements by the Human Silencing Hub (HUSH) complex; PKMTs methylate histone lysines; Regulation of endogenous retroelements by KRAB-ZFP proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6VMQ6](https://www.uniprot.org/uniprotkb/Q6VMQ6) (Activating transcription factor 7-interacting protein 1):

> Recruiter that couples transcriptional factors to general transcription apparatus and thereby modulates transcription regulation and chromatin formation. Can both act as an activator or a repressor depending on the context. Required for HUSH-mediated heterochromatin formation and gene silencing. Mediates MBD1-dependent transcriptional repression, probably by recruiting complexes containing SETDB1. Stabilizes SETDB1, is required to stimulate histone methyltransferase activity of SETDB1 and …

**Summary**, from NCBI Gene [55729](https://www.ncbi.nlm.nih.gov/gene/55729):

> ATF7IP is a multifunctional nuclear protein that associates with heterochromatin. It can act as a transcriptional coactivator or corepressor depending upon its binding partners (summary by Liu et al., 2009 [PubMed 19106100]).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:20092](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20092) · Entrez [55729](https://www.ncbi.nlm.nih.gov/gene/55729) · UniProt [Q6VMQ6](https://www.uniprot.org/uniprotkb/Q6VMQ6) · Ensembl [ENSG00000171681](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171681)

## Data

Gene col 10147: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10147); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10147, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10147]; `tensor/DDL_lfc|DDL_z.npy` [10147]; `embed/gene_vectors.npy` [10147]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10147 or target_col == 10147). Every well: [[ATF7IP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATF7IP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
