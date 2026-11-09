---
symbol: "BLOC1S5-TXNDC5"
type: "gene"
col: 15165
ensembl_id: "ENSG00000259040"
name: "BLOC1S5-TXNDC5 readthrough (NMD candidate)"
location: "6p24.3"
module: 207
arm: "+"
pooled_cpm: 16.78
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 35
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/207"]
generated_by: "tahoemap"
---

# BLOC1S5-TXNDC5

*BLOC1S5-TXNDC5 readthrough (NMD candidate)* — 6p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.38× (z +7.0, q 2e-09, up in 29 of 48 measured lines) ⚠ cell-cycle shift, explains ~84% of this change. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 1.34× (z +4.5, q 0.002, up in 16 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (22 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.354× (z -15.9, q 0e+00, down in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.248× (z -11.2, q 9e-27, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLE1]] (+0.62, fdr 1e-05), [[BLOC1S5]] (+0.58, fdr 1e-05, ⚠ same locus), [[TMED8]] (+0.52, fdr 5e-05), [[PPP1R8]] (+0.51, fdr 3e-05); moves opposite to [[B4GAT1-DT]] (-0.52, fdr 5e-05), [[GDF11]] (-0.48, fdr 3e-05), [[ADGRL1]] (-0.46, fdr 6e-05).
> It sits in the **+** arm of [[Module 207]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15165.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.38×** | +7.0 | 2e-09 | 29/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **1.34×** | +4.5 | 0.002 | 16/48 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.34×** | +4.4 | 0.002 | 17/48 (LS 180, J82, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.26× | +3.4 | 0.10 | 6/47 (NCI-H2030, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 23 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15165.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.354×** | -15.9 | 0e+00 | 43/48 (KATO III, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.566×** | -12.3 | 2e-32 | 29/47 (HEC-1-A, Panc 03.27, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.461×** | -11.9 | 3e-30 | 42/47 (HOP62, SHP-77, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.248×** | -11.2 | 9e-27 | 41/48 (A549, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.473×** | -11.1 | 2e-26 | 41/48 (AsPC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.488×** | -11.0 | 4e-26 | 36/48 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.483×** | -10.7 | 5e-25 | 40/46 (HepG2/C3A, Hs 766T, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.485×** | -10.7 | 1e-24 | 29/48 (HS-578T, HEC-1-A, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.533×** | -9.7 | 3e-20 | 22/40 (LoVo, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.559×** | -8.6 | 4e-16 | 36/47 (HT-29, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.573×** | -8.2 | 1e-14 | 19/30 (LOX-IMVI, KATO III, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.588×** | -7.5 | 2e-12 | 20/36 (HS-578T, PANC-1, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.639×** | -6.9 | 3e-10 | 28/47 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.633×** | -6.8 | 6e-10 | 26/44 (NCI-H2030, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.660×** | -6.2 | 3e-08 | 27/47 (NCI-H1792, SW480, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.499×** | -5.6 | 9e-07 | 24/47 (HEC-1-A, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.704×** | -5.2 | 7e-06 | 24/48 (J82, HCT15, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.839× | -3.8 | 0.004 | 16/48 (MIA PaCa-2, RPMI-7951, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.780×** | -3.7 | 0.006 | 8/48 (NCI-H2030, SW 1088, …) | top dose only |  |
| [[NG25 (drug)]] 0.05 µM |  | **0.804×** | -3.2 | 0.030 | 8/48 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.681×** | -3.1 | 0.039 | 7/45 (SW 900, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.732×** | -3.1 | 0.041 | 5/47 (Panc 03.27, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.812×** | -3.0 | 0.043 | 13/48 (CFPAC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.879× | -2.8 | 0.080 | 9/48 (CFPAC-1, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.709×** | -2.8 | 0.089 | 5/47 (SW1417, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **0.831×** | -2.7 | 0.089 | 7/47 (NCI-H661, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15165. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 26.4 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.254× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.136× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 25.5 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -13.0) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.294× (z -8.9) |
| [[A549 (line)]] | wt | 15.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0383× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 16.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.8) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.238× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 29.6 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0731× (z -12.7) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 24.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0518× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[KATO III (line)]] | alt | 23.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[LOX-IMVI (line)]] | wt | 19.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.1000× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[NCI-H2030 (line)]] | alt | 32.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[Panc 03.27 (line)]] | alt | 23.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[RPMI-7951 (line)]] | alt | 20.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -11.4) ⚠ cell-cycle shift, explains ~68% of this change |
| [[A-172 (line)]] | wt | 12.8 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -9.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 10.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -10.7) ⚠ cell-cycle shift, explains ~68% of this change |
| [[AsPC-1 (line)]] | alt | 6.96 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HT-29 (line)]] | alt | 9.74 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0805× (z -12.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[hTERT-HPNE (line)]] | wt | 17.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0787× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Roxadustat (drug)]] 0.05 µM 0.0819× (z -10.6) |
| [[J82 (line)]] | alt | 19.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -9.6) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.257× (z -8.6) |
| [[LoVo (line)]] | wt | 16.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0981× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[MIA PaCa-2 (line)]] | alt | 20.7 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.166× (z -11.7) ⚠ transcription drop; cell-cycle shift, explains ~85% of this change |
| [[NCI-H1792 (line)]] | alt | 14.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[PANC-1 (line)]] | alt | 12.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-427 (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -9.0) ⚠ cell-cycle shift, explains ~68% of this change |
| [[AN3 CA (line)]] | alt | 26.9 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.0922× (z -8.5) |
| [[C32 (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -10.0) ⚠ cell-cycle shift, explains ~68% of this change |
| [[HCT15 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.158× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[Hs 766T (line)]] | wt | 10.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0981× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 8.85 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.141× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 9.03 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.243× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[RKO (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -11.1) ⚠ cell-cycle shift, explains ~68% of this change |
| [[SHP-77 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SNU-1 (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.163× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -11.0) ⚠ cell-cycle shift, explains ~68% of this change |
| [[SW 900 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0865× (z -12.4) ⚠ transcription drop; cell-cycle shift, explains ~85% of this change |
| [[BT-474 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15165), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLE1]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[BLOC1S5]] | +0.58 | +0.63 / +0.49 | both halves | 1e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TMED8]] | +0.52 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[PPP1R8]] | +0.51 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[METTL21EP-1]] | +0.49 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[TSNAX-DISC1]] | +0.49 | +0.44 / +0.35 | both halves | 1e-04 |  |
| [[VPS39]] | +0.49 | +0.40 / +0.37 | both halves | 8e-05 |  |
| [[TXNL4B]] | +0.49 | +0.43 / +0.30 | both halves | 2e-04 |  |
| [[METTL15]] | +0.48 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[FAM209A]] | +0.47 | +0.39 / +0.43 | both halves | 6e-05 |  |
| [[RNF14]] | +0.47 | +0.38 / +0.47 | both halves | 6e-05 |  |
| [[PMS2P4-1]] | +0.46 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[GET1-SH3BGR]] | +0.46 | +0.53 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B4GAT1-DT]] | -0.52 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[GDF11]] | -0.48 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[ADGRL1]] | -0.46 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[LINC00173]] | -0.45 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[MAGI1]] | -0.44 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[MMP16]] | -0.42 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[LRP2]] | -0.42 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[ALCAM]] | -0.42 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[CENPB]] | -0.42 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[GSK3B]] | -0.42 | -0.31 / -0.21 | both halves | 7e-04 |  |
| [[NCAM2]] | -0.41 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[PREX1]] | -0.41 | -0.31 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 207]]; 15 genes; this gene is in the **+** arm (projection on the module's main direction 0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-16.1, 19.3); signed map (-19.6, -13.2). **Vector** length 64.8, 11.2% of its response variance represented; |z| ≥ 3 in 1,169 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | +5.8 | +7.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.8 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +2.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +2.4 | -3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | +1.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.5 | +0.7 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +1.4 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -3.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | -4.0 | -10.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.2 | -6.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.1 | -4.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.0 | -11.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -11.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | +1.2 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | BLOC1S5-TXNDC5 readthrough (NMD candidate) |
| Locus type | readthrough (other) |
| Location | 6p24.3 — chr6:7,881,522-8,064,364 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MUTED-TXNDC5 |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100526836](https://www.ncbi.nlm.nih.gov/gene/100526836):

> This locus represents naturally occurring read-through transcription between the neighboring MUTED (muted homolog) and TXNDC5 (thioredoxin domain containing 5) genes on chromosome 6. The read-through transcript is a candidate for nonsense-mediated mRNA decay (NMD) and is unlikely to produce a protein product. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:42001](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42001) · Entrez [100526836](https://www.ncbi.nlm.nih.gov/gene/100526836) · Ensembl [ENSG00000259040](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259040)

## Data

Gene col 15165: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15165); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15165, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15165]; `tensor/DDL_lfc|DDL_z.npy` [15165]; `embed/gene_vectors.npy` [15165]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15165 or target_col == 15165). Every well: [[BLOC1S5-TXNDC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BLOC1S5-TXNDC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
