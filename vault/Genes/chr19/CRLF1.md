---
symbol: "CRLF1"
type: "gene"
col: 98
ensembl_id: "ENSG00000006016"
name: "cytokine receptor like factor 1"
location: "19p12"
module: 21
arm: "+"
pooled_cpm: 5.8
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# CRLF1

*cytokine receptor like factor 1* — 19p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.01× (z +15.6, q 0e+00, up in 36 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-172 0.228×, H4 0.0884×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.238×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 0.211×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKAP13-AS1]] (+0.75, fdr 1e-05), [[SLC26A5]] (+0.69, fdr 1e-05), [[FAM217A]] (+0.69, fdr 1e-05); moves opposite to [[DCLRE1A]] (-0.56, fdr 1e-04), [[SENP1]] (-0.54, fdr 4e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CECR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 98.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.01×** | +15.6 | 0e+00 | 36/40 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.00×** | +10.6 | 8e-24 | 5/7 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.97×** | +9.6 | 2e-19 | 32/47 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.54×** | +9.4 | 1e-18 | 20/25 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.23×** | +8.0 | 1e-13 | 31/45 (SW480, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.17×** | +7.8 | 7e-13 | 29/47 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +6.8 | 1e-09 | 5/11 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.82×** | +6.0 | 1e-07 | 22/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +5.5 | 2e-06 | 18/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.66×** | +5.1 | 2e-05 | 21/47 (PANC-1, J82, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.53×** | +4.3 | 9e-04 | 13/40 (NCI-H460, J82, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +4.2 | 0.002 | 15/44 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.1 | 0.002 | 7/32 (SHP-77, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.1 | 0.002 | 12/25 (NCI-H2030, H4, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.45×** | +3.6 | 0.012 | 11/39 (NCI-H460, SW480, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.036 | 6/41 (A498, A549, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.61×** | +3.2 | 0.037 | 3/42 (NCI-H2030, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.57×** | +3.1 | 0.063 | 3/37 (A-172, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 98.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-172 0.228×, H4 0.0884×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.238×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 0.211×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.708× | -3.5 | 0.29 | 14/40 (A-172, H4, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 98. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 28.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.211× (z -10.0) |
| [[SW480 (line)]] | alt | 3.27 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.10× (z +11.8) | — |
| [[A498 (line)]] | wt | 3.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.83× (z +10.3) | — |
| [[A549 (line)]] | wt | 2.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.9× (z +11.8) | — |
| [[H4 (line)]] | wt | 11.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0884× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 2.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.54× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 5.69 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.1× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 6.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.41× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 2.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.81× (z +9.4) | — |
| [[A-427 (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 78.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 98), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP13-AS1]] | +0.75 | +0.49 / +0.81 | both halves | 1e-05 |  |
| [[SLC26A5]] | +0.69 | +0.53 / +0.78 | both halves | 1e-05 |  |
| [[FAM217A]] | +0.69 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[RN7SL2]] | +0.69 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[NFATC2IP-AS1]] | +0.69 | +0.46 / +0.73 | both halves | 2e-05 |  |
| [[EFCAB14-AS1]] | +0.69 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[TICAM2-AS1]] | +0.66 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[UBOX5-AS1]] | +0.66 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[LRRC75A]] | +0.66 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[ZRANB2-AS1]] | +0.64 | +0.46 / +0.70 | both halves | 2e-05 |  |
| [[ATP6V1C2]] | +0.64 | +0.42 / +0.72 | both halves | 4e-05 |  |
| [[DDN-AS1]] | +0.64 | +0.36 / +0.72 | both halves | 1e-04 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCLRE1A]] | -0.56 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[SENP1]] | -0.54 | -0.40 / -0.57 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CECR2]] | B | CECR2 activity raises CRLF1's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 1.34× lower at baseline in the lines without CECR2 | 0.060 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent |
| [[RET]] | B | RET activity raises CRLF1's level | lines that do not express RET (28) vs lines expressing it (22) | 1.54× lower at baseline in the lines without RET | 0.067 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[RTN4RL1]] | B | RTN4RL1 activity raises CRLF1's level | lines that do not express RTN4RL1 (14) vs lines expressing it (36) | 1.70× lower at baseline in the lines without RTN4RL1 | 0.083 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.678). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.0, 30.0); signed map (35.1, 6.7). **Vector** length 61.0, 9.21% of its response variance represented; |z| ≥ 3 in 814 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +15.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +9.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +10.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +8.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +1.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +1.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.7 | -3.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -1.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -2.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -1.8 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -1.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | cytokine receptor like factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p12 — chr19:18,572,220-18,607,741 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CLF-1, CLF, CISS, CISS1 |
| Gene groups (HGNC) | Fibronectin type III domain containing |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 6 pathways, smallest: Interleukin-27 signaling; IL-6-type cytokine receptor ligand interactions; Interleukin-6 family signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O75462](https://www.uniprot.org/uniprotkb/O75462) (Cytokine receptor-like factor 1):

> Functions as secretory protein carrier chaperone that promotes cellular release. Also functions as a cytokine subunit within the CRLF1-CLCF1 heterodimer, which engages the CNTF receptor complex (CNTFR, IL6ST/gp130, LIFR). As part of the CRLF-CLCF1 complex, binds to CNTFR, induces dimerization of the IL6ST/gp130 and LIFR, which activates JAK tyrosine kinases (JAK1 or JAK2 and to lesser extent TYK2) bound to their intracellular domains. These kinases subsequently phosphorylate IL6ST/gp130 and …

**Summary**, from NCBI Gene [9244](https://www.ncbi.nlm.nih.gov/gene/9244):

> This gene encodes a member of the cytokine type I receptor family. The protein forms a secreted complex with cardiotrophin-like cytokine factor 1 and acts on cells expressing ciliary neurotrophic factor receptors. The complex can promote survival of neuronal cells. Mutations in this gene result in Crisponi syndrome and cold-induced sweating syndrome. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:2364](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2364) · Entrez [9244](https://www.ncbi.nlm.nih.gov/gene/9244) · UniProt [O75462](https://www.uniprot.org/uniprotkb/O75462) · Ensembl [ENSG00000006016](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006016)

## Data

Gene col 98: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 98); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 98, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 98]; `tensor/DDL_lfc|DDL_z.npy` [98]; `embed/gene_vectors.npy` [98]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 98 or target_col == 98). Every well: [[CRLF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRLF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
