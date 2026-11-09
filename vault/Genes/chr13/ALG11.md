---
symbol: "ALG11"
type: "gene"
col: 14833
ensembl_id: "ENSG00000253710"
name: "ALG11 alpha-1,2-mannosyltransferase"
location: "13q14.3"
module: 41
arm: "+"
pooled_cpm: 64.78
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# ALG11

*ALG11 alpha-1,2-mannosyltransferase* — 13q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.41× (z +50.8, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.942× (z -5.7, q 5e-06, down in 0 of 49 measured lines) ⚠ position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H23 0.229×, A498 0.366×, NCI-H1573 0.333×, SNU-1 0.220×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.271×, COLO 205 0.259×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (SNU-1 0.347×, LoVo 0.465×; ⚠ toxic); [[Monocrotaline (drug)]] 0.05 µM in 1 line (AN3 CA 0.160×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCGF3-AS1]] (+0.66, fdr 1e-05), [[TICAM2]] (+0.65, fdr 1e-05), [[GOLGA5]] (+0.64, fdr 1e-05); moves opposite to [[TRAK1]] (-0.53, fdr 5e-05), [[SOAT1]] (-0.52, fdr 5e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14833.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.41×** | +50.8 | 0e+00 | 49/49 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +20.3 | 0e+00 | 41/50 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +17.3 | 0e+00 | 37/48 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +15.7 | 0e+00 | 33/48 (HOP62, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +15.0 | 0e+00 | 46/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +11.5 | 1e-28 | 35/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +11.5 | 1e-28 | 43/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +11.5 | 1e-28 | 36/47 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +10.0 | 1e-21 | 31/48 (HCT15, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +8.7 | 2e-16 | 37/48 (SW480, BT-474, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.13× | +5.1 | 2e-05 | 20/48 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.18× | +5.0 | 3e-05 | 13/48 (BT-474, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.8 | 8e-05 | 18/44 (NCI-H2347, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.17× | +4.7 | 1e-04 | 16/48 (COLO 205, SW480, …) | rises with dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.12× | +4.6 | 2e-04 | 6/48 (HEC-1-A, A549, …) | rises with dose |  |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | 1.10× | +3.9 | 0.003 | 4/48 (NCI-H23, LOX-IMVI, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.14× | +3.8 | 0.004 | 4/47 (SW1417, NCI-H23, …) | two highest doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.09× | +3.7 | 0.005 | 9/48 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.13× | +3.6 | 0.007 | 8/49 (A-172, HOP62, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.027 | 7/48 (NCI-H460, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (mesylate) (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.036 | 6/48 (J82, A-427, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14833.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H23 0.229×, A498 0.366×, NCI-H1573 0.333×, SNU-1 0.220×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.271×, COLO 205 0.259×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (SNU-1 0.347×, LoVo 0.465×; ⚠ toxic); [[Monocrotaline (drug)]] 0.05 µM in 1 line (AN3 CA 0.160×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -5.7 | 5e-06 | 0/49 | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.818×** | -5.6 | 5e-06 | 22/47 (SNU-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.832×** | -5.3 | 1e-05 | 23/49 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.826×** | -5.3 | 1e-05 | 22/42 (NCI-H23, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.871× | -4.0 | 0.007 | 14/48 (hTERT-HPNE, PANC-1, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.849× | -3.4 | 0.064 | 16/48 (COLO 205, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14833. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 41.9 | 7 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.28× (z +23.8) | — |
| [[SW480 (line)]] | alt | 86.9 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +31.6) | — |
| [[LOX-IMVI (line)]] | wt | 40.1 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.20× (z +23.0) | — |
| [[BT-474 (line)]] | alt | 55.6 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.03× (z +23.7) | — |
| [[NCI-H1573 (line)]] | alt | 159 | 3 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -17.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 64.0 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -15.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 73.2 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 62.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.38× (z +26.3) | — |
| [[HEC-1-A (line)]] | alt | 77.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +28.8) | — |
| [[HOP62 (line)]] | alt | 68.4 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +25.2) | — |
| [[Hs 766T (line)]] | wt | 75.4 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +18.3) | — |
| [[Panc 03.27 (line)]] | alt | 80.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +26.4) | — |
| [[SW1417 (line)]] | alt | 52.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.71× (z +28.9) | — |
| [[C32 (line)]] | wt | 51.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +14.1) | — |
| [[HS-578T (line)]] | alt | 50.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.92× (z +21.0) | — |
| [[LoVo (line)]] | wt | 74.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.440× (z -9.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 65.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +19.3) | — |
| [[RPMI-7951 (line)]] | alt | 74.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +19.3) | — |
| [[SNU-423 (line)]] | alt | 38.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.84× (z +22.6) | — |
| [[SW 900 (line)]] | alt | 65.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +23.3) | — |
| [[A498 (line)]] | wt | 103 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.366× (z -13.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 63.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +10.5) | [[Monocrotaline (drug)]] 0.05 µM 0.160× (z -9.8) |
| [[C-33 A (line)]] | alt | 39.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +12.6) | — |
| [[COLO 205 (line)]] | alt | 199 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +24.8) | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -15.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 100 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +17.2) | — |
| [[NCI-H2030 (line)]] | alt | 29.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +15.6) | — |
| [[NCI-H2347 (line)]] | alt | 39.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +19.8) | — |
| [[NCI-H460 (line)]] | wt | 48.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +17.0) | — |
| [[PANC-1 (line)]] | alt | 53.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +26.8) | — |
| [[SK-MEL-2 (line)]] | alt | 39.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +18.6) | — |
| [[A549 (line)]] | wt | 46.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +12.4) | — |
| [[AsPC-1 (line)]] | alt | 36.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.71× (z +22.7) | — |
| [[CFPAC-1 (line)]] | alt | 36.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.57× (z +24.1) | — |
| [[CHP-212 (line)]] | wt | 93.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +10.9) | — |
| [[H4 (line)]] | wt | 54.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -9.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 76.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +12.3) | — |
| [[HepG2_C3A (line)]] | wt | 46.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +16.2) | — |
| [[J82 (line)]] | alt | 71.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +22.0) | — |
| [[KATO III (line)]] | alt | 101 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +17.8) | — |
| [[LS 180 (line)]] | wt | 68.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +15.5) | — |
| [[NCI-H1792 (line)]] | alt | 31.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +13.6) | — |
| [[NCI-H661 (line)]] | alt | 115 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 46.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +18.1) | — |
| [[SW48 (line)]] | wt | 47.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +13.3) | — |
| [[A-427 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 67.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14833), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCGF3-AS1]] | +0.66 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[TICAM2]] | +0.65 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[GOLGA5]] | +0.64 | +0.49 / +0.73 | both halves | 1e-05 |  |
| [[GOSR2]] | +0.63 | +0.53 / +0.66 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[ZBTB11]] | +0.63 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[BET1]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[MED4]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[AKAP17A]] | +0.61 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[COPB2]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation; STRING 427 |
| [[SLC33A1]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[PLPP5]] | +0.58 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[SPTY2D1]] | +0.58 | +0.49 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAK1]] | -0.53 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[SOAT1]] | -0.52 | -0.39 / -0.47 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ALG11's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.555). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (7.4, -37.5); signed map (0.7, 3.2). **Vector** length 101, 25.3% of its response variance represented; |z| ≥ 3 in 1,016 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +50.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +17.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +20.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +15.7 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.5 | +3.0 |
|  | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +2.3 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +1.4 | +1.1 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.8 | -5.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.3 | -5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -5.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.9 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | +0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.0 | -4.0 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ALG11 alpha-1,2-mannosyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.3 — chr13:52,012,391-52,079,232 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0266, CDG1P |
| Gene groups (HGNC) | Glycosyl transferases group 1 domain containing |
| Reactome | 5 pathways, smallest: Diseases associated with N-glycosylation of proteins; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein; Diseases of glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2TAA5](https://www.uniprot.org/uniprotkb/Q2TAA5) (GDP-Man:Man(3)GlcNAc(2)-PP-Dol alpha-1,2-mannosyltransferase):

> GDP-Man:Man(3)GlcNAc(2)-PP-Dol alpha-1,2-mannosyltransferase that operates in the biosynthetic pathway of dolichol-linked oligosaccharides, the glycan precursors employed in protein asparagine (N)-glycosylation. The assembly of dolichol-linked oligosaccharides begins on the cytosolic side of the endoplasmic reticulum membrane and finishes in its lumen. The sequential addition of sugars to dolichol pyrophosphate produces dolichol-linked oligosaccharides containing fourteen sugars, including two …

**Summary**, from NCBI Gene [440138](https://www.ncbi.nlm.nih.gov/gene/440138):

> This gene encodes a GDP-Man:Man3GlcNAc2-PP-dolichol-alpha1,2-mannosyltransferase which is localized to the cytosolic side of the endoplasmic reticulum (ER) and catalyzes the transfer of the fourth and fifth mannose residue from GDP-mannose (GDP-Man) to Man3GlcNAc2-PP-dolichol and Man4GlcNAc2-PP-dolichol resulting in the production of Man5GlcNAc2-PP-dolichol. Mutations in this gene are associated with congenital disorder of glycosylation type Ip (CDGIP). This gene overlaps but is distinct from …

**Accessions** — [HGNC:32456](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32456) · Entrez [440138](https://www.ncbi.nlm.nih.gov/gene/440138) · UniProt [Q2TAA5](https://www.uniprot.org/uniprotkb/Q2TAA5) · Ensembl [ENSG00000253710](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253710)

## Data

Gene col 14833: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14833); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14833, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14833]; `tensor/DDL_lfc|DDL_z.npy` [14833]; `embed/gene_vectors.npy` [14833]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14833 or target_col == 14833). Every well: [[ALG11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALG11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
