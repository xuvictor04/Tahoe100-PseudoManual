---
symbol: "PHYH"
type: "gene"
col: 2856
ensembl_id: "ENSG00000107537"
name: "phytanoyl-CoA 2-hydroxylase"
location: "10p13"
module: 35
arm: "+"
pooled_cpm: 14.44
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 15
n_dd_up_clean: 19
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# PHYH

*phytanoyl-CoA 2-hydroxylase* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.01× (z +15.8, q 0e+00, up in 36 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.08× (z +14.8, q 0e+00, up in 31 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.603× (z -7.2, q 5e-10, down in 27 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.617× (z -6.8, q 2e-09, down in 29 of 46 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RWDD2B]] (+0.72, fdr 3e-05), [[ZNF563]] (+0.72, fdr 1e-05), [[TCEAL1]] (+0.72, fdr 3e-05); moves opposite to [[TRABD]] (-0.61, fdr 2e-04), [[ERCC2]] (-0.60, fdr 3e-04), [[VKORC1L1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 035]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2856.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.01×** | +15.8 | 0e+00 | 36/37 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.08×** | +14.8 | 0e+00 | 31/46 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.17×** | +14.3 | 8e-44 | 20/26 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.93×** | +13.3 | 2e-38 | 41/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +12.0 | 3e-31 | 33/46 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +10.3 | 9e-23 | 25/31 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.73×** | +7.8 | 4e-13 | 28/45 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +7.8 | 4e-13 | 29/44 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +7.5 | 4e-12 | 30/46 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +7.0 | 2e-10 | 24/45 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +5.4 | 3e-06 | 20/45 (SW1417, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +5.3 | 7e-06 | 21/45 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +5.1 | 2e-05 | 21/46 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.41×** | +5.0 | 3e-05 | 17/47 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~20% of this change | **1.35×** | +4.3 | 7e-04 | 13/42 (LS 180, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.001 | 16/46 (A498, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.004 | 14/47 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.005 | 12/47 (NCI-H23, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.010 | 14/46 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2856.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.603×** | -7.2 | 5e-10 | 27/44 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.617×** | -6.8 | 2e-09 | 29/46 (NCI-H2030, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.619×** | -6.8 | 2e-09 | 31/46 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.643×** | -6.2 | 7e-08 | 24/46 (J82, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.656×** | -5.9 | 3e-07 | 25/46 (NCI-H2030, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.660×** | -5.9 | 4e-07 | 28/46 (SNU-423, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.695×** | -5.1 | 2e-05 | 23/46 (J82, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.713×** | -4.2 | 0.002 | 15/46 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.758×** | -3.9 | 0.006 | 15/44 (Hs 766T, NCI-H460, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.616×** | -3.6 | 0.020 | 7/45 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.796×** | -3.2 | 0.070 | 7/47 (SW 1088, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.799×** | -3.1 | 0.079 | 16/46 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.804×** | -3.1 | 0.097 | 14/46 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.806×** | -3.0 | 0.097 | 12/45 (Panc 03.27, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | **0.806×** | -3.0 | 0.097 | 3/47 (NCI-H460, HOP62, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2856. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 12.2 | 3 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.45× (z +9.7) | [[AZD2858 (drug)]] 0.5 µM 0.101× (z -9.0) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 13.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 20.8 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 2.47× (z +11.0) | — |
| [[RKO (line)]] | wt | 12.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +10.0) | — |
| [[J82 (line)]] | alt | 21.0 | 2 | 0 | [[Selinexor (drug)]] 5 µM 2.68× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 2 | 0 | [[Selinexor (drug)]] 5 µM 3.10× (z +9.9) | — |
| [[A-172 (line)]] | wt | 18.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +8.5) | — |
| [[A-427 (line)]] | wt | 48.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 14.7 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.71× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 8.76 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.23× (z +8.8) | — |
| [[KATO III (line)]] | alt | 9.56 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.53× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +10.0) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 8.73 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.112× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 16.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.54× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 33.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 8.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 17.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +11.3) | — |
| [[SW480 (line)]] | alt | 10.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2856), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RWDD2B]] | +0.72 | +0.75 / +0.45 | both halves | 3e-05 |  |
| [[ZNF563]] | +0.72 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[TCEAL1]] | +0.72 | +0.74 / +0.43 | both halves | 3e-05 |  |
| [[CLN5]] | +0.71 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[TMEM35B]] | +0.71 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[SDSL]] | +0.71 | +0.76 / +0.53 | both halves | 1e-05 |  |
| [[TCEAL4]] | +0.70 | +0.74 / +0.41 | both halves | 4e-05 |  |
| [[ZNF442]] | +0.70 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[ZC2HC1C]] | +0.70 | +0.73 / +0.48 | both halves | 2e-05 |  |
| [[IFT46]] | +0.68 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[SUCLG2-DT]] | +0.67 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[C17orf75]] | +0.67 | +0.66 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRABD]] | -0.61 | -0.65 / -0.32 | both halves | 2e-04 |  |
| [[ERCC2]] | -0.60 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[VKORC1L1]] | -0.59 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[GNB1L]] | -0.59 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[SCART1]] | -0.58 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[ST6GALNAC4]] | -0.58 | -0.58 / -0.24 | both halves | 5e-04 |  |
| [[CORO7]] | -0.58 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[LPCAT1]] | -0.58 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[LPCAT4]] | -0.57 | -0.65 / -0.21 | both halves | 7e-04 |  |
| [[TSEN54]] | -0.57 | -0.57 / -0.28 | both halves | 3e-04 |  |
| [[TMEM120B]] | -0.57 | -0.58 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.577). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-22.1, 22.4); signed map (17.3, -16.7). **Vector** length 94.3, 21.5% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.8 | +13.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +14.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.5 | +7.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.2 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +12.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.2 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +1.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +3.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.5 | -6.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.5 | -5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.1 | -6.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.7 | -6.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.8 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -0.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | phytanoyl-CoA 2-hydroxylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:13,277,796-13,302,412 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PAHX, RD, PHYH1 |
| Gene groups (HGNC) | Iron (II) and 2-oxoglutarate dependent oxygenases |
| Hallmark sets | BILE_ACID_METABOLISM, ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 7 pathways, smallest: Alpha-oxidation of phytanate; TYSND1 cleaves peroxisomal proteins; Peroxisomal lipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O14832](https://www.uniprot.org/uniprotkb/O14832) (Phytanoyl-CoA dioxygenase, peroxisomal):

> Catalyzes the 2-hydroxylation of not only racemic phytanoyl-CoA and the isomers of 3-methylhexadecanoyl-CoA, but also a variety of other mono-branched 3-methylacyl-CoA esters (with a chain length of at least seven carbon atoms) and straight-chain acyl-CoA esters (with a chain length longer than four carbon atoms). Does not hydroxylate long and very long straight chain acyl-CoAs or 2-methyl- and 4-methyl-branched acyl-CoAs.

**Summary**, from NCBI Gene [5264](https://www.ncbi.nlm.nih.gov/gene/5264):

> This gene is a member of the PhyH family and encodes a peroxisomal protein that is involved in the alpha-oxidation of 3-methyl branched fatty acids. Specifically, this protein converts phytanoyl-CoA to 2-hydroxyphytanoyl-CoA. Mutations in this gene have been associated with Refsum disease (RD) and deficient protein activity has been associated with Zellweger syndrome and rhizomelic chondrodysplasia punctata. Alternate transcriptional splice variants, encoding different isoforms, have been …

**Accessions** — [HGNC:8940](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8940) · Entrez [5264](https://www.ncbi.nlm.nih.gov/gene/5264) · UniProt [O14832](https://www.uniprot.org/uniprotkb/O14832) · Ensembl [ENSG00000107537](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107537)

## Data

Gene col 2856: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2856); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2856, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2856]; `tensor/DDL_lfc|DDL_z.npy` [2856]; `embed/gene_vectors.npy` [2856]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2856 or target_col == 2856). Every well: [[PHYH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHYH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
