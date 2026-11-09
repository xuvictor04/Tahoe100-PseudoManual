---
symbol: "ST8SIA6-AS1"
type: "gene"
col: 12922
ensembl_id: "ENSG00000204832"
name: "ST8SIA6 antisense RNA 1"
location: "10p12.33"
module: 9
arm: "+"
pooled_cpm: 4.98
n_lines_expressing: 10
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 20
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ST8SIA6-AS1

*ST8SIA6 antisense RNA 1* — 10p12.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.81× (z +13.0, q 6e-36, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.08× (z +8.9, q 1e-16, up in 1 of 8 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.113×, NCI-H23 0.200×; ⚠ toxic); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H23 0.262×, NCI-H1792 0.226×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H1792 0.202×, NCI-H23 0.309×; ⚠ cell-cycle shift, explains ~0% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-423 0.0984×).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNTG1]] (+0.61, fdr 4e-05), [[PEX5L]] (+0.60, fdr 6e-05), [[POU6F2]] (+0.60, fdr 7e-05); moves opposite to [[ATP7B]] (-0.44, fdr 5e-04), [[EEPD1]] (-0.41, fdr 8e-04, ⚠ not reproduced).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 20 go from it, the strongest it → [[GRID2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12922.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.81×** | +13.0 | 6e-36 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.46×** | +12.9 | 2e-35 | 1/8 (SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.47×** | +9.9 | 9e-21 | 1/8 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +8.9 | 1e-16 | 1/8 (NCI-H23) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +6.2 | 7e-08 | 1/7 (NCI-H23) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +5.8 | 7e-07 | 1/8 (AN3 CA) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.94×** | +5.7 | 1e-06 | 4/8 (SHP-77, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +5.0 | 5e-05 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.73×** | +4.7 | 2e-04 | 1/7 (SHP-77) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +4.7 | 2e-04 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.90×** | +3.9 | 0.004 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.9 | 0.004 | 1/7 (BT-474) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.55×** | +3.7 | 0.008 | 2/8 (CFPAC-1, NCI-H23) | inconsistent across doses | position effect removed |
| [[Proglumide (drug)]] 0.05 µM |  | **1.55×** | +3.7 | 0.008 | 0/8 | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.82×** | +3.7 | 0.010 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.011 | 0/8 | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.020 | 0/8 | top dose only |  |
| [[Silodosin (drug)]] 5 µM |  | **1.50×** | +3.3 | 0.027 | 0/8 | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.045 | 0/8 | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.66×** | +3.1 | 0.048 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.065 | 5/8 (SHP-77, BT-474, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.62×** | +2.9 | 0.075 | 0/8 | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12922.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.113×, NCI-H23 0.200×; ⚠ toxic); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H23 0.262×, NCI-H1792 0.226×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H1792 0.202×, NCI-H23 0.309×; ⚠ cell-cycle shift, explains ~0% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-423 0.0984×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | 0.681× | -3.4 | 0.44 | 7/8 (NCI-H1792, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.709× | -3.0 | 0.49 | 0/8 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12922. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 25.3 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 58.9 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.200× (z -11.4) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 36.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.113× (z -13.1) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 10.0 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0984× (z -10.1) |
| [[A-172 (line)]] | wt | 0.751 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.574 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.650 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.714 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.704 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.751 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.739 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.804 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.731 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.729 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.687 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.829 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.809 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.751 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.768 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.683 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.722 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.804 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.914 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.731 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.896 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.789 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.669 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12922), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNTG1]] | +0.61 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[PEX5L]] | +0.60 | +0.39 / +0.46 | both halves | 6e-05 |  |
| [[POU6F2]] | +0.60 | +0.63 / +0.38 | both halves | 7e-05 |  |
| [[ADAMTS9-AS2]] | +0.60 | +0.42 / +0.58 | both halves | 4e-05 | same gene group |
| [[LINC02438]] | +0.60 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[MIR2052HG]] | +0.59 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[LINC00648]] | +0.58 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[CDH8]] | +0.58 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[F11-AS1]] | +0.57 | +0.47 / +0.55 | both halves | 2e-05 | same gene group |
| [[ZIC1]] | +0.57 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[RIMS2]] | +0.57 | +0.56 / +0.32 | both halves | 2e-04 |  |
| [[LINC01287]] | +0.55 | +0.39 / +0.42 | both halves | 5e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP7B]] | -0.44 | -0.33 / -0.24 | both halves | 5e-04 |  |
| [[EEPD1]] | -0.41 | -0.39 / -0.19 | ⚠ not reproduced | 8e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ST8SIA6-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.4% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PI15]] | C | PI15 activity raises ST8SIA6-AS1's level | lines that do not express PI15 (36) vs lines expressing it (14) | 4.26× lower at baseline in the lines without PI15 | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC02566, ENSG00000275016, ASCL1; co-absent with the target |
| [[LINC01905]] | C | LINC01905 activity raises ST8SIA6-AS1's level | lines that do not express LINC01905 (35) vs lines expressing it (15) | 2.43× lower at baseline in the lines without LINC01905 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000267327, ENSG00000267284, SLC25A24P1; co-absent with the target |
| [[F11-AS1]] | C | F11-AS1 activity raises ST8SIA6-AS1's level | lines that do not express F11-AS1 (34) vs lines expressing it (16) | 1.93× lower at baseline in the lines without F11-AS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent; co-absent with the target |
| [[ZNF793]] | C | ZNF793 activity raises ST8SIA6-AS1's level | lines that do not express ZNF793 (22) vs lines expressing it (28) | 2.33× lower at baseline in the lines without ZNF793 | 0.093 | ⚠ within organs, on part of the lines; also absent: PEG10, MAP6, ZNF570; co-absent with the target |
| [[MIR2052HG]] | C | MIR2052HG activity raises ST8SIA6-AS1's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 2.66× lower at baseline in the lines without MIR2052HG | 0.094 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 5, C 15. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRID2]] | B | ST8SIA6-AS1 activity raises GRID2's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 2.60× lower at baseline in the lines without ST8SIA6-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267 |
| [[DNAAF11]] | B | ST8SIA6-AS1 activity raises DNAAF11's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 2.46× lower at baseline in the lines without ST8SIA6-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267 |
| [[STPG2]] | B | ST8SIA6-AS1 activity raises STPG2's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 1.95× lower at baseline in the lines without ST8SIA6-AS1 | 0.087 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267 |
| [[VENTXP1]] | B | ST8SIA6-AS1 activity raises VENTXP1's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 2.15× lower at baseline in the lines without ST8SIA6-AS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267 |
| [[NRXN1]] | B | ST8SIA6-AS1 activity raises NRXN1's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 2.95× lower at baseline in the lines without ST8SIA6-AS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267 |
| [[PEX5L]] | C | ST8SIA6-AS1 activity raises PEX5L's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 4.34× lower at baseline in the lines without ST8SIA6-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267; co-absent with the target |
| [[POU6F2]] | C | ST8SIA6-AS1 activity raises POU6F2's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 3.72× lower at baseline in the lines without ST8SIA6-AS1 | 0.025 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267; co-absent with the target |
| [[CHMP1B2P]] | C | ST8SIA6-AS1 activity raises CHMP1B2P's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 6.28× lower at baseline in the lines without ST8SIA6-AS1 | 0.029 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267; co-absent with the target |
| [[LINC00648]] | C | ST8SIA6-AS1 activity raises LINC00648's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 3.59× lower at baseline in the lines without ST8SIA6-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267; co-absent with the target |
| [[F11-AS1]] | C | ST8SIA6-AS1 activity raises F11-AS1's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 3.15× lower at baseline in the lines without ST8SIA6-AS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267; co-absent with the target |
| [[NOVA1]] | C | ST8SIA6-AS1 activity raises NOVA1's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 4.67× lower at baseline in the lines without ST8SIA6-AS1 | 0.040 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267; co-absent with the target |
| [[MIR3171HG]] | C | ST8SIA6-AS1 activity raises MIR3171HG's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 5.24× lower at baseline in the lines without ST8SIA6-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.474). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.0, 28.1); signed map (32.6, 37.4). **Vector** length 25.1, 7.38% of its response variance represented; |z| ≥ 3 in 169 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +12.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +9.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.0 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.8 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +3.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -1.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -0.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.7 | -0.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.7 | -1.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ST8SIA6 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10p12.33 — chr10:17,386,919-17,445,758 (+) |
| Ensembl biotype | lncRNA |
| Also known as | APAL |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44880](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44880) · Entrez [100128098](https://www.ncbi.nlm.nih.gov/gene/100128098) · Ensembl [ENSG00000204832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204832)

## Data

Gene col 12922: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12922); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12922, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12922]; `tensor/DDL_lfc|DDL_z.npy` [12922]; `embed/gene_vectors.npy` [12922]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12922 or target_col == 12922). Every well: [[ST8SIA6-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST8SIA6-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
