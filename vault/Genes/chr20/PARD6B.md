---
symbol: "PARD6B"
type: "gene"
col: 4490
ensembl_id: "ENSG00000124171"
name: "par-6 family cell polarity regulator beta"
location: "20q13.13"
module: 31
arm: "+"
pooled_cpm: 80.78
n_lines_expressing: 43
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 16
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 21
direction_downstream: 1
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# PARD6B

*par-6 family cell polarity regulator beta* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.19× (z +17.3, q 0e+00, up in 33 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.438× (z -17.6, q 0e+00, down in 27 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.660× (z -4.8, q 3e-04, down in 20 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH2D3A]] (+0.61, fdr 1e-05), [[RNF39]] (+0.57, fdr 2e-05), [[PIM1]] (+0.56, fdr 7e-05); moves opposite to [[ILF3]] (-0.50, fdr 4e-05), [[NDUFA10]] (-0.48, fdr 2e-04), [[NNT]] (-0.47, fdr 5e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[CRYBG2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[FOXO3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4490.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.19×** | +17.3 | 0e+00 | 33/41 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.68×** | +16.3 | 0e+00 | 30/40 (A-427, A549, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +14.8 | 0e+00 | 30/41 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.82×** | +13.3 | 3e-38 | 29/40 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +12.7 | 9e-35 | 30/40 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.56×** | +9.5 | 2e-19 | 30/41 (BT-474, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +9.1 | 5e-18 | 28/40 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +9.1 | 5e-18 | 23/41 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +8.7 | 2e-16 | 25/40 (SW480, A-427, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.10×** | +8.6 | 6e-16 | 26/42 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +8.4 | 3e-15 | 26/41 (KATO III, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +8.3 | 4e-15 | 28/41 (A-427, A549, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +7.4 | 8e-12 | 22/41 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.33×** | +6.3 | 1e-08 | 22/41 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.71×** | +6.2 | 2e-08 | 23/40 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +5.8 | 2e-07 | 17/42 (A-427, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +5.0 | 2e-05 | 15/40 (KATO III, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +5.0 | 2e-05 | 15/42 (HepG2/C3A, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +4.2 | 8e-04 | 13/40 (A-427, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4490.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.438×** | -17.6 | 0e+00 | 27/34 (NCI-H661, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.593×** | -11.6 | 2e-28 | 30/38 (HT-29, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.660×** | -4.8 | 3e-04 | 20/40 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.681×** | -4.4 | 0.001 | 18/40 (HEC-1-A, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 0.872× | -4.3 | 0.002 | 16/41 (Hs 766T, HT-29, …) | rises with dose | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **0.830×** | -4.0 | 0.007 | 17/41 (NCI-H2347, LS 180, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.833× | -3.9 | 0.008 | 17/40 (NCI-H23, J82, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.729×** | -3.7 | 0.018 | 16/41 (HEC-1-A, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.892× | -3.6 | 0.021 | 16/42 (HEC-1-A, SW48, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.735×** | -3.6 | 0.021 | 18/40 (KATO III, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.860× | -3.1 | 0.10 | 17/35 (KATO III, NCI-H661, …) | all doses, stronger at high dose | composition shift |
| [[Arbutin (drug)]] 0.05 µM |  | 0.861× | -3.1 | 0.10 | 3/40 (AN3 CA, SNU-423, …) | all doses, flat | position effect removed |
| [[Arbutin (drug)]] 0.5 µM |  | 0.873× | -3.0 | 0.11 | 5/40 (HepG2/C3A, A549, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4490. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 130 | 10 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +20.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.73× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -11.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 131 | 9 (7 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +13.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.00× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 81.3 | 9 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.74× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -12.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 92.5 | 8 (2 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.62× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.544× (z -8.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 134 | 3 (1 ⚠) | 4 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.25× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.382× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.271× (z -8.6) |
| [[PANC-1 (line)]] | alt | 89.8 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.62× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -10.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 175 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -12.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 22.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +10.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.81× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 26.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.95× (z +10.9) | [[Selinexor (drug)]] 5 µM 0.351× (z -9.2) ⚠ cell-cycle shift, explains ~75% of this change |
| [[NCI-H661 (line)]] | alt | 153 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0355× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.232× (z -8.8) |
| [[A549 (line)]] | wt | 59.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +14.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.66× (z +13.5) | — |
| [[HCT15 (line)]] | alt | 138 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -12.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 148 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -13.9) ⚠ cell-cycle shift, explains ~17% of this change |
| [[HT-29 (line)]] | alt | 190 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -13.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 25.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.87× (z +9.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.233× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 25.9 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.20× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.208× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 65.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.12× (z +16.6) | — |
| [[A498 (line)]] | wt | 63.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.8) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -8.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 225 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -9.3) ⚠ cell-cycle shift, explains ~17% of this change |
| [[HepG2_C3A (line)]] | wt | 76.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +12.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.62× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 120 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -10.0) ⚠ cell-cycle shift, explains ~17% of this change |
| [[Panc 03.27 (line)]] | alt | 222 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -11.3) ⚠ cell-cycle shift, explains ~17% of this change |
| [[SNU-423 (line)]] | alt | 54.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +8.9) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 5 µM 0.313× (z -9.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 146 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -11.8) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.322× (z -8.6) |
| [[J82 (line)]] | alt | 100.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 57.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.25× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 29.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -9.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 34.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +9.4) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SW 900 (line)]] | alt | 60.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -17.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.6 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 19.9 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.74 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 88.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.5 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 81.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 193 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4490), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH2D3A]] | +0.61 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[RNF39]] | +0.57 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[PIM1]] | +0.56 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[GRB7]] | +0.55 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[GJB3]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[EPHA2-AS1]] | +0.55 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[BACH2]] | +0.55 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[RDH13]] | +0.54 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[GPRC5A]] | +0.54 | +0.36 / +0.49 | both halves | 9e-05 |  |
| [[PLIN3]] | +0.54 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[CTTNBP2NL]] | +0.53 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[SERTAD2]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ILF3]] | -0.50 | -0.44 / -0.41 | both halves | 4e-05 | pathway: Cell junction organization |
| [[NDUFA10]] | -0.48 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[NNT]] | -0.47 | -0.24 / -0.38 | both halves | 5e-04 |  |
| [[TAS2R30]] | -0.47 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[SNX5]] | -0.46 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[FAM53B]] ⚠ | -0.46 | -0.36 / -0.34 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[METTL4]] | -0.45 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[HCFC1]] | -0.45 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[CA5BP1-1]] | -0.45 | -0.24 / -0.39 | both halves | 5e-04 |  |
| [[EIF2D]] | -0.44 | -0.23 / -0.37 | both halves | 5e-04 |  |
| [[STXBP4]] | -0.44 | -0.46 / -0.35 | both halves | 1e-04 | same gene group |
| [[SEPHS1]] | -0.43 | -0.25 / -0.42 | both halves | 4e-04 |  |
| [[GALC]] | -0.43 | -0.34 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 20, C 1. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRYBG2]] | B | CRYBG2 activity raises PARD6B's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 3.48× lower at baseline in the lines without CRYBG2 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[IL18]] | B | IL18 activity raises PARD6B's level | lines that do not express IL18 (18) vs lines expressing it (32) | 3.60× lower at baseline in the lines without IL18 | 5e-04 | ⚠ within organs, on part of the lines; also absent: LSR, SPINT2, LAMA3 |
| [[SH2D3A]] | B | SH2D3A activity raises PARD6B's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 3.27× lower at baseline in the lines without SH2D3A | 1e-03 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[GRB7]] | B | GRB7 activity raises PARD6B's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 3.49× lower at baseline in the lines without GRB7 | 0.002 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[RNF39]] | B | RNF39 activity raises PARD6B's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 3.07× lower at baseline in the lines without RNF39 | 0.002 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[C1orf116]] | B | C1orf116 activity raises PARD6B's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 3.36× lower at baseline in the lines without C1orf116 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[CLDN4]] | B | CLDN4 activity raises PARD6B's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 3.16× lower at baseline in the lines without CLDN4 | 0.004 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[JUP]] | B | JUP activity raises PARD6B's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.72× lower at baseline in the lines without JUP | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[PCDH1]] | B | PCDH1 activity raises PARD6B's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.31× lower at baseline in the lines without PCDH1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[FGD6]] | B | FGD6 activity raises PARD6B's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 3.68× lower at baseline in the lines without FGD6 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[USP43]] | B | USP43 activity raises PARD6B's level | lines that do not express USP43 (10) vs lines expressing it (40) | 3.50× lower at baseline in the lines without USP43 | 0.008 | ⚠ within organs, on part of the lines; also absent: LLGL2, KRTAP5-AS1, BTG3-AS1 |
| [[TMC6]] | B | TMC6 activity raises PARD6B's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 3.03× lower at baseline in the lines without TMC6 | 0.010 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FOXO3]] | B | PARD6B activity raises FOXO3's level | lines that do not express PARD6B (7) vs lines expressing it (43) | 1.33× lower at baseline in the lines without PARD6B | 0.044 | ⚠ within organs, on part of the lines; also absent: CCDC120, ENSG00000291079, MERTK; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.500). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.5, 57.6); signed map (-2.1, 36.5). **Vector** length 105, 26.6% of its response variance represented; |z| ≥ 3 in 1,305 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +8.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.1 | +8.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.8 | +13.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +17.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.7 | +5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +5.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.2 | -1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -17.6 |
|  | [[EX229 (drug)]] 5 µM |  | -4.6 | -4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.4 | -11.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.3 | -4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.1 | -3.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.1 | -3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.7 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | par-6 family cell polarity regulator beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:50,731,580-50,756,795 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAR-6B |
| Gene groups (HGNC) | PDZ domain containing |
| Reactome | 8 pathways, smallest: Tight junction interactions; RHOV GTPase cycle; Cell-cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYG5](https://www.uniprot.org/uniprotkb/Q9BYG5) (Partitioning defective 6 homolog beta):

> Adapter protein involved in asymmetrical cell division and cell polarization processes. Probably involved in formation of epithelial tight junctions. Association with PARD3 may prevent the interaction of PARD3 with F11R/JAM1, thereby preventing tight junction assembly. The PARD6-PARD3 complex links GTP-bound Rho small GTPases to atypical protein kinase C proteins.

**Summary**, from NCBI Gene [84612](https://www.ncbi.nlm.nih.gov/gene/84612):

> This gene is a member of the PAR6 family and encodes a protein with a PSD95/Discs-large/ZO1 (PDZ) domain, an OPR domain and a semi-Cdc42/Rac interactive binding (CRIB) domain. This cytoplasmic protein is involved in asymmetrical cell division and cell polarization processes as a member of a multi-protein complex. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16245](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16245) · Entrez [84612](https://www.ncbi.nlm.nih.gov/gene/84612) · UniProt [Q9BYG5](https://www.uniprot.org/uniprotkb/Q9BYG5) · Ensembl [ENSG00000124171](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124171)

## Data

Gene col 4490: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4490); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4490, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4490]; `tensor/DDL_lfc|DDL_z.npy` [4490]; `embed/gene_vectors.npy` [4490]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4490 or target_col == 4490). Every well: [[PARD6B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARD6B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
