---
symbol: "NETO1"
type: "gene"
col: 9288
ensembl_id: "ENSG00000166342"
name: "neuropilin and tolloid like 1"
location: "18q22.3"
module: 108
arm: "+"
pooled_cpm: 8.47
n_lines_expressing: 7
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 13
direction_downstream: 35
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# NETO1

*neuropilin and tolloid like 1* — 18q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.10× (z +11.5, q 8e-28, up in 0 of 5 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.195×); [[Panobinostat (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.131×; ⚠ cell-cycle shift, explains ~39% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (LOX-IMVI 0.151×; ⚠ cell-cycle shift, explains ~25% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02267]] (+0.70, fdr 1e-05), [[LINC00993]] (+0.67, fdr 7e-06), [[MGAT4C]] (+0.65, fdr 1e-05).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[LINC00993]] → it (grade C ⚠); 35 go from it, the strongest it → [[MME-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9288.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.10×** | +11.5 | 8e-28 | 0/5 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.30×** | +10.5 | 3e-23 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.76×** | +9.2 | 1e-17 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.91×** | +7.1 | 2e-10 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +5.5 | 4e-06 | 0/5 | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +4.5 | 8e-04 | 0/4 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.35×** | +4.4 | 9e-04 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.79×** | +4.2 | 0.002 | 0/4 | rises with dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.60×** | +3.6 | 0.020 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.020 | 2/5 (A-427, SHP-77) | top dose only | cell-cycle shift (explains ~17% here); composition shift |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.64×** | +3.6 | 0.020 | 0/4 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.029 | 1/5 (A-427) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.93×** | +3.4 | 0.033 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.90×** | +3.3 | 0.040 | 0/4 | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +3.3 | 0.040 | 0/4 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +3.2 | 0.054 | 1/5 (CHP-212) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Erythromycin (drug)]] 5 µM |  | **1.52×** | +3.0 | 0.083 | 0/5 | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.51×** | +3.0 | 0.088 | 0/5 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9288.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.195×); [[Panobinostat (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.131×; ⚠ cell-cycle shift, explains ~39% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (LOX-IMVI 0.151×; ⚠ cell-cycle shift, explains ~25% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | 0.606× | -3.3 | 0.32 | 0/5 | inconsistent across doses | position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.629× | -3.1 | 0.32 | 0/5 | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.652× | -3.1 | 0.32 | 0/5 | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.654× | -3.0 | 0.32 | 0/5 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9288. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 298 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -14.4) |
| [[A-172 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.816 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.812 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 78.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.683 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.648 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.598 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.768 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.565 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.565 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.869 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.657 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.677 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.945 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.639 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.759 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.569 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9288), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02267]] | +0.70 | +0.56 / +0.73 | both halves | 1e-05 | **novel candidate** |
| [[LINC00993]] | +0.67 | +0.58 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[MGAT4C]] | +0.65 | +0.50 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[KCNH5]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[PHACTR1]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SYT9]] | +0.61 | +0.64 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[NALF1]] | +0.61 | +0.52 / +0.57 | both halves | 1e-05 | same gene group |
| [[NTM]] | +0.61 | +0.50 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[TCF4]] | +0.60 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[NTNG1]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 | STRING 536 |
| [[ADAMTS18]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[NOL4]] | +0.59 | +0.44 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00993]] | C | LINC00993 activity raises NETO1's level | lines that do not express LINC00993 (35) vs lines expressing it (15) | 3.02× lower at baseline in the lines without LINC00993 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANKRD30A, KCNH5, KCNB2; maybe low, not absent; co-absent with the target |
| [[NALF1]] | C | NALF1 activity raises NETO1's level | lines that do not express NALF1 (28) vs lines expressing it (22) | 2.43× lower at baseline in the lines without NALF1 | 0.025 | ⚠ within organs, on part of the lines; also absent: EPHA5, COL3A1, ENSG00000248837; co-absent with the target |
| [[KC6]] | C | KC6 activity raises NETO1's level | lines that do not express KC6 (32) vs lines expressing it (18) | 2.75× lower at baseline in the lines without KC6 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1; co-absent with the target |
| [[LINC02492]] | C | LINC02492 activity raises NETO1's level | lines that do not express LINC02492 (32) vs lines expressing it (18) | 2.19× lower at baseline in the lines without LINC02492 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000260289, ENSG00000254337, RHOJ; maybe low, not absent; co-absent with the target |
| [[MSR1]] | C | MSR1 activity raises NETO1's level | lines that do not express MSR1 (36) vs lines expressing it (14) | 2.24× lower at baseline in the lines without MSR1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02438, SAMMSON, ENSG00000286523; co-absent with the target |
| [[PSG5]] | C | PSG5 activity raises NETO1's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 2.23× lower at baseline in the lines without PSG5 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486; co-absent with the target |
| [[HGF]] | C | HGF activity raises NETO1's level | lines that do not express HGF (38) vs lines expressing it (12) | 1.94× lower at baseline in the lines without HGF | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; co-absent with the target |
| [[LINC01036]] | C | LINC01036 activity raises NETO1's level | lines that do not express LINC01036 (33) vs lines expressing it (17) | 1.70× lower at baseline in the lines without LINC01036 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MSR1, IHO1, ENSG00000250038; co-absent with the target |
| [[ZNF804A]] | C | ZNF804A activity raises NETO1's level | lines that do not express ZNF804A (31) vs lines expressing it (19) | 2.49× lower at baseline in the lines without ZNF804A | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, CARMN, PAPPA; co-absent with the target |
| [[ANKRD30A]] | C | ANKRD30A activity raises NETO1's level | lines that do not express ANKRD30A (37) vs lines expressing it (13) | 3.59× lower at baseline in the lines without ANKRD30A | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00993, ENSG00000232252, ASCL1; co-absent with the target |
| [[CDH10]] | C | CDH10 activity raises NETO1's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 3.62× lower at baseline in the lines without CDH10 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[NOL4]] | C | NOL4 activity raises NETO1's level | lines that do not express NOL4 (30) vs lines expressing it (20) | 2.60× lower at baseline in the lines without NOL4 | 0.079 | ⚠ within organs, on part of the lines; also absent: KCTD8, ASXL3, DSCAM; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 7, C 28. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MME-AS1]] | B | NETO1 activity raises MME-AS1's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 1.84× lower at baseline in the lines without NETO1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4 |
| [[SHANK1]] | B | NETO1 activity raises SHANK1's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 3.25× lower at baseline in the lines without NETO1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4 |
| [[FAM167A]] | B | NETO1 activity raises FAM167A's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 3.87× lower at baseline in the lines without NETO1 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4 |
| [[CACNA1A]] | B | NETO1 activity raises CACNA1A's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 3.41× lower at baseline in the lines without NETO1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4 |
| [[DIRC3-AS1]] | B | NETO1 activity raises DIRC3-AS1's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 2.42× lower at baseline in the lines without NETO1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4 |
| [[BCL11A]] | B | NETO1 activity raises BCL11A's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 4.71× lower at baseline in the lines without NETO1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4 |
| [[HTR2C]] | B | NETO1 activity raises HTR2C's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 2.16× lower at baseline in the lines without NETO1 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4 |
| [[RGS7]] | C | NETO1 activity raises RGS7's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 5.60× lower at baseline in the lines without NETO1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[FAP]] | C | NETO1 activity raises FAP's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 7.12× lower at baseline in the lines without NETO1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[PRKG1]] | C | NETO1 activity raises PRKG1's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 6.77× lower at baseline in the lines without NETO1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[SAMD3]] | C | NETO1 activity raises SAMD3's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 7.00× lower at baseline in the lines without NETO1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[MSR1]] | C | NETO1 activity raises MSR1's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 5.42× lower at baseline in the lines without NETO1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.5, 23.7); signed map (34.6, 42.6). **Vector** length 22.3, 10.0% of its response variance represented; |z| ≥ 3 in 106 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.6 | +4.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.5 | +3.4 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.6 | -2.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.6 | -1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.5 | -0.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.5 | -0.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.5 | +0.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.5 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | neuropilin and tolloid like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q22.3 — chr18:72,742,314-72,868,146 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BTCL1, BCTL1 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Neuropilin and tolloid like family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDF5](https://www.uniprot.org/uniprotkb/Q8TDF5) (Neuropilin and tolloid-like protein 1):

