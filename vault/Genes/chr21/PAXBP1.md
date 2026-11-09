---
symbol: "PAXBP1"
type: "gene"
col: 8215
ensembl_id: "ENSG00000159086"
name: "PAX3 and PAX7 binding protein 1"
location: "21q22.11"
module: 18
arm: "+"
pooled_cpm: 110.53
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PAXBP1

*PAX3 and PAX7 binding protein 1* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.54× (z +21.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.896× (z -8.9, q 2e-16, down in 3 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.762× (z -6.4, q 5e-08, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (AN3 CA 0.302×, SK-MEL-2 0.434×, SW48 0.443×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Docetaxel (drug)]] 0.05 µM in 2 lines (SW 1271 0.147×, PANC-1 0.567×; ⚠ transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (SW480 0.577×); [[AT7519 (drug)]] 5 µM in 1 line (CHP-212 0.0795×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2I]] (+0.67, fdr 1e-05), [[ARHGEF11]] (+0.62, fdr 1e-05), [[AK3]] (+0.59, fdr 2e-05); moves opposite to [[BCL10]] (-0.59, fdr 1e-05), [[JMJD6]] (-0.57, fdr 1e-05), [[CLIC1]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[IRF6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8215.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.54×** | +21.7 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +18.2 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.93×** | +15.3 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.91×** | +15.1 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +12.9 | 3e-36 | 39/48 (HEC-1-A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.43×** | +10.8 | 3e-25 | 46/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.31×** | +10.2 | 2e-22 | 38/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.49×** | +9.3 | 2e-18 | 32/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.32×** | +9.2 | 2e-18 | 32/49 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +9.1 | 8e-18 | 37/48 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.42×** | +7.9 | 1e-13 | 39/47 (COLO 205, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +7.3 | 1e-11 | 36/48 (NCI-H460, HCT15, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.38×** | +7.2 | 2e-11 | 35/48 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +7.0 | 1e-10 | 29/48 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.34×** | +6.9 | 3e-10 | 37/48 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.32×** | +6.5 | 3e-09 | 32/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +5.7 | 5e-07 | 29/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +4.7 | 6e-05 | 28/48 (CFPAC-1, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.002 | 23/48 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.011 | 18/49 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8215.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (AN3 CA 0.302×, SK-MEL-2 0.434×, SW48 0.443×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Docetaxel (drug)]] 0.05 µM in 2 lines (SW 1271 0.147×, PANC-1 0.567×; ⚠ transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (SW480 0.577×); [[AT7519 (drug)]] 5 µM in 1 line (CHP-212 0.0795×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.896× | -8.9 | 2e-16 | 3/50 (AsPC-1, SW 1271, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.762×** | -6.4 | 5e-08 | 31/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.815×** | -4.8 | 3e-04 | 23/48 (SW 1271, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.866× | -3.4 | 0.10 | 13/48 (Hs 766T, hTERT-HPNE, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.823× | -3.3 | 0.12 | 20/48 (A498, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 0.774× | -3.1 | 0.16 | 16/45 (SNU-1, H4, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | 0.835× | -3.0 | 0.18 | 16/48 (C32, SW48, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8215. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 98.3 | 11 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.31× (z +18.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 3.20× (z +17.8) | — |
| [[SW480 (line)]] | alt | 174 | 8 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.60× (z +24.1) | [[Auranofin (drug)]] 5 µM 0.577× (z -10.2) |
| [[LS 180 (line)]] | wt | 135 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +15.8) | — |
| [[PANC-1 (line)]] | alt | 89.8 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +16.6) | [[Docetaxel (drug)]] 0.05 µM 0.567× (z -8.5) ⚠ transcription drop |
| [[HOP62 (line)]] | alt | 89.7 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +15.0) | — |
| [[BT-474 (line)]] | alt | 89.8 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +11.1) | — |
| [[COLO 205 (line)]] | alt | 80.7 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +14.2) | — |
| [[H4 (line)]] | wt | 98.9 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.07× (z +11.6) | — |
| [[KATO III (line)]] | alt | 70.7 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +12.3) | — |
| [[LoVo (line)]] | wt | 114 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.71× (z +19.0) | — |
| [[NCI-H1573 (line)]] | alt | 77.0 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +13.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 167 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +15.6) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.08× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 118 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +12.0) | — |
| [[HEC-1-A (line)]] | alt | 144 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +15.4) | — |
| [[Hs 766T (line)]] | wt | 59.3 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.98× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 71.0 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +11.6) | — |
| [[NCI-H1792 (line)]] | alt | 97.2 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +11.1) | — |
| [[NCI-H2347 (line)]] | alt | 75.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +13.8) | — |
| [[RKO (line)]] | wt | 192 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +11.9) | — |
| [[SNU-423 (line)]] | alt | 81.5 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +10.4) | — |
| [[SW 900 (line)]] | alt | 94.4 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +10.0) | — |
| [[A-172 (line)]] | wt | 111 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.2) | — |
| [[AsPC-1 (line)]] | alt | 44.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +14.1) | — |
| [[CFPAC-1 (line)]] | alt | 60.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +14.2) | — |
| [[HepG2_C3A (line)]] | wt | 96.8 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 85.7 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +10.8) | — |
| [[hTERT-HPNE (line)]] | wt | 79.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +11.4) | — |
| [[J82 (line)]] | alt | 79.8 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 155 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +11.5) | — |
| [[SNU-1 (line)]] | wt | 169 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.54× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 165 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +11.2) | — |
| [[SW48 (line)]] | wt | 198 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.443× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 139 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +9.9) | — |
| [[A498 (line)]] | wt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +13.3) | — |
| [[A549 (line)]] | wt | 89.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.5) | — |
| [[AN3 CA (line)]] | alt | 269 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 222 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +8.9) | — |
| [[C32 (line)]] | wt | 102 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +9.3) | — |
| [[CHP-212 (line)]] | wt | 150 | 0 | 1 | — | [[AT7519 (drug)]] 5 µM 0.0795× (z -9.6) |
| [[HCT15 (line)]] | alt | 130 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +11.0) | — |
| [[LOX-IMVI (line)]] | wt | 125 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 94.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +8.6) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 97.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 98.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.147× (z -9.1) ⚠ transcription drop |
| [[NCI-H2030 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 84.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8215), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2I]] | +0.67 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ARHGEF11]] | +0.62 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[AK3]] | +0.59 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[MACROH2A2]] | +0.58 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[PKD2]] | +0.58 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[BMPR1A]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[NAF1]] | +0.56 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[TDRD3]] | +0.56 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[NDUFAF6]] | +0.55 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[CIAO2A]] | +0.55 | +0.51 / +0.43 | both halves | 4e-05 |  |
| [[PUM2]] | +0.55 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[RNASEH2B]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL10]] | -0.59 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[JMJD6]] | -0.57 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[CLIC1]] | -0.56 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[ATOSB]] | -0.54 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[KCTD5]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ALAS1]] | -0.52 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[PTPRH]] | -0.52 | -0.50 / -0.43 | both halves | 4e-05 |  |
| [[TOX4]] | -0.51 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[UBC]] | -0.51 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[CREB3]] | -0.50 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[ZNF222]] | -0.50 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[EXOC8]] | -0.50 | -0.33 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRF6]] | B | IRF6 activity lowers PAXBP1's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.18× higher at baseline in the lines without IRF6 | 0.018 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[MVB12B]] | B | MVB12B activity raises PAXBP1's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 1.76× lower at baseline in the lines without MVB12B | 0.058 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.472). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.6, 14.0); signed map (6.9, -4.5). **Vector** length 85.3, 24.7% of its response variance represented; |z| ≥ 3 in 1,283 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.6 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | +5.0 | +7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.5 | +15.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.4 | +7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.1 | +21.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +0.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +4.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +0.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.0 | +1.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.2 | -6.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | +2.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | +7.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.3 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | +0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.6 | +0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.5 | -2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | PAX3 and PAX7 binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:32,733,899-32,771,792 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GCFC, fSAP105; previously C21orf66, GCFC1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5B6](https://www.uniprot.org/uniprotkb/Q9Y5B6) (PAX3- and PAX7-binding protein 1):

> Adapter protein linking the transcription factors PAX3 and PAX7 to the histone methylation machinery and involved in myogenesis. Associates with a histone methyltransferase complex that specifically mediates dimethylation and trimethylation of 'Lys-4' of histone H3. Mediates the recruitment of that complex to the transcription factors PAX3 and PAX7 on chromatin to regulate the expression of genes involved in muscle progenitor cells proliferation including ID3 and CDC20.

**Summary**, from NCBI Gene [94104](https://www.ncbi.nlm.nih.gov/gene/94104):

> Predicted to enable DNA binding activity and histone methyltransferase binding activity. Predicted to be involved in positive regulation of transcription by RNA polymerase II. Predicted to act upstream of or within positive regulation of myoblast proliferation and regulation of skeletal muscle satellite cell proliferation. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13579) · Entrez [94104](https://www.ncbi.nlm.nih.gov/gene/94104) · UniProt [Q9Y5B6](https://www.uniprot.org/uniprotkb/Q9Y5B6) · Ensembl [ENSG00000159086](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159086)

## Data

Gene col 8215: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8215); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8215, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8215]; `tensor/DDL_lfc|DDL_z.npy` [8215]; `embed/gene_vectors.npy` [8215]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8215 or target_col == 8215). Every well: [[PAXBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAXBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
