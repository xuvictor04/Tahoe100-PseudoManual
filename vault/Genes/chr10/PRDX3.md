---
symbol: "PRDX3"
type: "gene"
col: 9163
ensembl_id: "ENSG00000165672"
name: "peroxiredoxin 3"
location: "10q26.11"
module: 29
arm: "+"
pooled_cpm: 29.48
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# PRDX3

*peroxiredoxin 3* — 10q26.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.70× (z +20.1, q 0e+00, up in 42 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 5 µM: 1.98× (z +4.6, q 5e-04, up in 30 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (NCI-H460 7.03×, PANC-1 4.56×, A549 8.15×, SW480 4.62×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 5.81×, MIA PaCa-2 6.79×, LoVo 6.88×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.38×).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.455× (z -14.5, q 1e-44, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPT1]] (+0.79, fdr 7e-06), [[CRTAP]] (+0.75, fdr 7e-06), [[LAPTM4B]] (+0.70, fdr 8e-06); moves opposite to [[ATF4]] (-0.63, fdr 7e-06), [[NSRP1]] (-0.63, fdr 7e-06), [[PDCD7]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MEST]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9163.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (NCI-H460 7.03×, PANC-1 4.56×, A549 8.15×, SW480 4.62×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 5.81×, MIA PaCa-2 6.79×, LoVo 6.88×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.38×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.70×** | +20.1 | 0e+00 | 42/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.78×** | +16.6 | 0e+00 | 34/35 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.91×** | +12.8 | 2e-35 | 40/40 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **1.98×** | +4.6 | 5e-04 | 30/45 (KATO III, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.2 | 0.003 | 27/45 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **1.36×** | +4.0 | 0.007 | 24/46 (RPMI-7951, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.30×** | +3.3 | 0.071 | 22/48 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.3 | 0.071 | 0/48 | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.57× | +3.1 | 0.13 | 12/30 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9163.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.455×** | -14.5 | 1e-44 | 43/47 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.506×** | -8.9 | 2e-16 | 42/47 (SW1417, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.536×** | -7.8 | 1e-12 | 39/48 (AsPC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.666×** | -5.3 | 2e-05 | 32/48 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.729×** | -4.1 | 0.004 | 20/47 (C-33 A, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 5 µM |  | **0.800×** | -4.1 | 0.004 | 27/48 (SW480, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.745×** | -3.8 | 0.011 | 22/48 (SW48, RKO, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.815×** | -3.7 | 0.013 | 24/47 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.765×** | -3.3 | 0.066 | 17/48 (HS-578T, RPMI-7951, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.635× | -3.1 | 0.11 | 11/48 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.779× | -3.1 | 0.11 | 14/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.716× | -3.0 | 0.11 | 11/48 (HEC-1-A, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9163. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 23.8 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.53× (z +12.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 30.3 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.79× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -8.9) |
| [[HOP62 (line)]] | alt | 16.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.91× (z +13.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -8.8) |
| [[HS-578T (line)]] | alt | 17.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -10.3) |
| [[KATO III (line)]] | alt | 28.2 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.28× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 34.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 7.03× (z +16.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -11.5) |
| [[PANC-1 (line)]] | alt | 45.0 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +15.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -10.9) |
| [[A549 (line)]] | wt | 29.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.15× (z +14.9) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 41.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 34.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +12.8) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 19.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.88× (z +12.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 35.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.10× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 25.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.12× (z +13.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 23.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -9.5) |
| [[SNU-423 (line)]] | alt | 28.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +11.9) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 40.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.23× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -10.1) |
| [[SW480 (line)]] | alt | 35.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +14.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -11.6) |
| [[A-172 (line)]] | wt | 25.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.28× (z +11.8) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 47.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +13.7) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 18.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.32× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 36.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +9.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 34.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.51× (z +11.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 19.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.91× (z +12.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 39.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.01× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 26.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -17.5) |
| [[NCI-H2347 (line)]] | alt | 36.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.3) | — |
| [[RKO (line)]] | wt | 35.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -13.7) |
| [[SW1417 (line)]] | alt | 18.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -9.9) |
| [[A-427 (line)]] | wt | 30.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -14.0) |
| [[AN3 CA (line)]] | alt | 36.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0846× (z -9.7) |
| [[C32 (line)]] | wt | 22.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.35× (z +9.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 25.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 50.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -12.1) |
| [[HT-29 (line)]] | alt | 24.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.52× (z +10.7) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 19.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.44× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 9.62 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.7× (z +11.6) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -9.0) |
| [[SHP-77 (line)]] | alt | 25.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 26.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -9.5) |
| [[BT-474 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9163), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPT1]] | +0.79 | +0.75 / +0.80 | both halves | 7e-06 |  |
| [[CRTAP]] | +0.75 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[LAPTM4B]] | +0.70 | +0.58 / +0.73 | both halves | 8e-06 |  |
| [[ATP5F1B]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 673 |
| [[BANF1]] | +0.69 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[ERMP1]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[TMEM106C]] | +0.68 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[FKBP9]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[PFKM]] | +0.67 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[CNPY3]] | +0.66 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[OPA1]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 541 |
| [[TMX1]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATF4]] | -0.63 | -0.66 / -0.62 | both halves | 7e-06 | pathway: Cellular response to chemical stress |
| [[NSRP1]] | -0.63 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[PDCD7]] | -0.62 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[STYXL1]] | -0.62 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[PLEKHN1]] | -0.62 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[ZBTB7A]] | -0.61 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[WASHC1]] | -0.61 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[SURF6]] | -0.61 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[GATAD1]] | -0.59 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[ZNF316]] | -0.59 | -0.70 / -0.49 | both halves | 1e-05 |  |
| [[ARRDC2]] | -0.59 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.59 | -0.64 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEST]] | B | MEST activity raises PRDX3's level | lines that do not express MEST (17) vs lines expressing it (33) | 1.19× lower at baseline in the lines without MEST | 0.063 | ⚠ within organs, on part of the lines; also absent: COPG2IT1, CHDH, IL17RB |
| [[GGH]] | B | GGH activity raises PRDX3's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.25× lower at baseline in the lines without GGH | 0.092 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[CRTAP]] | C | CRTAP activity raises PRDX3's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.79× lower at baseline in the lines without CRTAP | 0.021 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.800). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.9, -21.8); signed map (-22.7, -38.9). **Vector** length 84.8, 20.0% of its response variance represented; |z| ≥ 3 in 817 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +16.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +20.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +0.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.0 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.9 | -0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | -0.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.2 | -8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.5 | -14.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.3 | -5.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.2 | -7.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -2.0 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | peroxiredoxin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.11 — chr10:119,167,720-119,178,812 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MER5, AOP-1, SP-22; previously AOP1 |
| Gene groups (HGNC) | Peroxiredoxins |
| Hallmark sets | ADIPOGENESIS, MYC_TARGETS_V1, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 4 pathways, smallest: Detoxification of Reactive Oxygen Species; Cellular response to chemical stress; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [P30048](https://www.uniprot.org/uniprotkb/P30048) (Thioredoxin-dependent peroxide reductase, mitochondrial):

> Thiol-specific peroxidase that catalyzes the reduction of hydrogen peroxide and organic hydroperoxides to water and alcohols, respectively. Plays a role in cell protection against oxidative stress by detoxifying peroxides. Acts synergistically with MAP3K13 to regulate the activation of NF-kappa-B in the cytosol. Required for the maintenance of physical strength (By similarity).

**Summary**, from NCBI Gene [10935](https://www.ncbi.nlm.nih.gov/gene/10935):

> This gene encodes a mitochondrial protein with antioxidant function. The protein is similar to the C22 subunit of Salmonella typhimurium alkylhydroperoxide reductase, and it can rescue bacterial resistance to alkylhydroperoxide in E. coli that lack the C22 subunit. The human and mouse genes are highly conserved, and they map to the regions syntenic between mouse and human chromosomes. Sequence comparisons with recently cloned mammalian homologs suggest that these genes consist of a family that …

**Accessions** — [HGNC:9354](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9354) · Entrez [10935](https://www.ncbi.nlm.nih.gov/gene/10935) · UniProt [P30048](https://www.uniprot.org/uniprotkb/P30048) · Ensembl [ENSG00000165672](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165672)

## Data

Gene col 9163: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9163); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9163, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9163]; `tensor/DDL_lfc|DDL_z.npy` [9163]; `embed/gene_vectors.npy` [9163]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9163 or target_col == 9163). Every well: [[PRDX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRDX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
