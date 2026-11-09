---
symbol: "DENND2C"
type: "gene"
col: 10669
ensembl_id: "ENSG00000175984"
name: "DENN domain containing 2C"
location: "1p13.2"
module: 34
arm: "+"
pooled_cpm: 25.06
n_lines_expressing: 40
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 13
direction_downstream: 6
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# DENND2C

*DENN domain containing 2C* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 4.31× (z +26.0, q 0e+00, up in 35 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.674× (z -7.0, q 1e-09, down in 21 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pralsetinib (drug)]] 5 µM: 0.677× (z -3.6, q 0.054, down in 9 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2347 0.180×, NCI-H23 0.174×, SK-MEL-2 0.138×, NCI-H2030 0.205×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 3 lines (HOP62 0.0880×, AN3 CA 0.0415×, Panc 03.27 0.259×; ⚠ transcription drop; cell-cycle shift, explains ~42% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (AsPC-1 0.233×, LoVo 0.300×, NCI-H2347 0.497×); [[Radotinib (drug)]] 5 µM in 2 lines (AsPC-1 0.307×, LoVo 0.290×); [[Binimetinib (drug)]] 0.5 µM in 1 line (AsPC-1 0.255×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA3B]] (+0.69, fdr 7e-06), [[PRSS3]] (+0.65, fdr 1e-05), [[TMC7]] (+0.64, fdr 7e-06); moves opposite to [[MBNL3]] (-0.50, fdr 2e-04), [[PRIMPOL]] (-0.49, fdr 1e-04), [[LINC01145-1]] (-0.48, fdr 5e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[SERPINB5]] → it (grade B ⚠); 6 go from it, the strongest it → [[PLCD3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10669.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **4.31×** | +26.0 | 0e+00 | 35/37 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.99×** | +24.6 | 0e+00 | 35/37 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.71×** | +23.3 | 0e+00 | 34/37 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.17×** | +18.8 | 0e+00 | 28/36 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.55×** | +16.6 | 0e+00 | 32/37 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.98×** | +12.1 | 7e-32 | 29/36 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +11.6 | 2e-29 | 22/39 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +11.2 | 2e-27 | 26/38 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.78×** | +9.5 | 1e-19 | 26/39 (PANC-1, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +8.8 | 8e-17 | 24/38 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +8.4 | 2e-15 | 20/37 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +6.8 | 4e-10 | 19/36 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +6.6 | 2e-09 | 16/36 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.94×** | +6.1 | 3e-08 | 19/31 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +6.0 | 7e-08 | 13/39 (LS 180, Panc 03.27, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.37×** | +5.6 | 9e-07 | 13/36 (LS 180, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10669.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2347 0.180×, NCI-H23 0.174×, SK-MEL-2 0.138×, NCI-H2030 0.205×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 3 lines (HOP62 0.0880×, AN3 CA 0.0415×, Panc 03.27 0.259×; ⚠ transcription drop; cell-cycle shift, explains ~42% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (AsPC-1 0.233×, LoVo 0.300×, NCI-H2347 0.497×); [[Radotinib (drug)]] 5 µM in 2 lines (AsPC-1 0.307×, LoVo 0.290×); [[Binimetinib (drug)]] 0.5 µM in 1 line (AsPC-1 0.255×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.674×** | -7.0 | 1e-09 | 21/36 (NCI-H2347, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.716×** | -5.5 | 1e-05 | 13/29 (NCI-H2347, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Pralsetinib (drug)]] 5 µM |  | **0.677×** | -3.6 | 0.054 | 9/37 (NCI-H1573, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.828× | -3.4 | 0.11 | 8/38 (A498, HOP62, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.828× | -3.2 | 0.14 | 8/36 (C32, NCI-H2030, …) | top dose only |  |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.839× | -3.1 | 0.17 | 12/37 (SW 900, NCI-H661, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.843× | -3.0 | 0.18 | 16/36 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.838× | -3.0 | 0.18 | 15/37 (SK-MEL-2, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10669. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 165 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -14.5) |
| [[NCI-H2030 (line)]] | alt | 28.9 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.192× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 6.76 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +13.9) | — |
| [[SK-MEL-2 (line)]] | alt | 33.4 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.28× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -12.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 26.6 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.60× (z +11.4) | — |
| [[NCI-H23 (line)]] | alt | 41.1 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.90× (z +21.2) | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 36.5 | 5 (1 ⚠) | 1 (1 ⚠) | [[Trametinib (drug)]] 5 µM 4.40× (z +10.6) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 4.32× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -10.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 14.5 | 6 | 0 | [[Belinostat (drug)]] 5 µM 4.10× (z +10.7) | — |
| [[A498 (line)]] | wt | 13.2 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 5.12× (z +11.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.4 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.82× (z +9.5) | [[Docetaxel (drug)]] 0.05 µM 0.205× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~42% of this change |
| [[HCT15 (line)]] | alt | 23.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 75.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -9.2) |
| [[J82 (line)]] | alt | 14.6 | 3 | 0 | [[Belinostat (drug)]] 5 µM 5.41× (z +10.7) | — |
| [[LoVo (line)]] | wt | 48.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.290× (z -10.4) |
| [[HOP62 (line)]] | alt | 9.36 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.46× (z +9.0) | [[Docetaxel (drug)]] 0.05 µM 0.0880× (z -14.7) ⚠ transcription drop; cell-cycle shift, explains ~42% of this change |
| [[LOX-IMVI (line)]] | wt | 12.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.70× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 56.9 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.259× (z -11.1) ⚠ transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SW 900 (line)]] | alt | 14.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.84× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 33.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.15× (z +8.6) | — |
| [[A-172 (line)]] | wt | 7.84 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 32.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -9.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0415× (z -11.8) ⚠ transcription drop; cell-cycle shift, explains ~42% of this change |
| [[Hs 766T (line)]] | wt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 9.49 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.42× (z +9.4) | — |
| [[A549 (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.58 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.41 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.83 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.28 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.88 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10669), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA3B]] | +0.69 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[PRSS3]] | +0.65 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[TMC7]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[JUP]] | +0.64 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[KLK11]] | +0.63 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[PLEKHM1P1]] | +0.63 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[DHRS9]] | +0.62 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[GIPR]] | +0.62 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[LYPD3]] | +0.62 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[RHOF]] | +0.61 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[KLK10]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[FA2H]] | +0.60 | +0.47 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBNL3]] | -0.50 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[PRIMPOL]] | -0.49 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[LINC01145-1]] | -0.48 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[C5orf15]] | -0.48 | -0.43 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINB5]] | B | SERPINB5 activity weakens DENND2C's drug response | lines that do not express SERPINB5 (27) vs lines expressing it (12) | the lines without SERPINB5 respond 3.16× as strongly (z diff -3.84); strongest at Idarubicin (hydrochloride) 5 µM: 1.82x vs 0.54x (z diff -8.8) | 0.004 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; target measured in part of the lines; artifact flags |
| [[KRT16]] | B | KRT16 activity raises DENND2C's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 1.60× lower at baseline in the lines without KRT16 | 0.023 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[PCDH1]] | B | PCDH1 activity raises DENND2C's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.04× lower at baseline in the lines without PCDH1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[MEGF6]] | B | MEGF6 activity raises DENND2C's level | lines that do not express MEGF6 (11) vs lines expressing it (39) | 2.12× lower at baseline in the lines without MEGF6 | 0.045 | ⚠ within organs, on part of the lines; also absent: SQOR; maybe low, not absent |
| [[GJB3]] | B | GJB3 activity raises DENND2C's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 2.04× lower at baseline in the lines without GJB3 | 0.045 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[LINC01610]] | B | LINC01610 activity raises DENND2C's level | lines that do not express LINC01610 (45) vs lines expressing it (5) | 2.50× lower at baseline in the lines without LINC01610 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OVAAL, LINC00879, LINC02099 |
| [[RNF223]] | B | RNF223 activity raises DENND2C's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 1.76× lower at baseline in the lines without RNF223 | 0.057 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2 |
| [[PKP1]] | B | PKP1 activity weakens DENND2C's drug response | lines that do not express PKP1 (26) vs lines expressing it (13) | the lines without PKP1 respond 2.38× as strongly (z diff -3.10); strongest at Idarubicin (hydrochloride) 5 µM: 1.72x vs 0.67x (z diff -7.0) | 0.076 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5; target measured in part of the lines; artifact flags |
| [[SERPINB5]] | B | SERPINB5 activity raises DENND2C's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 2.27× lower at baseline in the lines without SERPINB5 | 0.076 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[TFF1]] | B | TFF1 activity weakens DENND2C's drug response | lines that do not express TFF1 (26) vs lines expressing it (13) | the lines without TFF1 respond 2.01× as strongly (z diff -2.71); strongest at Idarubicin (hydrochloride) 5 µM: 1.67x vs 0.71x (z diff -5.7) | 0.081 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC; target measured in part of the lines; artifact flags |
| [[RNF223]] | B | RNF223 activity weakens DENND2C's drug response | lines that do not express RNF223 (23) vs lines expressing it (16) | the lines without RNF223 respond 1.79× as strongly (z diff -2.64); strongest at Idarubicin (hydrochloride) 5 µM: 1.83x vs 0.73x (z diff -6.3) | 0.081 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2; target measured in part of the lines; artifact flags |
| [[LAMC2]] | B | LAMC2 activity raises DENND2C's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 1.76× lower at baseline in the lines without LAMC2 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLCD3]] | B | DENND2C activity raises PLCD3's level | lines that do not express DENND2C (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without DENND2C | 0.019 | ⚠ within organs, on part of the lines; also absent: MSN, CAV1, RIMKLB |
| [[SH3BGRL3]] | B | DENND2C activity raises SH3BGRL3's level | lines that do not express DENND2C (10) vs lines expressing it (40) | 1.73× lower at baseline in the lines without DENND2C | 0.067 | ⚠ within organs, on part of the lines; also absent: MSN, CAV1, RIMKLB |
| [[PLIN3]] | B | DENND2C activity raises PLIN3's level | lines that do not express DENND2C (10) vs lines expressing it (40) | 1.66× lower at baseline in the lines without DENND2C | 0.069 | ⚠ within organs, on part of the lines; also absent: MSN, CAV1, RIMKLB |
| [[ALS2CL]] | B | DENND2C activity raises ALS2CL's level | lines that do not express DENND2C (10) vs lines expressing it (40) | 1.38× lower at baseline in the lines without DENND2C | 0.072 | ⚠ within organs, on part of the lines; also absent: MSN, CAV1, RIMKLB |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM | B | DENND2C activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express DENND2C (10) vs lines expressing it (38) | the lines without DENND2C: 0.87× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: MSN, CAV1, RIMKLB |
| [[KRT19]] | B | DENND2C activity raises KRT19's level | lines that do not express DENND2C (10) vs lines expressing it (40) | 1.25× lower at baseline in the lines without DENND2C | 0.098 | ⚠ within organs, on part of the lines; also absent: MSN, CAV1, RIMKLB |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.620). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.5, 54.9); signed map (-0.2, 39.3). **Vector** length 107, 26.7% of its response variance represented; |z| ≥ 3 in 1,134 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +11.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +8.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.2 | +16.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.0 | +8.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.9 | +12.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.6 | +6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +4.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.1 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +2.7 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | -3.4 | -3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | +0.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | DENN domain containing 2C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:114,582,848-114,670,422 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37099, DKFZp686G0351, DKFZp779P1149, dJ1156J9.1, RP5-1156J9.1 |
| Gene groups (HGNC) | DENN domain containing |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68D51](https://www.uniprot.org/uniprotkb/Q68D51) (DENN domain-containing protein 2C):

> Guanine nucleotide exchange factor (GEF) which may activate RAB9A and RAB9B. Promotes the exchange of GDP to GTP, converting inactive GDP-bound Rab proteins into their active GTP-bound form.

**Summary**, from NCBI Gene [163259](https://www.ncbi.nlm.nih.gov/gene/163259):

> Enables guanyl-nucleotide exchange factor activity. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24748](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24748) · Entrez [163259](https://www.ncbi.nlm.nih.gov/gene/163259) · UniProt [Q68D51](https://www.uniprot.org/uniprotkb/Q68D51) · Ensembl [ENSG00000175984](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175984)

## Data

Gene col 10669: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10669); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10669, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10669]; `tensor/DDL_lfc|DDL_z.npy` [10669]; `embed/gene_vectors.npy` [10669]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10669 or target_col == 10669). Every well: [[DENND2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DENND2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
