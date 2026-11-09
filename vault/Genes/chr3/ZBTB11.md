---
symbol: "ZBTB11"
type: "gene"
col: 827
ensembl_id: "ENSG00000066422"
name: "zinc finger and BTB domain containing 11"
location: "3q12.3"
module: 15
arm: "+"
pooled_cpm: 79.27
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 4
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ZBTB11

*zinc finger and BTB domain containing 11* — 3q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.58× (z +22.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.615× (z -7.9, q 1e-12, down in 32 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.777× (z -4.1, q 0.008, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (KATO III 0.207×, J82 0.328×, NCI-H2347 0.464×, SW1417 0.411×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 7 lines (H4 0.236×, A498 0.351×, J82 0.393×, SK-MEL-2 0.389×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.254×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Atazanavir (sulfate) (drug)]] 5 µM in 1 line (NCI-H596 0.191×).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALG11]] (+0.63, fdr 1e-05), [[KIAA0753]] (+0.58, fdr 4e-05), [[TICAM2]] (+0.58, fdr 3e-05); moves opposite to [[NBDY]] (-0.56, fdr 2e-04), [[SAAL1]] (-0.54, fdr 5e-05), [[RAD54L2]] (-0.52, fdr 3e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 827.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.58×** | +22.6 | 0e+00 | 48/48 (NCI-H1792, C32, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.54×** | +22.3 | 0e+00 | 48/49 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.65×** | +21.9 | 0e+00 | 48/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.74×** | +17.0 | 0e+00 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.67×** | +16.6 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.49×** | +15.4 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.20×** | +14.6 | 0e+00 | 47/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.31×** | +13.6 | 3e-40 | 45/48 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +13.2 | 5e-38 | 46/50 (HOP62, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.72×** | +11.6 | 2e-29 | 46/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +9.8 | 4e-21 | 43/48 (SW480, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +9.6 | 2e-20 | 36/48 (HOP62, NCI-H2347, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +8.9 | 3e-17 | 43/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.66×** | +8.5 | 6e-16 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +8.5 | 7e-16 | 38/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +6.4 | 4e-09 | 36/48 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 827.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (KATO III 0.207×, J82 0.328×, NCI-H2347 0.464×, SW1417 0.411×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 7 lines (H4 0.236×, A498 0.351×, J82 0.393×, SK-MEL-2 0.389×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.254×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Atazanavir (sulfate) (drug)]] 5 µM in 1 line (NCI-H596 0.191×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.615×** | -7.9 | 1e-12 | 32/44 (KATO III, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.699×** | -6.1 | 4e-07 | 30/49 (H4, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.777×** | -4.1 | 0.008 | 27/48 (NCI-H2347, J82, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.789×** | -3.7 | 0.029 | 27/47 (hTERT-HPNE, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | 0.879× | -3.1 | 0.23 | 16/48 (NCI-H1573, HS-578T, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 827. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 72.5 | 17 (5 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.30× (z +23.4) | [[Dinaciclib (drug)]] 5 µM 0.475× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 59.5 | 16 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +21.5) | — |
| [[PANC-1 (line)]] | alt | 101 | 12 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +21.3) | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -9.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 99.1 | 11 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -10.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 69.5 | 11 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +23.6) | [[Dinaciclib (drug)]] 5 µM 0.501× (z -8.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 69.2 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +19.7) | — |
| [[RKO (line)]] | wt | 74.1 | 12 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.74× (z +16.0) | — |
| [[LoVo (line)]] | wt | 64.3 | 11 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.55× (z +24.5) | — |
| [[NCI-H2347 (line)]] | alt | 89.2 | 10 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +23.1) | [[Dinaciclib (drug)]] 5 µM 0.464× (z -10.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 96.3 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +18.0) | — |
| [[BT-474 (line)]] | alt | 81.2 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.39× (z +18.4) | — |
| [[KATO III (line)]] | alt | 73.3 | 8 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.57× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 84.8 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +18.6) | [[Dinaciclib (drug)]] 5 µM 0.367× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 61.1 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +22.6) | — |
| [[Panc 03.27 (line)]] | alt | 69.7 | 9 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +19.5) | — |
| [[LS 180 (line)]] | wt | 97.0 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.65× (z +19.8) | — |
| [[NCI-H23 (line)]] | alt | 82.0 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +16.3) | — |
| [[AsPC-1 (line)]] | alt | 67.5 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +21.4) | — |
| [[COLO 205 (line)]] | alt | 66.6 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +15.7) | — |
| [[HS-578T (line)]] | alt | 99.1 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +16.7) | — |
| [[HT-29 (line)]] | alt | 97.2 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.12× (z +15.0) | — |
| [[J82 (line)]] | alt | 93.3 | 4 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +17.4) | [[Dinaciclib (drug)]] 5 µM 0.328× (z -12.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 72.5 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +15.1) | — |
| [[SHP-77 (line)]] | alt | 99.8 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +13.0) | — |
| [[SK-MEL-2 (line)]] | alt | 83.9 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +17.8) | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 92.8 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +15.4) | — |
| [[SW 900 (line)]] | alt | 75.2 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.81× (z +11.7) | — |
| [[A-427 (line)]] | wt | 118 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -9.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 49.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +22.1) | — |
| [[hTERT-HPNE (line)]] | wt | 76.7 | 5 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.362× (z -8.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 95.8 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.24× (z +14.7) | — |
| [[A-172 (line)]] | wt | 74.0 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.442× (z -9.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 52.5 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +19.7) | — |
| [[HepG2_C3A (line)]] | wt | 43.8 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.11× (z +12.7) | — |
| [[Hs 766T (line)]] | wt | 56.7 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 46.4 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +15.4) | — |
| [[A549 (line)]] | wt | 76.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +14.1) | — |
| [[C-33 A (line)]] | alt | 75.3 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.61× (z +10.8) | — |
| [[H4 (line)]] | wt | 94.2 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -11.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 101 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 57.0 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 80.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +12.1) | — |
| [[HCT15 (line)]] | alt | 125 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.69× (z +11.8) | — |
| [[AN3 CA (line)]] | alt | 70.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 85.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.58× (z +8.6) | — |
| [[NCI-H596 (line)]] | alt | 78.6 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.191× (z -8.7) |
| [[NCI-H2122 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 97.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 827), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG11]] | +0.63 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[KIAA0753]] | +0.58 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[TICAM2]] | +0.58 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[LEMD3]] | +0.57 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[KIAA2026]] | +0.56 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[LEPR]] | +0.56 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[EMC1-AS1]] | +0.54 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[PRDM10]] | +0.53 | +0.30 / +0.39 | both halves | 2e-04 | same gene group |
| [[EMSY]] | +0.52 | +0.29 / +0.54 | both halves | 2e-04 |  |
| [[LINC00159]] | +0.52 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[KCTD1]] | +0.51 | +0.35 / +0.35 | both halves | 1e-04 | same gene group |
| [[PMS2P4-1]] | +0.51 | +0.39 / +0.43 | both halves | 5e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBDY]] | -0.56 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[SAAL1]] | -0.54 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[RAD54L2]] | -0.52 | -0.29 / -0.59 | both halves | 3e-04 |  |
| [[MOCS1]] | -0.52 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[COMMD2]] | -0.50 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[SSB]] | -0.50 | -0.22 / -0.53 | both halves | 6e-04 |  |
| [[CAMK1]] | -0.50 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[FKTN]] | -0.50 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[ZDHHC18]] | -0.49 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[UBE2E2]] | -0.48 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[NEK3]] | -0.48 | -0.25 / -0.53 | both halves | 4e-04 |  |
| [[DDX19B]] | -0.48 | -0.32 / -0.39 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZBTB11's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.426). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-4.7, 19.0); signed map (6.9, 2.1). **Vector** length 79.3, 25.0% of its response variance represented; |z| ≥ 3 in 1,535 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +22.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +13.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +13.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +9.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.0 | +0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +1.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.1 | +8.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.3 | +22.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | -4.2 | -3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.0 | -6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.8 | -7.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.9 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.1 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.3 — chr3:101,648,889-101,677,135 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF-U69274, ZNF913 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing; Integrase like retrotransposon derived |
| Matched by | ensembl_id |

**Function**, from UniProt [O95625](https://www.uniprot.org/uniprotkb/O95625) (Zinc finger and BTB domain-containing protein 11):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [27107](https://www.ncbi.nlm.nih.gov/gene/27107):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of DNA-templated transcription. Located in nucleoplasm. Implicated in autosomal recessive intellectual developmental disorder 69. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16740](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16740) · Entrez [27107](https://www.ncbi.nlm.nih.gov/gene/27107) · UniProt [O95625](https://www.uniprot.org/uniprotkb/O95625) · Ensembl [ENSG00000066422](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066422)

## Data

Gene col 827: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 827); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 827, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 827]; `tensor/DDL_lfc|DDL_z.npy` [827]; `embed/gene_vectors.npy` [827]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 827 or target_col == 827). Every well: [[ZBTB11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
