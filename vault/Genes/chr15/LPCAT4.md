---
symbol: "LPCAT4"
type: "gene"
col: 10721
ensembl_id: "ENSG00000176454"
name: "lysophosphatidylcholine acyltransferase 4"
location: "15q14"
module: 77
arm: "+"
pooled_cpm: 17.86
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 24
n_dd_up_clean: 13
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# LPCAT4

*lysophosphatidylcholine acyltransferase 4* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.72× (z +8.3, q 4e-14, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.165× (z -39.2, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD27]] (+0.73, fdr 1e-05), [[TSEN54]] (+0.72, fdr 7e-06), [[METAP1]] (+0.71, fdr 1e-05); moves opposite to [[ZNF764]] (-0.75, fdr 7e-06), [[ZNF181]] (-0.75, fdr 1e-05), [[RAB30-DT]] (-0.74, fdr 1e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[P2RY2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10721.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.72×** | +8.3 | 4e-14 | 32/47 (LOX-IMVI, SW480, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.64×** | +7.6 | 7e-12 | 30/47 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +7.4 | 2e-11 | 27/47 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +6.8 | 2e-09 | 26/48 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +6.4 | 1e-08 | 27/47 (NCI-H1573, LoVo, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +5.4 | 5e-06 | 24/45 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.41×** | +3.7 | 0.014 | 9/45 (HCT15, HEC-1-A, …) | all doses, flat | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.7 | 0.014 | 14/39 (LOX-IMVI, J82, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Naproxen (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.037 | 10/46 (H4, A-427, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.052 | 12/46 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +3.3 | 0.053 | 6/48 (PANC-1, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.2 | 0.061 | 11/36 (KATO III, LS 180, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.079 | 9/48 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.085 | 5/47 (HS-578T, PANC-1, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.1 | 0.085 | 12/48 (PANC-1, A549, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.091 | 9/48 (SNU-423, NCI-H2347, …) | all doses, flat |  |
| [[Naproxen (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.091 | 3/47 (SW480, SK-MEL-2, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10721.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.165×** | -39.2 | 0e+00 | 47/47 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.183×** | -25.1 | 0e+00 | 43/46 (KATO III, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.224×** | -23.0 | 0e+00 | 43/44 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.376×** | -15.1 | 0e+00 | 37/46 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.624×** | -10.3 | 1e-22 | 29/45 (CFPAC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.590×** | -8.1 | 4e-14 | 30/47 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.629×** | -7.2 | 7e-11 | 25/47 (CFPAC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.641×** | -6.3 | 2e-08 | 20/32 (SW1417, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.672×** | -6.1 | 6e-08 | 26/47 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.775×** | -5.6 | 2e-06 | 24/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.706×** | -5.4 | 4e-06 | 24/47 (HCT15, SW480, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **0.753×** | -4.5 | 3e-04 | 21/48 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.819×** | -4.4 | 6e-04 | 17/48 (Hs 766T, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.774×** | -4.0 | 0.003 | 17/47 (HepG2/C3A, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.812×** | -3.9 | 0.003 | 14/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 5 µM |  | 0.837× | -3.9 | 0.003 | 14/48 (A498, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10721. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 30.9 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0917× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.197× (z -19.0) |
| [[CFPAC-1 (line)]] | alt | 49.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0565× (z -27.4) |
| [[Hs 766T (line)]] | wt | 38.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0722× (z -24.7) |
| [[KATO III (line)]] | alt | 22.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0581× (z -23.8) |
| [[A-172 (line)]] | wt | 18.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0715× (z -21.9) |
| [[A498 (line)]] | wt | 10.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0898× (z -22.0) |
| [[HOP62 (line)]] | alt | 16.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0685× (z -24.5) |
| [[HS-578T (line)]] | alt | 14.9 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.0685× (z -14.0) |
| [[LoVo (line)]] | wt | 25.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0938× (z -26.2) |
| [[LOX-IMVI (line)]] | wt | 16.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 18.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0338× (z -30.6) |
| [[NCI-H2030 (line)]] | alt | 20.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0922× (z -23.8) |
| [[NCI-H23 (line)]] | alt | 13.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 24.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -18.1) |
| [[SW480 (line)]] | alt | 17.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -21.8) |
| [[AsPC-1 (line)]] | alt | 18.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0762× (z -19.8) |
| [[HCT15 (line)]] | alt | 23.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -13.3) |
| [[hTERT-HPNE (line)]] | wt | 22.2 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.116× (z -9.3) |
| [[J82 (line)]] | alt | 12.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -16.4) |
| [[NCI-H2347 (line)]] | alt | 13.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -20.0) |
| [[NCI-H460 (line)]] | wt | 9.67 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -19.0) |
| [[PANC-1 (line)]] | alt | 13.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0813× (z -24.6) |
| [[RKO (line)]] | wt | 20.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0509× (z -17.8) |
| [[SNU-423 (line)]] | alt | 9.26 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -11.4) |
| [[SW1417 (line)]] | alt | 14.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -16.0) |
| [[A549 (line)]] | wt | 13.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0881× (z -19.4) |
| [[COLO 205 (line)]] | alt | 26.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0774× (z -19.8) |
| [[HT-29 (line)]] | alt | 33.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0701× (z -23.0) |
| [[LS 180 (line)]] | wt | 21.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -17.6) |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.117× (z -10.3) |
| [[SW 900 (line)]] | alt | 12.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -15.1) |
| [[SW48 (line)]] | wt | 30.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -15.1) |
| [[C32 (line)]] | wt | 7.99 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0790× (z -9.7) |
| [[H4 (line)]] | wt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 7.88 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0351× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -11.0) |
| [[SHP-77 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -11.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 10.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0255× (z -15.8) |
| [[A-427 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10721), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*34 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD27]] | +0.73 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[TSEN54]] | +0.72 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[METAP1]] | +0.71 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[IGSF8]] | +0.71 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[SPTLC2]] | +0.69 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[CKLF]] | +0.68 | +0.70 / +0.40 | both halves | 5e-05 |  |
| [[GNA12]] | +0.68 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[BICD2]] | +0.68 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[NFRKB]] | +0.68 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[PCMT1]] | +0.68 | +0.66 / +0.35 | both halves | 1e-04 |  |
| [[MINK1]] | +0.67 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[SLC9A6]] | +0.67 | +0.63 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*66 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF764]] | -0.75 | -0.75 / -0.58 | both halves | 7e-06 |  |
| [[ZNF181]] | -0.75 | -0.76 / -0.55 | both halves | 1e-05 |  |
| [[RAB30-DT]] | -0.74 | -0.75 / -0.53 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | -0.72 | -0.74 / -0.51 | both halves | 1e-05 |  |
| [[PATL2]] | -0.71 | -0.75 / -0.41 | both halves | 4e-05 |  |
| [[DCAF8]] | -0.71 | -0.67 / -0.61 | both halves | 7e-06 |  |
| [[TIA1]] | -0.71 | -0.75 / -0.56 | both halves | 1e-05 |  |
| [[TMEM202-AS1]] | -0.71 | -0.76 / -0.24 | both halves | 5e-04 |  |
| [[KRCC1]] | -0.70 | -0.73 / -0.45 | both halves | 3e-05 |  |
| [[PCNX4-DT]] | -0.70 | -0.76 / -0.27 | both halves | 3e-04 |  |
| [[ZXDA]] | -0.69 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[C11orf58]] | -0.69 | -0.66 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P2RY2]] | B | P2RY2 activity raises LPCAT4's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 1.44× lower at baseline in the lines without P2RY2 | 0.092 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.833). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (4.6, 6.1); signed map (-41.9, -4.8). **Vector** length 116, 29.9% of its response variance represented; |z| ≥ 3 in 1,074 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.5 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +6.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.0 | +8.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.9 | +5.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.6 | +7.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.5 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +2.2 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.6 | -23.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.1 | -25.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.3 | -15.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.2 | -39.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.6 | -8.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.3 | -2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -3.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | lysophosphatidylcholine acyltransferase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:34,358,633-34,367,196 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10257, LPAAT-eta, LPEAT2, LPLAT10; previously AYTL3, AGPAT7 |
| Gene groups (HGNC) | 1-acylglycerol-3-phosphate O-acyltransferases; Lysophospholipid acyltransferases; 1-acylglycerophosphoethanolamine O-acyltransferases |
| Reactome | 8 pathways, smallest: Acyl chain remodelling of PG; Acyl chain remodelling of PS; Acyl chain remodelling of PC |
| Matched by | ensembl_id |

