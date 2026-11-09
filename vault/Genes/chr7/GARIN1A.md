---
symbol: "GARIN1A"
type: "gene"
col: 12947
ensembl_id: "ENSG00000205085"
name: "golgi associated RAB2 interactor 1A"
location: "7q32.1"
module: 39
arm: "+"
pooled_cpm: 10.26
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 23
n_dd_up_clean: 7
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# GARIN1A

*golgi associated RAB2 interactor 1A* — 7q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.77× (z +5.9, q 3e-06, up in 25 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.234× (z -10.6, q 2e-23, down in 35 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.237× (z -10.5, q 3e-23, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYOCOS]] (+0.88, fdr 7e-06), [[SLC6A13]] (+0.87, fdr 7e-06), [[USP50]] (+0.84, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ABCA10]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12947.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.77×** | +5.9 | 3e-06 | 25/45 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +5.5 | 9e-06 | 32/43 (NCI-H23, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.21×** | +4.9 | 1e-04 | 23/48 (NCI-H23, C32, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.55×** | +4.5 | 0.001 | 29/47 (NCI-H23, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +4.2 | 0.004 | 21/43 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +3.5 | 0.045 | 20/44 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.61×** | +3.5 | 0.045 | 18/48 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 5 µM |  | **1.58×** | +3.2 | 0.094 | 12/48 (SW1417, LS 180, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.52× | +3.0 | 0.15 | 15/48 (NCI-H460, SW1417, …) | inconsistent across doses |  |
| [[Tetracycline (hydrochloride) (drug)]] 0.05 µM |  | 1.57× | +3.0 | 0.15 | 16/46 (NCI-H1792, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12947.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.234×** | -10.6 | 2e-23 | 35/43 (J82, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.237×** | -10.5 | 3e-23 | 46/48 (Hs 766T, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.273×** | -9.4 | 7e-19 | 38/48 (LOX-IMVI, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.294×** | -8.9 | 6e-17 | 44/48 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.300×** | -8.8 | 2e-16 | 41/47 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.303×** | -8.7 | 3e-16 | 35/46 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.304×** | -8.7 | 3e-16 | 38/47 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.417×** | -5.7 | 7e-07 | 31/46 (BT-474, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.551×** | -4.2 | 0.002 | 25/44 (SK-MEL-2, A549, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.559×** | -4.0 | 0.004 | 22/45 (Hs 766T, HEC-1-A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.686×** | -3.9 | 0.005 | 26/47 (LoVo, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.572×** | -3.7 | 0.012 | 21/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.582×** | -3.5 | 0.017 | 23/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 5 µM |  | **0.718×** | -3.4 | 0.025 | 19/48 (Hs 766T, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.630×** | -3.4 | 0.027 | 20/43 (Hs 766T, COLO 205, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.414×** | -3.4 | 0.027 | 15/47 (BT-474, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mozavaptan (drug)]] 0.5 µM |  | **0.640×** | -3.3 | 0.038 | 15/47 (SNU-1, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12947. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 8.96 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0306× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 11.3 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0337× (z -14.0) |
| [[LoVo (line)]] | wt | 17.7 | 0 | 4 | — | [[Belumosudil (drug)]] 5 µM 0.0367× (z -17.0) |
| [[LOX-IMVI (line)]] | wt | 9.40 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0570× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0802× (z -10.7) |
| [[A-172 (line)]] | wt | 10.5 | 0 | 3 | — | [[Apalutamide (drug)]] 0.05 µM 0.0764× (z -9.6) |
| [[A-427 (line)]] | wt | 6.70 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0379× (z -10.4) |
| [[J82 (line)]] | alt | 13.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0450× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.146× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 19.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0524× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0756× (z -11.4) |
| [[BT-474 (line)]] | alt | 14.6 | 0 | 2 | — | [[Digitoxin (drug)]] 0.05 µM 0.0251× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 7.37 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0404× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 9.84 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0785× (z -9.4) |
| [[SNU-423 (line)]] | alt | 9.05 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0640× (z -10.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0879× (z -9.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -9.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0431× (z -10.4) |
| [[Hs 766T (line)]] | wt | 7.10 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0362× (z -12.3) |
| [[HT-29 (line)]] | alt | 8.68 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0692× (z -9.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0931× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0726× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~51% of this change |
| [[NCI-H460 (line)]] | wt | 6.31 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -8.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 4.70 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0497× (z -11.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.133× (z -8.5) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 11.1 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0546× (z -10.2) |
| [[SNU-1 (line)]] | wt | 7.32 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.5 µM 0.0459× (z -8.6) |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0684× (z -11.3) |
| [[A498 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12947), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYOCOS]] | +0.88 | +0.87 / +0.81 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.87 | +0.85 / +0.80 | both halves | 7e-06 |  |
| [[USP50]] | +0.84 | +0.85 / +0.75 | both halves | 7e-06 |  |
| [[LINC02803]] | +0.84 | +0.88 / +0.83 | both halves | 7e-06 |  |
| [[GARIN1B]] | +0.84 | +0.81 / +0.81 | both halves | 7e-06 | ⚠ same locus (21.2 kb, same strand: neighbours can correlate without regulation) |
| [[IMPG2]] | +0.83 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | +0.83 | +0.86 / +0.70 | both halves | 7e-06 |  |
| [[PILRA]] | +0.83 | +0.87 / +0.69 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.83 | +0.84 / +0.69 | both halves | 7e-06 |  |
| [[SLC22A1]] | +0.83 | +0.85 / +0.71 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.82 | +0.81 / +0.67 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.81 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[MPP4]] | +0.81 | +0.83 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA10]] | B | ABCA10 activity raises GARIN1A's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.15× lower at baseline in the lines without ABCA10 | 0.021 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |
| [[SEMA4A]] | B | SEMA4A activity raises GARIN1A's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without SEMA4A | 0.061 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[TXK]] | B | TXK activity lowers GARIN1A's level | lines that do not express TXK (7) vs lines expressing it (43) | 1.02× higher at baseline in the lines without TXK | 0.089 | ⚠ within organs, on part of the lines; also absent: TEC; maybe low, not absent; its own permutation p |
| [[GARIN1B]] | C | GARIN1B activity raises GARIN1A's level | lines that do not express GARIN1B (4) vs lines expressing it (46) | 2.37× lower at baseline in the lines without GARIN1B | 0.001 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PGGHG, ALPK1; maybe low, not absent |
| [[STAC3]] | C | STAC3's natural level strengthens GARIN1A's drug response | STAC3's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.12; direction not clear | 0.029 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[MMP25]] | C | MMP25 activity raises GARIN1A's level | lines that do not express MMP25 (3) vs lines expressing it (47) | 1.96× lower at baseline in the lines without MMP25 | 0.091 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000250842, MPP4, KDELR3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.886). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.1, -13.8); signed map (17.7, 8.6). **Vector** length 119, 33.0% of its response variance represented; |z| ≥ 3 in 1,339 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +4.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.1 | +3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.6 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +2.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.6 | -10.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.2 | -8.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.9 | -10.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.6 | -8.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.2 | -8.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -5.2 | -4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.5 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.5 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.7 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | golgi associated RAB2 interactor 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.1 — chr7:128,671,693-128,687,877 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GARI; previously FAM137B, FAM71F2 |
| Gene groups (HGNC) | Golgi associated RAB2 interactor family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NXP2](https://www.uniprot.org/uniprotkb/Q6NXP2) (Golgi-associated RAB2 interactor protein 1A):

> RAB2B effector protein required for accurate acrosome formation and normal male fertility.

**Summary**, from NCBI Gene [346653](https://www.ncbi.nlm.nih.gov/gene/346653):

> Predicted to be involved in acrosome assembly. Predicted to be located in Golgi apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27998](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27998) · Entrez [346653](https://www.ncbi.nlm.nih.gov/gene/346653) · UniProt [Q6NXP2](https://www.uniprot.org/uniprotkb/Q6NXP2) · Ensembl [ENSG00000205085](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205085)

## Data

Gene col 12947: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12947); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12947, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12947]; `tensor/DDL_lfc|DDL_z.npy` [12947]; `embed/gene_vectors.npy` [12947]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12947 or target_col == 12947). Every well: [[GARIN1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GARIN1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
