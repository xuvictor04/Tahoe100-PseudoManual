---
symbol: "IQGAP2"
type: "gene"
col: 7014
ensembl_id: "ENSG00000145703"
name: "IQ motif containing GTPase activating protein 2"
location: "5q13.3"
module: 55
arm: "+"
pooled_cpm: 21.36
n_lines_expressing: 25
n_dd_up: 24
n_dd_down: 19
n_dd_up_clean: 16
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 10
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# IQGAP2

*IQ motif containing GTPase activating protein 2* — 5q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.62× (z +20.2, q 0e+00, up in 20 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.551× (z -8.8, q 8e-16, down in 18 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIK3AP1]] (+0.62, fdr 1e-05), [[GRIN2B]] (+0.61, fdr 2e-05), [[PADI2]] (+0.59, fdr 1e-05); moves opposite to [[TMCO3]] (-0.46, fdr 3e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[KLHL13]] → it (grade C ⚠); 10 go from it, the strongest it → [[PDE9A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7014.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.62×** | +20.2 | 0e+00 | 20/23 (PANC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.06×** | +16.6 | 0e+00 | 12/18 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +15.2 | 0e+00 | 9/15 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.62×** | +14.3 | 2e-44 | 13/22 (BT-474, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +11.0 | 5e-26 | 3/21 (PANC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.88×** | +9.4 | 4e-19 | 8/22 (PANC-1, NCI-H1573, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.81×** | +8.8 | 9e-17 | 12/22 (PANC-1, BT-474, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.80×** | +8.7 | 2e-16 | 3/22 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.77×** | +8.5 | 1e-15 | 6/22 (PANC-1, NCI-H1573, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.63×** | +6.7 | 1e-09 | 7/15 (PANC-1, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.50×** | +6.0 | 9e-08 | 5/22 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.41×** | +4.9 | 4e-05 | 0/22 | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +4.3 | 7e-04 | 7/23 (SW1417, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.77×** | +4.1 | 0.001 | 4/23 (PANC-1, BT-474, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.32×** | +4.1 | 0.002 | 4/23 (LS 180, BT-474, …) | all doses, stronger at high dose |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.31×** | +3.7 | 0.006 | 7/22 (NCI-H2030, A549, …) | all doses, flat | position effect removed |
| [[Busulfan (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.010 | 4/22 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.024 | 5/22 (SW 900, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.045 | 0/22 | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.081 | 4/21 (SW480, SW1417, …) | all doses, flat | position effect removed |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.23×** | +2.9 | 0.081 | 1/23 (HepG2/C3A) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.22×** | +2.9 | 0.081 | 6/23 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7014.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.551×** | -8.8 | 8e-16 | 18/22 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.604×** | -7.4 | 3e-11 | 19/22 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.731×** | -6.5 | 1e-08 | 16/23 (HT-29, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.680×** | -5.7 | 2e-06 | 18/22 (NCI-H2030, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.796×** | -4.7 | 2e-04 | 8/23 (LoVo, SW480, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.755×** | -4.0 | 0.006 | 7/22 (MIA PaCa-2, SW 900, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.764×** | -4.0 | 0.006 | 8/22 (HT-29, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.770×** | -3.8 | 0.009 | 12/22 (LS 180, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.838× | -3.7 | 0.015 | 14/22 (LoVo, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.779×** | -3.6 | 0.015 | 10/22 (HT-29, LS 180, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.792×** | -3.4 | 0.031 | 6/23 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.792×** | -3.4 | 0.031 | 11/22 (A549, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.636×** | -3.3 | 0.050 | 7/21 (KATO III, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.804×** | -3.2 | 0.056 | 13/22 (SW480, LoVo, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.805×** | -3.2 | 0.056 | 10/21 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.806×** | -3.2 | 0.056 | 12/22 (A498, LoVo, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.800×** | -3.1 | 0.056 | 10/22 (HT-29, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.809×** | -3.1 | 0.060 | 15/22 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.656×** | -3.0 | 0.073 | 2/22 (PANC-1, A549) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.664×** | -2.9 | 0.094 | 8/20 (HT-29, LS 180, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7014. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 80.1 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -15.6) |
| [[LoVo (line)]] | wt | 133 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -23.7) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.184× (z -12.8) |
| [[LS 180 (line)]] | wt | 34.7 | 1 | 8 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.07× (z +10.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -13.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.207× (z -10.3) |
| [[HT-29 (line)]] | alt | 48.2 | 0 | 7 (3 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.242× (z -12.3) |
| [[KATO III (line)]] | alt | 128 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -12.5) |
| [[PANC-1 (line)]] | alt | 5.54 | 5 (3 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 7.06× (z +15.8) | [[AZD2858 (drug)]] 0.5 µM 0.115× (z -8.8) ⚠ toxic |
| [[SW480 (line)]] | alt | 50.7 | 1 (1 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.97× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -10.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.310× (z -8.6) |
| [[A549 (line)]] | wt | 30.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -13.9) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 15.2 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0740× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.148× (z -10.0) |
| [[A-427 (line)]] | wt | 31.3 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0469× (z -20.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.272× (z -12.7) |
| [[NCI-H2030 (line)]] | alt | 18.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.197× (z -8.7) |
| [[A498 (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -11.9) ⚠ cell-cycle shift, explains ~19% of this change |
| [[BT-474 (line)]] | alt | 14.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.80× (z +10.1) | — |
| [[C-33 A (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0623× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 5.98 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.10× (z +10.0) | — |
| [[A-172 (line)]] | wt | 4.80 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.27 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.10 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 87.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.44 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.31 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.23 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.51 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.11 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.37 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7014), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIK3AP1]] | +0.62 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[GRIN2B]] | +0.61 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[PADI2]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[ENTREP2]] | +0.59 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[HNF4A]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[LINC01819]] | +0.58 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[CTSE]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[LINC00937]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[HCN1]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[REG4]] | +0.56 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[PCK1]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[CFTR]] | +0.56 | +0.52 / +0.63 | both halves | 1e-05 | pathway: RHO GTPase Effectors |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMCO3]] | -0.46 | -0.48 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLHL13]] | C | KLHL13 activity raises IQGAP2's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 2.04× lower at baseline in the lines without KLHL13 | 0.010 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4; co-absent with the target |
| [[IGFL4]] | C | IGFL4 activity raises IQGAP2's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 2.55× lower at baseline in the lines without IGFL4 | 0.044 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent; co-absent with the target |
| [[KSR2]] | C | KSR2 activity raises IQGAP2's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 1.71× lower at baseline in the lines without KSR2 | 0.080 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE9A]] | B | IQGAP2 activity raises PDE9A's level | lines that do not express IQGAP2 (25) vs lines expressing it (25) | 2.48× lower at baseline in the lines without IQGAP2 | 0.016 | ⚠ within organs, on part of the lines; also absent: KLHL13, KCNQ2, CHD5; maybe low, not absent |
| [[NKD2]] | B | IQGAP2 activity raises NKD2's level | lines that do not express IQGAP2 (25) vs lines expressing it (25) | 2.24× lower at baseline in the lines without IQGAP2 | 0.016 | ⚠ within organs, on part of the lines; also absent: KLHL13, KCNQ2, CHD5; maybe low, not absent |
| [[ADGRB1]] | B | IQGAP2 activity raises ADGRB1's level | lines that do not express IQGAP2 (25) vs lines expressing it (25) | 1.73× lower at baseline in the lines without IQGAP2 | 0.018 | ⚠ within organs, on part of the lines; also absent: KLHL13, KCNQ2, CHD5; maybe low, not absent |
| [[SHH]] | B | IQGAP2 activity raises SHH's level | lines that do not express IQGAP2 (25) vs lines expressing it (25) | 1.67× lower at baseline in the lines without IQGAP2 | 0.039 | ⚠ within organs, on part of the lines; also absent: KLHL13, KCNQ2, CHD5; maybe low, not absent |
| [[ELOVL4]] | B | IQGAP2 activity lowers ELOVL4's level | lines that do not express IQGAP2 (25) vs lines expressing it (25) | 1.40× higher at baseline in the lines without IQGAP2 | 0.046 | ⚠ within organs, on part of the lines; also absent: KLHL13, KCNQ2, CHD5; maybe low, not absent |
| [[SORL1]] | B | IQGAP2 activity raises SORL1's level | lines that do not express IQGAP2 (25) vs lines expressing it (25) | 2.40× lower at baseline in the lines without IQGAP2 | 0.053 | ⚠ within organs, on part of the lines; also absent: KLHL13, KCNQ2, CHD5; maybe low, not absent |
| [[NFE2L3]] | B | IQGAP2 activity strengthens NFE2L3's drug response | lines that do not express IQGAP2 (24) vs lines expressing it (23) | the lines without IQGAP2 respond 0.80× as strongly (z diff +0.67); strongest at Selinexor 5 µM: 0.81x vs 0.64x (z diff +2.3) | 0.067 | ⚠ within organs, on part of the lines; also absent: KLHL13, KCNQ2, CHD5; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[KCNQ1]] | B | IQGAP2 activity raises KCNQ1's level | lines that do not express IQGAP2 (25) vs lines expressing it (25) | 1.51× lower at baseline in the lines without IQGAP2 | 0.079 | ⚠ within organs, on part of the lines; also absent: KLHL13, KCNQ2, CHD5; maybe low, not absent |
| [[NFE2L3]] | B | IQGAP2 activity raises NFE2L3's level | lines that do not express IQGAP2 (25) vs lines expressing it (25) | 1.50× lower at baseline in the lines without IQGAP2 | 0.082 | ⚠ within organs, on part of the lines; also absent: KLHL13, KCNQ2, CHD5; maybe low, not absent |
| [[KLHL13]] | C | IQGAP2 activity raises KLHL13's level | lines that do not express IQGAP2 (25) vs lines expressing it (25) | 2.88× lower at baseline in the lines without IQGAP2 | 0.001 | ⚠ within organs, on part of the lines; also absent: KLHL13, KCNQ2, CHD5; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.580). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.4, 48.5); signed map (65.1, 9.9). **Vector** length 75.8, 21.5% of its response variance represented; |z| ≥ 3 in 693 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.8 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.5 | +16.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +20.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.1 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +7.1 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.6 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -7.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -6.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.3 | -4.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | IQ motif containing GTPase activating protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.3 — chr5:76,403,285-76,708,132 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | IQ motif containing GTPase activating protein family |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 10 pathways, smallest: RHO GTPases activate IQGAPs; RHOG GTPase cycle; CDC42 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13576](https://www.uniprot.org/uniprotkb/Q13576) (Ras GTPase-activating-like protein IQGAP2):

> Binds to activated CDC42 and RAC1 but does not seem to stimulate their GTPase activity. Associates with calmodulin.

**Summary**, from NCBI Gene [10788](https://www.ncbi.nlm.nih.gov/gene/10788):

> This gene encodes a member of the IQGAP family. The encoded protein contains three IQ domains, one calponin homology domain, one Ras-GAP domain and one WW domain. This protein interacts with components of the cytoskeleton, with cell adhesion molecules, and with several signaling molecules to regulate cell morphology and motility. It also acts as a tumor suppressor and has been found to play a role in regulating innate antiviral responses. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:6111](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6111) · Entrez [10788](https://www.ncbi.nlm.nih.gov/gene/10788) · UniProt [Q13576](https://www.uniprot.org/uniprotkb/Q13576) · Ensembl [ENSG00000145703](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145703)

## Data

Gene col 7014: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7014); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7014, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7014]; `tensor/DDL_lfc|DDL_z.npy` [7014]; `embed/gene_vectors.npy` [7014]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7014 or target_col == 7014). Every well: [[IQGAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IQGAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
