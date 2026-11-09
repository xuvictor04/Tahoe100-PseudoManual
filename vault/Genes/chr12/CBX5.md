---
symbol: "CBX5"
type: "gene"
col: 1730
ensembl_id: "ENSG00000094916"
name: "chromobox 5"
location: "12q13.13"
module: 3
arm: "-"
pooled_cpm: 106.27
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CBX5

*chromobox 5* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.54× (z +19.9, q 0e+00, up in 43 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 1.36× (z +5.0, q 8e-05, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.562× (z -8.9, q 2e-16, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOXM1]] (+0.75, fdr 7e-06), [[SRP9]] (+0.73, fdr 1e-05), [[POGLUT3]] (+0.72, fdr 7e-06); moves opposite to [[COMMD6]] (-0.68, fdr 2e-05), [[RPP21]] (-0.67, fdr 7e-06), [[SMIM26]] (-0.66, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[EPB41L4A-AS1]] (-0.66, fdr 2e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1730.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.54×** | +19.9 | 0e+00 | 43/43 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.30×** | +19.5 | 0e+00 | 48/49 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +14.7 | 0e+00 | 45/45 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.29×** | +5.9 | 6e-07 | 27/48 (HS-578T, LoVo, …) | inconsistent across doses | composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.36×** | +5.0 | 8e-05 | 35/48 (BT-474, PANC-1, …) | top dose only |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.33×** | +4.7 | 3e-04 | 32/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.34×** | +4.2 | 0.002 | 25/48 (NCI-H1573, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.9 | 0.007 | 24/47 (C32, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.007 | 25/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.7 | 0.012 | 1/50 (NCI-H23) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.015 | 23/48 (A-427, A-172, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **1.25×** | +3.5 | 0.025 | 23/47 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.24×** | +3.4 | 0.025 | 25/48 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.045 | 18/48 (PANC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.25×** | +3.2 | 0.045 | 22/48 (HOP62, A498, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.14× | +3.0 | 0.079 | 9/48 (LOX-IMVI, NCI-H1573, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.0 | 0.079 | 15/48 (NCI-H1792, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1730.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.562×** | -8.9 | 2e-16 | 46/48 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.613×** | -8.0 | 3e-13 | 41/48 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.643×** | -7.2 | 8e-11 | 41/48 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.765×** | -6.2 | 6e-08 | 26/49 (LS 180, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.725×** | -5.3 | 2e-05 | 34/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.782×** | -4.0 | 0.005 | 25/48 (H4, LS 180, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.626×** | -4.0 | 0.005 | 25/45 (HCT15, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.721×** | -3.8 | 0.009 | 26/49 (C32, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.814×** | -3.4 | 0.045 | 21/48 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.818×** | -3.3 | 0.053 | 19/48 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 0.874× | -3.2 | 0.083 | 10/48 (HOP62, A-427, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.878× | -3.0 | 0.11 | 19/49 (KATO III, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1730. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 83.4 | 3 (3 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +11.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 128 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.83× (z +23.5) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 2.24× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 131 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +16.1) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.363× (z -12.3) |
| [[H4 (line)]] | wt | 112 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.44× (z +9.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -10.9) |
| [[HS-578T (line)]] | alt | 62.8 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +18.7) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[KATO III (line)]] | alt | 97.5 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +12.7) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.333× (z -10.0) |
| [[SNU-423 (line)]] | alt | 78.5 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +15.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 217 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +11.2) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 0.5 µM 0.403× (z -10.1) |
| [[A-172 (line)]] | wt | 95.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +17.4) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 86.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +18.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 57.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +16.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 38.1 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +17.3) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 50.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +12.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 71.2 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.99× (z +15.6) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.556× (z -8.5) ⚠ cell-cycle shift, explains ~90% of this change |
| [[NCI-H2347 (line)]] | alt | 73.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +10.8) | — |
| [[A498 (line)]] | wt | 162 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +14.7) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 36.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.66× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +9.3) | — |
| [[C32 (line)]] | wt | 106 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +11.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 161 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.91× (z +11.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 189 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +11.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -12.2) |
| [[HOP62 (line)]] | alt | 129 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +11.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -8.6) |
| [[HT-29 (line)]] | alt | 70.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +13.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 75.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +10.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 81.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.97× (z +10.6) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.403× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 165 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +12.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 118 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +13.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 62.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +11.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 58.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +13.9) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 96.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +12.8) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 67.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +11.5) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 114 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +10.1) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 65.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +8.9) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 78.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +10.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 65.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.88× (z +15.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 191 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +10.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -12.8) |
| [[SK-MEL-2 (line)]] | alt | 72.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +12.9) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 52.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +9.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 136 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +8.6) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 154 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +9.1) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 148 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.203× (z -11.5) ⚠ cell-cycle shift, explains ~12% of this change |
| [[COLO 205 (line)]] | alt | 56.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 63.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.36× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 59.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.07× (z +11.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 130 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1730), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXM1]] | +0.75 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[SRP9]] | +0.73 | +0.51 / +0.74 | both halves | 1e-05 |  |
| [[POGLUT3]] | +0.72 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[LMNB2]] | +0.69 | +0.58 / +0.75 | both halves | 7e-06 | same gene group; STRING 444 |
| [[TMPO]] | +0.69 | +0.64 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 448 |
| [[HNRNPL]] | +0.69 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[SRSF1]] | +0.69 | +0.57 / +0.70 | both halves | 9e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[RAB1B]] | +0.69 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[HELLS]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 459 |
| [[NONO]] | +0.68 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[YWHAE]] | +0.67 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[ANLN]] | +0.67 | +0.59 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD6]] | -0.68 | -0.48 / -0.75 | both halves | 2e-05 |  |
| [[RPP21]] | -0.67 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | -0.66 | -0.54 / -0.66 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EPB41L4A-AS1]] | -0.66 | -0.47 / -0.70 | both halves | 2e-05 |  |
| [[BAHD1]] | -0.66 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[CAMLG]] | -0.66 | -0.56 / -0.68 | both halves | 1e-05 |  |
| [[MRPL32]] | -0.66 | -0.48 / -0.70 | both halves | 2e-05 |  |
| [[ZNF593]] | -0.65 | -0.41 / -0.66 | both halves | 4e-05 |  |
| [[ARL8A]] | -0.65 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[IL17RA]] | -0.64 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[CIAO2B]] | -0.64 | -0.48 / -0.67 | both halves | 2e-05 |  |
| [[RPS27]] | -0.64 | -0.48 / -0.69 | both halves | 2e-05 |  |
| [[ATP5MK]] | -0.62 | -0.38 / -0.70 | both halves | 7e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CBX5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises CBX5's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[POGLUT3]] | B | POGLUT3 activity raises CBX5's level | lines that do not express POGLUT3 (5) vs lines expressing it (45) | 1.24× lower at baseline in the lines without POGLUT3 | 0.087 | ⚠ within organs, on part of the lines; also absent: DENND2B, MEX3A, CAMKK1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.666). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-41.1, -26.9); signed map (-33.0, -47.8). **Vector** length 149, 50.1% of its response variance represented; |z| ≥ 3 in 1,247 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA 3'-end processing* (reactome, mean cos +0.57 to 12); *mRNA Polyadenylation* (reactome, mean cos +0.58 to 11); *mRNA Splicing - Major Pathway* (reactome, mean cos +0.56 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.0 | +14.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +19.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +19.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.5 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.2 | +2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.7 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +1.7 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +3.1 | +3.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -9.7 | -8.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -8.7 | -8.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -8.4 | -7.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -6.3 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.1 | -5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.3 | -3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -5.0 | -3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.4 | -2.5 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | chromobox 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:54,230,942-54,280,133 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HP1Hs-alpha, HP1, HP1-ALPHA, HP1alpha |
| Gene groups (HGNC) | Chromobox family; MicroRNA protein coding host genes |
| Hallmark sets | E2F_TARGETS |
| Reactome | 9 pathways, smallest: Transcriptional Regulation by E2F6; SUMOylation of chromatin organization proteins; Regulation of endogenous retroelements by KRAB-ZFP proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P45973](https://www.uniprot.org/uniprotkb/P45973) (Chromobox protein homolog 5):

> Component of heterochromatin that recognizes and binds histone H3 tails methylated at 'Lys-9' (H3K9me), leading to epigenetic repression. In contrast, it is excluded from chromatin when 'Tyr-41' of histone H3 is phosphorylated (H3Y41ph). Also recognizes and binds histone H1.4 methylated at 'Lys-26' (H1.4K26me). Excluded from chromatin when histone H1.4 is Simultaneously methylated at Lys-26 (H1.4K26me) and phosphorylated at Ser-27 (H1.4S27Ph). May contribute to the association of …

**Summary**, from NCBI Gene [23468](https://www.ncbi.nlm.nih.gov/gene/23468):

> This gene encodes a highly conserved nonhistone protein, which is a member of the heterochromatin protein family. The protein is enriched in the heterochromatin and associated with centromeres. The protein has a single N-terminal chromodomain which can bind to histone proteins via methylated lysine residues, and a C-terminal chromo shadow-domain (CSD) which is responsible for the homodimerization and interaction with a number of chromatin-associated nonhistone proteins. The encoded product is …

**Accessions** — [HGNC:1555](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1555) · Entrez [23468](https://www.ncbi.nlm.nih.gov/gene/23468) · UniProt [P45973](https://www.uniprot.org/uniprotkb/P45973) · Ensembl [ENSG00000094916](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000094916)

## Data

Gene col 1730: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1730); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1730, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1730]; `tensor/DDL_lfc|DDL_z.npy` [1730]; `embed/gene_vectors.npy` [1730]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1730 or target_col == 1730). Every well: [[CBX5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CBX5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
