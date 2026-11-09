---
symbol: "RABL2B"
type: "gene"
col: 1270
ensembl_id: "ENSG00000079974"
name: "RAB, member of RAS oncogene family like 2B"
location: "22q13.33"
module: 15
arm: "+"
pooled_cpm: 9.87
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 15
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# RABL2B

*RAB, member of RAS oncogene family like 2B* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.62× (z +17.2, q 0e+00, up in 40 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.455× (z -9.9, q 2e-20, down in 34 of 46 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RABL2A]] (+0.91, fdr 7e-06), [[MORN1]] (+0.64, fdr 7e-06), [[PACRGL]] (+0.62, fdr 3e-05); moves opposite to [[ATP1A3]] (-0.58, fdr 0.001, ⚠ one half only (not replicated)), [[CFD]] (-0.58, fdr 1e-04), [[CBR1]] (-0.56, fdr 3e-04), [[PRKAR2B]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1270.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.62×** | +17.2 | 0e+00 | 40/43 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +10.9 | 2e-25 | 36/44 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.77×** | +10.3 | 2e-22 | 36/48 (CFPAC-1, RKO, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +7.1 | 2e-10 | 12/17 (HT-29, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +7.1 | 2e-10 | 26/42 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.73×** | +7.0 | 3e-10 | 29/47 (LoVo, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +6.1 | 8e-08 | 20/34 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.60×** | +5.7 | 7e-07 | 22/36 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +5.5 | 2e-06 | 24/47 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.32×** | +4.9 | 5e-05 | 19/48 (NCI-H1573, RKO, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +4.4 | 5e-04 | 12/26 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.41×** | +4.4 | 6e-04 | 16/45 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.41×** | +4.3 | 7e-04 | 10/47 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.036 | 7/48 (A549, NCI-H460, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.046 | 12/45 (NCI-H23, C-33 A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.047 | 12/47 (RKO, SNU-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.085 | 6/47 (NCI-H460, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1270.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.455×** | -9.9 | 2e-20 | 34/46 (NCI-H460, SW480, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.562×** | -7.3 | 9e-11 | 27/47 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.682×** | -6.8 | 2e-09 | 30/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.591×** | -6.6 | 4e-09 | 25/45 (SNU-423, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.601×** | -6.4 | 2e-08 | 25/45 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.615×** | -6.1 | 8e-08 | 26/46 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.631×** | -5.8 | 5e-07 | 23/47 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.661×** | -5.0 | 4e-05 | 18/38 (hTERT-HPNE, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.718×** | -3.9 | 0.005 | 18/44 (LS 180, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.740×** | -3.8 | 0.009 | 11/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.744×** | -3.7 | 0.010 | 20/46 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.750×** | -3.6 | 0.014 | 19/46 (A-427, HS-578T, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.581×** | -3.6 | 0.015 | 11/39 (LS 180, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.620×** | -3.2 | 0.064 | 10/33 (HS-578T, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.780×** | -3.1 | 0.067 | 16/46 (LoVo, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1270. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 14.0 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.188× (z -13.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.266× (z -10.3) |
| [[LoVo (line)]] | wt | 11.4 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.238× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 9.03 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.0756× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.170× (z -8.7) |
| [[KATO III (line)]] | alt | 10.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.166× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 7.80 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 17.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.8) | [[Digitoxin (drug)]] 5 µM 0.277× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 9.63 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.175× (z -9.4) ⚠ toxic |
| [[A498 (line)]] | wt | 8.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +8.9) | — |
| [[AsPC-1 (line)]] | alt | 3.76 | 0 | 1 | — | [[Flutamide (drug)]] 5 µM 0.0622× (z -8.9) |
| [[BT-474 (line)]] | alt | 4.85 | 0 | 1 | — | [[Budesonide (drug)]] 0.5 µM 0.0675× (z -8.7) |
| [[H4 (line)]] | wt | 8.33 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0647× (z -8.5) |
| [[Hs 766T (line)]] | wt | 11.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM 0.0657× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 7.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.189× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 9.23 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0576× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 5.06 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.101× (z -9.1) ⚠ toxic |
| [[A-172 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1270), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABL2A]] | +0.91 | +0.88 / +0.88 | both halves | 7e-06 | same gene group; STRING 454 |
| [[MORN1]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[PACRGL]] | +0.62 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[LENG8-AS1]] | +0.61 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[SENP8]] | +0.61 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[EFCAB6]] | +0.61 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[POLDIP2]] | +0.60 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[CEP164]] | +0.59 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[UBE3B]] | +0.59 | +0.64 / +0.36 | both halves | 9e-05 |  |
| [[DDX59]] | +0.59 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[QTRT1]] | +0.59 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[ARSD]] | +0.58 | +0.41 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP1A3]] | -0.58 | -0.18 / -0.56 | ⚠ one half (not replicated) | 0.001 |  |
| [[CFD]] | -0.58 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[CBR1]] | -0.56 | -0.29 / -0.51 | both halves | 3e-04 |  |
| [[PRKAR2B]] | -0.56 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[SUSD4]] | -0.54 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[HMGN3]] | -0.54 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[CAMK2G]] | -0.53 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[FCHO1]] | -0.53 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[RASAL1]] | -0.52 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[RADX]] | -0.51 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[EDA]] | -0.51 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[PEDS1]] | -0.51 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[CDC14B]] | -0.51 | -0.44 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RABL2B's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 2.8% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[NCMAP]] | B | NCMAP activity lowers RABL2B's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 1.25× higher at baseline in the lines without NCMAP | 0.034 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |
| [[PREX1]] | B | PREX1 activity raises RABL2B's level | lines that do not express PREX1 (18) vs lines expressing it (32) | 1.24× lower at baseline in the lines without PREX1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, SOGA3, PCBP3 |
| [[SLC5A4-AS1]] | B | SLC5A4-AS1 activity raises RABL2B's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.34× lower at baseline in the lines without SLC5A4-AS1 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.510). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-7.3, 17.4); signed map (27.9, -20.7). **Vector** length 75.0, 13.5% of its response variance represented; |z| ≥ 3 in 1,128 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +17.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +10.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +10.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.2 | +7.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.7 | +3.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.4 | +3.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.4 | -6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.7 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.3 | -9.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.3 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -0.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.6 | -2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | +1.3 |

