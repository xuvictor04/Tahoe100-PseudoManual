---
symbol: "ATP6V0D1-DT"
type: "gene"
col: 15649
ensembl_id: "ENSG00000270049"
name: "ATP6V0D1 divergent transcript"
location: "16q22.1"
module: 35
arm: "+"
pooled_cpm: 9.34
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 31
n_dd_up_clean: 8
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# ATP6V0D1-DT

*ATP6V0D1 divergent transcript* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.97× (z +6.4, q 1e-07, up in 32 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (14 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.187× (z -15.8, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APPBP2-DT]] (+0.65, fdr 1e-05), [[KCTD21-AS1]] (+0.63, fdr 1e-05), [[RPRD2]] (+0.62, fdr 3e-05); moves opposite to [[ARHGDIA]] (-0.57, fdr 2e-05), [[R3HDM4]] (-0.57, fdr 4e-05), [[SCART1]] (-0.56, fdr 8e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[DLX6-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15649.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.97×** | +6.4 | 1e-07 | 32/45 (HOP62, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.76×** | +5.2 | 5e-05 | 32/45 (SW480, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.45×** | +4.9 | 2e-04 | 19/47 (RKO, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.57×** | +4.0 | 0.008 | 15/46 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.49×** | +3.7 | 0.021 | 14/45 (LS 180, A-427, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.047 | 12/47 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.055 | 16/47 (SK-MEL-2, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.076 | 11/46 (SW480, Hs 766T, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.083 | 12/44 (RKO, NCI-H2030, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.083 | 11/47 (Hs 766T, SW480, …) | all doses, flat | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.38× | +3.0 | 0.13 | 8/46 (SW480, SW1417, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15649.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.187×** | -15.8 | 0e+00 | 45/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.231×** | -13.5 | 5e-39 | 43/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.243×** | -13.3 | 4e-38 | 39/41 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.416×** | -11.7 | 2e-29 | 38/44 (COLO 205, A498, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.302×** | -11.0 | 3e-26 | 36/45 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.358×** | -9.3 | 1e-18 | 38/44 (MIA PaCa-2, COLO 205, …) | rises with dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.387×** | -8.6 | 6e-16 | 27/38 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.414×** | -8.3 | 7e-15 | 31/43 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.311×** | -5.8 | 5e-07 | 28/45 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.545×** | -5.7 | 6e-07 | 25/46 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.547×** | -5.7 | 6e-07 | 29/46 (COLO 205, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.559×** | -5.5 | 2e-06 | 26/46 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.557×** | -5.2 | 7e-06 | 23/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.573×** | -5.1 | 1e-05 | 26/46 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.352×** | -5.1 | 1e-05 | 24/42 (NCI-H1573, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.616×** | -4.6 | 2e-04 | 22/46 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.642×** | -4.1 | 0.001 | 21/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.646×** | -4.0 | 0.002 | 18/42 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.762×** | -3.6 | 0.008 | 20/47 (SW480, SNU-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.689×** | -3.5 | 0.011 | 12/46 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Hesperidin (drug)]] 0.05 µM |  | **0.677×** | -3.4 | 0.016 | 11/45 (SW48, RKO, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.702×** | -3.2 | 0.036 | 14/45 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.724×** | -2.9 | 0.077 | 8/47 (A549, LS 180, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.808×** | -2.8 | 0.086 | 16/47 (HT-29, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15649. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.53 | 0 | 11 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0154× (z -25.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0397× (z -20.0) |
| [[NCI-H1573 (line)]] | alt | 16.3 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -15.1) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0865× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 15.0 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0509× (z -14.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0837× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 14.3 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0468× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.123× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 10.0 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0747× (z -13.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.194× (z -8.5) |
| [[SW480 (line)]] | alt | 21.9 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0684× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.111× (z -15.0) |
| [[COLO 205 (line)]] | alt | 15.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0565× (z -17.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0774× (z -10.8) |
| [[Hs 766T (line)]] | wt | 13.3 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0864× (z -11.3) |
| [[J82 (line)]] | alt | 10.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -10.1) |
| [[HCT15 (line)]] | alt | 9.10 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0355× (z -10.9) |
| [[HT-29 (line)]] | alt | 9.34 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0499× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.146× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 5.95 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -9.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H2030 (line)]] | alt | 16.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.142× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 9.05 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0942× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 15.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0885× (z -9.3) |
| [[SW1417 (line)]] | alt | 7.41 | 0 | 2 | — | [[Silodosin (drug)]] 5 µM 0.0834× (z -10.1) |
| [[A-172 (line)]] | wt | 7.82 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0974× (z -10.1) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 13.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -10.5) |
| [[A498 (line)]] | wt | 4.99 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0599× (z -16.7) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A549 (line)]] | wt | 6.02 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -9.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[C-33 A (line)]] | alt | 17.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.116× (z -9.0) |
| [[C32 (line)]] | wt | 8.95 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.117× (z -8.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HOP62 (line)]] | alt | 5.40 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0874× (z -10.2) |
| [[HS-578T (line)]] | alt | 5.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0623× (z -9.7) |
| [[LoVo (line)]] | wt | 6.71 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.139× (z -8.8) |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0714× (z -11.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 5.09 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0623× (z -9.6) |
| [[SW 900 (line)]] | alt | 4.90 | 0 | 1 | — | [[Phenytoin (sodium) (drug)]] 5 µM 0.0576× (z -8.8) |
| [[AN3 CA (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15649), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APPBP2-DT]] | +0.65 | +0.58 / +0.56 | both halves | 1e-05 | same gene group |
| [[KCTD21-AS1]] | +0.63 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[RPRD2]] | +0.62 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[DNAJC30]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[NLRX1]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[DICER1-AS1]] | +0.61 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[TLK2]] | +0.61 | +0.54 / +0.36 | both halves | 9e-05 |  |
| [[RWDD3]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[IDNK]] | +0.60 | +0.65 / +0.39 | both halves | 6e-05 |  |
| [[SLC2A11]] | +0.60 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[PAAF1]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[NUDT13]] | +0.58 | +0.50 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGDIA]] | -0.57 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[R3HDM4]] | -0.57 | -0.40 / -0.55 | both halves | 4e-05 |  |
| [[SCART1]] | -0.56 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[TGM2]] | -0.56 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[EHD4]] | -0.55 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[MICAL2]] | -0.55 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[CYP2E1]] | -0.55 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[NCOR2]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[ACTN1]] | -0.52 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[CADM4]] | -0.52 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[CLIC1]] | -0.51 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[TTLL12]] | -0.51 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLX6-AS1]] | B | DLX6-AS1 activity raises ATP6V0D1-DT's level | lines that do not express DLX6-AS1 (23) vs lines expressing it (27) | 1.66× lower at baseline in the lines without DLX6-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000249776, FBXO27, KIF1A; maybe low, not absent |
| [[ZNF594-DT]] | B | ZNF594-DT activity raises ATP6V0D1-DT's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.77× lower at baseline in the lines without ZNF594-DT | 0.009 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers ATP6V0D1-DT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |
| [[INHA]] | B | INHA activity raises ATP6V0D1-DT's level | lines that do not express INHA (11) vs lines expressing it (39) | 1.50× lower at baseline in the lines without INHA | 0.031 | ⚠ within organs, on part of the lines; also absent: OBSL1, KCNK13 |
| [[STRIP2]] | B | STRIP2 activity weakens ATP6V0D1-DT's drug response | lines that do not express STRIP2 (6) vs lines expressing it (41) | the lines without STRIP2 respond 1.55× as strongly (z diff -2.00); strongest at Harringtonine 5 µM: 0.15x vs 0.34x (z diff -3.5) | 0.052 | ⚠ within organs, on part of the lines; also absent: STK31, HLA-F-AS1, MIR181A2HG; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[DLX6-AS1]] | B | DLX6-AS1 activity strengthens ATP6V0D1-DT's drug response | lines that do not express DLX6-AS1 (22) vs lines expressing it (25) | the lines without DLX6-AS1 respond 0.75× as strongly (z diff +1.48); strongest at Ouabain (Octahydrate) 0.5 µM: 0.40x vs 0.24x (z diff +2.1) | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000249776, FBXO27, KIF1A; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity lowers ATP6V0D1-DT's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[RDM1P5]] | B | RDM1P5 activity raises ATP6V0D1-DT's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.81× lower at baseline in the lines without RDM1P5 | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[CATSPER2P1]] | C | CATSPER2P1 activity raises ATP6V0D1-DT's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 1.94× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent; its own permutation p |
| [[LRRIQ3]] | C | LRRIQ3 activity raises ATP6V0D1-DT's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.57× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.481). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (1.3, 23.7); signed map (34.1, -14.8). **Vector** length 65.4, 12.6% of its response variance represented; |z| ≥ 3 in 1,139 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +4.1 | +4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +5.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.0 | +3.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.7 | -3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.6 | -5.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.4 | -5.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -3.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ATP6V0D1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16q22.1 — chr16:67,481,314-67,505,977 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55268](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55268) · Entrez [101927837](https://www.ncbi.nlm.nih.gov/gene/101927837) · Ensembl [ENSG00000270049](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000270049)

## Data

Gene col 15649: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15649); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15649, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15649]; `tensor/DDL_lfc|DDL_z.npy` [15649]; `embed/gene_vectors.npy` [15649]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15649 or target_col == 15649). Every well: [[ATP6V0D1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6V0D1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
