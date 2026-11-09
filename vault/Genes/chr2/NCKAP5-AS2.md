---
symbol: "NCKAP5-AS2"
type: "gene"
col: 13563
ensembl_id: "ENSG00000226953"
name: "NCKAP5 antisense RNA 2"
location: "2q21.2"
module: 19
arm: "+"
pooled_cpm: 2.03
n_lines_expressing: 19
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 12
direction_downstream: 19
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# NCKAP5-AS2

*NCKAP5 antisense RNA 2* — 2q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.76× (z +10.1, q 4e-21, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.26× (z +6.9, q 9e-10, up in 3 of 7 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H460 0.0794×, A549 0.116×, SHP-77 0.317×; ⚠ cell-cycle shift, explains ~23% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0890×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.108×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.125×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.147×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPDYE10]] (+0.80, fdr 7e-06), [[LINC01035]] (+0.79, fdr 7e-06), [[CTNND2]] (+0.79, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[KCNE4]] → it (grade C ⚠); 19 go from it, the strongest it → [[P4HA3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13563.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.76×** | +10.1 | 4e-21 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.10×** | +9.7 | 6e-20 | 1/4 (SHP-77) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.81×** | +7.4 | 3e-11 | 1/2 (SHP-77) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +6.9 | 9e-10 | 3/7 (NCI-H460, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.86×** | +4.5 | 8e-04 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.00×** | +4.3 | 0.001 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.01×** | +4.2 | 0.002 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +4.1 | 0.003 | 1/4 (A549) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +3.9 | 0.005 | 1/4 (PANC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | **1.58×** | +3.9 | 0.007 | 1/6 (hTERT-HPNE) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.30×** | +3.6 | 0.020 | 1/5 (SHP-77) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.79×** | +3.5 | 0.026 | 0/11 | inconsistent across doses |  |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.78×** | +3.4 | 0.026 | 3/7 (SHP-77, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +3.4 | 0.026 | 2/4 (SHP-77, A549) | rises with dose | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +3.4 | 0.028 | 1/4 (PANC-1) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.15×** | +3.3 | 0.041 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.70×** | +3.2 | 0.049 | 0/5 | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +3.1 | 0.059 | 0/12 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.69×** | +2.9 | 0.093 | 0/4 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13563.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H460 0.0794×, A549 0.116×, SHP-77 0.317×; ⚠ cell-cycle shift, explains ~23% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0890×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.108×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.125×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.147×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Abiraterone acetate (drug)]] 0.5 µM |  | 0.597× | -3.1 | 0.30 | 4/14 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.05 µM |  | 0.601× | -3.1 | 0.30 | 3/12 (SNU-423, J82, …) | inconsistent across doses |  |
| [[Encorafenib (drug)]] 5 µM |  | 0.379× | -3.0 | 0.30 | 0/12 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.604× | -3.0 | 0.30 | 5/12 (NCI-H460, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[crizotinib (drug)]] 5 µM |  | 0.596× | -3.0 | 0.30 | 3/10 (PANC-1, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13563. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 23.0 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0794× (z -21.0) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.108× (z -13.1) |
| [[A549 (line)]] | wt | 3.24 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -8.5) ⚠ cell-cycle shift, explains ~23% of this change |
| [[SHP-77 (line)]] | alt | 20.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -8.5) ⚠ cell-cycle shift, explains ~23% of this change |
| [[A-172 (line)]] | wt | 0.423 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.750 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.294 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.551 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.307 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.638 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.617 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.298 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.533 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.544 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.559 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.289 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.261 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.370 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.291 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.262 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.302 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.218 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.303 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.350 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.627 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.923 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.296 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13563), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPDYE10]] | +0.80 | +0.74 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[LINC01035]] | +0.79 | +0.84 / +0.58 | both halves | 7e-06 |  |
| [[CTNND2]] | +0.79 | +0.78 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[LINC03000]] | +0.77 | +0.81 / +0.57 | both halves | 1e-05 |  |
| [[KCNK2]] | +0.77 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[DPP10]] | +0.76 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[COL4A6]] | +0.76 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[ADGRD1]] | +0.76 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[PAX7]] | +0.75 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[GREM2]] | +0.75 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[SLITRK4]] | +0.75 | +0.63 / +0.78 | both halves | 7e-06 |  |
| [[LIN7A]] | +0.75 | +0.72 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNE4]] | C | KCNE4 activity raises NCKAP5-AS2's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 1.88× lower at baseline in the lines without KCNE4 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[LIN7A]] | C | LIN7A activity raises NCKAP5-AS2's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 1.93× lower at baseline in the lines without LIN7A | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |
| [[PDE1A]] | C | PDE1A activity raises NCKAP5-AS2's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 2.12× lower at baseline in the lines without PDE1A | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |
| [[LINC01508]] | C | LINC01508 activity raises NCKAP5-AS2's level | lines that do not express LINC01508 (42) vs lines expressing it (8) | 2.16× lower at baseline in the lines without LINC01508 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SPINK13, RHEX; co-absent with the target |
| [[UNC5D]] | C | UNC5D activity raises NCKAP5-AS2's level | lines that do not express UNC5D (36) vs lines expressing it (14) | 2.04× lower at baseline in the lines without UNC5D | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01266, KCNH5, NAA11; co-absent with the target |
| [[ADARB2]] | C | ADARB2 activity raises NCKAP5-AS2's level | lines that do not express ADARB2 (39) vs lines expressing it (11) | 2.05× lower at baseline in the lines without ADARB2 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, GSG1L2; co-absent with the target |
| [[LINC02994]] | C | LINC02994 activity raises NCKAP5-AS2's level | lines that do not express LINC02994 (33) vs lines expressing it (17) | 1.68× lower at baseline in the lines without LINC02994 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000234352, ANKRD30B, ENSG00000287598; co-absent with the target |
| [[TRPA1]] | C | TRPA1 activity raises NCKAP5-AS2's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 1.87× lower at baseline in the lines without TRPA1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises NCKAP5-AS2's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 2.17× lower at baseline in the lines without DPP10 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[NCKAP5]] | C | NCKAP5 activity raises NCKAP5-AS2's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 1.63× lower at baseline in the lines without NCKAP5 | 0.081 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent; co-absent with the target |
| [[GPRIN3]] | C | GPRIN3 activity raises NCKAP5-AS2's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 1.77× lower at baseline in the lines without GPRIN3 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031; co-absent with the target |
| [[TBX18]] | C | TBX18 activity raises NCKAP5-AS2's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 1.65× lower at baseline in the lines without TBX18 | 0.098 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 2, C 17. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P4HA3]] | B | NCKAP5-AS2 activity raises P4HA3's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 1.66× lower at baseline in the lines without NCKAP5-AS2 | 0.061 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D |
| [[GABBR2]] | B | NCKAP5-AS2 activity raises GABBR2's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 1.94× lower at baseline in the lines without NCKAP5-AS2 | 0.093 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D |
| [[NCKAP5]] | C | NCKAP5-AS2 activity raises NCKAP5's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 4.44× lower at baseline in the lines without NCKAP5-AS2 | 3e-04 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |
| [[KCNE4]] | C | NCKAP5-AS2 activity raises KCNE4's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 3.38× lower at baseline in the lines without NCKAP5-AS2 | 0.016 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |
| [[TBX18]] | C | NCKAP5-AS2 activity raises TBX18's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 3.82× lower at baseline in the lines without NCKAP5-AS2 | 0.034 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |
| [[EYA2]] | C | NCKAP5-AS2 activity raises EYA2's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 2.55× lower at baseline in the lines without NCKAP5-AS2 | 0.035 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |
| [[CDH19]] | C | NCKAP5-AS2 activity raises CDH19's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 1.53× lower at baseline in the lines without NCKAP5-AS2 | 0.040 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |
| [[P3H2-AS1]] | C | NCKAP5-AS2 activity raises P3H2-AS1's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 1.65× lower at baseline in the lines without NCKAP5-AS2 | 0.041 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |
| [[SCUBE1]] | C | NCKAP5-AS2 activity raises SCUBE1's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 2.49× lower at baseline in the lines without NCKAP5-AS2 | 0.042 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |
| [[UNC5D]] | C | NCKAP5-AS2 activity raises UNC5D's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 2.21× lower at baseline in the lines without NCKAP5-AS2 | 0.043 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |
| [[PDE10A]] | C | NCKAP5-AS2 activity raises PDE10A's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 3.76× lower at baseline in the lines without NCKAP5-AS2 | 0.048 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |
| [[KCNK2]] | C | NCKAP5-AS2 activity raises KCNK2's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 2.07× lower at baseline in the lines without NCKAP5-AS2 | 0.056 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.852). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.3, 35.9); signed map (42.4, 44.5). **Vector** length 32.2, 9.30% of its response variance represented; |z| ≥ 3 in 310 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.53 to 18).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +3.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.8 | +2.3 |
|  | [[Vitamin K4 (drug)]] 0.05 µM |  | +0.8 | +2.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | NCKAP5 antisense RNA 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q21.2 — chr2:133,264,968-133,285,445 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54065](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54065) · Entrez [101928161](https://www.ncbi.nlm.nih.gov/gene/101928161) · Ensembl [ENSG00000226953](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226953)

## Data

Gene col 13563: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13563); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13563, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13563]; `tensor/DDL_lfc|DDL_z.npy` [13563]; `embed/gene_vectors.npy` [13563]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13563 or target_col == 13563). Every well: [[NCKAP5-AS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCKAP5-AS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
