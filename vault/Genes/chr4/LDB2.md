---
symbol: "LDB2"
type: "gene"
col: 9848
ensembl_id: "ENSG00000169744"
name: "LIM domain binding 2"
location: "4p15.32"
module: 9
arm: "+"
pooled_cpm: 4.06
n_lines_expressing: 36
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 27
direction_downstream: 1
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# LDB2

*LIM domain binding 2* — 4p15.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.39× (z +17.2, q 0e+00, up in 11 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.127×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.0629×; ⚠ cell-cycle shift, explains ~66% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.177×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.0805×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA6D]] (+0.70, fdr 9e-06), [[SLC14A2]] (+0.68, fdr 7e-06), [[PKNOX2]] (+0.67, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[LINC01242]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PKNOX2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9848.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.39×** | +17.2 | 0e+00 | 11/21 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.72×** | +14.9 | 0e+00 | 1/5 (Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.32×** | +12.0 | 9e-31 | 6/12 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +9.6 | 8e-20 | 11/24 (CFPAC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.77×** | +9.4 | 6e-19 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.91×** | +9.1 | 7e-18 | 18/31 (C32, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.19×** | +7.8 | 5e-13 | 9/28 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +5.0 | 4e-05 | 11/23 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +4.3 | 0.001 | 0/10 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.005 | 1/21 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +3.7 | 0.012 | 5/21 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.6 | 0.014 | 2/15 (HOP62, NCI-H460) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.026 | 3/23 (HEC-1-A, HS-578T, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.44×** | +3.4 | 0.031 | 5/17 (LOX-IMVI, SK-MEL-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.048 | 7/30 (SK-MEL-2, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +3.0 | 0.087 | 4/24 (SK-MEL-2, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.0 | 0.091 | 1/26 (NCI-H23) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9848.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.127×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.0629×; ⚠ cell-cycle shift, explains ~66% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.177×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.0805×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Peretinoin (drug)]] 5 µM |  | 0.706× | -3.3 | 0.45 | 6/25 (A498, AsPC-1, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 0.728× | -3.2 | 0.45 | 1/26 (HEC-1-A) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9848. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 112 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -12.4) |
| [[H4 (line)]] | wt | 42.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.899 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.988 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.997 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.896 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.941 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.933 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.916 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.803 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.929 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.951 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.952 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9848), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA6D]] | +0.70 | +0.57 / +0.74 | both halves | 9e-06 | **novel candidate** |
| [[SLC14A2]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[PKNOX2]] | +0.67 | +0.63 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTSL1]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[CDH12]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[ATRNL1]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SORCS1]] | +0.64 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[CNTN4]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[ST8SIA1]] | +0.64 | +0.45 / +0.73 | both halves | 3e-05 |  |
| [[LINC01266]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[CFAP20DC-DT]] | +0.63 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[SGCD]] | +0.63 | +0.59 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 26, C 1. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01242]] | B | LINC01242 activity raises LDB2's level | lines that do not express LINC01242 (42) vs lines expressing it (8) | 4.46× lower at baseline in the lines without LINC01242 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, LINC00879, ENSG00000234426; maybe low, not absent |
| [[HTR1F]] | B | HTR1F activity raises LDB2's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 3.72× lower at baseline in the lines without HTR1F | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent |
| [[HGF]] | B | HGF activity raises LDB2's level | lines that do not express HGF (38) vs lines expressing it (12) | 3.53× lower at baseline in the lines without HGF | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA |
| [[KC6]] | B | KC6 activity raises LDB2's level | lines that do not express KC6 (32) vs lines expressing it (18) | 3.48× lower at baseline in the lines without KC6 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1 |
| [[PDZRN3]] | B | PDZRN3 activity raises LDB2's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 2.54× lower at baseline in the lines without PDZRN3 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[HMCN1]] | B | HMCN1 activity raises LDB2's level | lines that do not express HMCN1 (26) vs lines expressing it (24) | 2.40× lower at baseline in the lines without HMCN1 | 0.020 | ⚠ within organs, on part of the lines; also absent: EPHA5, EPHA5-AS1, ITGA4; maybe low, not absent |
| [[TIMP3]] | B | TIMP3 activity raises LDB2's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 3.31× lower at baseline in the lines without TIMP3 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1 |
| [[PCSK2]] | B | PCSK2 activity raises LDB2's level | lines that do not express PCSK2 (27) vs lines expressing it (23) | 2.38× lower at baseline in the lines without PCSK2 | 0.032 | ⚠ within organs, on part of the lines; also absent: PGR, UNC5D, PDE3A; maybe low, not absent |
| [[BAALC]] | B | BAALC activity raises LDB2's level | lines that do not express BAALC (32) vs lines expressing it (18) | 2.34× lower at baseline in the lines without BAALC | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |
| [[EBF1]] | B | EBF1 activity raises LDB2's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 2.65× lower at baseline in the lines without EBF1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4 |
| [[CNTN6]] | B | CNTN6 activity raises LDB2's level | lines that do not express CNTN6 (38) vs lines expressing it (12) | 3.16× lower at baseline in the lines without CNTN6 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC02476, SPARC; maybe low, not absent |
| [[CCDC144NL-AS1]] | B | CCDC144NL-AS1 activity raises LDB2's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 2.33× lower at baseline in the lines without CCDC144NL-AS1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKNOX2]] | B | LDB2 activity raises PKNOX2's level | lines that do not express LDB2 (14) vs lines expressing it (36) | 1.63× lower at baseline in the lines without LDB2 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000256915, SLC2A14, ENSG00000253496; maybe low, not absent |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.2, 29.7); signed map (36.2, 33.8). **Vector** length 42.9, 6.98% of its response variance represented; |z| ≥ 3 in 670 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +12.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +3.0 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -0.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -1.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | LIM domain binding 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.32 — chr4:16,501,541-16,898,678 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CLIM1, LDB1 |
| Gene groups (HGNC) | Wnt enhanceosome complex |
| Matched by | ensembl_id |

**Function**, from UniProt [O43679](https://www.uniprot.org/uniprotkb/O43679) (LIM domain-binding protein 2):

> Transcription cofactor. Binds to the LIM domain of a wide variety of LIM domain-containing transcription factors.

**Summary**, from NCBI Gene [9079](https://www.ncbi.nlm.nih.gov/gene/9079):

> The protein encoded by this gene belongs to the LIM-domain binding family. Members of this family are characterized by a conserved nuclear localization sequence, an amino-terminal homodimerization domain and a carboxy-terminal LIM interaction domain. These proteins function as adapter molecules to allow assembly of transcriptional regulatory complexes. Genetic association studies suggest functions for this gene in rhegmatogenous retinal detachment and coronary artery disease. Alternative …

**Accessions** — [HGNC:6533](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6533) · Entrez [9079](https://www.ncbi.nlm.nih.gov/gene/9079) · UniProt [O43679](https://www.uniprot.org/uniprotkb/O43679) · Ensembl [ENSG00000169744](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169744)

## Data

Gene col 9848: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9848); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9848, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9848]; `tensor/DDL_lfc|DDL_z.npy` [9848]; `embed/gene_vectors.npy` [9848]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9848 or target_col == 9848). Every well: [[LDB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LDB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
