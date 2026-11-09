---
symbol: "MOCOS"
type: "gene"
col: 1127
ensembl_id: "ENSG00000075643"
name: "molybdenum cofactor sulfurase"
location: "18q12.2"
module: 133
arm: "+"
pooled_cpm: 23.23
n_lines_expressing: 43
n_dd_up: 29
n_dd_down: 16
n_dd_up_clean: 23
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# MOCOS

*molybdenum cofactor sulfurase* — 18q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.94× (z +14.2, q 7e-43, up in 34 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.372× (z -14.4, q 2e-44, down in 34 of 40 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.585× (z -8.2, q 4e-14, down in 26 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC6A9]] (+0.80, fdr 7e-06), [[IARS1]] (+0.77, fdr 7e-06), [[YARS1]] (+0.76, fdr 7e-06); moves opposite to [[IFT88]] (-0.49, fdr 5e-05), [[PDHB]] (-0.48, fdr 5e-05), [[CGN]] (-0.47, fdr 4e-05).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC22A15]] → it (grade B ⚠); 1 goes from it, the strongest it → [[KIAA0232]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1127.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +14.2 | 7e-43 | 34/39 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.97×** | +10.3 | 2e-22 | 33/41 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.97×** | +10.2 | 2e-22 | 33/41 (NCI-H460, LoVo, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +8.1 | 6e-14 | 24/39 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.59×** | +7.0 | 3e-10 | 24/39 (LoVo, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.38×** | +6.9 | 6e-10 | 26/41 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.55×** | +6.7 | 2e-09 | 22/41 (NCI-H460, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +5.9 | 3e-07 | 21/41 (LoVo, A498, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.45×** | +5.7 | 1e-06 | 20/41 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Neratinib (drug)]] 5 µM |  | **1.43×** | +5.4 | 3e-06 | 17/41 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.4 | 3e-06 | 18/38 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.42×** | +5.0 | 3e-05 | 13/38 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.36×** | +4.7 | 1e-04 | 17/41 (A549, HOP62, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.6 | 2e-04 | 18/36 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.23×** | +4.5 | 3e-04 | 17/41 (LoVo, NCI-H460, …) | two highest doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.73×** | +4.4 | 5e-04 | 14/37 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +4.3 | 5e-04 | 17/40 (NCI-H460, RKO, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.72×** | +4.3 | 5e-04 | 14/38 (NCI-H2347, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.31×** | +4.1 | 0.001 | 10/41 (LS 180, H4, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1127.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.372×** | -14.4 | 2e-44 | 34/40 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.526×** | -13.8 | 6e-41 | 30/40 (PANC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.548×** | -9.1 | 1e-17 | 25/38 (RKO, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.557×** | -8.9 | 9e-17 | 26/41 (PANC-1, LoVo, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.585×** | -8.2 | 4e-14 | 26/40 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.621×** | -7.2 | 4e-11 | 25/39 (RKO, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.658×** | -6.4 | 2e-08 | 21/40 (PANC-1, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.682×** | -5.8 | 4e-07 | 24/41 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.699×** | -5.5 | 3e-06 | 18/41 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.515×** | -5.3 | 7e-06 | 19/37 (HCT15, H4, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.708×** | -5.2 | 7e-06 | 20/41 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.708×** | -5.2 | 7e-06 | 23/41 (PANC-1, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.812×** | -4.5 | 3e-04 | 18/41 (A-427, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.766×** | -3.7 | 0.007 | 17/38 (LoVo, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.788×** | -3.6 | 0.010 | 14/41 (KATO III, SW48, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.797×** | -3.5 | 0.020 | 15/40 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.871× | -3.0 | 0.093 | 17/41 (KATO III, LS 180, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.65 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1127. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 60.8 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -17.6) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.173× (z -12.7) |
| [[LoVo (line)]] | wt | 70.0 | 1 | 10 (5 ⚠) | [[Neratinib (maleate) (drug)]] 5 µM 2.03× (z +8.6) | [[Harringtonine (drug)]] 5 µM 0.100× (z -19.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.176× (z -15.0) |
| [[PANC-1 (line)]] | alt | 18.2 | 1 | 8 (7 ⚠) | [[Pentamidine (isethionate) (drug)]] 5 µM 2.18× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -20.2) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.204× (z -12.2) |
| [[RKO (line)]] | wt | 56.2 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0581× (z -22.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.193× (z -12.8) |
| [[A-427 (line)]] | wt | 37.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -15.4) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.411× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 18.5 | 4 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +14.1) | [[Harringtonine (drug)]] 0.5 µM 0.270× (z -10.3) |
| [[A498 (line)]] | wt | 51.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -17.6) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.364× (z -9.5) |
| [[HT-29 (line)]] | alt | 29.2 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -18.0) ⚠ cell-cycle shift, explains ~65% of this change |
| [[LS 180 (line)]] | wt | 44.9 | 2 | 2 (2 ⚠) | [[Artesunate (drug)]] 5 µM 3.34× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.3) ⚠ cell-cycle shift, explains ~65% of this change |
| [[J82 (line)]] | alt | 35.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -14.6) ⚠ cell-cycle shift, explains ~65% of this change |
| [[A549 (line)]] | wt | 11.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +8.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -10.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW48 (line)]] | wt | 43.6 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -9.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW480 (line)]] | alt | 10.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.39× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Artesunate (drug)]] 5 µM 2.73× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 8.24 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0770× (z -10.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[C-33 A (line)]] | alt | 7.49 | 0 | 1 | — | [[Captopril (drug)]] 0.5 µM 0.0730× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 7.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +9.0) | — |
| [[H4 (line)]] | wt | 94.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -11.0) ⚠ cell-cycle shift, explains ~65% of this change |
| [[HEC-1-A (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -10.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 47.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -10.9) ⚠ cell-cycle shift, explains ~65% of this change |
| [[NCI-H1573 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.270× (z -8.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H2347 (line)]] | alt | 17.6 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.60× (z +8.5) ⚠ unreliable plate only | — |
| [[SK-MEL-2 (line)]] | alt | 33.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.241× (z -9.8) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.30 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.34 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.44 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.57 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1127), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC6A9]] | +0.80 | +0.75 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_HEME_METABOLISM |
| [[IARS1]] | +0.77 | +0.78 / +0.77 | both halves | 7e-06 |  |
| [[YARS1]] | +0.76 | +0.76 / +0.75 | both halves | 7e-06 | STRING 416 |
| [[XPOT]] | +0.74 | +0.74 / +0.81 | both halves | 7e-06 |  |
| [[PCK2]] | +0.73 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[NBR2]] | +0.73 | +0.66 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[MARS1]] | +0.72 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[KCTD15]] | +0.72 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[MTHFD2]] | +0.72 | +0.70 / +0.79 | both halves | 7e-06 | pathway: Metabolism of vitamins and cofactors |
| [[EIF2S2]] | +0.71 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[CEBPG]] | +0.70 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[NARS1]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT88]] | -0.49 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[PDHB]] | -0.48 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[CGN]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC22A15]] | B | SLC22A15 activity raises MOCOS's level | lines that do not express SLC22A15 (13) vs lines expressing it (37) | 2.44× lower at baseline in the lines without SLC22A15 | 0.062 | ⚠ within organs, on part of the lines; also absent: MCTP2, CARMIL1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA0232]] | B | MOCOS activity raises KIAA0232's level | lines that do not express MOCOS (7) vs lines expressing it (43) | 1.48× lower at baseline in the lines without MOCOS | 0.040 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.809). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.7, 46.8); signed map (-13.6, 23.2). **Vector** length 123, 33.7% of its response variance represented; |z| ≥ 3 in 1,149 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.7 | +10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +14.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +7.0 | +10.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +8.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.5 | +4.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +5.1 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.4 | +4.3 |
|  | [[Neratinib (drug)]] 5 µM |  | +4.2 | +5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +4.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -6.0 | -14.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -4.7 | -5.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.1 | -8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -3.9 | -13.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -3.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Ixazomib (drug)]] 5 µM |  | -2.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | molybdenum cofactor sulfurase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.2 — chr18:36,187,497-36,272,157 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HMCS, FLJ20733, MOS, MCS |
| Gene groups (HGNC) | Molybdenum cofactor synthesis proteins |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 3 pathways, smallest: Molybdenum cofactor biosynthesis; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EN8](https://www.uniprot.org/uniprotkb/Q96EN8) (Molybdenum cofactor sulfurase):

> Sulfurates the molybdenum cofactor. Sulfation of molybdenum is essential for xanthine dehydrogenase (XDH) and aldehyde oxidase (ADO) enzymes in which molybdenum cofactor is liganded by 1 oxygen and 1 sulfur atom in active form.

**Summary**, from NCBI Gene [55034](https://www.ncbi.nlm.nih.gov/gene/55034):

> This gene encodes an enzyme that sulfurates the molybdenum cofactor which is required for activation of the xanthine dehydrogenase (XDH) and aldehyde oxidase (AO) enzymes. XDH catalyzes the conversion of hypoxanthine to uric acid via xanthine, as well as the conversion of allopurinol to oxypurinol, and pyrazinamide to 5-hydroxy pyrazinamide. Mutations in this gene cause the metabolic disorder classical xanthinuria type II which is characterized by the loss of XDH/XO and AO enzyme activity, …

**Accessions** — [HGNC:18234](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18234) · Entrez [55034](https://www.ncbi.nlm.nih.gov/gene/55034) · UniProt [Q96EN8](https://www.uniprot.org/uniprotkb/Q96EN8) · Ensembl [ENSG00000075643](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075643)

## Data

Gene col 1127: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1127); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1127, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1127]; `tensor/DDL_lfc|DDL_z.npy` [1127]; `embed/gene_vectors.npy` [1127]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1127 or target_col == 1127). Every well: [[MOCOS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOCOS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
