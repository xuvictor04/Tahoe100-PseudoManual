---
symbol: "SNX25"
type: "gene"
col: 3078
ensembl_id: "ENSG00000109762"
name: "sorting nexin 25"
location: "4q35.1"
module: 134
arm: "+"
pooled_cpm: 149.08
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 28
n_dd_up_clean: 1
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# SNX25

*sorting nexin 25* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[PF-06260933 (drug)]] 5 µM: 1.50× (z +3.8, q 0.084, up in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW 900 2.57×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.411× (z -16.0, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.615× (z -12.4, q 4e-33, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIAA1958]] (+0.73, fdr 7e-06), [[FAM117B]] (+0.70, fdr 7e-06), [[ANKRD37]] (+0.67, fdr 1e-05, ⚠ same locus), [[KDM4B]] (+0.65, fdr 1e-05); moves opposite to [[PGGT1B]] (-0.62, fdr 2e-05), [[CENPBD1P]] (-0.61, fdr 3e-05), [[ZNF747]] (-0.61, fdr 3e-04).
> It is in [[Module 134]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3078.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW 900 2.57×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PF-06260933 (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.084 | 26/48 (HOP62, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 1.44× | +3.4 | 0.19 | 22/48 (SW480, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.2 | 0.22 | 23/48 (SW 900, LoVo, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.18× | +3.0 | 0.34 | 15/48 (PANC-1, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3078.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.411×** | -16.0 | 0e+00 | 46/49 (RKO, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.408×** | -15.5 | 0e+00 | 43/44 (CFPAC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.615×** | -12.4 | 4e-33 | 37/48 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.484×** | -12.1 | 2e-31 | 40/45 (CFPAC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.519×** | -11.4 | 6e-28 | 40/48 (C32, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.557×** | -10.5 | 5e-24 | 38/48 (NCI-H23, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.590×** | -9.1 | 5e-18 | 43/47 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -7.7 | 9e-13 | 30/49 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.670×** | -7.2 | 3e-11 | 40/48 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.694×** | -6.6 | 2e-09 | 36/48 (C32, HCT15, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~20% of this change | **0.754×** | -5.1 | 2e-05 | 33/48 (C32, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **0.606×** | -4.7 | 1e-04 | 32/48 (NCI-H1573, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.771×** | -4.7 | 1e-04 | 28/48 (C32, HOP62, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.611×** | -4.6 | 1e-04 | 29/49 (A498, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.779×** | -4.5 | 2e-04 | 27/48 (CFPAC-1, C32, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.782×** | -4.5 | 3e-04 | 28/48 (CFPAC-1, C32, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.776×** | -4.4 | 3e-04 | 32/48 (NCI-H1573, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.813×** | -3.7 | 0.005 | 24/48 (C32, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.816×** | -3.7 | 0.006 | 24/48 (HT-29, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.682×** | -3.6 | 0.008 | 25/48 (SW480, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.682×** | -3.6 | 0.008 | 25/47 (RPMI-7951, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3078. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 281 | 0 | 14 (7 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.235× (z -16.8) |
| [[NCI-H1573 (line)]] | alt | 204 | 0 | 10 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.253× (z -13.4) ⚠ toxic; cell-cycle shift, explains ~53% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.357× (z -10.0) |
| [[A-172 (line)]] | wt | 198 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -17.3) |
| [[CFPAC-1 (line)]] | alt | 310 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -16.4) |
| [[NCI-H2347 (line)]] | alt | 222 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -15.2) |
| [[HOP62 (line)]] | alt | 167 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.409× (z -9.8) |
| [[J82 (line)]] | alt | 196 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -12.8) |
| [[SNU-423 (line)]] | alt | 117 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.334× (z -11.7) |
| [[SW48 (line)]] | wt | 196 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -9.0) |
| [[SW480 (line)]] | alt | 247 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -16.2) |
| [[HCT15 (line)]] | alt | 273 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.367× (z -14.5) |
| [[HepG2_C3A (line)]] | wt | 226 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.493× (z -10.4) |
| [[KATO III (line)]] | alt | 154 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 150 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -15.8) |
| [[HEC-1-A (line)]] | alt | 112 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.358× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 131 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -16.3) |
| [[LS 180 (line)]] | wt | 175 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.246× (z -13.7) |
| [[NCI-H23 (line)]] | alt | 113 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -28.5) |
| [[SK-MEL-2 (line)]] | alt | 137 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.441× (z -12.5) |
| [[HS-578T (line)]] | alt | 125 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -14.9) |
| [[LoVo (line)]] | wt | 160 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.422× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.606× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 152 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -9.0) |
| [[RKO (line)]] | wt | 194 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.469× (z -8.9) |
| [[A-427 (line)]] | wt | 90.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -24.5) |
| [[AN3 CA (line)]] | alt | 212 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 148 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 68.2 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.342× (z -10.6) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.408× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 128 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.391× (z -9.1) |
| [[SNU-1 (line)]] | wt | 79.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.236× (z -11.3) |
| [[A498 (line)]] | wt | 68.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.445× (z -10.0) |
| [[C-33 A (line)]] | alt | 217 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.353× (z -9.3) |
| [[HT-29 (line)]] | alt | 96.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -11.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 162 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -16.4) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 89.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0602× (z -13.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.357× (z -10.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 86.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 108 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0727× (z -13.1) |
| [[SW 900 (line)]] | alt | 107 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 82.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 93.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 90.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 64.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 123 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3078), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1958]] | +0.73 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[FAM117B]] | +0.70 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.67 | +0.71 / +0.53 | both halves | 1e-05 | STRING 419; ⚠ same locus (25.8 kb, same strand: neighbours can correlate without regulation) |
| [[KDM4B]] | +0.65 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[BNIP3L]] | +0.62 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[NGLY1]] | +0.62 | +0.69 / +0.46 | both halves | 2e-05 |  |
| [[UBA6]] | +0.61 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[SLC2A3]] | +0.60 | +0.65 / +0.38 | both halves | 6e-05 |  |
| [[SUN1]] | +0.59 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[NARF]] | +0.59 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[DNAJC5]] | +0.59 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[RERE]] | +0.59 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[STK32C]] | +0.59 | +0.56 / +0.37 | both halves | 7e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGGT1B]] | -0.62 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[CENPBD1P]] | -0.61 | -0.69 / -0.44 | both halves | 3e-05 |  |
| [[ZNF747]] | -0.61 | -0.68 / -0.28 | both halves | 3e-04 |  |
| [[ZXDA]] | -0.60 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[ZNF793]] | -0.60 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[FIZ1]] | -0.58 | -0.65 / -0.31 | both halves | 2e-04 |  |
| [[ZNF268]] | -0.58 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[CC2D2A]] | -0.58 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[EXOSC10]] | -0.58 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[ZNF181]] | -0.58 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[ZNF620]] | -0.57 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[ZNF280D]] | -0.57 | -0.57 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.9, -12.8); signed map (-35.2, 27.8). **Vector** length 109, 36.1% of its response variance represented; |z| ≥ 3 in 1,292 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | -1.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | -2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +4.9 | -4.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.1 | +3.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.4 | +2.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.1 | -10.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.5 | -11.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.9 | -12.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.0 | -4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -7.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -4.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.4 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.3 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:185,204,237-185,370,185 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SBBI31; previously LRP2BP-AS1 |
| Gene groups (HGNC) | Sorting nexins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3E2](https://www.uniprot.org/uniprotkb/Q9H3E2) (Sorting nexin-25):

> May be involved in several stages of intracellular trafficking.

**Summary**, from NCBI Gene [83891](https://www.ncbi.nlm.nih.gov/gene/83891):

> Predicted to enable phosphatidylinositol binding activity. Involved in negative regulation of transforming growth factor beta receptor signaling pathway and receptor catabolic process. Predicted to be located in endosome membrane. Predicted to be active in endosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21883](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21883) · Entrez [83891](https://www.ncbi.nlm.nih.gov/gene/83891) · UniProt [Q9H3E2](https://www.uniprot.org/uniprotkb/Q9H3E2) · Ensembl [ENSG00000109762](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109762)

## Data

Gene col 3078: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3078); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3078, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3078]; `tensor/DDL_lfc|DDL_z.npy` [3078]; `embed/gene_vectors.npy` [3078]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3078 or target_col == 3078). Every well: [[SNX25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
