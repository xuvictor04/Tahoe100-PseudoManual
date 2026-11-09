---
symbol: "BZW2"
type: "gene"
col: 5845
ensembl_id: "ENSG00000136261"
name: "basic leucine zipper and W2 domains 2"
location: "7p21.1"
module: 93
arm: "+"
pooled_cpm: 136.86
n_lines_expressing: 48
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# BZW2

*basic leucine zipper and W2 domains 2* — 7p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (17 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +12.7, q 3e-34, up in 41 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.405×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (A498 0.530×; ⚠ cell-cycle shift, explains ~60% of this change); [[Ponatinib (drug)]] 5 µM in 1 line (RKO 0.457×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC16A1]] (+0.61, fdr 1e-05), [[MLF1]] (+0.58, fdr 1e-05), [[AMD1]] (+0.56, fdr 2e-05); moves opposite to [[LEMD2]] (-0.57, fdr 1e-05), [[ABHD13]] (-0.51, fdr 4e-05), [[PRKAB1]] (-0.51, fdr 3e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 17 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5845.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +12.7 | 3e-34 | 41/47 (MIA PaCa-2, HT-29, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.78×** | +11.5 | 3e-28 | 33/46 (A498, AsPC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.25×** | +11.4 | 6e-28 | 46/46 (AsPC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.08×** | +10.3 | 1e-22 | 45/46 (AsPC-1, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.95×** | +8.5 | 2e-15 | 43/46 (AsPC-1, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.71×** | +7.2 | 5e-11 | 34/46 (A498, AsPC-1, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.48×** | +5.3 | 1e-05 | 30/48 (A-172, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.2 | 2e-05 | 29/46 (C32, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.99×** | +5.0 | 3e-05 | 35/46 (MIA PaCa-2, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.43×** | +5.0 | 3e-05 | 29/47 (LS 180, HT-29, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +4.9 | 5e-05 | 26/46 (RPMI-7951, AN3 CA, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **1.43×** | +4.8 | 7e-05 | 28/45 (SHP-77, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.40×** | +4.8 | 8e-05 | 27/46 (AsPC-1, LS 180, …) | inconsistent across doses | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.36×** | +4.4 | 5e-04 | 33/46 (NCI-H23, H4, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.2 | 0.001 | 32/43 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.010 | 29/47 (RPMI-7951, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.012 | 25/46 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.024 | 22/47 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.026 | 21/46 (MIA PaCa-2, RPMI-7951, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.027 | 22/46 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.55×** | +3.2 | 0.027 | 19/46 (A498, AN3 CA, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.027 | 22/46 (HT-29, COLO 205, …) | top dose only |  |
| [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.027 | 22/46 (H4, CFPAC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.032 | 20/47 (Panc 03.27, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.034 | 21/46 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.057 | 20/46 (A498, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5845.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.405×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (A498 0.530×; ⚠ cell-cycle shift, explains ~60% of this change); [[Ponatinib (drug)]] 5 µM in 1 line (RKO 0.457×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | 0.769× | -3.7 | 0.11 | 25/46 (RKO, KATO III, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.848× | -3.3 | 0.26 | 14/46 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | 0.788× | -3.0 | 0.43 | 24/46 (J82, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5845. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 108 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +16.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +11.2) | — |
| [[A498 (line)]] | wt | 159 | 5 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +20.0) ⚠ cell-cycle shift, explains ~39% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.530× (z -9.2) ⚠ cell-cycle shift, explains ~60% of this change |
| [[HT-29 (line)]] | alt | 108 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +13.8) | — |
| [[A-172 (line)]] | wt | 65.6 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +12.5) | — |
| [[SNU-423 (line)]] | alt | 60.5 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +11.1) | — |
| [[H4 (line)]] | wt | 217 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.44× (z +10.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +8.5) | — |
| [[LoVo (line)]] | wt | 133 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +13.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +10.4) | — |
| [[SW1417 (line)]] | alt | 165 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +12.1) | — |
| [[HS-578T (line)]] | alt | 137 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.6) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[LS 180 (line)]] | wt | 105 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +11.7) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H23 (line)]] | alt | 89.9 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.85× (z +8.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 2.82× (z +8.5) | — |
| [[C32 (line)]] | wt | 138 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +16.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.75× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 161 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +13.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 78.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +12.8) | — |
| [[HOP62 (line)]] | alt | 53.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +13.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +11.9) | — |
| [[hTERT-HPNE (line)]] | wt | 84.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +10.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +9.2) | — |
| [[J82 (line)]] | alt | 80.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +10.7) | — |
| [[KATO III (line)]] | alt | 149 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.61× (z +9.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 134 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +19.2) | — |
| [[Panc 03.27 (line)]] | alt | 103 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +11.4) | — |
| [[RKO (line)]] | wt | 175 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.405× (z -9.5) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.457× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 175 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 147 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.23× (z +8.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[COLO 205 (line)]] | alt | 47.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +11.6) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[HCT15 (line)]] | alt | 103 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 133 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +13.5) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1792 (line)]] | alt | 163 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +15.9) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H2347 (line)]] | alt | 112 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 236 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +8.5) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 170 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.53× (z +9.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW48 (line)]] | wt | 204 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.10× (z +10.3) | — |
| [[A-427 (line)]] | wt | 29.4 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 81.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 228 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 188 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 147 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5845), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC16A1]] | +0.61 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[MLF1]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[AMD1]] | +0.56 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[FAM222A]] | +0.55 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[SRSF7]] | +0.54 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[ARIH1]] | +0.54 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[CDKL2]] | +0.53 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[LGMN]] | +0.53 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[NOP58]] | +0.52 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[TXLNG]] | +0.51 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[PPAT]] | +0.50 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[SKP1]] | +0.50 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEMD2]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[ABHD13]] | -0.51 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[PRKAB1]] | -0.51 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[VPS16]] | -0.51 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[SNRNP35]] | -0.51 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[RNF25]] | -0.51 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[CC2D1B]] | -0.50 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[ZNF865]] | -0.50 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[TOP3B]] | -0.48 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[NECAP2]] | -0.48 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[ZNF700]] | -0.47 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[WASH8P]] ⚠ | -0.47 | -0.38 / -0.42 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZSCAN25]] | -0.46 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.594). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-14.7, 5.9); signed map (3.2, 18.6). **Vector** length 108, 34.9% of its response variance represented; |z| ≥ 3 in 1,133 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +12.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +2.8 | +5.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[Artemether (drug)]] 0.05 µM |  | +2.5 | +2.0 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +2.5 | +2.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -0.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -4.9 | -0.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.0 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -4.0 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -2.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.0 | -0.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.6 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | basic leucine zipper and W2 domains 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.1 — chr7:16,646,131-16,706,523 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC028, MST017, MSTP017, 5MP1 |
| Gene groups (HGNC) | Basic leucine zipper and W2 domains family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6E2](https://www.uniprot.org/uniprotkb/Q9Y6E2) (eIF5-mimic protein 1):

> Translation initiation regulator which represses non-AUG initiated translation and repeat-associated non-AUG (RAN) initiated translation by acting as a competitive inhibitor of eukaryotic translation initiation factor 5 (EIF5) function. Increases the accuracy of translation initiation by impeding EIF5-dependent translation from non-AUG codons by competing with it for interaction with EIF2S2 within the 43S pre-initiation complex (PIC) in an EIF3C-binding dependent manner.

**Summary**, from NCBI Gene [28969](https://www.ncbi.nlm.nih.gov/gene/28969):

> Enables cadherin binding activity. Involved in regulation of translational initiation. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18808](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18808) · Entrez [28969](https://www.ncbi.nlm.nih.gov/gene/28969) · UniProt [Q9Y6E2](https://www.uniprot.org/uniprotkb/Q9Y6E2) · Ensembl [ENSG00000136261](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136261)

## Data

Gene col 5845: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5845); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5845, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5845]; `tensor/DDL_lfc|DDL_z.npy` [5845]; `embed/gene_vectors.npy` [5845]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5845 or target_col == 5845). Every well: [[BZW2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BZW2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
