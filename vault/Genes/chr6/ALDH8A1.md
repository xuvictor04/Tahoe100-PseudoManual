---
symbol: "ALDH8A1"
type: "gene"
col: 3999
ensembl_id: "ENSG00000118514"
name: "aldehyde dehydrogenase 8 family member A1"
location: "6q23.3"
module: 39
arm: "+"
pooled_cpm: 4.98
n_lines_expressing: 49
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 14
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# ALDH8A1

*aldehyde dehydrogenase 8 family member A1* — 6q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.44× (z +14.0, q 2e-41, up in 37 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Radotinib (drug)]] 5 µM: 0.720× (z -3.8, q 0.093, down in 14 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H460 0.0997×); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (LoVo 0.132×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IMPA1P1]] (+0.88, fdr 7e-06), [[USP50]] (+0.87, fdr 7e-06), [[SLC6A13]] (+0.87, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[FSIP2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3999.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.44×** | +14.0 | 2e-41 | 37/39 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.60×** | +10.2 | 4e-22 | 32/40 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.86×** | +10.0 | 4e-21 | 12/18 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.49×** | +9.8 | 2e-20 | 35/43 (SW480, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +8.5 | 2e-15 | 27/37 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.30×** | +7.8 | 6e-13 | 33/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.61×** | +7.4 | 1e-11 | 29/42 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.41×** | +6.7 | 1e-09 | 21/37 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +6.7 | 1e-09 | 26/40 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.16×** | +6.1 | 4e-08 | 25/44 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.65×** | +5.6 | 9e-07 | 17/46 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +5.5 | 2e-06 | 3/10 (NCI-H2030, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +5.3 | 6e-06 | 20/45 (SW480, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.92×** | +4.5 | 3e-04 | 19/41 (NCI-H460, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.72×** | +4.2 | 0.001 | 13/39 (COLO 205, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.70×** | +4.0 | 0.002 | 13/43 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +3.9 | 0.003 | 14/45 (KATO III, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3999.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H460 0.0997×); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (LoVo 0.132×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **0.720×** | -3.8 | 0.093 | 14/45 (SW 900, RKO, …) | top dose only |  |
| [[Carbamazepine (drug)]] 0.5 µM |  | 0.657× | -3.4 | 0.19 | 17/43 (A-427, SW48, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.659× | -3.2 | 0.22 | 16/43 (hTERT-HPNE, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | 0.677× | -3.2 | 0.22 | 9/30 (BT-474, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Pralsetinib (drug)]] 5 µM |  | 0.483× | -3.1 | 0.22 | 9/27 (NCI-H1573, J82, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.676× | -3.0 | 0.22 | 16/43 (BT-474, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3999. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.26 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 15.8× (z +10.8) ⚠ toxic; transcription drop | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0997× (z -9.8) |
| [[SW480 (line)]] | alt | 4.33 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 32.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +10.9) | — |
| [[LoVo (line)]] | wt | 8.01 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.132× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 8.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 2.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.9× (z +12.3) | — |
| [[A-172 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.921 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3999), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMPA1P1]] | +0.88 | +0.89 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[USP50]] | +0.87 | +0.88 / +0.80 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.87 | +0.90 / +0.80 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.86 | +0.87 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[LINC01031]] | +0.85 | +0.83 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[LINC01191]] | +0.85 | +0.88 / +0.74 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.84 | +0.87 / +0.76 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.83 | +0.85 / +0.74 | both halves | 7e-06 |  |
| [[OIT3]] | +0.83 | +0.81 / +0.78 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.82 | +0.77 / +0.78 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.82 | +0.78 / +0.81 | both halves | 7e-06 |  |
| [[GARIN1B]] | +0.81 | +0.81 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 8, C 6. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises ALDH8A1's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 2.12× lower at baseline in the lines without FSIP2-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[SLC26A4]] | B | SLC26A4 activity raises ALDH8A1's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.63× lower at baseline in the lines without SLC26A4 | 0.019 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[CD226]] | B | CD226 activity raises ALDH8A1's level | lines that do not express CD226 (7) vs lines expressing it (43) | 2.13× lower at baseline in the lines without CD226 | 0.023 | ⚠ within organs, on part of the lines; also absent: FRZB, GALNT16, KLRG1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ALDH8A1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NEK10]] | B | NEK10 activity raises ALDH8A1's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 2.17× lower at baseline in the lines without NEK10 | 0.051 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[ZNF474]] | B | ZNF474 activity raises ALDH8A1's level | lines that do not express ZNF474 (6) vs lines expressing it (44) | 2.07× lower at baseline in the lines without ZNF474 | 0.070 | ⚠ within organs, on part of the lines; also absent: RBFOX1, NEK10, LINC01524; maybe low, not absent |
| [[AOX1]] | B | AOX1 activity raises ALDH8A1's level | lines that do not express AOX1 (17) vs lines expressing it (33) | 1.24× lower at baseline in the lines without AOX1 | 0.084 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[LINC01291]] | B | LINC01291 activity raises ALDH8A1's level | lines that do not express LINC01291 (10) vs lines expressing it (40) | 1.46× lower at baseline in the lines without LINC01291 | 0.097 | ⚠ within organs, on part of the lines; also absent: ANTXR2, ENSG00000230479, PROCR; maybe low, not absent |
| [[ITPR2-AS1]] | C | ITPR2-AS1 activity raises ALDH8A1's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 2.43× lower at baseline in the lines without ITPR2-AS1 | 0.029 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17 |
| [[MPP4]] | C | MPP4 activity raises ALDH8A1's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 2.41× lower at baseline in the lines without MPP4 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; its own permutation p |
| [[TRIM72]] | C | TRIM72 activity raises ALDH8A1's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 2.18× lower at baseline in the lines without TRIM72 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |
| [[LINC02133]] | C | LINC02133 activity raises ALDH8A1's level | lines that do not express LINC02133 (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without LINC02133 | 0.063 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LYG1, RBM44, TRIM72; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.915). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.1, -13.6); signed map (17.9, 8.6). **Vector** length 81.3, 15.3% of its response variance represented; |z| ≥ 3 in 1,327 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.4 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +14.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.4 | +4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.1 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +5.3 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.8 | -3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | +0.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.1 | -3.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | +3.9 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.2 | -2.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | aldehyde dehydrogenase 8 family member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.3 — chr6:134,917,393-134,950,115 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ALDH12 |
| Gene groups (HGNC) | Aldehyde dehydrogenases |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 3 pathways, smallest: RA biosynthesis pathway; Signaling by Retinoic Acid; Signaling by Nuclear Receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2A2](https://www.uniprot.org/uniprotkb/Q9H2A2) (2-aminomuconic semialdehyde dehydrogenase):

> Catalyzes the NAD-dependent oxidation of 2-aminomuconic semialdehyde of the kynurenine metabolic pathway in L-tryptophan degradation.

**Summary**, from NCBI Gene [64577](https://www.ncbi.nlm.nih.gov/gene/64577):

> This gene encodes a member of the aldehyde dehydrogenase family of proteins. The encoded protein has been implicated in the synthesis of 9-cis-retinoic acid and in the breakdown of the amino acid tryptophan. This enzyme converts 9-cis-retinal into the retinoid X receptor ligand 9-cis-retinoic acid, and has approximately 40-fold higher activity with 9-cis-retinal than with all-trans-retinal. In addition, this enzyme has been shown to catalyze the conversion of 2-aminomuconic semialdehyde to …

**Accessions** — [HGNC:15471](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15471) · Entrez [64577](https://www.ncbi.nlm.nih.gov/gene/64577) · UniProt [Q9H2A2](https://www.uniprot.org/uniprotkb/Q9H2A2) · Ensembl [ENSG00000118514](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118514)

## Data

Gene col 3999: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3999); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3999, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3999]; `tensor/DDL_lfc|DDL_z.npy` [3999]; `embed/gene_vectors.npy` [3999]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3999 or target_col == 3999). Every well: [[ALDH8A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDH8A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
