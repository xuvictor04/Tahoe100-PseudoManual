---
symbol: "TMEM184B"
type: "gene"
col: 12678
ensembl_id: "ENSG00000198792"
name: "transmembrane protein 184B"
location: "22q13.1"
module: 136
arm: "+"
pooled_cpm: 63.27
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 21
n_dd_up_clean: 17
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# TMEM184B

*transmembrane protein 184B* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.77× (z +12.4, q 3e-32, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.662× (z -12.6, q 1e-33, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO9B]] (+0.74, fdr 7e-06), [[DNAJC5]] (+0.71, fdr 7e-06), [[FAM131A]] (+0.71, fdr 7e-06); moves opposite to [[BCLAF1]] (-0.69, fdr 1e-05), [[U2SURP]] (-0.68, fdr 1e-05), [[FUBP1]] (-0.67, fdr 3e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC1A1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PITPNM1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12678.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.77×** | +12.4 | 3e-32 | 44/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.70×** | +11.4 | 8e-28 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +11.4 | 8e-28 | 45/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +7.7 | 1e-12 | 30/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.38×** | +6.7 | 2e-09 | 35/47 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.33×** | +6.1 | 1e-07 | 28/47 (NCI-H23, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +5.6 | 2e-06 | 23/49 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +5.1 | 3e-05 | 24/49 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.25×** | +4.9 | 6e-05 | 24/48 (A549, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +4.8 | 1e-04 | 23/48 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.24×** | +4.7 | 2e-04 | 21/48 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.23×** | +4.4 | 4e-04 | 21/47 (COLO 205, LoVo, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.003 | 17/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.20× | +3.9 | 0.005 | 20/48 (LoVo, PANC-1, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.006 | 18/48 (SW480, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.014 | 7/48 (CFPAC-1, A549, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.028 | 12/48 (PANC-1, NCI-H1792, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12678.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.662×** | -12.6 | 1e-33 | 36/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.619×** | -10.0 | 6e-21 | 36/48 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.660×** | -9.0 | 4e-17 | 32/48 (NCI-H2030, SW 1088, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.470×** | -8.5 | 2e-15 | 42/49 (NCI-H2030, H4, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.687×** | -8.1 | 5e-14 | 30/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.692×** | -8.0 | 2e-13 | 35/48 (C32, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.706×** | -7.5 | 4e-12 | 35/48 (KATO III, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.698×** | -7.5 | 5e-12 | 30/47 (A-172, LoVo, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.788×** | -7.3 | 2e-11 | 29/48 (KATO III, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.745×** | -6.1 | 5e-08 | 24/42 (NCI-H1573, HT-29, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.705×** | -6.1 | 6e-08 | 25/45 (A-427, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.612×** | -5.5 | 1e-06 | 30/47 (SNU-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.789×** | -5.1 | 1e-05 | 25/49 (RKO, LS 180, …) | all doses, flat | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.796×** | -5.0 | 3e-05 | 25/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.803×** | -4.8 | 8e-05 | 24/48 (NCI-H2030, H4, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.812×** | -4.5 | 2e-04 | 23/48 (Hs 766T, AN3 CA, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.809×** | -4.4 | 3e-04 | 22/48 (NCI-H2030, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.783×** | -4.3 | 5e-04 | 20/47 (H4, J82, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.880× | -3.9 | 0.002 | 16/48 (CHP-212, Hs 766T, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.849× | -3.4 | 0.017 | 16/49 (SW 1271, AsPC-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12678. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 80.0 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.465× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 77.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -14.3) |
| [[SW 1088 (line)]] | alt | 127 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0900× (z -9.5) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Decitabine (drug)]] 0.5 µM 0.121× (z -8.6) |
| [[SW480 (line)]] | alt | 42.7 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.12× (z +13.5) | [[Digitoxin (drug)]] 0.5 µM 0.484× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 101 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0903× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.376× (z -11.4) |
| [[PANC-1 (line)]] | alt | 32.5 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.28× (z +10.8) | — |
| [[A-172 (line)]] | wt | 69.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -15.7) |
| [[A498 (line)]] | wt | 85.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -14.8) |
| [[AsPC-1 (line)]] | alt | 92.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -10.7) |
| [[HT-29 (line)]] | alt | 54.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.436× (z -11.2) |
| [[LoVo (line)]] | wt | 65.2 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.423× (z -9.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.588× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -9.3) |
| [[SNU-1 (line)]] | wt | 67.7 | 0 | 2 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0573× (z -11.3) |
| [[SW 900 (line)]] | alt | 70.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -14.3) |
| [[A-427 (line)]] | wt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -11.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 48.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.26× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 76.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -9.5) |
| [[C32 (line)]] | wt | 88.9 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.155× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 60.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.19× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 80.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -13.1) |
| [[Hs 766T (line)]] | wt | 141 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -10.8) |
| [[HS-578T (line)]] | alt | 97.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.600× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 104 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -11.5) |
| [[J82 (line)]] | alt | 56.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 35.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -10.1) |
| [[LS 180 (line)]] | wt | 55.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[NCI-H1792 (line)]] | alt | 69.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 44.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 68.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -14.1) |
| [[Panc 03.27 (line)]] | alt | 73.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -8.5) |
| [[RKO (line)]] | wt | 52.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[SHP-77 (line)]] | alt | 31.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.26× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 59.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -9.1) |
| [[SW1417 (line)]] | alt | 38.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.55× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 67.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 69.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12678), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO9B]] | +0.74 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[DNAJC5]] | +0.71 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[FAM131A]] | +0.71 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[TMEM104]] | +0.71 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[CDR2L]] | +0.68 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[CSNK1E]] | +0.68 | +0.67 / +0.59 | both halves | 7e-06 | ⚠ same locus (17.7 kb, same strand: neighbours can correlate without regulation) |
| [[SLC35E4]] | +0.68 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[CARD19]] | +0.68 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[ARID3B]] | +0.67 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[TPST2]] | +0.67 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[GNAI2]] | +0.67 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[TMED9]] | +0.67 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[MPG]] | +0.67 | +0.74 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCLAF1]] | -0.69 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[U2SURP]] | -0.68 | -0.57 / -0.68 | both halves | 1e-05 |  |
| [[FUBP1]] | -0.67 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[GTF3C6]] | -0.66 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[AFG1L]] | -0.66 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[USP24]] | -0.65 | -0.38 / -0.63 | both halves | 6e-05 |  |
| [[EIF1B-AS1]] | -0.64 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[HNRNPU]] | -0.64 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[DECR1]] | -0.63 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[MRRF]] | -0.63 | -0.57 / -0.60 | both halves | 9e-06 |  |
| [[CC2D2A]] | -0.63 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[SUCLG2-DT]] | -0.63 | -0.61 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC1A1]] | B | SLC1A1 activity raises TMEM184B's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 1.58× lower at baseline in the lines without SLC1A1 | 0.007 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[CADM4]] | B | CADM4 activity raises TMEM184B's level | lines that do not express CADM4 (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without CADM4 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PITPNM1]] | C | TMEM184B's natural level strengthens PITPNM1's drug response | TMEM184B's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.61, reverse -0.23; direction not clear | 0.0995 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.812). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.3, 1.6); signed map (-24.2, 20.9). **Vector** length 131, 38.8% of its response variance represented; |z| ≥ 3 in 1,194 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +8.0 | +12.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.7 | +11.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.5 | +11.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.8 | +5.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.2 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +7.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.7 | +3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.5 | +3.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.2 | +2.0 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.9 | -7.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.7 | -10.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -9.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.9 | -4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.8 | -12.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.6 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -3.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.0 | -3.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 184B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:38,219,291-38,273,010 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HS5O6A, DKFZP586A1024, FM08, SLC51C2; previously C22orf5 |
| Gene groups (HGNC) | Solute carrier family 51 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y519](https://www.uniprot.org/uniprotkb/Q9Y519) (Transmembrane protein 184B):

> May activate the MAP kinase signaling pathway.

**Summary**, from NCBI Gene [25829](https://www.ncbi.nlm.nih.gov/gene/25829):

> Predicted to enable transmembrane transporter activity. Predicted to be involved in transmembrane transport. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1310](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1310) · Entrez [25829](https://www.ncbi.nlm.nih.gov/gene/25829) · UniProt [Q9Y519](https://www.uniprot.org/uniprotkb/Q9Y519) · Ensembl [ENSG00000198792](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198792)

## Data

Gene col 12678: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12678); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12678, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12678]; `tensor/DDL_lfc|DDL_z.npy` [12678]; `embed/gene_vectors.npy` [12678]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12678 or target_col == 12678). Every well: [[TMEM184B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM184B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
