---
symbol: "PAF1"
type: "gene"
col: 125
ensembl_id: "ENSG00000006712"
name: "PAF1 component of Paf1/RNA polymerase II complex"
location: "19q13.2"
module: 173
arm: "+"
pooled_cpm: 40.25
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# PAF1

*PAF1 component of Paf1/RNA polymerase II complex* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.67× (z +19.9, q 0e+00, up in 46 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +9.7, q 5e-20, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Carbidopa (monohydrate) (drug)]] 0.05 µM: 0.702× (z -5.1, q 2e-04, down in 32 of 48 measured lines) ⚠ unreliable plate only; position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Allantoin (drug)]] 0.05 µM in 1 line (SNU-1 0.102×; ⚠ transcription drop); [[Belinostat (drug)]] 0.5 µM in 1 line (SNU-1 0.130×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACIN1]] (+0.66, fdr 1e-05), [[MEPCE]] (+0.65, fdr 1e-05), [[SCAF1]] (+0.64, fdr 1e-05); moves opposite to [[LYPLA1]] (-0.59, fdr 2e-05), [[ANKS6]] (-0.57, fdr 5e-05), [[ST6GALNAC4]] (-0.56, fdr 4e-05).
> It is in [[Module 173]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 125.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.67×** | +19.9 | 0e+00 | 46/47 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.35×** | +11.8 | 1e-29 | 43/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +9.7 | 5e-20 | 36/47 (AsPC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.87×** | +8.9 | 6e-17 | 35/47 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.74×** | +8.0 | 2e-13 | 36/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.69×** | +7.2 | 4e-11 | 28/35 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.62×** | +6.9 | 4e-10 | 32/42 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.61×** | +6.8 | 6e-10 | 35/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.59×** | +6.6 | 3e-09 | 30/46 (NCI-H460, AsPC-1, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.53×** | +6.1 | 5e-08 | 35/46 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +5.5 | 2e-06 | 25/43 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.46×** | +5.2 | 1e-05 | 25/47 (PANC-1, NCI-H460, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.43×** | +5.2 | 1e-05 | 26/47 (NCI-H460, LS 180, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.97×** | +5.1 | 1e-05 | 25/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.8 | 5e-05 | 1/48 (COLO 205) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +4.3 | 6e-04 | 18/47 (CFPAC-1, PANC-1, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.009 | 21/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.4 | 0.018 | 15/48 (MIA PaCa-2, J82, …) | top dose only |  |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.032 | 12/48 (C-33 A, SW 900, …) | rises with dose | position effect removed |
| [[Pemigatinib (drug)]] 0.05 µM |  | **1.24×** | +2.9 | 0.084 | 9/48 (SK-MEL-2, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 0.05 µM |  | **1.24×** | +2.9 | 0.088 | 10/48 (PANC-1, HOP62, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.22×** | +2.9 | 0.088 | 7/47 (HOP62, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 125.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Allantoin (drug)]] 0.05 µM in 1 line (SNU-1 0.102×; ⚠ transcription drop); [[Belinostat (drug)]] 0.5 µM in 1 line (SNU-1 0.130×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.702×** | -5.1 | 2e-04 | 32/48 (HS-578T, PANC-1, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.716×** | -4.8 | 4e-04 | 25/47 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.852× | -3.3 | 0.16 | 15/48 (Hs 766T, PANC-1, …) | top dose only | position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.853× | -3.3 | 0.16 | 8/48 (SW480, SHP-77, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 125. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.8 | 9 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +17.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.29× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 329 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +22.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.89× (z +13.8) | — |
| [[A549 (line)]] | wt | 32.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.17× (z +19.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.78× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 29.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +14.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.15× (z +9.1) | — |
| [[LoVo (line)]] | wt | 19.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +17.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.35× (z +9.5) | — |
| [[AsPC-1 (line)]] | alt | 22.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +13.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 20.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +13.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.80× (z +9.0) | — |
| [[A498 (line)]] | wt | 29.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +14.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1573 (line)]] | alt | 14.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +15.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SNU-1 (line)]] | wt | 17.4 | 0 | 2 (2 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.102× (z -10.0) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 23.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +13.2) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[C32 (line)]] | wt | 15.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +10.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[CFPAC-1 (line)]] | alt | 22.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HOP62 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +13.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HS-578T (line)]] | alt | 25.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +11.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HT-29 (line)]] | alt | 36.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 20.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +9.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[J82 (line)]] | alt | 22.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +14.2) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[LOX-IMVI (line)]] | wt | 14.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +9.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 19.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +10.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 18.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +13.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2347 (line)]] | alt | 24.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +8.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[RPMI-7951 (line)]] | alt | 27.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +8.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 19.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +11.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW 900 (line)]] | alt | 30.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW1417 (line)]] | alt | 26.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW480 (line)]] | alt | 21.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-427 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 125), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACIN1]] | +0.66 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[MEPCE]] | +0.65 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[SCAF1]] | +0.64 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[ZNF687]] | +0.64 | +0.64 / +0.54 | both halves | 1e-05 | pathway: ATP-dependent chromatin remodelers |
| [[MED12]] | +0.64 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[FBRS]] | +0.63 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[TSPYL1]] | +0.63 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[THAP9]] | +0.63 | +0.63 / +0.49 | both halves | 2e-05 |  |
| [[IRF2BP1]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ARFGAP2]] | +0.62 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[HMGN2P5]] | +0.62 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[HMGN2]] | +0.61 | +0.61 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYPLA1]] | -0.59 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[ANKS6]] | -0.57 | -0.60 / -0.39 | both halves | 5e-05 |  |
| [[ST6GALNAC4]] | -0.56 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[NME2]] | -0.55 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[EIF3K]] | -0.55 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[GPR89A]] | -0.54 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[MRPL52]] | -0.54 | -0.61 / -0.35 | both halves | 1e-04 |  |
| [[PIGF]] | -0.54 | -0.61 / -0.37 | both halves | 9e-05 |  |
| [[UQCRH]] | -0.53 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[DAP3]] | -0.53 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[DUXAP10]] | -0.53 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[PACC1]] | -0.53 | -0.57 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.764). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-10.8, 5.0); signed map (15.5, -21.9). **Vector** length 83.1, 18.0% of its response variance represented; |z| ≥ 3 in 896 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +6.6 | +19.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.9 | +11.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | +4.8 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +9.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.8 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.3 | +1.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.0 | -1.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -1.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -2.1 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.9 | -4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.5 | -0.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | PAF1 component of Paf1/RNA polymerase II complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:39,385,629-39,391,154 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PD2, F23149_1, FLJ11123 |
| Gene groups (HGNC) | Paf1/RNA polymerase II complex |
| Reactome | 17 pathways, smallest: Dengue virus activates/modulates innate and adaptive immune responses; E3 ubiquitin ligases ubiquitinate target proteins; CHD1 and CHD2 subfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N7H5](https://www.uniprot.org/uniprotkb/Q8N7H5) (RNA polymerase II-associated factor 1 homolog):

> Component of the PAF1 complex (PAF1C) which has multiple functions during transcription by RNA polymerase II and is implicated in regulation of development and maintenance of embryonic stem cell pluripotency. PAF1C associates with RNA polymerase II through interaction with POLR2A CTD non-phosphorylated and 'Ser-2'- and 'Ser-5'-phosphorylated forms and is involved in transcriptional elongation, acting both independently and synergistically with TCEA1 and in cooperation with the DSIF complex and …

**Summary**, from NCBI Gene [54623](https://www.ncbi.nlm.nih.gov/gene/54623):

> This gene encodes a subunit of the polymerase associated factor (PAF1) complex. The PAF1 complex interacts with RNA polymerase II and plays a role in transcription elongation as well as histone modifications including ubiquitylation and methylation. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:25459](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25459) · Entrez [54623](https://www.ncbi.nlm.nih.gov/gene/54623) · UniProt [Q8N7H5](https://www.uniprot.org/uniprotkb/Q8N7H5) · Ensembl [ENSG00000006712](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006712)

## Data

Gene col 125: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 125); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 125, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 125]; `tensor/DDL_lfc|DDL_z.npy` [125]; `embed/gene_vectors.npy` [125]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 125 or target_col == 125). Every well: [[PAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
