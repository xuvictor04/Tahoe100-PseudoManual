---
symbol: "BIRC2"
type: "gene"
col: 3130
ensembl_id: "ENSG00000110330"
name: "baculoviral IAP repeat containing 2"
location: "11q22.2"
module: 14
arm: "+"
pooled_cpm: 163.21
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# BIRC2

*baculoviral IAP repeat containing 2* — 11q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.01× (z +22.0, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.572× (z -12.5, q 3e-33, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFKB1]] (+0.65, fdr 1e-05), [[HIVEP2]] (+0.65, fdr 1e-05), [[BIRC3]] (+0.64, fdr 7e-06, ⚠ same locus), [[NFKB2]] (+0.60, fdr 1e-05); moves opposite to [[SS18L1]] (-0.57, fdr 1e-05), [[TNPO3]] (-0.57, fdr 2e-05), [[NFATC3]] (-0.56, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TNFAIP3]] → it (grade C ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3130.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.01×** | +22.0 | 0e+00 | 44/48 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.30×** | +17.9 | 0e+00 | 46/48 (RPMI-7951, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.79×** | +13.1 | 1e-36 | 45/48 (C32, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +12.7 | 1e-34 | 45/48 (HS-578T, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +11.3 | 1e-27 | 42/48 (LoVo, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +9.0 | 2e-17 | 40/48 (SNU-1, SW48, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +8.7 | 3e-16 | 39/48 (SW48, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +8.6 | 4e-16 | 32/45 (PANC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +8.3 | 6e-15 | 37/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +8.3 | 6e-15 | 39/49 (PANC-1, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +7.1 | 8e-11 | 32/48 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.36×** | +6.3 | 1e-08 | 36/47 (SNU-1, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.63×** | +5.7 | 4e-07 | 24/38 (HS-578T, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.27×** | +5.4 | 3e-06 | 29/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.18× | +3.7 | 0.009 | 19/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.6 | 0.011 | 12/49 (C32, SNU-1, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.18× | +3.5 | 0.017 | 18/48 (HS-578T, NCI-H2030, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3130.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.572×** | -12.5 | 3e-33 | 36/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.719×** | -10.4 | 4e-23 | 35/49 (RKO, PANC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.638×** | -9.8 | 3e-20 | 34/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.651×** | -9.6 | 8e-20 | 36/48 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.700×** | -7.6 | 4e-12 | 34/48 (H4, PANC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.709×** | -7.4 | 1e-11 | 26/44 (SK-MEL-2, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.724×** | -7.2 | 3e-11 | 32/48 (NCI-H23, HT-29, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.650×** | -5.0 | 3e-05 | 32/45 (H4, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.802×** | -5.0 | 4e-05 | 27/48 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.796×** | -4.9 | 5e-05 | 26/47 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.808×** | -4.6 | 2e-04 | 27/48 (AsPC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.815×** | -4.6 | 2e-04 | 24/49 (HOP62, A-172, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.681×** | -4.5 | 3e-04 | 22/47 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.828×** | -4.2 | 9e-04 | 24/49 (RKO, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.887× | -3.8 | 0.005 | 18/48 (HEC-1-A, HOP62, …) | top dose only | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.866× | -3.2 | 0.039 | 18/48 (C32, A-427, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.868× | -3.1 | 0.059 | 15/48 (A-427, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3130. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 425 | 9 (2 ⚠) | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +15.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -18.5) |
| [[RKO (line)]] | wt | 239 | 0 | 12 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -19.6) |
| [[H4 (line)]] | wt | 224 | 2 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -16.1) |
| [[A549 (line)]] | wt | 193 | 5 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +16.6) | [[Panobinostat (drug)]] 5 µM 0.288× (z -13.9) |
| [[C32 (line)]] | wt | 234 | 6 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +17.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -10.4) |
| [[LoVo (line)]] | wt | 85.5 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +21.5) | — |
| [[HOP62 (line)]] | alt | 148 | 5 (2 ⚠) | 3 | [[Harringtonine (drug)]] 5 µM 3.53× (z +14.6) | [[Panobinostat (drug)]] 5 µM 0.407× (z -10.9) |
| [[A-172 (line)]] | wt | 175 | 4 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.343× (z -11.4) |
| [[HS-578T (line)]] | alt | 153 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +18.7) | — |
| [[SW48 (line)]] | wt | 125 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +14.0) | — |
| [[hTERT-HPNE (line)]] | wt | 138 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +17.5) | — |
| [[SW 900 (line)]] | alt | 101 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.2) | — |
| [[A-427 (line)]] | wt | 378 | 3 | 2 | [[Harringtonine (drug)]] 0.5 µM 2.42× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.465× (z -9.9) |
| [[KATO III (line)]] | alt | 153 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +12.6) | — |
| [[NCI-H1573 (line)]] | alt | 175 | 1 (1 ⚠) | 4 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.15× (z +8.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.345× (z -12.3) |
| [[A498 (line)]] | wt | 127 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +14.9) | — |
| [[LOX-IMVI (line)]] | wt | 167 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.377× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 159 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +15.6) | — |
| [[NCI-H23 (line)]] | alt | 232 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.311× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 130 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.462× (z -9.9) |
| [[Hs 766T (line)]] | wt | 173 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -12.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 110 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 324 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.344× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.371× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 137 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.9) | — |
| [[Panc 03.27 (line)]] | alt | 118 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.8) | — |
| [[RPMI-7951 (line)]] | alt | 133 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 5.10× (z +17.7) | — |
| [[SNU-1 (line)]] | wt | 113 | 3 | 0 | [[Harringtonine (drug)]] 0.5 µM 4.64× (z +9.8) | — |
| [[SW1417 (line)]] | alt | 110 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +18.5) | — |
| [[BT-474 (line)]] | alt | 134 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.2) | — |
| [[J82 (line)]] | alt | 91.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +14.6) | — |
| [[LS 180 (line)]] | wt | 87.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.9) | — |
| [[SK-MEL-2 (line)]] | alt | 82.2 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.63× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -18.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 164 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +18.7) | — |
| [[C-33 A (line)]] | alt | 81.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.408× (z -8.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 143 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +14.2) | — |
| [[CHP-212 (line)]] | wt | 166 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 128 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 134 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 195 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.64× (z +11.0) | — |
| [[SW480 (line)]] | alt | 94.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 102 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 296 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3130), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKB1]] | +0.65 | +0.52 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 773 |
| [[HIVEP2]] | +0.65 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[BIRC3]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 996; ⚠ same locus (7.8 kb, same strand: neighbours can correlate without regulation) |
| [[NFKB2]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 748 |
| [[TNFAIP3]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 931 |
| [[VEZF1]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[IL6ST]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[GCA]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[NHLRC2]] | +0.57 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[NUAK2]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[TNIP1]] | +0.56 | +0.42 / +0.62 | both halves | 4e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 446 |
| [[ZNF217]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 | pathway: Adherens junctions interactions |
| [[FAM111A]] | +0.56 | +0.48 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SS18L1]] | -0.57 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[TNPO3]] | -0.57 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[NFATC3]] | -0.56 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[MBOAT7]] | -0.55 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[ANKRD39]] | -0.54 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[FTL]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[UBE4B]] | -0.54 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[TPST2]] | -0.53 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[CMTM8]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[UBE2R2]] | -0.53 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SAP130]] | -0.52 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[SDHAP2]] | -0.52 | -0.39 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFAIP3]] | C | TNFAIP3 activity lowers BIRC2's level | lines that do not express TNFAIP3 (3) vs lines expressing it (47) | 1.40× higher at baseline in the lines without TNFAIP3 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IER3, JAG1, ATXN1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | BIRC2's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | BIRC2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.57 | 0.500 over the table, 0.085 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.529). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.7, 9.3); signed map (17.3, -8.9). **Vector** length 116, 36.6% of its response variance represented; |z| ≥ 3 in 1,462 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NF-kB* (control, mean cos +0.52 to 12); *IkBA variant leads to EDA-ID* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +9.5 | +13.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.3 | +12.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.8 | +17.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.7 | +9.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +22.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.1 | +6.3 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | +2.0 | +2.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.7 | +0.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | -9.4 | -7.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -9.2 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.4 | -7.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | -6.6 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.9 | -0.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -5.3 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | +2.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.6 | +1.5 |

