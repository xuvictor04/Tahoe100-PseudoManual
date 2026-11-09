---
symbol: "EDRF1"
type: "gene"
col: 2900
ensembl_id: "ENSG00000107938"
name: "erythroid differentiation regulatory factor 1"
location: "10q26.2"
module: 179
arm: "+"
pooled_cpm: 60.21
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# EDRF1

*erythroid differentiation regulatory factor 1* — 10q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.04× (z +14.2, q 3e-43, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.460× (z -15.6, q 0e+00, down in 44 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (LS 180 0.0660×, SHP-77 0.102×, SW48 0.110×, SNU-423 0.204×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (RKO 0.151×, COLO 205 0.127×, SW1417 0.247×, PANC-1 0.337×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.104×, C32 0.148×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INTS4]] (+0.74, fdr 7e-06), [[USPL1]] (+0.71, fdr 7e-06), [[MED23]] (+0.66, fdr 7e-06); moves opposite to [[EEA1]] (-0.61, fdr 1e-05), [[HIVEP1]] (-0.60, fdr 1e-05), [[DGKH]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 179]] (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BOLA3-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2900.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.04×** | +14.2 | 3e-43 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +12.2 | 6e-32 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.98×** | +9.7 | 4e-20 | 45/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +8.6 | 1e-15 | 43/48 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.40×** | +7.8 | 7e-13 | 38/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +7.5 | 5e-12 | 42/48 (RKO, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.30×** | +7.3 | 3e-11 | 31/48 (CFPAC-1, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +6.0 | 1e-07 | 35/48 (HEC-1-A, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +5.6 | 2e-06 | 31/48 (RKO, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +5.1 | 2e-05 | 27/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.29×** | +5.1 | 2e-05 | 27/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.30×** | +5.0 | 2e-05 | 26/47 (NCI-H2030, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.5 | 3e-04 | 24/45 (RKO, J82, …) | all doses, flat | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +4.4 | 4e-04 | 23/48 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.35×** | +4.2 | 0.001 | 21/49 (RKO, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.8 | 0.005 | 13/48 (LoVo, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2900.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (LS 180 0.0660×, SHP-77 0.102×, SW48 0.110×, SNU-423 0.204×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (RKO 0.151×, COLO 205 0.127×, SW1417 0.247×, PANC-1 0.337×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.104×, C32 0.148×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.460×** | -15.6 | 0e+00 | 44/49 (RKO, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.462×** | -14.9 | 0e+00 | 37/42 (LS 180, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.595×** | -9.6 | 1e-19 | 34/45 (NCI-H2030, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **0.803×** | -4.4 | 0.001 | 24/47 (SW48, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.794× | -3.3 | 0.11 | 18/48 (LoVo, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.858× | -3.1 | 0.17 | 12/47 (hTERT-HPNE, LoVo, …) | two highest doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.806× | -3.1 | 0.17 | 16/48 (Hs 766T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2900. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 78.6 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.35× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.449× (z -11.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 77.2 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.14× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -13.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 57.6 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.55× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.0660× (z -24.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 52.2 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.30× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -12.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 81.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -15.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 72.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -13.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 69.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 88.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -12.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 51.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.00× (z +12.4) | — |
| [[NCI-H460 (line)]] | wt | 65.4 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.29× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -11.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 71.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -15.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 53.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.06× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -12.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 42.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.08× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 53.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 53.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.74× (z +9.1) ⚠ toxic; cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -19.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 79.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -15.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 63.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.62× (z +8.7) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -18.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 60.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -8.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 52.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -15.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 62.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -15.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 60.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -16.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 58.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -8.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 40.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.395× (z -8.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 56.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -9.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 58.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 49.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 65.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -13.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 81.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -23.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 63.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -11.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 76.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -15.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 75.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 64.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2900), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS4]] | +0.74 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[USPL1]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[MED23]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[NDUFAF7]] | +0.63 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[MED17]] | +0.62 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[IQCB1]] | +0.62 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[RNF121]] | +0.61 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[KHDC4]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[RINT1]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[TFB2M]] | +0.60 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[NUP54]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[HEATR6]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEA1]] | -0.61 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[HIVEP1]] | -0.60 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[DGKH]] | -0.57 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[HIVEP2]] | -0.56 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[TIA1]] | -0.55 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[PHF19]] | -0.53 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[SKIL]] | -0.53 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[TENM3-AS1]] | -0.53 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[ARAP2]] | -0.53 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[MSRA]] | -0.53 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[GYG1]] | -0.53 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[MLLT6]] | -0.52 | -0.35 / -0.54 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BOLA3-DT]] | B | BOLA3-DT activity raises EDRF1's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 1.33× lower at baseline in the lines without BOLA3-DT | 0.034 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **+** arm (projection on the module's main direction 0.641). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-2.1, -16.0); signed map (-35.2, -9.3). **Vector** length 89.6, 22.2% of its response variance represented; |z| ≥ 3 in 1,050 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +6.8 | +7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | +5.6 | +5.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.9 | +12.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +3.9 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.6 | +7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +7.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +1.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +4.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +5.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -9.1 | -0.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.8 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | +2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.2 | -15.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.0 | -3.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.6 | +0.2 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.6 | +0.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | erythroid differentiation regulatory factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.2 — chr10:125,719,515-125,764,143 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp586F1019, FLJ21617; previously C10orf137 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3B7T1](https://www.uniprot.org/uniprotkb/Q3B7T1) (Erythroid differentiation-related factor 1):

> Transcription factor involved in erythroid differentiation. Involved in transcriptional activation of the globin gene.

**Summary**, from NCBI Gene [26098](https://www.ncbi.nlm.nih.gov/gene/26098):

> This gene may play a role in erythroid cell differentiation. The encoded protein inhibits DNA binding of the erythroid transcription factor GATA-1 and may regulate the expression of alpha-globin and gamma-globin. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:24640](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24640) · Entrez [26098](https://www.ncbi.nlm.nih.gov/gene/26098) · UniProt [Q3B7T1](https://www.uniprot.org/uniprotkb/Q3B7T1) · Ensembl [ENSG00000107938](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107938)

## Data

Gene col 2900: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2900); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2900, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2900]; `tensor/DDL_lfc|DDL_z.npy` [2900]; `embed/gene_vectors.npy` [2900]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2900 or target_col == 2900). Every well: [[EDRF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EDRF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
