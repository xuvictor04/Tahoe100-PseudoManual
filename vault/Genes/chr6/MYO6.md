---
symbol: "MYO6"
type: "gene"
col: 12243
ensembl_id: "ENSG00000196586"
name: "myosin VI"
location: "6q14.1"
module: 5
arm: "-"
pooled_cpm: 265.13
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# MYO6

*myosin VI* — 6q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.27× (z +9.3, q 9e-18, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.739× (z -11.6, q 1e-28, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SVIP]] (+0.59, fdr 3e-05), [[AFDN]] (+0.53, fdr 1e-05), [[GXYLT1]] (+0.52, fdr 4e-05); moves opposite to [[RAVER1]] (-0.50, fdr 3e-05), [[ACAD9]] (-0.50, fdr 3e-05), [[DUS3L]] (-0.48, fdr 2e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[ADGRF1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12243.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +9.3 | 9e-18 | 27/47 (SW480, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +7.8 | 1e-12 | 22/48 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.32×** | +7.7 | 4e-12 | 30/47 (CFPAC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +6.8 | 1e-09 | 29/48 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.24×** | +5.6 | 2e-06 | 26/46 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +5.4 | 8e-06 | 22/47 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.8 | 1e-04 | 24/47 (PANC-1, BT-474, …) | inconsistent across doses | composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.17× | +4.3 | 0.001 | 19/46 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.9 | 0.005 | 18/47 (SNU-423, NCI-H2030, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.15× | +3.8 | 0.010 | 20/47 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.13× | +3.3 | 0.044 | 8/47 (SW480, NCI-H1792, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Retinoic acid (drug)]] 5 µM |  | 1.08× | +3.1 | 0.094 | 3/48 (KATO III, RPMI-7951, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | 1.24× | +3.0 | 0.11 | 11/48 (NCI-H23, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12243.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.739×** | -11.6 | 1e-28 | 30/48 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.679×** | -10.1 | 1e-21 | 31/46 (HT-29, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.816×** | -7.8 | 9e-13 | 27/47 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.757×** | -7.6 | 4e-12 | 26/47 (NCI-H2347, KATO III, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.773×** | -7.0 | 3e-10 | 32/47 (AsPC-1, HT-29, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.659×** | -6.0 | 2e-07 | 31/47 (NCI-H2347, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.673×** | -5.7 | 1e-06 | 29/47 (NCI-H2347, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.677×** | -5.6 | 2e-06 | 33/46 (AsPC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.728×** | -4.5 | 4e-04 | 22/48 (J82, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.892× | -4.4 | 6e-04 | 4/47 (AsPC-1, Panc 03.27, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.741×** | -4.3 | 1e-03 | 23/47 (NCI-H2347, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.860× | -4.1 | 0.002 | 13/47 (NCI-H23, NCI-H1573, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.866× | -3.9 | 0.004 | 15/47 (KATO III, PANC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | 0.879× | -3.4 | 0.031 | 18/43 (LoVo, Panc 03.27, …) | inconsistent across doses | composition shift |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.889× | -3.2 | 0.051 | 10/48 (SW48, LS 180, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.891× | -3.1 | 0.061 | 13/47 (KATO III, PANC-1, …) | all doses, flat |  |
| [[Isocorydine (drug)]] 0.5 µM |  | 0.894× | -3.0 | 0.077 | 7/47 (Panc 03.27, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12243. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 304 | 4 (2 ⚠) | 7 | [[Daptomycin (drug)]] 5 µM 2.12× (z +9.2) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 2.07× (z +8.6) | [[Clobetasol propionate (drug)]] 0.05 µM 0.463× (z -9.5) |
| [[KATO III (line)]] | alt | 420 | 1 (1 ⚠) | 9 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.84× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -14.4) |
| [[HT-29 (line)]] | alt | 609 | 1 (1 ⚠) | 7 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.81× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -17.9) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -14.6) |
| [[NCI-H2347 (line)]] | alt | 1,127 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.329× (z -17.0) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -14.9) |
| [[Panc 03.27 (line)]] | alt | 1,234 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -15.5) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -14.1) |
| [[BT-474 (line)]] | alt | 451 | 4 (4 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.437× (z -12.2) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -11.6) |
| [[LoVo (line)]] | wt | 488 | 2 | 4 (3 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.61× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.412× (z -13.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.530× (z -9.4) |
| [[PANC-1 (line)]] | alt | 290 | 4 (3 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.16× (z +16.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 1.57× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -19.7) |
| [[CFPAC-1 (line)]] | alt | 208 | 5 (3 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.28× (z +12.8) | — |
| [[LS 180 (line)]] | wt | 240 | 5 (3 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.66× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 132 | 1 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.53× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -13.8) |
| [[AsPC-1 (line)]] | alt | 369 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.342× (z -12.5) |
| [[CHP-212 (line)]] | wt | 590 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -14.5) |
| [[NCI-H23 (line)]] | alt | 209 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -13.4) |
| [[SW1417 (line)]] | alt | 290 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.449× (z -12.3) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -10.8) |
| [[COLO 205 (line)]] | alt | 281 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.487× (z -9.6) ⚠ cell-cycle shift, explains ~77% of this change |
| [[MIA PaCa-2 (line)]] | alt | 135 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.13× (z +10.2) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.573× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 197 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -14.1) |
| [[A549 (line)]] | wt | 158 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -9.8) |
| [[HCT15 (line)]] | alt | 290 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.87× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HepG2_C3A (line)]] | wt | 349 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -8.8) |
| [[HS-578T (line)]] | alt | 139 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 138 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.574× (z -8.6) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 114 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -11.5) |
| [[A-427 (line)]] | wt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[A498 (line)]] | wt | 99.0 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.9) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[C32 (line)]] | wt | 112 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 204 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.628× (z -8.8) |
| [[Hs 766T (line)]] | wt | 121 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 109 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.646× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 265 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.59× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[SW 1088 (line)]] | alt | 88.7 | 0 | 1 | — | [[Verapamil (drug)]] 5 µM 0.0546× (z -9.0) |
| [[SW480 (line)]] | alt | 130 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +14.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 165 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 186 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 97.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 191 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 275 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12243), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SVIP]] | +0.59 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[AFDN]] | +0.53 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[GXYLT1]] | +0.52 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[DAPP1]] | +0.51 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[SWAP70]] | +0.50 | +0.34 / +0.60 | both halves | 1e-04 |  |
| [[USP53]] | +0.50 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[GLIPR2]] | +0.50 | +0.37 / +0.45 | both halves | 9e-05 |  |
| [[RALGPS2]] | +0.50 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[PAK1]] | +0.50 | +0.45 / +0.47 | both halves | 3e-05 | pathway: RHOU GTPase cycle; STRING 928 |
| [[GRHL1]] | +0.49 | +0.34 / +0.54 | both halves | 1e-04 |  |
| [[ABTB2]] | +0.49 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[LBH]] | +0.49 | +0.43 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAVER1]] | -0.50 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[ACAD9]] | -0.50 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[DUS3L]] | -0.48 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[NAT10]] | -0.48 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[DDX56]] | -0.46 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[TM9SF4]] | -0.45 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[GTF3C4]] | -0.45 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[COX10]] | -0.44 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[TRMT1]] | -0.44 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[MTERF1]] | -0.44 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[RPTOR]] | -0.44 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[AKAP8]] | -0.44 | -0.28 / -0.55 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRF1]] | B | ADGRF1 activity raises MYO6's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 2.31× lower at baseline in the lines without ADGRF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[CLDN4]] | B | CLDN4 activity raises MYO6's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 2.14× lower at baseline in the lines without CLDN4 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[DAPP1]] | B | DAPP1 activity raises MYO6's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 2.49× lower at baseline in the lines without DAPP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[MPZL3]] | B | MPZL3 activity raises MYO6's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.75× lower at baseline in the lines without MPZL3 | 0.015 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[NECTIN4]] | B | NECTIN4 activity raises MYO6's level | lines that do not express NECTIN4 (33) vs lines expressing it (17) | 1.91× lower at baseline in the lines without NECTIN4 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25 |
| [[MYO5B]] | B | MYO5B activity raises MYO6's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 1.85× lower at baseline in the lines without MYO5B | 0.034 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[VNN1]] | B | VNN1 activity raises MYO6's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 1.50× lower at baseline in the lines without VNN1 | 0.037 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[JUP]] | B | JUP activity raises MYO6's level | lines that do not express JUP (16) vs lines expressing it (34) | 1.83× lower at baseline in the lines without JUP | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[ADGRF1]] | B | ADGRF1 activity strengthens MYO6's drug response | lines that do not express ADGRF1 (34) vs lines expressing it (14) | the lines without ADGRF1 respond 0.83× as strongly (z diff +0.46); rises at some drug-doses, falls at others (39% from rises): Topotecan (hydrochloride) 5 µM: 0.77x vs 0.55x (z diff +3.3); Daptomycin 5 µM: 1.24x vs 1.53x (z diff +2.2); Vinblastine (sulfate) 5 µM: 1.17x vs 1.39x (z diff +2.2) | 0.045 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |
| [[MAP7]] | B | MAP7 activity raises MYO6's level | lines that do not express MAP7 (21) vs lines expressing it (29) | 1.89× lower at baseline in the lines without MAP7 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: MST1R, ENTPD2, TC2N |
| [[FGD6]] | B | FGD6 activity raises MYO6's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 1.60× lower at baseline in the lines without FGD6 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[RAB3IP]] | B | RAB3IP activity raises MYO6's level | lines that do not express RAB3IP (8) vs lines expressing it (42) | 1.81× lower at baseline in the lines without RAB3IP | 0.092 | ⚠ within organs, on part of the lines; also absent: TBC1D30, CXCL16, ENSG00000288591; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.302). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-17.2, 31.1); signed map (6.1, 20.7). **Vector** length 143, 47.6% of its response variance represented; |z| ≥ 3 in 1,623 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.4 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +9.2 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.4 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | +7.8 | -3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.2 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.8 | +7.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.8 | +3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.7 | +5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.4 | +5.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.9 | -4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.9 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.7 | -7.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.7 | -6.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.1 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -7.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.9 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | myosin VI |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.1 — chr6:75,749,201-75,919,537 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0389; previously DFNA22, DFNB37 |
| Gene groups (HGNC) | Myosin heavy chains, class VI |
| Reactome | 17 pathways, smallest: Gap junction degradation; RHOBTB1 GTPase cycle; RHOBTB2 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UM54](https://www.uniprot.org/uniprotkb/Q9UM54) (Unconventional myosin-VI):

> Myosins are actin-based motor molecules with ATPase activity (By similarity). Unconventional myosins serve in intracellular movements (By similarity). Myosin 6 is a reverse-direction motor protein that moves towards the minus-end of actin filaments. Has slow rate of actin-activated ADP release due to weak ATP binding (By similarity). Functions in a variety of intracellular processes such as vesicular membrane trafficking and cell migration (By similarity). Required for the structural integrity …

**Summary**, from NCBI Gene [4646](https://www.ncbi.nlm.nih.gov/gene/4646):

> This gene encodes a reverse-direction motor protein that moves toward the minus end of actin filaments and plays a role in intracellular vesicle and organelle transport. The protein consists of a motor domain containing an ATP- and an actin-binding site and a globular tail which interacts with other proteins. This protein maintains the structural integrity of inner ear hair cells and mutations in this gene cause non-syndromic autosomal dominant and recessive hearing loss. Alternative splicing …

**Accessions** — [HGNC:7605](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7605) · Entrez [4646](https://www.ncbi.nlm.nih.gov/gene/4646) · UniProt [Q9UM54](https://www.uniprot.org/uniprotkb/Q9UM54) · Ensembl [ENSG00000196586](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196586)

## Data

Gene col 12243: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12243); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12243, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12243]; `tensor/DDL_lfc|DDL_z.npy` [12243]; `embed/gene_vectors.npy` [12243]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12243 or target_col == 12243). Every well: [[MYO6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
