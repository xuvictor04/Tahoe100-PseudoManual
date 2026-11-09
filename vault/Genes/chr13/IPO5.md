---
symbol: "IPO5"
type: "gene"
col: 774
ensembl_id: "ENSG00000065150"
name: "importin 5"
location: "13q32.2"
module: 20
arm: "+"
pooled_cpm: 94.87
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# IPO5

*importin 5* — 13q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.12× (z +16.9, q 0e+00, up in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.74× (z +8.5, q 2e-15, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 0.620× (z -5.3, q 7e-05, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRKDC]] (+0.82, fdr 7e-06), [[MTHFD1]] (+0.76, fdr 7e-06), [[NONO]] (+0.75, fdr 7e-06); moves opposite to [[SMIM26]] (-0.75, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[MRPS18C]] (-0.73, fdr 7e-06), [[INAFM1]] (-0.73, fdr 7e-06), [[IFI27L2]] (-0.72, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MSX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 774.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.12×** | +16.9 | 0e+00 | 44/44 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.90×** | +16.4 | 0e+00 | 48/49 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.26×** | +11.2 | 6e-27 | 45/45 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +8.5 | 2e-15 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +8.5 | 3e-15 | 42/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +6.1 | 9e-08 | 39/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.11×** | +6.0 | 2e-07 | 41/48 (RKO, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.44×** | +5.6 | 1e-06 | 40/48 (NCI-H460, HT-29, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.01×** | +5.6 | 1e-06 | 41/49 (RKO, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +4.8 | 9e-05 | 32/48 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.36×** | +4.8 | 9e-05 | 31/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +4.5 | 4e-04 | 36/48 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.32×** | +4.3 | 7e-04 | 28/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.32×** | +4.1 | 0.002 | 25/50 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.1 | 0.002 | 0/50 | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.58×** | +3.7 | 0.008 | 23/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.010 | 25/48 (MIA PaCa-2, SHP-77, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.48×** | +3.2 | 0.040 | 21/48 (NCI-H1792, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.059 | 20/49 (CFPAC-1, H4, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.31×** | +2.9 | 0.076 | 16/48 (A498, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.24×** | +2.9 | 0.079 | 18/48 (HepG2/C3A, A498, …) | inconsistent across doses | position effect removed |
| [[Erlotinib (drug)]] 5 µM |  | **1.22×** | +2.9 | 0.089 | 15/47 (A-172, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.22×** | +2.9 | 0.089 | 20/48 (HT-29, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 774.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.620×** | -5.3 | 7e-05 | 36/48 (SW480, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.813×** | -4.6 | 0.001 | 30/48 (RKO, J82, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.773×** | -3.8 | 0.023 | 30/47 (A549, C-33 A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.841× | -3.7 | 0.031 | 23/49 (SW480, HEC-1-A, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.792×** | -3.6 | 0.031 | 25/49 (SW480, LS 180, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.739×** | -3.4 | 0.074 | 19/48 (LS 180, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.815× | -3.2 | 0.12 | 22/48 (HS-578T, SW48, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.817× | -3.1 | 0.12 | 22/48 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.819× | -3.1 | 0.12 | 20/47 (NCI-H661, A-427, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.763× | -3.0 | 0.15 | 16/48 (CHP-212, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 774. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 83.4 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +11.7) | — |
| [[LoVo (line)]] | wt | 83.9 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +17.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +9.3) | — |
| [[A498 (line)]] | wt | 79.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +14.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 70.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.92× (z +12.9) ⚠ toxic; transcription drop | [[Thymol (drug)]] 0.5 µM 0.348× (z -8.9) |
| [[KATO III (line)]] | alt | 65.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 82.5 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 64.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +9.5) | — |
| [[A549 (line)]] | wt | 87.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.53× (z +13.9) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 50.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 34.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 94.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +13.4) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 90.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +12.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 85.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.58× (z +13.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 56.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 60.2 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 77.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +14.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 83.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +10.6) | — |
| [[SW480 (line)]] | alt | 197 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.89× (z +15.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 89.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.04× (z +13.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 59.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +12.9) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 54.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.77× (z +12.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 103 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 71.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +10.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 133 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +10.1) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 78.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 93.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 43.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +12.9) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 119 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +12.9) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 57.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 179 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 95.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.67× (z +9.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 98.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +10.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 97.8 | 0 | 1 | — | [[Bimiralisib (drug)]] 0.5 µM 0.0540× (z -11.9) |
| [[H4 (line)]] | wt | 56.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.23× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 119 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +11.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 141 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H596 (line)]] | alt | 98.9 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.166× (z -9.6) |
| [[RKO (line)]] | wt | 148 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.62× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 190 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.26× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 50.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 63.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +8.5) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 185 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 136 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 774), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | +0.82 | +0.83 / +0.84 | both halves | 7e-06 |  |
| [[MTHFD1]] | +0.76 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[NONO]] | +0.75 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[LRPPRC]] | +0.74 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[PAICS]] | +0.74 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[TXNDC5]] | +0.74 | +0.59 / +0.80 | both halves | 7e-06 |  |
| [[CAPRIN1]] | +0.74 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[RPSA]] | +0.73 | +0.63 / +0.76 | both halves | 7e-06 | pathway: Influenza Infection |
| [[DHFR]] | +0.72 | +0.58 / +0.76 | both halves | 7e-06 |  |
| [[DARS2]] | +0.71 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[IPO7]] | +0.71 | +0.74 / +0.67 | both halves | 7e-06 | same gene group; STRING 884 |
| [[EIF4H]] | +0.71 | +0.58 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | -0.75 | -0.65 / -0.78 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS18C]] | -0.73 | -0.63 / -0.74 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.73 | -0.67 / -0.74 | both halves | 7e-06 |  |
| [[KRT10]] ⚠ | -0.72 | -0.67 / -0.77 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[IFI27L2]] | -0.72 | -0.50 / -0.80 | both halves | 1e-05 |  |
| [[SCAND1]] | -0.72 | -0.56 / -0.77 | both halves | 1e-05 |  |
| [[MED19]] | -0.71 | -0.57 / -0.74 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | -0.71 | -0.54 / -0.76 | both halves | 1e-05 | pathway: Influenza Infection; ⚠ in the vector space only through flagged drug-doses |
| [[MTHFR]] | -0.70 | -0.68 / -0.73 | both halves | 7e-06 |  |
| [[C19orf81]] | -0.70 | -0.50 / -0.77 | both halves | 1e-05 |  |
| [[TMEM258]] | -0.70 | -0.54 / -0.72 | both halves | 1e-05 |  |
| [[TRAPPC2B]] | -0.69 | -0.56 / -0.73 | both halves | 1e-05 |  |
| [[LAMTOR5]] | -0.68 | -0.49 / -0.76 | both halves | 1e-05 |  |
| [[ZNF503]] | -0.68 | -0.56 / -0.72 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.68 | -0.62 / -0.73 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSX2]] | B | MSX2 activity lowers IPO5's level | lines that do not express MSX2 (11) vs lines expressing it (39) | 1.27× higher at baseline in the lines without MSX2 | 0.033 | ⚠ within organs, on part of the lines; also absent: CD9, ABCC3, CDCP1 |
| [[PTGFRN]] | B | PTGFRN activity lowers IPO5's level | lines that do not express PTGFRN (8) vs lines expressing it (42) | 1.19× higher at baseline in the lines without PTGFRN | 0.051 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |
| [[CDKN1C]] | B | CDKN1C activity lowers IPO5's level | lines that do not express CDKN1C (8) vs lines expressing it (42) | 1.21× higher at baseline in the lines without CDKN1C | 0.097 | ⚠ within organs, on part of the lines; also absent: MAP3K9, CARD10, TESMIN; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.793). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.7, -31.0); signed map (-19.9, -44.7). **Vector** length 130, 45.7% of its response variance represented; |z| ≥ 3 in 1,212 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cap-dependent Translation Initiation* (reactome, mean cos +0.52 to 12); *Eukaryotic Translation Initiation* (reactome, mean cos +0.52 to 12); *L13a-mediated translational silencing of Ceruloplasmin expression* (reactome, mean cos +0.54 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.2 | +16.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.5 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.1 | +16.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +1.9 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +3.0 | +2.9 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +3.0 | +2.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | +2.8 | +2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +2.8 | +1.9 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -5.3 | -5.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.6 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +2.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +0.1 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -3.3 | -2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.3 | -3.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | importin 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.2 — chr13:97,953,658-98,024,296 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IMB3, MGC2068, PSE1; previously KPNB3, RANBP5 |
| Gene groups (HGNC) | Importins; TOG domain containing |
| Reactome | 4 pathways, smallest: vRNP Assembly; Influenza Viral RNA Transcription and Replication; Influenza Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [O00410](https://www.uniprot.org/uniprotkb/O00410) (Importin-5):

> Functions in nuclear protein import as nuclear transport receptor. Serves as receptor for nuclear localization signals (NLS) in cargo substrates. Is thought to mediate docking of the importin/substrate complex to the nuclear pore complex (NPC) through binding to nucleoporin and the complex is subsequently translocated through the pore by an energy requiring, Ran-dependent mechanism. At the nucleoplasmic side of the NPC, Ran binds to the importin, the importin/substrate complex dissociates and …

**Summary**, from NCBI Gene [3843](https://www.ncbi.nlm.nih.gov/gene/3843):

> Nucleocytoplasmic transport, a signal- and energy-dependent process, takes place through nuclear pore complexes embedded in the nuclear envelope. The import of proteins containing a nuclear localization signal (NLS) requires the NLS import receptor, a heterodimer of importin alpha and beta subunits also known as karyopherins. Importin alpha binds the NLS-containing cargo in the cytoplasm and importin beta docks the complex at the cytoplasmic side of the nuclear pore complex. In the presence of …

**Accessions** — [HGNC:6402](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6402) · Entrez [3843](https://www.ncbi.nlm.nih.gov/gene/3843) · UniProt [O00410](https://www.uniprot.org/uniprotkb/O00410) · Ensembl [ENSG00000065150](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065150)

## Data

Gene col 774: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 774); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 774, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 774]; `tensor/DDL_lfc|DDL_z.npy` [774]; `embed/gene_vectors.npy` [774]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 774 or target_col == 774). Every well: [[IPO5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IPO5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
