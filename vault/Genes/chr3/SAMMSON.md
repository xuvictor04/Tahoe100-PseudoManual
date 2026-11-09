---
symbol: "SAMMSON"
type: "gene"
col: 14235
ensembl_id: "ENSG00000240405"
name: "survival associated mitochondrial melanoma specific oncogenic non-coding RNA"
location: "3p13"
module: 87
arm: "+"
pooled_cpm: 12.09
n_lines_expressing: 16
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 21
direction_downstream: 3
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# SAMMSON

*survival associated mitochondrial melanoma specific oncogenic non-coding RNA* — 3p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.51× (z +20.5, q 0e+00, up in 8 of 10 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (SW 900 0.0693×, C32 0.148×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (C32 0.0934×; ⚠ cell-cycle shift, explains ~8% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (C32 0.0860×; ⚠ toxic; transcription drop); [[Fedratinib (hydrochloride hydrate) (drug)]] 0.05 µM in 1 line (A-172 0.0599×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOX10]] (+0.78, fdr 7e-06), [[LEF1-AS1]] (+0.77, fdr 7e-06), [[MIR3681HG]] (+0.75, fdr 7e-06).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[FZD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14235.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.51×** | +20.5 | 0e+00 | 8/10 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.66×** | +12.0 | 7e-31 | 1/7 (RPMI-7951) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.05×** | +10.8 | 1e-24 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.19×** | +10.7 | 1e-24 | 7/11 (LOX-IMVI, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.63×** | +9.3 | 1e-18 | 2/12 (NCI-H1792, NCI-H2030) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +7.7 | 1e-12 | 8/11 (A-172, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +6.7 | 1e-09 | 6/10 (LOX-IMVI, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.98×** | +6.6 | 3e-09 | 6/10 (A-172, RPMI-7951, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +6.2 | 3e-08 | 2/8 (LOX-IMVI, SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.0 | 1e-07 | 5/13 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +4.8 | 8e-05 | 4/12 (A-172, RPMI-7951, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +3.6 | 0.015 | 0/10 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.019 | 4/12 (SW 900, LOX-IMVI, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.60×** | +3.3 | 0.045 | 1/10 (NCI-H1792) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.094 | 4/10 (SW 900, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14235.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (SW 900 0.0693×, C32 0.148×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (C32 0.0934×; ⚠ cell-cycle shift, explains ~8% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (C32 0.0860×; ⚠ toxic; transcription drop); [[Fedratinib (hydrochloride hydrate) (drug)]] 0.05 µM in 1 line (A-172 0.0599×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (drug)]] 0.05 µM |  | 0.666× | -3.6 | 0.18 | 1/12 (AN3 CA) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.690× | -3.3 | 0.29 | 0/11 | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | 0.536× | -3.1 | 0.33 | 3/10 (C32, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14235. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 227 | 0 | 6 (6 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0934× (z -12.2) ⚠ cell-cycle shift, explains ~8% of this change |
| [[SK-MEL-2 (line)]] | alt | 328 | 0 | 3 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0318× (z -11.4) ⚠ toxic |
| [[A-172 (line)]] | wt | 5.06 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.47× (z +9.9) | [[Fedratinib (hydrochloride hydrate) (drug)]] 0.05 µM 0.0599× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 15.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +13.5) | — |
| [[SNU-423 (line)]] | alt | 8.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.87× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0693× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.32 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14235), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOX10]] | +0.78 | +0.68 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[LEF1-AS1]] | +0.77 | +0.69 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[MIR3681HG]] | +0.75 | +0.71 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[CD96]] | +0.75 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[A2M]] | +0.74 | +0.59 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[RMEL3]] | +0.73 | +0.72 / +0.65 | both halves | 7e-06 | same gene group |
| [[COL19A1]] | +0.72 | +0.59 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[LHFPL3-AS1]] | +0.71 | +0.61 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[PI15]] | +0.70 | +0.55 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[C10orf90]] | +0.69 | +0.52 / +0.73 | both halves | 1e-05 | **novel candidate** |
| [[LINC02566]] | +0.66 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[LINC02941]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 1, C 20. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SAMMSON's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[APOD]] | C | APOD activity raises SAMMSON's level | lines that do not express APOD (43) vs lines expressing it (7) | 10.00× lower at baseline in the lines without APOD | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LHFPL3-AS1, SOX10, CALCA; co-absent with the target |
| [[DGKB]] | C | DGKB activity raises SAMMSON's level | lines that do not express DGKB (23) vs lines expressing it (27) | 2.10× lower at baseline in the lines without DGKB | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent; co-absent with the target |
| [[LHFPL3-AS1]] | C | LHFPL3-AS1 activity raises SAMMSON's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 8.32× lower at baseline in the lines without LHFPL3-AS1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[MIR3681HG]] | C | MIR3681HG activity raises SAMMSON's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 2.83× lower at baseline in the lines without MIR3681HG | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent; co-absent with the target |
| [[LOXL4]] | C | LOXL4 activity raises SAMMSON's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 1.61× lower at baseline in the lines without LOXL4 | 0.031 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3; co-absent with the target |
| [[RHOJ]] | C | RHOJ activity raises SAMMSON's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 2.79× lower at baseline in the lines without RHOJ | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[LINC00698]] | C | LINC00698 activity raises SAMMSON's level | lines that do not express LINC00698 (30) vs lines expressing it (20) | 2.14× lower at baseline in the lines without LINC00698 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253642, HEPH, SRRM4; maybe low, not absent; co-absent with the target |
| [[LINC02438]] | C | LINC02438 activity raises SAMMSON's level | lines that do not express LINC02438 (36) vs lines expressing it (14) | 4.05× lower at baseline in the lines without LINC02438 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, MSR1, FSTL5; co-absent with the target |
| [[FCRLA]] | C | FCRLA activity raises SAMMSON's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 4.99× lower at baseline in the lines without FCRLA | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[CTHRC1]] | C | CTHRC1 activity raises SAMMSON's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 2.94× lower at baseline in the lines without CTHRC1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent; co-absent with the target |
| [[NLGN4X]] | C | NLGN4X activity raises SAMMSON's level | lines that do not express NLGN4X (37) vs lines expressing it (13) | 2.85× lower at baseline in the lines without NLGN4X | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FZD1]] | B | SAMMSON activity raises FZD1's level | lines that do not express SAMMSON (34) vs lines expressing it (16) | 1.75× lower at baseline in the lines without SAMMSON | 0.048 | ⚠ within organs, on part of the lines; also absent: MSR1, ENSG00000286523, PDE1A |
| [[RHOJ]] | C | SAMMSON activity raises RHOJ's level | lines that do not express SAMMSON (34) vs lines expressing it (16) | 2.30× lower at baseline in the lines without SAMMSON | 0.093 | ⚠ within organs, on part of the lines; also absent: MSR1, ENSG00000286523, PDE1A; co-absent with the target |
| [[MIR3681HG]] | C | SAMMSON activity raises MIR3681HG's level | lines that do not express SAMMSON (34) vs lines expressing it (16) | 3.85× lower at baseline in the lines without SAMMSON | 0.094 | ⚠ within organs, on part of the lines; also absent: MSR1, ENSG00000286523, PDE1A; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.850). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.3, 28.8); signed map (29.6, 39.1). **Vector** length 48.3, 18.3% of its response variance represented; |z| ≥ 3 in 292 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +20.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +10.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +6.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.0 | +1.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.7 | +0.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.9 | -2.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | survival associated mitochondrial melanoma specific oncogenic non-coding RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p13 — chr3:69,999,550-70,518,064 (+) |
| Ensembl biotype | lncRNA |
| Also known as | uc.116; previously LINC01212 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49644](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49644) · Entrez [101927152](https://www.ncbi.nlm.nih.gov/gene/101927152) · Ensembl [ENSG00000240405](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240405)

## Data

Gene col 14235: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14235); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14235, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14235]; `tensor/DDL_lfc|DDL_z.npy` [14235]; `embed/gene_vectors.npy` [14235]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14235 or target_col == 14235). Every well: [[SAMMSON — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAMMSON.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