> Involved in the development and/or maintenance of neuronal circuitry. Accessory subunit of the neuronal N-methyl-D-aspartate receptor (NMDAR) critical for maintaining the abundance of GRIN2A-containing NMDARs in the postsynaptic density. Regulates long-term NMDA receptor-dependent synaptic plasticity and cognition, at least in the context of spatial learning and memory (By similarity).

**Summary**, from NCBI Gene [81832](https://www.ncbi.nlm.nih.gov/gene/81832):

> This gene encodes a transmembrane protein containing two extracellular CUB domains followed by a low-density lipoprotein class A (LDLa) domain. This protein is thought to play a critical role in spatial learning and memory by regulating the function of synaptic N-methyl-D-aspartic acid receptor complexes in the hippocampus. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Aug 2017]

**Accessions** — [HGNC:13823](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13823) · Entrez [81832](https://www.ncbi.nlm.nih.gov/gene/81832) · UniProt [Q8TDF5](https://www.uniprot.org/uniprotkb/Q8TDF5) · Ensembl [ENSG00000166342](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166342)

## Data

Gene col 9288: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9288); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9288, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9288]; `tensor/DDL_lfc|DDL_z.npy` [9288]; `embed/gene_vectors.npy` [9288]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9288 or target_col == 9288). Every well: [[NETO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NETO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
