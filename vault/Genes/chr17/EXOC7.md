---
symbol: "EXOC7"
type: "gene"
col: 11289
ensembl_id: "ENSG00000182473"
name: "exocyst complex component 7"
location: "17q25.1"
module: 215
arm: "+"
pooled_cpm: 38.1
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/215"]
generated_by: "tahoemap"
---

# EXOC7

*exocyst complex component 7* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.27× (z +14.8, q 0e+00, up in 34 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.40× (z +6.3, q 5e-08, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.685× (z -10.0, q 7e-21, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMC3]] (+0.63, fdr 7e-06), [[TRIP12]] (+0.63, fdr 1e-05), [[ATXN1L]] (+0.63, fdr 2e-05); moves opposite to [[C15orf61]] (-0.65, fdr 1e-05, ⚠ C15orf61 in the vector space only through flagged drug-doses), [[LSM2]] (-0.63, fdr 1e-05), [[RPL22L1]] (-0.57, fdr 2e-04, ⚠ RPL22L1 in the vector space only through flagged drug-doses), [[SAC3D1]] (-0.56, fdr 2e-05), [[DBF4]] (-0.55, fdr 1e-05).
> It is in [[Module 215]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11289.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +14.8 | 0e+00 | 34/40 (SHP-77, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +12.4 | 7e-33 | 42/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +6.3 | 5e-08 | 27/48 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.1 | 2e-07 | 27/48 (SW1417, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.40×** | +5.8 | 6e-07 | 24/43 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.38×** | +5.7 | 1e-06 | 26/48 (H4, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +5.4 | 4e-06 | 30/48 (HEC-1-A, HOP62, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.8 | 1e-04 | 25/48 (SW 900, J82, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.20× | +4.7 | 2e-04 | 20/48 (LoVo, HOP62, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.009 | 19/47 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.20×** | +3.4 | 0.030 | 17/48 (BT-474, SW48, …) | inconsistent across doses |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.19× | +3.3 | 0.044 | 5/48 (A498, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.044 | 5/48 (hTERT-HPNE, HEC-1-A, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | 1.36× | +3.0 | 0.11 | 6/46 (HCT15, LoVo, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11289.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.685×** | -10.0 | 7e-21 | 44/48 (Panc 03.27, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.729×** | -8.4 | 2e-14 | 30/47 (J82, HEC-1-A, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.672×** | -7.5 | 1e-11 | 33/48 (SW480, SW 1088, …) | all doses, flat | cell-cycle shift (explains ~6% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.696×** | -6.8 | 1e-09 | 31/48 (NCI-H1792, HT-29, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.699×** | -6.7 | 2e-09 | 37/48 (HOP62, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.609×** | -4.9 | 9e-05 | 23/48 (NCI-H2347, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.773×** | -4.8 | 9e-05 | 22/47 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.611×** | -4.8 | 9e-05 | 27/49 (A-427, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.777×** | -4.6 | 3e-04 | 23/47 (COLO 205, SNU-1, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.790×** | -4.4 | 5e-04 | 22/47 (RKO, SW1417, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.791×** | -4.4 | 5e-04 | 19/48 (LS 180, PANC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.804×** | -4.1 | 0.002 | 20/48 (COLO 205, RPMI-7951, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.809×** | -4.0 | 0.003 | 19/48 (NCI-H23, SW1417, …) | all doses, flat | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.706×** | -3.4 | 0.025 | 15/48 (HT-29, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.842× | -3.2 | 0.044 | 14/48 (J82, KATO III, …) | all doses, stronger at high dose |  |
| [[Silodosin (drug)]] 5 µM |  | 0.844× | -3.1 | 0.067 | 13/47 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.891× | -3.1 | 0.067 | 10/48 (NCI-H661, COLO 205, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.848× | -3.0 | 0.082 | 17/47 (A498, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11289. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 54.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.80× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -10.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[J82 (line)]] | alt | 28.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.52× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -10.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A498 (line)]] | wt | 36.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +11.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 37.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.93× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -9.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[PANC-1 (line)]] | alt | 43.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +11.3) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 37.1 | 0 | 1 | — | [[Filgotinib (drug)]] 0.5 µM 0.0610× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 36.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -10.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[CHP-212 (line)]] | wt | 67.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -9.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 52.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.217× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[LoVo (line)]] | wt | 25.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -10.4) ⚠ cell-cycle shift, explains ~45% of this change |
| [[NCI-H2030 (line)]] | alt | 33.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 33.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.398× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[Panc 03.27 (line)]] | alt | 50.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -9.0) ⚠ cell-cycle shift, explains ~45% of this change |
| [[RPMI-7951 (line)]] | alt | 33.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.207× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 43.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.36× (z +11.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 38.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 39.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 42.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11289), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMC3]] | +0.63 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[TRIP12]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[ATXN1L]] | +0.63 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[DPP3]] | +0.62 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[PEX19]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ALKBH6]] | +0.62 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[ERVK13-1]] | +0.61 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[BECN1]] | +0.61 | +0.45 / +0.59 | both halves | 3e-05 | same gene group |
| [[DBNL]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 | same gene group |
| [[PSMC5]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[C17orf80]] | +0.60 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[HARS1]] | +0.59 | +0.66 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C15orf61]] ⚠ | -0.65 | -0.53 / -0.59 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LSM2]] | -0.63 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[RPL22L1]] ⚠ | -0.57 | -0.30 / -0.57 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[COX5A]] ⚠ | -0.56 | -0.45 / -0.46 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SAC3D1]] | -0.56 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[DBF4]] | -0.55 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[RNF145]] | -0.55 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[KBTBD3]] | -0.55 | -0.43 / -0.56 | both halves | 4e-05 |  |
| [[SAP30]] | -0.54 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[SYBU]] | -0.54 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[DDIT4]] | -0.54 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[RAC3]] | -0.53 | -0.29 / -0.48 | both halves | 3e-04 |  |
| [[LCORL]] | -0.53 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[ATP5MC2]] | -0.53 | -0.39 / -0.47 | both halves | 5e-05 | pathway: Organelle biogenesis and maintenance |
| [[ANAPC11]] | -0.53 | -0.33 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EXOC7's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers EXOC7's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers EXOC7's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 215]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.0, -9.4); signed map (-7.6, -36.2). **Vector** length 105, 25.5% of its response variance represented; |z| ≥ 3 in 915 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.8 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.6 | +5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.2 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +12.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.4 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.6 | -10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.7 | -6.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.9 | -7.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.8 | -3.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | -3.4 | -4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | exocyst complex component 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:76,081,016-76,121,576 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EXO70, KIAA1067, YJL085W, Exo70p, BLOM4 |
| Gene groups (HGNC) | Exocyst complex; MicroRNA protein coding host genes |
| Reactome | 10 pathways, smallest: VxPx cargo-targeting to cilium; Insulin processing; Peptide hormone metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPT5](https://www.uniprot.org/uniprotkb/Q9UPT5) (Exocyst complex component 7):

> Component of the exocyst complex involved in the docking of exocytic vesicles with fusion sites on the plasma membrane. In adipocytes, plays a crucial role in targeting SLC2A4 vesicle to the plasma membrane in response to insulin, perhaps directing the vesicle to the precise site of fusion (By similarity). It is required for neuron survival and plays an essential role in cortical development (By similarity).

**Summary**, from NCBI Gene [23265](https://www.ncbi.nlm.nih.gov/gene/23265):

> The protein encoded by this gene is a component of the exocyst complex. The exocyst complex plays a critical role in vesicular trafficking and the secretory pathway by targeting post-Golgi vesicles to the plasma membrane. The encoded protein is required for assembly of the exocyst complex and docking of the complex to the plasma membrane. The encoded protein may also play a role in pre-mRNA splicing through interactions with pre-mRNA-processing factor 19. Alternatively spliced transcript …

**Accessions** — [HGNC:23214](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23214) · Entrez [23265](https://www.ncbi.nlm.nih.gov/gene/23265) · UniProt [Q9UPT5](https://www.uniprot.org/uniprotkb/Q9UPT5) · Ensembl [ENSG00000182473](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182473)

## Data

Gene col 11289: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11289); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11289, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11289]; `tensor/DDL_lfc|DDL_z.npy` [11289]; `embed/gene_vectors.npy` [11289]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11289 or target_col == 11289). Every well: [[EXOC7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOC7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
