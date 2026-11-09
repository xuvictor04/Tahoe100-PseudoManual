---
symbol: "PELI2"
type: "gene"
col: 6357
ensembl_id: "ENSG00000139946"
name: "pellino E3 ubiquitin protein ligase family member 2"
location: "14q22.3"
module: 97
arm: "+"
pooled_cpm: 64.48
n_lines_expressing: 34
n_dd_up: 21
n_dd_down: 24
n_dd_up_clean: 18
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 9
direction_downstream: 10
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# PELI2

*pellino E3 ubiquitin protein ligase family member 2* — 14q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.02× (z +17.6, q 0e+00, up in 22 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.421× (z -15.8, q 0e+00, down in 32 of 32 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.285× (z -10.9, q 1e-25, down in 28 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02284]] (+0.66, fdr 7e-06, ⚠ read-through risk), [[GAREM1]] (+0.60, fdr 1e-05), [[LITAF]] (+0.57, fdr 1e-05), [[RNF103]] (+0.55, fdr 3e-05); moves opposite to [[GEMIN5]] (-0.49, fdr 1e-04), [[LINC02985]] (-0.49, fdr 4e-05), [[TBC1D9B]] (-0.49, fdr 3e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PROX1]] → it (grade B ⚠); 10 go from it, the strongest it → [[CHN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6357.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.02×** | +17.6 | 0e+00 | 22/32 (BT-474, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +10.4 | 9e-23 | 19/32 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +7.6 | 8e-12 | 16/33 (J82, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +7.2 | 8e-11 | 19/32 (BT-474, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +7.1 | 2e-10 | 21/33 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +6.8 | 7e-10 | 16/31 (HS-578T, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +6.5 | 8e-09 | 18/32 (NCI-H23, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +5.7 | 9e-07 | 18/31 (NCI-H23, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.9 | 7e-05 | 12/32 (CFPAC-1, KATO III, …) | top dose only |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.64×** | +4.3 | 0.001 | 16/33 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.002 | 16/32 (SW 900, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.27×** | +4.1 | 0.002 | 17/32 (C32, SW480, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.27×** | +4.0 | 0.002 | 12/32 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.57×** | +3.9 | 0.003 | 14/34 (AsPC-1, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.004 | 11/31 (H4, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 5 µM |  | 1.16× | +3.8 | 0.005 | 7/33 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.008 | 14/32 (BT-474, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6357.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.421×** | -15.8 | 0e+00 | 32/32 (SW1417, LoVo, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.458×** | -14.2 | 2e-43 | 23/30 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.285×** | -10.9 | 1e-25 | 28/31 (HT-29, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.293×** | -10.7 | 1e-24 | 29/32 (AsPC-1, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.587×** | -9.3 | 1e-18 | 21/26 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.536×** | -8.1 | 3e-14 | 27/32 (A498, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.394×** | -8.1 | 3e-14 | 24/32 (KATO III, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.394×** | -8.1 | 3e-14 | 24/32 (HT-29, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.676×** | -7.1 | 6e-11 | 20/32 (SHP-77, AsPC-1, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.681×** | -6.5 | 5e-09 | 19/26 (SW1417, C32, …) | all doses, stronger at high dose | composition shift |
| [[EX229 (drug)]] 0.05 µM |  | **0.690×** | -6.4 | 8e-09 | 20/32 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.645×** | -5.7 | 5e-07 | 24/33 (KATO III, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.525×** | -5.6 | 8e-07 | 21/31 (LoVo, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.534×** | -5.5 | 2e-06 | 15/31 (Hs 766T, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.744×** | -5.4 | 2e-06 | 19/32 (SHP-77, AsPC-1, …) | two highest doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.668×** | -5.2 | 5e-06 | 21/32 (NCI-H460, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.799×** | -3.9 | 0.003 | 11/32 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **0.650×** | -3.8 | 0.005 | 13/31 (hTERT-HPNE, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.864× | -3.7 | 0.006 | 15/33 (Panc 03.27, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.757×** | -3.6 | 0.007 | 16/32 (AsPC-1, CFPAC-1, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.870× | -3.5 | 0.010 | 7/32 (COLO 205, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6357. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 631 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -21.3) |
| [[BT-474 (line)]] | alt | 16.4 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +16.2) | — |
| [[SW1417 (line)]] | alt | 194 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 49.5 | 2 | 4 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.78× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C32 (line)]] | wt | 131 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 148 | 0 | 5 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.251× (z -14.1) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.408× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 141 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.204× (z -13.7) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 171 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HT-29 (line)]] | alt | 79.6 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.307× (z -11.2) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.144× (z -8.8) |
| [[SW 900 (line)]] | alt | 106 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.258× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H1573 (line)]] | alt | 69.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.387× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 136 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SNU-1 (line)]] | wt | 37.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +8.9) | [[AZD2858 (drug)]] 0.5 µM 0.122× (z -9.2) ⚠ toxic |
| [[A549 (line)]] | wt | 56.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +10.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.336× (z -9.2) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 80.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +14.3) | — |
| [[KATO III (line)]] | alt | 111 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.267× (z -12.4) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.130× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 17.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 98.9 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.421× (z -9.0) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 37.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +8.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.292× (z -9.0) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 52.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.264× (z -9.0) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 70.1 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.131× (z -9.6) |
| [[COLO 205 (line)]] | alt | 172 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.286× (z -9.5) ⚠ cell-cycle shift, explains ~54% of this change |
| [[H4 (line)]] | wt | 34.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.332× (z -9.5) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 26.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +13.4) | — |
| [[J82 (line)]] | alt | 22.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 32.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +8.8) | — |
| [[SW48 (line)]] | wt | 17.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.60× (z +8.8) | — |
| [[A-172 (line)]] | wt | 6.06 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.96 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.77 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 13.4 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.63 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.83 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.80 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.79 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.36 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.59 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.72 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.80 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6357), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02284]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 | ⚠ **readthrough risk**: LINC02284 lies 9.4 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[GAREM1]] | +0.60 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[LITAF]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[RNF103]] | +0.55 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[DIP2C-AS1]] | +0.54 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[FOXP1]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[RGCC]] | +0.53 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[PRKCH-AS1]] | +0.53 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[ARHGEF12]] | +0.52 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[TCF7L2]] | +0.52 | +0.38 / +0.58 | both halves | 7e-05 |  |
| [[OTUD1]] | +0.52 | +0.38 / +0.57 | both halves | 7e-05 |  |
| [[SYNE2]] | +0.52 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[SLCO3A1]] | +0.52 | +0.53 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GEMIN5]] | -0.49 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[LINC02985]] | -0.49 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[TBC1D9B]] | -0.49 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[RPGRIP1L]] | -0.48 | -0.41 / -0.37 | both halves | 9e-05 |  |
| [[ZNF526]] | -0.47 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[ZNF70]] | -0.47 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[TRIT1]] | -0.46 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[CHD1L]] | -0.46 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[RABEPK]] | -0.46 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[PIGU]] | -0.46 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[NUDCD3]] | -0.45 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[EARS2]] | -0.45 | -0.41 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PROX1]] | B | PROX1 activity raises PELI2's level | lines that do not express PROX1 (30) vs lines expressing it (20) | 3.96× lower at baseline in the lines without PROX1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH17, CLRN3, LINC02964 |
| [[CHN2]] | B | CHN2 activity raises PELI2's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 3.49× lower at baseline in the lines without CHN2 | 0.002 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |
| [[TOX3]] | B | TOX3 activity raises PELI2's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 3.88× lower at baseline in the lines without TOX3 | 0.003 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[FBXO32]] | B | FBXO32 activity raises PELI2's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 3.39× lower at baseline in the lines without FBXO32 | 0.012 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[RDH10]] | B | RDH10 activity raises PELI2's level | lines that do not express RDH10 (9) vs lines expressing it (41) | 1.95× lower at baseline in the lines without RDH10 | 0.043 | ⚠ within organs, on part of the lines; also absent: SEL1L3, EPB41L4B, JDP2; maybe low, not absent |
| [[PDK4]] | B | PDK4 activity raises PELI2's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 2.48× lower at baseline in the lines without PDK4 | 0.059 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA |
| [[STAT5A]] | B | STAT5A activity raises PELI2's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 2.85× lower at baseline in the lines without STAT5A | 0.068 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[TMC5]] | B | TMC5 activity raises PELI2's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 2.59× lower at baseline in the lines without TMC5 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4 |
| [[LINC02284]] | C | LINC02284 activity raises PELI2's level | lines that do not express LINC02284 (17) vs lines expressing it (33) | 7.22× lower at baseline in the lines without LINC02284 | 1e-05 | ⚠ within organs, on part of the lines; also absent: PELI2, CFH, ADAM28; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHN2]] | B | PELI2 activity raises CHN2's level | lines that do not express PELI2 (16) vs lines expressing it (34) | 2.31× lower at baseline in the lines without PELI2 | 0.002 | ⚠ within organs, on part of the lines; also absent: LINC02284, DNAJC12, ADAM28 |
| [[SIPA1L2]] | B | PELI2 activity raises SIPA1L2's level | lines that do not express PELI2 (16) vs lines expressing it (34) | 2.84× lower at baseline in the lines without PELI2 | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC02284, DNAJC12, ADAM28 |
| [[RDH10]] | B | PELI2 activity raises RDH10's level | lines that do not express PELI2 (16) vs lines expressing it (34) | 1.69× lower at baseline in the lines without PELI2 | 0.027 | ⚠ within organs, on part of the lines; also absent: LINC02284, DNAJC12, ADAM28 |
| [[ARHGAP42]] | B | PELI2 activity strengthens ARHGAP42's drug response | lines that do not express PELI2 (10) vs lines expressing it (26) | the lines without PELI2 respond 0.85× as strongly (z diff +1.08); strongest at Idarubicin (hydrochloride) 5 µM: 0.72x vs 0.50x (z diff +3.0) | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC02284, DNAJC12, ADAM28; target measured in part of the lines; artifact flags |
| [[TOX3]] | B | PELI2 activity raises TOX3's level | lines that do not express PELI2 (16) vs lines expressing it (34) | 2.22× lower at baseline in the lines without PELI2 | 0.067 | ⚠ within organs, on part of the lines; also absent: LINC02284, DNAJC12, ADAM28 |
| [[FOXC1]] | B | PELI2 activity raises FOXC1's level | lines that do not express PELI2 (16) vs lines expressing it (34) | 1.33× lower at baseline in the lines without PELI2 | 0.074 | ⚠ within organs, on part of the lines; also absent: LINC02284, DNAJC12, ADAM28 |
| [[ZNF70]] | B | PELI2 activity raises ZNF70's level | lines that do not express PELI2 (16) vs lines expressing it (34) | 1.42× lower at baseline in the lines without PELI2 | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC02284, DNAJC12, ADAM28 |
| [[PROX1]] | B | PELI2 activity raises PROX1's level | lines that do not express PELI2 (16) vs lines expressing it (34) | 1.84× lower at baseline in the lines without PELI2 | 0.087 | ⚠ within organs, on part of the lines; also absent: LINC02284, DNAJC12, ADAM28 |
| [[EPS8]] | B | PELI2 activity raises EPS8's level | lines that do not express PELI2 (16) vs lines expressing it (34) | 1.79× lower at baseline in the lines without PELI2 | 0.095 | ⚠ within organs, on part of the lines; also absent: LINC02284, DNAJC12, ADAM28 |
| [[LINC02284]] | C | PELI2 activity raises LINC02284's level | lines that do not express PELI2 (16) vs lines expressing it (34) | 3.21× lower at baseline in the lines without PELI2 | 2e-04 | ⚠ within organs, on part of the lines; also absent: LINC02284, DNAJC12, ADAM28; co-absent with the target |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.131). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.2, 43.4); signed map (51.7, 11.6). **Vector** length 112, 31.2% of its response variance represented; |z| ≥ 3 in 1,105 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +7.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.7 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.1 | -14.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +4.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.6 | +0.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.5 | +0.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.4 | -15.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.1 | -10.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.0 | -10.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.5 | -8.1 |
|  | [[EX229 (drug)]] 5 µM |  | -5.0 | -8.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.9 | -8.1 |

