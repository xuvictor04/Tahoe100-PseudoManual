---
symbol: "ABCA1"
type: "gene"
col: 9055
ensembl_id: "ENSG00000165029"
name: "ATP binding cassette subfamily A member 1"
location: "9q31.1"
module: 13
arm: "+"
pooled_cpm: 216.9
n_lines_expressing: 30
n_dd_up: 18
n_dd_down: 34
n_dd_up_clean: 13
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 28
direction_downstream: 19
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# ABCA1

*ATP binding cassette subfamily A member 1* — 9q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Retinoic acid (drug)]] 5 µM: 2.14× (z +12.8, q 1e-34, up in 24 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.308× (z -13.9, q 3e-41, down in 28 of 28 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.447× (z -13.5, q 5e-39, down in 28 of 29 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NR3C1]] (+0.59, fdr 1e-05), [[AIM2]] (+0.57, fdr 1e-05), [[MSC]] (+0.55, fdr 1e-05); moves opposite to [[MYO5C]] (-0.44, fdr 2e-04), [[ESRP1]] (-0.42, fdr 1e-04), [[PKP2]] (-0.42, fdr 7e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[PLIN2]] → it (grade B ⚠); 19 go from it, the strongest it → [[IFIT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9055.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Retinoic acid (drug)]] 5 µM |  | **2.14×** | +12.8 | 1e-34 | 24/29 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose |  |
| [[Bexarotene (drug)]] 0.05 µM |  | **2.56×** | +11.1 | 2e-26 | 27/28 (KATO III, MIA PaCa-2, …) | all doses, flat |  |
| [[Bexarotene (drug)]] 0.5 µM |  | **2.56×** | +11.1 | 2e-26 | 27/28 (KATO III, MIA PaCa-2, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **2.48×** | +10.8 | 8e-25 | 26/28 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bexarotene (drug)]] 5 µM |  | **1.64×** | +5.9 | 5e-07 | 22/28 (HepG2/C3A, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.61×** | +5.6 | 2e-06 | 19/28 (KATO III, HepG2/C3A, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +4.8 | 1e-04 | 17/27 (Hs 766T, NCI-H23, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.42×** | +4.1 | 0.002 | 15/28 (HOP62, A498, …) | all doses, flat |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.38×** | +3.8 | 0.009 | 19/28 (LOX-IMVI, CFPAC-1, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.81×** | +3.7 | 0.014 | 20/29 (hTERT-HPNE, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.75×** | +3.5 | 0.028 | 12/30 (LOX-IMVI, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.39×** | +3.2 | 0.061 | 15/30 (LOX-IMVI, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.061 | 15/29 (CFPAC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.067 | 10/28 (NCI-H2347, KATO III, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.32×** | +3.1 | 0.067 | 15/28 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.29×** | +3.0 | 0.086 | 14/28 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.19× | +3.0 | 0.095 | 9/29 (A498, HS-578T, …) | top dose only |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +2.9 | 0.097 | 13/28 (KATO III, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 17 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9055.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.308×** | -13.9 | 3e-41 | 28/28 (A-172, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.318×** | -13.5 | 3e-39 | 28/28 (A-172, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.447×** | -13.5 | 5e-39 | 28/29 (NCI-H1792, A-172, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.327×** | -13.2 | 1e-37 | 28/28 (A-172, J82, …) | all doses, stronger at high dose |  |
| [[Clotrimazole (drug)]] 5 µM |  | **0.503×** | -11.5 | 2e-28 | 28/29 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.405×** | -10.3 | 1e-22 | 23/25 (J82, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.411×** | -10.1 | 4e-22 | 23/27 (J82, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **0.441×** | -8.5 | 1e-15 | 25/29 (J82, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.534×** | -7.4 | 8e-12 | 26/28 (J82, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.663×** | -6.9 | 4e-10 | 19/28 (C32, NCI-H1792, …) | rises with dose | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.568×** | -6.7 | 1e-09 | 25/29 (C32, NCI-H1792, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.561×** | -6.6 | 3e-09 | 21/28 (RPMI-7951, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.588×** | -6.3 | 2e-08 | 26/28 (J82, HS-578T, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | **0.610×** | -5.6 | 9e-07 | 22/27 (NCI-H1792, J82, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **0.607×** | -5.4 | 2e-06 | 21/26 (J82, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | **0.762×** | -4.5 | 2e-04 | 18/28 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.696×** | -4.3 | 6e-04 | 20/28 (CFPAC-1, H4, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.713×** | -4.0 | 0.002 | 15/28 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.532×** | -3.9 | 0.003 | 18/29 (A-172, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.792×** | -3.9 | 0.003 | 13/28 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.720×** | -3.9 | 0.003 | 15/28 (CFPAC-1, NCI-H2347, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.725×** | -3.8 | 0.003 | 18/28 (C32, LOX-IMVI, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.738×** | -3.6 | 0.007 | 15/28 (CFPAC-1, NCI-H460, …) | all doses, flat |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.573×** | -3.4 | 0.011 | 18/28 (J82, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.748×** | -3.3 | 0.019 | 14/28 (H4, SW 900, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.761×** | -3.2 | 0.023 | 13/28 (A549, SNU-423, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.69 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9055. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 228 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -22.3) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -12.6) |
| [[H4 (line)]] | wt | 243 | 4 | 8 (7 ⚠) | [[Retinoic acid (drug)]] 5 µM 3.97× (z +12.3) | [[Belinostat (drug)]] 5 µM 0.0997× (z -14.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Clotrimazole (drug)]] 5 µM 0.381× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 746 | 0 | 12 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -27.9) |
| [[NCI-H460 (line)]] | wt | 63.9 | 4 | 8 (6 ⚠) | [[Retinoic acid (drug)]] 0.5 µM 3.43× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -16.2) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 492 | 0 | 12 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -21.0) |
| [[A-172 (line)]] | wt | 1,743 | 0 | 11 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -25.4) |
| [[HOP62 (line)]] | alt | 192 | 4 | 7 (6 ⚠) | [[Retinoic acid (drug)]] 5 µM 2.73× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -17.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Clotrimazole (drug)]] 5 µM 0.378× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 471 | 2 | 9 (8 ⚠) | [[Retinoic acid (drug)]] 5 µM 2.36× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -17.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -16.1) |
| [[HS-578T (line)]] | alt | 175 | 2 | 8 (7 ⚠) | [[Bexarotene (drug)]] 0.5 µM 3.43× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -16.7) |
| [[J82 (line)]] | alt | 836 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -22.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -21.0) |
| [[MIA PaCa-2 (line)]] | alt | 107 | 4 | 6 (3 ⚠) | [[Retinoic acid (drug)]] 5 µM 5.38× (z +15.1) | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -12.9) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Clotrimazole (drug)]] 5 µM 0.269× (z -11.8) |
| [[A498 (line)]] | wt | 712 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -22.2) |
| [[LOX-IMVI (line)]] | wt | 215 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -15.1) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -10.4) |
| [[SNU-423 (line)]] | alt | 738 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -16.1) |
| [[SW 900 (line)]] | alt | 455 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -15.0) |
| [[HepG2_C3A (line)]] | wt | 250 | 3 | 4 (4 ⚠) | [[Bexarotene (drug)]] 0.5 µM 3.93× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.208× (z -11.9) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SK-MEL-2 (line)]] | alt | 56.6 | 1 | 6 (5 ⚠) | [[Bexarotene (drug)]] 0.5 µM 4.43× (z +9.8) | [[Belinostat (drug)]] 5 µM 0.123× (z -13.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Clotrimazole (drug)]] 5 µM 0.389× (z -8.8) |
| [[COLO 205 (line)]] | alt | 229 | 3 | 3 (1 ⚠) | [[Bexarotene (drug)]] 0.05 µM 6.69× (z +9.3) | [[Clotrimazole (drug)]] 5 µM 0.201× (z -11.1) |
| [[A549 (line)]] | wt | 174 | 0 | 5 (3 ⚠) | — | [[Clotrimazole (drug)]] 5 µM 0.411× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 195 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -12.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -11.7) |
| [[KATO III (line)]] | alt | 69.8 | 4 | 1 | [[Retinoic acid (drug)]] 5 µM 4.99× (z +14.2) | [[Clotrimazole (drug)]] 5 µM 0.313× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 286 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.203× (z -12.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -12.5) |
| [[Hs 766T (line)]] | wt | 193 | 1 | 2 | [[Cobimetinib (drug)]] 5 µM 3.27× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -14.4) |
| [[SW 1088 (line)]] | alt | 270 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.102× (z -9.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 56.2 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.68× (z +8.9) ⚠ position not correctable | — |
| [[Panc 03.27 (line)]] | alt | 67.5 | 0 | 1 | — | [[Clotrimazole (drug)]] 5 µM 0.349× (z -9.1) |
| [[A-427 (line)]] | wt | 8.80 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 24.2 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 20.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 24.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 71.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 32.3 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 19.0 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.3 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 53.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.4 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 16.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 22.2 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 34.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 14.9 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 24.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9055), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR3C1]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[AIM2]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[MSC]] | +0.55 | +0.57 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[TMEM132D]] | +0.55 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[ZEB2]] | +0.55 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[CPQ]] | +0.54 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[KLF7]] | +0.53 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[NAV1]] | +0.53 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[KCNIP1]] | +0.53 | +0.37 / +0.44 | both halves | 8e-05 |  |
| [[LINC01411]] | +0.53 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ABI3BP]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[APBB1IP]] | +0.53 | +0.50 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO5C]] | -0.44 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[ESRP1]] | -0.42 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[PKP2]] | -0.42 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[TMEM181]] | -0.41 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[PHKA1]] | -0.41 | -0.48 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 7, C 21. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLIN2]] | B | PLIN2 activity raises ABCA1's level | lines that do not express PLIN2 (17) vs lines expressing it (33) | 3.82× lower at baseline in the lines without PLIN2 | 0.013 | ⚠ within organs, on part of the lines; also absent: AXL, UBE2Q2P13, SLC2A3 |
| [[PRRX1]] | B | PRRX1 activity raises ABCA1's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 2.97× lower at baseline in the lines without PRRX1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN |
| [[VSTM4]] | B | VSTM4 activity raises ABCA1's level | lines that do not express VSTM4 (31) vs lines expressing it (19) | 3.32× lower at baseline in the lines without VSTM4 | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC01411, KIRREL3, CCL2 |
| [[IFIT3]] | B | IFIT3 activity raises ABCA1's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 6.05× lower at baseline in the lines without IFIT3 | 0.041 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[MTOR]] | B | MTOR activity lowers ABCA1's level | compounds that target MTOR: 4 of 8 raise it (Bimiralisib, GSK1059615, Sapanisertib, Temsirolimus) | 50% of the class's compounds vs 3.9% of all compounds | 0.060 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EDNRA]] | B | EDNRA activity weakens ABCA1's drug response | lines that do not express EDNRA (12) vs lines expressing it (17) | the lines without EDNRA respond 1.11× as strongly (z diff -0.77); rises at some drug-doses, falls at others (71% from rises): Retinoic acid 5 µM: 2.58x vs 1.64x (z diff -3.4); Retinoic acid 0.5 µM: 3.20x vs 1.95x (z diff -3.0); Clotrimazole 5 µM: 0.38x vs 0.51x (z diff -2.1) | 0.060 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12; target measured in part of the lines; rises at some drug-doses, falls at others; line-wide correction only |
| [[IFIT2]] | B | IFIT2 activity raises ABCA1's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 4.10× lower at baseline in the lines without IFIT2 | 0.087 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[IDO1]] | C | IDO1 activity raises ABCA1's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 6.88× lower at baseline in the lines without IDO1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3; co-absent with the target |
| [[EDNRA]] | C | EDNRA activity raises ABCA1's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 6.95× lower at baseline in the lines without EDNRA | 0.001 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12; co-absent with the target |
| [[LINC01705]] | C | LINC01705 activity raises ABCA1's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 5.41× lower at baseline in the lines without LINC01705 | 0.001 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137; co-absent with the target |
| [[LOXL2]] | C | LOXL2 activity raises ABCA1's level | lines that do not express LOXL2 (18) vs lines expressing it (32) | 6.71× lower at baseline in the lines without LOXL2 | 0.002 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1; co-absent with the target |
| [[SPOCD1]] | C | SPOCD1 activity raises ABCA1's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 6.81× lower at baseline in the lines without SPOCD1 | 0.003 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 8, C 11. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFIT3]] | B | ABCA1 activity raises IFIT3's level | lines that do not express ABCA1 (20) vs lines expressing it (30) | 2.95× lower at baseline in the lines without ABCA1 | 0.007 | ⚠ within organs, on part of the lines; also absent: FN1, CDH2, IGFBP7 |
| [[PLIN2]] | B | ABCA1 activity raises PLIN2's level | lines that do not express ABCA1 (20) vs lines expressing it (30) | 3.95× lower at baseline in the lines without ABCA1 | 0.013 | ⚠ within organs, on part of the lines; also absent: FN1, CDH2, IGFBP7 |
| [[FNIP2]] | B | ABCA1 activity raises FNIP2's level | lines that do not express ABCA1 (20) vs lines expressing it (30) | 1.52× lower at baseline in the lines without ABCA1 | 0.022 | ⚠ within organs, on part of the lines; also absent: FN1, CDH2, IGFBP7 |
| [[CARD6]] | B | ABCA1 activity raises CARD6's level | lines that do not express ABCA1 (20) vs lines expressing it (30) | 2.23× lower at baseline in the lines without ABCA1 | 0.034 | ⚠ within organs, on part of the lines; also absent: FN1, CDH2, IGFBP7 |
| [[LINC01483]] | B | ABCA1 activity raises LINC01483's level | lines that do not express ABCA1 (20) vs lines expressing it (30) | 1.30× lower at baseline in the lines without ABCA1 | 0.066 | ⚠ within organs, on part of the lines; also absent: FN1, CDH2, IGFBP7 |
| [[TMEM181]] | B | ABCA1 activity lowers TMEM181's level | lines that do not express ABCA1 (20) vs lines expressing it (30) | 1.35× higher at baseline in the lines without ABCA1 | 0.068 | ⚠ within organs, on part of the lines; also absent: FN1, CDH2, IGFBP7 |
| [[FNIP2]] | B | ABCA1 activity strengthens FNIP2's drug response | lines that do not express ABCA1 (20) vs lines expressing it (28) | the lines without ABCA1 respond 0.63× as strongly (z diff +1.74); strongest at Panobinostat 0.5 µM: 0.77x vs 0.47x (z diff +3.7) | 0.069 | ⚠ within organs, on part of the lines; also absent: FN1, CDH2, IGFBP7; target measured in part of the lines; artifact flags |
| [[PLTP]] | B | ABCA1 activity raises PLTP's level | lines that do not express ABCA1 (20) vs lines expressing it (30) | 2.73× lower at baseline in the lines without ABCA1 | 0.092 | ⚠ within organs, on part of the lines; also absent: FN1, CDH2, IGFBP7 |
| [[MAF]] | C | ABCA1 activity raises MAF's level | lines that do not express ABCA1 (20) vs lines expressing it (30) | 4.69× lower at baseline in the lines without ABCA1 | 0.003 | ⚠ within organs, on part of the lines; also absent: FN1, CDH2, IGFBP7; co-absent with the target |
| [[LOXL2]] | C | ABCA1 activity raises LOXL2's level | lines that do not express ABCA1 (20) vs lines expressing it (30) | 5.64× lower at baseline in the lines without ABCA1 | 0.004 | ⚠ within organs, on part of the lines; also absent: FN1, CDH2, IGFBP7; co-absent with the target |
| [[SPOCD1]] | C | ABCA1 activity raises SPOCD1's level | lines that do not express ABCA1 (20) vs lines expressing it (30) | 4.20× lower at baseline in the lines without ABCA1 | 0.014 | ⚠ within organs, on part of the lines; also absent: FN1, CDH2, IGFBP7; co-absent with the target |
| [[LINC01705]] | C | ABCA1 activity raises LINC01705's level | lines that do not express ABCA1 (20) vs lines expressing it (30) | 3.80× lower at baseline in the lines without ABCA1 | 0.030 | ⚠ within organs, on part of the lines; also absent: FN1, CDH2, IGFBP7; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.499). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.1, 19.6); signed map (28.9, 45.3). **Vector** length 101, 28.0% of its response variance represented; |z| ≥ 3 in 1,264 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +2.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | -0.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +3.2 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | -0.3 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -3.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.3 | -3.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.1 | -2.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.1 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily A member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.1 — chr9:104,781,006-104,928,155 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TGD; previously ABC1, HDLDT1 |
| Gene groups (HGNC) | ATP binding cassette subfamily A; ATPase phospholipid transporting |
| Hallmark sets | BILE_ACID_METABOLISM, PROTEIN_SECRETION, INFLAMMATORY_RESPONSE, ADIPOGENESIS, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 12 pathways, smallest: HDL assembly; Plasma lipoprotein assembly; NR1H3 & NR1H2 regulate gene expression linked to cholesterol transport and efflux |
| Matched by | ensembl_id |

