---
symbol: "DCTN2"
type: "gene"
col: 10580
ensembl_id: "ENSG00000175203"
name: "dynactin subunit 2"
location: "12q13.3"
module: 64
arm: "+"
pooled_cpm: 50.79
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 5
n_dd_up_clean: 20
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# DCTN2

*dynactin subunit 2* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.32× (z +16.5, q 0e+00, up in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.70× (z +10.4, q 7e-23, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.691× (z -7.3, q 2e-10, down in 30 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.833× (z -5.1, q 1e-04, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLII]] (+0.67, fdr 7e-06), [[CLIP1]] (+0.64, fdr 7e-06), [[ANXA7]] (+0.63, fdr 7e-06); moves opposite to [[TLE6]] (-0.52, fdr 3e-05), [[PPAT]] (-0.52, fdr 3e-05), [[MNX1]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10580.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.32×** | +16.5 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.33×** | +15.9 | 0e+00 | 38/41 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.70×** | +10.4 | 7e-23 | 44/48 (NCI-H460, COLO 205, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +8.2 | 2e-14 | 39/48 (A-427, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +8.0 | 1e-13 | 29/44 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +7.8 | 5e-13 | 36/48 (A-427, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.36×** | +6.0 | 2e-07 | 30/47 (RKO, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.35×** | +5.7 | 9e-07 | 35/47 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +5.6 | 1e-06 | 28/48 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +5.2 | 1e-05 | 29/48 (A498, A-427, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +5.2 | 1e-05 | 24/48 (LS 180, HT-29, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **1.29×** | +5.0 | 3e-05 | 27/47 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **1.43×** | +5.0 | 3e-05 | 31/48 (RKO, LS 180, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.27×** | +4.6 | 2e-04 | 23/47 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.25×** | +4.4 | 4e-04 | 23/48 (NCI-H1573, A-427, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.36×** | +4.3 | 7e-04 | 22/47 (NCI-H460, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +4.0 | 0.002 | 20/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.007 | 21/47 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.008 | 11/48 (NCI-H460, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10580.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.691×** | -7.3 | 2e-10 | 30/47 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.833×** | -5.1 | 1e-04 | 28/48 (SW480, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.847× | -4.6 | 8e-04 | 21/48 (RPMI-7951, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.795×** | -4.5 | 0.001 | 21/48 (A-172, NCI-H1792, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.641×** | -4.2 | 0.003 | 22/49 (LOX-IMVI, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.832×** | -3.6 | 0.030 | 19/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.852× | -3.1 | 0.13 | 11/48 (SNU-1, J82, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10580. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 55.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.44× (z +12.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 60.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +11.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 48.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +11.9) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 40.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.337× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~4% of this change |
| [[CFPAC-1 (line)]] | alt | 36.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 38.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +12.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 36.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +10.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 49.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +9.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 27.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 41.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 68.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 40.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.67× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 49.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +12.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 48.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +14.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 48.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 54.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +10.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 50.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CHP-212 (line)]] | wt | 37.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.109× (z -9.5) ⚠ transcription drop; cell-cycle shift, explains ~22% of this change |
| [[HS-578T (line)]] | alt | 49.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +10.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 53.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 217 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -13.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 64.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.36× (z +9.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 62.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +9.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.408× (z -9.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 31.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.31× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 55.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0722× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 41.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 81.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 69.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10580), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLII]] | +0.67 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[CLIP1]] | +0.64 | +0.61 / +0.68 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 785 |
| [[ANXA7]] | +0.63 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[CCSER2]] | +0.59 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[TCTA]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[PSMD4]] | +0.57 | +0.61 / +0.48 | both halves | 2e-05 | STRING 420 |
| [[MAP7D1]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PSMD6]] | +0.56 | +0.64 / +0.43 | both halves | 3e-05 | pathway: G2/M Transition |
| [[ACTR1A]] | +0.55 | +0.45 / +0.60 | both halves | 3e-05 | same gene group; pathway: AURKA Activation by TPX2; STRING 999 |
| [[EIF3G]] | +0.55 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[VPS29]] | +0.54 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[EXOC5]] | +0.54 | +0.49 / +0.50 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLE6]] | -0.52 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[PPAT]] | -0.52 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[MNX1]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[CGREF1]] | -0.49 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[IGFBP2]] | -0.47 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[CLEC11A]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[PTMA]] | -0.47 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[SFXN1]] | -0.47 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ANKRD13D]] | -0.47 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[KDM4A-AS1]] | -0.46 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[NUP62CL]] | -0.46 | -0.37 / -0.47 | both halves | 7e-05 |  |
| [[CENPV]] | -0.46 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DCTN2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.435). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-5.9, -1.8); signed map (-0.2, -10.3). **Vector** length 108, 28.4% of its response variance represented; |z| ≥ 3 in 957 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.6 | +10.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.9 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.5 | +8.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +6.5 | +5.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +5.5 | +6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.5 | +5.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.2 | +4.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.9 | +4.6 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.5 | -7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.2 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -5.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.6 | -4.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.7 | -3.1 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.1 | +0.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.8 | +0.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Vilanterol (drug)]] 5 µM |  | -1.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | dynactin subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:57,529,633-57,547,224 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RBP50, DCTN-50 |
| Gene groups (HGNC) | Dynactin subunits |
| Reactome | 34 pathways, smallest: COPI-independent Golgi-to-ER retrograde traffic; HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; Loss of Nlp from mitotic centrosomes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13561](https://www.uniprot.org/uniprotkb/Q13561) (Dynactin subunit 2):

> Part of the dynactin complex that activates the molecular motor dynein for ultra-processive transport along microtubules. In the dynactin soulder domain, binds the ACTR1A filament and acts as a molecular ruler to determine the length (By similarity). Modulates cytoplasmic dynein binding to an organelle, and plays a role in prometaphase chromosome alignment and spindle organization during mitosis. Involved in anchoring microtubules to centrosomes. May play a role in synapse formation during …

**Summary**, from NCBI Gene [10540](https://www.ncbi.nlm.nih.gov/gene/10540):

> This gene encodes a 50-kD subunit of dynactin, a macromolecular complex consisting of 10-11 subunits ranging in size from 22 to 150 kD. Dynactin binds to both microtubules and cytoplasmic dynein. It is involved in a diverse array of cellular functions, including ER-to-Golgi transport, the centripetal movement of lysosomes and endosomes, spindle formation, chromosome movement, nuclear positioning, and axonogenesis. This subunit is present in 4-5 copies per dynactin molecule. It contains three …

**Accessions** — [HGNC:2712](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2712) · Entrez [10540](https://www.ncbi.nlm.nih.gov/gene/10540) · UniProt [Q13561](https://www.uniprot.org/uniprotkb/Q13561) · Ensembl [ENSG00000175203](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175203)

## Data

Gene col 10580: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10580); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10580, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10580]; `tensor/DDL_lfc|DDL_z.npy` [10580]; `embed/gene_vectors.npy` [10580]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10580 or target_col == 10580). Every well: [[DCTN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCTN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
