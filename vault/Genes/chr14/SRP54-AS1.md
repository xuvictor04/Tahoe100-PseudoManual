---
symbol: "SRP54-AS1"
type: "gene"
col: 15132
ensembl_id: "ENSG00000258704"
name: "SRP54 antisense RNA 1"
location: "14q13.2"
module: 40
arm: "+"
pooled_cpm: 40.78
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 27
n_dd_up_clean: 10
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# SRP54-AS1

*SRP54 antisense RNA 1* — 14q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +8.0, q 7e-13, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.488× (z -8.3, q 5e-14, down in 34 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.497× (z -8.1, q 2e-13, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAX]] (+0.80, fdr 7e-06), [[TBC1D22A-DT]] (+0.79, fdr 7e-06), [[ELP2]] (+0.78, fdr 7e-06); moves opposite to [[COMMD10]] (-0.74, fdr 7e-06), [[TMEM185B]] (-0.74, fdr 7e-06), [[PUF60]] (-0.73, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MHENCR]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15132.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +8.0 | 7e-13 | 40/48 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.91×** | +7.5 | 2e-11 | 40/48 (Panc 03.27, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.87×** | +7.3 | 6e-11 | 39/48 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +5.9 | 5e-07 | 36/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +4.6 | 3e-04 | 29/48 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.36×** | +4.6 | 3e-04 | 25/48 (A-427, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +4.6 | 3e-04 | 29/48 (A498, SW48, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.5 | 5e-04 | 29/48 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.46×** | +4.4 | 7e-04 | 30/48 (A-427, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +4.3 | 9e-04 | 33/48 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.03×** | +4.3 | 9e-04 | 36/48 (HEC-1-A, SHP-77, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.012 | 23/48 (COLO 205, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15132.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.488×** | -8.3 | 5e-14 | 34/46 (NCI-H23, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.497×** | -8.1 | 2e-13 | 34/47 (HS-578T, SW 900, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.485×** | -7.7 | 2e-12 | 31/44 (C-33 A, C32, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.551×** | -6.9 | 8e-10 | 41/48 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.570×** | -6.2 | 5e-08 | 28/41 (NCI-H2347, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.590×** | -5.9 | 4e-07 | 31/48 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Megestrol (drug)]] 0.05 µM |  | **0.635×** | -5.3 | 1e-05 | 36/48 (HOP62, A498, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.640×** | -5.2 | 2e-05 | 35/48 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.639×** | -5.0 | 4e-05 | 36/48 (hTERT-HPNE, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.664×** | -4.7 | 1e-04 | 29/48 (RPMI-7951, A498, …) | all doses, flat |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.675×** | -4.5 | 3e-04 | 36/48 (KATO III, A498, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.697×** | -4.2 | 0.001 | 30/48 (NCI-H1573, HEC-1-A, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.697×** | -4.2 | 0.001 | 30/48 (RKO, NCI-H460, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.698×** | -4.1 | 0.001 | 28/48 (HS-578T, SW 900, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.715×** | -3.9 | 0.004 | 29/48 (CFPAC-1, HOP62, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.722×** | -3.8 | 0.006 | 23/48 (A498, J82, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.728×** | -3.7 | 0.008 | 27/48 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.732×** | -3.6 | 0.010 | 25/48 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.735×** | -3.6 | 0.011 | 22/48 (PANC-1, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15132. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 54.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.386× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 58.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -10.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 52.7 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.215× (z -9.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.229× (z -9.1) |
| [[C-33 A (line)]] | alt | 86.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0831× (z -16.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 58.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 26.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +11.0) | — |
| [[SNU-1 (line)]] | wt | 58.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -13.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 50.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -13.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 35.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -9.1) |
| [[C32 (line)]] | wt | 30.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0912× (z -14.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 67.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 35.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.107× (z -12.5) ⚠ toxic; cell-cycle shift, explains ~85% of this change |
| [[HS-578T (line)]] | alt | 41.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 57.3 | 0 | 1 | — | [[OTS514 (drug)]] 5 µM 0.0584× (z -8.6) |
| [[LS 180 (line)]] | wt | 33.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 38.1 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.298× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 42.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 51.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 250 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -9.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 35.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.362× (z -8.9) |
| [[RKO (line)]] | wt | 23.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 37.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 43.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -9.4) |
| [[A-172 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 49.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 32.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15132), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAX]] | +0.80 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[TBC1D22A-DT]] | +0.79 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[ELP2]] | +0.78 | +0.80 / +0.74 | both halves | 7e-06 |  |
| [[PIK3C2A]] | +0.77 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[RAB6A]] | +0.76 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[DPM1]] | +0.74 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.74 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.73 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[NDUFAF7]] | +0.73 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[GPR107]] | +0.72 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[MED26]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[SDHAP1]] | +0.72 | +0.71 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD10]] | -0.74 | -0.73 / -0.67 | both halves | 7e-06 |  |
| [[TMEM185B]] | -0.74 | -0.76 / -0.68 | both halves | 7e-06 |  |
| [[PUF60]] | -0.73 | -0.68 / -0.72 | both halves | 7e-06 |  |
| [[CENPBD1P]] | -0.69 | -0.72 / -0.62 | both halves | 7e-06 |  |
| [[MED1]] | -0.69 | -0.71 / -0.65 | both halves | 7e-06 |  |
| [[ZBTB38]] | -0.69 | -0.67 / -0.66 | both halves | 7e-06 |  |
| [[ZNF518B]] | -0.68 | -0.69 / -0.63 | both halves | 7e-06 |  |
| [[SRCAP]] | -0.68 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[CHTOP]] | -0.68 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[SNX19]] | -0.68 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[ZKSCAN2]] | -0.67 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[RTL6]] | -0.67 | -0.71 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SRP54-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PCNX2]] | B | PCNX2 activity lowers SRP54-AS1's level | lines that do not express PCNX2 (8) vs lines expressing it (42) | 1.56× higher at baseline in the lines without PCNX2 | 0.071 | ⚠ within organs, on part of the lines; also absent: NAALADL2, PLEKHA5, KLHL29; maybe low, not absent |
| [[ENC1]] | B | ENC1 activity lowers SRP54-AS1's level | lines that do not express ENC1 (5) vs lines expressing it (45) | 1.59× higher at baseline in the lines without ENC1 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000285868, NMI, NABP1 |
| [[FAM13A]] | B | FAM13A activity lowers SRP54-AS1's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 1.27× higher at baseline in the lines without FAM13A | 0.084 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[SH3RF1]] | C | SH3RF1 activity lowers SRP54-AS1's level | lines that do not express SH3RF1 (3) vs lines expressing it (47) | 2.56× higher at baseline in the lines without SH3RF1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: LHFPL2, SESTD1, HIPK2; its own permutation p |
| [[PMS2P3]] | C | PMS2P3's natural level strengthens SRP54-AS1's drug response | PMS2P3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.26; direction not clear | 0.078 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MHENCR]] | C | SRP54-AS1's natural level weakens MHENCR's drug response | SRP54-AS1's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.70, reverse -0.04; direction not clear | 0.032 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.800). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (4.8, -18.7); signed map (-42.4, 13.5). **Vector** length 132, 42.5% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +5.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +4.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.9 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +8.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.9 | +2.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.8 | +0.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.7 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +4.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.0 | -8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -8.9 | -2.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -8.1 | -5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.5 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.5 | -4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.5 | -5.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.5 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.4 | -2.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -4.3 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | SRP54 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q13.2 — chr14:34,954,859-34,982,526 (-) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50643](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50643) · Entrez [100506157](https://www.ncbi.nlm.nih.gov/gene/100506157) · Ensembl [ENSG00000258704](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258704)

## Data

Gene col 15132: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15132); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15132, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15132]; `tensor/DDL_lfc|DDL_z.npy` [15132]; `embed/gene_vectors.npy` [15132]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15132 or target_col == 15132). Every well: [[SRP54-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRP54-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
