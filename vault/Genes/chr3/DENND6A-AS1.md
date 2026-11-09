---
symbol: "DENND6A-AS1"
type: "gene"
col: 14212
ensembl_id: "ENSG00000239801"
name: "DENND6A antisense RNA 1"
location: "3p14.3"
module: 26
arm: "+"
pooled_cpm: 3.2
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# DENND6A-AS1

*DENND6A antisense RNA 1* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.64× (z +27.1, q 0e+00, up in 38 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Econazole (drug)]] 0.05 µM in 1 line (RKO 0.0570×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA1]] (+0.83, fdr 7e-06), [[CIBAR1-DT]] (+0.81, fdr 7e-06), [[FAM184B]] (+0.81, fdr 7e-06).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14212.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.64×** | +27.1 | 0e+00 | 38/38 (LOX-IMVI, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.80×** | +14.2 | 2e-43 | 27/33 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.33×** | +13.8 | 4e-41 | 36/44 (SW480, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.74×** | +13.4 | 8e-39 | 31/36 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.33×** | +13.3 | 4e-38 | 28/36 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.17×** | +10.3 | 6e-23 | 28/46 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.74×** | +9.5 | 2e-19 | 25/37 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.13×** | +7.0 | 2e-10 | 5/5 (LoVo, J82, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +6.5 | 4e-09 | 9/19 (NCI-H2030, A498, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +5.9 | 2e-07 | 15/44 (NCI-H460, SHP-77, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +5.9 | 2e-07 | 3/4 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +5.4 | 3e-06 | 10/20 (NCI-H1573, LS 180, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.90×** | +5.3 | 7e-06 | 16/38 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +4.9 | 3e-05 | 4/7 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +4.3 | 6e-04 | 10/36 (RKO, LS 180, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +4.2 | 9e-04 | 11/43 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.003 | 13/46 (COLO 205, LS 180, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.22×** | +3.9 | 0.003 | 7/37 (LoVo, MIA PaCa-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.039 | 7/45 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.053 | 11/44 (HOP62, Hs 766T, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +3.1 | 0.054 | 9/41 (HEC-1-A, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14212.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Econazole (drug)]] 0.05 µM in 1 line (RKO 0.0570×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.864× | -4.9 | 7e-04 | 21/48 (A549, SW1417, …) | inconsistent across doses |  |
| [[Malotilate (drug)]] 0.5 µM |  | 0.711× | -3.2 | 0.35 | 10/43 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14212. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 6.79 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.38× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 3.43 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.4× (z +12.6) | — |
| [[HS-578T (line)]] | alt | 3.39 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.7× (z +12.6) | — |
| [[NCI-H460 (line)]] | wt | 3.07 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.86× (z +12.2) | — |
| [[SW480 (line)]] | alt | 3.90 | 2 | 0 | [[Auranofin (drug)]] 5 µM 7.95× (z +9.7) | — |
| [[A-172 (line)]] | wt | 2.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +11.0) | — |
| [[A498 (line)]] | wt | 2.01 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +11.3) | — |
| [[AsPC-1 (line)]] | alt | 2.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 33.2× (z +13.0) | — |
| [[C32 (line)]] | wt | 5.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.01× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 2.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +10.2) | — |
| [[HepG2_C3A (line)]] | wt | 2.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.3× (z +9.6) | — |
| [[LoVo (line)]] | wt | 3.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +12.7) | — |
| [[LOX-IMVI (line)]] | wt | 2.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.5× (z +13.8) | — |
| [[NCI-H2030 (line)]] | alt | 3.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.77× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 2.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.71× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 2.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 2.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.81× (z +10.0) | — |
| [[RKO (line)]] | wt | 4.17 | 0 | 1 | — | [[Econazole (drug)]] 0.05 µM 0.0570× (z -8.6) |
| [[SNU-423 (line)]] | alt | 2.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 2.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.5× (z +9.6) | — |
| [[A-427 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14212), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA1]] | +0.83 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[CIBAR1-DT]] | +0.81 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[FAM184B]] | +0.81 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[LANCL1-AS1]] | +0.80 | +0.70 / +0.76 | both halves | 7e-06 | same gene group |
| [[PSMD14-DT]] | +0.80 | +0.82 / +0.58 | both halves | 7e-06 |  |
| [[ZFHX2-AS1]] | +0.79 | +0.80 / +0.60 | both halves | 7e-06 | same gene group |
| [[SIAH2-AS1]] | +0.79 | +0.71 / +0.61 | both halves | 7e-06 | same gene group |
| [[COLEC11]] | +0.79 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[PAXBP1-AS1]] | +0.78 | +0.79 / +0.62 | both halves | 7e-06 | same gene group |
| [[PSMD7-DT]] | +0.78 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[DNAH10]] | +0.78 | +0.81 / +0.63 | both halves | 7e-06 |  |
| [[LINC01618]] | +0.78 | +0.77 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DENND6A-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MGC4859]] | B | MGC4859 activity raises DENND6A-AS1's level | lines that do not express MGC4859 (8) vs lines expressing it (42) | 1.23× lower at baseline in the lines without MGC4859 | 0.067 | ⚠ within organs, on part of the lines; also absent: LINC00922, LINC01811, LINC00276; maybe low, not absent |
| [[LINC01358]] | B | LINC01358 activity raises DENND6A-AS1's level | lines that do not express LINC01358 (14) vs lines expressing it (36) | 1.08× lower at baseline in the lines without LINC01358 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, BMPER, FRMD4A; maybe low, not absent |
| [[IGSF11]] | B | IGSF11 activity raises DENND6A-AS1's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.18× lower at baseline in the lines without IGSF11 | 0.090 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.814). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.9, 22.9); signed map (29.4, -0.2). **Vector** length 62.1, 9.19% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +27.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.9 | +13.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +14.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +10.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +13.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +3.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.3 | +3.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +0.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -0.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -2.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -0.9 | -1.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -0.9 | +0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | DENND6A antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p14.3 — chr3:57,628,810-57,654,918 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41152](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41152) · Entrez [106144528](https://www.ncbi.nlm.nih.gov/gene/106144528) · Ensembl [ENSG00000239801](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239801)

## Data

Gene col 14212: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14212); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14212, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14212]; `tensor/DDL_lfc|DDL_z.npy` [14212]; `embed/gene_vectors.npy` [14212]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14212 or target_col == 14212). Every well: [[DENND6A-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DENND6A-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
