---
symbol: "RARS2"
type: "gene"
col: 7083
ensembl_id: "ENSG00000146282"
name: "arginyl-tRNA synthetase 2, mitochondrial"
location: "6q15"
module: 142
arm: "+"
pooled_cpm: 98.02
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# RARS2

*arginyl-tRNA synthetase 2, mitochondrial* — 6q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.41× (z +6.0, q 9e-07, up in 34 of 48 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.28× (z +4.6, q 9e-04, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.561× (z -10.3, q 3e-22, down in 34 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.680× (z -7.2, q 9e-11, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZCCHC17]] (+0.79, fdr 7e-06), [[COPA]] (+0.77, fdr 7e-06), [[RINT1]] (+0.75, fdr 7e-06); moves opposite to [[VEZF1]] (-0.71, fdr 7e-06), [[LIG4]] (-0.67, fdr 7e-06), [[ATF7IP]] (-0.66, fdr 1e-05).
> It is in [[Module 142]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7083.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.41×** | +6.0 | 9e-07 | 34/48 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.35×** | +5.6 | 8e-06 | 31/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.28×** | +4.6 | 9e-04 | 25/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.006 | 25/48 (MIA PaCa-2, A-427, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.51×** | +4.0 | 0.007 | 26/45 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.029 | 22/49 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.3 | 0.075 | 23/48 (J82, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.1 | 0.15 | 21/50 (SK-MEL-2, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7083.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.561×** | -10.3 | 3e-22 | 34/44 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.582×** | -9.3 | 4e-18 | 35/45 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.625×** | -8.7 | 5e-16 | 37/49 (RPMI-7951, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.633×** | -8.2 | 5e-14 | 39/48 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.680×** | -7.2 | 9e-11 | 42/48 (AN3 CA, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **0.738×** | -5.7 | 1e-06 | 33/48 (HOP62, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.809×** | -5.4 | 4e-06 | 25/48 (HOP62, SNU-423, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.757×** | -5.2 | 2e-05 | 31/48 (A-172, H4, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.789×** | -4.4 | 7e-04 | 27/48 (SW48, hTERT-HPNE, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.804×** | -4.1 | 0.003 | 25/48 (LS 180, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.801×** | -4.0 | 0.004 | 28/47 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.812×** | -3.9 | 0.005 | 26/48 (A-172, NCI-H2347, …) | all doses, flat |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.814×** | -3.8 | 0.005 | 29/48 (HS-578T, AsPC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.801×** | -3.8 | 0.005 | 23/47 (hTERT-HPNE, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **0.822×** | -3.6 | 0.010 | 21/48 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.829×** | -3.3 | 0.027 | 22/48 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.841× | -3.2 | 0.039 | 17/49 (SW480, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7083. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 110 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -14.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.431× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 144 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.416× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 142 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.308× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 90.7 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.518× (z -8.6) |
| [[A-172 (line)]] | wt | 82.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -12.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.349× (z -12.3) |
| [[HS-578T (line)]] | alt | 147 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -9.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.431× (z -9.3) |
| [[NCI-H596 (line)]] | alt | 97.7 | 1 | 2 | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 2.16× (z +11.3) | [[Methylthiouracil (drug)]] 0.05 µM 0.249× (z -20.4) |
| [[A-427 (line)]] | wt | 92.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -12.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 122 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.184× (z -12.5) |
| [[KATO III (line)]] | alt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -9.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 187 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -13.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 111 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.501× (z -9.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 96.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.492× (z -8.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 79.1 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.405× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -11.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 86.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -11.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 74.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -9.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 90.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -12.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.406× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 80.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -19.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 79.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -9.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 98.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -12.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 98.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -21.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 76.2 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.297× (z -9.7) |
| [[SW 900 (line)]] | alt | 95.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.381× (z -8.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 83.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -11.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 80.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.313× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[BT-474 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 76.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 103 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 75.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 110 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 97.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 81.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 96.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 61.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7083), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC17]] | +0.79 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[COPA]] | +0.77 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[RINT1]] | +0.75 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[GPR107]] | +0.74 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[SEC23A]] | +0.73 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[ARPC3]] | +0.73 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[SLC30A6]] | +0.72 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[DHDDS]] | +0.72 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[SRP54]] | +0.72 | +0.73 / +0.67 | both halves | 7e-06 | STRING 640 |
| [[RNF121]] | +0.71 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[NDEL1]] | +0.71 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[GOLT1B]] | +0.71 | +0.72 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VEZF1]] | -0.71 | -0.64 / -0.68 | both halves | 7e-06 |  |
| [[LIG4]] | -0.67 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[ATF7IP]] | -0.66 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[CHTOP]] | -0.63 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[TIGD2]] | -0.63 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[PNRC2]] | -0.61 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[RFK]] | -0.61 | -0.67 / -0.49 | both halves | 1e-05 |  |
| [[ZNF260]] | -0.61 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[TSC22D1]] | -0.61 | -0.63 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers RARS2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.807). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.7, -32.3); signed map (-46.8, 6.4). **Vector** length 119, 37.4% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.6 | +6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.0 | +5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.7 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +0.5 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -8.3 | -5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -7.6 | -8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.3 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -6.6 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -3.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.3 | -3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | arginyl-tRNA synthetase 2, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q15 — chr6:87,513,459-87,590,028 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14993, MGC23778, PRO1992, dJ382I10.6, DALRD2; previously RARSL |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class I |
| Reactome | 3 pathways, smallest: Mitochondrial tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T160](https://www.uniprot.org/uniprotkb/Q5T160) (Probable arginine--tRNA ligase, mitochondrial):

> Catalyzes the attachment of arginine to tRNA(Arg) in a two-step reaction: arginine is first activated by ATP to form Arg-AMP and then transferred to the acceptor end of tRNA(Arg).

**Summary**, from NCBI Gene [57038](https://www.ncbi.nlm.nih.gov/gene/57038):

> This nuclear gene encodes a protein that localizes to the mitochondria, where it catalyzes the transfer of L-arginine to its cognate tRNA, an important step in translation of mitochondrially-encoded proteins. Defects in this gene are a cause of pontocerebellar hypoplasia type 6 (PCH6). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:21406](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21406) · Entrez [57038](https://www.ncbi.nlm.nih.gov/gene/57038) · UniProt [Q5T160](https://www.uniprot.org/uniprotkb/Q5T160) · Ensembl [ENSG00000146282](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146282)

## Data

Gene col 7083: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7083); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7083, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7083]; `tensor/DDL_lfc|DDL_z.npy` [7083]; `embed/gene_vectors.npy` [7083]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7083 or target_col == 7083). Every well: [[RARS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RARS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
