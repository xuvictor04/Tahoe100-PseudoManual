---
symbol: "NT5E"
type: "gene"
col: 5682
ensembl_id: "ENSG00000135318"
name: "5'-nucleotidase ecto"
location: "6q14.3"
module: 147
arm: "+"
pooled_cpm: 121.19
n_lines_expressing: 36
n_dd_up: 8
n_dd_down: 78
n_dd_up_clean: 5
n_dd_down_clean: 67
in_vector_space: true
direction_upstream: 22
direction_downstream: 18
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# NT5E

*5'-nucleotidase ecto* — 6q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.05× (z +8.5, q 1e-14, up in 24 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 1.33× (z +3.6, q 0.050, up in 20 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 78 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.191× (z -28.5, q 0e+00, down in 34 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANTXR2]] (+0.79, fdr 7e-06), [[DCBLD2]] (+0.78, fdr 7e-06), [[ITGA2]] (+0.78, fdr 7e-06); moves opposite to [[EDN2]] (-0.60, fdr 1e-05), [[MBNL2]] (-0.56, fdr 1e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[S100A16]] → it (grade B ⚠); 18 go from it, the strongest it → [[IL15]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5682.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +8.5 | 1e-14 | 24/31 (Panc 03.27, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +8.2 | 7e-14 | 25/35 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.63×** | +5.5 | 6e-06 | 24/31 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.050 | 20/34 (LOX-IMVI, Hs 766T, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.052 | 20/34 (Hs 766T, SW 1271, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Busulfan (drug)]] 0.05 µM |  | **1.32×** | +3.5 | 0.052 | 16/35 (A-172, A549, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.092 | 18/34 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.2 | 0.097 | 16/33 (RPMI-7951, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 1.29× | +3.1 | 0.11 | 17/35 (Hs 766T, LOX-IMVI, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.28× | +3.1 | 0.12 | 17/35 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 78 in all, 11 with an alert ⚠; shown: the 15 strongest. 78 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5682.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.191×** | -28.5 | 0e+00 | 34/34 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.216×** | -18.6 | 0e+00 | 32/34 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.233×** | -17.4 | 0e+00 | 34/36 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.263×** | -16.2 | 0e+00 | 33/34 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.350×** | -15.9 | 0e+00 | 32/34 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.290×** | -14.5 | 1e-45 | 30/34 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.311×** | -14.2 | 7e-44 | 33/34 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.298×** | -14.2 | 1e-43 | 30/33 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.312×** | -14.2 | 1e-43 | 31/34 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.314×** | -14.1 | 2e-43 | 32/35 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.384×** | -13.9 | 2e-42 | 31/34 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.334×** | -13.4 | 2e-39 | 33/35 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.480×** | -12.6 | 9e-35 | 29/35 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.348×** | -12.3 | 2e-33 | 30/34 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.395×** | -11.3 | 7e-28 | 24/34 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5682. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 180 | 0 | 32 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0738× (z -40.4) |
| [[MIA PaCa-2 (line)]] | alt | 346 | 0 | 25 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.287× (z -41.5) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.101× (z -31.6) |
| [[NCI-H23 (line)]] | alt | 174 | 0 | 25 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0630× (z -30.3) |
| [[PANC-1 (line)]] | alt | 263 | 0 | 24 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0499× (z -33.8) |
| [[HOP62 (line)]] | alt | 201 | 0 | 23 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.115× (z -18.6) |
| [[SK-MEL-2 (line)]] | alt | 181 | 0 | 23 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -24.8) |
| [[SW48 (line)]] | wt | 159 | 0 | 23 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -23.8) |
| [[HEC-1-A (line)]] | alt | 183 | 0 | 20 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -21.5) |
| [[NCI-H1573 (line)]] | alt | 93.7 | 0 | 18 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0780× (z -24.1) |
| [[A-172 (line)]] | wt | 261 | 0 | 17 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -21.7) |
| [[RPMI-7951 (line)]] | alt | 290 | 0 | 15 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -22.8) |
| [[SW 900 (line)]] | alt | 180 | 0 | 15 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -20.5) |
| [[LOX-IMVI (line)]] | wt | 212 | 0 | 14 | — | [[Panobinostat (drug)]] 5 µM 0.0748× (z -20.0) |
| [[A549 (line)]] | wt | 94.0 | 0 | 12 | — | [[Homoharringtonine (drug)]] 5 µM 0.0524× (z -26.2) |
| [[CFPAC-1 (line)]] | alt | 76.2 | 1 (1 ⚠) | 11 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +8.6) ⚠ toxic; transcription drop | [[Binimetinib (drug)]] 0.5 µM 0.203× (z -16.2) |
| [[HS-578T (line)]] | alt | 155 | 0 | 12 | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -12.9) |
| [[J82 (line)]] | alt | 146 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0965× (z -27.0) |
| [[LS 180 (line)]] | wt | 85.7 | 0 | 12 | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -14.4) |
| [[AsPC-1 (line)]] | alt | 159 | 0 | 10 | — | [[Panobinostat (drug)]] 5 µM 0.185× (z -14.2) |
| [[NCI-H1792 (line)]] | alt | 82.7 | 0 | 10 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.542× (z -14.8) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.274× (z -12.7) |
| [[hTERT-HPNE (line)]] | wt | 318 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -19.6) |
| [[NCI-H2030 (line)]] | alt | 157 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.0617× (z -32.3) |
| [[NCI-H2347 (line)]] | alt | 136 | 4 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -17.7) |
| [[SNU-423 (line)]] | alt | 180 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -14.8) |
| [[Panc 03.27 (line)]] | alt | 61.8 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 5.26× (z +12.4) ⚠ toxic; transcription drop | [[Binimetinib (drug)]] 0.5 µM 0.344× (z -10.0) |
| [[LoVo (line)]] | wt | 40.4 | 0 | 5 | — | [[Trametinib (drug)]] 5 µM 0.230× (z -9.6) |
| [[SW 1271 (line)]] | alt | 458 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -16.0) |
| [[Hs 766T (line)]] | wt | 123 | 0 | 4 | — | [[Cobimetinib (drug)]] 5 µM 0.268× (z -9.6) |
| [[A498 (line)]] | wt | 30.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -16.1) |
| [[HT-29 (line)]] | alt | 37.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.67× (z +11.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 31.4 | 0 | 1 | — | [[Trametinib (drug)]] 0.5 µM 0.324× (z -9.1) |
| [[CHP-212 (line)]] | wt | 78.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -9.1) |
| [[AN3 CA (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.85 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.50 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 17.4 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 20.8 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 26.8 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 25.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 27.6 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.01 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.7 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 20.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5682), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANTXR2]] | +0.79 | +0.79 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[DCBLD2]] | +0.78 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.78 | +0.79 / +0.78 | both halves | 7e-06 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 482 |
| [[LINC02454]] | +0.75 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[ITGB5]] | +0.73 | +0.75 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[LINC00941]] | +0.73 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[PHLDA1]] | +0.72 | +0.73 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[RPSAP52]] | +0.72 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[SPRY4-AS1]] | +0.70 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[HMGA2]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[ELK3]] | +0.69 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.69 | +0.71 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDN2]] | -0.60 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[MBNL2]] | -0.56 | -0.56 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 18, C 4. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100A16]] | B | S100A16 activity raises NT5E's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 4.00× lower at baseline in the lines without S100A16 | 0.023 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[CD44]] | B | CD44 activity raises NT5E's level | lines that do not express CD44 (15) vs lines expressing it (35) | 4.15× lower at baseline in the lines without CD44 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[TOR4A]] | B | TOR4A activity raises NT5E's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 2.43× lower at baseline in the lines without TOR4A | 0.028 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[VEGFC]] | B | VEGFC activity raises NT5E's level | lines that do not express VEGFC (22) vs lines expressing it (28) | 2.96× lower at baseline in the lines without VEGFC | 0.032 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1 |
| [[C13orf46]] | B | C13orf46 activity raises NT5E's level | lines that do not express C13orf46 (11) vs lines expressing it (39) | 2.93× lower at baseline in the lines without C13orf46 | 0.034 | ⚠ within organs, on part of the lines; also absent: RASA3, COL27A1, PRR5L |
| [[NLRP3]] | B | NLRP3 activity raises NT5E's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 3.37× lower at baseline in the lines without NLRP3 | 0.036 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |
| [[ITGA2]] | B | ITGA2 activity raises NT5E's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 3.13× lower at baseline in the lines without ITGA2 | 0.038 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[RNF182]] | B | RNF182 activity raises NT5E's level | lines that do not express RNF182 (22) vs lines expressing it (28) | 3.18× lower at baseline in the lines without RNF182 | 0.045 | ⚠ within organs, on part of the lines; also absent: PTX3, FZD8, ENSG00000230615 |
| [[IL15]] | B | IL15 activity raises NT5E's level | lines that do not express IL15 (10) vs lines expressing it (40) | 2.98× lower at baseline in the lines without IL15 | 0.045 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[RAC2]] | B | RAC2 activity raises NT5E's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 3.13× lower at baseline in the lines without RAC2 | 0.057 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[FOSL1]] | B | FOSL1 activity raises NT5E's level | lines that do not express FOSL1 (5) vs lines expressing it (45) | 7.14× lower at baseline in the lines without FOSL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PLS3, ENSG00000281883, NIBAN2; its own permutation p |
| [[SMOX]] | B | SMOX activity raises NT5E's level | lines that do not express SMOX (6) vs lines expressing it (44) | 3.53× lower at baseline in the lines without SMOX | 0.060 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 18, C 0. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL15]] | B | NT5E activity raises IL15's level | lines that do not express NT5E (14) vs lines expressing it (36) | 2.78× lower at baseline in the lines without NT5E | 0.004 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |
| [[VGF]] | B | NT5E activity lowers VGF's level | lines that do not express NT5E (14) vs lines expressing it (36) | 1.89× higher at baseline in the lines without NT5E | 0.017 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |
| [[TFPI2]] | B | NT5E activity raises TFPI2's level | lines that do not express NT5E (14) vs lines expressing it (36) | 4.81× lower at baseline in the lines without NT5E | 0.018 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |
| [[ITPRID2]] | B | NT5E activity raises ITPRID2's level | lines that do not express NT5E (14) vs lines expressing it (36) | 1.66× lower at baseline in the lines without NT5E | 0.022 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |
| [[F2R]] | B | NT5E activity raises F2R's level | lines that do not express NT5E (14) vs lines expressing it (36) | 3.24× lower at baseline in the lines without NT5E | 0.033 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |
| [[CD44]] | B | NT5E activity raises CD44's level | lines that do not express NT5E (14) vs lines expressing it (36) | 4.22× lower at baseline in the lines without NT5E | 0.045 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |
| [[FOSL1]] | B | NT5E activity raises FOSL1's level | lines that do not express NT5E (14) vs lines expressing it (36) | 2.03× lower at baseline in the lines without NT5E | 0.048 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |
| [[MIR31HG]] | B | NT5E activity raises MIR31HG's level | lines that do not express NT5E (14) vs lines expressing it (36) | 2.58× lower at baseline in the lines without NT5E | 0.049 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |
| [[KIF13A]] | B | NT5E activity raises KIF13A's level | lines that do not express NT5E (14) vs lines expressing it (36) | 1.30× lower at baseline in the lines without NT5E | 0.059 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |
| [[LAMC2]] | B | NT5E activity raises LAMC2's level | lines that do not express NT5E (14) vs lines expressing it (36) | 2.17× lower at baseline in the lines without NT5E | 0.068 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |
| [[MYEOV]] | B | NT5E activity raises MYEOV's level | lines that do not express NT5E (14) vs lines expressing it (36) | 1.60× lower at baseline in the lines without NT5E | 0.073 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |
| [[GJA1]] | B | NT5E activity raises GJA1's level | lines that do not express NT5E (14) vs lines expressing it (36) | 3.25× lower at baseline in the lines without NT5E | 0.074 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.798). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.7, 7.2); signed map (8.1, 46.1). **Vector** length 139, 51.9% of its response variance represented; |z| ≥ 3 in 1,907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +5.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.9 | -18.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.9 | -16.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +8.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +1.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +3.4 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +3.6 |
|  | [[Dabrafenib (drug)]] 5 µM |  | +2.7 | +1.1 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +2.6 | +2.6 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -11.5 | -15.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -11.4 | -17.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -10.1 | -13.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -10.0 | -14.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -9.6 | -12.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -9.4 | -14.2 |

