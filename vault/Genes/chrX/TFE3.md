---
symbol: "TFE3"
type: "gene"
col: 886
ensembl_id: "ENSG00000068323"
name: "transcription factor binding to IGHM enhancer 3"
location: "Xp11.23"
module: 96
arm: "+"
pooled_cpm: 29.64
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# TFE3

*transcription factor binding to IGHM enhancer 3* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.22× (z +30.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.793× (z -6.1, q 7e-07, down in 28 of 47 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.830× (z -3.4, q 0.085, down in 14 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RPMI-7951 0.487×, CFPAC-1 0.475×; ⚠ cell-cycle shift, explains ~25% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H1573 0.368×; ⚠ cell-cycle shift, explains ~57% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.149×; ⚠ cell-cycle shift, explains ~38% of this change); [[Olanzapine (drug)]] 0.5 µM in 1 line (CHP-212 0.0757×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRIPAP1]] (+0.69, fdr 7e-06, ⚠ same locus), [[CELSR3]] (+0.69, fdr 7e-06), [[DUSP8]] (+0.66, fdr 7e-06), [[ZNF674]] (+0.65, fdr 7e-06); moves opposite to [[RNF4]] (-0.67, fdr 7e-06), [[NDC1]] (-0.66, fdr 8e-06), [[SNHG30]] (-0.65, fdr 7e-06).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KRTAP5-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 886.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.22×** | +30.6 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.62×** | +17.1 | 0e+00 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.38×** | +16.1 | 0e+00 | 43/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.87×** | +11.6 | 7e-29 | 39/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +10.8 | 4e-25 | 35/44 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +10.6 | 2e-24 | 28/34 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +9.4 | 3e-19 | 43/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +8.7 | 2e-16 | 37/47 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +7.8 | 4e-13 | 29/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +7.4 | 6e-12 | 36/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +6.7 | 1e-09 | 29/48 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +6.2 | 2e-08 | 26/47 (A-427, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +5.9 | 1e-07 | 24/37 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +5.1 | 1e-05 | 18/48 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.29×** | +4.7 | 9e-05 | 20/48 (HEC-1-A, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.29×** | +4.3 | 5e-04 | 21/47 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +4.3 | 6e-04 | 21/48 (KATO III, SNU-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.2 | 8e-04 | 17/48 (LS 180, LoVo, …) | two highest doses | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.003 | 14/47 (HT-29, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.010 | 16/48 (A-427, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 886.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RPMI-7951 0.487×, CFPAC-1 0.475×; ⚠ cell-cycle shift, explains ~25% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H1573 0.368×; ⚠ cell-cycle shift, explains ~57% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.149×; ⚠ cell-cycle shift, explains ~38% of this change); [[Olanzapine (drug)]] 0.5 µM in 1 line (CHP-212 0.0757×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.793×** | -6.1 | 7e-07 | 28/47 (RPMI-7951, CFPAC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.804×** | -3.9 | 0.030 | 20/47 (AN3 CA, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.829×** | -3.5 | 0.085 | 17/48 (NCI-H1573, H4, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.830×** | -3.4 | 0.085 | 14/48 (HT-29, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 886. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.3 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +24.0) | — |
| [[A-172 (line)]] | wt | 43.0 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +19.2) | — |
| [[A549 (line)]] | wt | 35.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +20.6) | — |
| [[J82 (line)]] | alt | 44.0 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +17.7) | — |
| [[A498 (line)]] | wt | 16.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +13.8) | — |
| [[BT-474 (line)]] | alt | 23.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 20.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +18.3) | — |
| [[LoVo (line)]] | wt | 18.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +16.1) | — |
| [[NCI-H1573 (line)]] | alt | 47.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +15.7) | [[Panobinostat (drug)]] 5 µM 0.368× (z -9.3) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SNU-423 (line)]] | alt | 59.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +21.1) | — |
| [[A-427 (line)]] | wt | 30.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +11.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 43.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +22.6) | — |
| [[PANC-1 (line)]] | alt | 30.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +26.0) | — |
| [[RPMI-7951 (line)]] | alt | 52.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +15.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[AsPC-1 (line)]] | alt | 21.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.69× (z +18.0) | — |
| [[CFPAC-1 (line)]] | alt | 30.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HEC-1-A (line)]] | alt | 21.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +12.8) | — |
| [[HepG2_C3A (line)]] | wt | 31.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +10.4) | — |
| [[SNU-1 (line)]] | wt | 28.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 23.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +12.2) | — |
| [[SW480 (line)]] | alt | 32.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +14.9) | — |
| [[AN3 CA (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -8.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[C32 (line)]] | wt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +10.6) | — |
| [[CHP-212 (line)]] | wt | 21.8 | 0 | 1 | — | [[Olanzapine (drug)]] 0.5 µM 0.0757× (z -8.6) |
| [[COLO 205 (line)]] | alt | 26.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +12.3) | — |
| [[Hs 766T (line)]] | wt | 40.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +12.4) | — |
| [[HS-578T (line)]] | alt | 21.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +12.7) | — |
| [[HT-29 (line)]] | alt | 34.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +16.8) | — |
| [[KATO III (line)]] | alt | 33.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.4) | — |
| [[LOX-IMVI (line)]] | wt | 27.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 14.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +13.2) | — |
| [[NCI-H23 (line)]] | alt | 22.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +16.0) | — |
| [[NCI-H2347 (line)]] | alt | 26.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.9) | — |
| [[Panc 03.27 (line)]] | alt | 31.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +13.6) | — |
| [[SK-MEL-2 (line)]] | alt | 22.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +12.2) | — |
| [[SW1417 (line)]] | alt | 33.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +12.2) | — |
| [[SW48 (line)]] | wt | 16.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 886), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRIPAP1]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 | STRING 612; ⚠ same locus (26.5 kb, same strand: neighbours can correlate without regulation) |
| [[CELSR3]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[DUSP8]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ZNF674]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[TNKS1BP1]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[CHMP4A]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[MBD6]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[FAM50A]] | +0.64 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[DEDD]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[GPR108]] | +0.62 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[SYNPO]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[KDM6B]] | +0.60 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[CIC]] | +0.60 | +0.67 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF4]] | -0.67 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[NDC1]] | -0.66 | -0.67 / -0.58 | both halves | 8e-06 |  |
| [[SNHG30]] | -0.65 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[IPO11]] | -0.64 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[NUP54]] | -0.63 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[NME2]] | -0.62 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[IQCB1]] | -0.61 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[PPP2R5E]] | -0.61 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[NFATC3]] | -0.60 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[TAF5L]] | -0.60 | -0.54 / -0.70 | both halves | 1e-05 |  |
| [[SNRPA1]] | -0.59 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[MFSD14CP]] | -0.58 | -0.50 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRTAP5-AS1]] | B | KRTAP5-AS1 activity raises TFE3's level | lines that do not express KRTAP5-AS1 (12) vs lines expressing it (38) | 1.28× lower at baseline in the lines without KRTAP5-AS1 | 0.070 | ⚠ within organs, on part of the lines; also absent: LLGL2, TFR2, USP43; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.652). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-5.9, -14.2); signed map (-4.1, 22.1). **Vector** length 100, 24.4% of its response variance represented; |z| ≥ 3 in 1,024 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.1 | +30.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.0 | +17.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +16.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +7.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +4.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.0 | +2.9 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -5.0 | -1.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -0.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.4 | -6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -4.2 | -3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.6 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.8 | -0.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor binding to IGHM enhancer 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:49,028,726-49,043,410 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TFEA, bHLHe33 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Reactome | 2 pathways, smallest: Transcriptional and post-translational regulation of MITF-M expression and activity; MITF-M-regulated melanocyte development |
| Matched by | ensembl_id |

