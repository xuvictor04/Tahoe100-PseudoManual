---
symbol: "SH3BP4"
type: "gene"
col: 5023
ensembl_id: "ENSG00000130147"
name: "SH3 domain binding protein 4"
location: "2q37.2"
module: 36
arm: "+"
pooled_cpm: 60.52
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# SH3BP4

*SH3 domain binding protein 4* — 2q37.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.74× (z +5.4, q 2e-05, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.599× (z -13.4, q 4e-38, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LARP1]] (+0.56, fdr 1e-05), [[UPF1]] (+0.49, fdr 2e-05), [[STXBP5]] (+0.49, fdr 3e-05); moves opposite to [[ETNK1]] (-0.47, fdr 2e-05), [[TFF1]] (-0.46, fdr 4e-05), [[CEMIP]] (-0.46, fdr 5e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5023.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.74×** | +5.4 | 2e-05 | 29/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +5.4 | 2e-05 | 25/47 (A498, C32, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.71×** | +5.2 | 3e-05 | 24/46 (C32, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.26×** | +4.4 | 0.001 | 21/47 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 0.001 | 22/47 (NCI-H1792, SW 900, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.21×** | +3.6 | 0.026 | 16/46 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.026 | 16/47 (NCI-H1792, SW 900, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.13× | +3.4 | 0.048 | 11/47 (HOP62, H4, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.048 | 17/46 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.19× | +3.3 | 0.049 | 18/47 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.19× | +3.3 | 0.053 | 18/47 (NCI-H1792, AsPC-1, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.057 | 16/47 (C32, A498, …) | top dose only | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.074 | 8/47 (SW1417, NCI-H1792, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.20× | +3.1 | 0.075 | 17/47 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5023.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -13.4 | 4e-38 | 36/47 (SW1417, HS-578T, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.518×** | -11.3 | 3e-27 | 28/38 (NCI-H460, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.552×** | -11.1 | 4e-26 | 40/47 (PANC-1, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.569×** | -10.5 | 1e-23 | 39/47 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.571×** | -10.4 | 2e-23 | 36/45 (A-172, HCT15, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.671×** | -10.4 | 2e-23 | 33/46 (LOX-IMVI, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.578×** | -9.8 | 9e-21 | 38/48 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.630×** | -8.3 | 9e-15 | 26/37 (SW480, SW1417, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.668×** | -7.2 | 3e-11 | 26/46 (LOX-IMVI, NCI-H1573, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.686×** | -7.0 | 1e-10 | 30/47 (PANC-1, SW1417, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -6.8 | 5e-10 | 28/47 (HS-578T, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.734×** | -5.5 | 2e-06 | 25/44 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.748×** | -5.4 | 3e-06 | 25/47 (HCT15, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.750×** | -5.3 | 4e-06 | 25/47 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -3.4 | 0.021 | 3/48 (NCI-H23, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5023. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 58.2 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -24.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -12.2) |
| [[PANC-1 (line)]] | alt | 99.5 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.39× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -17.7) |
| [[SW480 (line)]] | alt | 69.8 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -17.0) |
| [[A-172 (line)]] | wt | 73.5 | 1 (1 ⚠) | 5 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.80× (z +9.6) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -11.9) |
| [[HS-578T (line)]] | alt | 91.1 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -17.2) |
| [[J82 (line)]] | alt | 59.9 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.351× (z -10.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.359× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 82.8 | 4 | 1 (1 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 2.50× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.283× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[SW1417 (line)]] | alt | 90.3 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -18.2) |
| [[HCT15 (line)]] | alt | 198 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -16.4) |
| [[RPMI-7951 (line)]] | alt | 88.0 | 1 (1 ⚠) | 3 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.78× (z +8.5) ⚠ unreliable plate only | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 58.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -13.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 110 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -11.8) |
| [[A498 (line)]] | wt | 56.6 | 2 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.77× (z +10.9) ⚠ unreliable plate only | — |
| [[C32 (line)]] | wt | 42.4 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.10× (z +10.1) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -11.2) |
| [[HOP62 (line)]] | alt | 66.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -8.5) |
| [[RKO (line)]] | wt | 24.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -12.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 50.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -10.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SNU-423 (line)]] | alt | 158 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -13.7) |
| [[A549 (line)]] | wt | 41.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[AsPC-1 (line)]] | alt | 47.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 45.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.295× (z -9.8) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 49.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0884× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[COLO 205 (line)]] | alt | 71.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -14.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HepG2_C3A (line)]] | wt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.358× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[HT-29 (line)]] | alt | 53.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -9.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 61.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -11.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.447× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[LoVo (line)]] | wt | 41.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -8.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LS 180 (line)]] | wt | 55.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[MIA PaCa-2 (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 38.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -11.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H23 (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.212× (z -10.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 25.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -17.1) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 54.6 | 0 | 1 | — | [[Elimusertib hydrochloride (drug)]] 0.5 µM 0.265× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 55.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -8.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 53.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -10.2) |
| [[SW48 (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -8.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 88.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.18 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5023), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARP1]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[UPF1]] | +0.49 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[STXBP5]] | +0.49 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[KPNA3]] | +0.49 | +0.56 / +0.35 | both halves | 1e-04 |  |
| [[HIPK2]] | +0.48 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[SORBS2]] | +0.48 | +0.34 / +0.49 | both halves | 1e-04 | same gene group |
| [[SYBU]] | +0.47 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[ZFYVE9]] | +0.46 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[MYC]] | +0.46 | +0.53 / +0.34 | both halves | 1e-04 |  |
| [[NDST1]] | +0.46 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[GLUL]] | +0.46 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[HEG1]] | +0.45 | +0.46 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETNK1]] | -0.47 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[TFF1]] | -0.46 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[CEMIP]] | -0.46 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[C15orf48]] | -0.45 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[SYTL5]] | -0.45 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[CCNYL1]] | -0.45 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[WNT7B]] | -0.44 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[CYP27C1]] | -0.43 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[ARL5B]] | -0.43 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[MXD1]] | -0.43 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[CEP95]] | -0.42 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[LUCAT1]] | -0.42 | -0.46 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SH3BP4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DUSP1]] | B | DUSP1 activity raises SH3BP4's level | lines that do not express DUSP1 (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without DUSP1 | 0.073 | ⚠ within organs, on part of the lines; also absent: PC, PLD1, DENND3; maybe low, not absent |
| [[TGFBR2]] | B | TGFBR2 activity raises SH3BP4's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 2.31× lower at baseline in the lines without TGFBR2 | 0.089 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.330). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (32.4, 16.5); signed map (19.8, 33.1). **Vector** length 100.0, 24.7% of its response variance represented; |z| ≥ 3 in 1,324 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.4 | +5.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.3 | +5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | +4.0 | +3.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +1.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.5 | +3.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.5 | +2.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +3.4 | +1.7 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | -6.3 | -8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -5.9 | -10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.1 | -11.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -13.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -9.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.9 | -1.2 |
|  | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | SH3 domain binding protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.2 — chr2:234,952,017-235,055,714 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ZU5 domain containing ; SH3 domain containing |
| Reactome | 4 pathways, smallest: Amino acids regulate mTORC1; Cellular response to starvation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0V3](https://www.uniprot.org/uniprotkb/Q9P0V3) (SH3 domain-binding protein 4):

> May function in transferrin receptor internalization at the plasma membrane through a cargo-specific control of clathrin-mediated endocytosis. Alternatively, may act as a negative regulator of the amino acid-induced TOR signaling by inhibiting the formation of active Rag GTPase complexes. Preferentially binds inactive Rag GTPase complexes and prevents their interaction with the mTORC1 complex inhibiting its relocalization to lysosomes and its activation. Thereby, may indirectly regulate cell …

**Summary**, from NCBI Gene [23677](https://www.ncbi.nlm.nih.gov/gene/23677):

> This gene encodes a protein with 3 Asn-Pro-Phe (NPF) motifs, an SH3 domain, a PXXP motif, a bipartite nuclear targeting signal, and a tyrosine phosphorylation site. This protein is involved in cargo-specific control of clathrin-mediated endocytosis, specifically controlling the internalization of a specific protein receptor. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10826](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10826) · Entrez [23677](https://www.ncbi.nlm.nih.gov/gene/23677) · UniProt [Q9P0V3](https://www.uniprot.org/uniprotkb/Q9P0V3) · Ensembl [ENSG00000130147](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130147)

## Data

Gene col 5023: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5023); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5023, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5023]; `tensor/DDL_lfc|DDL_z.npy` [5023]; `embed/gene_vectors.npy` [5023]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5023 or target_col == 5023). Every well: [[SH3BP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3BP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
