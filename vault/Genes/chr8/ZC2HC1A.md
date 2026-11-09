---
symbol: "ZC2HC1A"
type: "gene"
col: 2460
ensembl_id: "ENSG00000104427"
name: "zinc finger C2HC-type containing 1A"
location: "8q21.13"
module: 3
arm: "+"
pooled_cpm: 44.1
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 17
n_dd_up_clean: 25
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# ZC2HC1A

*zinc finger C2HC-type containing 1A* — 8q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.01× (z +14.5, q 1e-44, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.436× (z -17.2, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNIH4]] (+0.65, fdr 3e-05), [[EXOC1]] (+0.64, fdr 9e-06), [[DCXR]] (+0.62, fdr 1e-05); moves opposite to [[SSU72]] (-0.58, fdr 7e-05), [[TRRAP]] (-0.57, fdr 1e-05), [[TARDBP]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NOTCH2NLR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2460.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.01×** | +14.5 | 1e-44 | 43/47 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.91×** | +13.4 | 2e-38 | 38/47 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +12.9 | 5e-36 | 38/47 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +10.6 | 4e-24 | 35/47 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +7.5 | 6e-12 | 23/47 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +7.2 | 6e-11 | 30/47 (RKO, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +7.1 | 9e-11 | 28/47 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.27×** | +7.0 | 1e-10 | 25/47 (J82, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.30×** | +5.3 | 6e-06 | 22/47 (J82, LS 180, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.29×** | +5.2 | 1e-05 | 25/47 (SW1417, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +5.1 | 2e-05 | 21/47 (J82, LOX-IMVI, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.9 | 4e-05 | 22/47 (RKO, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.8 | 6e-05 | 18/47 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +4.7 | 1e-04 | 20/47 (RKO, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.25×** | +4.5 | 2e-04 | 16/47 (RKO, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.24×** | +4.5 | 2e-04 | 22/47 (NCI-H2347, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.24×** | +4.5 | 2e-04 | 18/47 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.49×** | +4.3 | 6e-04 | 19/47 (RKO, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2460.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.436×** | -17.2 | 0e+00 | 45/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.459×** | -16.1 | 0e+00 | 44/47 (HEC-1-A, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.489×** | -14.8 | 0e+00 | 43/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.281×** | -13.7 | 8e-41 | 43/48 (HOP62, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.528×** | -13.2 | 6e-38 | 36/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.557×** | -12.1 | 7e-32 | 39/47 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.334×** | -11.9 | 2e-30 | 40/47 (HEC-1-A, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.633×** | -8.8 | 1e-16 | 29/42 (HS-578T, HOP62, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.659×** | -8.7 | 3e-16 | 28/45 (SK-MEL-2, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.655×** | -8.4 | 2e-15 | 31/39 (Panc 03.27, HS-578T, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.706×** | -7.2 | 2e-11 | 29/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.696×** | -7.2 | 2e-11 | 27/46 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.734×** | -6.4 | 6e-09 | 27/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.741×** | -6.2 | 2e-08 | 29/47 (PANC-1, Hs 766T, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.788×** | -4.9 | 3e-05 | 22/47 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.830×** | -3.7 | 0.008 | 16/47 (SW 1271, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.898× | -3.2 | 0.043 | 4/47 (SW 1271, HCT15, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.858× | -3.0 | 0.077 | 14/46 (HEC-1-A, BT-474, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 0.5 µM |  | 0.869× | -2.9 | 0.095 | 6/47 (NCI-H1573, HEC-1-A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2460. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 58.1 | 0 | 12 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.237× (z -17.3) |
| [[HS-578T (line)]] | alt | 132 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.467× (z -13.7) |
| [[RKO (line)]] | wt | 54.3 | 9 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +15.3) | — |
| [[SW480 (line)]] | alt | 26.2 | 4 | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +11.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.263× (z -13.6) |
| [[NCI-H460 (line)]] | wt | 27.0 | 1 | 7 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +12.2) | [[Digitoxin (drug)]] 5 µM 0.202× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.222× (z -15.4) |
| [[HOP62 (line)]] | alt | 71.2 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.123× (z -12.1) |
| [[A498 (line)]] | wt | 84.4 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.69× (z +13.5) | [[TAK-901 (drug)]] 5 µM 0.238× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 46.9 | 0 | 6 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.292× (z -14.4) |
| [[LoVo (line)]] | wt | 22.7 | 4 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +10.8) | [[TAK-901 (drug)]] 5 µM 0.141× (z -8.9) |
| [[A549 (line)]] | wt | 49.8 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.132× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 47.3 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.315× (z -11.2) |
| [[LS 180 (line)]] | wt | 23.5 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.29× (z +10.5) | [[Digitoxin (drug)]] 5 µM 0.203× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.303× (z -8.6) |
| [[A-172 (line)]] | wt | 72.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -12.6) |
| [[Hs 766T (line)]] | wt | 57.1 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.271× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.308× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 47.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.227× (z -13.3) |
| [[SHP-77 (line)]] | alt | 65.1 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +8.6) | [[Digitoxin (drug)]] 0.5 µM 0.388× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 48.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.342× (z -9.0) |
| [[J82 (line)]] | alt | 40.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.34× (z +11.7) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.359× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 40.9 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.292× (z -10.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 45.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -10.6) |
| [[C32 (line)]] | wt | 44.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.01× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.238× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 20.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.87× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.207× (z -10.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 42.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.293× (z -10.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 62.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -10.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -9.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 26.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.31× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 28.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.15× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 18.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.252× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 71.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.418× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 46.8 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.123× (z -8.6) ⚠ toxic |
| [[SW1417 (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -10.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.70 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2460), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNIH4]] | +0.65 | +0.46 / +0.69 | both halves | 3e-05 |  |
| [[EXOC1]] | +0.64 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[DCXR]] | +0.62 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[MRPS31]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[CDK7]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[RRAGC]] | +0.58 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ZYG11B]] | +0.58 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[DYNC1I2]] | +0.58 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[PDCD5]] | +0.58 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[FBXW5]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ACTR10]] | +0.57 | +0.64 / +0.40 | both halves | 4e-05 |  |
| [[SMIM29]] | +0.57 | +0.52 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSU72]] | -0.58 | -0.38 / -0.64 | both halves | 7e-05 |  |
| [[TRRAP]] | -0.57 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[TARDBP]] | -0.57 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[ATP2A2]] | -0.55 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[HCFC1]] | -0.55 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[SRSF1]] | -0.54 | -0.26 / -0.61 | both halves | 4e-04 |  |
| [[C2CD3]] | -0.53 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[HNRNPA3]] | -0.53 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[MFN2]] | -0.53 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[ILF3]] | -0.52 | -0.32 / -0.57 | both halves | 1e-04 |  |
| [[XRCC5]] | -0.52 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[TMEM33]] | -0.51 | -0.37 / -0.48 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOTCH2NLR]] | B | NOTCH2NLR activity raises ZC2HC1A's level | lines that do not express NOTCH2NLR (9) vs lines expressing it (41) | 1.51× lower at baseline in the lines without NOTCH2NLR | 0.038 | ⚠ within organs, on part of the lines |
| [[ADGRF5]] | B | ADGRF5 activity raises ZC2HC1A's level | lines that do not express ADGRF5 (39) vs lines expressing it (11) | 1.37× lower at baseline in the lines without ADGRF5 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01425, OVAAL, LINC02267 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.419). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-26.4, -31.0); signed map (-15.4, 2.0). **Vector** length 101, 28.6% of its response variance represented; |z| ≥ 3 in 1,360 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +4.2 | +7.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +4.0 | +4.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.8 | +3.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.7 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.6 | +4.1 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.5 | +3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.2 | +4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.4 | +0.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.5 | -16.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.4 | -8.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.6 | -13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -5.5 | -8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -5.1 | -8.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | -11.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | +3.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger C2HC-type containing 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.13 — chr8:78,666,050-78,719,765 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-62; previously C8orf70, FAM164A |
| Gene groups (HGNC) | Zinc fingers ZC2HC1-type |
| Matched by | ensembl_id |

UniProt [Q96GY0](https://www.uniprot.org/uniprotkb/Q96GY0) carries no function annotation.

**Summary**, from NCBI Gene [51101](https://www.ncbi.nlm.nih.gov/gene/51101):

> Predicted to enable zinc ion binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24277](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24277) · Entrez [51101](https://www.ncbi.nlm.nih.gov/gene/51101) · UniProt [Q96GY0](https://www.uniprot.org/uniprotkb/Q96GY0) · Ensembl [ENSG00000104427](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104427)

## Data

Gene col 2460: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2460); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2460, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2460]; `tensor/DDL_lfc|DDL_z.npy` [2460]; `embed/gene_vectors.npy` [2460]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2460 or target_col == 2460). Every well: [[ZC2HC1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZC2HC1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
