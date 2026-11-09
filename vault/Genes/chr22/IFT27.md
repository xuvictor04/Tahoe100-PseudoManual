---
symbol: "IFT27"
type: "gene"
col: 1940
ensembl_id: "ENSG00000100360"
name: "intraflagellar transport 27"
location: "22q12.3"
module: 69
arm: "+"
pooled_cpm: 9.2
n_lines_expressing: 48
n_dd_up: 22
n_dd_down: 17
n_dd_up_clean: 16
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# IFT27

*intraflagellar transport 27* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.22× (z +9.7, q 2e-19, up in 10 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.49× (z +7.1, q 2e-10, up in 22 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.455× (z -10.0, q 1e-20, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WBP1]] (+0.54, fdr 2e-05), [[KAZALD1]] (+0.45, fdr 3e-05), [[ZNF862]] (+0.43, fdr 3e-05); moves opposite to [[ZNF124]] (-0.40, fdr 0.002, ⚠ not reproduced), [[ZNF813]] (-0.40, fdr 6e-04), [[CDK5R1]] (-0.39, fdr 0.001, ⚠ not reproduced), [[COX10]] (-0.39, fdr 2e-04), [[POP1]] (-0.38, fdr 1e-04).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1940.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +9.7 | 2e-19 | 10/14 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +8.7 | 1e-15 | 22/32 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +7.1 | 2e-10 | 22/41 (BT-474, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +6.9 | 9e-10 | 29/41 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +6.1 | 1e-07 | 28/46 (LS 180, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.2 | 2e-05 | 14/46 (NCI-H2030, BT-474, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +5.1 | 2e-05 | 13/42 (LS 180, SW48, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.47×** | +4.7 | 2e-04 | 12/34 (A-172, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +4.7 | 2e-04 | 15/46 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.45×** | +4.6 | 2e-04 | 18/46 (SW480, RKO, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +4.4 | 5e-04 | 18/46 (KATO III, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.002 | 14/43 (LS 180, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.43×** | +4.0 | 0.003 | 11/23 (NCI-H2030, A498, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.37×** | +3.9 | 0.003 | 12/45 (SW480, SHP-77, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.004 | 8/45 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.004 | 14/45 (KATO III, NCI-H460, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.012 | 6/36 (SW480, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.021 | 7/46 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.026 | 14/46 (CFPAC-1, RPMI-7951, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.036 | 8/39 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.063 | 8/42 (KATO III, Hs 766T, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1940.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.455×** | -10.0 | 1e-20 | 30/46 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.492×** | -9.0 | 7e-17 | 33/45 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.526×** | -8.1 | 8e-14 | 29/44 (SW480, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.571×** | -7.1 | 2e-10 | 22/42 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.583×** | -6.8 | 9e-10 | 27/45 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.623×** | -6.0 | 2e-07 | 21/45 (KATO III, BT-474, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.640×** | -5.7 | 1e-06 | 23/45 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.447×** | -5.3 | 7e-06 | 21/40 (J82, HT-29, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.450×** | -5.3 | 8e-06 | 16/39 (HEC-1-A, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.804×** | -3.9 | 0.005 | 19/43 (NCI-H1573, A498, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.723×** | -3.9 | 0.005 | 14/45 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.738×** | -3.9 | 0.005 | 6/46 (C-33 A, NCI-H2030, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.575×** | -3.7 | 0.011 | 18/45 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.780×** | -3.0 | 0.093 | 10/36 (Panc 03.27, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.788×** | -3.0 | 0.093 | 11/45 (NCI-H460, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.790×** | -3.0 | 0.095 | 7/44 (RPMI-7951, SW 1271, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.771×** | -3.0 | 0.095 | 10/44 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1940. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 15.5 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.169× (z -11.0) |
| [[PANC-1 (line)]] | alt | 17.0 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.295× (z -10.1) |
| [[HS-578T (line)]] | alt | 9.09 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -9.3) |
| [[SW480 (line)]] | alt | 10.4 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -12.0) |
| [[BT-474 (line)]] | alt | 5.12 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 0.5 µM 0.0576× (z -8.8) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -8.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 6.99 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0691× (z -9.0) |
| [[LoVo (line)]] | wt | 9.98 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -8.8) |
| [[LS 180 (line)]] | wt | 9.89 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0618× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -9.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 7.91 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0756× (z -15.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.708 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1940), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 12 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WBP1]] | +0.54 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[KAZALD1]] | +0.45 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[ZNF862]] | +0.43 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[DNAJC4]] | +0.43 | +0.34 / +0.44 | both halves | 1e-04 |  |
| [[GSTZ1]] | +0.43 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[CCDC159]] | +0.42 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[GMPPB]] | +0.41 | +0.28 / +0.39 | both halves | 3e-04 |  |
| [[SMIM14]] | +0.41 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[CRELD2]] | +0.41 | +0.24 / +0.50 | both halves | 4e-04 |  |
| [[FASTK]] | +0.41 | +0.44 / +0.38 | both halves | 6e-05 |  |
| [[GBF1]] | +0.41 | +0.15 / +0.61 | ⚠ one half (not replicated) | 0.001 | pathway: Assembly of the 9+0 primary cilium |
| [[UBN2]] | +0.41 | +0.31 / +0.46 | both halves | 2e-04 |  |
| [[VAMP4]] | +0.41 | +0.28 / +0.46 | both halves | 3e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF124]] | -0.40 | -0.14 / -0.42 | ⚠ not reproduced | 0.002 |  |
| [[ZNF813]] | -0.40 | -0.22 / -0.43 | both halves | 6e-04 |  |
| [[CDK5R1]] | -0.39 | -0.15 / -0.31 | ⚠ not reproduced | 0.001 |  |
| [[COX10]] | -0.39 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[POP1]] | -0.38 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[NKRF]] | -0.38 | -0.24 / -0.38 | both halves | 4e-04 |  |
| [[OPN3]] | -0.37 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[LSP1P4]] | -0.37 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[DIAPH2]] | -0.37 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[TBC1D1]] | -0.37 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[MATR3-1]] | -0.37 | -0.07 / -0.47 | ⚠ not reproduced | 0.004 |  |
| [[GTF2IRD1]] | -0.36 | -0.28 / -0.31 | both halves | 3e-04 |  |
| [[UTP4]] | -0.36 | -0.32 / -0.41 | both halves | 1e-04 |  |
| [[CCT3]] | -0.36 | -0.34 / -0.35 | both halves | 1e-04 | pathway: Assembly of the 9+0 primary cilium |
| [[DSG2]] | -0.36 | -0.34 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.285). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.0, -45.2); signed map (34.7, -5.0). **Vector** length 51.4, 7.08% of its response variance represented; |z| ≥ 3 in 866 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +9.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +2.0 | +4.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.9 | +3.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +3.6 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.3 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -5.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.1 | -6.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | intraflagellar transport 27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:36,758,202-36,776,256 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RAYL, BBS19, FAP156, CFAP156; previously RABL4 |
| Gene groups (HGNC) | RAB like GTPases; IFT-B1 complex |
| Reactome | 4 pathways, smallest: Intraflagellar transport; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BW83](https://www.uniprot.org/uniprotkb/Q9BW83) (Intraflagellar transport protein 27 homolog):

> Small GTPase-like component of the intraflagellar transport (IFT) complex B that promotes the exit of the BBSome complex from cilia via its interaction with ARL6. Not involved in entry of the BBSome complex into cilium. Prevents aggregation of GTP-free ARL6. Required for hedgehog signaling. Forms a subcomplex within the IFT complex B with IFT25. Its role in intraflagellar transport is mainly seen in tissues rich in ciliated cells such as kidney and testis. Essential for male fertility, …

**Summary**, from NCBI Gene [11020](https://www.ncbi.nlm.nih.gov/gene/11020):

> This gene encodes a GTP-binding protein that is a core component of the intraflagellar transport complex B. Characterization of the similar Chlamydomonas protein indicates a function in cell cycle control. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:18626](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18626) · Entrez [11020](https://www.ncbi.nlm.nih.gov/gene/11020) · UniProt [Q9BW83](https://www.uniprot.org/uniprotkb/Q9BW83) · Ensembl [ENSG00000100360](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100360)

## Data

Gene col 1940: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1940); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1940, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1940]; `tensor/DDL_lfc|DDL_z.npy` [1940]; `embed/gene_vectors.npy` [1940]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1940 or target_col == 1940). Every well: [[IFT27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFT27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
