---
symbol: "MMGT1"
type: "gene"
col: 9810
ensembl_id: "ENSG00000169446"
name: "membrane magnesium transporter 1"
location: "Xq26.3"
module: 25
arm: "+"
pooled_cpm: 23.98
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# MMGT1

*membrane magnesium transporter 1* — Xq26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.26× (z +19.9, q 0e+00, up in 42 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.65× (z +8.5, q 4e-15, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.919× (z -4.7, q 0.001, down in 3 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[BAY1125976 (drug)]] 0.5 µM: 0.705× (z -4.2, q 0.008, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0622×); [[Bortezomib (drug)]] 5 µM in 1 line (SK-MEL-2 0.0998×; ⚠ toxic); [[Silodosin (drug)]] 5 µM in 1 line (C32 0.153×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (HS-578T 0.249×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TGOLN2]] (+0.79, fdr 7e-06), [[MOB1A]] (+0.77, fdr 7e-06), [[LIN7C]] (+0.76, fdr 1e-05); moves opposite to [[SMIM26]] (-0.66, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[SUMO4]] (-0.65, fdr 1e-05), [[ZNF503]] (-0.64, fdr 3e-05), [[CCDC174]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[AKT1]], [[AKT2]], [[AKT3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9810.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.26×** | +19.9 | 0e+00 | 42/43 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.38×** | +19.8 | 0e+00 | 32/32 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.19×** | +12.3 | 3e-32 | 33/38 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +8.5 | 4e-15 | 38/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +7.1 | 2e-10 | 29/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +6.3 | 3e-08 | 27/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +6.2 | 5e-08 | 29/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +5.7 | 1e-06 | 28/47 (LoVo, LS 180, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +5.6 | 2e-06 | 27/48 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +5.4 | 4e-06 | 24/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +5.1 | 2e-05 | 22/48 (J82, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +5.1 | 2e-05 | 23/47 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +4.8 | 6e-05 | 23/45 (SW1417, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **1.28×** | +4.0 | 0.002 | 18/44 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.21×** | +3.2 | 0.056 | 5/47 (AsPC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.072 | 5/48 (NCI-H1573, SW1417, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.081 | 4/48 (HEC-1-A, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9810.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0622×); [[Bortezomib (drug)]] 5 µM in 1 line (SK-MEL-2 0.0998×; ⚠ toxic); [[Silodosin (drug)]] 5 µM in 1 line (C32 0.153×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (HS-578T 0.249×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.919× | -4.7 | 0.001 | 3/48 (SW48, NCI-H661, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **0.705×** | -4.2 | 0.008 | 19/48 (SW 900, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.729×** | -3.8 | 0.030 | 17/45 (NCI-H460, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.824× | -3.2 | 0.17 | 16/47 (SW1417, J82, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.820× | -3.1 | 0.17 | 15/48 (CHP-212, SK-MEL-2, …) | all doses, flat |  |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | 0.864× | -3.1 | 0.17 | 13/48 (COLO 205, PANC-1, …) | top dose only |  |
| [[Bergenin (drug)]] 0.5 µM |  | 0.831× | -3.1 | 0.17 | 12/48 (SHP-77, A549, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 0.709× | -3.0 | 0.19 | 15/40 (SK-MEL-2, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9810. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 12.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.77× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 26.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +13.3) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 39.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.58× (z +11.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 21.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.46× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 17.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +9.4) ⚠ toxic; transcription drop | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.249× (z -8.9) |
| [[HT-29 (line)]] | alt | 25.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.78× (z +11.7) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 16.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.20× (z +9.3) ⚠ toxic; transcription drop | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.190× (z -8.5) |
| [[J82 (line)]] | alt | 25.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 19.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.32× (z +15.2) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 23.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.28× (z +12.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 14.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.68× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 35.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 17.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 20.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.25× (z +11.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 29.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +12.1) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 16.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +8.5) ⚠ toxic; transcription drop | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0622× (z -15.2) |
| [[SK-MEL-2 (line)]] | alt | 40.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +12.4) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.0998× (z -9.9) ⚠ toxic |
| [[A549 (line)]] | wt | 22.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.19× (z +13.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 34.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +9.4) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 13.3 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.153× (z -9.0) |
| [[Hs 766T (line)]] | wt | 28.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.31× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 24.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +11.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 34.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +9.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 11.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 37.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9810), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGOLN2]] | +0.79 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[MOB1A]] | +0.77 | +0.72 / +0.84 | both halves | 7e-06 |  |
| [[LIN7C]] | +0.76 | +0.52 / +0.84 | both halves | 1e-05 |  |
| [[TMX1]] | +0.73 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[VAMP3]] | +0.73 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[TMEM30A]] | +0.71 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[ERLIN2]] | +0.70 | +0.45 / +0.76 | both halves | 3e-05 |  |
| [[FAM91A1]] | +0.70 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[PPT1]] | +0.69 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[VMA21]] | +0.69 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[TWF1]] | +0.69 | +0.49 / +0.85 | both halves | 1e-05 |  |
| [[AP2M1]] | +0.69 | +0.58 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | -0.66 | -0.54 / -0.70 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SUMO4]] | -0.65 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[ZNF503]] | -0.64 | -0.46 / -0.70 | both halves | 3e-05 |  |
| [[CCDC174]] | -0.64 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[NSUN5P1-1]] | -0.64 | -0.54 / -0.70 | both halves | 1e-05 |  |
| [[CTBP1-AS]] ⚠ | -0.64 | -0.61 / -0.62 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF593]] | -0.63 | -0.41 / -0.70 | both halves | 4e-05 |  |
| [[ADPRS]] | -0.63 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[TMEM258]] | -0.63 | -0.38 / -0.73 | both halves | 6e-05 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[ZNF3]] | -0.62 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[SNHG8]] | -0.62 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[ADPRM]] | -0.61 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[AKAP8L]] | -0.61 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[NKAP]] | -0.61 | -0.51 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKT1]], [[AKT2]], [[AKT3]] | B | AKT1, AKT2, AKT3 activity raises MMGT1's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 0.6% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.752). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.7, -21.7); signed map (-18.0, -37.5). **Vector** length 96.9, 20.9% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.8 | +19.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.8 | +19.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.7 | +12.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.5 | +8.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +3.9 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +5.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +3.0 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +2.1 | +2.6 |
|  | [[Erlotinib (drug)]] 5 µM |  | +2.1 | +1.2 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +1.9 | +1.5 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -3.9 | -3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | -3.4 | -3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.8 | -2.8 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.6 | -4.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.5 | -2.7 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | membrane magnesium transporter 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.3 — chrX:135,960,588-135,974,029 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EMC5; previously TMEM32 |
| Gene groups (HGNC) | ER membrane protein complex subunits |
| Reactome | 4 pathways, smallest: Miscellaneous transport and binding events; Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4V1](https://www.uniprot.org/uniprotkb/Q8N4V1) (ER membrane protein complex subunit 5):

> Part of the endoplasmic reticulum membrane protein complex (EMC) that enables the energy-independent insertion into endoplasmic reticulum membranes of newly synthesized membrane proteins. Preferentially accommodates proteins with transmembrane domains that are weakly hydrophobic or contain destabilizing features such as charged and aromatic residues. Involved in the cotranslational insertion of multi-pass membrane proteins in which stop-transfer membrane-anchor sequences become ER membrane …

**Summary**, from NCBI Gene [93380](https://www.ncbi.nlm.nih.gov/gene/93380):

> Contributes to membrane insertase activity. Involved in protein insertion into ER membrane by stop-transfer membrane-anchor sequence and tail-anchored membrane protein insertion into ER membrane. Located in endoplasmic reticulum membrane. Part of EMC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28100](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28100) · Entrez [93380](https://www.ncbi.nlm.nih.gov/gene/93380) · UniProt [Q8N4V1](https://www.uniprot.org/uniprotkb/Q8N4V1) · Ensembl [ENSG00000169446](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169446)

## Data

Gene col 9810: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9810); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9810, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9810]; `tensor/DDL_lfc|DDL_z.npy` [9810]; `embed/gene_vectors.npy` [9810]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9810 or target_col == 9810). Every well: [[MMGT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMGT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
