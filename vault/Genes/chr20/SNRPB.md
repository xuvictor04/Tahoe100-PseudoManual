---
symbol: "SNRPB"
type: "gene"
col: 4672
ensembl_id: "ENSG00000125835"
name: "small nuclear ribonucleoprotein polypeptides B and B1"
location: "20p13"
module: 71
arm: "+"
pooled_cpm: 81.04
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# SNRPB

*small nuclear ribonucleoprotein polypeptides B and B1* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (18 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.92× (z +9.7, q 2e-19, up in 46 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.43× (z +4.5, q 3e-04, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.617× (z -3.8, q 0.080, down in 36 of 50 measured lines) ⚠ cell-cycle shift, explains ~50% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.236×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FEN1]] (+0.66, fdr 7e-06), [[UHRF1]] (+0.65, fdr 7e-06), [[ZNF876P]] (+0.64, fdr 7e-06); moves opposite to [[PRKAB2]] (-0.67, fdr 1e-05), [[CLIP3]] (-0.65, fdr 1e-05), [[ACTR10]] (-0.60, fdr 1e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF876P]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 18 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4672.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.92×** | +9.7 | 2e-19 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **2.85×** | +9.5 | 9e-19 | 44/49 (A549, NCI-H460, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **2.43×** | +8.0 | 3e-13 | 47/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **2.37×** | +7.2 | 9e-11 | 42/45 (A549, NCI-H1792, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **2.27×** | +7.1 | 1e-10 | 39/44 (NCI-H460, A549, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.95×** | +6.0 | 2e-07 | 43/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.94×** | +6.0 | 2e-07 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~72% of this change | **1.77×** | +5.1 | 2e-05 | 41/48 (HOP62, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~66% of this change | **1.77×** | +5.0 | 4e-05 | 38/47 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.48×** | +4.9 | 5e-05 | 35/49 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.5 | 3e-04 | 38/48 (A-172, SW1417, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.63×** | +4.2 | 0.001 | 38/50 (SNU-423, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.59×** | +4.2 | 0.001 | 32/48 (A549, NCI-H1792, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.60×** | +4.0 | 0.002 | 31/48 (A549, NCI-H1792, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.55×** | +3.9 | 0.003 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.006 | 31/48 (SW480, RPMI-7951, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.024 | 30/48 (HOP62, SW 900, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.046 | 29/47 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.87×** | +2.9 | 0.094 | 29/48 (A549, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4672.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.236×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.617×** | -3.8 | 0.080 | 36/50 (NCI-H23, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 0.480× | -3.4 | 0.18 | 36/50 (NCI-H23, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.688× | -3.2 | 0.30 | 29/48 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.784× | -3.1 | 0.30 | 31/48 (SW480, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.61 per unit of S-phase module lfc, +0.66 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4672. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 80.0 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.15× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[SW480 (line)]] | alt | 117 | 5 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.62× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H1792 (line)]] | alt | 34.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.66× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[PANC-1 (line)]] | alt | 78.4 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.83× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[AsPC-1 (line)]] | alt | 98.7 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +12.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[KATO III (line)]] | alt | 100 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.79× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | — |
| [[NCI-H1573 (line)]] | alt | 29.9 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.62× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H460 (line)]] | wt | 73.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.28× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[HOP62 (line)]] | alt | 100.0 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.20× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A-172 (line)]] | wt | 86.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[A498 (line)]] | wt | 60.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[COLO 205 (line)]] | alt | 76.2 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +8.5) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[HT-29 (line)]] | alt | 56.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[LOX-IMVI (line)]] | wt | 65.6 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.96× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H23 (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.14× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H2347 (line)]] | alt | 88.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +10.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[RKO (line)]] | wt | 166 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[RPMI-7951 (line)]] | alt | 108 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[SNU-423 (line)]] | alt | 72.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[SW 900 (line)]] | alt | 68.6 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.85× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[SW48 (line)]] | wt | 84.0 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.37× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A-427 (line)]] | wt | 69.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 97.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 97.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 123 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 71.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 71.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4672), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FEN1]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[UHRF1]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[ZNF876P]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[HNRNPAB]] | +0.63 | +0.70 / +0.54 | both halves | 1e-05 | STRING 513 |
| [[E2F3]] | +0.62 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[C9orf40]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[EHBP1]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[SMC1A]] | +0.61 | +0.71 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[EIF5A]] | +0.61 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[ZRANB3]] | +0.61 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[CDC25A]] | +0.60 | +0.63 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[PKP4]] | +0.60 | +0.58 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKAB2]] | -0.67 | -0.71 / -0.56 | both halves | 1e-05 |  |
| [[CLIP3]] | -0.65 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[ACTR10]] | -0.60 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[ZFAND1]] | -0.60 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[THAP8]] | -0.59 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[TUBE1]] | -0.58 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[LINC00888-1]] | -0.58 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[USP30]] | -0.58 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[IFT52]] | -0.58 | -0.56 / -0.66 | both halves | 1e-05 |  |
| [[TMEM167B]] | -0.57 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[UFSP2]] | -0.57 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[ABHD4]] | -0.56 | -0.52 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF876P]] | B | ZNF876P activity raises SNRPB's level | lines that do not express ZNF876P (17) vs lines expressing it (33) | 1.32× lower at baseline in the lines without ZNF876P | 0.064 | ⚠ within organs, on part of the lines; also absent: ZNF718, PAX8 |
| [[ZNF367]] | C | ZNF367 activity raises SNRPB's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 1.79× lower at baseline in the lines without ZNF367 | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.479). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.1, -43.3); signed map (4.6, -51.1). **Vector** length 66.1, 25.6% of its response variance represented; |z| ≥ 3 in 1,015 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +4.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +3.4 | +9.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +3.4 | +6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +3.2 | +8.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +3.2 | +6.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +0.3 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.0 | +1.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.0 | +2.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.8 | +2.3 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -0.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | +0.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.9 | -0.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.5 | -0.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear ribonucleoprotein polypeptides B and B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:2,461,634-2,470,853 (-) |
| Ensembl biotype | protein_coding |
| Also known as | COD, SmB/SmB', Sm-B/B', snRNP-B; previously SNRPB1 |
| Gene groups (HGNC) | Sm spliceosomal proteins; Small nucleolar RNA protein coding host genes |
| Hallmark sets | E2F_TARGETS |
| Reactome | 24 pathways, smallest: SLBP independent Processing of Histone Pre-mRNAs; SLBP Dependent Processing of Replication-Dependent Histone Pre-mRNAs; Processing of Capped Intronless Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P14678](https://www.uniprot.org/uniprotkb/P14678) (Small nuclear ribonucleoprotein-associated proteins B and B'):

> Plays a role in pre-mRNA splicing as a core component of the spliceosomal U1, U2, U4 and U5 small nuclear ribonucleoproteins (snRNPs), the building blocks of the spliceosome. Component of both the pre-catalytic spliceosome B complex and activated spliceosome C complexes. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs. As part of the U7 snRNP it is involved in histone pre-mRNA 3'-end processing.

**Summary**, from NCBI Gene [6628](https://www.ncbi.nlm.nih.gov/gene/6628):

> The protein encoded by this gene is one of several nuclear proteins that are found in common among U1, U2, U4/U6, and U5 small ribonucleoprotein particles (snRNPs). These snRNPs are involved in pre-mRNA splicing, and the encoded protein may also play a role in pre-mRNA splicing or snRNP structure. Autoantibodies from patients with systemic lupus erythematosus frequently recognize epitopes on the encoded protein. Two transcript variants encoding different isoforms (B and B') have been found for …

**Accessions** — [HGNC:11153](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11153) · Entrez [6628](https://www.ncbi.nlm.nih.gov/gene/6628) · UniProt [P14678](https://www.uniprot.org/uniprotkb/P14678) · Ensembl [ENSG00000125835](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125835)

## Data

Gene col 4672: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4672); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4672, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4672]; `tensor/DDL_lfc|DDL_z.npy` [4672]; `embed/gene_vectors.npy` [4672]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4672 or target_col == 4672). Every well: [[SNRPB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNRPB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
