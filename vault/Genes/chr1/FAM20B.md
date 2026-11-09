---
symbol: "FAM20B"
type: "gene"
col: 3774
ensembl_id: "ENSG00000116199"
name: "FAM20B glycosaminoglycan xylosylkinase"
location: "1q25.2"
module: 18
arm: "+"
pooled_cpm: 56.89
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# FAM20B

*FAM20B glycosaminoglycan xylosylkinase* — 1q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.24× (z +5.6, q 2e-05, up in 24 of 42 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (CFPAC-1 2.29×, C32 2.72×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (CFPAC-1 2.79×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.406× (z -34.1, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NTAQ1]] (+0.71, fdr 7e-06), [[TCF3]] (+0.70, fdr 7e-06), [[TMTC4]] (+0.68, fdr 7e-06); moves opposite to [[TRMT1L]] (-0.68, fdr 7e-06), [[CLK4]] (-0.67, fdr 7e-06), [[SGO1-AS1]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TNFRSF14]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3774.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (CFPAC-1 2.29×, C32 2.72×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (CFPAC-1 2.79×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +5.6 | 2e-05 | 24/42 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +4.3 | 0.004 | 14/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.16× | +3.9 | 0.017 | 15/47 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.15× | +3.7 | 0.026 | 16/47 (CFPAC-1, C32, …) | rises with dose | composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.5 | 0.052 | 1/48 (SNU-423) | top dose only |  |
| [[vincristine (drug)]] 0.05 µM |  | 1.14× | +3.3 | 0.076 | 7/48 (MIA PaCa-2, RKO, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.14× | +3.3 | 0.076 | 4/48 (AsPC-1, LoVo, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | 1.24× | +3.0 | 0.16 | 10/48 (MIA PaCa-2, C32, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.12× | +3.0 | 0.16 | 6/48 (SW480, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3774.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.406×** | -34.1 | 0e+00 | 48/48 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.328×** | -28.7 | 0e+00 | 47/48 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.491×** | -18.3 | 0e+00 | 41/48 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.508×** | -18.1 | 0e+00 | 41/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.442×** | -11.4 | 4e-28 | 39/49 (A-427, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.795×** | -8.7 | 4e-16 | 24/48 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.733×** | -8.3 | 6e-15 | 29/48 (SW480, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.833×** | -6.9 | 3e-10 | 23/48 (NCI-H23, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.796×** | -6.1 | 5e-08 | 28/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.809×** | -5.2 | 1e-05 | 26/47 (NCI-H460, SW1417, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.822×** | -5.1 | 2e-05 | 23/48 (A-427, C-33 A, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.882× | -4.8 | 9e-05 | 18/48 (A-427, SNU-1, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -4.6 | 2e-04 | 18/48 (H4, hTERT-HPNE, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.739×** | -4.2 | 9e-04 | 16/48 (SW48, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.870× | -3.7 | 0.007 | 18/48 (PANC-1, A-427, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.828×** | -3.6 | 0.010 | 15/46 (HS-578T, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | 0.888× | -3.2 | 0.048 | 12/48 (SW 900, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3774. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 102 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -23.5) |
| [[NCI-H460 (line)]] | wt | 87.0 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -28.1) |
| [[PANC-1 (line)]] | alt | 73.4 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -14.0) |
| [[HOP62 (line)]] | alt | 55.9 | 0 | 6 | — | [[Harringtonine (drug)]] 5 µM 0.238× (z -16.0) |
| [[RKO (line)]] | wt | 84.1 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -29.0) |
| [[SW48 (line)]] | wt | 56.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -15.3) |
| [[A-172 (line)]] | wt | 77.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -25.9) |
| [[HEC-1-A (line)]] | alt | 55.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -22.0) |
| [[MIA PaCa-2 (line)]] | alt | 77.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.260× (z -14.9) |
| [[A498 (line)]] | wt | 62.8 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.279× (z -17.3) |
| [[A549 (line)]] | wt | 54.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -21.1) |
| [[CFPAC-1 (line)]] | alt | 38.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -16.4) |
| [[J82 (line)]] | alt | 69.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -24.6) |
| [[LoVo (line)]] | wt | 44.2 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.550× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 49.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 56.9 | 0 | 4 | — | [[Harringtonine (drug)]] 0.5 µM 0.278× (z -13.1) |
| [[C32 (line)]] | wt | 39.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.254× (z -11.1) |
| [[HS-578T (line)]] | alt | 47.0 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.162× (z -17.7) |
| [[NCI-H23 (line)]] | alt | 52.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -19.1) |
| [[SW 900 (line)]] | alt | 75.6 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.278× (z -12.7) |
| [[SW1417 (line)]] | alt | 55.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -19.7) |
| [[SW480 (line)]] | alt | 44.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -18.1) |
| [[AN3 CA (line)]] | alt | 62.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.129× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 53.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -18.2) |
| [[CHP-212 (line)]] | wt | 83.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -9.5) |
| [[COLO 205 (line)]] | alt | 49.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.142× (z -14.9) |
| [[H4 (line)]] | wt | 66.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -24.2) |
| [[Hs 766T (line)]] | wt | 34.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -11.4) |
| [[HT-29 (line)]] | alt | 40.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -13.4) |
| [[KATO III (line)]] | alt | 37.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -10.1) |
| [[LS 180 (line)]] | wt | 40.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -18.8) |
| [[NCI-H1792 (line)]] | alt | 46.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.291× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 48.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.312× (z -12.7) |
| [[NCI-H2347 (line)]] | alt | 57.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -17.4) |
| [[Panc 03.27 (line)]] | alt | 46.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -27.1) |
| [[SNU-423 (line)]] | alt | 36.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -11.2) |
| [[BT-474 (line)]] | alt | 43.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -11.3) |
| [[C-33 A (line)]] | alt | 75.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -11.9) |
| [[HCT15 (line)]] | alt | 46.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 45.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.324× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 78.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -11.3) |
| [[SNU-1 (line)]] | wt | 57.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1271 (line)]] | alt | 36.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3774), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTAQ1]] | +0.71 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[TCF3]] | +0.70 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[TMTC4]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[NUTF2]] | +0.68 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[VKORC1L1]] | +0.67 | +0.70 / +0.63 | both halves | 7e-06 | STRING 503 |
| [[LIMK1]] | +0.67 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[TPST2]] | +0.66 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[PEMT]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[MTFR1]] | +0.65 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[TTL]] | +0.65 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[COPG2]] | +0.64 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[CPSF4]] | +0.64 | +0.70 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT1L]] | -0.68 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[CLK4]] | -0.67 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[SGO1-AS1]] | -0.67 | -0.71 / -0.59 | both halves | 7e-06 |  |
| [[ZNF585A]] | -0.66 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[ZNF44]] | -0.65 | -0.66 / -0.58 | both halves | 7e-06 |  |
| [[FAM200A]] | -0.65 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[PEX12]] | -0.64 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[NBR1]] | -0.64 | -0.75 / -0.52 | both halves | 1e-05 |  |
| [[RSF1]] | -0.63 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[METTL25B]] | -0.63 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[STK16]] | -0.61 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[ANKRD26]] | -0.61 | -0.65 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF14]] | B | TNFRSF14 activity lowers FAM20B's level | lines that do not express TNFRSF14 (12) vs lines expressing it (38) | 1.27× higher at baseline in the lines without TNFRSF14 | 0.076 | ⚠ within organs, on part of the lines; also absent: ZNF785, ZNF69, ENSG00000259345 |
| [[TNFAIP3]] | C | TNFAIP3 activity lowers FAM20B's level | lines that do not express TNFAIP3 (3) vs lines expressing it (47) | 1.67× higher at baseline in the lines without TNFAIP3 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IER3, JAG1, ATXN1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-6.6, -28.3); signed map (-43.5, -15.8). **Vector** length 109, 27.3% of its response variance represented; |z| ≥ 3 in 1,024 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.5 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.9 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +1.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.3 | +3.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.4 | -28.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.6 | -18.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.2 | -18.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.7 | -34.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.4 | -11.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -6.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -4.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | FAM20B glycosaminoglycan xylosylkinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.2 — chr1:179,025,804-179,076,567 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0475, GXK1 |
| Gene groups (HGNC) | Golgi associated kinase family; Carbohydrate kinases |
| Reactome | 3 pathways, smallest: Glycosaminoglycan-protein linkage region biosynthesis; Glycosaminoglycan metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [O75063](https://www.uniprot.org/uniprotkb/O75063) (Glycosaminoglycan xylosylkinase):

> Responsible for the 2-O-phosphorylation of xylose in the glycosaminoglycan-protein linkage region of proteoglycans thereby regulating the amount of mature GAG chains. Sulfated glycosaminoglycans (GAGs), including heparan sulfate and chondroitin sulfate, are synthesized on the so-called common GAG-protein linkage region (GlcUAbeta1-3Galbeta1-3Galbeta1-4Xylbeta1-O-Ser) of core proteins, which is formed by the stepwise addition of monosaccharide residues by the respective specific …

**Summary**, from NCBI Gene [9917](https://www.ncbi.nlm.nih.gov/gene/9917):

> Enables phosphotransferase activity, alcohol group as acceptor. Predicted to be involved in proteoglycan biosynthetic process. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23017](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23017) · Entrez [9917](https://www.ncbi.nlm.nih.gov/gene/9917) · UniProt [O75063](https://www.uniprot.org/uniprotkb/O75063) · Ensembl [ENSG00000116199](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116199)

## Data

Gene col 3774: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3774); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3774, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3774]; `tensor/DDL_lfc|DDL_z.npy` [3774]; `embed/gene_vectors.npy` [3774]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3774 or target_col == 3774). Every well: [[FAM20B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM20B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
