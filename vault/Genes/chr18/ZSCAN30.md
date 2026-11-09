---
symbol: "ZSCAN30"
type: "gene"
col: 11857
ensembl_id: "ENSG00000186814"
name: "zinc finger and SCAN domain containing 30"
location: "18q12.2"
module: 10
arm: "+"
pooled_cpm: 21.0
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 21
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ZSCAN30

*zinc finger and SCAN domain containing 30* — 18q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 1.62× (z +5.4, q 5e-05, up in 21 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.54× (z +5.0, q 1e-04, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.280× (z -15.2, q 0e+00, down in 38 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.281× (z -15.2, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF655]] (+0.67, fdr 1e-05), [[RIPK2-DT]] (+0.67, fdr 7e-06), [[GDAP1]] (+0.67, fdr 1e-05); moves opposite to [[NPHP4]] (-0.63, fdr 2e-05), [[ZMYND19]] (-0.63, fdr 3e-05), [[PBX4]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[THBS4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11857.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +5.4 | 5e-05 | 21/36 (NCI-H2347, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.54×** | +5.0 | 1e-04 | 29/47 (NCI-H23, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.49×** | +4.8 | 3e-04 | 23/43 (NCI-H2347, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.45×** | +4.2 | 0.003 | 20/48 (A-427, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.42×** | +4.2 | 0.003 | 21/47 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.27×** | +4.0 | 0.005 | 23/48 (LS 180, A-427, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.29×** | +4.0 | 0.005 | 20/48 (NCI-H23, A-427, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.38×** | +3.7 | 0.013 | 20/47 (NCI-H23, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.018 | 21/48 (A-427, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.33×** | +3.5 | 0.031 | 18/48 (A-172, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.091 | 17/47 (NCI-H23, A-427, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.0 | 0.11 | 16/48 (NCI-H2347, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11857.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.280×** | -15.2 | 0e+00 | 38/47 (SHP-77, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.281×** | -15.2 | 0e+00 | 45/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.338×** | -13.0 | 2e-36 | 42/48 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.342×** | -12.9 | 1e-35 | 45/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.488×** | -8.6 | 1e-15 | 37/48 (J82, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.542×** | -7.1 | 2e-10 | 32/47 (A549, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.531×** | -7.0 | 3e-10 | 30/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.679×** | -6.6 | 4e-09 | 28/47 (CFPAC-1, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.616×** | -5.8 | 4e-07 | 29/48 (NCI-H1792, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.638×** | -5.4 | 4e-06 | 29/48 (SK-MEL-2, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.659×** | -5.0 | 3e-05 | 29/48 (SK-MEL-2, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.644×** | -5.0 | 3e-05 | 27/48 (J82, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.469×** | -4.7 | 1e-04 | 20/40 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.709×** | -3.8 | 0.006 | 20/47 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.737×** | -3.6 | 0.010 | 19/48 (J82, Panc 03.27, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.753×** | -3.4 | 0.023 | 16/48 (C32, AsPC-1, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.588×** | -3.3 | 0.028 | 21/48 (SW1417, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.681×** | -3.3 | 0.030 | 13/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11857. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 31.7 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.86× (z +11.1) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 39.8 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.180× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 26.8 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.141× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 35.7 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.168× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.221× (z -9.9) |
| [[PANC-1 (line)]] | alt | 26.0 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.205× (z -12.4) |
| [[SHP-77 (line)]] | alt | 20.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0469× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.189× (z -9.8) |
| [[A-427 (line)]] | wt | 27.0 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 19.1 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.201× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.270× (z -8.5) |
| [[COLO 205 (line)]] | alt | 13.9 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -9.9) |
| [[H4 (line)]] | wt | 29.1 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0866× (z -10.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -10.4) |
| [[HOP62 (line)]] | alt | 20.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.235× (z -10.1) |
| [[Hs 766T (line)]] | wt | 33.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -9.2) |
| [[J82 (line)]] | alt | 23.8 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.180× (z -11.2) |
| [[LoVo (line)]] | wt | 13.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.214× (z -10.2) |
| [[LS 180 (line)]] | wt | 22.6 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 41.3 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.199× (z -12.0) |
| [[SW480 (line)]] | alt | 8.53 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -9.8) |
| [[HS-578T (line)]] | alt | 26.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.218× (z -9.0) |
| [[A549 (line)]] | wt | 6.82 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.104× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[AsPC-1 (line)]] | alt | 8.57 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.101× (z -9.8) |
| [[C32 (line)]] | wt | 26.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -13.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0572× (z -12.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.186× (z -11.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 15.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 18.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.261× (z -10.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 23.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.207× (z -9.3) |
| [[RKO (line)]] | wt | 33.8 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.179× (z -11.3) ⚠ cell-cycle shift, explains ~48% of this change |
| [[RPMI-7951 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.234× (z -8.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 14.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.162× (z -9.3) |
| [[A-172 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11857), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF655]] | +0.67 | +0.51 / +0.63 | both halves | 1e-05 | same gene group |
| [[RIPK2-DT]] | +0.67 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[GDAP1]] | +0.67 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[SUCLG2-DT]] | +0.67 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[USP40]] | +0.66 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[KRBA2]] | +0.66 | +0.71 / +0.41 | both halves | 4e-05 |  |
| [[TSPYL4]] | +0.66 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ARRDC3-AS1]] | +0.64 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[NRAS]] | +0.64 | +0.38 / +0.62 | both halves | 6e-05 |  |
| [[ZNF528]] | +0.64 | +0.61 / +0.49 | both halves | 1e-05 | same gene group |
| [[FNBP1P1]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[CTBP1-DT]] | +0.64 | +0.65 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHP4]] | -0.63 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[ZMYND19]] | -0.63 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[PBX4]] | -0.62 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[MRPL41]] ⚠ | -0.61 | -0.35 / -0.49 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[SH2B2]] | -0.61 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[SIVA1]] | -0.61 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ANAPC11]] | -0.60 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[LSM2]] | -0.60 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[FANCE]] | -0.60 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[CCNQ]] | -0.60 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[SLC25A5]] | -0.59 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[PI4KAP2]] | -0.59 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[MPG]] | -0.59 | -0.49 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THBS4]] | B | THBS4 activity raises ZSCAN30's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 2.24× lower at baseline in the lines without THBS4 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |
| [[THBS4]] | B | THBS4 activity strengthens ZSCAN30's drug response | lines that do not express THBS4 (6) vs lines expressing it (42) | the lines without THBS4 respond 0.53× as strongly (z diff +2.15); strongest at Digitoxin 5 µM: 0.63x vs 0.26x (z diff +5.2) | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ZNF518B]] | B | ZNF518B activity raises ZSCAN30's level | lines that do not express ZNF518B (16) vs lines expressing it (34) | 1.58× lower at baseline in the lines without ZNF518B | 0.062 | ⚠ within organs, on part of the lines; also absent: EHD3, KCNG1, TUB |
| [[ZNF655]] | B | ZNF655 activity raises ZSCAN30's level | lines that do not express ZNF655 (7) vs lines expressing it (43) | 1.95× lower at baseline in the lines without ZNF655 | 0.077 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SRSF12 |
| [[ZNF382]] | B | ZNF382 activity raises ZSCAN30's level | lines that do not express ZNF382 (18) vs lines expressing it (32) | 1.53× lower at baseline in the lines without ZNF382 | 0.079 | ⚠ within organs, on part of the lines; also absent: AFF3, DZIP1, MMP16 |
| [[ZNF528]] | B | ZNF528 activity raises ZSCAN30's level | lines that do not express ZNF528 (21) vs lines expressing it (29) | 1.50× lower at baseline in the lines without ZNF528 | 0.080 | ⚠ within organs, on part of the lines; also absent: ZNF528-AS1, ZNF625, ZNF880 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.694). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (2.6, 15.7); signed map (20.6, -21.6). **Vector** length 78.8, 17.6% of its response variance represented; |z| ≥ 3 in 1,101 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +2.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | -0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +5.0 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -4.0 | -5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -3.9 | -5.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -3.7 | -5.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -12.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.7 | -13.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -3.4 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | -1.3 | -1.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and SCAN domain containing 30 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.2 — chr18:35,251,058-35,290,245 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF917; previously ZNF397OS |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86W11](https://www.uniprot.org/uniprotkb/Q86W11) (Zinc finger and SCAN domain-containing protein 30):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [100101467](https://www.ncbi.nlm.nih.gov/gene/100101467):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:33517](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33517) · Entrez [100101467](https://www.ncbi.nlm.nih.gov/gene/100101467) · UniProt [Q86W11](https://www.uniprot.org/uniprotkb/Q86W11) · Ensembl [ENSG00000186814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186814)

## Data

Gene col 11857: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11857); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11857, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11857]; `tensor/DDL_lfc|DDL_z.npy` [11857]; `embed/gene_vectors.npy` [11857]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11857 or target_col == 11857). Every well: [[ZSCAN30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSCAN30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
