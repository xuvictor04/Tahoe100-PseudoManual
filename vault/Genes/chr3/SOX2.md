---
symbol: "SOX2"
type: "gene"
col: 11187
ensembl_id: "ENSG00000181449"
name: "SRY-box transcription factor 2"
location: "3q26.33"
module: 9
arm: "+"
pooled_cpm: 8.01
n_lines_expressing: 15
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SOX2

*SRY-box transcription factor 2* — 3q26.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.91× (z +12.9, q 2e-35, up in 6 of 10 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (C-33 A 0.223×, NCI-H661 0.215×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H661 0.0864×, C-33 A 0.196×); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H661 0.0984×, C-33 A 0.203×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 2 lines (C-33 A 0.178×, NCI-H661 0.145×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NR2F1]] (+0.63, fdr 1e-05), [[CACNB2]] (+0.58, fdr 1e-05), [[MEF2C]] (+0.55, fdr 3e-05); moves opposite to [[TPD52L2]] (-0.51, fdr 6e-05), [[SDCBP2]] (-0.48, fdr 9e-05), [[RAPGEF3]] (-0.46, fdr 3e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[RUNX1T1]] → it (grade C ⚠); 10 go from it, the strongest it → [[ZNF608]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11187.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.91×** | +12.9 | 2e-35 | 6/10 (CFPAC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.81×** | +9.8 | 4e-20 | 7/10 (CFPAC-1, KATO III, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.15×** | +7.4 | 3e-11 | 1/5 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.95×** | +7.0 | 5e-10 | 8/10 (CFPAC-1, SW480, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.82×** | +6.9 | 5e-10 | 2/8 (SW480, SW 900) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +6.3 | 3e-08 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.37×** | +5.8 | 7e-07 | 7/12 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +5.0 | 5e-05 | 5/12 (KATO III, SHP-77, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **2.09×** | +4.9 | 5e-05 | 4/7 (SW480, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.07×** | +4.9 | 6e-05 | 7/10 (CFPAC-1, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.94×** | +4.4 | 5e-04 | 7/11 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +4.4 | 6e-04 | 6/10 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +4.0 | 0.003 | 3/7 (KATO III, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.79×** | +3.9 | 0.004 | 6/11 (SW480, KATO III, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.79×** | +3.9 | 0.004 | 7/11 (KATO III, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +3.8 | 0.005 | 1/9 (KATO III) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +3.5 | 0.013 | 5/11 (NCI-H1573, H4, …) | rises with dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.029 | 1/12 (CFPAC-1) | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.038 | 1/10 (SHP-77) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.57×** | +3.0 | 0.065 | 1/11 (C32) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +2.9 | 0.087 | 0/12 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (C-33 A 0.223×, NCI-H661 0.215×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H661 0.0864×, C-33 A 0.196×); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H661 0.0984×, C-33 A 0.203×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 2 lines (C-33 A 0.178×, NCI-H661 0.145×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11187. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 330 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -13.5) |
| [[NCI-H661 (line)]] | alt | 310 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0864× (z -13.1) |
| [[CFPAC-1 (line)]] | alt | 16.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.7× (z +19.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[KATO III (line)]] | alt | 14.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.56× (z +13.8) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW480 (line)]] | alt | 24.6 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 9.34× (z +10.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.997 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.886 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.956 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.916 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.852 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.914 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.45 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11187), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR2F1]] | +0.63 | +0.50 / +0.65 | both halves | 1e-05 | STRING 454 |
| [[CACNB2]] | +0.58 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[MEF2C]] | +0.55 | +0.45 / +0.52 | both halves | 3e-05 | pathway: Transcriptional Regulation by MECP2; STRING 626 |
| [[LINC01194]] | +0.54 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[SOBP]] | +0.54 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[POGZ]] | +0.53 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[RUNX1T1]] | +0.53 | +0.31 / +0.63 | both halves | 2e-04 |  |
| [[LINC02197]] | +0.52 | +0.26 / +0.62 | both halves | 4e-04 |  |
| [[NPFFR2]] | +0.51 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[JADE1]] | +0.51 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[ID3]] | +0.51 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[RALYL]] | +0.51 | +0.50 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPD52L2]] | -0.51 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[SDCBP2]] | -0.48 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[RAPGEF3]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[NIBAN2]] | -0.46 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[RBM44]] | -0.45 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[JMJD7]] | -0.45 | -0.32 / -0.34 | both halves | 2e-04 |  |
| [[SCAT1]] | -0.44 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[BLACAT1]] | -0.44 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[EHBP1L1]] | -0.44 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[LINC02320]] | -0.44 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[RAB43]] | -0.43 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[ZDHHC6]] | -0.43 | -0.31 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RUNX1T1]] | C | RUNX1T1 activity raises SOX2's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.82× lower at baseline in the lines without RUNX1T1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[LINC02506]] | C | LINC02506 activity raises SOX2's level | lines that do not express LINC02506 (40) vs lines expressing it (10) | 2.64× lower at baseline in the lines without LINC02506 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OVAAL, LINC01610, ENSG00000241168; co-absent with the target |
| [[LINC02197]] | C | LINC02197 activity raises SOX2's level | lines that do not express LINC02197 (35) vs lines expressing it (15) | 3.18× lower at baseline in the lines without LINC02197 | 0.060 | ⚠ within organs, on part of the lines; also absent: RIT2, SNTG1, CALCA; maybe low, not absent; co-absent with the target |
| [[FUT9]] | C | FUT9 activity raises SOX2's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 2.31× lower at baseline in the lines without FUT9 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF608]] | B | SOX2 activity raises ZNF608's level | lines that do not express SOX2 (35) vs lines expressing it (15) | 2.98× lower at baseline in the lines without SOX2 | 0.086 | ⚠ within organs, on part of the lines; also absent: SNTG1, SCG3, CGA |
| [[SEMA6A]] | B | SOX2 activity raises SEMA6A's level | lines that do not express SOX2 (35) vs lines expressing it (15) | 2.29× lower at baseline in the lines without SOX2 | 0.087 | ⚠ within organs, on part of the lines; also absent: SNTG1, SCG3, CGA |
| [[FAM171A1]] | B | SOX2 activity lowers FAM171A1's level | lines that do not express SOX2 (35) vs lines expressing it (15) | 1.79× higher at baseline in the lines without SOX2 | 0.089 | ⚠ within organs, on part of the lines; also absent: SNTG1, SCG3, CGA |
| [[BLACAT1]] | B | SOX2 activity raises BLACAT1's level | lines that do not express SOX2 (35) vs lines expressing it (15) | 1.40× lower at baseline in the lines without SOX2 | 0.091 | ⚠ within organs, on part of the lines; also absent: SNTG1, SCG3, CGA |
| [[RUNX1T1]] | C | SOX2 activity raises RUNX1T1's level | lines that do not express SOX2 (35) vs lines expressing it (15) | 3.44× lower at baseline in the lines without SOX2 | 0.012 | ⚠ within organs, on part of the lines; also absent: SNTG1, SCG3, CGA; co-absent with the target |
| [[PPARGC1A]] | C | SOX2 activity raises PPARGC1A's level | lines that do not express SOX2 (35) vs lines expressing it (15) | 2.40× lower at baseline in the lines without SOX2 | 0.034 | ⚠ within organs, on part of the lines; also absent: SNTG1, SCG3, CGA; co-absent with the target |
| [[FOXA2]] | C | SOX2 activity raises FOXA2's level | lines that do not express SOX2 (35) vs lines expressing it (15) | 1.86× lower at baseline in the lines without SOX2 | 0.048 | ⚠ within organs, on part of the lines; also absent: SNTG1, SCG3, CGA; co-absent with the target |
| [[CXXC4]] | C | SOX2 activity raises CXXC4's level | lines that do not express SOX2 (35) vs lines expressing it (15) | 2.85× lower at baseline in the lines without SOX2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SNTG1, SCG3, CGA; co-absent with the target |
| [[SEMA3E]] | C | SOX2 activity raises SEMA3E's level | lines that do not express SOX2 (35) vs lines expressing it (15) | 2.49× lower at baseline in the lines without SOX2 | 0.079 | ⚠ within organs, on part of the lines; also absent: SNTG1, SCG3, CGA; co-absent with the target |
| [[FGF9]] | C | SOX2 activity raises FGF9's level | lines that do not express SOX2 (35) vs lines expressing it (15) | 1.85× lower at baseline in the lines without SOX2 | 0.091 | ⚠ within organs, on part of the lines; also absent: SNTG1, SCG3, CGA; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.549). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.6, 38.0); signed map (42.5, 34.2). **Vector** length 35.2, 10.1% of its response variance represented; |z| ≥ 3 in 276 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.1 | +9.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +1.9 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +12.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +1.5 | +7.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.0 | +0.8 |
| fall | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -2.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -1.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.8 | -2.4 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.8 | +0.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.7 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | SRY-box transcription factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.33 — chr3:181,711,925-181,714,436 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SRY-box transcription factors |
| Reactome | 19 pathways, smallest: Formation of the posterior neural plate; Formation of the anterior neural plate; POU5F1 (OCT4), SOX2, NANOG repress genes related to differentiation |
| Matched by | ensembl_id |