## What is on record

|  |  |
|---|---|
| Name | RAB, member of RAS oncogene family like 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,767,501-50,783,667 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB like GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNT1](https://www.uniprot.org/uniprotkb/Q9UNT1) (Rab-like protein 2B):

> Small GTPase required for ciliation. Activated in a guanine nucleotide exchange factor (GEF)-independent manner via its intrinsic GDP for GTP nucleotide exchange ability. Involved in ciliary assembly by binding the intraflagellar transport (IFT) complex B from the large pool pre-docked at the base of the cilium and thus triggers its entry into the cilia.

**Summary**, from NCBI Gene [11158](https://www.ncbi.nlm.nih.gov/gene/11158):

> The RABL2B protein is a member of the RAB gene family which belongs to the RAS GTPase superfamily. RABL2B is located within a subtelomeric region of 22q13.3. Multiple alternatively spliced transcript variants encoding several different isoforms have been found for this gene. [provided by RefSeq, Aug 2008]

**Accessions** — [HGNC:9800](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9800) · Entrez [11158](https://www.ncbi.nlm.nih.gov/gene/11158) · UniProt [Q9UNT1](https://www.uniprot.org/uniprotkb/Q9UNT1) · Ensembl [ENSG00000079974](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079974)

## Data

Gene col 1270: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1270); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1270, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1270]; `tensor/DDL_lfc|DDL_z.npy` [1270]; `embed/gene_vectors.npy` [1270]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1270 or target_col == 1270). Every well: [[RABL2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RABL2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
