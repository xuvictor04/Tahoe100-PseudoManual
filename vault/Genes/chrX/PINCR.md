---
symbol: "PINCR"
type: "gene"
col: 13394
ensembl_id: "ENSG00000224294"
name: "p53-induced noncoding RNA"
location: "Xp11.3"
module: 62
arm: "+"
pooled_cpm: 3.47
n_lines_expressing: 21
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 8
direction_downstream: 75
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# PINCR

*p53-induced noncoding RNA* — Xp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.23× (z +9.4, q 3e-18, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 3.86× (z +9.2, q 1e-17, up in 13 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Lumateperone (tosylate) (drug)]] 0.5 µM: 0.571× (z -3.8, q 0.081, down in 3 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (LS 180 0.0226×); [[Belinostat (drug)]] 5 µM in 1 line (LS 180 0.0390×); [[Panobinostat (drug)]] 0.5 µM in 1 line (LS 180 0.0559×; ⚠ cell-cycle shift, explains ~21% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 0.104×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA18]] (+0.83, fdr 7e-06), [[PTCHD4]] (+0.80, fdr 7e-06), [[GRIN2C]] (+0.79, fdr 7e-06).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 75 go from it, the strongest it → [[MDM2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13394.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.23×** | +9.4 | 3e-18 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.86×** | +9.2 | 1e-17 | 13/17 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.39×** | +8.2 | 3e-14 | 9/14 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.50×** | +8.2 | 4e-14 | 7/10 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.57×** | +8.0 | 2e-13 | 1/5 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.08×** | +7.0 | 3e-10 | 9/18 (NCI-H460, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.08×** | +6.8 | 6e-10 | 10/19 (NCI-H460, A498, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.83×** | +6.8 | 9e-10 | 9/15 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +6.2 | 3e-08 | 2/10 (Hs 766T, H4) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.37×** | +5.8 | 3e-07 | 2/11 (SHP-77, SW480) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +5.5 | 3e-06 | 2/17 (LoVo, A498) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +5.3 | 5e-06 | 8/13 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.32×** | +5.2 | 9e-06 | 2/6 (A549, NCI-H460) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | **1.73×** | +5.1 | 1e-05 | 10/17 (NCI-H460, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +4.7 | 1e-04 | 9/19 (SHP-77, Hs 766T, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.92×** | +4.4 | 3e-04 | 3/18 (H4, NCI-H460, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +3.3 | 0.026 | 5/17 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.41×** | +3.2 | 0.044 | 5/18 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.64×** | +3.1 | 0.054 | 7/12 (SNU-1, H4, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +2.9 | 0.098 | 14/19 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.81×** | +2.9 | 0.099 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13394.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (LS 180 0.0226×); [[Belinostat (drug)]] 5 µM in 1 line (LS 180 0.0390×); [[Panobinostat (drug)]] 0.5 µM in 1 line (LS 180 0.0559×; ⚠ cell-cycle shift, explains ~21% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 0.104×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | **0.571×** | -3.8 | 0.081 | 3/18 (hTERT-HPNE, A-172, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.616× | -3.3 | 0.29 | 0/19 | inconsistent across doses |  |
| [[Sinomenine (drug)]] 0.5 µM |  | 0.634× | -3.1 | 0.36 | 3/18 (hTERT-HPNE, SW480, …) | inconsistent across doses |  |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 0.726× | -3.0 | 0.36 | 3/19 (SW48, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13394. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.82 | 11 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.6× (z +10.9) | — |
| [[LS 180 (line)]] | wt | 20.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0226× (z -14.7) |
| [[H4 (line)]] | wt | 20.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -9.5) |
| [[SW480 (line)]] | alt | 12.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 1.45 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 80.3× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0994× (z -9.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.598 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.288 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13394), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA18]] | +0.83 | +0.70 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[PTCHD4]] | +0.80 | +0.65 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[GRIN2C]] | +0.79 | +0.60 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[PURPL]] | +0.78 | +0.63 / +0.82 | both halves | 7e-06 | same gene group |
| [[ZMAT3]] | +0.75 | +0.69 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[EDA2R]] | +0.75 | +0.53 / +0.78 | both halves | 1e-05 | **novel candidate** |
| [[ACTA2]] | +0.74 | +0.65 / +0.78 | both halves | 7e-06 |  |
| [[FDXR]] | +0.74 | +0.60 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTS7]] | +0.71 | +0.56 / +0.76 | both halves | 1e-05 | **novel candidate** |
| [[DNAI3]] | +0.71 | +0.50 / +0.75 | both halves | 1e-05 |  |
| [[MDM2]] | +0.71 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[ABCA12]] | +0.71 | +0.59 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PINCR's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.2% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[FAM13C]] | B | FAM13C activity raises PINCR's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 2.00× lower at baseline in the lines without FAM13C | 0.048 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| [[ADAMTS7]] | B | ADAMTS7 activity raises PINCR's level | lines that do not express ADAMTS7 (17) vs lines expressing it (33) | 1.48× lower at baseline in the lines without ADAMTS7 | 0.063 | ⚠ within organs, on part of the lines; also absent: VASH1, FHL1, ANTXR1; maybe low, not absent |
| [[GRIN2C]] | B | GRIN2C activity raises PINCR's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 2.28× lower at baseline in the lines without GRIN2C | 0.067 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[GAS6-AS1]] | B | GAS6-AS1 activity raises PINCR's level | lines that do not express GAS6-AS1 (16) vs lines expressing it (34) | 2.14× lower at baseline in the lines without GAS6-AS1 | 0.082 | ⚠ within organs, on part of the lines; also absent: ECM1, LINC02055, LINC02220; maybe low, not absent |
| [[PTCHD4]] | C | PTCHD4 activity raises PINCR's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 2.59× lower at baseline in the lines without PTCHD4 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1; co-absent with the target |
| [[PURPL]] | C | PURPL activity raises PINCR's level | lines that do not express PURPL (25) vs lines expressing it (25) | 2.30× lower at baseline in the lines without PURPL | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1; co-absent with the target |
| [[EDA2R]] | C | EDA2R activity raises PINCR's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.54× lower at baseline in the lines without EDA2R | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3; co-absent with the target |

### Downstream of this gene

*75 arrows, 75 of them with an alert ⚠; grade A 0, B 73, C 2. Shown: the 12 strongest; 63 more arrows (63 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MDM2]] | B | PINCR activity raises MDM2's level | lines that do not express PINCR (29) vs lines expressing it (21) | 2.44× lower at baseline in the lines without PINCR | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[FDXR]] | B | PINCR activity raises FDXR's level | lines that do not express PINCR (29) vs lines expressing it (21) | 3.22× lower at baseline in the lines without PINCR | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[AEN]] | B | PINCR activity raises AEN's level | lines that do not express PINCR (29) vs lines expressing it (21) | 2.29× lower at baseline in the lines without PINCR | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[ZMAT3]] | B | PINCR activity raises ZMAT3's level | lines that do not express PINCR (29) vs lines expressing it (21) | 2.98× lower at baseline in the lines without PINCR | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[CYFIP2]] | B | PINCR activity raises CYFIP2's level | lines that do not express PINCR (29) vs lines expressing it (21) | 2.54× lower at baseline in the lines without PINCR | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[DDB2]] | B | PINCR activity raises DDB2's level | lines that do not express PINCR (29) vs lines expressing it (21) | 2.15× lower at baseline in the lines without PINCR | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[ZNF79]] | B | PINCR activity raises ZNF79's level | lines that do not express PINCR (29) vs lines expressing it (21) | 1.44× lower at baseline in the lines without PINCR | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[ZMAT3]] | B | PINCR activity weakens ZMAT3's drug response | lines that do not express PINCR (25) vs lines expressing it (19) | the lines without PINCR respond 1.16× as strongly (z diff -0.62); strongest at Panobinostat 0.5 µM: 2.44x vs 0.86x (z diff -6.2) | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; both ways; artifact flags |
| [[BAX]] | B | PINCR activity strengthens BAX's drug response | lines that do not express PINCR (29) vs lines expressing it (19) | the lines without PINCR respond 0.73× as strongly (z diff +0.77); strongest at Selinexor 5 µM: 1.12x vs 1.80x (z diff +3.2) | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[ACTA2]] | B | PINCR activity strengthens ACTA2's drug response | lines that do not express PINCR (19) vs lines expressing it (17) | the lines without PINCR respond 0.55× as strongly (z diff +2.40); strongest at Mitoxantrone (dihydrochloride) 5 µM: 1.50x vs 2.56x (z diff +4.0) | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[BLOC1S2]] | B | PINCR activity strengthens BLOC1S2's drug response | lines that do not express PINCR (29) vs lines expressing it (19) | the lines without PINCR respond 0.82× as strongly (z diff +0.80); strongest at Topotecan (hydrochloride) 5 µM: 1.74x vs 2.94x (z diff +3.0) | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[SESN1]] | B | PINCR activity strengthens SESN1's drug response | lines that do not express PINCR (29) vs lines expressing it (20) | the lines without PINCR respond 0.84× as strongly (z diff +0.80); strongest at Topotecan (hydrochloride) 5 µM: 1.66x vs 2.76x (z diff +3.6) | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; both ways; artifact flags |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.888). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.6, 36.9); signed map (42.9, -23.6). **Vector** length 68.9, 23.6% of its response variance represented; |z| ≥ 3 in 504 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *p53 targets up* (control, mean cos +0.64 to 26); *p53 pathway* (hallmark, mean cos +0.59 to 26); *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.61 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +5.2 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +8.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +8.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.8 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +3.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +4.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -1.9 | -2.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | p53-induced noncoding RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xp11.3 — chrX:43,176,994-43,226,598 (+) |
| Ensembl biotype | lncRNA |
| Also known as | RP3-326I13.1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53590](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53590) · Entrez [101927501](https://www.ncbi.nlm.nih.gov/gene/101927501) · Ensembl [ENSG00000224294](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224294)

## Data

Gene col 13394: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13394); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13394, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13394]; `tensor/DDL_lfc|DDL_z.npy` [13394]; `embed/gene_vectors.npy` [13394]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13394 or target_col == 13394). Every well: [[PINCR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PINCR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