**Function**, from UniProt [P19532](https://www.uniprot.org/uniprotkb/P19532) (Transcription factor E3):

> Transcription factor that acts as a master regulator of lysosomal biogenesis and immune response. Specifically recognizes and binds E-box sequences (5'-CANNTG-3'); efficient DNA-binding requires dimerization with itself or with another MiT/TFE family member such as TFEB or MITF. Involved in the cellular response to amino acid availability by acting downstream of MTOR: in the presence of nutrients, TFE3 phosphorylation by MTOR promotes its inactivation. Upon starvation or lysosomal stress, …

**Summary**, from NCBI Gene [7030](https://www.ncbi.nlm.nih.gov/gene/7030):

> This gene encodes a basic helix-loop-helix domain-containing transcription factor that binds MUE3-type E-box sequences in the promoter of genes. The encoded protein promotes the expression of genes downstream of transforming growth factor beta (TGF-beta) signaling. This gene may be involved in chromosomal translocations in renal cell carcinomas and other cancers, resulting in the production of fusion proteins. Translocation partners include PRCC (papillary renal cell carcinoma), NONO (non-POU …

**Accessions** — [HGNC:11752](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11752) · Entrez [7030](https://www.ncbi.nlm.nih.gov/gene/7030) · UniProt [P19532](https://www.uniprot.org/uniprotkb/P19532) · Ensembl [ENSG00000068323](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068323)

## Data

Gene col 886: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 886); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 886, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 886]; `tensor/DDL_lfc|DDL_z.npy` [886]; `embed/gene_vectors.npy` [886]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 886 or target_col == 886). Every well: [[TFE3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFE3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
