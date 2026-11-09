---
symbol: "BTG3-AS1"
type: "gene"
col: 15961
ensembl_id: "ENSG00000280594"
name: "BTG3 antisense RNA 1"
location: "21q21.1"
module: 39
arm: "+"
pooled_cpm: 2.95
n_lines_expressing: 43
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 9
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# BTG3-AS1

*BTG3 antisense RNA 1* — 21q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.27× (z +18.2, q 0e+00, up in 23 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.568× (z -4.8, q 0.001, down in 9 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Pentagastrin (drug)]] 5 µM in 1 line (SW 1271 0.182×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0587×); [[Belinostat (drug)]] 5 µM in 1 line (LoVo 0.200×; ⚠ cell-cycle shift, explains ~72% of this change); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H460 0.0763×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02955]] (+0.79, fdr 7e-06), [[LINC01191]] (+0.79, fdr 7e-06), [[C3orf20]] (+0.77, fdr 7e-06); moves opposite to [[BRAT1]] (-0.71, fdr 3e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[NLGN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15961.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.27×** | +18.2 | 0e+00 | 23/26 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.13×** | +14.3 | 6e-44 | 18/29 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.85×** | +11.5 | 3e-28 | 14/23 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.72×** | +11.2 | 6e-27 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.29×** | +9.8 | 2e-20 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.00×** | +8.7 | 3e-16 | 13/38 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.64×** | +8.6 | 7e-16 | 13/26 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.74×** | +6.9 | 3e-10 | 16/37 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +6.7 | 1e-09 | 6/12 (HOP62, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.09×** | +6.5 | 4e-09 | 18/35 (HOP62, SW48, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +5.5 | 2e-06 | 11/26 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.74×** | +4.9 | 5e-05 | 11/39 (A-427, HepG2/C3A, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +3.8 | 0.005 | 10/33 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.007 | 7/37 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +3.7 | 0.008 | 6/36 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.45×** | +3.1 | 0.062 | 4/35 (BT-474, LS 180, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.062 | 2/35 (LOX-IMVI, MIA PaCa-2) | rises with dose | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15961.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Pentagastrin (drug)]] 5 µM in 1 line (SW 1271 0.182×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0587×); [[Belinostat (drug)]] 5 µM in 1 line (LoVo 0.200×; ⚠ cell-cycle shift, explains ~72% of this change); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H460 0.0763×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.568×** | -4.8 | 0.001 | 9/32 (LoVo, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.650×** | -3.8 | 0.034 | 10/39 (KATO III, NCI-H2030, …) | rises with dose | composition shift |
| [[Pemetrexed (drug)]] 5 µM |  | 0.677× | -3.4 | 0.15 | 12/25 (HT-29, SW48, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.685× | -3.2 | 0.21 | 3/26 (HEC-1-A, LoVo, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15961. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 15.3 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +13.1) | [[Belinostat (drug)]] 5 µM 0.200× (z -9.2) ⚠ cell-cycle shift, explains ~72% of this change |
| [[NCI-H460 (line)]] | wt | 2.44 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.51× (z +9.2) | [[Belumosudil (drug)]] 5 µM 0.0763× (z -8.6) |
| [[A-172 (line)]] | wt | 1.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.9× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0587× (z -9.2) |
| [[KATO III (line)]] | alt | 4.60 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0777× (z -8.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 1271 (line)]] | alt | 1.92 | 0 | 1 | — | [[Pentagastrin (drug)]] 5 µM 0.182× (z -13.2) |
| [[A-427 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.982 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.716 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.909 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.603 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.722 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.918 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.765 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15961), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02955]] | +0.79 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.79 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.77 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.76 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[USP50]] | +0.76 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.76 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[LINC00880]] | +0.76 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[LINC02542]] | +0.75 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[ALDH8A1]] | +0.75 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.75 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[NEB]] | +0.75 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[SLC2A9]] | +0.75 | +0.74 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRAT1]] | -0.71 | -0.66 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BTG3-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00857]] | B | LINC00857 activity raises BTG3-AS1's level | lines that do not express LINC00857 (17) vs lines expressing it (33) | 1.41× lower at baseline in the lines without LINC00857 | 0.067 | ⚠ within organs, on part of the lines; also absent: KRT18, C19orf33, OCLN |
| [[SPOCK2]] | B | SPOCK2 activity raises BTG3-AS1's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.77× lower at baseline in the lines without SPOCK2 | 0.096 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NLGN3]] | B | BTG3-AS1 activity raises NLGN3's level | lines that do not express BTG3-AS1 (7) vs lines expressing it (43) | 1.69× lower at baseline in the lines without BTG3-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: DUSP8, USP43, EFNA2; maybe low, not absent |
| [[GSK3B-DT]] | B | BTG3-AS1 activity raises GSK3B-DT's level | lines that do not express BTG3-AS1 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without BTG3-AS1 | 0.033 | ⚠ within organs, on part of the lines; also absent: DUSP8, USP43, EFNA2; maybe low, not absent |
| [[LINC02901]] | B | BTG3-AS1 activity raises LINC02901's level | lines that do not express BTG3-AS1 (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without BTG3-AS1 | 0.044 | ⚠ within organs, on part of the lines; also absent: DUSP8, USP43, EFNA2; maybe low, not absent |
| [[LINC00310]] | B | BTG3-AS1 activity lowers LINC00310's level | lines that do not express BTG3-AS1 (7) vs lines expressing it (43) | 2.85× higher at baseline in the lines without BTG3-AS1 | 0.066 | ⚠ within organs, on part of the lines; also absent: DUSP8, USP43, EFNA2; maybe low, not absent |
| [[KRTAP5-AS1]] | B | BTG3-AS1 activity raises KRTAP5-AS1's level | lines that do not express BTG3-AS1 (7) vs lines expressing it (43) | 2.28× lower at baseline in the lines without BTG3-AS1 | 0.071 | ⚠ within organs, on part of the lines; also absent: DUSP8, USP43, EFNA2; maybe low, not absent |
| [[LINC01393]] | B | BTG3-AS1 activity lowers LINC01393's level | lines that do not express BTG3-AS1 (7) vs lines expressing it (43) | 1.91× higher at baseline in the lines without BTG3-AS1 | 0.075 | ⚠ within organs, on part of the lines; also absent: DUSP8, USP43, EFNA2; maybe low, not absent |
| [[CKLF]] | B | BTG3-AS1 activity strengthens CKLF's drug response | lines that do not express BTG3-AS1 (7) vs lines expressing it (41) | the lines without BTG3-AS1 respond 0.85× as strongly (z diff +0.66); strongest at Idarubicin (hydrochloride) 5 µM: 0.77x vs 0.56x (z diff +2.5) | 0.086 | ⚠ within organs, on part of the lines; also absent: DUSP8, USP43, EFNA2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TRIM59]] | B | BTG3-AS1 activity raises TRIM59's level | lines that do not express BTG3-AS1 (7) vs lines expressing it (43) | 1.79× lower at baseline in the lines without BTG3-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: DUSP8, USP43, EFNA2; maybe low, not absent |
| [[C5AR1]] | B | BTG3-AS1 activity raises C5AR1's level | lines that do not express BTG3-AS1 (7) vs lines expressing it (43) | 1.22× lower at baseline in the lines without BTG3-AS1 | 0.098 | ⚠ within organs, on part of the lines; also absent: DUSP8, USP43, EFNA2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.800). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.2, -12.2); signed map (20.1, 5.2). **Vector** length 58.9, 8.82% of its response variance represented; |z| ≥ 3 in 1,105 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +14.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +18.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +11.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +6.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | -0.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -2.8 | -1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -2.7 | -1.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | -1.9 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.7 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | BTG3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 21q21.1 — chr21:17,611,696-17,633,943 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ASBEL |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53145](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53145) · Entrez [110806272](https://www.ncbi.nlm.nih.gov/gene/110806272) · Ensembl [ENSG00000280594](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000280594)

## Data

Gene col 15961: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15961); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15961, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15961]; `tensor/DDL_lfc|DDL_z.npy` [15961]; `embed/gene_vectors.npy` [15961]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15961 or target_col == 15961). Every well: [[BTG3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTG3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
