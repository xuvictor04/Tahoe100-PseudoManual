---
symbol: "CNBD1"
type: "gene"
col: 10731
ensembl_id: "ENSG00000176571"
name: "cyclic nucleotide binding domain containing 1"
location: "8q21.3"
module: 90
arm: "+"
pooled_cpm: 6.14
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 2
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# CNBD1

*cyclic nucleotide binding domain containing 1* — 8q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.41× (z +22.2, q 0e+00, up in 30 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0698×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (A498 0.0730×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRT]] (+0.87, fdr 7e-06), [[CNTNAP5]] (+0.84, fdr 7e-06), [[SORCS1]] (+0.83, fdr 7e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ZNF208]] → it (grade B ⚠); 2 go from it, the strongest it → [[CLVS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10731.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.41×** | +22.2 | 0e+00 | 30/37 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.38×** | +13.1 | 1e-36 | 29/45 (C32, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.20×** | +11.8 | 8e-30 | 23/37 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.71×** | +10.9 | 1e-25 | 27/42 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.72×** | +10.5 | 8e-24 | 3/8 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.45×** | +9.8 | 1e-20 | 15/21 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.31×** | +9.1 | 5e-18 | 26/41 (C32, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.39×** | +8.8 | 1e-16 | 4/10 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.16×** | +8.4 | 2e-15 | 21/42 (HOP62, HT-29, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +7.2 | 3e-11 | 14/37 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +6.8 | 4e-10 | 17/37 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.9 | 2e-07 | 10/45 (HOP62, A498, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.70×** | +5.8 | 2e-07 | 5/20 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.55×** | +5.3 | 4e-06 | 1/10 (A498) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.51×** | +4.5 | 3e-04 | 17/46 (C32, A-427, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +4.3 | 5e-04 | 10/35 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +3.5 | 0.012 | 13/45 (C32, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.041 | 7/40 (RKO, Panc 03.27, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10731.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0698×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (A498 0.0730×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Asciminib (drug)]] 0.05 µM |  | 0.732× | -3.4 | 0.35 | 3/44 (J82, A498, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -3.0 | 0.72 | 10/48 (HCT15, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10731. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 5.19 | 6 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 64.2× (z +16.7) | — |
| [[A-427 (line)]] | wt | 8.24 | 4 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 15.6× (z +14.8) | — |
| [[LOX-IMVI (line)]] | wt | 4.72 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.31× (z +9.7) | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0698× (z -9.5) |
| [[A498 (line)]] | wt | 2.89 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.7× (z +14.1) | [[Imiquimod (maleate) (drug)]] 5 µM 0.0730× (z -9.4) |
| [[KATO III (line)]] | alt | 4.23 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 13.3× (z +12.1) | — |
| [[NCI-H23 (line)]] | alt | 4.16 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 12.0× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 2.42 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.16× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 2.83 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 24.9× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 3.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.21× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 19.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.37× (z +9.3) | — |
| [[LoVo (line)]] | wt | 3.11 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 15.4× (z +12.9) | — |
| [[PANC-1 (line)]] | alt | 1.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.81× (z +8.6) | — |
| [[SW480 (line)]] | alt | 2.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.12× (z +8.5) | — |
| [[A-172 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10731), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRT]] | +0.87 | +0.75 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[CNTNAP5]] | +0.84 | +0.78 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[SORCS1]] | +0.83 | +0.67 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[SGCZ]] | +0.81 | +0.70 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[SCHLAP1]] | +0.81 | +0.72 / +0.86 | both halves | 7e-06 |  |
| [[LINC02511]] | +0.81 | +0.70 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[GLRA3]] | +0.80 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CLVS1]] | +0.80 | +0.70 / +0.83 | both halves | 7e-06 |  |
| [[CNTN5]] | +0.80 | +0.74 / +0.81 | both halves | 7e-06 |  |
| [[SEMA6D]] | +0.78 | +0.65 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[LINC00871]] | +0.78 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[RALYL]] | +0.78 | +0.81 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF208]] | B | ZNF208 activity raises CNBD1's level | lines that do not express ZNF208 (41) vs lines expressing it (9) | 3.75× lower at baseline in the lines without ZNF208 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC01029, ENSG00000287598 |
| [[LINC01320]] | B | LINC01320 activity raises CNBD1's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 2.62× lower at baseline in the lines without LINC01320 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168 |
| [[CALCA]] | B | CALCA activity raises CNBD1's level | lines that do not express CALCA (45) vs lines expressing it (5) | 2.50× lower at baseline in the lines without CALCA | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[TOP2A]] | B | TOP2A activity lowers CNBD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01287]] | B | LINC01287 activity raises CNBD1's level | lines that do not express LINC01287 (39) vs lines expressing it (11) | 2.75× lower at baseline in the lines without LINC01287 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253642, POU6F2, RIT2 |
| [[F11-AS1]] | B | F11-AS1 activity raises CNBD1's level | lines that do not express F11-AS1 (34) vs lines expressing it (16) | 1.65× lower at baseline in the lines without F11-AS1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent |
| [[KCNH1]] | C | KCNH1's natural level weakens CNBD1's drug response | KCNH1's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.41; direction not clear | 0.077 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[GRM7]] | C | GRM7's natural level weakens CNBD1's drug response | GRM7's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.44; direction not clear | 0.085 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLVS1]] | C | CNBD1's natural level weakens CLVS1's drug response | CNBD1's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.70, reverse -0.51; direction clear | 0.027 | ⚠ tissue can mimic it; precision caveat |
| [[OFCC1]] | C | CNBD1's natural level weakens OFCC1's drug response | CNBD1's natural level across 33 lines (lineage-adjusted; a glimpse) | r -0.78, reverse -0.59; direction not clear | 0.066 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.891). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.6, 29.7); signed map (33.1, 15.8). **Vector** length 62.4, 9.32% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.1 | +22.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +9.9 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.1 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.7 | +10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.2 | +9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +5.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.4 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +2.4 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.1 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.3 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -1.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.8 | -2.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.7 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | cyclic nucleotide binding domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.3 — chr8:86,866,415-87,615,219 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35802 |
| Matched by | ensembl_id |

UniProt [Q8NA66](https://www.uniprot.org/uniprotkb/Q8NA66) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26663](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26663) · Entrez [168975](https://www.ncbi.nlm.nih.gov/gene/168975) · UniProt [Q8NA66](https://www.uniprot.org/uniprotkb/Q8NA66) · Ensembl [ENSG00000176571](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176571)

## Data

Gene col 10731: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10731); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10731, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10731]; `tensor/DDL_lfc|DDL_z.npy` [10731]; `embed/gene_vectors.npy` [10731]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10731 or target_col == 10731). Every well: [[CNBD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNBD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
