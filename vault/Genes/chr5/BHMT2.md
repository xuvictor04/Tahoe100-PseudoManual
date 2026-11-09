---
symbol: "BHMT2"
type: "gene"
col: 5382
ensembl_id: "ENSG00000132840"
name: "betaine--homocysteine S-methyltransferase 2"
location: "5q14.1"
module: 9
arm: "+"
pooled_cpm: 3.45
n_lines_expressing: 10
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 10
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# BHMT2

*betaine--homocysteine S-methyltransferase 2* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.28× (z +12.0, q 2e-30, up in 5 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +5.4, q 7e-06, up in 1 of 8 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SHP-77 0.144×, NCI-H1792 0.205×); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.142×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.259×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSX1]] (+0.63, fdr 3e-05), [[EGF]] (+0.62, fdr 1e-05), [[LINC02492]] (+0.62, fdr 1e-04); moves opposite to [[CDKN2D]] (-0.46, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CFI]] → it (grade C ⚠); 10 go from it, the strongest it → [[OFCC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5382.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.28×** | +12.0 | 2e-30 | 5/5 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.08×** | +11.3 | 3e-27 | 5/6 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.69×** | +9.0 | 6e-17 | 4/5 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.73×** | +5.9 | 6e-07 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +5.4 | 7e-06 | 1/8 (NCI-H2347) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.30×** | +5.2 | 2e-05 | 6/8 (NCI-H2347, SHP-77, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.10×** | +4.6 | 3e-04 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +4.6 | 3e-04 | 1/7 (SHP-77) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.99×** | +4.3 | 1e-03 | 8/8 (NCI-H1792, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.63×** | +4.3 | 1e-03 | 2/8 (NCI-H2347, NCI-H1792) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.41×** | +4.0 | 0.003 | 3/5 (NCI-H2347, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.43×** | +4.0 | 0.003 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +3.9 | 0.004 | 2/7 (SNU-423, NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.86×** | +3.9 | 0.004 | 0/8 | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.85×** | +3.8 | 0.005 | 7/8 (SNU-423, NCI-H2347, …) | rises with dose |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.008 | 1/7 (NCI-H2347) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.80×** | +3.5 | 0.016 | 6/8 (NCI-H1792, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.034 | 1/7 (A498) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.99×** | +3.1 | 0.057 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.98×** | +3.0 | 0.057 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SHP-77 0.144×, NCI-H1792 0.205×); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.142×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.259×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5382. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 48.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -15.9) |
| [[NCI-H1792 (line)]] | alt | 15.3 | 1 | 1 | [[Bortezomib (drug)]] 0.05 µM 8.46× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -9.9) |
| [[A-172 (line)]] | wt | 0.325 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.228 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.334 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.294 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.378 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.389 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.310 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.350 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.377 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.321 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.285 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.314 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.324 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.360 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.354 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.431 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.351 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5382), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSX1]] | +0.63 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[EGF]] | +0.62 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[LINC02492]] | +0.62 | +0.55 / +0.34 | both halves | 1e-04 |  |
| [[GNGT1]] | +0.61 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[TRIM16L]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[LINC01287]] | +0.59 | +0.61 / +0.28 | both halves | 3e-04 |  |
| [[HTATIP2]] | +0.59 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[PSMD11]] | +0.58 | +0.46 / +0.47 | both halves | 2e-05 | pathway: Metabolism of amino acids and derivatives |
| [[ALOX12P2-1]] | +0.58 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[NRK]] | +0.58 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[ABCC2]] | +0.58 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[MLLT11]] | +0.57 | +0.48 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN2D]] | -0.46 | -0.34 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFI]] | C | CFI activity raises BHMT2's level | lines that do not express CFI (31) vs lines expressing it (19) | 2.27× lower at baseline in the lines without CFI | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 1, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OFCC1]] | B | BHMT2 activity raises OFCC1's level | lines that do not express BHMT2 (40) vs lines expressing it (10) | 2.01× lower at baseline in the lines without BHMT2 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, LINC01320, CP |
| [[EGF]] | C | BHMT2 activity raises EGF's level | lines that do not express BHMT2 (40) vs lines expressing it (10) | 2.02× lower at baseline in the lines without BHMT2 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, LINC01320, CP; co-absent with the target |
| [[MAGEA10]] | C | BHMT2 activity raises MAGEA10's level | lines that do not express BHMT2 (40) vs lines expressing it (10) | 2.89× lower at baseline in the lines without BHMT2 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, LINC01320, CP; co-absent with the target |
| [[KCNE4]] | C | BHMT2 activity raises KCNE4's level | lines that do not express BHMT2 (40) vs lines expressing it (10) | 2.68× lower at baseline in the lines without BHMT2 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, LINC01320, CP; co-absent with the target |
| [[PEX5L]] | C | BHMT2 activity raises PEX5L's level | lines that do not express BHMT2 (40) vs lines expressing it (10) | 2.84× lower at baseline in the lines without BHMT2 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, LINC01320, CP; co-absent with the target |
| [[KCND2]] | C | BHMT2 activity raises KCND2's level | lines that do not express BHMT2 (40) vs lines expressing it (10) | 3.17× lower at baseline in the lines without BHMT2 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, LINC01320, CP; co-absent with the target |
| [[PGR]] | C | BHMT2 activity raises PGR's level | lines that do not express BHMT2 (40) vs lines expressing it (10) | 1.41× lower at baseline in the lines without BHMT2 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, LINC01320, CP; co-absent with the target |
| [[HGF]] | C | BHMT2 activity raises HGF's level | lines that do not express BHMT2 (40) vs lines expressing it (10) | 1.36× lower at baseline in the lines without BHMT2 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, LINC01320, CP; co-absent with the target |
| [[CFI]] | C | BHMT2 activity raises CFI's level | lines that do not express BHMT2 (40) vs lines expressing it (10) | 3.19× lower at baseline in the lines without BHMT2 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, LINC01320, CP; co-absent with the target |
| [[TDO2]] | C | BHMT2 activity raises TDO2's level | lines that do not express BHMT2 (40) vs lines expressing it (10) | 2.14× lower at baseline in the lines without BHMT2 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, LINC01320, CP; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.562). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.1, 38.6); signed map (42.9, 23.0). **Vector** length 25.2, 7.88% of its response variance represented; |z| ≥ 3 in 150 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.1 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.1 | +1.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | -2.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -0.8 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -0.8 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -2.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.7 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -1.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -1.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | betaine--homocysteine S-methyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:79,069,767-79,090,069 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Homocysteine domain containing methyltransferases; Small molecule methyltransferases |
| Reactome | 2 pathways, smallest: Sulfur amino acid metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2M3](https://www.uniprot.org/uniprotkb/Q9H2M3) (S-methylmethionine--homocysteine S-methyltransferase BHMT2):

> Involved in the regulation of homocysteine metabolism. Converts homocysteine to methionine using S-methylmethionine (SMM) as a methyl donor.

**Summary**, from NCBI Gene [23743](https://www.ncbi.nlm.nih.gov/gene/23743):

> Homocysteine is a sulfur-containing amino acid that plays a crucial role in methylation reactions. Transfer of the methyl group from betaine to homocysteine creates methionine, which donates the methyl group to methylate DNA, proteins, lipids, and other intracellular metabolites. The protein encoded by this gene is one of two methyl transferases that can catalyze the transfer of the methyl group from betaine to homocysteine. Anomalies in homocysteine metabolism have been implicated in disorders …

**Accessions** — [HGNC:1048](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1048) · Entrez [23743](https://www.ncbi.nlm.nih.gov/gene/23743) · UniProt [Q9H2M3](https://www.uniprot.org/uniprotkb/Q9H2M3) · Ensembl [ENSG00000132840](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132840)

## Data

Gene col 5382: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5382); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5382, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5382]; `tensor/DDL_lfc|DDL_z.npy` [5382]; `embed/gene_vectors.npy` [5382]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5382 or target_col == 5382). Every well: [[BHMT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BHMT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
