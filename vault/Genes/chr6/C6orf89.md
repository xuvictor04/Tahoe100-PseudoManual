---
symbol: "C6orf89"
type: "gene"
col: 12636
ensembl_id: "ENSG00000198663"
name: "chromosome 6 open reading frame 89"
location: "6p21.2"
module: 209
arm: "+"
pooled_cpm: 48.55
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/209"]
generated_by: "tahoemap"
---

# C6orf89

*chromosome 6 open reading frame 89* — 6p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.20× (z +18.3, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.665× (z -10.2, q 8e-22, down in 35 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.711× (z -8.9, q 2e-16, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS16]] (+0.60, fdr 1e-05), [[KLHL12]] (+0.59, fdr 7e-06), [[RNF141]] (+0.58, fdr 1e-05); moves opposite to [[CSPG5]] (-0.55, fdr 2e-05), [[SFXN5]] (-0.54, fdr 1e-05), [[FERMT3]] (-0.54, fdr 3e-05).
> It is in [[Module 209]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12636.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.20×** | +18.3 | 0e+00 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.96×** | +17.7 | 0e+00 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +13.7 | 1e-40 | 41/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +8.2 | 3e-14 | 31/47 (NCI-H2030, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +6.1 | 2e-07 | 24/48 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +5.6 | 2e-06 | 23/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +5.6 | 2e-06 | 12/48 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +5.2 | 2e-05 | 20/40 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +5.1 | 2e-05 | 20/48 (NCI-H23, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.15× | +5.1 | 2e-05 | 15/48 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.21×** | +5.0 | 3e-05 | 20/48 (LoVo, NCI-H23, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +4.9 | 5e-05 | 15/48 (SW480, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +4.7 | 1e-04 | 18/48 (PANC-1, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.19× | +4.6 | 1e-04 | 20/48 (HEC-1-A, BT-474, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +4.4 | 4e-04 | 14/48 (SW1417, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Alpelisib (drug)]] 5 µM |  | **1.36×** | +4.2 | 0.001 | 10/47 (MIA PaCa-2, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 1.12× | +4.1 | 0.001 | 8/48 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.17× | +4.0 | 0.002 | 12/48 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.16× | +3.9 | 0.002 | 14/48 (NCI-H1573, A-427, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.8 | 0.003 | 12/48 (A-427, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12636.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.665×** | -10.2 | 8e-22 | 35/47 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.711×** | -8.9 | 2e-16 | 32/48 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.715×** | -8.3 | 2e-14 | 31/48 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.701×** | -8.2 | 3e-14 | 33/48 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.580×** | -7.4 | 2e-11 | 29/48 (NCI-H460, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.584×** | -7.3 | 3e-11 | 27/44 (Panc 03.27, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.820×** | -5.2 | 2e-05 | 25/48 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.685×** | -5.1 | 2e-05 | 23/49 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.763×** | -5.0 | 3e-05 | 20/48 (SNU-423, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.730×** | -4.2 | 0.001 | 20/48 (RPMI-7951, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | 0.858× | -4.0 | 0.003 | 17/48 (NCI-H460, hTERT-HPNE, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.862× | -3.7 | 0.012 | 16/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.872× | -3.4 | 0.026 | 13/48 (C-33 A, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 0.878× | -3.3 | 0.042 | 16/48 (NCI-H1792, H4, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12636. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 66.8 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.33× (z +12.3) | [[Ixazomib citrate (drug)]] 5 µM 0.572× (z -9.2) |
| [[A-172 (line)]] | wt | 41.1 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.46× (z +11.9) | — |
| [[A498 (line)]] | wt | 25.9 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.63× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 41.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.79× (z +11.1) | — |
| [[NCI-H23 (line)]] | alt | 64.3 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.15× (z +9.2) | — |
| [[SW480 (line)]] | alt | 51.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.63× (z +14.1) | — |
| [[HOP62 (line)]] | alt | 58.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.46× (z +9.3) | — |
| [[J82 (line)]] | alt | 43.6 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.398× (z -10.1) |
| [[LoVo (line)]] | wt | 35.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.85× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 41.8 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +8.8) ⚠ cell-cycle shift, explains ~13% of this change | — |
| [[A-427 (line)]] | wt | 33.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.272× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 54.9 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.181× (z -8.6) |
| [[H4 (line)]] | wt | 40.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.276× (z -8.5) ⚠ toxic |
| [[HCT15 (line)]] | alt | 68.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 45.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.00× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 46.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.395× (z -9.4) ⚠ toxic |
| [[LS 180 (line)]] | wt | 42.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 39.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.454× (z -9.8) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 95.0 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.259× (z -8.7) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 80.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -12.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12636), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS16]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[KLHL12]] | +0.59 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[RNF141]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[SENP2]] | +0.57 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[MRPS14]] | +0.54 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[MCRIP1]] | +0.54 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[FAM149B1]] | +0.53 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[TMEM175]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[TRAPPC6B]] | +0.52 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[TMEM254]] | +0.51 | +0.60 / +0.35 | both halves | 1e-04 |  |
| [[THAP6]] | +0.51 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[COA5]] | +0.51 | +0.61 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSPG5]] | -0.55 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[SFXN5]] | -0.54 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[FERMT3]] | -0.54 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[HSPH1]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[GRAMD2A]] | -0.52 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[HSPE1]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[BEND3]] | -0.51 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[PHTF1]] | -0.50 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[MTNR1A]] | -0.50 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[CCT6A]] | -0.49 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[CHADL]] | -0.49 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[KCNQ4]] | -0.49 | -0.45 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises C6orf89's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 209]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-26.9, 21.1); signed map (-14.3, -15.1). **Vector** length 87.9, 19.4% of its response variance represented; |z| ≥ 3 in 1,031 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +18.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +8.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | -0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +4.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.0 | +5.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -5.4 | -8.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.4 | -8.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.3 | -10.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -5.3 | -7.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.4 | -5.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -7.4 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 6 open reading frame 89 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2 — chr6:36,871,870-36,928,964 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25357, BRAP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UWU4](https://www.uniprot.org/uniprotkb/Q6UWU4) (Bombesin receptor-activated protein C6orf89):

> Exhibits histone deacetylase (HDAC) enhancer properties. May play a role in cell cycle progression and wound repair of bronchial epithelial cells.

**Summary**, from NCBI Gene [221477](https://www.ncbi.nlm.nih.gov/gene/221477):

> Involved in several processes, including epithelial cell proliferation; positive regulation of cell cycle; and wound healing. Located in several cellular components, including Golgi membrane; midbody; and nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21114](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21114) · Entrez [221477](https://www.ncbi.nlm.nih.gov/gene/221477) · UniProt [Q6UWU4](https://www.uniprot.org/uniprotkb/Q6UWU4) · Ensembl [ENSG00000198663](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198663)

## Data

Gene col 12636: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12636); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12636, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12636]; `tensor/DDL_lfc|DDL_z.npy` [12636]; `embed/gene_vectors.npy` [12636]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12636 or target_col == 12636). Every well: [[C6orf89 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C6orf89.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
