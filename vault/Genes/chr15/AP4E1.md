---
symbol: "AP4E1"
type: "gene"
col: 1300
ensembl_id: "ENSG00000081014"
name: "adaptor related protein complex 4 subunit epsilon 1"
location: "15q21.2"
module: 11
arm: "+"
pooled_cpm: 37.63
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# AP4E1

*adaptor related protein complex 4 subunit epsilon 1* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.74× (z +17.3, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.787× (z -5.3, q 6e-05, down in 23 of 48 measured lines) ⚠ cell-cycle shift, explains ~23% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.134×, SHP-77 0.286×, SNU-1 0.183×, SK-MEL-2 0.273×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (NCI-H460 0.299×, RKO 0.218×, A549 0.291×, PANC-1 0.467×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (HepG2/C3A 0.128×, NCI-H2030 0.309×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.218×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (BT-474 0.204×); [[Aprepitant (drug)]] 0.5 µM in 1 line (SW 1271 0.0553×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERCC4]] (+0.62, fdr 7e-06), [[NSD1]] (+0.60, fdr 1e-05), [[RAB28]] (+0.59, fdr 1e-05); moves opposite to [[OAT]] (-0.52, fdr 2e-05), [[RADX]] (-0.52, fdr 1e-04), [[NPTN]] (-0.52, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FXYD6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1300.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +17.3 | 0e+00 | 40/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +14.6 | 0e+00 | 37/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.74×** | +12.3 | 1e-32 | 41/47 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.74×** | +11.8 | 4e-30 | 40/48 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.70×** | +11.8 | 6e-30 | 41/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.67×** | +11.3 | 8e-28 | 36/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +10.4 | 3e-23 | 37/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +9.9 | 2e-21 | 36/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.58×** | +9.8 | 8e-21 | 34/47 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.43×** | +7.9 | 2e-13 | 36/47 (A498, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +7.3 | 2e-11 | 30/47 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +6.8 | 6e-10 | 22/48 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.37×** | +6.7 | 1e-09 | 28/47 (A498, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.30×** | +5.9 | 2e-07 | 28/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.29×** | +5.6 | 7e-07 | 22/48 (A498, A549, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +5.1 | 1e-05 | 22/48 (HT-29, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +5.0 | 2e-05 | 15/48 (A549, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +4.6 | 1e-04 | 20/48 (KATO III, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.22×** | +4.5 | 2e-04 | 18/47 (HOP62, C32, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.22×** | +4.4 | 3e-04 | 12/47 (CFPAC-1, NCI-H1573, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +4.0 | 0.002 | 13/48 (RKO, NCI-H460, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.13× | +3.9 | 0.002 | 12/48 (A549, A498, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +3.6 | 0.005 | 19/47 (A-172, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1300.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.134×, SHP-77 0.286×, SNU-1 0.183×, SK-MEL-2 0.273×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (NCI-H460 0.299×, RKO 0.218×, A549 0.291×, PANC-1 0.467×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (HepG2/C3A 0.128×, NCI-H2030 0.309×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.218×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (BT-474 0.204×); [[Aprepitant (drug)]] 0.5 µM in 1 line (SW 1271 0.0553×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.787×** | -5.3 | 6e-05 | 23/48 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.867× | -4.5 | 0.002 | 16/48 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.825×** | -3.9 | 0.012 | 19/44 (NCI-H460, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.838× | -3.9 | 0.012 | 13/48 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.834× | -3.9 | 0.012 | 20/47 (HepG2/C3A, NCI-H2030, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.847× | -3.4 | 0.064 | 10/47 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.873× | -3.0 | 0.20 | 4/48 (NCI-H2030, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1300. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 46.1 | 2 (1 ⚠) | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -14.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 31.6 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +14.0) | — |
| [[LoVo (line)]] | wt | 51.2 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +15.1) | — |
| [[SW480 (line)]] | alt | 35.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +17.6) | — |
| [[A549 (line)]] | wt | 47.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +12.2) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -11.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 47.7 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +13.7) | [[Dinaciclib (drug)]] 0.05 µM 0.218× (z -12.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 17.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +11.1) | — |
| [[KATO III (line)]] | alt | 31.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +11.6) | — |
| [[NCI-H23 (line)]] | alt | 40.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 18.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +11.1) | — |
| [[PANC-1 (line)]] | alt | 52.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.467× (z -10.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 53.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 37.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 36.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 37.9 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +13.2) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[AN3 CA (line)]] | alt | 53.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -11.0) |
| [[BT-474 (line)]] | alt | 20.7 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.204× (z -9.4) |
| [[COLO 205 (line)]] | alt | 18.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 43.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 38.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.128× (z -14.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 25.4 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.95× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 39.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 59.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.403× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 56.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.309× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 48.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 47.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 42.9 | 0 | 1 | — | [[Aprepitant (drug)]] 0.5 µM 0.0553× (z -8.8) |
| [[A-172 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1300), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC4]] | +0.62 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[NSD1]] | +0.60 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[RAB28]] | +0.59 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[CPSF2]] | +0.58 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[LEMD2]] | +0.58 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[PRDM5]] | +0.57 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[PRKAB1]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[PSMD7]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[ATAD2B]] | +0.56 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[MACROH2A2]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[MTG2]] | +0.55 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[MED27]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OAT]] | -0.52 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[RADX]] | -0.52 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[NPTN]] | -0.52 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[LGMN]] | -0.52 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[AZIN2]] | -0.49 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[C14orf132]] | -0.49 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[MARCHF6]] | -0.48 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[RHPN2]] | -0.48 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[HNRNPA1]] | -0.47 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[FXYD6]] | -0.47 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[FKBP7]] | -0.47 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[PTMAP5]] | -0.47 | -0.47 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FXYD6]] | B | FXYD6 activity strengthens AP4E1's drug response | lines that do not express FXYD6 (25) vs lines expressing it (23) | the lines without FXYD6 respond 0.83× as strongly (z diff +1.08); strongest at Homoharringtonine 5 µM: 1.43x vs 1.81x (z diff +2.3) | 0.068 | ⚠ within organs, on part of the lines; also absent: MARK1, KIF1A, MAP6; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.451). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-14.1, 5.2); signed map (-4.9, -21.4). **Vector** length 95.4, 23.2% of its response variance represented; |z| ≥ 3 in 1,145 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.9 | +7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | +3.9 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +10.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.2 | +1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +5.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.9 | -4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -5.9 | -5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -2.0 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | -3.9 | -3.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.5 | -2.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | +0.9 |
|  | [[AZD-8055 (drug)]] 5 µM |  | -1.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 4 subunit epsilon 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:50,908,672-51,005,895 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AP-4-EPSILON, SPG51 |
| Gene groups (HGNC) | Clathrin/coatomer adaptor, adaptin-like, N-terminal domain containing; Adaptor related protein complex 4 |
| Reactome | 5 pathways, smallest: Lysosome Vesicle Biogenesis; Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPM8](https://www.uniprot.org/uniprotkb/Q9UPM8) (AP-4 complex subunit epsilon-1):

> Component of the adaptor protein complex 4 (AP-4). Adaptor protein complexes are vesicle coat components involved both in vesicle formation and cargo selection. They control the vesicular transport of proteins in different trafficking pathways. AP-4 forms a non clathrin-associated coat on vesicles departing the trans-Golgi network (TGN) and may be involved in the targeting of proteins from the trans-Golgi network (TGN) to the endosomal-lysosomal system. It is also involved in protein sorting to …

**Summary**, from NCBI Gene [23431](https://www.ncbi.nlm.nih.gov/gene/23431):

> This gene encodes a member of the adaptor complexes large subunit protein family. These proteins are components of the heterotetrameric adaptor protein complexes, which play important roles in the secretory and endocytic pathways by mediating vesicle formation and sorting of integral membrane proteins. The encoded protein is a large subunit of adaptor protein complex-4, which is associated with both clathrin- and nonclathrin-coated vesicles. Disruption of this gene may be associated with …

**Accessions** — [HGNC:573](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:573) · Entrez [23431](https://www.ncbi.nlm.nih.gov/gene/23431) · UniProt [Q9UPM8](https://www.uniprot.org/uniprotkb/Q9UPM8) · Ensembl [ENSG00000081014](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081014)

## Data

Gene col 1300: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1300); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1300, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1300]; `tensor/DDL_lfc|DDL_z.npy` [1300]; `embed/gene_vectors.npy` [1300]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1300 or target_col == 1300). Every well: [[AP4E1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP4E1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