**Function**, from UniProt [Q643R3](https://www.uniprot.org/uniprotkb/Q643R3) (Lysophospholipid acyltransferase LPCAT4):

> Acyl-CoA-dependent lysophospholipid acyltransferase involved in phospholipid remodeling. Displays acyltransferase activity with a subset of lysophospholipids as substrates; converts lysophosphatidylethanolamine to phosphatidylethanolamine, lysophosphatidylcholine to phosphatidycholine, 1-alkenyl-lysophatidylethanolamine to 1-alkenyl-phosphatidylethanolamine, lysophosphatidylglycerol and alkyl-lysophosphatidylcholine to phosphatidylglycerol and alkyl-phosphatidylcholine, respectively. Can use …

**Summary**, from NCBI Gene [254531](https://www.ncbi.nlm.nih.gov/gene/254531):

> Members of the 1-acylglycerol-3-phosphate O-acyltransferase (EC 2.3.1.51) family, such as AGPAT7, catalyze the conversion of lysophosphatidic acid (LPA) to phosphatidic acid (PA), a precursor in the biosynthesis of all glycerolipids. Both LPA and PA are involved in signal transduction (Ye et al., 2005 [PubMed 16243729]).[supplied by OMIM, May 2008]

**Accessions** — [HGNC:30059](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30059) · Entrez [254531](https://www.ncbi.nlm.nih.gov/gene/254531) · UniProt [Q643R3](https://www.uniprot.org/uniprotkb/Q643R3) · Ensembl [ENSG00000176454](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176454)

## Data

Gene col 10721: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10721); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10721, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10721]; `tensor/DDL_lfc|DDL_z.npy` [10721]; `embed/gene_vectors.npy` [10721]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10721 or target_col == 10721). Every well: [[LPCAT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LPCAT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
