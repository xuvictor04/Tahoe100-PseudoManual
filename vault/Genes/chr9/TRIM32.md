---
symbol: "TRIM32"
type: "gene"
col: 4061
ensembl_id: "ENSG00000119401"
name: "tripartite motif containing 32"
location: "9q33.1"
module: 17
arm: "+"
pooled_cpm: 8.14
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# TRIM32

*tripartite motif containing 32* — 9q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.65× (z +9.6, q 3e-19, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.487× (z -12.2, q 2e-31, down in 34 of 45 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.495× (z -11.9, q 2e-30, down in 33 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF25]] (+0.63, fdr 1e-05), [[ZNF112]] (+0.63, fdr 7e-06), [[HARS2]] (+0.61, fdr 7e-06); moves opposite to [[MFSD11]] (-0.54, fdr 1e-05), [[LARP1B]] (-0.54, fdr 3e-05), [[EFCAB10]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ZNF71]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4061.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.65×** | +9.6 | 3e-19 | 37/47 (A498, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.49×** | +6.8 | 3e-09 | 24/48 (A498, A-172, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **2.91×** | +6.7 | 4e-09 | 24/42 (HEC-1-A, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +4.1 | 0.005 | 11/45 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.005 | 11/47 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.36×** | +3.7 | 0.019 | 13/46 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.037 | 8/47 (SW480, A549, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 1.30× | +3.1 | 0.14 | 6/47 (KATO III, COLO 205, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.30× | +3.0 | 0.16 | 6/35 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~8% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4061.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.487×** | -12.2 | 2e-31 | 34/45 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.495×** | -11.9 | 2e-30 | 33/44 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.490×** | -8.6 | 2e-15 | 19/29 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.523×** | -7.5 | 1e-11 | 22/43 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.527×** | -7.4 | 2e-11 | 25/37 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.597×** | -5.9 | 3e-07 | 13/17 (HOP62, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.640×** | -5.3 | 7e-06 | 20/43 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.648×** | -5.0 | 4e-05 | 22/43 (SNU-423, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.680×** | -4.6 | 2e-04 | 16/47 (NCI-H460, PANC-1, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.715×** | -4.0 | 0.003 | 16/47 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.731×** | -3.8 | 0.009 | 10/48 (NCI-H460, NCI-H2030, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.748×** | -3.5 | 0.024 | 18/46 (SNU-423, SNU-1, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.732×** | -3.5 | 0.024 | 6/19 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.760×** | -3.2 | 0.063 | 16/46 (NCI-H460, COLO 205, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4061. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 17.3 | 0 | 6 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -12.8) |
| [[HOP62 (line)]] | alt | 8.23 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0750× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 9.10 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0613× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SNU-423 (line)]] | alt | 11.9 | 0 | 4 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0763× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 10.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0992× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -9.5) |
| [[A498 (line)]] | wt | 7.60 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 19.9× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 2 | — | [[Bimatoprost (drug)]] 0.5 µM 0.0929× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 19.3 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -14.1) |
| [[Panc 03.27 (line)]] | alt | 5.51 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -10.7) |
| [[PANC-1 (line)]] | alt | 5.87 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -12.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0889× (z -8.7) |
| [[C32 (line)]] | wt | 6.82 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -9.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 6.07 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0559× (z -8.9) ⚠ cell-cycle shift, explains ~62% of this change |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.106× (z -10.2) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 5.21 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -8.6) |
| [[J82 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -9.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LS 180 (line)]] | wt | 7.61 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -9.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 9.69 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1573 (line)]] | alt | 4.81 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -11.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 4.47 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -10.9) |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0786× (z -9.1) |
| [[SW1417 (line)]] | alt | 6.84 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -9.1) |
| [[SW480 (line)]] | alt | 7.93 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.224× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4061), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF25]] | +0.63 | +0.56 / +0.67 | both halves | 1e-05 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[ZNF112]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[HARS2]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ZNF71]] | +0.61 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[FITM2]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ZNF232]] | +0.60 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[VTA1]] | +0.60 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[ZNF445]] | +0.59 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[ZSCAN20]] | +0.59 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[ZNF30]] | +0.58 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[ZNF484]] | +0.58 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[SNAP47]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD11]] | -0.54 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[LARP1B]] | -0.54 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[EFCAB10]] | -0.52 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[DLEU2]] | -0.50 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[MFSD2B]] | -0.50 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[FAM151B]] | -0.50 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[CCDC146]] | -0.49 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[NPIPB14P]] | -0.49 | -0.41 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF71]] | B | ZNF71 activity raises TRIM32's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 1.28× lower at baseline in the lines without ZNF71 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28 |
| [[TOP2A]] | B | TOP2A activity raises TRIM32's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF420]] | B | ZNF420 activity raises TRIM32's level | lines that do not express ZNF420 (7) vs lines expressing it (43) | 1.45× lower at baseline in the lines without ZNF420 | 0.079 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF850, ZNF540 |
| [[ZNF256]] | B | ZNF256 activity raises TRIM32's level | lines that do not express ZNF256 (14) vs lines expressing it (36) | 1.31× lower at baseline in the lines without ZNF256 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ZNF331, GAMT, ZNF625 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.499). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-29.4, -3.8); signed map (-18.9, -18.6). **Vector** length 76.6, 13.4% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.5 | +9.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.0 | +6.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +5.0 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.6 | -12.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -11.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -7.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -5.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.7 | -7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -3.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[9-ING-41 (drug)]] 0.05 µM |  | -1.3 | -0.2 |
|  | [[Auranofin (drug)]] 0.5 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 32 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.1 — chr9:116,687,305-116,701,300 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HT2A, TATIP, BBS11; previously LGMD2H |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Reactome | 6 pathways, smallest: Regulation of innate immune responses to cytosolic DNA; Cytosolic sensors of pathogen-associated DNA; Antigen processing: Ubiquitination & Proteasome degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13049](https://www.uniprot.org/uniprotkb/Q13049) (E3 ubiquitin-protein ligase TRIM32):

> E3 ubiquitin ligase that plays a role in various biological processes including neural stem cell differentiation, innate immunity, inflammatory resonse and autophagy. Plays a role in virus-triggered induction of IFN-beta and TNF by mediating the ubiquitination of STING1. Mechanistically, targets STING1 for 'Lys-63'-linked ubiquitination which promotes the interaction of STING1 with TBK1. Regulates bacterial clearance and promotes autophagy in Mycobacterium tuberculosis-infected macrophages. …

**Summary**, from NCBI Gene [22954](https://www.ncbi.nlm.nih.gov/gene/22954):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The protein localizes to cytoplasmic bodies. The protein has also been localized to the nucleus, where it interacts with the activation domain of the HIV-1 Tat protein. The Tat protein activates transcription of HIV-1 genes. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16380](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16380) · Entrez [22954](https://www.ncbi.nlm.nih.gov/gene/22954) · UniProt [Q13049](https://www.uniprot.org/uniprotkb/Q13049) · Ensembl [ENSG00000119401](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119401)

## Data

Gene col 4061: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4061); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4061, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4061]; `tensor/DDL_lfc|DDL_z.npy` [4061]; `embed/gene_vectors.npy` [4061]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4061 or target_col == 4061). Every well: [[TRIM32 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM32.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
