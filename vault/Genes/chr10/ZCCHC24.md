---
symbol: "ZCCHC24"
type: "gene"
col: 9119
ensembl_id: "ENSG00000165424"
name: "zinc finger CCHC-type containing 24"
location: "10q22.3"
module: 136
arm: "+"
pooled_cpm: 21.54
n_lines_expressing: 45
n_dd_up: 17
n_dd_down: 14
n_dd_up_clean: 14
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 13
direction_downstream: 11
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# ZCCHC24

*zinc finger CCHC-type containing 24* — 10q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.94× (z +26.4, q 0e+00, up in 41 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.217× (z -15.4, q 0e+00, down in 36 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDLIM7]] (+0.70, fdr 7e-06), [[EFR3B]] (+0.60, fdr 2e-05), [[ECE1]] (+0.60, fdr 3e-05); moves opposite to [[MRRF]] (-0.62, fdr 1e-05), [[TBCEL]] (-0.56, fdr 4e-05), [[LDAH]] (-0.54, fdr 8e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[TIMP3]] → it (grade B ⚠); 11 go from it, the strongest it → [[PLP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9119.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.94×** | +26.4 | 0e+00 | 41/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.63×** | +24.9 | 0e+00 | 40/43 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.30×** | +23.0 | 0e+00 | 39/43 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +19.1 | 0e+00 | 29/42 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.14×** | +14.7 | 0e+00 | 37/43 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.71×** | +14.7 | 0e+00 | 35/43 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.65×** | +9.7 | 3e-20 | 24/42 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.55×** | +9.4 | 3e-19 | 32/43 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.56×** | +8.6 | 5e-16 | 27/43 (NCI-H460, PANC-1, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.14×** | +7.6 | 1e-12 | 26/41 (SW480, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +6.7 | 1e-09 | 19/43 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.41×** | +6.4 | 8e-09 | 19/41 (NCI-H460, RKO, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.28×** | +4.3 | 7e-04 | 11/43 (CFPAC-1, SW480, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.3 | 7e-04 | 15/42 (LoVo, CFPAC-1, …) | top dose only | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.23×** | +3.8 | 0.005 | 14/42 (NCI-H460, SW480, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.008 | 16/42 (H4, hTERT-HPNE, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.013 | 15/42 (H4, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.032 | 1/43 (SW480) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9119.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.217×** | -15.4 | 0e+00 | 36/43 (HOP62, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.307×** | -11.9 | 2e-30 | 31/42 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.616×** | -9.4 | 1e-18 | 23/43 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.420×** | -8.8 | 3e-16 | 20/29 (C32, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.661×** | -7.4 | 2e-11 | 24/43 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.696×** | -6.8 | 1e-09 | 20/39 (LoVo, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.725×** | -6.2 | 4e-08 | 19/43 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.739×** | -5.9 | 3e-07 | 23/42 (H4, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.741×** | -5.6 | 1e-06 | 18/43 (C32, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.763×** | -5.2 | 9e-06 | 21/43 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.782×** | -4.8 | 9e-05 | 18/43 (A-172, C32, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.801×** | -4.3 | 8e-04 | 20/43 (SW 900, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -4.3 | 8e-04 | 15/43 (SK-MEL-2, RPMI-7951, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.813×** | -4.0 | 0.002 | 16/41 (A-172, SK-MEL-2, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.823×** | -3.8 | 0.006 | 15/42 (hTERT-HPNE, RPMI-7951, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.876× | -3.7 | 0.009 | 11/43 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.835× | -3.4 | 0.024 | 12/43 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.887× | -3.3 | 0.029 | 7/43 (SW 1271, A-427, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.840× | -3.1 | 0.047 | 10/41 (SNU-1, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[5-Fluorouracil (drug)]] 5 µM |  | 0.859× | -3.0 | 0.076 | 2/43 (RKO, PANC-1) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9119. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 85.2 | 0 | 9 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.154× (z -18.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0392× (z -16.9) |
| [[NCI-H460 (line)]] | wt | 17.5 | 6 (2 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.169× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.321× (z -9.8) |
| [[SW480 (line)]] | alt | 26.5 | 5 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.80× (z +14.8) | [[Lonafarnib (drug)]] 5 µM 0.105× (z -13.0) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.124× (z -12.0) |
| [[A-172 (line)]] | wt | 68.0 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -17.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.341× (z -11.3) |
| [[A498 (line)]] | wt | 24.4 | 4 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +16.4) | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.165× (z -8.5) |
| [[LoVo (line)]] | wt | 9.93 | 5 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +11.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0964× (z -14.1) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 12.4 | 5 | 1 | [[Panobinostat (drug)]] 5 µM 6.67× (z +10.7) | [[TAK-901 (drug)]] 5 µM 0.0369× (z -9.7) |
| [[PANC-1 (line)]] | alt | 7.74 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 10.3× (z +13.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.205× (z -9.4) |
| [[H4 (line)]] | wt | 52.6 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0951× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0321× (z -11.7) |
| [[HOP62 (line)]] | alt | 77.7 | 0 | 5 (3 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0726× (z -13.4) |
| [[RPMI-7951 (line)]] | alt | 66.6 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.148× (z -13.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0675× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 49.4 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 11.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.97× (z +15.8) | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.81× (z +10.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.58 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.45× (z +11.2) | — |
| [[Panc 03.27 (line)]] | alt | 16.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.33× (z +11.4) | — |
| [[SNU-423 (line)]] | alt | 27.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.45× (z +12.9) | — |
| [[A-427 (line)]] | wt | 12.2 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0702× (z -14.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HEC-1-A (line)]] | alt | 11.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +9.1) | [[PH-797804 (drug)]] 5 µM 0.0546× (z -9.7) |
| [[Hs 766T (line)]] | wt | 13.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.25× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 31.7 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0567× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 38.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.08× (z +9.5) | — |
| [[RKO (line)]] | wt | 10.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.84× (z +12.1) | [[Digitoxin (drug)]] 5 µM 0.0953× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 37.2 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0829× (z -11.5) |
| [[SW1417 (line)]] | alt | 8.67 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.98× (z +10.3) | — |
| [[CHP-212 (line)]] | wt | 65.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -9.3) ⚠ cell-cycle shift, explains ~53% of this change |
| [[HepG2_C3A (line)]] | wt | 26.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.17× (z +8.9) | — |
| [[KATO III (line)]] | alt | 7.26 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.99× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 39.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.00× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 6.77 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.38× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 6.62 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0590× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 18.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.63× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 35.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.278× (z -8.8) ⚠ toxic |
| [[SW48 (line)]] | wt | 17.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.29 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.51 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9119), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDLIM7]] | +0.70 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[EFR3B]] | +0.60 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[ECE1]] | +0.60 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[LDLRAP1]] | +0.60 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[LOXL2]] | +0.59 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[CALM1]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ADAM19]] | +0.58 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[DYNLT3]] | +0.58 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[FAM89B]] | +0.58 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[INPP5A]] | +0.58 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[TMEM184B]] | +0.58 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[GNAI2]] | +0.57 | +0.46 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRRF]] | -0.62 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[TBCEL]] | -0.56 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[LDAH]] | -0.54 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[CYP4A22-AS1]] | -0.53 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[CCNT2]] | -0.53 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[METAP1D]] | -0.52 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[MTPAP]] | -0.52 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[SP2-AS1]] | -0.52 | -0.42 / -0.37 | both halves | 7e-05 |  |
| [[SLC24A1]] | -0.50 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[NOL8]] | -0.50 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[MYO16-AS1]] | -0.50 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[USP40]] | -0.50 | -0.29 / -0.53 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TIMP3]] | B | TIMP3 activity raises ZCCHC24's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 3.10× lower at baseline in the lines without TIMP3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1 |
| [[GDNF]] | B | GDNF activity raises ZCCHC24's level | lines that do not express GDNF (38) vs lines expressing it (12) | 2.59× lower at baseline in the lines without GDNF | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9 |
| [[ITGA11]] | B | ITGA11 activity raises ZCCHC24's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.50× lower at baseline in the lines without ITGA11 | 0.031 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[AEBP1]] | B | AEBP1 activity raises ZCCHC24's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 2.87× lower at baseline in the lines without AEBP1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1 |
| [[LOXL2]] | B | LOXL2 activity raises ZCCHC24's level | lines that do not express LOXL2 (18) vs lines expressing it (32) | 2.30× lower at baseline in the lines without LOXL2 | 0.035 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1 |
| [[SDC2]] | B | SDC2 activity raises ZCCHC24's level | lines that do not express SDC2 (26) vs lines expressing it (24) | 2.48× lower at baseline in the lines without SDC2 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, TENM2, AMPH |
| [[FAM20C]] | B | FAM20C activity raises ZCCHC24's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 2.24× lower at baseline in the lines without FAM20C | 0.039 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |
| [[FCRLA]] | B | FCRLA activity raises ZCCHC24's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 2.78× lower at baseline in the lines without FCRLA | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474 |
| [[ADAM19]] | B | ADAM19 activity raises ZCCHC24's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 1.87× lower at baseline in the lines without ADAM19 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[TUBA1A]] | B | TUBA1A activity raises ZCCHC24's level | lines that do not express TUBA1A (10) vs lines expressing it (40) | 2.39× lower at baseline in the lines without TUBA1A | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, GABBR1, CHST10 |
| [[SFRP1]] | B | SFRP1 activity raises ZCCHC24's level | lines that do not express SFRP1 (32) vs lines expressing it (18) | 1.94× lower at baseline in the lines without SFRP1 | 0.083 | ⚠ within organs, on part of the lines; also absent: LAYN, INSYN2B, EVC2 |
| [[TOP2A]] | B | TOP2A activity lowers ZCCHC24's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLP2]] | B | ZCCHC24 activity raises PLP2's level | lines that do not express ZCCHC24 (5) vs lines expressing it (45) | 2.01× lower at baseline in the lines without ZCCHC24 | 0.012 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent |
| [[TGFB1]] | B | ZCCHC24 activity raises TGFB1's level | lines that do not express ZCCHC24 (5) vs lines expressing it (45) | 2.80× lower at baseline in the lines without ZCCHC24 | 0.022 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent |
| [[U2SURP]] | B | ZCCHC24 activity weakens U2SURP's drug response | lines that do not express ZCCHC24 (5) vs lines expressing it (44) | the lines without ZCCHC24 respond 1.23× as strongly (z diff -1.35); strongest at Digitoxin 5 µM: 2.27x vs 1.63x (z diff -2.9) | 0.036 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[EXTL3]] | B | ZCCHC24 activity lowers EXTL3's level | lines that do not express ZCCHC24 (5) vs lines expressing it (45) | 2.11× higher at baseline in the lines without ZCCHC24 | 0.037 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent |
| [[CDR2L]] | B | ZCCHC24 activity raises CDR2L's level | lines that do not express ZCCHC24 (5) vs lines expressing it (45) | 2.00× lower at baseline in the lines without ZCCHC24 | 0.059 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent |
| [[TUBA1A]] | B | ZCCHC24 activity raises TUBA1A's level | lines that do not express ZCCHC24 (5) vs lines expressing it (45) | 3.12× lower at baseline in the lines without ZCCHC24 | 0.069 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent |
| cells under [[Procainamide (hydrochloride) (drug)]] 0.5 µM | B | ZCCHC24 activity lowers the cells' numbers under Procainamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express ZCCHC24 (5) vs lines expressing it (43) | the lines without ZCCHC24: 1.26× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent |
| [[ST3GAL2]] | B | ZCCHC24 activity raises ST3GAL2's level | lines that do not express ZCCHC24 (5) vs lines expressing it (45) | 2.17× lower at baseline in the lines without ZCCHC24 | 0.084 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent |
| [[LOXL2]] | B | ZCCHC24 activity raises LOXL2's level | lines that do not express ZCCHC24 (5) vs lines expressing it (45) | 3.84× lower at baseline in the lines without ZCCHC24 | 0.091 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent |
| [[SNAI1]] | B | ZCCHC24 activity raises SNAI1's level | lines that do not express ZCCHC24 (5) vs lines expressing it (45) | 1.80× lower at baseline in the lines without ZCCHC24 | 0.093 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent |
| [[VIM]] | B | ZCCHC24 activity raises VIM's level | lines that do not express ZCCHC24 (5) vs lines expressing it (45) | 5.44× lower at baseline in the lines without ZCCHC24 | 0.098 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.626). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.0, 1.9); signed map (-1.7, 48.7). **Vector** length 95.9, 23.0% of its response variance represented; |z| ≥ 3 in 1,292 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +14.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.5 | +14.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.4 | +23.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.3 | +7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +24.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +9.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +3.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | -4.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.6 | -15.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.6 | -4.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | -11.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -4.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.1 | -0.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCHC-type containing 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.3 — chr10:79,382,325-79,445,624 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90798, Z3CXXC8; previously C10orf56 |
| Gene groups (HGNC) | Zinc fingers CCHC-type; Zinc fingers 3CxxC-type |
| Matched by | ensembl_id |

UniProt [Q8N2G6](https://www.uniprot.org/uniprotkb/Q8N2G6) carries no function annotation.

**Summary**, from NCBI Gene [219654](https://www.ncbi.nlm.nih.gov/gene/219654):

> Enables RNA binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26911](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26911) · Entrez [219654](https://www.ncbi.nlm.nih.gov/gene/219654) · UniProt [Q8N2G6](https://www.uniprot.org/uniprotkb/Q8N2G6) · Ensembl [ENSG00000165424](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165424)

## Data

Gene col 9119: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9119); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9119, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9119]; `tensor/DDL_lfc|DDL_z.npy` [9119]; `embed/gene_vectors.npy` [9119]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9119 or target_col == 9119). Every well: [[ZCCHC24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZCCHC24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
