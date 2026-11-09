---
symbol: "ZNF385D"
type: "gene"
col: 7566
ensembl_id: "ENSG00000151789"
name: "zinc finger protein 385D"
location: "3p24.3"
module: 13
arm: "+"
pooled_cpm: 12.78
n_lines_expressing: 25
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 32
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# ZNF385D

*zinc finger protein 385D* — 3p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.39× (z +24.8, q 0e+00, up in 10 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.323×, PANC-1 0.311×); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H1792 0.171×; ⚠ cell-cycle shift, explains ~22% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (HS-578T 0.0874×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NTNG2]] (+0.69, fdr 7e-06), [[PECAM1]] (+0.64, fdr 7e-06), [[ABCA13]] (+0.63, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 32 go from it, the strongest it → [[ZNF697]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7566.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.39×** | +24.8 | 0e+00 | 10/20 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.44×** | +14.9 | 0e+00 | 12/21 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.30×** | +13.9 | 7e-42 | 15/22 (SW480, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.05×** | +13.2 | 2e-37 | 12/20 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +11.0 | 3e-26 | 5/18 (SW480, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +10.0 | 1e-21 | 2/11 (A498, NCI-H2030) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.45×** | +9.8 | 8e-21 | 2/11 (NCI-H2030, A498) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +8.1 | 4e-14 | 5/19 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.77×** | +6.5 | 6e-09 | 5/21 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +6.1 | 8e-08 | 13/20 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +5.0 | 3e-05 | 9/21 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.5 | 3e-04 | 4/18 (LOX-IMVI, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.001 | 3/22 (A498, SK-MEL-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.009 | 4/21 (A-172, SW 900, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +3.6 | 0.012 | 2/18 (SW480, A-172) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.32×** | +3.2 | 0.042 | 2/21 (C32, NCI-H1792) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.43×** | +3.0 | 0.085 | 3/20 (C32, SHP-77, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7566.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.323×, PANC-1 0.311×); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H1792 0.171×; ⚠ cell-cycle shift, explains ~22% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (HS-578T 0.0874×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.735× | -3.7 | 0.14 | 6/21 (SW1417, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7566. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.58 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 18.5× (z +11.0) | — |
| [[NCI-H1792 (line)]] | alt | 168 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -10.8) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.323× (z -9.8) |
| [[SW480 (line)]] | alt | 3.81 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.75× (z +11.9) | — |
| [[A-172 (line)]] | wt | 7.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.25× (z +11.9) | — |
| [[HS-578T (line)]] | alt | 33.7 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0874× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 3.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.58× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 33.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.2) |
| [[A-427 (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.76 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7566), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTNG2]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[PECAM1]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[ABCA13]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[HTR7]] | +0.63 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[CNIH3]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[PLXNA4]] | +0.61 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[ASIC2]] | +0.59 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[LINC02813]] | +0.59 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[SALL1]] | +0.58 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[AFF2]] | +0.58 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[APCDD1L-DT]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[FRMD4A]] | +0.57 | +0.57 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZNF385D's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOX]] | C | TOX activity raises ZNF385D's level | lines that do not express TOX (30) vs lines expressing it (20) | 2.63× lower at baseline in the lines without TOX | 0.008 | ⚠ within organs, on part of the lines; also absent: CDH6, DKK3, MXRA5; co-absent with the target |
| [[LAMA4]] | C | LAMA4 activity raises ZNF385D's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 2.55× lower at baseline in the lines without LAMA4 | 0.027 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC; co-absent with the target |
| [[MIR3681HG]] | C | MIR3681HG activity raises ZNF385D's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 2.91× lower at baseline in the lines without MIR3681HG | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent; co-absent with the target |
| [[NRG1]] | C | NRG1 activity raises ZNF385D's level | lines that do not express NRG1 (19) vs lines expressing it (31) | 2.82× lower at baseline in the lines without NRG1 | 0.056 | ⚠ within organs, on part of the lines; also absent: TRIM9, DOCK2, ADAM23; co-absent with the target |
| [[CTHRC1]] | C | CTHRC1 activity raises ZNF385D's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 3.28× lower at baseline in the lines without CTHRC1 | 0.064 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent; co-absent with the target |
| [[PRRX1]] | C | PRRX1 activity raises ZNF385D's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 2.54× lower at baseline in the lines without PRRX1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |

### Downstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 10, C 22. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF697]] | B | ZNF385D activity raises ZNF697's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 2.18× lower at baseline in the lines without ZNF385D | 0.007 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent |
| [[DPY19L2P2]] | B | ZNF385D activity raises DPY19L2P2's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 1.83× lower at baseline in the lines without ZNF385D | 0.021 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent |
| [[ABCA13]] | B | ZNF385D activity raises ABCA13's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 2.21× lower at baseline in the lines without ZNF385D | 0.024 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent |
| [[PECAM1]] | B | ZNF385D activity raises PECAM1's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 1.89× lower at baseline in the lines without ZNF385D | 0.062 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent |
| [[EVA1A]] | B | ZNF385D activity raises EVA1A's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 2.88× lower at baseline in the lines without ZNF385D | 0.075 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent |
| [[CNIH3]] | B | ZNF385D activity raises CNIH3's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 2.58× lower at baseline in the lines without ZNF385D | 0.078 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent |
| [[ATP13A3-DT]] | B | ZNF385D activity raises ATP13A3-DT's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 1.58× lower at baseline in the lines without ZNF385D | 0.084 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent |
| [[CALCRL]] | B | ZNF385D activity raises CALCRL's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 2.09× lower at baseline in the lines without ZNF385D | 0.089 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent |
| [[MTSS1]] | B | ZNF385D activity raises MTSS1's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 2.30× lower at baseline in the lines without ZNF385D | 0.091 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent |
| [[PCDHGA2]] | B | ZNF385D activity raises PCDHGA2's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 2.29× lower at baseline in the lines without ZNF385D | 0.094 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent |
| [[FRMD4A]] | C | ZNF385D activity raises FRMD4A's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 4.99× lower at baseline in the lines without ZNF385D | 0.017 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |
| [[PRRX1]] | C | ZNF385D activity raises PRRX1's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 4.68× lower at baseline in the lines without ZNF385D | 0.023 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.580). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.5, 9.1); signed map (11.6, 50.4). **Vector** length 54.0, 12.2% of its response variance represented; |z| ≥ 3 in 567 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +11.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +13.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +0.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -2.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -0.9 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 385D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.3 — chr3:21,412,218-22,373,321 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22419; previously ZNF659 |
| Gene groups (HGNC) | Zinc fingers matrin-type |
| Matched by | ensembl_id |

UniProt [Q9H6B1](https://www.uniprot.org/uniprotkb/Q9H6B1) carries no function annotation.

**Summary**, from NCBI Gene [79750](https://www.ncbi.nlm.nih.gov/gene/79750):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26191](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26191) · Entrez [79750](https://www.ncbi.nlm.nih.gov/gene/79750) · UniProt [Q9H6B1](https://www.uniprot.org/uniprotkb/Q9H6B1) · Ensembl [ENSG00000151789](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151789)

## Data

Gene col 7566: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7566); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7566, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7566]; `tensor/DDL_lfc|DDL_z.npy` [7566]; `embed/gene_vectors.npy` [7566]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7566 or target_col == 7566). Every well: [[ZNF385D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF385D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
