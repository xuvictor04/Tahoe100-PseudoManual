---
symbol: "ST8SIA5"
type: "gene"
col: 2160
ensembl_id: "ENSG00000101638"
name: "ST8 alpha-N-acetyl-neuraminide alpha-2,8-sialyltransferase 5"
location: "18q21.1"
module: 26
arm: "+"
pooled_cpm: 2.46
n_lines_expressing: 45
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 17
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# ST8SIA5

*ST8 alpha-N-acetyl-neuraminide alpha-2,8-sialyltransferase 5* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.94× (z +14.2, q 5e-43, up in 27 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-423 0.0824×; ⚠ toxic; transcription drop); [[Dorzolamide (hydrochloride) (drug)]] 5 µM in 1 line (C-33 A 0.0564×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEB]] (+0.85, fdr 7e-06), [[PSMD7-DT]] (+0.80, fdr 7e-06), [[SLC26A7]] (+0.80, fdr 7e-06).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 17 go from it, the strongest it → [[LRRC39]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2160.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.94×** | +14.2 | 5e-43 | 27/30 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.75×** | +13.7 | 3e-40 | 22/30 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.04×** | +9.8 | 1e-20 | 22/26 (MIA PaCa-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.91×** | +9.6 | 1e-19 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.58×** | +9.4 | 1e-18 | 26/35 (A-427, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.51×** | +9.2 | 3e-18 | 18/26 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.62×** | +9.1 | 1e-17 | 26/31 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.02×** | +7.5 | 5e-12 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.72×** | +5.6 | 1e-06 | 11/41 (HS-578T, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.04×** | +5.2 | 9e-06 | 2/9 (HS-578T, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.61×** | +5.0 | 4e-05 | 6/41 (J82, LoVo, …) | top dose only | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **2.01×** | +4.9 | 4e-05 | 14/31 (LoVo, C32, …) | rises with dose | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **2.49×** | +3.5 | 0.021 | 1/23 (PANC-1) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.55×** | +3.2 | 0.050 | 9/37 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.079 | 8/40 (LoVo, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.54×** | +3.0 | 0.093 | 6/35 (A-427, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2160.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-423 0.0824×; ⚠ toxic; transcription drop); [[Dorzolamide (hydrochloride) (drug)]] 5 µM in 1 line (C-33 A 0.0564×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | 0.383× | -3.7 | 0.14 | 9/22 (HepG2/C3A, J82, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.654× | -3.1 | 0.54 | 6/42 (PANC-1, NCI-H661, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2160. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 3.46 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 18.5× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 12.5 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 5 µM 0.0564× (z -8.7) |
| [[LoVo (line)]] | wt | 2.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 1.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.1× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 1.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.7× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 8.19 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0824× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.910 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.399 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.988 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.625 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.954 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.616 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2160), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEB]] | +0.85 | +0.83 / +0.74 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.80 | +0.83 / +0.62 | both halves | 7e-06 |  |
| [[SLC26A7]] | +0.80 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[CCDC90B-AS1]] | +0.79 | +0.81 / +0.57 | both halves | 1e-05 |  |
| [[CFAP70]] | +0.79 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[PKD1L1]] | +0.79 | +0.81 / +0.68 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.79 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.78 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[MGAM]] | +0.78 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.78 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[INTS6-AS1]] | +0.77 | +0.78 / +0.61 | both halves | 7e-06 |  |
| [[LINC02955]] | +0.77 | +0.81 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ST8SIA5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF382]] | B | ZNF382 activity raises ST8SIA5's level | lines that do not express ZNF382 (18) vs lines expressing it (32) | 1.85× lower at baseline in the lines without ZNF382 | 0.024 | ⚠ within organs, on part of the lines; also absent: AFF3, DZIP1, MMP16 |
| [[PYROXD2]] | B | PYROXD2 activity lowers ST8SIA5's level | lines that do not express PYROXD2 (7) vs lines expressing it (43) | 1.79× higher at baseline in the lines without PYROXD2 | 0.042 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises ST8SIA5's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.60× lower at baseline in the lines without FSIP2-AS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[LINC01239]] | B | LINC01239 activity lowers ST8SIA5's level | lines that do not express LINC01239 (19) vs lines expressing it (31) | 1.51× higher at baseline in the lines without LINC01239 | 0.086 | ⚠ within organs, on part of the lines; also absent: DMRTA1, ZFPM2-AS1, MIR4500HG |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC39]] | B | ST8SIA5 activity raises LRRC39's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.69× lower at baseline in the lines without ST8SIA5 | 0.028 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[CFAP70]] | B | ST8SIA5 activity raises CFAP70's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 2.11× lower at baseline in the lines without ST8SIA5 | 0.034 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[EFCAB10]] | B | ST8SIA5 activity raises EFCAB10's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.30× lower at baseline in the lines without ST8SIA5 | 0.040 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[LINC01618]] | B | ST8SIA5 activity raises LINC01618's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.47× lower at baseline in the lines without ST8SIA5 | 0.046 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[USP38-DT]] | B | ST8SIA5 activity raises USP38-DT's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.39× lower at baseline in the lines without ST8SIA5 | 0.047 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[YIPF7]] | B | ST8SIA5 activity raises YIPF7's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.71× lower at baseline in the lines without ST8SIA5 | 0.050 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[CFAP53]] | B | ST8SIA5 activity raises CFAP53's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.65× lower at baseline in the lines without ST8SIA5 | 0.060 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[SLC26A7]] | B | ST8SIA5 activity raises SLC26A7's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.93× lower at baseline in the lines without ST8SIA5 | 0.066 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[LINC00240]] | B | ST8SIA5 activity raises LINC00240's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.50× lower at baseline in the lines without ST8SIA5 | 0.067 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[CCDC13]] | B | ST8SIA5 activity raises CCDC13's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.63× lower at baseline in the lines without ST8SIA5 | 0.078 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[CMYA5]] | B | ST8SIA5 activity raises CMYA5's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 2.08× lower at baseline in the lines without ST8SIA5 | 0.078 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[GLIPR1-AS1]] | B | ST8SIA5 activity raises GLIPR1-AS1's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.54× lower at baseline in the lines without ST8SIA5 | 0.079 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.885). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (12.1, 16.5); signed map (23.0, 0.4). **Vector** length 59.5, 8.92% of its response variance represented; |z| ≥ 3 in 1,031 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.7 | +9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +13.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +14.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +5.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +4.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.3 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | ST8 alpha-N-acetyl-neuraminide alpha-2,8-sialyltransferase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:46,667,821-46,759,257 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SIAT8E |
| Gene groups (HGNC) | Sialyltransferases |
| Reactome | 8 pathways, smallest: Glycosphingolipid biosynthesis; Sialic acid metabolism; Glycosphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O15466](https://www.uniprot.org/uniprotkb/O15466) (Alpha-2,8-sialyltransferase 8E):

> Involved in the synthesis of gangliosides GD1c, GT1a, GQ1b, GP1c and GT3 from GD1a, GT1b, GM1b and GD3 respectively.

**Summary**, from NCBI Gene [29906](https://www.ncbi.nlm.nih.gov/gene/29906):

> The protein encoded by this gene is a type II membrane protein that may be present in the Golgi apparatus. The encoded protein, which is a member of glycosyltransferase family 29, may be involved in the synthesis of gangliosides GD1c, GT1a, GQ1b, and GT3 from GD1a, GT1b, GM1b, and GD3, respectively. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17827](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17827) · Entrez [29906](https://www.ncbi.nlm.nih.gov/gene/29906) · UniProt [O15466](https://www.uniprot.org/uniprotkb/O15466) · Ensembl [ENSG00000101638](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101638)

## Data

Gene col 2160: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2160); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2160, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2160]; `tensor/DDL_lfc|DDL_z.npy` [2160]; `embed/gene_vectors.npy` [2160]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2160 or target_col == 2160). Every well: [[ST8SIA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST8SIA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
