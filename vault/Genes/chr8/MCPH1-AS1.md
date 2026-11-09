---
symbol: "MCPH1-AS1"
type: "gene"
col: 14649
ensembl_id: "ENSG00000249898"
name: "MCPH1 antisense RNA 1"
location: "8p23.1"
module: 23
arm: "+"
pooled_cpm: 20.23
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 16
n_dd_up_clean: 20
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# MCPH1-AS1

*MCPH1 antisense RNA 1* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.51× (z +44.9, q 0e+00, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.467× (z -11.5, q 4e-28, down in 28 of 43 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.523× (z -10.2, q 5e-22, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01135]] (+0.69, fdr 7e-06), [[HAS2-AS1]] (+0.64, fdr 1e-05), [[DPY19L2P2]] (+0.62, fdr 5e-05); moves opposite to [[MPST]] (-0.54, fdr 4e-04), [[CYRIB]] (-0.54, fdr 9e-05), [[LPCAT4]] (-0.53, fdr 4e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14649.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.51×** | +44.9 | 0e+00 | 38/46 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.94×** | +30.6 | 0e+00 | 41/45 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.41×** | +29.3 | 0e+00 | 37/45 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.39×** | +17.8 | 0e+00 | 30/35 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.92×** | +16.9 | 0e+00 | 34/47 (SHP-77, HCT15, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.29×** | +13.1 | 3e-37 | 24/40 (NCI-H460, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.19×** | +11.9 | 1e-30 | 26/46 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +11.4 | 3e-28 | 35/45 (KATO III, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +9.3 | 1e-18 | 13/28 (NCI-H460, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.97×** | +9.0 | 2e-17 | 17/29 (LOX-IMVI, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +7.5 | 3e-12 | 26/47 (KATO III, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +7.2 | 3e-11 | 25/47 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +7.0 | 1e-10 | 22/47 (LS 180, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.1 | 4e-08 | 23/47 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +5.3 | 4e-06 | 15/46 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.35×** | +4.8 | 7e-05 | 10/47 (A-172, LS 180, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.36×** | +4.6 | 1e-04 | 12/46 (LOX-IMVI, C-33 A, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.33×** | +4.5 | 3e-04 | 12/46 (C-33 A, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +4.3 | 6e-04 | 16/47 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14649.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.467×** | -11.5 | 4e-28 | 28/43 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.523×** | -10.2 | 5e-22 | 28/46 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.596×** | -8.2 | 6e-14 | 27/47 (PANC-1, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.668×** | -6.4 | 3e-08 | 21/45 (C-33 A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.822×** | -4.4 | 0.001 | 14/47 (C32, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.751×** | -4.3 | 0.002 | 19/47 (C32, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.774×** | -4.0 | 0.004 | 17/47 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.791×** | -3.7 | 0.014 | 10/47 (NCI-H2030, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.792×** | -3.7 | 0.014 | 20/47 (C-33 A, LS 180, …) | all doses, flat | composition shift |
| [[Retinoic acid (drug)]] 5 µM |  | 0.848× | -3.7 | 0.014 | 8/47 (PANC-1, C32, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.796×** | -3.5 | 0.026 | 13/46 (SNU-423, HT-29, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.658×** | -3.5 | 0.026 | 16/44 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.806×** | -3.4 | 0.029 | 17/46 (PANC-1, C-33 A, …) | all doses, flat |  |
| [[Fumaric acid (drug)]] 5 µM |  | **0.813×** | -3.1 | 0.065 | 6/47 (SW 1088, HT-29, …) | top dose only | plate-row cell shift |
| [[Pralsetinib (drug)]] 5 µM |  | **0.684×** | -3.1 | 0.065 | 13/45 (A-172, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.818×** | -3.0 | 0.078 | 9/47 (AN3 CA, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14649. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 87.4 | 0 | 14 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0339× (z -22.8) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.107× (z -15.1) |
| [[SW480 (line)]] | alt | 18.1 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 26.0× (z +33.4) | — |
| [[NCI-H2347 (line)]] | alt | 8.83 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 56.8× (z +29.4) | — |
| [[NCI-H460 (line)]] | wt | 16.2 | 6 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +17.9) | [[Ixazomib citrate (drug)]] 5 µM 0.210× (z -10.5) |
| [[SW48 (line)]] | wt | 16.1 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 251× (z +24.4) | — |
| [[A-172 (line)]] | wt | 51.4 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.83× (z +25.9) | [[Selinexor (drug)]] 5 µM 0.374× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 9.56 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.1× (z +15.1) | — |
| [[KATO III (line)]] | alt | 15.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +23.5) | — |
| [[LoVo (line)]] | wt | 7.24 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 105× (z +30.3) | — |
| [[LS 180 (line)]] | wt | 16.3 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +14.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.160× (z -10.7) ⚠ cell-cycle shift, explains ~22% of this change |
| [[NCI-H1573 (line)]] | alt | 26.9 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 68.5× (z +34.4) | — |
| [[PANC-1 (line)]] | alt | 14.5 | 0 | 6 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.198× (z -12.1) |
| [[C-33 A (line)]] | alt | 70.3 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.235× (z -9.2) |
| [[COLO 205 (line)]] | alt | 10.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 273× (z +28.0) | — |
| [[SNU-1 (line)]] | wt | 31.5 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0544× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.104× (z -9.7) |
| [[A549 (line)]] | wt | 9.21 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +16.1) | — |
| [[AsPC-1 (line)]] | alt | 8.72 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 43.6× (z +18.0) | — |
| [[CFPAC-1 (line)]] | alt | 8.24 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.7× (z +20.0) | — |
| [[HepG2_C3A (line)]] | wt | 24.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.5× (z +18.2) | — |
| [[HOP62 (line)]] | alt | 24.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.29× (z +17.0) | — |
| [[HS-578T (line)]] | alt | 38.7 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.84× (z +13.7) | [[Ixazomib citrate (drug)]] 5 µM 0.188× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 16.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +22.2) | — |
| [[A498 (line)]] | wt | 9.25 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.81× (z +13.3) | — |
| [[HCT15 (line)]] | alt | 17.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.1× (z +17.5) | — |
| [[HEC-1-A (line)]] | alt | 31.9 | 3 | 0 | [[Auranofin (drug)]] 5 µM 9.92× (z +14.8) | — |
| [[HT-29 (line)]] | alt | 6.35 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +13.5) | — |
| [[NCI-H2030 (line)]] | alt | 10.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 46.5× (z +22.7) | — |
| [[NCI-H23 (line)]] | alt | 18.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +12.1) | [[Digitoxin (drug)]] 5 µM 0.212× (z -8.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 29.0 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 28.8× (z +22.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.254× (z -9.0) ⚠ cell-cycle shift, explains ~22% of this change |
| [[H4 (line)]] | wt | 34.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.54× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.19× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 12.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.7× (z +18.2) | — |
| [[hTERT-HPNE (line)]] | wt | 9.13 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.96× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 51.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.183× (z -10.9) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 49.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.243× (z -9.0) ⚠ toxic |
| [[SW 900 (line)]] | alt | 14.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 6.06 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.23× (z +11.5) | — |
| [[A-427 (line)]] | wt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +13.8) | — |
| [[J82 (line)]] | alt | 8.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +8.5) | — |
| [[RKO (line)]] | wt | 8.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.92× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +20.6) | — |
| [[AN3 CA (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.65 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14649), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01135]] | +0.69 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[HAS2-AS1]] | +0.64 | +0.62 / +0.53 | both halves | 1e-05 | same gene group |
| [[DPY19L2P2]] | +0.62 | +0.70 / +0.40 | both halves | 5e-05 |  |
| [[AGPAT5]] | +0.62 | +0.52 / +0.61 | both halves | 1e-05 | ⚠ same locus (0.4 kb: neighbours can correlate without regulation) |
| [[SEPTIN7-DT]] | +0.62 | +0.70 / +0.35 | both halves | 1e-04 |  |
| [[MFF-DT]] | +0.61 | +0.65 / +0.39 | both halves | 6e-05 |  |
| [[ZBTB1]] | +0.60 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[ZNF554]] | +0.60 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[CAVIN4]] | +0.59 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[MAD2L1-DT]] | +0.59 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[PPP1R3F]] | +0.59 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[MSANTD3-TMEFF1]] | +0.59 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[SLC30A9]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPST]] | -0.54 | -0.59 / -0.25 | both halves | 4e-04 |  |
| [[CYRIB]] | -0.54 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[LPCAT4]] | -0.53 | -0.61 / -0.25 | both halves | 4e-04 |  |
| [[CDC42SE2]] | -0.53 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[SPTLC2]] | -0.53 | -0.55 / -0.27 | both halves | 3e-04 |  |
| [[RAPGEF5]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[TRAK1]] | -0.52 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[MFSD9]] | -0.52 | -0.51 / -0.32 | both halves | 1e-04 |  |
| [[L2HGDH]] | -0.52 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[DPY30]] | -0.52 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[CAMK2G]] | -0.52 | -0.52 / -0.26 | both halves | 3e-04 |  |
| [[RALGPS1]] | -0.52 | -0.55 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MCPH1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RAPGEF5]] | B | RAPGEF5 activity strengthens MCPH1-AS1's drug response | lines that do not express RAPGEF5 (17) vs lines expressing it (30) | the lines without RAPGEF5 respond 0.65× as strongly (z diff +1.61); strongest at Auranofin 5 µM: 1.58x vs 4.88x (z diff +4.8) | 0.051 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.562). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (11.9, 14.5); signed map (27.4, 2.2). **Vector** length 108, 27.4% of its response variance represented; |z| ≥ 3 in 1,306 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.5 | +16.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.4 | +44.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.8 | +29.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.8 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +17.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +6.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[Roxadustat (drug)]] 5 µM |  | +1.3 | +0.9 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.9 | -11.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.1 | +7.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.1 | +7.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.6 | -10.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -8.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | -0.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.5 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | MCPH1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8p23.1 — chr8:6,617,310-6,708,224 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51655](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51655) · Entrez [100507530](https://www.ncbi.nlm.nih.gov/gene/100507530) · Ensembl [ENSG00000249898](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249898)

## Data

Gene col 14649: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14649); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14649, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14649]; `tensor/DDL_lfc|DDL_z.npy` [14649]; `embed/gene_vectors.npy` [14649]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14649 or target_col == 14649). Every well: [[MCPH1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCPH1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
