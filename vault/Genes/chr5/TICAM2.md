---
symbol: "TICAM2"
type: "gene"
col: 14357
ensembl_id: "ENSG00000243414"
name: "TIR domain containing adaptor molecule 2"
location: "5q22.3"
module: 37
arm: "+"
pooled_cpm: 34.76
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 13
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# TICAM2

*TIR domain containing adaptor molecule 2* — 5q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.71× (z +20.7, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.607× (z -7.6, q 2e-11, down in 24 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.663× (z -6.2, q 1e-07, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED7-TICAM2]] (+0.80, fdr 7e-06, ⚠ same locus), [[DNHD1]] (+0.76, fdr 7e-06), [[GOSR2]] (+0.76, fdr 7e-06), [[WDR49]] (+0.76, fdr 7e-06); moves opposite to [[BRD7]] (-0.65, fdr 1e-05), [[C2CD5]] (-0.58, fdr 1e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14357.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.71×** | +20.7 | 0e+00 | 45/48 (SW480, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +12.4 | 9e-33 | 38/48 (AsPC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +6.2 | 9e-08 | 28/48 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.1 | 2e-07 | 27/48 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +4.7 | 2e-04 | 22/48 (SW480, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.5 | 7e-04 | 1/49 (CHP-212) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +4.4 | 0.001 | 20/48 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.30×** | +4.1 | 0.003 | 18/48 (SW480, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.64×** | +4.1 | 0.003 | 21/49 (NCI-H460, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.003 | 16/48 (A-427, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.004 | 22/47 (NCI-H1573, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.006 | 20/48 (SW480, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.008 | 18/47 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.014 | 10/48 (A498, AsPC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.5 | 0.018 | 14/44 (A-172, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14357.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.607×** | -7.6 | 2e-11 | 24/36 (NCI-H1573, KATO III, …) | rises with dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.663×** | -6.2 | 1e-07 | 32/48 (RKO, NCI-H1573, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.676×** | -6.2 | 1e-07 | 27/48 (A498, HS-578T, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.702×** | -5.4 | 1e-05 | 23/48 (A-427, H4, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); composition shift |
| [[Pralsetinib (drug)]] 5 µM |  | **0.532×** | -5.2 | 2e-05 | 21/47 (AsPC-1, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.750×** | -4.6 | 4e-04 | 20/48 (AsPC-1, RPMI-7951, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.750×** | -4.5 | 4e-04 | 23/48 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.765×** | -4.2 | 0.002 | 23/48 (A498, HS-578T, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.618×** | -4.0 | 0.004 | 18/47 (C32, SW48, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.778×** | -4.0 | 0.004 | 19/48 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.783×** | -3.9 | 0.006 | 19/48 (COLO 205, LoVo, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.790×** | -3.7 | 0.009 | 16/48 (NCI-H1792, RKO, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.861× | -3.4 | 0.034 | 14/48 (HT-29, COLO 205, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.864× | -3.3 | 0.044 | 15/48 (AsPC-1, CHP-212, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.870× | -3.1 | 0.068 | 15/48 (KATO III, COLO 205, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.824×** | -3.1 | 0.078 | 19/48 (LS 180, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14357. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 126 | 2 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.63× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.0573× (z -23.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.295× (z -10.0) |
| [[LoVo (line)]] | wt | 53.3 | 3 (1 ⚠) | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.55× (z +12.2) | [[Belumosudil (drug)]] 5 µM 0.241× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 47.9 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +14.2) | [[Belinostat (drug)]] 5 µM 0.262× (z -10.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[Hs 766T (line)]] | wt | 28.7 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.130× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 36.1 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.89× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 31.5 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.12× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.234× (z -10.0) |
| [[A498 (line)]] | wt | 46.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[H4 (line)]] | wt | 80.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.229× (z -9.9) |
| [[HS-578T (line)]] | alt | 51.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +11.7) | — |
| [[SW 900 (line)]] | alt | 22.6 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 5.42× (z +10.7) | [[Docetaxel (drug)]] 0.05 µM 0.207× (z -10.0) ⚠ transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SW48 (line)]] | wt | 24.3 | 2 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 6.86× (z +9.2) | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0617× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 22.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.26× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 36.5 | 0 | 2 (1 ⚠) | — | [[Belumosudil (drug)]] 5 µM 0.220× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 20.6 | 2 | 0 | [[Auranofin (drug)]] 5 µM 7.52× (z +13.1) | — |
| [[PANC-1 (line)]] | alt | 11.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +14.0) | — |
| [[SW480 (line)]] | alt | 20.6 | 2 | 0 | [[Auranofin (drug)]] 5 µM 10.6× (z +16.4) | — |
| [[AN3 CA (line)]] | alt | 37.5 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0984× (z -8.9) |
| [[C-33 A (line)]] | alt | 27.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.86× (z +9.7) | — |
| [[C32 (line)]] | wt | 16.5 | 0 | 1 | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.164× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 42.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.09× (z +12.5) | — |
| [[HOP62 (line)]] | alt | 40.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.82× (z +12.7) | — |
| [[HT-29 (line)]] | alt | 24.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.2× (z +13.2) | — |
| [[KATO III (line)]] | alt | 45.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0965× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LOX-IMVI (line)]] | wt | 23.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.04× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 29.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.49× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 42.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.88× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 50.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.47× (z +8.7) | — |
| [[RKO (line)]] | wt | 41.9 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0568× (z -16.2) |
| [[RPMI-7951 (line)]] | alt | 40.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.63× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 18.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.49× (z +10.4) | — |
| [[SK-MEL-2 (line)]] | alt | 47.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.60× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 21.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.07× (z +11.9) | — |
| [[SW1417 (line)]] | alt | 8.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +11.0) | — |
| [[A549 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14357), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED7-TICAM2]] | +0.80 | +0.77 / +0.84 | both halves | 7e-06 | STRING 800; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[DNHD1]] | +0.76 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[GOSR2]] | +0.76 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[WDR49]] | +0.76 | +0.68 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[CORIN]] | +0.74 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[RRH]] | +0.73 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[KLRA1P]] | +0.73 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[CFAP53]] | +0.72 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[LINC02936]] | +0.72 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[SNX31]] | +0.70 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[CCDC62]] | +0.70 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[GABRR2]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[LINC02680]] | +0.69 | +0.58 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRD7]] | -0.65 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[C2CD5]] | -0.58 | -0.50 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TICAM2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DAB2IP]] | C | DAB2IP activity lowers TICAM2's level | lines that do not express DAB2IP (4) vs lines expressing it (46) | 1.70× higher at baseline in the lines without DAB2IP | 0.053 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF22; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.797). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.2, -17.8); signed map (11.8, 6.4). **Vector** length 125, 34.5% of its response variance represented; |z| ≥ 3 in 1,147 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +14.6 | +20.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.9 | +12.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +6.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +2.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | +3.0 | +4.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.0 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +3.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.8 | -5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.5 | -6.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.1 | -4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.0 | -4.2 |
|  | [[NG25 (drug)]] 5 µM |  | -3.5 | -4.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -3.0 | -5.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.9 | -3.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.6 | -3.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | TIR domain containing adaptor molecule 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.3 — chr5:115,578,496-115,602,479 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRAM, TICAM-2, TIRP |
| Gene groups (HGNC) | TIR domain containing |
| Reactome | 20 pathways, smallest: TRIF-mediated programmed cell death; Regulation of TBK1, IKKε (IKBKE)-mediated activation of IRF3, IRF7; Caspase activation via Death Receptors in the presence of ligand |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XR7](https://www.uniprot.org/uniprotkb/Q86XR7) (TIR domain-containing adapter molecule 2):

> Functions as a sorting adapter in different signaling pathways to facilitate downstream signaling leading to type I interferon induction. In TLR4 signaling, physically bridges TLR4 and TICAM1 and functionally transmits signal to TICAM1 in early endosomes after endocytosis of TLR4. In TLR2 signaling, physically bridges TLR2 and MYD88 and is required for the TLR2-dependent movement of MYD88 to endosomes following ligand engagement. Involved in IL-18 signaling and is proposed to function as a …

**Summary**, from NCBI Gene [353376](https://www.ncbi.nlm.nih.gov/gene/353376):

> Enables molecular adaptor activity. Involved in several processes, including positive regulation of interleukin-18-mediated signaling pathway; regulation of cytokine production; and regulation of innate immune response. Located in endoplasmic reticulum; endosome; and phagocytic cup. Is active in endosome membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21354](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21354) · Entrez [353376](https://www.ncbi.nlm.nih.gov/gene/353376) · UniProt [Q86XR7](https://www.uniprot.org/uniprotkb/Q86XR7) · Ensembl [ENSG00000243414](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243414)

## Data

Gene col 14357: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14357); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14357, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14357]; `tensor/DDL_lfc|DDL_z.npy` [14357]; `embed/gene_vectors.npy` [14357]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14357 or target_col == 14357). Every well: [[TICAM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TICAM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
