---
symbol: "FHIP2A"
type: "gene"
col: 7535
ensembl_id: "ENSG00000151553"
name: "FHF complex subunit HOOK interacting protein 2A"
location: "10q25.3"
module: 190
arm: "+"
pooled_cpm: 43.52
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 25
n_dd_up_clean: 9
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/190"]
generated_by: "tahoemap"
---

# FHIP2A

*FHF complex subunit HOOK interacting protein 2A* — 10q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.59× (z +6.1, q 8e-07, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.335× (z -14.2, q 3e-43, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DRAM2]] (+0.73, fdr 7e-06), [[NAPB]] (+0.72, fdr 1e-05), [[TADA1]] (+0.68, fdr 7e-06); moves opposite to [[EGR1]] (-0.69, fdr 7e-06), [[IER2]] (-0.69, fdr 7e-06), [[EGR3]] (-0.66, fdr 7e-06).
> It is in [[Module 190]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF618]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7535.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +6.1 | 8e-07 | 36/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +5.6 | 5e-06 | 34/48 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +5.2 | 4e-05 | 26/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.09×** | +5.0 | 7e-05 | 28/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +4.6 | 6e-04 | 31/48 (CFPAC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.91×** | +4.4 | 0.001 | 24/43 (SNU-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.3 | 0.001 | 23/47 (LoVo, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.009 | 22/49 (CFPAC-1, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.056 | 17/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.056 | 17/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.60×** | +3.2 | 0.070 | 15/48 (NCI-H1573, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.094 | 22/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.096 | 18/48 (PANC-1, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7535.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.335×** | -14.2 | 3e-43 | 46/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.350×** | -13.6 | 6e-40 | 47/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.391×** | -12.2 | 5e-32 | 39/46 (C32, H4, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.443×** | -10.2 | 3e-22 | 37/42 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.513×** | -8.7 | 4e-16 | 39/48 (A498, A-172, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.679×** | -7.1 | 9e-11 | 38/48 (A-172, SW1417, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.684×** | -7.0 | 2e-10 | 28/48 (AsPC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.560×** | -7.0 | 2e-10 | 34/44 (SW 900, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.615×** | -6.3 | 2e-08 | 34/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.744×** | -5.4 | 3e-06 | 34/48 (A498, SW1417, …) | rises with dose |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.757×** | -3.6 | 0.015 | 23/48 (HEC-1-A, NCI-H1573, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.762×** | -3.5 | 0.019 | 23/48 (NCI-H2030, Panc 03.27, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **0.769×** | -3.4 | 0.028 | 20/48 (SW 900, SW1417, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.771×** | -3.4 | 0.028 | 17/48 (NCI-H2030, CFPAC-1, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.764×** | -3.4 | 0.029 | 20/49 (SW48, A-172, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.778×** | -3.3 | 0.039 | 18/48 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.782×** | -3.2 | 0.045 | 20/48 (NCI-H2030, SHP-77, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.841× | -3.2 | 0.045 | 16/48 (SHP-77, HOP62, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.784×** | -3.2 | 0.045 | 15/48 (HEC-1-A, SW1417, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.790×** | -3.1 | 0.059 | 14/47 (SW480, Panc 03.27, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.793×** | -3.0 | 0.063 | 17/48 (NCI-H1573, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7535. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 70.2 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -18.0) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.197× (z -16.7) |
| [[NCI-H460 (line)]] | wt | 58.0 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.229× (z -14.3) |
| [[A498 (line)]] | wt | 71.6 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.138× (z -16.7) |
| [[A549 (line)]] | wt | 63.3 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.193× (z -12.6) |
| [[AsPC-1 (line)]] | alt | 36.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -15.4) |
| [[NCI-H2030 (line)]] | alt | 96.1 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.239× (z -10.5) |
| [[SW1417 (line)]] | alt | 54.0 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.333× (z -9.1) |
| [[SW480 (line)]] | alt | 27.9 | 1 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.370× (z -9.0) |
| [[HOP62 (line)]] | alt | 26.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -10.3) |
| [[HS-578T (line)]] | alt | 43.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -15.3) |
| [[LoVo (line)]] | wt | 38.4 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 33.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.265× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 35.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.330× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 51.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.336× (z -10.4) |
| [[SNU-423 (line)]] | alt | 50.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -11.2) |
| [[C32 (line)]] | wt | 53.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0843× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[CHP-212 (line)]] | wt | 52.8 | 0 | 2 | — | [[Ritonavir (drug)]] 0.5 µM 0.0711× (z -11.0) |
| [[H4 (line)]] | wt | 49.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0638× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.203× (z -9.5) |
| [[J82 (line)]] | alt | 30.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 52.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 42.5 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.283× (z -9.2) |
| [[PANC-1 (line)]] | alt | 41.1 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.41× (z +13.2) | — |
| [[RKO (line)]] | wt | 48.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SNU-1 (line)]] | wt | 69.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.240× (z -9.7) |
| [[SW 900 (line)]] | alt | 54.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.298× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 34.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[LOX-IMVI (line)]] | wt | 43.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -10.1) |
| [[LS 180 (line)]] | wt | 43.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SW48 (line)]] | wt | 55.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7535), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRAM2]] | +0.73 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[NAPB]] | +0.72 | +0.86 / +0.54 | both halves | 1e-05 |  |
| [[TADA1]] | +0.68 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[SNX4]] | +0.68 | +0.80 / +0.58 | both halves | 8e-06 |  |
| [[RTCA]] | +0.67 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[JKAMP]] | +0.67 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[BMPR1A]] | +0.66 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[RWDD3]] | +0.66 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[SEC24B]] | +0.65 | +0.78 / +0.57 | both halves | 9e-06 |  |
| [[NAA16]] | +0.65 | +0.65 / +0.53 | both halves | 1e-05 | same gene group |
| [[C12orf76]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[FBXO7]] | +0.63 | +0.73 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGR1]] | -0.69 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[IER2]] | -0.69 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[EGR3]] | -0.66 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[EGR2]] | -0.63 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[ERCC1]] | -0.60 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[GALE]] | -0.60 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[PPP1R10]] | -0.59 | -0.70 / -0.50 | both halves | 1e-05 |  |
| [[MCL1]] | -0.59 | -0.59 / -0.57 | both halves | 8e-06 |  |
| [[CSRNP1]] | -0.57 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[BACH1]] | -0.57 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[CCDC57]] | -0.57 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[PHLDA1]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF618]] | B | ZNF618 activity raises FHIP2A's level | lines that do not express ZNF618 (9) vs lines expressing it (41) | 1.48× lower at baseline in the lines without ZNF618 | 0.023 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63 |
| [[ZNF618]] | B | ZNF618 activity strengthens FHIP2A's drug response | lines that do not express ZNF618 (9) vs lines expressing it (40) | the lines without ZNF618 respond 0.81× as strongly (z diff +1.31); strongest at Panobinostat 0.5 µM: 0.48x vs 0.33x (z diff +2.6) | 0.091 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63; target measured in part of the lines; artifact flags |
| [[SMAD4]] | C | SMAD4 activity raises FHIP2A's level | lines that do not express SMAD4 (4) vs lines expressing it (46) | 1.68× lower at baseline in the lines without SMAD4 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC26A11; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 190]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.788). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.7, -8.9); signed map (-30.8, -17.7). **Vector** length 97.1, 28.5% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.2 | +0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.9 | +0.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.0 | +3.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.5 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.2 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | +0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.0 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -7.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -1.4 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -2.2 | -3.0 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -2.2 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | FHF complex subunit HOOK interacting protein 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.3 — chr10:114,821,744-114,899,832 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA106M7.3; previously KIAA1600, FAM160B1 |
| Gene groups (HGNC) | Armadillo like helical domain containing; FHF complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5W0V3](https://www.uniprot.org/uniprotkb/Q5W0V3) (FHF complex subunit HOOK interacting protein 2A):

> Required for proper functioning of the nervous system.

**Summary**, from NCBI Gene [57700](https://www.ncbi.nlm.nih.gov/gene/57700):

> Predicted to be involved in protein transport along microtubule. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29320](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29320) · Entrez [57700](https://www.ncbi.nlm.nih.gov/gene/57700) · UniProt [Q5W0V3](https://www.uniprot.org/uniprotkb/Q5W0V3) · Ensembl [ENSG00000151553](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151553)

## Data

Gene col 7535: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7535); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7535, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7535]; `tensor/DDL_lfc|DDL_z.npy` [7535]; `embed/gene_vectors.npy` [7535]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7535 or target_col == 7535). Every well: [[FHIP2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FHIP2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
