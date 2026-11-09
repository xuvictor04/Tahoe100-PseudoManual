---
symbol: "NUCB1"
type: "gene"
col: 2498
ensembl_id: "ENSG00000104805"
name: "nucleobindin 1"
location: "19q13.33"
module: 50
arm: "+"
pooled_cpm: 48.81
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# NUCB1

*nucleobindin 1* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.33× (z +15.9, q 0e+00, up in 43 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.83× (z +11.4, q 9e-28, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.413× (z -16.6, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OS9]] (+0.73, fdr 7e-06), [[PLOD1]] (+0.69, fdr 7e-06), [[MAN2B2]] (+0.68, fdr 7e-06); moves opposite to [[WDR75]] (-0.66, fdr 1e-05), [[TMEM70]] (-0.63, fdr 1e-05), [[MRPL15]] (-0.62, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2498.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.33×** | +15.9 | 0e+00 | 43/46 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +14.6 | 1e-45 | 36/38 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +11.4 | 9e-28 | 41/47 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +10.8 | 6e-25 | 37/43 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +9.9 | 3e-21 | 33/47 (NCI-H2347, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +7.0 | 3e-10 | 30/47 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +6.7 | 2e-09 | 27/47 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +6.6 | 3e-09 | 30/47 (LoVo, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.74×** | +5.5 | 3e-06 | 30/44 (SW1417, LoVo, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +5.5 | 3e-06 | 29/47 (A498, SW1417, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +4.7 | 2e-04 | 26/47 (SW1417, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.24×** | +4.0 | 0.003 | 23/46 (KATO III, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Omeprazole (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.063 | 12/47 (A498, A549, …) | inconsistent across doses |  |
| [[Bicalutamide (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.11 | 5/47 (NCI-H1792, LS 180, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2498.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.413×** | -16.6 | 0e+00 | 43/47 (A-427, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.478×** | -13.3 | 4e-38 | 43/47 (CFPAC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.638×** | -11.9 | 1e-30 | 29/47 (A-427, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.631×** | -8.7 | 7e-16 | 39/47 (NCI-H23, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.660×** | -7.5 | 7e-12 | 37/47 (HS-578T, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.687×** | -7.0 | 2e-10 | 37/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.707×** | -6.5 | 6e-09 | 33/47 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.784×** | -4.4 | 8e-04 | 22/45 (C-33 A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.798×** | -4.2 | 0.001 | 22/46 (SW480, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.807×** | -4.0 | 0.003 | 25/47 (C-33 A, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.667×** | -4.0 | 0.003 | 20/47 (A498, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.821×** | -3.7 | 0.010 | 17/47 (LS 180, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.825×** | -3.6 | 0.013 | 20/47 (C32, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.826×** | -3.6 | 0.013 | 19/47 (KATO III, A549, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trimetrexate (drug)]] 5 µM |  | 0.891× | -3.1 | 0.084 | 8/47 (C32, MIA PaCa-2, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2498. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 75.2 | 3 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.53× (z +10.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -15.0) |
| [[A-427 (line)]] | wt | 58.0 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.97× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -25.9) |
| [[LoVo (line)]] | wt | 26.2 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +17.0) | [[Harringtonine (drug)]] 5 µM 0.321× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 43.0 | 3 (2 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -16.1) |
| [[AsPC-1 (line)]] | alt | 27.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 52.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.97× (z +14.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.40× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 51.6 | 1 | 3 | [[Auranofin (drug)]] 5 µM 3.23× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -21.5) |
| [[J82 (line)]] | alt | 85.3 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.48× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -13.0) |
| [[LS 180 (line)]] | wt | 44.0 | 1 | 3 | [[Panobinostat (drug)]] 0.5 µM 2.74× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -16.1) |
| [[NCI-H460 (line)]] | wt | 38.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.05 µM 0.345× (z -12.2) |
| [[PANC-1 (line)]] | alt | 38.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.278× (z -14.4) |
| [[SNU-1 (line)]] | wt | 46.1 | 0 | 4 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.279× (z -11.7) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.295× (z -11.2) |
| [[SW1417 (line)]] | alt | 54.7 | 2 (1 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 2.30× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -13.8) |
| [[A-172 (line)]] | wt | 48.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -8.6) |
| [[A498 (line)]] | wt | 74.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +11.1) ⚠ toxic; transcription drop | [[Penfluridol (drug)]] 5 µM 0.489× (z -9.0) |
| [[A549 (line)]] | wt | 61.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -14.2) |
| [[CFPAC-1 (line)]] | alt | 37.7 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -16.3) |
| [[HOP62 (line)]] | alt | 39.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 39.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.05 µM 0.342× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 66.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.255× (z -14.1) |
| [[SW 900 (line)]] | alt | 60.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.301× (z -11.5) |
| [[H4 (line)]] | wt | 82.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -14.4) |
| [[HS-578T (line)]] | alt | 115 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.433× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 68.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.421× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 29.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -17.7) |
| [[RPMI-7951 (line)]] | alt | 110 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.286× (z -13.2) |
| [[SHP-77 (line)]] | alt | 77.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -12.1) |
| [[SK-MEL-2 (line)]] | alt | 46.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -13.6) |
| [[SW480 (line)]] | alt | 14.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +9.3) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.235× (z -9.5) ⚠ toxic |
| [[C32 (line)]] | wt | 89.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.382× (z -9.7) |
| [[CHP-212 (line)]] | wt | 37.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 28.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 48.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -13.3) |
| [[hTERT-HPNE (line)]] | wt | 68.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 33.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 19.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 33.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.304× (z -8.9) |
| [[NCI-H661 (line)]] | alt | 48.9 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.110× (z -9.2) |
| [[RKO (line)]] | wt | 42.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 44.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.256× (z -11.8) |
| [[SW 1088 (line)]] | alt | 73.6 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.0914× (z -8.7) |
| [[AN3 CA (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2498), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OS9]] | +0.73 | +0.71 / +0.70 | both halves | 7e-06 | STRING 683 |
| [[PLOD1]] | +0.69 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[MAN2B2]] | +0.68 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[PSAP]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[FKBP8]] | +0.65 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[SDF4]] | +0.65 | +0.60 / +0.74 | both halves | 7e-06 | STRING 526 |
| [[PRKCSH]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 | same gene group; pathway: Post-translational protein phosphorylation; STRING 490 |
| [[CANX]] | +0.64 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[GRN]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[LAMP1]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[HDLBP]] | +0.62 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[DDOST]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR75]] | -0.66 | -0.56 / -0.69 | both halves | 1e-05 |  |
| [[TMEM70]] | -0.63 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[MRPL15]] | -0.62 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[MRPS18B]] | -0.62 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[BRIX1]] | -0.61 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[DMAC1]] | -0.60 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[CMTR2]] | -0.60 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[PPP1R35]] ⚠ | -0.60 | -0.47 / -0.62 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TIMM9]] | -0.59 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[ZNF593]] | -0.58 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[LSM6]] | -0.56 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[TMEM265]] | -0.56 | -0.34 / -0.61 | both halves | 1e-04 |  |
| [[MRPS16]] | -0.56 | -0.54 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers NUCB1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.3, -20.5); signed map (-52.1, -4.4). **Vector** length 125, 35.8% of its response variance represented; |z| ≥ 3 in 1,069 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Extracellular matrix organization* (reactome, mean cos +0.53 to 12); *Degradation of the extracellular matrix* (reactome, mean cos +0.56 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.0 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.6 | +15.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.5 | +10.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.1 | +11.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +9.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.3 | +5.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.4 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +1.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.0 | +2.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -11.1 | -8.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.7 | -13.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.1 | -16.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.2 | -7.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -6.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.5 | -4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | nucleobindin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,900,050-48,923,473 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NUC, Calnuc |
| Gene groups (HGNC) | EF-hand domain containing |
| Reactome | 2 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02818](https://www.uniprot.org/uniprotkb/Q02818) (Nucleobindin-1):

> Major calcium-binding protein of the Golgi which may have a role in calcium homeostasis (By similarity). Acts as a non-receptor guanine nucleotide exchange factor which binds to and activates alpha subunits of guanine nucleotide-binding proteins (G proteins) (By similarity).

**Summary**, from NCBI Gene [4924](https://www.ncbi.nlm.nih.gov/gene/4924):

> This gene encodes a member of a small calcium-binding EF-hand protein family. The encoded protein is thought to have a key role in Golgi calcium homeostasis and Ca(2+)-regulated signal transduction events. [provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:8043](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8043) · Entrez [4924](https://www.ncbi.nlm.nih.gov/gene/4924) · UniProt [Q02818](https://www.uniprot.org/uniprotkb/Q02818) · Ensembl [ENSG00000104805](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104805)

## Data

Gene col 2498: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2498); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2498, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2498]; `tensor/DDL_lfc|DDL_z.npy` [2498]; `embed/gene_vectors.npy` [2498]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2498 or target_col == 2498). Every well: [[NUCB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUCB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