**Function**, from UniProt [P48431](https://www.uniprot.org/uniprotkb/P48431) (Transcription factor SOX-2):

> Transcription factor that forms a trimeric complex with OCT4 on DNA and controls the expression of a number of genes involved in embryonic development such as YES1, FGF4, UTF1 and ZFP206 (By similarity). Binds to the proximal enhancer region of NANOG (By similarity). Critical for early embryogenesis and for embryonic stem cell pluripotency. Downstream SRRT target that mediates the promotion of neural stem cell self-renewal (By similarity). Keeps neural cells undifferentiated by counteracting …

**Summary**, from NCBI Gene [6657](https://www.ncbi.nlm.nih.gov/gene/6657):

> This intronless gene encodes a member of the SRY-related HMG-box (SOX) family of transcription factors involved in the regulation of embryonic development and in the determination of cell fate. The product of this gene is required for stem-cell maintenance in the central nervous system, and also regulates gene expression in the stomach. Mutations in this gene have been associated with optic nerve hypoplasia and with syndromic microphthalmia, a severe form of structural eye malformation. This …

**Accessions** — [HGNC:11195](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11195) · Entrez [6657](https://www.ncbi.nlm.nih.gov/gene/6657) · UniProt [P48431](https://www.uniprot.org/uniprotkb/P48431) · Ensembl [ENSG00000181449](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181449)

## Data

Gene col 11187: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11187); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11187, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11187]; `tensor/DDL_lfc|DDL_z.npy` [11187]; `embed/gene_vectors.npy` [11187]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11187 or target_col == 11187). Every well: [[SOX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
