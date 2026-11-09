---
symbol: "SMUG1"
type: "gene"
col: 4431
ensembl_id: "ENSG00000123415"
name: "single-strand-selective monofunctional uracil-DNA glycosylase 1"
location: "12q13.13"
module: 15
arm: "+"
pooled_cpm: 19.65
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 20
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# SMUG1

*single-strand-selective monofunctional uracil-DNA glycosylase 1* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.77× (z +9.5, q 9e-19, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.360× (z -12.1, q 1e-30, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DARS1-AS1]] (+0.67, fdr 1e-05), [[ANKRD17-DT]] (+0.65, fdr 7e-06), [[CHD1-DT]] (+0.63, fdr 3e-05); moves opposite to [[HLTF]] (-0.57, fdr 5e-05), [[RPAP3]] (-0.54, fdr 8e-04, ⚠ not reproduced), [[SEPTIN6]] (-0.53, fdr 7e-04), [[DYNC2H1]] (-0.53, fdr 2e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4431.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +9.5 | 9e-19 | 40/47 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.4 | 3e-11 | 36/48 (SW1417, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +6.7 | 5e-09 | 32/46 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.42×** | +4.0 | 0.009 | 22/42 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.011 | 18/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.019 | 19/48 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.060 | 14/48 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.074 | 17/47 (SW480, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.099 | 7/48 (A498, LoVo, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.29× | +3.0 | 0.15 | 12/47 (A-172, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4431.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.360×** | -12.1 | 1e-30 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.439×** | -9.7 | 8e-20 | 37/46 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.482×** | -8.6 | 1e-15 | 39/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.506×** | -8.0 | 1e-13 | 36/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.278×** | -7.9 | 3e-13 | 40/48 (A-427, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.626×** | -7.8 | 6e-13 | 29/47 (COLO 205, A-427, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.540×** | -7.0 | 2e-10 | 34/47 (COLO 205, A-427, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.569×** | -6.6 | 2e-09 | 36/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.375×** | -6.0 | 1e-07 | 31/44 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.622×** | -5.4 | 4e-06 | 24/44 (HCT15, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.663×** | -4.8 | 7e-05 | 26/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.492×** | -4.4 | 6e-04 | 19/36 (PANC-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.695×** | -4.0 | 0.002 | 22/47 (HT-29, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.731×** | -3.7 | 0.009 | 16/48 (A-427, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.733×** | -3.4 | 0.027 | 15/35 (HCT15, NCI-H23, …) | inconsistent across doses | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.698×** | -3.0 | 0.076 | 13/48 (PANC-1, SNU-423, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4431. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 27.7 | 1 | 8 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +11.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -16.1) |
| [[SW480 (line)]] | alt | 38.0 | 1 | 8 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.179× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -15.7) |
| [[A-427 (line)]] | wt | 31.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -13.3) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0473× (z -12.5) |
| [[LoVo (line)]] | wt | 24.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0782× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.343× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 30.4 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.137× (z -14.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 23.6 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +8.5) | [[Digitoxin (drug)]] 0.5 µM 0.165× (z -10.0) |
| [[COLO 205 (line)]] | alt | 51.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -18.5) ⚠ cell-cycle shift, explains ~67% of this change |
| [[NCI-H1792 (line)]] | alt | 37.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +9.8) | [[Digitoxin (drug)]] 5 µM 0.126× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 16.4 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -9.6) |
| [[C32 (line)]] | wt | 16.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Imiquimod (maleate) (drug)]] 5 µM 0.155× (z -8.7) |
| [[HCT15 (line)]] | alt | 36.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0420× (z -18.6) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0755× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Verteporfin (drug)]] 0.05 µM 0.0777× (z -8.6) |
| [[LS 180 (line)]] | wt | 12.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.199× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 23.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.3) ⚠ cell-cycle shift, explains ~67% of this change |
| [[RPMI-7951 (line)]] | alt | 14.1 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.121× (z -9.2) ⚠ toxic · without an alert: [[Hesperidin (drug)]] 5 µM 0.142× (z -8.5) |
| [[A-172 (line)]] | wt | 11.4 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0918× (z -12.2) ⚠ toxic |
| [[A549 (line)]] | wt | 21.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -11.4) ⚠ cell-cycle shift, explains ~67% of this change |
| [[CFPAC-1 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -9.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 21.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0943× (z -10.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[HOP62 (line)]] | alt | 10.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -9.8) |
| [[HT-29 (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -12.9) ⚠ cell-cycle shift, explains ~67% of this change |
| [[KATO III (line)]] | alt | 24.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -9.4) |
| [[A498 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4431), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DARS1-AS1]] | +0.67 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[ANKRD17-DT]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[CHD1-DT]] | +0.63 | +0.69 / +0.44 | both halves | 3e-05 |  |
| [[PELO-AS1]] | +0.62 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[LINC01376]] | +0.61 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ZNF213-AS1]] | +0.61 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[SMIM12]] | +0.61 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[PRANCR]] | +0.60 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[CHTF8]] | +0.59 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[SPESP1]] | +0.59 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[SIAH2-AS1]] | +0.59 | +0.59 / +0.34 | both halves | 1e-04 |  |
| [[HLA-DMA]] | +0.58 | +0.54 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLTF]] | -0.57 | -0.41 / -0.40 | both halves | 5e-05 | STRING 444 |
| [[RPAP3]] | -0.54 | -0.19 / -0.41 | ⚠ not reproduced | 8e-04 |  |
| [[SEPTIN6]] | -0.53 | -0.54 / -0.20 | both halves | 7e-04 |  |
| [[DYNC2H1]] | -0.53 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[SKIC3]] | -0.52 | -0.46 / -0.32 | both halves | 1e-04 |  |
| [[IFT52]] | -0.51 | -0.41 / -0.28 | both halves | 3e-04 |  |
| [[MNS1]] | -0.51 | -0.25 / -0.32 | both halves | 4e-04 |  |
| [[CCDC112]] | -0.51 | -0.40 / -0.11 | ⚠ not reproduced | 0.002 |  |
| [[LRRCC1]] | -0.50 | -0.18 / -0.48 | ⚠ not reproduced | 9e-04 |  |
| [[TTC26]] | -0.50 | -0.17 / -0.39 | ⚠ not reproduced | 0.001 |  |
| [[ALDH7A1]] | -0.50 | -0.22 / -0.49 | both halves | 6e-04 |  |
| [[SSX2IP]] | -0.50 | -0.37 / -0.44 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SMUG1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.610). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (4.6, 17.5); signed map (26.5, -7.1). **Vector** length 58.1, 9.98% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +9.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +0.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +0.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.5 | +2.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -2.7 | +3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +1.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.3 | -7.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.2 | +3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | +2.0 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.5 | -1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | single-strand-selective monofunctional uracil-DNA glycosylase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:54,121,277-54,189,008 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UNG3, FDG, HMUDG |
| Gene groups (HGNC) | DNA glycosylases |
| Reactome | 8 pathways, smallest: Displacement of DNA glycosylase by APEX1; Cleavage of the damaged pyrimidine; Depyrimidination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53HV7](https://www.uniprot.org/uniprotkb/Q53HV7) (Single-strand selective monofunctional uracil DNA glycosylase):

> Recognizes base lesions in the genome and initiates base excision DNA repair. Acts as a monofunctional DNA glycosylase specific for uracil (U) residues in DNA with a preference for single-stranded DNA substrates. The activity is greater toward mismatches (U/G) compared to matches (U/A). Excises uracil (U), 5-formyluracil (fU) and uracil derivatives bearing an oxidized group at C5 [5-hydroxyuracil (hoU) and 5-hydroxymethyluracil (hmU)] in ssDNA and dsDNA, but not analogous cytosine derivatives …

**Summary**, from NCBI Gene [23583](https://www.ncbi.nlm.nih.gov/gene/23583):

> This gene encodes a protein that participates in base excision repair by removing uracil from single- and double-stranded DNA. Many alternatively spliced transcript variants exist for this gene; the full-length nature is known for some but not all of the variants. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:17148](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17148) · Entrez [23583](https://www.ncbi.nlm.nih.gov/gene/23583) · UniProt [Q53HV7](https://www.uniprot.org/uniprotkb/Q53HV7) · Ensembl [ENSG00000123415](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123415)

## Data

Gene col 4431: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4431); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4431, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4431]; `tensor/DDL_lfc|DDL_z.npy` [4431]; `embed/gene_vectors.npy` [4431]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4431 or target_col == 4431). Every well: [[SMUG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMUG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
