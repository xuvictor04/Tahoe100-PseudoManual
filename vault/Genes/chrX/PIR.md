---
symbol: "PIR"
type: "gene"
col: 1513
ensembl_id: "ENSG00000087842"
name: "pirin"
location: "Xp22.2"
module: 117
arm: "+"
pooled_cpm: 37.05
n_lines_expressing: 40
n_dd_up: 41
n_dd_down: 24
n_dd_up_clean: 36
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 15
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# PIR

*pirin* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 4.31× (z +22.9, q 0e+00, up in 36 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.455× (z -17.5, q 0e+00, down in 32 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VEGFD]] (+0.88, fdr 7e-06, ⚠ same locus), [[ME1]] (+0.70, fdr 7e-06), [[CYP4F11]] (+0.70, fdr 7e-06), [[NMRAL2P]] (+0.68, fdr 7e-06); moves opposite to [[SDC4]] (-0.48, fdr 2e-05), [[CHCHD7]] (-0.48, fdr 5e-05), [[STMN3]] (-0.47, fdr 4e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 15 go from it, the strongest it → [[VWA8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1513.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **4.31×** | +22.9 | 0e+00 | 36/37 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **4.33×** | +21.7 | 0e+00 | 37/38 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.90×** | +21.3 | 0e+00 | 35/37 (NCI-H1792, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.99×** | +10.8 | 6e-25 | 26/37 (LS 180, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.47×** | +10.1 | 5e-22 | 31/38 (NCI-H1792, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 0.5 µM |  | **1.74×** | +8.7 | 4e-16 | 26/38 (LoVo, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +8.0 | 7e-14 | 23/37 (KATO III, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.88×** | +7.7 | 9e-13 | 27/33 (LS 180, J82, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.62×** | +7.2 | 3e-11 | 23/37 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.45×** | +7.0 | 2e-10 | 22/38 (C32, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.53×** | +6.7 | 1e-09 | 19/38 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.50×** | +6.3 | 1e-08 | 18/38 (SK-MEL-2, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.33×** | +6.2 | 2e-08 | 16/38 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +5.9 | 1e-07 | 16/38 (SK-MEL-2, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.55×** | +5.8 | 3e-07 | 21/38 (PANC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.46×** | +5.7 | 4e-07 | 21/37 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.36×** | +5.4 | 2e-06 | 16/38 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1513.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.455×** | -17.5 | 0e+00 | 32/38 (SHP-77, A498, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.474×** | -11.3 | 5e-27 | 27/38 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.552×** | -9.3 | 2e-18 | 24/38 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -8.7 | 4e-16 | 26/38 (KATO III, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.640×** | -7.0 | 3e-10 | 28/38 (A498, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.414×** | -6.4 | 1e-08 | 24/38 (A-427, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.666×** | -6.4 | 2e-08 | 20/37 (SK-MEL-2, SW480, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.712×** | -5.1 | 2e-05 | 17/37 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.723×** | -5.1 | 2e-05 | 17/36 (PANC-1, SW480, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.744×** | -4.6 | 2e-04 | 18/37 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.743×** | -4.5 | 4e-04 | 16/38 (PANC-1, Hs 766T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.760×** | -4.3 | 8e-04 | 19/37 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **0.765×** | -4.2 | 0.001 | 13/38 (KATO III, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.768×** | -4.1 | 0.001 | 19/37 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.696×** | -4.1 | 0.002 | 15/36 (SW 900, C32, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.834× | -4.0 | 0.002 | 19/38 (C32, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.839× | -3.9 | 0.003 | 17/38 (SW480, KATO III, …) | rises with dose |  |
| [[APTO-253 (drug)]] 5 µM |  | **0.608×** | -3.6 | 0.008 | 13/38 (Hs 766T, NCI-H460, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1513. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 46.3 | 3 | 11 (5 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.20× (z +14.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -20.1) |
| [[KATO III (line)]] | alt | 118 | 2 (1 ⚠) | 9 (5 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.19× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -17.8) |
| [[PANC-1 (line)]] | alt | 43.8 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -16.3) |
| [[COLO 205 (line)]] | alt | 20.9 | 4 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 15.2× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 14.6 | 4 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 8.34× (z +13.5) | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -8.9) |
| [[LS 180 (line)]] | wt | 20.7 | 4 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 7.88× (z +13.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -9.6) |
| [[A-172 (line)]] | wt | 13.1 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 11.6× (z +13.1) | — |
| [[A549 (line)]] | wt | 27.5 | 3 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 4.20× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.3) |
| [[HT-29 (line)]] | alt | 31.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -15.7) |
| [[LoVo (line)]] | wt | 19.4 | 4 | 0 | [[Bortezomib (drug)]] 0.05 µM 9.72× (z +14.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 12.0 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 8.76× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 36.7 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 9.75× (z +14.4) | — |
| [[A-427 (line)]] | wt | 72.2 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.369× (z -10.6) |
| [[A498 (line)]] | wt | 26.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -18.0) |
| [[BT-474 (line)]] | alt | 14.1 | 2 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 7.62× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -9.1) |
| [[C32 (line)]] | wt | 43.9 | 3 | 0 | [[Auranofin (drug)]] 5 µM 6.26× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 13.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.32× (z +10.5) | — |
| [[J82 (line)]] | alt | 23.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.40× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 9.47 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 10.9× (z +10.5) | — |
| [[SNU-1 (line)]] | wt | 67.7 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0441× (z -20.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.330× (z -10.5) |
| [[SNU-423 (line)]] | alt | 14.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 10.2× (z +11.6) | — |
| [[AN3 CA (line)]] | alt | 74.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -9.8) |
| [[Hs 766T (line)]] | wt | 111 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 120 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.19× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.193× (z -11.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 114 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -15.8) |
| [[H4 (line)]] | wt | 27.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 12.5 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0968× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 95.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 17.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.07× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 36.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -19.0) |
| [[SK-MEL-2 (line)]] | alt | 35.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.31× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 15.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -9.0) |
| [[SW48 (line)]] | wt | 65.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0963× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 5.18 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.09 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.18 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.42 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.40 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.54 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.94 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.60 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.58 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1513), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VEGFD]] | +0.88 | +0.88 / +0.85 | both halves | 7e-06 | STRING 459; ⚠ same locus (0.4 kb, same strand: neighbours can correlate without regulation) |
| [[ME1]] | +0.70 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[CYP4F11]] | +0.70 | +0.66 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[NMRAL2P]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[AKR1C1]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[GCLM]] | +0.67 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[SLC7A11]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[PSMA1]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[GSR]] | +0.65 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[EGF]] | +0.65 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[NMRAL2P-1]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[ABCC2]] | +0.62 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[NXPE3]] | +0.61 | +0.64 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDC4]] | -0.48 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[CHCHD7]] | -0.48 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[STMN3]] | -0.47 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[NOTCH2NLA]] | -0.47 | -0.51 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers PIR's level | compounds that target MAP2K1: 4 of 4 raise it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 7.6% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds |
| [[VEGFD]] | C | VEGFD activity raises PIR's level | lines that do not express VEGFD (13) vs lines expressing it (37) | 4.33× lower at baseline in the lines without VEGFD | 2e-04 | ⚠ within organs, on part of the lines; also absent: PIR, ELMO1; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 14, C 1. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VWA8]] | B | PIR activity raises VWA8's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.39× lower at baseline in the lines without PIR | 0.008 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |
| [[GSEC]] | B | PIR activity raises GSEC's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.24× lower at baseline in the lines without PIR | 0.026 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |
| [[TSEN15]] | B | PIR activity raises TSEN15's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.55× lower at baseline in the lines without PIR | 0.040 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |
| [[TRIM16]] | B | PIR activity raises TRIM16's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.47× lower at baseline in the lines without PIR | 0.042 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |
| [[HSD17B4]] | B | PIR activity raises HSD17B4's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.44× lower at baseline in the lines without PIR | 0.042 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |
| [[DTWD2]] | B | PIR activity raises DTWD2's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.60× lower at baseline in the lines without PIR | 0.042 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |
| [[IDH1]] | B | PIR activity raises IDH1's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.50× lower at baseline in the lines without PIR | 0.054 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |
| [[TRIM16L-1]] | B | PIR activity raises TRIM16L-1's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.57× lower at baseline in the lines without PIR | 0.068 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |
| [[PTPN4]] | B | PIR activity raises PTPN4's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.29× lower at baseline in the lines without PIR | 0.074 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |
| [[IDE]] | B | PIR activity raises IDE's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.39× lower at baseline in the lines without PIR | 0.076 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |
| [[FAM217B]] | B | PIR activity raises FAM217B's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.33× lower at baseline in the lines without PIR | 0.078 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |
| [[CYP39A1]] | B | PIR activity raises CYP39A1's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.54× lower at baseline in the lines without PIR | 0.089 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.803). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.4, 48.1); signed map (51.4, -10.0). **Vector** length 131, 37.7% of its response variance represented; |z| ≥ 3 in 1,252 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NRF2* (control, mean cos +0.61 to 8); *Nuclear events mediated by NFE2L2* (reactome, mean cos +0.62 to 7); *KEAP1-NFE2L2 pathway* (reactome, mean cos +0.62 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +12.4 | +21.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +11.3 | +21.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +11.1 | +22.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +7.2 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.1 | +10.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.3 | +5.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.1 | +7.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.1 | +10.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.3 | -6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -17.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -3.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.7 | -7.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.7 | -11.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | -4.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -3.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.2 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | pirin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:15,384,799-15,493,564 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Oxygenases |
| Reactome | 2 pathways, smallest: Digestion; Digestion and absorption |
| Matched by | ensembl_id |

**Function**, from UniProt [O00625](https://www.uniprot.org/uniprotkb/O00625) (Pirin):

> Transcriptional coregulator of NF-kappa-B which facilitates binding of NF-kappa-B proteins to target kappa-B genes in a redox-state-dependent manner. May be required for efficient terminal myeloid maturation of hematopoietic cells. Has quercetin 2,3-dioxygenase activity (in vitro).

**Summary**, from NCBI Gene [8544](https://www.ncbi.nlm.nih.gov/gene/8544):

> This gene encodes a member of the cupin superfamily. The encoded protein is an Fe(II)-containing nuclear protein expressed in all tissues of the body and concentrated within dot-like subnuclear structures. Interactions with nuclear factor I/CCAAT box transcription factor as well as B cell lymphoma 3-encoded oncoprotein suggest the encoded protein may act as a transcriptional cofactor and be involved in the regulation of DNA transcription and replication. Alternatively spliced transcript …

**Accessions** — [HGNC:30048](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30048) · Entrez [8544](https://www.ncbi.nlm.nih.gov/gene/8544) · UniProt [O00625](https://www.uniprot.org/uniprotkb/O00625) · Ensembl [ENSG00000087842](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087842)

## Data

Gene col 1513: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1513); `tables/drug_effects.parquet` (75 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1513, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1513]; `tensor/DDL_lfc|DDL_z.npy` [1513]; `embed/gene_vectors.npy` [1513]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1513 or target_col == 1513). Every well: [[PIR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
