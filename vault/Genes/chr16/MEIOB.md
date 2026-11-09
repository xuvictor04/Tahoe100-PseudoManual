---
symbol: "MEIOB"
type: "gene"
col: 8472
ensembl_id: "ENSG00000162039"
name: "meiosis specific with OB-fold"
location: "16p13.3"
module: 19
arm: "+"
pooled_cpm: 2.34
n_lines_expressing: 22
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# MEIOB

*meiosis specific with OB-fold* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.71× (z +13.5, q 1e-38, up in 0 of 7 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.250×); [[Harringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.214×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (C-33 A 0.116×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNTN1]] (+0.67, fdr 7e-06), [[SPDYE10]] (+0.65, fdr 1e-05), [[DDIT4L]] (+0.64, fdr 1e-05); moves opposite to [[SLC2A10]] (-0.44, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RTN4RL2]] → it (grade B ⚠); 2 go from it, the strongest it → [[ATP2A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8472.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.71×** | +13.5 | 1e-38 | 0/7 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.93×** | +11.6 | 1e-28 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.88×** | +11.1 | 3e-26 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.44×** | +10.0 | 2e-21 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.57×** | +9.7 | 3e-20 | 3/10 (A-172, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.26×** | +8.6 | 8e-16 | 6/12 (C-33 A, AsPC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.19×** | +5.7 | 1e-06 | 7/15 (NCI-H1792, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.83×** | +5.4 | 5e-06 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.67×** | +5.2 | 1e-05 | 2/16 (HepG2/C3A, NCI-H1573) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +4.8 | 8e-05 | 0/15 | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +4.6 | 2e-04 | 0/5 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.34×** | +4.6 | 2e-04 | 1/4 (C-33 A) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.14×** | +4.4 | 6e-04 | 1/4 (SK-MEL-2) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.001 | 8/15 (NCI-H1573, A498, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.77×** | +4.1 | 0.001 | 1/12 (A498) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.71×** | +3.9 | 0.003 | 5/16 (H4, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.76×** | +3.9 | 0.004 | 3/12 (C-33 A, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +3.7 | 0.005 | 6/14 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.66×** | +3.7 | 0.006 | 5/15 (A498, H4, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.015 | 2/15 (SK-MEL-2, NCI-H1573) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.91×** | +3.4 | 0.019 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +3.2 | 0.028 | 2/14 (NCI-H1573, C-33 A) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8472.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.250×); [[Harringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.214×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (C-33 A 0.116×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Captopril (drug)]] 0.5 µM |  | 0.623× | -3.5 | 0.29 | 0/15 | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.624× | -3.2 | 0.39 | 0/14 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8472. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 27.1 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.05 µM 0.116× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 58.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -13.8) |
| [[A-172 (line)]] | wt | 0.690 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.689 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.698 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.759 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.580 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.599 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.571 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.392 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.462 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.370 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.596 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.681 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.489 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.698 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.883 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.473 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.502 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8472), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTN1]] | +0.67 | +0.59 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[SPDYE10]] | +0.65 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[DDIT4L]] | +0.64 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[NCKAP5-AS2]] | +0.64 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[CTNND2]] | +0.63 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[LINC03000]] | +0.62 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[SCUBE1]] | +0.61 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[DPP10]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[TENM1]] | +0.58 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[LINC01967]] | +0.58 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[PAX7]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[LINC01035]] | +0.57 | +0.51 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC2A10]] | -0.44 | -0.38 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RTN4RL2]] | B | RTN4RL2 activity lowers MEIOB's level | lines that do not express RTN4RL2 (11) vs lines expressing it (39) | 1.53× higher at baseline in the lines without RTN4RL2 | 0.040 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PAX7]] | C | PAX7 activity raises MEIOB's level | lines that do not express PAX7 (35) vs lines expressing it (15) | 1.64× lower at baseline in the lines without PAX7 | 0.051 | ⚠ within organs, on part of the lines; also absent: LINC00408, ENSG00000289605, SLC15A5; maybe low, not absent; co-absent with the target |
| [[CNTN1]] | C | CNTN1 activity raises MEIOB's level | lines that do not express CNTN1 (33) vs lines expressing it (17) | 1.97× lower at baseline in the lines without CNTN1 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR141, MAGEB2, S100A9; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP2A3]] | B | MEIOB activity raises ATP2A3's level | lines that do not express MEIOB (28) vs lines expressing it (22) | 1.90× lower at baseline in the lines without MEIOB | 0.085 | ⚠ within organs, on part of the lines; also absent: SHISAL1, DOK6, DPP10; maybe low, not absent |
| [[LINC01967]] | C | MEIOB activity raises LINC01967's level | lines that do not express MEIOB (28) vs lines expressing it (22) | 1.93× lower at baseline in the lines without MEIOB | 0.047 | ⚠ within organs, on part of the lines; also absent: SHISAL1, DOK6, DPP10; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.0, 35.7); signed map (42.1, 45.0). **Vector** length 23.8, 4.15% of its response variance represented; |z| ≥ 3 in 355 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.0 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +11.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +8.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.0 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.8 | +4.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.8 | -2.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -1.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | -0.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.7 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -1.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | meiosis specific with OB-fold |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,833,986-1,884,294 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC35212; previously C16orf73 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N635](https://www.uniprot.org/uniprotkb/Q8N635) (Meiosis-specific with OB domain-containing protein):

> Single-stranded DNA-binding protein required for homologous recombination in meiosis I. Required for double strand breaks (DSBs) repair and crossover formation and promotion of faithful and complete synapsis. Not required for the initial loading of recombinases but required to maintain a proper number of RAD51 and DMC1 foci after the zygotene stage. May act by ensuring the stabilization of recombinases, which is required for successful homology search and meiotic recombination. Displays …

**Summary**, from NCBI Gene [254528](https://www.ncbi.nlm.nih.gov/gene/254528):

> Predicted to enable chromatin binding activity; single-stranded DNA 3'-5' DNA exonuclease activity; and single-stranded DNA binding activity. Predicted to be involved in double-strand break repair via homologous recombination; fertilization; and meiotic nuclear division. Located in nucleus. Implicated in primary ovarian insufficiency and spermatogenic failure 22. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28569](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28569) · Entrez [254528](https://www.ncbi.nlm.nih.gov/gene/254528) · UniProt [Q8N635](https://www.uniprot.org/uniprotkb/Q8N635) · Ensembl [ENSG00000162039](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162039)

## Data

Gene col 8472: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8472); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8472, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8472]; `tensor/DDL_lfc|DDL_z.npy` [8472]; `embed/gene_vectors.npy` [8472]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8472 or target_col == 8472). Every well: [[MEIOB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEIOB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
