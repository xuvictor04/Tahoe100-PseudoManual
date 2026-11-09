---
symbol: "MORC4"
type: "gene"
col: 5423
ensembl_id: "ENSG00000133131"
name: "MORC family CW-type zinc finger 4"
location: "Xq22.3"
module: 60
arm: "+"
pooled_cpm: 53.83
n_lines_expressing: 47
n_dd_up: 38
n_dd_down: 3
n_dd_up_clean: 25
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# MORC4

*MORC family CW-type zinc finger 4* — Xq22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (13 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.13× (z +23.1, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.738× (z -6.2, q 4e-07, down in 23 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 1 line (HT-29 0.136×; ⚠ toxic); [[Isocorydine (drug)]] 0.5 µM in 1 line (NCI-H661 0.0785×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.448×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (AN3 CA 0.277×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUGT1]] (+0.55, fdr 1e-05), [[MYO5A]] (+0.52, fdr 3e-05), [[HSPA4L]] (+0.51, fdr 1e-05); moves opposite to [[MARK2]] (-0.47, fdr 2e-04), [[SIK2]] (-0.45, fdr 3e-04), [[KRI1]] (-0.44, fdr 2e-04).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[ZNF423]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5423.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.13×** | +23.1 | 0e+00 | 43/45 (HT-29, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +21.9 | 0e+00 | 41/44 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +14.5 | 1e-45 | 35/45 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.90×** | +12.9 | 3e-36 | 31/44 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.98×** | +11.6 | 8e-29 | 33/40 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.73×** | +11.1 | 2e-26 | 34/45 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.68×** | +10.1 | 3e-22 | 31/45 (NCI-H460, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.64×** | +10.0 | 7e-22 | 35/44 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.69×** | +10.0 | 1e-21 | 34/45 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.64×** | +9.6 | 3e-20 | 34/45 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +9.2 | 2e-18 | 36/45 (SW480, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.60×** | +9.2 | 2e-18 | 22/36 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +8.8 | 9e-17 | 32/45 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +8.7 | 1e-16 | 27/45 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +8.2 | 1e-14 | 28/45 (A549, RKO, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +7.3 | 1e-11 | 29/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.63×** | +7.0 | 6e-11 | 31/45 (KATO III, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +6.6 | 1e-09 | 23/45 (SW1417, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +6.0 | 6e-08 | 23/45 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +5.3 | 2e-06 | 27/45 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5423.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 1 line (HT-29 0.136×; ⚠ toxic); [[Isocorydine (drug)]] 0.5 µM in 1 line (NCI-H661 0.0785×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.448×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (AN3 CA 0.277×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.738×** | -6.2 | 4e-07 | 23/45 (LoVo, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.795×** | -4.7 | 9e-04 | 23/45 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.808×** | -4.3 | 0.003 | 20/44 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -3.3 | 0.14 | 15/44 (PANC-1, SW 1271, …) | all doses, stronger at high dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.854× | -3.2 | 0.14 | 13/43 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.855× | -3.2 | 0.14 | 7/45 (Panc 03.27, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5423. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 40.8 | 10 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +22.2) | — |
| [[KATO III (line)]] | alt | 75.9 | 8 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.85× (z +18.2) | — |
| [[PANC-1 (line)]] | alt | 22.7 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.63× (z +13.9) | — |
| [[LoVo (line)]] | wt | 110 | 6 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.37× (z +15.7) | — |
| [[SW1417 (line)]] | alt | 74.0 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +19.4) | — |
| [[Panc 03.27 (line)]] | alt | 42.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +16.3) | — |
| [[RKO (line)]] | wt | 70.5 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.16× (z +18.0) | — |
| [[A498 (line)]] | wt | 149 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +11.8) | — |
| [[CFPAC-1 (line)]] | alt | 37.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +14.6) | — |
| [[HOP62 (line)]] | alt | 34.6 | 4 | 0 | [[Auranofin (drug)]] 5 µM 6.83× (z +17.0) | — |
| [[HT-29 (line)]] | alt | 42.3 | 3 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 9.59× (z +20.0) | [[Lonafarnib (drug)]] 5 µM 0.136× (z -9.2) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 74.5 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +23.3) | — |
| [[A-172 (line)]] | wt | 25.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +10.7) | — |
| [[A-427 (line)]] | wt | 58.9 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 5.40× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[C-33 A (line)]] | alt | 31.9 | 3 | 0 | [[Auranofin (drug)]] 5 µM 7.20× (z +12.7) | — |
| [[C32 (line)]] | wt | 29.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +13.9) | — |
| [[J82 (line)]] | alt | 46.5 | 3 | 0 | [[Selinexor (drug)]] 5 µM 2.21× (z +10.9) | — |
| [[LOX-IMVI (line)]] | wt | 42.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +14.8) | — |
| [[LS 180 (line)]] | wt | 63.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.28× (z +18.4) | — |
| [[AsPC-1 (line)]] | alt | 22.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +10.7) | — |
| [[H4 (line)]] | wt | 44.9 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +9.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 32.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.42× (z +15.5) | — |
| [[NCI-H1573 (line)]] | alt | 19.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +15.0) | — |
| [[NCI-H23 (line)]] | alt | 57.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +14.5) | — |
| [[SW 900 (line)]] | alt | 28.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.5) | — |
| [[SW48 (line)]] | wt | 81.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +10.0) | — |
| [[A549 (line)]] | wt | 166 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.82× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 82.9 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.277× (z -8.6) |
| [[BT-474 (line)]] | alt | 45.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.70× (z +15.4) | — |
| [[COLO 205 (line)]] | alt | 34.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.97× (z +14.3) | — |
| [[HCT15 (line)]] | alt | 121 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HepG2_C3A (line)]] | wt | 34.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.88× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 40.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.67× (z +10.2) | — |
| [[hTERT-HPNE (line)]] | wt | 41.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +12.7) | — |
| [[NCI-H1792 (line)]] | alt | 38.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +12.4) | — |
| [[NCI-H2347 (line)]] | alt | 49.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +8.6) | — |
| [[NCI-H661 (line)]] | alt | 45.8 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0785× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 88.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.95× (z +12.0) | — |
| [[SNU-423 (line)]] | alt | 74.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.89× (z +14.6) | — |
| [[CHP-212 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.18 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.33 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5423), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUGT1]] | +0.55 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[MYO5A]] | +0.52 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[HSPA4L]] | +0.51 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[CHORDC1]] | +0.50 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[UBE2Q2]] | +0.50 | +0.29 / +0.36 | both halves | 2e-04 |  |
| [[ATP2C1]] | +0.49 | +0.30 / +0.48 | both halves | 2e-04 |  |
| [[SERPINH1]] | +0.49 | +0.38 / +0.35 | both halves | 1e-04 |  |
| [[TMEM167A]] | +0.48 | +0.27 / +0.43 | both halves | 3e-04 |  |
| [[CTH]] | +0.48 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[DNAJA4]] | +0.48 | +0.40 / +0.38 | both halves | 7e-05 |  |
| [[BLOC1S2]] | +0.47 | +0.56 / +0.33 | both halves | 1e-04 |  |
| [[WDR41]] | +0.47 | +0.47 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARK2]] | -0.47 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[SIK2]] | -0.45 | -0.36 / -0.28 | both halves | 3e-04 |  |
| [[KRI1]] | -0.44 | -0.29 / -0.37 | both halves | 2e-04 |  |
| [[GPATCH8]] | -0.44 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[ATF7]] | -0.44 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[C1QTNF3-AMACR]] | -0.43 | -0.37 / -0.26 | both halves | 4e-04 |  |
| [[NUP98]] | -0.43 | -0.40 / -0.27 | both halves | 3e-04 |  |
| [[GATAD2B]] | -0.43 | -0.44 / -0.26 | both halves | 4e-04 |  |
| [[GGA1]] | -0.43 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[ZBTB48]] | -0.43 | -0.27 / -0.36 | both halves | 3e-04 |  |
| [[GGA3]] | -0.42 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[INTS5]] | -0.41 | -0.26 / -0.39 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MORC4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DNAJA4]] | B | DNAJA4 activity strengthens MORC4's drug response | lines that do not express DNAJA4 (20) vs lines expressing it (25) | the lines without DNAJA4 respond 0.78× as strongly (z diff +0.73); strongest at Homoharringtonine 5 µM: 1.40x vs 2.07x (z diff +3.4) | 0.068 | ⚠ within organs, on part of the lines; also absent: COL17A1, ENSG00000262302, KIAA0040; target measured in part of the lines; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF423]] | C | MORC4 activity lowers ZNF423's level | lines that do not express MORC4 (3) vs lines expressing it (47) | 3.48× higher at baseline in the lines without MORC4 | 0.049 | ⚠ few lines (3 vs 47); across organs; also absent: USP53, OSBPL10, TESK2; maybe low, not absent |
| [[SESN2]] | C | MORC4 activity lowers SESN2's level | lines that do not express MORC4 (3) vs lines expressing it (47) | 2.72× higher at baseline in the lines without MORC4 | 0.053 | ⚠ few lines (3 vs 47); across organs; also absent: USP53, OSBPL10, TESK2; maybe low, not absent |
| cells under [[Homoharringtonine (drug)]] 0.05 µM | C | MORC4 activity raises the cells' numbers under Homoharringtonine 0.05 µM (protects the cells) | lines that do not express MORC4 (3) vs lines expressing it (45) | the lines without MORC4: 0.63× the cells of the other lines | 0.088 | ⚠ few lines (3 vs 47); across organs; also absent: USP53, OSBPL10, TESK2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.471). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.1, 41.8); signed map (-8.9, 23.3). **Vector** length 104, 27.3% of its response variance represented; |z| ≥ 3 in 1,364 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.4 | +23.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +9.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.0 | +6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +6.0 | +9.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +8.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.5 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.0 | +1.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.3 | -6.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.0 | -4.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -4.8 | +6.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | +1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -2.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.6 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | MORC family CW-type zinc finger 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.3 — chrX:106,813,871-107,000,212 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZCW4, FLJ11565; previously ZCWCC2 |
| Gene groups (HGNC) | Zinc fingers CW-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TE76](https://www.uniprot.org/uniprotkb/Q8TE76) (MORC family CW-type zinc finger protein 4):

> Histone methylation reader which binds to non-methylated (H3K4me0), monomethylated (H3K4me1), dimethylated (H3K4me2) and trimethylated (H3K4me3) 'Lys-4' on histone H3. The order of binding preference is H3K4me3 > H3K4me2 > H3K4me1 > H3K4me0.

**Summary**, from NCBI Gene [79710](https://www.ncbi.nlm.nih.gov/gene/79710):

> In human, the four current members of the microrchidia (morc) gene family share an N-terminal ATPase-like ATP-binding region and a CW four-cysteine zinc-finger motif. The protein encoded by this gene also has a nuclear matrix binding domain and a two-stranded coiled-coil motif near its C-terminus. This gene is widely expressed at low levels in normal tissues and has elevated expression in placenta and testis. Alternative splicing results in multiple transcript variants encoding distinct …

**Accessions** — [HGNC:23485](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23485) · Entrez [79710](https://www.ncbi.nlm.nih.gov/gene/79710) · UniProt [Q8TE76](https://www.uniprot.org/uniprotkb/Q8TE76) · Ensembl [ENSG00000133131](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133131)

## Data

Gene col 5423: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5423); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5423, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5423]; `tensor/DDL_lfc|DDL_z.npy` [5423]; `embed/gene_vectors.npy` [5423]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5423 or target_col == 5423). Every well: [[MORC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MORC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
