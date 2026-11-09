---
symbol: "PPM1L"
type: "gene"
col: 8722
ensembl_id: "ENSG00000163590"
name: "protein phosphatase, Mg2+/Mn2+ dependent 1L"
location: "3q25.33-q26.1"
module: 143
arm: "+"
pooled_cpm: 52.39
n_lines_expressing: 42
n_dd_up: 29
n_dd_down: 3
n_dd_up_clean: 25
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# PPM1L

*protein phosphatase, Mg2+/Mn2+ dependent 1L* — 3q25.33-q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.57× (z +30.9, q 0e+00, up in 37 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.546× (z -5.4, q 3e-05, down in 23 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SNU-1 0.0590×, A-427 0.218×, NCI-H23 0.298×, KATO III 0.297×, …; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 4 lines (LoVo 0.415×, NCI-H23 0.420×, SHP-77 0.358×, SNU-1 0.354×); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-427 0.202×, NCI-H23 0.185×, SNU-1 0.166×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[PH-797804 (drug)]] 5 µM in 1 line (LOX-IMVI 0.0332×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.547×).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JADE3]] (+0.54, fdr 2e-05), [[ARL15]] (+0.54, fdr 1e-05), [[TPK1]] (+0.53, fdr 2e-05); moves opposite to [[KRBOX4]] (-0.55, fdr 3e-05), [[ZNF526]] (-0.52, fdr 8e-05), [[IFT172]] (-0.50, fdr 4e-04).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GRIP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 9 with an alert ⚠; shown: the 15 strongest. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8722.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.57×** | +30.9 | 0e+00 | 37/40 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.92×** | +26.0 | 0e+00 | 35/40 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.43×** | +21.2 | 0e+00 | 36/40 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.08×** | +19.3 | 0e+00 | 38/40 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.83×** | +17.9 | 0e+00 | 35/39 (NCI-H2030, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.76×** | +17.4 | 0e+00 | 35/40 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.31×** | +13.9 | 1e-41 | 32/39 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.20×** | +13.5 | 8e-40 | 32/40 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +13.4 | 2e-39 | 30/40 (HEC-1-A, J82, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.68×** | +12.7 | 4e-35 | 31/40 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.88×** | +10.9 | 7e-26 | 36/39 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +10.7 | 3e-25 | 30/40 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +10.6 | 1e-24 | 24/40 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.05×** | +10.0 | 5e-22 | 36/40 (A-427, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +10.0 | 9e-22 | 27/40 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8722.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SNU-1 0.0590×, A-427 0.218×, NCI-H23 0.298×, KATO III 0.297×, …; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 4 lines (LoVo 0.415×, NCI-H23 0.420×, SHP-77 0.358×, SNU-1 0.354×); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-427 0.202×, NCI-H23 0.185×, SNU-1 0.166×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[PH-797804 (drug)]] 5 µM in 1 line (LOX-IMVI 0.0332×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.547×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.546×** | -5.4 | 3e-05 | 23/41 (NCI-H23, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.553×** | -5.3 | 3e-05 | 20/39 (LOX-IMVI, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.758×** | -4.7 | 4e-04 | 19/37 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.823× | -3.2 | 0.18 | 6/40 (NCI-H1792, HS-578T, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8722. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 17.4 | 25 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.04× (z +16.6) | — |
| [[HS-578T (line)]] | alt | 34.2 | 25 | 0 | [[Budesonide (drug)]] 0.05 µM 15.2× (z +17.7) | — |
| [[HEC-1-A (line)]] | alt | 19.9 | 10 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.73× (z +18.4) | — |
| [[HOP62 (line)]] | alt | 18.4 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +23.9) | — |
| [[Panc 03.27 (line)]] | alt | 28.9 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.37× (z +20.0) | — |
| [[CFPAC-1 (line)]] | alt | 16.5 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +20.7) | — |
| [[J82 (line)]] | alt | 14.5 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +15.5) | — |
| [[A-427 (line)]] | wt | 131 | 2 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.44× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.547× (z -9.4) |
| [[SW480 (line)]] | alt | 56.9 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +17.5) | — |
| [[C32 (line)]] | wt | 18.8 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.66× (z +13.5) | — |
| [[COLO 205 (line)]] | alt | 42.1 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 20.1× (z +24.7) | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 146 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.39× (z +30.7) | [[Dinaciclib (drug)]] 5 µM 0.362× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.415× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 33.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +14.2) | — |
| [[NCI-H23 (line)]] | alt | 313 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.420× (z -8.9) |
| [[SW1417 (line)]] | alt | 105 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.424× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 106 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 47.6 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +13.6) | [[PH-797804 (drug)]] 5 µM 0.0332× (z -16.4) |
| [[HT-29 (line)]] | alt | 47.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +14.7) | — |
| [[NCI-H1792 (line)]] | alt | 58.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +17.5) | — |
| [[NCI-H2030 (line)]] | alt | 39.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.58× (z +13.1) | — |
| [[SK-MEL-2 (line)]] | alt | 14.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.33× (z +11.9) | — |
| [[SNU-1 (line)]] | wt | 291 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0590× (z -22.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.354× (z -8.7) |
| [[Hs 766T (line)]] | wt | 14.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +8.9) | — |
| [[RKO (line)]] | wt | 47.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +15.4) | — |
| [[RPMI-7951 (line)]] | alt | 17.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 76.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +8.5) | [[Auranofin (drug)]] 5 µM 0.358× (z -8.9) |
| [[SNU-423 (line)]] | alt | 18.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 40.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +8.9) | — |
| [[A-172 (line)]] | wt | 13.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.69× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 139 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +11.3) | — |
| [[C-33 A (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0874× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 14.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +11.6) | — |
| [[HCT15 (line)]] | alt | 20.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 73.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +12.6) | — |
| [[PANC-1 (line)]] | alt | 99.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.43× (z +9.9) | — |
| [[A549 (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.11 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.29 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.58 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.09 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.67 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8722), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JADE3]] | +0.54 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[ARL15]] | +0.54 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[TPK1]] | +0.53 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[PARD3]] | +0.52 | +0.29 / +0.35 | both halves | 3e-04 |  |
| [[SIK3]] | +0.51 | +0.36 / +0.43 | both halves | 9e-05 |  |
| [[AHCYL2]] | +0.51 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[ATP11C]] | +0.51 | +0.45 / +0.32 | both halves | 2e-04 |  |
| [[TSC22D1]] | +0.50 | +0.51 / +0.31 | both halves | 2e-04 |  |
| [[TCF12]] | +0.50 | +0.51 / +0.30 | both halves | 2e-04 |  |
| [[CACHD1]] | +0.50 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[TMEM164]] | +0.50 | +0.26 / +0.50 | both halves | 4e-04 |  |
| [[NETO2]] | +0.50 | +0.49 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRBOX4]] | -0.55 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[ZNF526]] | -0.52 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[IFT172]] | -0.50 | -0.61 / -0.26 | both halves | 4e-04 |  |
| [[ZNF568]] | -0.50 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[CLEC4A]] | -0.49 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[RCN3]] | -0.47 | -0.42 / -0.26 | both halves | 4e-04 |  |
| [[ACOX3]] | -0.46 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[THOC1]] | -0.45 | -0.47 / -0.23 | both halves | 5e-04 |  |
| [[RTCB]] | -0.45 | -0.44 / -0.24 | both halves | 5e-04 |  |
| [[NPRL2]] | -0.45 | -0.52 / -0.28 | both halves | 3e-04 |  |
| [[SLC25A42]] | -0.45 | -0.32 / -0.30 | both halves | 2e-04 |  |
| [[TMEM14B]] | -0.45 | -0.33 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PPM1L's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[B3GALT1]] | B | B3GALT1 activity raises PPM1L's level | lines that do not express B3GALT1 (20) vs lines expressing it (30) | 1.34× lower at baseline in the lines without B3GALT1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ANTXR1, LINC00882, LINC01695; maybe low, not absent |
| [[RASSF8-AS1]] | B | RASSF8-AS1 activity raises PPM1L's level | lines that do not express RASSF8-AS1 (14) vs lines expressing it (36) | 1.09× lower at baseline in the lines without RASSF8-AS1 | 0.072 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804 |
| [[CHN1]] | B | CHN1 activity raises PPM1L's level | lines that do not express CHN1 (10) vs lines expressing it (40) | 1.49× lower at baseline in the lines without CHN1 | 0.098 | ⚠ within organs, on part of the lines; also absent: GXYLT2, HHIPL2, CARMIL2; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIP1]] | B | PPM1L activity raises GRIP1's level | lines that do not express PPM1L (8) vs lines expressing it (42) | 2.75× lower at baseline in the lines without PPM1L | 0.051 | ⚠ within organs, on part of the lines; also absent: SLC25A27, SORBS1, LINC01277; maybe low, not absent |

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.0, 11.1); signed map (4.4, 11.2). **Vector** length 87.8, 21.1% of its response variance represented; |z| ≥ 3 in 1,289 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +3.8 | +10.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | +3.4 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +12.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.6 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +2.5 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +13.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +3.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.9 | +4.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.9 | +3.0 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.5 | -5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.0 | +0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.7 | +1.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.5 | +21.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.4 | +17.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.1 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase, Mg2+/Mn2+ dependent 1L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.33-q26.1 — chr3:160,755,602-161,078,902 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PP2CE |
| Gene groups (HGNC) | Protein phosphatases, Mg2+/Mn2+ dependent |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5SGD2](https://www.uniprot.org/uniprotkb/Q5SGD2) (Protein phosphatase 1L):

> Acts as a suppressor of the SAPK signaling pathways by associating with and dephosphorylating MAP3K7/TAK1 and MAP3K5, and by attenuating the association between MAP3K7/TAK1 and MAP2K4 or MAP2K6.

**Summary**, from NCBI Gene [151742](https://www.ncbi.nlm.nih.gov/gene/151742):

> The protein encoded by this gene is a magnesium or manganese-requiring phosphatase that is involved in several signaling pathways. The encoded protein downregulates apoptosis signal-regulating kinase 1, a protein that initiates a signaling cascade that leads to apoptosis when cells are subjected to cytotoxic stresses. This protein also is an endoplasmic reticulum transmembrane protein that helps regulate ceramide transport from the endoplasmic reticulum to the Golgi apparatus. Finally, this …

**Accessions** — [HGNC:16381](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16381) · Entrez [151742](https://www.ncbi.nlm.nih.gov/gene/151742) · UniProt [Q5SGD2](https://www.uniprot.org/uniprotkb/Q5SGD2) · Ensembl [ENSG00000163590](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163590)

## Data

Gene col 8722: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8722); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8722, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8722]; `tensor/DDL_lfc|DDL_z.npy` [8722]; `embed/gene_vectors.npy` [8722]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8722 or target_col == 8722). Every well: [[PPM1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPM1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
