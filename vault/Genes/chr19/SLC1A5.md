---
symbol: "SLC1A5"
type: "gene"
col: 2575
ensembl_id: "ENSG00000105281"
name: "solute carrier family 1 member 5"
location: "19q13.32"
module: 63
arm: "+"
pooled_cpm: 59.39
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 24
n_dd_up_clean: 15
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# SLC1A5

*solute carrier family 1 member 5* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.74× (z +10.0, q 1e-20, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.385× (z -17.3, q 0e+00, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTHFD2]] (+0.73, fdr 7e-06), [[ASNS]] (+0.71, fdr 7e-06), [[CARS1]] (+0.70, fdr 7e-06); moves opposite to [[WBP4]] (-0.54, fdr 3e-05), [[PLPP3]] (-0.47, fdr 4e-05), [[ITSN2]] (-0.47, fdr 5e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SNTB1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2575.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +10.0 | 1e-20 | 37/47 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.68×** | +9.4 | 2e-18 | 41/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.35×** | +7.5 | 9e-12 | 24/47 (A549, NCI-H460, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.42×** | +6.3 | 5e-08 | 31/47 (Panc 03.27, Hs 766T, …) | rises with dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.41×** | +6.2 | 6e-08 | 32/47 (NCI-H2030, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.27×** | +6.1 | 9e-08 | 26/47 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.78×** | +5.4 | 4e-06 | 23/47 (NCI-H460, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +5.4 | 5e-06 | 26/46 (J82, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.35×** | +5.4 | 5e-06 | 23/45 (HEC-1-A, A549, …) | two highest doses | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +5.4 | 5e-06 | 22/45 (HOP62, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Neratinib (drug)]] 5 µM |  | **1.33×** | +5.2 | 1e-05 | 27/47 (HEC-1-A, RKO, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.20×** | +4.7 | 1e-04 | 22/47 (NCI-H2030, HEC-1-A, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.30×** | +4.6 | 2e-04 | 18/36 (HEC-1-A, NCI-H1792, …) | two highest doses | composition shift; position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 2e-04 | 23/47 (HEC-1-A, HCT15, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.27×** | +4.2 | 9e-04 | 22/47 (A549, A-427, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.003 | 16/46 (NCI-H460, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.17× | +3.9 | 0.003 | 17/48 (Hs 766T, NCI-H460, …) | top dose only |  |
| [[Erlotinib (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.006 | 16/46 (NCI-H2030, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.006 | 21/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.009 | 16/47 (SHP-77, BT-474, …) | top dose only |  |
| [[Neratinib (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.010 | 14/47 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.019 | 13/46 (hTERT-HPNE, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2575.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.385×** | -17.3 | 0e+00 | 37/47 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.424×** | -15.0 | 0e+00 | 34/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.489×** | -13.0 | 2e-36 | 33/46 (SW480, SW48, …) | all doses, flat | cell-cycle shift (explains ~13% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.507×** | -12.3 | 8e-33 | 33/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.549×** | -10.9 | 2e-25 | 36/47 (SW48, H4, …) | all doses, flat | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.698×** | -9.3 | 2e-18 | 27/46 (SW480, KATO III, …) | all doses, flat | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.610×** | -9.0 | 2e-17 | 28/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.618×** | -8.8 | 1e-16 | 32/47 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.623×** | -8.6 | 4e-16 | 30/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.625×** | -7.9 | 2e-13 | 32/46 (HS-578T, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | **0.668×** | -7.1 | 9e-11 | 34/47 (H4, SW480, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.514×** | -6.3 | 1e-08 | 30/46 (KATO III, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.515×** | -6.3 | 1e-08 | 31/48 (KATO III, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **0.818×** | -5.2 | 8e-06 | 21/47 (LOX-IMVI, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.749×** | -5.1 | 2e-05 | 27/46 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.777×** | -4.6 | 1e-04 | 22/47 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.810×** | -4.6 | 1e-04 | 20/47 (SW480, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2575. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 296 | 0 | 24 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -36.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0836× (z -27.2) |
| [[H4 (line)]] | wt | 151 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -20.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -18.0) |
| [[KATO III (line)]] | alt | 109 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -26.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.110× (z -25.2) |
| [[SW48 (line)]] | wt | 142 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -20.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0760× (z -19.1) |
| [[RKO (line)]] | wt | 70.4 | 0 | 9 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.124× (z -17.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.275× (z -11.5) |
| [[HS-578T (line)]] | alt | 71.3 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -16.0) |
| [[LoVo (line)]] | wt | 59.5 | 0 | 8 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.144× (z -19.9) |
| [[SW1417 (line)]] | alt | 86.9 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -12.4) |
| [[HOP62 (line)]] | alt | 33.0 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.267× (z -12.6) |
| [[A-172 (line)]] | wt | 30.1 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0918× (z -18.6) |
| [[A498 (line)]] | wt | 73.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -17.2) |
| [[HT-29 (line)]] | alt | 136 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -11.6) |
| [[PANC-1 (line)]] | alt | 45.0 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.270× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.349× (z -12.8) |
| [[A-427 (line)]] | wt | 30.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -18.3) |
| [[HEC-1-A (line)]] | alt | 49.7 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Homoharringtonine (drug)]] 0.05 µM 0.329× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 68.7 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.184× (z -14.4) |
| [[LS 180 (line)]] | wt | 44.9 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.206× (z -14.0) |
| [[NCI-H1792 (line)]] | alt | 22.0 | 3 (3 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.14× (z +9.4) ⚠ unreliable plate only | — |
| [[NCI-H460 (line)]] | wt | 24.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +10.8) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.27× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 64.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.135× (z -13.5) |
| [[HCT15 (line)]] | alt | 69.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -16.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[hTERT-HPNE (line)]] | wt | 47.9 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.221× (z -11.6) |
| [[SW 900 (line)]] | alt | 42.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.174× (z -12.2) |
| [[A549 (line)]] | wt | 38.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +12.5) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[AsPC-1 (line)]] | alt | 31.2 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.00× (z +8.6) ⚠ unreliable plate only | — |
| [[C-33 A (line)]] | alt | 23.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -9.8) |
| [[CHP-212 (line)]] | wt | 34.8 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.101× (z -9.3) ⚠ transcription drop |
| [[HepG2_C3A (line)]] | wt | 53.8 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.252× (z -8.9) |
| [[Hs 766T (line)]] | wt | 28.7 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.57× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 25.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.244× (z -10.6) |
| [[SNU-1 (line)]] | wt | 31.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -12.3) |
| [[AN3 CA (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2575), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTHFD2]] | +0.73 | +0.71 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 448 |
| [[ASNS]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 557 |
| [[CARS1]] | +0.70 | +0.65 / +0.73 | both halves | 7e-06 | STRING 433 |
| [[SLC1A4]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MTORC1_SIGNALING; STRING 654 |
| [[GOT1]] | +0.69 | +0.64 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 450 |
| [[PYCR1]] | +0.69 | +0.75 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_XENOBIOTIC_METABOLISM; STRING 406 |
| [[PSAT1]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 624 |
| [[SLC7A1]] | +0.69 | +0.72 / +0.67 | both halves | 7e-06 | pathway: Amino acid transport across the plasma membrane; STRING 747 |
| [[IARS1]] | +0.67 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ARHGEF2]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[XPOT]] | +0.65 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[AARS1]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WBP4]] | -0.54 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[PLPP3]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ITSN2]] | -0.47 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[ZSCAN18]] | -0.46 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[ZNF441]] | -0.46 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[DDX52]] | -0.45 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[STAT5B]] | -0.45 | -0.44 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNTB1]] | B | SNTB1 activity raises SLC1A5's level | lines that do not express SNTB1 (19) vs lines expressing it (31) | 1.84× lower at baseline in the lines without SNTB1 | 0.045 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979 |
| [[LINC00662]] | C | LINC00662 activity weakens SLC1A5's drug response | lines that do not express LINC00662 (3) vs lines expressing it (44) | the lines without LINC00662 respond 1.84× as strongly (z diff -3.16); strongest at Homoharringtonine 5 µM: 0.26x vs 0.67x (z diff -5.7) | 0.088 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: NME4, ZFP14, ZNF221; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.9, 48.3); signed map (-13.7, 25.1). **Vector** length 136, 41.7% of its response variance represented; |z| ≥ 3 in 1,420 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.60 to 16); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.62 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.62 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.4 | +9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +10.0 |
|  | [[Artesunate (drug)]] 5 µM |  | +5.7 | +6.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.4 | +5.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +5.4 | +5.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.6 | +6.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.3 | +3.7 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +4.0 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.8 | -10.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.6 | -17.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -6.8 | -7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -15.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.8 | -5.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -4.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 1 member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:46,774,883-46,788,594 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AAAT, ASCT2; previously RDRC, M7V1 |
| Gene groups (HGNC) | Minor histocompatibility antigens; Solute carrier family 1 |
| Hallmark sets | XENOBIOTIC_METABOLISM, IL2_STAT5_SIGNALING, ADIPOGENESIS, MTORC1_SIGNALING |
| Reactome | 12 pathways, smallest: Amino acid transport across the plasma membrane; SLC-mediated transport of amino acids; RHOH GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15758](https://www.uniprot.org/uniprotkb/Q15758) (Neutral amino acid transporter B(0)):

> Sodium-coupled antiporter of neutral amino acids. In a tri-substrate transport cycle, exchanges neutral amino acids between the extracellular and intracellular compartments, coupled to the inward cotransport of at least one sodium ion. The preferred substrate is the essential amino acid L-glutamine, a precursor for biosynthesis of proteins, nucleotides and amine sugars as well as an alternative fuel for mitochondrial oxidative phosphorylation. Exchanges L-glutamine with other neutral amino …

**Summary**, from NCBI Gene [6510](https://www.ncbi.nlm.nih.gov/gene/6510):

> The SLC1A5 gene encodes a sodium-dependent neutral amino acid transporter that can act as a receptor for RD114/type D retrovirus (Larriba et al., 2001 [PubMed 11781704]).[supplied by OMIM, Jan 2011]

**Accessions** — [HGNC:10943](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10943) · Entrez [6510](https://www.ncbi.nlm.nih.gov/gene/6510) · UniProt [Q15758](https://www.uniprot.org/uniprotkb/Q15758) · Ensembl [ENSG00000105281](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105281)

## Data

Gene col 2575: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2575); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2575, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2575]; `tensor/DDL_lfc|DDL_z.npy` [2575]; `embed/gene_vectors.npy` [2575]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2575 or target_col == 2575). Every well: [[SLC1A5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC1A5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
