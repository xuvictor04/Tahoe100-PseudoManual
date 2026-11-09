---
symbol: "PTPRT"
type: "gene"
col: 12128
ensembl_id: "ENSG00000196090"
name: "protein tyrosine phosphatase receptor type T"
location: "20q12-q13.11"
module: 90
arm: "+"
pooled_cpm: 2.72
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 5
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# PTPRT

*protein tyrosine phosphatase receptor type T* — 20q12-q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.08× (z +24.3, q 0e+00, up in 31 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.190×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNTNAP5]] (+0.88, fdr 7e-06), [[CNBD1]] (+0.87, fdr 7e-06), [[SGCZ]] (+0.85, fdr 7e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CALCA]] → it (grade B ⚠); 5 go from it, the strongest it → [[CLVS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12128.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.08×** | +24.3 | 0e+00 | 31/33 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.53×** | +13.8 | 7e-41 | 1/3 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.26×** | +13.8 | 8e-41 | 10/12 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.64×** | +13.1 | 6e-37 | 32/44 (A-427, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.33×** | +11.4 | 7e-28 | 23/34 (BT-474, SW48, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.96×** | +10.3 | 5e-23 | 26/41 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.38×** | +10.2 | 2e-22 | 3/7 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +7.0 | 1e-10 | 15/34 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +6.4 | 1e-08 | 14/29 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +5.4 | 3e-06 | 9/25 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.74×** | +5.2 | 8e-06 | 19/45 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.1 | 1e-05 | 11/44 (HOP62, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.71×** | +5.1 | 1e-05 | 2/11 (RKO, PANC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.73×** | +5.0 | 2e-05 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.4 | 4e-04 | 3/12 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +4.4 | 4e-04 | 9/32 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.58×** | +4.4 | 4e-04 | 14/44 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.53×** | +4.1 | 0.001 | 3/43 (LoVo, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +3.9 | 0.003 | 12/38 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.032 | 3/42 (SNU-423, COLO 205, …) | inconsistent across doses |  |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.46×** | +3.2 | 0.039 | 2/25 (SW1417, HOP62) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.87×** | +3.1 | 0.043 | 5/36 (NCI-H2030, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12128.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.190×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.893× | -3.8 | 0.083 | 13/47 (HepG2/C3A, BT-474, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.690× | -3.1 | 0.55 | 8/43 (LS 180, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12128. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.15 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.20× (z +9.7) | — |
| [[SW480 (line)]] | alt | 2.01 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.9× (z +14.0) | — |
| [[A-427 (line)]] | wt | 1.99 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 20.1× (z +10.7) | — |
| [[A549 (line)]] | wt | 2.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.65× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 2.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.4× (z +11.3) | — |
| [[C32 (line)]] | wt | 2.10 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.8× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 2.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.70× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 1.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +8.7) | — |
| [[KATO III (line)]] | alt | 2.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +10.4) | — |
| [[LoVo (line)]] | wt | 1.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +11.1) | — |
| [[NCI-H460 (line)]] | wt | 3.42 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 22.3× (z +12.3) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 1.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.41× (z +9.6) | — |
| [[RKO (line)]] | wt | 2.06 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.6× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 28.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -9.7) |
| [[SW1417 (line)]] | alt | 3.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.60× (z +10.0) | — |
| [[A-172 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12128), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTNAP5]] | +0.88 | +0.75 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[CNBD1]] | +0.87 | +0.75 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[SGCZ]] | +0.85 | +0.66 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[CNTN5]] | +0.82 | +0.71 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[USH2A]] | +0.82 | +0.62 / +0.88 | both halves | 7e-06 | same gene group |
| [[PWRN1]] | +0.81 | +0.59 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[SCHLAP1]] | +0.80 | +0.63 / +0.88 | both halves | 7e-06 |  |
| [[LINC00861]] | +0.79 | +0.66 / +0.79 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.79 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[SEMA6D]] | +0.79 | +0.67 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[CLVS1]] | +0.78 | +0.74 / +0.80 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.78 | +0.73 / +0.82 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALCA]] | B | CALCA activity raises PTPRT's level | lines that do not express CALCA (45) vs lines expressing it (5) | 1.85× lower at baseline in the lines without CALCA | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[TOP2A]] | B | TOP2A activity lowers PTPRT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CCDC39]] | C | CCDC39's natural level weakens PTPRT's drug response | CCDC39's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.69, reverse -0.01; direction clear | 0.041 | ⚠ tissue can mimic it; precision caveat |
| [[GLRA3]] | C | GLRA3's natural level weakens PTPRT's drug response | GLRA3's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.68, reverse -0.45; direction clear | 0.045 | ⚠ tissue can mimic it; precision caveat |
| [[CLVS1]] | C | CLVS1's natural level weakens PTPRT's drug response | CLVS1's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.79; direction not clear | 0.061 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CNTNAP5]] | C | CNTNAP5's natural level weakens PTPRT's drug response | CNTNAP5's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.31; direction clear | 0.063 | ⚠ tissue can mimic it; precision caveat |
| [[VENTXP1]] | C | VENTXP1's natural level weakens PTPRT's drug response | VENTXP1's natural level across 32 lines (lineage-adjusted; a glimpse) | r -0.79, reverse -0.40; direction clear | 0.075 | ⚠ tissue can mimic it; precision caveat |
| [[GRM7]] | C | GRM7's natural level weakens PTPRT's drug response | GRM7's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.51; direction not clear | 0.085 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLVS1]] | C | PTPRT's natural level weakens CLVS1's drug response | PTPRT's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.79, reverse -0.67; direction clear | 9e-04 | ⚠ tissue can mimic it; precision caveat |
| [[CHRM5]] | C | PTPRT's natural level weakens CHRM5's drug response | PTPRT's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.78, reverse -0.64; direction clear | 0.003 | ⚠ tissue can mimic it; precision caveat |
| [[C2CD5-AS1]] | C | PTPRT's natural level weakens C2CD5-AS1's drug response | PTPRT's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.69, reverse +0.22; direction clear | 0.015 | ⚠ tissue can mimic it; precision caveat |
| [[LINC00578]] | C | PTPRT's natural level weakens LINC00578's drug response | PTPRT's natural level across 43 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.50; direction clear | 0.066 | ⚠ tissue can mimic it; precision caveat |
| [[MAN1C1]] | C | PTPRT's natural level weakens MAN1C1's drug response | PTPRT's natural level across 37 lines (lineage-adjusted; a glimpse) | r -0.72, reverse -0.59; direction clear | 0.078 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.884). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.5, 29.9); signed map (32.7, 15.6). **Vector** length 54.8, 7.43% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +24.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +13.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +5.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +2.2 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -3.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | +0.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -2.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase receptor type T |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q12-q13.11 — chr20:42,072,752-43,189,970 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPTPrho, KIAA0283 |
| Gene groups (HGNC) | Fibronectin type III domain containing; Immunoglobulin like domain containing; Protein tyrosine phosphatases receptor type |
| Matched by | ensembl_id |

**Function**, from UniProt [O14522](https://www.uniprot.org/uniprotkb/O14522) (Receptor-type tyrosine-protein phosphatase T):

> May be involved in both signal transduction and cellular adhesion in the CNS.

**Summary**, from NCBI Gene [11122](https://www.ncbi.nlm.nih.gov/gene/11122):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP possesses an extracellular region, a single transmembrane region, and two tandem intracellular catalytic domains, and thus represents a receptor-type PTP. The extracellular region contains a meprin-A5 antigen-PTP (MAM) …

**Accessions** — [HGNC:9682](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9682) · Entrez [11122](https://www.ncbi.nlm.nih.gov/gene/11122) · UniProt [O14522](https://www.uniprot.org/uniprotkb/O14522) · Ensembl [ENSG00000196090](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196090)

## Data

Gene col 12128: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12128); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12128, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12128]; `tensor/DDL_lfc|DDL_z.npy` [12128]; `embed/gene_vectors.npy` [12128]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12128 or target_col == 12128). Every well: [[PTPRT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPRT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
