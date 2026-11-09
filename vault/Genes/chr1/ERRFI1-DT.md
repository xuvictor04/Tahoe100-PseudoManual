---
symbol: "ERRFI1-DT"
type: "gene"
col: 14181
ensembl_id: "ENSG00000238290"
name: "ERRFI1 divergent transcript"
location: "1p36.23"
module: 101
arm: "+"
pooled_cpm: 26.51
n_lines_expressing: 37
n_dd_up: 15
n_dd_down: 30
n_dd_up_clean: 12
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# ERRFI1-DT

*ERRFI1 divergent transcript* — 1p36.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.18× (z +23.7, q 0e+00, up in 30 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.397× (z -10.8, q 2e-24, down in 29 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCL1]] (+0.68, fdr 7e-06), [[LETM2]] (+0.65, fdr 1e-05), [[ITGA2-AS1]] (+0.65, fdr 1e-05); moves opposite to [[CAPN7]] (-0.56, fdr 3e-05), [[GPRC5B]] (-0.50, fdr 6e-05), [[IFT172]] (-0.50, fdr 9e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[ERRFI1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14181.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.18×** | +23.7 | 0e+00 | 30/34 (CFPAC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.41×** | +13.3 | 8e-38 | 19/29 (MIA PaCa-2, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.37×** | +10.1 | 9e-22 | 30/35 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.78×** | +9.6 | 1e-19 | 27/35 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +8.6 | 8e-16 | 23/35 (HCT15, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.93×** | +7.7 | 1e-12 | 18/31 (AsPC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +7.5 | 7e-12 | 19/34 (HOP62, AsPC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +7.4 | 1e-11 | 19/34 (AsPC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +6.0 | 1e-07 | 10/23 (HEC-1-A, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +5.1 | 2e-05 | 17/35 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.46×** | +4.4 | 5e-04 | 16/35 (HepG2/C3A, PANC-1, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.003 | 11/35 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.39×** | +3.9 | 0.005 | 13/34 (A-172, CFPAC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +3.8 | 0.007 | 12/35 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.029 | 15/34 (A-172, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14181.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.397×** | -10.8 | 2e-24 | 29/35 (SW 1271, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.449×** | -9.0 | 5e-17 | 28/33 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.477×** | -8.7 | 1e-15 | 29/34 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.513×** | -7.8 | 9e-13 | 24/34 (HOP62, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.528×** | -7.5 | 9e-12 | 25/35 (A-427, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.532×** | -7.4 | 2e-11 | 23/34 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.552×** | -6.9 | 3e-10 | 27/35 (A-427, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.571×** | -6.6 | 4e-09 | 29/35 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.579×** | -6.4 | 1e-08 | 25/34 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.579×** | -6.4 | 1e-08 | 25/34 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.366×** | -6.2 | 4e-08 | 24/35 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.583×** | -6.0 | 1e-07 | 25/35 (HepG2/C3A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.601×** | -6.0 | 1e-07 | 23/35 (HepG2/C3A, HOP62, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.731×** | -5.2 | 9e-06 | 21/35 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.717×** | -5.1 | 1e-05 | 22/35 (NCI-H1792, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.439×** | -5.0 | 2e-05 | 18/33 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.657×** | -4.9 | 3e-05 | 14/35 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.656×** | -4.7 | 7e-05 | 18/34 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14181. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 242 | 0 | 13 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0902× (z -17.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.165× (z -13.4) |
| [[NCI-H23 (line)]] | alt | 146 | 0 | 12 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0897× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.122× (z -15.2) |
| [[PANC-1 (line)]] | alt | 64.1 | 1 | 10 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.103× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -16.5) |
| [[HOP62 (line)]] | alt | 40.3 | 4 (1 ⚠) | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +16.0) | [[Ixazomib citrate (drug)]] 5 µM 0.139× (z -12.8) |
| [[A-427 (line)]] | wt | 134 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0981× (z -18.3) |
| [[AsPC-1 (line)]] | alt | 16.7 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.6× (z +16.3) | [[Docetaxel (drug)]] 0.05 µM 0.0775× (z -11.2) ⚠ transcription drop; cell-cycle shift, explains ~43% of this change |
| [[NCI-H1573 (line)]] | alt | 30.8 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -13.0) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.111× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 84.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 6.48× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +10.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.151× (z -13.3) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 108 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0146× (z -16.5) |
| [[HEC-1-A (line)]] | alt | 24.0 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -9.5) |
| [[LoVo (line)]] | wt | 8.42 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.35× (z +9.6) | — |
| [[A549 (line)]] | wt | 8.39 | 0 | 2 (1 ⚠) | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0424× (z -12.2) |
| [[KATO III (line)]] | alt | 12.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.75× (z +14.0) | — |
| [[Panc 03.27 (line)]] | alt | 17.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.54× (z +12.1) | [[EX229 (drug)]] 5 µM 0.0363× (z -8.7) |
| [[SHP-77 (line)]] | alt | 16.4 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0659× (z -11.1) |
| [[SW480 (line)]] | alt | 7.98 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +9.8) | — |
| [[C32 (line)]] | wt | 6.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.92× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.9× (z +17.6) | — |
| [[COLO 205 (line)]] | alt | 21.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.153× (z -8.6) |
| [[H4 (line)]] | wt | 24.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -10.9) ⚠ cell-cycle shift, explains ~65% of this change |
| [[HCT15 (line)]] | alt | 19.6 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0978× (z -10.2) |
| [[HS-578T (line)]] | alt | 22.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.110× (z -8.5) |
| [[HT-29 (line)]] | alt | 28.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.202× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 16.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 19.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.145× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 16.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.87× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 26.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0599× (z -11.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.37× (z +10.6) | — |
| [[A-172 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.30 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.41 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.10 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.54 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.57 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.91 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.69 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.33 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.01 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.66 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14181), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCL1]] | +0.68 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[LETM2]] | +0.65 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ITGA2-AS1]] | +0.65 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ACTR3-AS1]] | +0.64 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ADAMTSL4-AS2]] | +0.64 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[SPRY4-AS1]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[NOP14-AS1]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[MYADM-AS1]] | +0.62 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[PCBP1-AS1]] | +0.61 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[TMEM156]] | +0.60 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[LINC00705]] | +0.59 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[HCG20]] | +0.59 | +0.35 / +0.61 | both halves | 1e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN7]] | -0.56 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[GPRC5B]] | -0.50 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[IFT172]] | -0.50 | -0.38 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ERRFI1-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity raises ERRFI1-DT's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 5.6% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERRFI1]] | B | ERRFI1-DT activity raises ERRFI1's level | lines that do not express ERRFI1-DT (13) vs lines expressing it (37) | 2.67× lower at baseline in the lines without ERRFI1-DT | 0.010 | ⚠ within organs, on part of the lines; also absent: GCAWKR; maybe low, not absent |
| [[HIVEP2-DT]] | B | ERRFI1-DT activity raises HIVEP2-DT's level | lines that do not express ERRFI1-DT (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without ERRFI1-DT | 0.044 | ⚠ within organs, on part of the lines; also absent: GCAWKR; maybe low, not absent |
| [[LINC00705]] | B | ERRFI1-DT activity raises LINC00705's level | lines that do not express ERRFI1-DT (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without ERRFI1-DT | 0.046 | ⚠ within organs, on part of the lines; also absent: GCAWKR; maybe low, not absent |
| [[PIPOX]] | B | ERRFI1-DT activity raises PIPOX's level | lines that do not express ERRFI1-DT (13) vs lines expressing it (37) | 1.44× lower at baseline in the lines without ERRFI1-DT | 0.054 | ⚠ within organs, on part of the lines; also absent: GCAWKR; maybe low, not absent |
| [[HMGA2-AS1]] | B | ERRFI1-DT activity lowers HMGA2-AS1's level | lines that do not express ERRFI1-DT (13) vs lines expressing it (37) | 1.26× higher at baseline in the lines without ERRFI1-DT | 0.059 | ⚠ within organs, on part of the lines; also absent: GCAWKR; maybe low, not absent |
| [[MYOM1]] | B | ERRFI1-DT activity raises MYOM1's level | lines that do not express ERRFI1-DT (13) vs lines expressing it (37) | 2.03× lower at baseline in the lines without ERRFI1-DT | 0.066 | ⚠ within organs, on part of the lines; also absent: GCAWKR; maybe low, not absent |
| [[LINC01277]] | B | ERRFI1-DT activity raises LINC01277's level | lines that do not express ERRFI1-DT (13) vs lines expressing it (37) | 1.28× lower at baseline in the lines without ERRFI1-DT | 0.089 | ⚠ within organs, on part of the lines; also absent: GCAWKR; maybe low, not absent |

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.7, -6.4); signed map (16.5, 19.7). **Vector** length 112, 29.5% of its response variance represented; |z| ≥ 3 in 1,103 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +23.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.0 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +13.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +2.3 |
| fall | [[NG25 (drug)]] 5 µM |  | -5.3 | -4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.7 | -7.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.6 | -6.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.2 | -7.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.8 | -4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.4 | -5.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.3 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ERRFI1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p36.23 — chr1:8,026,738-8,122,702 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55646](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55646) · Entrez [121832806](https://www.ncbi.nlm.nih.gov/gene/121832806) · Ensembl [ENSG00000238290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000238290)

## Data

Gene col 14181: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14181); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14181, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14181]; `tensor/DDL_lfc|DDL_z.npy` [14181]; `embed/gene_vectors.npy` [14181]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14181 or target_col == 14181). Every well: [[ERRFI1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERRFI1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