**Function**, from UniProt [O95477](https://www.uniprot.org/uniprotkb/O95477) (Phospholipid-transporting ATPase ABCA1):

> Catalyzes the translocation of specific phospholipids from the cytoplasmic to the extracellular/lumenal leaflet of membrane coupled to the hydrolysis of ATP. Thereby, participates in phospholipid transfer to apolipoproteins to form nascent high density lipoproteins/HDLs. Transports preferentially phosphatidylcholine over phosphatidylserine. May play a similar role in the efflux of intracellular cholesterol to apolipoproteins and the formation of nascent high density lipoproteins/HDLs. …

**Summary**, from NCBI Gene [19](https://www.ncbi.nlm.nih.gov/gene/19):

> The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intracellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the ABC1 subfamily. Members of the ABC1 subfamily comprise the only major ABC subfamily found exclusively in multicellular eukaryotes. With cholesterol as its …

**Accessions** — [HGNC:29](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29) · Entrez [19](https://www.ncbi.nlm.nih.gov/gene/19) · UniProt [O95477](https://www.uniprot.org/uniprotkb/O95477) · Ensembl [ENSG00000165029](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165029)

## Data

Gene col 9055: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9055); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9055, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9055]; `tensor/DDL_lfc|DDL_z.npy` [9055]; `embed/gene_vectors.npy` [9055]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9055 or target_col == 9055). Every well: [[ABCA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
