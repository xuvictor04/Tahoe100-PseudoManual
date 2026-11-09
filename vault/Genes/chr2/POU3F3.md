---
symbol: "POU3F3"
type: "gene"
col: 12734
ensembl_id: "ENSG00000198914"
name: "POU class 3 homeobox 3"
location: "2q12.1"
module: 79
arm: "+"
pooled_cpm: 4.13
n_lines_expressing: 16
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# POU3F3

*POU class 3 homeobox 3* — 2q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.47× (z +9.4, q 4e-18, up in 2 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.00× (z +6.4, q 3e-08, up in 3 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LOX-IMVI 0.1000×, HEC-1-A 0.333×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.280×, AN3 CA 0.265×); [[Harringtonine (drug)]] 5 µM in 2 lines (AN3 CA 0.104×, LOX-IMVI 0.114×); [[Verteporfin (drug)]] 5 µM in 1 line (AN3 CA 0.0391×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RORA]] (+0.56, fdr 2e-04), [[PANTR1]] (+0.55, fdr 1e-05, ⚠ same locus), [[CAPN14]] (+0.55, fdr 2e-05), [[CHST9]] (+0.52, fdr 1e-05); moves opposite to [[AGAP5]] (-0.47, fdr 2e-04), [[MKRN5P]] (-0.46, fdr 4e-04), [[TAF13]] (-0.43, fdr 2e-04).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PANTR1]] → it (grade C ⚠); 5 go from it, the strongest it → [[TMEM266]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12734.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.47×** | +9.4 | 4e-18 | 2/5 (A498, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.09×** | +7.3 | 6e-11 | 2/7 (A498, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.30×** | +6.6 | 7e-09 | 2/5 (NCI-H2030, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +6.4 | 3e-08 | 3/11 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.51×** | +5.7 | 1e-06 | 2/9 (HCT15, NCI-H2030) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +5.4 | 5e-06 | 7/13 (SW480, A-427, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.71×** | +4.2 | 0.003 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +4.1 | 0.003 | 1/11 (A498) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.82×** | +3.9 | 0.006 | 7/13 (A-427, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.80×** | +3.8 | 0.008 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.78×** | +3.7 | 0.010 | 9/13 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +3.6 | 0.015 | 6/13 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LOX-IMVI 0.1000×, HEC-1-A 0.333×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.280×, AN3 CA 0.265×); [[Harringtonine (drug)]] 5 µM in 2 lines (AN3 CA 0.104×, LOX-IMVI 0.114×); [[Verteporfin (drug)]] 5 µM in 1 line (AN3 CA 0.0391×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12734. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 70.8 | 0 | 8 (2 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.0391× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 58.6 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 8.96 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.1000× (z -14.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.114× (z -9.3) |
| [[A-172 (line)]] | wt | 0.422 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.637 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.360 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.547 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.438 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.339 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.521 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.412 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.445 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.785 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.523 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12734), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RORA]] | +0.56 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[PANTR1]] | +0.55 | +0.66 / +0.57 | both halves | 1e-05 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[CAPN14]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[CHST9]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[RETREG1]] | +0.50 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[LINGO2]] | +0.50 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[TMEM266]] | +0.48 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[IGSF3]] | +0.47 | +0.37 / +0.38 | both halves | 8e-05 |  |
| [[RYBP]] | +0.47 | +0.24 / +0.53 | both halves | 4e-04 |  |
| [[PAFAH1B3]] | +0.47 | +0.32 / +0.44 | both halves | 2e-04 |  |
| [[ZBED2]] | +0.46 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[OLFM1]] | +0.46 | +0.31 / +0.45 | both halves | 2e-04 |  |
| [[LINC02899]] | +0.46 | +0.28 / +0.44 | both halves | 3e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGAP5]] | -0.47 | -0.30 / -0.33 | both halves | 2e-04 |  |
| [[MKRN5P]] | -0.46 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[TAF13]] | -0.43 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[AGAP13P]] | -0.42 | -0.28 / -0.34 | both halves | 3e-04 |  |
| [[ZNF587B]] | -0.42 | -0.28 / -0.36 | both halves | 3e-04 |  |
| [[ZNF587]] | -0.40 | -0.29 / -0.35 | both halves | 2e-04 |  |
| [[MAPKAPK5]] | -0.40 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[BMS1P4-1]] | -0.40 | -0.30 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[EFCAB2]] | -0.40 | -0.15 / -0.38 | ⚠ not reproduced | 0.001 |  |
| [[SERPINB9P1]] | -0.39 | -0.19 / -0.25 | ⚠ not reproduced | 8e-04 |  |
| [[UGDH]] | -0.39 | -0.24 / -0.32 | both halves | 5e-04 |  |
| [[TIMM23B-AGAP6]] | -0.38 | -0.20 / -0.43 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PANTR1]] | C | PANTR1 activity raises POU3F3's level | lines that do not express PANTR1 (37) vs lines expressing it (13) | 5.87× lower at baseline in the lines without PANTR1 | 5e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: POU3F3, LINC01508, TIMD4; co-absent with the target |
| [[NELL2]] | C | NELL2 activity raises POU3F3's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 1.99× lower at baseline in the lines without NELL2 | 0.096 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM266]] | B | POU3F3 activity raises TMEM266's level | lines that do not express POU3F3 (34) vs lines expressing it (16) | 1.39× lower at baseline in the lines without POU3F3 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PANTR1, EPGN, ENSG00000244468 |
| [[BCL11A]] | B | POU3F3 activity raises BCL11A's level | lines that do not express POU3F3 (34) vs lines expressing it (16) | 2.25× lower at baseline in the lines without POU3F3 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PANTR1, EPGN, ENSG00000244468 |
| [[PANTR1]] | C | POU3F3 activity raises PANTR1's level | lines that do not express POU3F3 (34) vs lines expressing it (16) | 3.53× lower at baseline in the lines without POU3F3 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PANTR1, EPGN, ENSG00000244468; co-absent with the target |
| [[GHR]] | C | POU3F3 activity raises GHR's level | lines that do not express POU3F3 (34) vs lines expressing it (16) | 4.93× lower at baseline in the lines without POU3F3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PANTR1, EPGN, ENSG00000244468; co-absent with the target |
| [[ANKRD20A7P]] | C | POU3F3 activity raises ANKRD20A7P's level | lines that do not express POU3F3 (34) vs lines expressing it (16) | 1.47× lower at baseline in the lines without POU3F3 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PANTR1, EPGN, ENSG00000244468; co-absent with the target |

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.405). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.0, 41.8); signed map (50.7, 36.3). **Vector** length 28.0, 6.08% of its response variance represented; |z| ≥ 3 in 320 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.7 | +3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.4 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.3 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.2 | +7.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.9 | -0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.7 | +2.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.7 | +2.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.6 | +1.7 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -0.8 | -0.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.8 | -0.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.8 | -1.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.7 | -0.2 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.7 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -2.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.6 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | POU class 3 homeobox 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q12.1 — chr2:104,853,287-104,858,574 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BRN1, OTF8 |
| Gene groups (HGNC) | POU class homeoboxes and pseudogenes |
| Reactome | 2 pathways, smallest: Nephron development; Kidney development |
| Matched by | ensembl_id |

**Function**, from UniProt [P20264](https://www.uniprot.org/uniprotkb/P20264) (POU domain, class 3, transcription factor 3):

> Transcription factor that acts synergistically with SOX11 and SOX4. Plays a role in neuronal development. Is implicated in an enhancer activity at the embryonic met-mesencephalic junction; the enhancer element contains the octamer motif (5'-ATTTGCAT-3') (By similarity).

**Summary**, from NCBI Gene [5455](https://www.ncbi.nlm.nih.gov/gene/5455):

> This gene encodes a POU-domain containing protein that functions as a transcription factor. The encoded protein recognizes an octamer sequence in the DNA of target genes. This protein may play a role in development of the nervous system. [provided by RefSeq, Apr 2015]

**Accessions** — [HGNC:9216](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9216) · Entrez [5455](https://www.ncbi.nlm.nih.gov/gene/5455) · UniProt [P20264](https://www.uniprot.org/uniprotkb/P20264) · Ensembl [ENSG00000198914](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198914)

## Data

Gene col 12734: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12734); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12734, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12734]; `tensor/DDL_lfc|DDL_z.npy` [12734]; `embed/gene_vectors.npy` [12734]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12734 or target_col == 12734). Every well: [[POU3F3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POU3F3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
