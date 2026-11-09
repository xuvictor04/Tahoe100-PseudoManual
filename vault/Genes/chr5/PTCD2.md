---
symbol: "PTCD2"
type: "gene"
col: 558
ensembl_id: "ENSG00000049883"
name: "pentatricopeptide repeat domain 2"
location: "5q13.2"
module: 1
arm: "+"
pooled_cpm: 13.96
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 17
n_dd_up_clean: 18
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PTCD2

*pentatricopeptide repeat domain 2* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.27× (z +11.2, q 1e-26, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.276× (z -17.6, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FANCF]] (+0.71, fdr 7e-06), [[DPH5]] (+0.71, fdr 7e-06), [[N6AMT1]] (+0.70, fdr 7e-06); moves opposite to [[CCDC65]] (-0.58, fdr 5e-05), [[TESK2]] (-0.58, fdr 2e-05), [[TPTEP2-CSNK1E]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RHBDL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 558.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.27×** | +11.2 | 1e-26 | 44/48 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.21×** | +10.9 | 4e-25 | 41/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.13×** | +10.4 | 4e-23 | 38/47 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.65×** | +6.8 | 1e-09 | 34/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.63×** | +6.7 | 2e-09 | 31/48 (LoVo, A-427, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +5.8 | 6e-07 | 23/48 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +5.6 | 2e-06 | 24/46 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +5.1 | 2e-05 | 19/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.30×** | +5.1 | 2e-05 | 18/48 (KATO III, SW 900, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +4.6 | 2e-04 | 18/39 (SW48, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +4.3 | 8e-04 | 14/25 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.76×** | +4.0 | 0.003 | 16/48 (LOX-IMVI, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.006 | 10/47 (RKO, PANC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.009 | 15/48 (NCI-H1573, RKO, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.37×** | +3.5 | 0.017 | 9/47 (NCI-H1573, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.017 | 18/46 (LoVo, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.025 | 16/47 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.036 | 14/46 (SW 900, SW480, …) | all doses, flat | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 558.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.276×** | -17.6 | 0e+00 | 45/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.305×** | -16.3 | 0e+00 | 44/46 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.407×** | -12.3 | 1e-32 | 38/47 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.426×** | -11.7 | 2e-29 | 41/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.309×** | -8.4 | 4e-15 | 37/48 (HOP62, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.612×** | -6.5 | 9e-09 | 26/42 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.436×** | -5.9 | 2e-07 | 22/45 (MIA PaCa-2, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.756×** | -5.4 | 4e-06 | 22/47 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.624×** | -5.2 | 1e-05 | 23/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.795×** | -4.4 | 5e-04 | 20/48 (CHP-212, RKO, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.584×** | -3.9 | 0.006 | 16/45 (SW480, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.762×** | -3.7 | 0.009 | 17/47 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.766×** | -3.7 | 0.011 | 13/48 (LoVo, AN3 CA, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.788×** | -3.3 | 0.045 | 12/48 (NCI-H2030, SNU-1, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.787×** | -3.2 | 0.060 | 9/48 (HepG2/C3A, SW 900, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.795×** | -3.1 | 0.060 | 19/47 (SHP-77, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 558. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 18.4 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0945× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.123× (z -18.3) |
| [[SNU-1 (line)]] | wt | 15.9 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0534× (z -11.8) |
| [[SNU-423 (line)]] | alt | 16.4 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0587× (z -16.8) |
| [[SW480 (line)]] | alt | 18.3 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.164× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.167× (z -13.9) |
| [[A-427 (line)]] | wt | 20.4 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.216× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0887× (z -8.7) |
| [[COLO 205 (line)]] | alt | 11.9 | 0 | 3 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.106× (z -9.4) |
| [[HOP62 (line)]] | alt | 15.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.166× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 19.5 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.107× (z -14.3) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 6.50 | 0 | 2 | — | [[Roxadustat (drug)]] 0.5 µM 0.0651× (z -9.1) |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.121× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Bimiralisib (drug)]] 0.5 µM 0.0870× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 24.1 | 0 | 2 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0332× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 19.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -13.7) |
| [[A-172 (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -9.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0710× (z -11.7) ⚠ cell-cycle shift, explains ~57% of this change |
| [[CHP-212 (line)]] | wt | 20.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0686× (z -8.7) |
| [[J82 (line)]] | alt | 13.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.166× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 13.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 9.74 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 8.95 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.221× (z -8.9) |
| [[SHP-77 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.163× (z -9.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 7.83 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -8.5) ⚠ cell-cycle shift, explains ~83% of this change |
| [[SW1417 (line)]] | alt | 9.53 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.170× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 558), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANCF]] | +0.71 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[DPH5]] | +0.71 | +0.75 / +0.73 | both halves | 7e-06 | STRING 443 |
| [[N6AMT1]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[PWP1]] | +0.68 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[NUDT12]] | +0.68 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[PRMT5]] | +0.68 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[TRUB1]] | +0.66 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[DLAT]] | +0.66 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[RPUSD3]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 | STRING 408 |
| [[IMPACT]] | +0.64 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[TTC5]] | +0.63 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[CCDC113]] | +0.63 | +0.60 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC65]] | -0.58 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[TESK2]] | -0.58 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.57 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[SERF2]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[RABGEF1]] | -0.55 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[PDE6D]] | -0.54 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[STX5]] | -0.54 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[PP2D1]] | -0.54 | -0.38 / -0.50 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHBDL3]] | B | RHBDL3 activity raises PTCD2's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 1.52× lower at baseline in the lines without RHBDL3 | 0.015 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.3, 1.1); signed map (0.3, -38.5). **Vector** length 64.6, 11.5% of its response variance represented; |z| ≥ 3 in 1,102 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial mRNA modification* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.4 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +6.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | +5.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +6.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -0.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -3.6 | +1.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -0.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | pentatricopeptide repeat domain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:72,320,367-72,368,395 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12598 |
| Gene groups (HGNC) | Pentatricopeptide repeat containing |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WV60](https://www.uniprot.org/uniprotkb/Q8WV60) (Pentatricopeptide repeat-containing protein 2, mitochondrial):

> Involved in mitochondrial RNA maturation and mitochondrial respiratory chain function.

**Summary**, from NCBI Gene [79810](https://www.ncbi.nlm.nih.gov/gene/79810):

> Enables RNA binding activity. Predicted to be involved in mitochondrion organization and regulation of mRNA processing. Predicted to act upstream of or within several processes, including liver development; muscle cell development; and ventricular cardiac muscle tissue morphogenesis. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25734](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25734) · Entrez [79810](https://www.ncbi.nlm.nih.gov/gene/79810) · UniProt [Q8WV60](https://www.uniprot.org/uniprotkb/Q8WV60) · Ensembl [ENSG00000049883](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000049883)

## Data

Gene col 558: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 558); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 558, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 558]; `tensor/DDL_lfc|DDL_z.npy` [558]; `embed/gene_vectors.npy` [558]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 558 or target_col == 558). Every well: [[PTCD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTCD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
