---
symbol: "PVR"
type: "gene"
col: 1040
ensembl_id: "ENSG00000073008"
name: "PVR cell adhesion molecule"
location: "19q13.31"
module: 65
arm: "-"
pooled_cpm: 54.22
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 14
n_dd_up_clean: 31
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# PVR

*PVR cell adhesion molecule* — 19q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.63× (z +14.7, q 1e-45, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.715× (z -7.1, q 7e-10, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEACAM19]] (+0.69, fdr 7e-06, ⚠ same locus), [[PEA15]] (+0.60, fdr 1e-05), [[BICD1]] (+0.57, fdr 2e-05), [[NBPF20]] (+0.56, fdr 1e-05); moves opposite to [[MXI1]] (-0.59, fdr 1e-05), [[BAG4]] (-0.56, fdr 2e-05), [[ALDH6A1]] (-0.55, fdr 1e-05).
> It sits in the **-** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1040.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +14.7 | 1e-45 | 35/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.94×** | +14.0 | 4e-42 | 42/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +14.0 | 4e-42 | 42/47 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.73×** | +11.6 | 5e-29 | 41/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.68×** | +10.9 | 1e-25 | 39/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.66×** | +10.7 | 7e-25 | 37/48 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.40×** | +10.0 | 1e-21 | 36/48 (HT-29, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.59×** | +9.8 | 1e-20 | 37/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +9.4 | 3e-19 | 36/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +8.8 | 6e-17 | 35/48 (HT-29, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.50×** | +8.5 | 1e-15 | 38/47 (HT-29, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.51×** | +8.3 | 5e-15 | 31/47 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.47×** | +8.2 | 1e-14 | 36/47 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +7.6 | 1e-12 | 28/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +7.5 | 2e-12 | 27/46 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +7.3 | 7e-12 | 28/47 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +6.7 | 7e-10 | 24/48 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.36×** | +6.4 | 4e-09 | 31/47 (HT-29, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +6.1 | 3e-08 | 28/48 (HT-29, SW480, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.92×** | +5.7 | 3e-07 | 25/45 (HT-29, HOP62, …) | rises with dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, none with an alert; shown: the 15 strongest. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1040.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.715×** | -7.1 | 7e-10 | 27/48 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.731×** | -6.6 | 9e-09 | 26/48 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.735×** | -6.5 | 2e-08 | 25/48 (J82, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.822×** | -5.9 | 6e-07 | 19/48 (HEC-1-A, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.805×** | -4.6 | 5e-04 | 15/49 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.832×** | -4.6 | 5e-04 | 18/48 (SK-MEL-2, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.811×** | -4.4 | 7e-04 | 20/48 (A-172, PANC-1, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.815×** | -4.3 | 0.001 | 14/48 (J82, A498, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.867× | -4.3 | 0.001 | 17/48 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.872× | -4.1 | 0.002 | 14/49 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **0.825×** | -4.1 | 0.003 | 19/48 (KATO III, J82, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.828×** | -4.0 | 0.003 | 20/48 (RKO, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.823×** | -4.0 | 0.003 | 20/47 (SW 1271, H4, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.831×** | -3.9 | 0.004 | 17/48 (NCI-H1792, J82, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.857× | -3.9 | 0.004 | 15/48 (SK-MEL-2, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1040. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 77.4 | 13 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +13.9) | — |
| [[PANC-1 (line)]] | alt | 37.7 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.25× (z +34.2) | — |
| [[SW480 (line)]] | alt | 49.1 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.36× (z +10.3) | — |
| [[A498 (line)]] | wt | 78.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +23.5) | — |
| [[A549 (line)]] | wt | 126 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +21.0) | [[Panobinostat (drug)]] 0.5 µM 0.398× (z -9.2) |
| [[RKO (line)]] | wt | 108 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.328× (z -12.4) |
| [[SW 900 (line)]] | alt | 33.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +12.5) | — |
| [[A-172 (line)]] | wt | 53.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +21.0) | — |
| [[HEC-1-A (line)]] | alt | 95.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -12.0) |
| [[J82 (line)]] | alt | 123 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.2) | [[Selinexor (drug)]] 5 µM 0.389× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.411× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 73.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 68.5 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.380× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.366× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 46.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +16.6) | — |
| [[HS-578T (line)]] | alt | 52.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +11.7) | — |
| [[hTERT-HPNE (line)]] | wt | 22.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +12.4) | — |
| [[NCI-H1573 (line)]] | alt | 18.4 | 2 (1 ⚠) | 0 | [[Daptomycin (drug)]] 5 µM 4.19× (z +8.6) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 2.73× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 78.1 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 3.62× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 47.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +18.0) | — |
| [[C-33 A (line)]] | alt | 37.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -13.5) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 62.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +16.4) | — |
| [[HOP62 (line)]] | alt | 101 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +15.8) | — |
| [[KATO III (line)]] | alt | 78.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.407× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 56.3 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.67× (z +8.7) ⚠ unreliable plate only | — |
| [[NCI-H23 (line)]] | alt | 49.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.374× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 45.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 26.5 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.70× (z +9.7) ⚠ unreliable plate only | — |
| [[A-427 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1040), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEACAM19]] | +0.69 | +0.61 / +0.70 | both halves | 7e-06 | same gene group; STRING 505; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PEA15]] | +0.60 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[BICD1]] | +0.57 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[NBPF20]] | +0.56 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SLC36A1]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[PUS1]] | +0.56 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[MICALL1]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ZNF83]] | +0.55 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[BMAL2]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[LINC03004]] | +0.54 | +0.37 / +0.57 | both halves | 7e-05 |  |
| [[EIF3J]] | +0.54 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[ACOT9]] | +0.54 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[GPATCH4]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXI1]] | -0.59 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[BAG4]] | -0.56 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[ALDH6A1]] | -0.55 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[MMUT]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[RNASE4]] | -0.54 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[TNRC6B]] | -0.54 | -0.53 / -0.55 | both halves | 1e-05 | pathway: Adherens junctions interactions |
| [[FAM13A]] | -0.53 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[MAP3K2]] | -0.53 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[TRIM23]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[FBXO33]] | -0.52 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[KDM3A]] | -0.52 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ARL3]] | -0.51 | -0.58 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **-** arm (projection on the module's main direction -0.450). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (19.4, -12.7); signed map (-6.1, 24.5). **Vector** length 114, 32.0% of its response variance represented; |z| ≥ 3 in 1,354 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +5.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.4 | +10.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +6.4 | +9.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.2 | +10.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.5 | +8.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.3 | +8.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.9 | +6.4 |
| fall | [[NG25 (drug)]] 5 µM |  | -5.7 | -3.6 |
|  | [[Ixazomib (drug)]] 5 µM |  | -3.2 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | +1.3 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -2.8 | -4.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.6 | -3.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | PVR cell adhesion molecule |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.31 — chr19:44,643,798-44,666,162 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD155, HVED, Necl-5, NECL5, Tage4; previously PVS |
| Gene groups (HGNC) | CD molecules; V-set domain containing; C2-set domain containing; Nectins and nectin-like molecules |
| Hallmark sets | INFLAMMATORY_RESPONSE, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 7 pathways, smallest: Nectin/Necl  trans heterodimerization; Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Adherens junctions interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P15151](https://www.uniprot.org/uniprotkb/P15151) (Poliovirus receptor):

> Mediates NK cell adhesion and triggers NK cell effector functions. Binds two different NK cell receptors: CD96 and CD226. These interactions accumulates at the cell-cell contact site, leading to the formation of a mature immunological synapse between NK cell and target cell. This may trigger adhesion and secretion of lytic granules and IFN-gamma and activate cytotoxicity of activated NK cells. May also promote NK cell-target cell modular exchange, and PVR transfer to the NK cell. This transfer …

**Summary**, from NCBI Gene [5817](https://www.ncbi.nlm.nih.gov/gene/5817):

> The protein encoded by this gene is a transmembrane glycoprotein belonging to the immunoglobulin superfamily. The external domain mediates cell attachment to the extracellular matrix molecule vitronectin, while its intracellular domain interacts with the dynein light chain Tctex-1/DYNLT1. The gene is specific to the primate lineage, and serves as a cellular receptor for poliovirus in the first step of poliovirus replication. Multiple transcript variants encoding different isoforms have been …

**Accessions** — [HGNC:9705](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9705) · Entrez [5817](https://www.ncbi.nlm.nih.gov/gene/5817) · UniProt [P15151](https://www.uniprot.org/uniprotkb/P15151) · Ensembl [ENSG00000073008](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073008)

## Data

Gene col 1040: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1040); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1040, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1040]; `tensor/DDL_lfc|DDL_z.npy` [1040]; `embed/gene_vectors.npy` [1040]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1040 or target_col == 1040). Every well: [[PVR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PVR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
