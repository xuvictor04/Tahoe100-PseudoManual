---
symbol: "SHLD1"
type: "gene"
col: 10193
ensembl_id: "ENSG00000171984"
name: "shieldin complex subunit 1"
location: "20p12.3"
module: 64
arm: "+"
pooled_cpm: 18.85
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 25
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# SHLD1

*shieldin complex subunit 1* — 20p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.58× (z +7.5, q 4e-11, up in 27 of 44 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.37× (z +5.3, q 3e-05, up in 16 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.321× (z -19.3, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKAR]] (+0.66, fdr 1e-05), [[TRMT11]] (+0.64, fdr 1e-05), [[PGGT1B]] (+0.62, fdr 1e-05); moves opposite to [[SUN1]] (-0.59, fdr 3e-05), [[CAMTA1]] (-0.54, fdr 1e-04), [[ADAM10]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10193.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +7.5 | 4e-11 | 27/44 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.35×** | +7.3 | 1e-10 | 26/48 (AsPC-1, LoVo, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +5.3 | 3e-05 | 16/47 (C32, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Afatinib (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.013 | 8/48 (A-427, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.096 | 13/48 (BT-474, KATO III, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.44× | +3.2 | 0.11 | 5/46 (BT-474, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.21× | +3.2 | 0.11 | 10/47 (Panc 03.27, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.21× | +3.2 | 0.11 | 8/48 (HepG2/C3A, CFPAC-1, …) | rises with dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.21× | +3.0 | 0.16 | 5/46 (COLO 205, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10193.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.321×** | -19.3 | 0e+00 | 46/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.513×** | -16.0 | 0e+00 | 36/47 (BT-474, LoVo, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.406×** | -15.3 | 0e+00 | 39/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.408×** | -15.2 | 0e+00 | 40/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.435×** | -14.1 | 2e-43 | 41/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.474×** | -12.7 | 8e-35 | 40/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.600×** | -12.3 | 9e-33 | 35/46 (COLO 205, SHP-77, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.486×** | -12.3 | 1e-32 | 31/46 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.546×** | -10.3 | 6e-23 | 33/45 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.578×** | -9.3 | 8e-19 | 32/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.580×** | -8.9 | 3e-17 | 27/46 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.607×** | -8.2 | 2e-14 | 29/43 (J82, PANC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.632×** | -7.8 | 3e-13 | 28/48 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **0.638×** | -7.6 | 1e-12 | 26/43 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.639×** | -7.6 | 1e-12 | 28/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.432×** | -7.4 | 3e-12 | 27/48 (A-427, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.735×** | -7.4 | 5e-12 | 32/48 (NCI-H460, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.817×** | -3.4 | 0.014 | 13/48 (SNU-423, PANC-1, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.689×** | -3.3 | 0.022 | 8/45 (Hs 766T, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.877× | -3.2 | 0.035 | 9/48 (SW 900, A549, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.837× | -2.9 | 0.075 | 16/46 (HepG2/C3A, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10193. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 21.4 | 0 | 10 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -15.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.310× (z -9.9) |
| [[SW480 (line)]] | alt | 30.7 | 0 | 10 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -17.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.268× (z -13.4) |
| [[PANC-1 (line)]] | alt | 13.5 | 0 | 8 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.220× (z -12.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.335× (z -8.7) |
| [[HOP62 (line)]] | alt | 20.6 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -11.7) |
| [[BT-474 (line)]] | alt | 46.2 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0539× (z -17.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.118× (z -8.9) |
| [[RKO (line)]] | wt | 32.9 | 0 | 6 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0553× (z -21.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.130× (z -15.6) |
| [[HEC-1-A (line)]] | alt | 17.5 | 0 | 5 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -10.2) |
| [[LoVo (line)]] | wt | 31.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -17.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.243× (z -11.8) |
| [[LS 180 (line)]] | wt | 37.9 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -13.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.297× (z -9.5) |
| [[COLO 205 (line)]] | alt | 51.2 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -17.6) |
| [[HepG2_C3A (line)]] | wt | 52.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0878× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -9.5) |
| [[J82 (line)]] | alt | 10.7 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0959× (z -12.6) ⚠ toxic; cell-cycle shift, explains ~35% of this change |
| [[NCI-H1573 (line)]] | alt | 15.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -13.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.205× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 29.2 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -10.6) |
| [[SHP-77 (line)]] | alt | 51.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -11.9) |
| [[SNU-423 (line)]] | alt | 11.6 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.138× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.138× (z -10.2) |
| [[A498 (line)]] | wt | 9.06 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -11.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[CFPAC-1 (line)]] | alt | 22.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -11.4) |
| [[H4 (line)]] | wt | 16.5 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0845× (z -10.1) |
| [[KATO III (line)]] | alt | 17.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 6.03× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.268× (z -8.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 12.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -13.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.132× (z -10.2) |
| [[SW 900 (line)]] | alt | 25.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -11.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-427 (line)]] | wt | 15.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -12.4) |
| [[A549 (line)]] | wt | 25.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.261× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -9.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0603× (z -8.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[hTERT-HPNE (line)]] | wt | 7.87 | 0 | 1 | — | [[Mebendazole (drug)]] 0.05 µM 0.0833× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.197× (z -8.6) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 11.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -9.5) |
| [[SNU-1 (line)]] | wt | 24.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.175× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~35% of this change |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.191× (z -8.9) |
| [[A-172 (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10193), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKAR]] | +0.66 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[TRMT11]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[PGGT1B]] | +0.62 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[PIGB]] | +0.60 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[METTL16]] | +0.60 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[MTHFS]] | +0.59 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[METTL25]] | +0.59 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[RMDN2]] | +0.58 | +0.36 / +0.60 | both halves | 1e-04 |  |
| [[TXNRD2]] | +0.58 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[CUL5]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[ZNF195]] | +0.56 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[TRMO]] | +0.56 | +0.43 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUN1]] | -0.59 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[CAMTA1]] | -0.54 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[ADAM10]] | -0.51 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[SRGAP2]] | -0.50 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[DNAAF3]] | -0.49 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[HMG20B]] | -0.49 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[ARHGEF10]] | -0.49 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[PRADC1]] | -0.48 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[FRYL]] | -0.48 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[SIN3A]] | -0.47 | -0.45 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.502). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-17.3, 4.0); signed map (8.0, -40.9). **Vector** length 79.7, 16.2% of its response variance represented; |z| ≥ 3 in 1,254 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +9.1 | +7.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +6.3 | +7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.6 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -1.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.2 | +3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | -3.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +2.0 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.7 | -10.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.2 | -12.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.2 | -19.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -7.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | -2.9 | -8.2 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.1 | -2.0 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.7 | -1.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | shieldin complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.3 — chr20:5,750,393-5,864,395 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25067, RINN3; previously C20orf196 |
| Gene groups (HGNC) | Shieldin complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYI0](https://www.uniprot.org/uniprotkb/Q8IYI0) (Shieldin complex subunit 1):

> Component of the shieldin complex, which plays an important role in repair of DNA double-stranded breaks (DSBs). During G1 and S phase of the cell cycle, the complex functions downstream of TP53BP1 to promote non-homologous end joining (NHEJ) and suppress DNA end resection. Mediates various NHEJ-dependent processes including immunoglobulin class-switch recombination, and fusion of unprotected telomeres.

**Summary**, from NCBI Gene [149840](https://www.ncbi.nlm.nih.gov/gene/149840):

> Involved in negative regulation of double-strand break repair via homologous recombination; positive regulation of double-strand break repair via nonhomologous end joining; and positive regulation of isotype switching. Located in site of double-strand break. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26318](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26318) · Entrez [149840](https://www.ncbi.nlm.nih.gov/gene/149840) · UniProt [Q8IYI0](https://www.uniprot.org/uniprotkb/Q8IYI0) · Ensembl [ENSG00000171984](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171984)

## Data

Gene col 10193: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10193); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10193, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10193]; `tensor/DDL_lfc|DDL_z.npy` [10193]; `embed/gene_vectors.npy` [10193]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10193 or target_col == 10193). Every well: [[SHLD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHLD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