## What is on record

|  |  |
|---|---|
| Name | 5'-nucleotidase ecto |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.3 — chr6:85,449,584-85,495,791 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD73, eN, eNT, CALJA; previously NT5 |
| Gene groups (HGNC) | CD molecules; 5'-nucleotidases |
| Hallmark sets | IL2_STAT5_SIGNALING, GLYCOLYSIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 11 pathways, smallest: Pyrimidine catabolism; Purine catabolism; Cell recruitment (pro-inflammatory response) |
| Matched by | ensembl_id |

**Function**, from UniProt [P21589](https://www.uniprot.org/uniprotkb/P21589) (5'-nucleotidase):

> Catalyzes the hydrolysis of nucleotide monophosphates, releasing inorganic phosphate and the corresponding nucleoside, with AMP being the preferred substrate. Shows a preference for ribonucleotide monophosphates over their equivalent deoxyribose forms. Other substrates include IMP, UMP, GMP, CMP, dAMP, dCMP, dTMP, NAD and NMN.

**Summary**, from NCBI Gene [4907](https://www.ncbi.nlm.nih.gov/gene/4907):

> The protein encoded by this gene is a plasma membrane protein that catalyzes the conversion of extracellular nucleotides to membrane-permeable nucleosides. The encoded protein is used as a determinant of lymphocyte differentiation. Defects in this gene can lead to the calcification of joints and arteries. Two transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:8021](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8021) · Entrez [4907](https://www.ncbi.nlm.nih.gov/gene/4907) · UniProt [P21589](https://www.uniprot.org/uniprotkb/P21589) · Ensembl [ENSG00000135318](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135318)

## Data

Gene col 5682: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5682); `tables/drug_effects.parquet` (88 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5682, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5682]; `tensor/DDL_lfc|DDL_z.npy` [5682]; `embed/gene_vectors.npy` [5682]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5682 or target_col == 5682). Every well: [[NT5E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NT5E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
