---
symbol: "NRIP1"
type: "gene"
col: 11113
ensembl_id: "ENSG00000180530"
name: "nuclear receptor interacting protein 1"
location: "21q11.2-q21.1"
module: 16
arm: "+"
pooled_cpm: 272.79
n_lines_expressing: 42
n_dd_up: 13
n_dd_down: 20
n_dd_up_clean: 13
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 14
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# NRIP1

*nuclear receptor interacting protein 1* — 21q11.2-q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.68× (z +11.0, q 1e-25, up in 35 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.135× (z -32.5, q 0e+00, down in 40 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL18]] (+0.61, fdr 2e-05), [[ZNF620]] (+0.59, fdr 5e-05), [[ZNF764]] (+0.55, fdr 8e-05); moves opposite to [[DCUN1D2]] (-0.58, fdr 1e-05), [[LONP1]] (-0.52, fdr 7e-05), [[GMCL1]] (-0.51, fdr 2e-04).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NR2F1-AS1]] → it (grade B ⚠); 14 go from it, the strongest it → [[LONP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11113.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.68×** | +11.0 | 1e-25 | 35/41 (LoVo, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +10.7 | 2e-24 | 29/40 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +8.6 | 2e-15 | 26/40 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +7.1 | 1e-10 | 30/40 (LoVo, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.46×** | +6.1 | 1e-07 | 30/40 (CFPAC-1, KATO III, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.04×** | +6.0 | 2e-07 | 27/40 (LS 180, C32, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | **1.23×** | +4.8 | 1e-04 | 23/41 (HOP62, CFPAC-1, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.005 | 26/40 (CFPAC-1, CHP-212, …) | all doses, flat |  |
| [[Tazarotene (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.013 | 25/40 (CFPAC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.024 | 21/40 (SNU-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.054 | 19/40 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.070 | 19/40 (LS 180, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.073 | 22/40 (NCI-H2347, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11113.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.135×** | -32.5 | 0e+00 | 40/40 (Hs 766T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.156×** | -30.1 | 0e+00 | 40/40 (Hs 766T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.209×** | -25.4 | 0e+00 | 40/40 (Hs 766T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.299×** | -18.9 | 0e+00 | 35/37 (HEC-1-A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.403×** | -14.8 | 0e+00 | 35/41 (HEC-1-A, Hs 766T, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.462×** | -12.5 | 6e-34 | 38/40 (A498, SW 900, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.612×** | -11.3 | 1e-27 | 30/41 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.553×** | -9.6 | 4e-20 | 36/40 (NCI-H2347, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.586×** | -8.4 | 4e-15 | 34/42 (SNU-423, NCI-H2347, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.618×** | -7.5 | 3e-12 | 32/40 (SNU-423, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.690×** | -5.8 | 3e-07 | 28/39 (Panc 03.27, LOX-IMVI, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.534×** | -5.3 | 5e-06 | 31/41 (A549, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.721×** | -5.3 | 5e-06 | 29/40 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.734×** | -5.0 | 2e-05 | 29/40 (SW1417, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.805×** | -5.0 | 2e-05 | 23/40 (SW 900, LOX-IMVI, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.853× | -3.6 | 0.009 | 17/40 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.813×** | -3.4 | 0.024 | 18/40 (BT-474, A-172, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.764×** | -3.1 | 0.052 | 20/40 (SW1417, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.873× | -3.1 | 0.052 | 15/40 (A-172, BT-474, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.826×** | -3.0 | 0.072 | 18/40 (HT-29, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11113. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 451 | 5 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +17.9) | [[Panobinostat (drug)]] 5 µM 0.134× (z -22.2) |
| [[Hs 766T (line)]] | wt | 692 | 1 | 11 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 5.54× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.0317× (z -34.1) |
| [[SW1417 (line)]] | alt | 298 | 4 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.183× (z -23.2) |
| [[BT-474 (line)]] | alt | 514 | 1 | 10 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.99× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.122× (z -19.4) |
| [[LS 180 (line)]] | wt | 218 | 6 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +15.9) | [[Panobinostat (drug)]] 5 µM 0.158× (z -24.8) |
| [[Panc 03.27 (line)]] | alt | 775 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0633× (z -28.6) |
| [[A498 (line)]] | wt | 683 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0583× (z -31.0) |
| [[HEC-1-A (line)]] | alt | 497 | 1 | 9 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 5.21× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.156× (z -23.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.199× (z -21.2) |
| [[LOX-IMVI (line)]] | wt | 425 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0597× (z -30.9) |
| [[NCI-H2347 (line)]] | alt | 406 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0755× (z -26.7) |
| [[SW 900 (line)]] | alt | 552 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0512× (z -23.7) |
| [[HS-578T (line)]] | alt | 211 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0896× (z -22.1) |
| [[LoVo (line)]] | wt | 170 | 6 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +17.6) | [[Panobinostat (drug)]] 5 µM 0.186× (z -24.6) |
| [[NCI-H2030 (line)]] | alt | 165 | 4 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.6× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.264× (z -14.1) |
| [[SNU-423 (line)]] | alt | 296 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -22.3) |
| [[A549 (line)]] | wt | 592 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0426× (z -23.9) |
| [[C32 (line)]] | wt | 243 | 3 | 5 | [[TAK-901 (drug)]] 5 µM 12.8× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.195× (z -17.3) |
| [[HT-29 (line)]] | alt | 149 | 3 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +17.2) | [[Panobinostat (drug)]] 5 µM 0.112× (z -27.3) |
| [[hTERT-HPNE (line)]] | wt | 267 | 1 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.0959× (z -23.8) |
| [[NCI-H460 (line)]] | wt | 205 | 2 (2 ⚠) | 6 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.98× (z +8.7) ⚠ unreliable plate only | [[Panobinostat (drug)]] 5 µM 0.122× (z -26.9) |
| [[RPMI-7951 (line)]] | alt | 450 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.113× (z -18.4) |
| [[SK-MEL-2 (line)]] | alt | 179 | 2 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.177× (z -18.6) |
| [[AsPC-1 (line)]] | alt | 364 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +13.8) | [[Panobinostat (drug)]] 5 µM 0.0815× (z -25.0) |
| [[CHP-212 (line)]] | wt | 423 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0628× (z -22.7) |
| [[HepG2_C3A (line)]] | wt | 487 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.02× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.108× (z -22.4) |
| [[NCI-H1573 (line)]] | alt | 351 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.46× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -24.1) |
| [[SNU-1 (line)]] | wt | 146 | 3 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.0981× (z -22.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.328× (z -11.4) |
| [[SW480 (line)]] | alt | 69.3 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +19.0) | [[Panobinostat (drug)]] 5 µM 0.183× (z -21.5) |
| [[A-172 (line)]] | wt | 202 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.157× (z -21.2) |
| [[HOP62 (line)]] | alt | 203 | 2 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.0892× (z -23.2) |
| [[J82 (line)]] | alt | 227 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.104× (z -19.0) |
| [[COLO 205 (line)]] | alt | 357 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0531× (z -21.9) |
| [[H4 (line)]] | wt | 183 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.0986× (z -20.0) |
| [[KATO III (line)]] | alt | 135 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -20.2) |
| [[PANC-1 (line)]] | alt | 90.9 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.282× (z -16.1) |
| [[SW48 (line)]] | wt | 105 | 3 | 2 | [[PH-797804 (drug)]] 5 µM 15.8× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.254× (z -11.1) |
| [[RKO (line)]] | wt | 161 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -19.7) |
| [[SW 1088 (line)]] | alt | 124 | 0 | 1 | — | [[Monocrotaline (drug)]] 5 µM 0.0814× (z -8.5) |
| [[A-427 (line)]] | wt | 64.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 41.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 50.6 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 64.2 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 15.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 62.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 67.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11113), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL18]] | +0.61 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ZNF620]] | +0.59 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[ZNF764]] | +0.55 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[ZNF644]] | +0.55 | +0.43 / +0.54 | both halves | 4e-05 |  |
| [[ZNF407-AS1]] | +0.55 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[NAIF1]] | +0.54 | +0.48 / +0.37 | both halves | 8e-05 |  |
| [[FAM200A]] | +0.53 | +0.44 / +0.34 | both halves | 1e-04 |  |
| [[ZNF268]] | +0.53 | +0.52 / +0.36 | both halves | 1e-04 |  |
| [[ZNF75A]] | +0.52 | +0.49 / +0.23 | both halves | 5e-04 |  |
| [[ELAC1]] | +0.52 | +0.32 / +0.39 | both halves | 2e-04 |  |
| [[ZBED9]] | +0.52 | +0.43 / +0.36 | both halves | 9e-05 |  |
| [[SH3RF1]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCUN1D2]] | -0.58 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[LONP1]] | -0.52 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[GMCL1]] | -0.51 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[CTDP1]] | -0.50 | -0.37 / -0.42 | both halves | 7e-05 |  |
| [[SLC31A1]] | -0.50 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[KYAT1]] | -0.50 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[GPR107]] | -0.50 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[PPP1R32]] | -0.49 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[SRP54-AS1]] | -0.49 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[PIK3C2A]] | -0.48 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[FAM118A]] | -0.48 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[SEL1L]] | -0.48 | -0.35 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR2F1-AS1]] | B | NR2F1-AS1 activity lowers NRIP1's level | lines that do not express NR2F1-AS1 (8) vs lines expressing it (42) | 1.64× higher at baseline in the lines without NR2F1-AS1 | 0.076 | ⚠ within organs, on part of the lines; also absent: TGFB1, NR2F1, PCDH15 |
| [[IFIT2]] | B | IFIT2 activity raises NRIP1's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 2.73× lower at baseline in the lines without IFIT2 | 0.094 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LONP1]] | B | NRIP1 activity lowers LONP1's level | lines that do not express NRIP1 (8) vs lines expressing it (42) | 1.32× higher at baseline in the lines without NRIP1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |
| [[RBPMS]] | B | NRIP1 activity raises RBPMS's level | lines that do not express NRIP1 (8) vs lines expressing it (42) | 4.39× lower at baseline in the lines without NRIP1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |
| [[CTDP1]] | B | NRIP1 activity lowers CTDP1's level | lines that do not express NRIP1 (8) vs lines expressing it (42) | 1.49× higher at baseline in the lines without NRIP1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |
| [[ZNF407-AS1]] | B | NRIP1 activity lowers ZNF407-AS1's level | lines that do not express NRIP1 (8) vs lines expressing it (42) | 1.64× higher at baseline in the lines without NRIP1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |
| [[LYRM2]] | B | NRIP1 activity lowers LYRM2's level | lines that do not express NRIP1 (8) vs lines expressing it (42) | 1.54× higher at baseline in the lines without NRIP1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |
| [[ZNF764]] | B | NRIP1 activity lowers ZNF764's level | lines that do not express NRIP1 (8) vs lines expressing it (42) | 1.36× higher at baseline in the lines without NRIP1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |
| [[ELAC1]] | B | NRIP1 activity lowers ELAC1's level | lines that do not express NRIP1 (8) vs lines expressing it (42) | 1.62× higher at baseline in the lines without NRIP1 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |
| [[DDX20]] | B | NRIP1 activity lowers DDX20's level | lines that do not express NRIP1 (8) vs lines expressing it (42) | 1.58× higher at baseline in the lines without NRIP1 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |
| cells under [[Adagrasib (drug)]] 5 µM | B | NRIP1 activity raises the cells' numbers under Adagrasib 5 µM (protects the cells) | lines that do not express NRIP1 (8) vs lines expressing it (40) | the lines without NRIP1: 0.78× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |
| [[ZNF268]] | B | NRIP1 activity lowers ZNF268's level | lines that do not express NRIP1 (8) vs lines expressing it (42) | 1.82× higher at baseline in the lines without NRIP1 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |
| [[ZNF414]] | B | NRIP1 activity lowers ZNF414's level | lines that do not express NRIP1 (8) vs lines expressing it (42) | 1.23× higher at baseline in the lines without NRIP1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |
| [[ZNF747]] | B | NRIP1 activity lowers ZNF747's level | lines that do not express NRIP1 (8) vs lines expressing it (42) | 1.47× higher at baseline in the lines without NRIP1 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.533). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-27.6, 12.2); signed map (4.6, -26.2). **Vector** length 102, 30.6% of its response variance represented; |z| ≥ 3 in 1,529 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.3 | +10.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.9 | +8.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.5 | +7.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.1 | +11.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +6.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +2.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.5 | +0.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.3 | -0.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.4 | -12.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | -2.7 | -4.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.2 | -3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q11.2-q21.1 — chr21:14,961,235-15,065,936 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RIP140 |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 15 pathways, smallest: NR1H2 & NR1H3 regulate gene expression linked to gluconeogenesis; NR1H2 & NR1H3 regulate gene expression linked to lipogenesis; RORA,B,C and NR1D1 (REV-ERBA) regulate gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [P48552](https://www.uniprot.org/uniprotkb/P48552) (Nuclear receptor-interacting protein 1):

> Modulates transcriptional activation by steroid receptors such as NR3C1, NR3C2 and ESR1. Also modulates transcriptional repression by nuclear hormone receptors. Positive regulator of the circadian clock gene expression: stimulates transcription of BMAL1, CLOCK and CRY1 by acting as a coactivator for RORA and RORC. Involved in the regulation of ovarian function (By similarity). Plays a role in renal development.

**Summary**, from NCBI Gene [8204](https://www.ncbi.nlm.nih.gov/gene/8204):

> Nuclear receptor interacting protein 1 (NRIP1) is a nuclear protein that specifically interacts with the hormone-dependent activation domain AF2 of nuclear receptors. Also known as RIP140, this protein modulates transcriptional activity of the estrogen receptor. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8001](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8001) · Entrez [8204](https://www.ncbi.nlm.nih.gov/gene/8204) · UniProt [P48552](https://www.uniprot.org/uniprotkb/P48552) · Ensembl [ENSG00000180530](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180530)

## Data

Gene col 11113: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11113); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11113, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11113]; `tensor/DDL_lfc|DDL_z.npy` [11113]; `embed/gene_vectors.npy` [11113]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11113 or target_col == 11113). Every well: [[NRIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