## What is on record

|  |  |
|---|---|
| Name | pellino E3 ubiquitin protein ligase family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.3 — chr14:56,117,814-56,301,524 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pellino E3 ubiquitin protein ligases |
| Reactome | 20 pathways, smallest: IRAK1 recruits IKK complex; IRAK1 recruits IKK complex upon TLR7/8 or 9 stimulation; MyD88 cascade initiated on plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAT8](https://www.uniprot.org/uniprotkb/Q9HAT8) (E3 ubiquitin-protein ligase pellino homolog 2):

> E3 ubiquitin ligase catalyzing the covalent attachment of ubiquitin moieties onto substrate proteins. Specifically recognizes and binds proteins phosphorylated on threonine residues. Involved in the TLR and IL-1 signaling pathways via interaction with the complex containing IRAK kinases and TRAF6. Mediates IL1B-induced IRAK1 'Lys-63'-linked polyubiquitination and possibly 'Lys-48'-linked ubiquitination. Acts as a negative regulator of cGAS-STING signaling: recognizes and binds phosphorylated …

**Summary**, from NCBI Gene [57161](https://www.ncbi.nlm.nih.gov/gene/57161):

> Predicted to enable protein-macromolecule adaptor activity and ubiquitin protein ligase activity. Acts upstream of or within positive regulation of MAPK cascade and positive regulation of protein phosphorylation. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:8828](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8828) · Entrez [57161](https://www.ncbi.nlm.nih.gov/gene/57161) · UniProt [Q9HAT8](https://www.uniprot.org/uniprotkb/Q9HAT8) · Ensembl [ENSG00000139946](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139946)

## Data

Gene col 6357: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6357); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6357, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6357]; `tensor/DDL_lfc|DDL_z.npy` [6357]; `embed/gene_vectors.npy` [6357]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6357 or target_col == 6357). Every well: [[PELI2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PELI2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
