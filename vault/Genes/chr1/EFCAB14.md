---
symbol: "EFCAB14"
type: "gene"
col: 8266
ensembl_id: "ENSG00000159658"
name: "EF-hand calcium binding domain 14"
location: "1p33"
module: 42
arm: "+"
pooled_cpm: 110.82
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# EFCAB14

*EF-hand calcium binding domain 14* — 1p33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.58× (z +13.6, q 3e-39, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.561× (z -24.3, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GDAP2]] (+0.73, fdr 7e-06), [[TM9SF2]] (+0.71, fdr 7e-06), [[GRB2]] (+0.69, fdr 1e-05); moves opposite to [[PNRC2]] (-0.61, fdr 1e-05), [[COL28A1]] (-0.61, fdr 2e-05), [[CMTR2]] (-0.60, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8266.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.58×** | +13.6 | 3e-39 | 44/48 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.35×** | +8.9 | 1e-16 | 38/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.32×** | +8.2 | 4e-14 | 30/48 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.32×** | +8.2 | 4e-14 | 30/49 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.32×** | +8.0 | 1e-13 | 28/44 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +6.8 | 8e-10 | 33/48 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.17× | +6.7 | 2e-09 | 21/49 (MIA PaCa-2, SW1417, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.22×** | +5.9 | 2e-07 | 24/48 (HEC-1-A, NCI-H2347, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.38×** | +5.0 | 4e-05 | 25/48 (A498, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.21×** | +4.7 | 1e-04 | 23/45 (HEC-1-A, RPMI-7951, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.6 | 3e-04 | 22/45 (LoVo, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.17× | +4.5 | 4e-04 | 22/48 (LoVo, CFPAC-1, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.003 | 11/49 (CFPAC-1, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.14× | +3.8 | 0.007 | 17/48 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.13× | +3.6 | 0.014 | 9/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.074 | 9/48 (J82, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8266.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.561×** | -24.3 | 0e+00 | 43/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.528×** | -18.3 | 0e+00 | 42/48 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.630×** | -13.7 | 1e-40 | 44/48 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.669×** | -10.0 | 2e-21 | 38/48 (NCI-H2347, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.742×** | -8.9 | 8e-17 | 38/48 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.824×** | -8.2 | 3e-14 | 24/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.766×** | -7.9 | 2e-13 | 30/48 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.802×** | -6.6 | 4e-09 | 28/48 (A-427, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.824×** | -5.8 | 5e-07 | 22/48 (HT-29, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | 0.836× | -5.1 | 2e-05 | 21/48 (NCI-H2030, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.826×** | -4.6 | 2e-04 | 23/47 (H4, A549, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.859× | -4.5 | 3e-04 | 15/48 (A-427, hTERT-HPNE, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.833×** | -4.5 | 3e-04 | 22/49 (LoVo, SHP-77, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.863× | -4.4 | 5e-04 | 21/48 (HT-29, Hs 766T, …) | rises with dose | composition shift |
| [[Verteporfin (drug)]] 5 µM |  | 0.864× | -4.2 | 0.001 | 18/49 (HS-578T, A498, …) | top dose only |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | 0.834× | -3.9 | 0.004 | 18/48 (H4, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.884× | -3.7 | 0.008 | 6/48 (LoVo, LS 180, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.849× | -3.5 | 0.016 | 17/48 (hTERT-HPNE, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Elagolix sodium (drug)]] 0.5 µM |  | 0.881× | -3.1 | 0.047 | 8/48 (Panc 03.27, SW 1271, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8266. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 86.7 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.41× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.551× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 109 | 4 (3 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +12.2) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.29× (z +11.9) | [[Harringtonine (drug)]] 0.5 µM 0.450× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 105 | 1 | 5 | [[Panobinostat (drug)]] 0.5 µM 1.87× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -23.4) |
| [[A498 (line)]] | wt | 177 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -17.8) |
| [[LoVo (line)]] | wt | 140 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -20.5) |
| [[PANC-1 (line)]] | alt | 133 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.84× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 1.66× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.660× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 129 | 2 (1 ⚠) | 2 | [[Panobinostat (drug)]] 0.5 µM 2.12× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -20.8) |
| [[H4 (line)]] | wt | 163 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.384× (z -10.4) |
| [[SW1417 (line)]] | alt | 109 | 1 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +10.1) ⚠ cell-cycle shift, explains ~23% of this change | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -20.1) |
| [[HOP62 (line)]] | alt | 97.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.553× (z -12.7) |
| [[HS-578T (line)]] | alt | 149 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.580× (z -11.7) |
| [[LS 180 (line)]] | wt | 145 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 103 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.581× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 81.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -9.5) |
| [[SW480 (line)]] | alt | 108 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 1.58× (z +9.3) | — |
| [[A-172 (line)]] | wt | 87.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -12.3) |
| [[A549 (line)]] | wt | 71.4 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.470× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 125 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -11.8) |
| [[C32 (line)]] | wt | 103 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -14.9) |
| [[Hs 766T (line)]] | wt | 145 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -12.7) |
| [[J82 (line)]] | alt | 111 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -15.6) |
| [[KATO III (line)]] | alt | 132 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.565× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 132 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -17.2) |
| [[SNU-423 (line)]] | alt | 81.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -15.8) |
| [[A-427 (line)]] | wt | 106 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.308× (z -14.0) |
| [[C-33 A (line)]] | alt | 83.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[COLO 205 (line)]] | alt | 116 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.582× (z -9.6) |
| [[HT-29 (line)]] | alt | 121 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 90.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -13.9) |
| [[LOX-IMVI (line)]] | wt | 85.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 1.96× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 121 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 70.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.655× (z -9.8) |
| [[RKO (line)]] | wt | 92.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.274× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 88.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.566× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.345× (z -9.4) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 97.8 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.48× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 94.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.481× (z -9.0) |
| [[AN3 CA (line)]] | alt | 101 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8266), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDAP2]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[TM9SF2]] | +0.71 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[GRB2]] | +0.69 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[IER3IP1]] | +0.67 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[TMED4]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[GLG1]] | +0.66 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[ZCCHC17]] | +0.65 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[STRAP]] | +0.65 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[NSDHL]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[NOMO2]] | +0.65 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[DDB1]] | +0.65 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[SAR1A]] | +0.65 | +0.69 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNRC2]] | -0.61 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[COL28A1]] | -0.61 | -0.64 / -0.46 | both halves | 2e-05 |  |
| [[CMTR2]] | -0.60 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[NEPRO-AS1]] | -0.60 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[ANGPT2]] | -0.59 | -0.61 / -0.39 | both halves | 5e-05 |  |
| [[NANOS3]] | -0.58 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[RBM26-AS1]] | -0.58 | -0.67 / -0.38 | both halves | 7e-05 |  |
| [[MAPK1IP1L]] | -0.58 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ZNF518A]] | -0.57 | -0.60 / -0.36 | both halves | 9e-05 |  |
| [[PATL2]] | -0.57 | -0.64 / -0.38 | both halves | 6e-05 |  |
| [[ZNF462]] | -0.57 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[PLA2G4C]] | -0.57 | -0.57 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers EFCAB14's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.697). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.3, -30.4); signed map (-50.0, -4.6). **Vector** length 128, 35.9% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.2 | +13.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +5.9 | +8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +5.6 | +6.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +5.3 | +5.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.3 | +8.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.4 | +5.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.4 | +2.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -12.3 | -18.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -10.7 | -13.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -9.3 | -24.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.3 | -10.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.4 | -8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.1 | -8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.1 | -6.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.8 | -4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.3 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | EF-hand calcium binding domain 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p33 — chr1:46,674,659-46,719,146 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0494 |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

UniProt [O75071](https://www.uniprot.org/uniprotkb/O75071) carries no function annotation.

**Summary**, from NCBI Gene [9813](https://www.ncbi.nlm.nih.gov/gene/9813):

> Predicted to enable calcium ion binding activity. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29051](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29051) · Entrez [9813](https://www.ncbi.nlm.nih.gov/gene/9813) · UniProt [O75071](https://www.uniprot.org/uniprotkb/O75071) · Ensembl [ENSG00000159658](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159658)

## Data

Gene col 8266: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8266); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8266, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8266]; `tensor/DDL_lfc|DDL_z.npy` [8266]; `embed/gene_vectors.npy` [8266]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8266 or target_col == 8266). Every well: [[EFCAB14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFCAB14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