## What is on record

|  |  |
|---|---|
| Name | baculoviral IAP repeat containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.2 — chr11:102,347,211-102,378,670 (+) |
| Ensembl biotype | protein_coding |
| Also known as | cIAP1, hiap-2, MIHB, RNF48, c-IAP1; previously API1 |
| Gene groups (HGNC) | Ring finger proteins; Baculoviral IAP repeat containing; Caspase recruitment domain containing; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 32 pathways, smallest: TNF receptor superfamily (TNFSF) members mediating non-canonical NF-kB pathway; TICAM1, RIP1-mediated IKK complex recruitment; IKK complex recruitment mediated by RIP1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13490](https://www.uniprot.org/uniprotkb/Q13490) (Baculoviral IAP repeat-containing protein 2):

> Multi-functional protein which regulates not only caspases and apoptosis, but also modulates inflammatory signaling and immunity, mitogenic kinase signaling, and cell proliferation, as well as cell invasion and metastasis. Acts as an E3 ubiquitin-protein ligase regulating NF-kappa-B signaling. Regulates both canonical and non-canonical NF-kappa-B signaling by acting in opposite directions: acts as a positive regulator of the canonical pathway and suppresses constitutive activation of …

**Summary**, from NCBI Gene [329](https://www.ncbi.nlm.nih.gov/gene/329):

> The protein encoded by this gene is a member of a family of proteins that inhibits apoptosis by binding to tumor necrosis factor receptor-associated factors TRAF1 and TRAF2, probably by interfering with activation of ICE-like proteases. This encoded protein inhibits apoptosis induced by serum deprivation and menadione, a potent inducer of free radicals. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:590](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:590) · Entrez [329](https://www.ncbi.nlm.nih.gov/gene/329) · UniProt [Q13490](https://www.uniprot.org/uniprotkb/Q13490) · Ensembl [ENSG00000110330](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110330)

## Data

Gene col 3130: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3130); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3130, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3130]; `tensor/DDL_lfc|DDL_z.npy` [3130]; `embed/gene_vectors.npy` [3130]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3130 or target_col == 3130). Every well: [[BIRC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BIRC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
