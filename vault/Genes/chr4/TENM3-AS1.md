---
symbol: "TENM3-AS1"
type: "gene"
col: 10866
ensembl_id: "ENSG00000177822"
name: "TENM3 antisense RNA 1"
location: "4q34.3"
module: 202
arm: "+"
pooled_cpm: 5.05
n_lines_expressing: 31
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 12
direction_downstream: 12
tags: ["gene", "module/202"]
generated_by: "tahoemap"
---

# TENM3-AS1

*TENM3 antisense RNA 1* — 4q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.61× (z +23.4, q 0e+00, up in 21 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (C-33 A 0.102×; ⚠ cell-cycle shift, explains ~0% of this change); [[Oxaprozin (drug)]] 0.5 µM in 1 line (H4 0.0540×); [[Bestatin (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-423 0.0564×); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (LS 180 0.0594×).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TENM3]] (+0.77, fdr 7e-06, ⚠ same locus), [[CACNA2D1]] (+0.72, fdr 4e-05), [[CYP1B1-AS1]] (+0.69, fdr 1e-05), [[ARHGAP15]] (+0.68, fdr 3e-05); moves opposite to [[LCMT1]] (-0.67, fdr 3e-05), [[DPY30]] (-0.66, fdr 3e-05), [[NBPF3]] (-0.65, fdr 1e-04).
> It is in [[Module 202]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[MIR99AHG]] → it (grade B ⚠); 12 go from it, the strongest it → [[FBN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10866.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.61×** | +23.4 | 0e+00 | 21/24 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.33×** | +18.5 | 0e+00 | 22/26 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.19×** | +12.1 | 2e-31 | 7/8 (NCI-H460, J82, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.31×** | +12.0 | 4e-31 | 5/9 (HS-578T, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.60×** | +10.4 | 4e-23 | 20/27 (HOP62, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.52×** | +10.0 | 1e-21 | 6/16 (SNU-423, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.29×** | +9.0 | 2e-17 | 21/25 (HOP62, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.23×** | +8.4 | 5e-15 | 21/26 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.71×** | +8.2 | 1e-14 | 14/27 (HOP62, J82, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.8 | 1e-04 | 9/21 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +4.6 | 3e-04 | 7/27 (C32, SNU-423, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +4.4 | 4e-04 | 8/26 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.2 | 0.001 | 9/25 (HOP62, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +4.1 | 0.001 | 4/22 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.0 | 0.003 | 6/19 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.021 | 3/21 (HT-29, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.055 | 9/26 (A-427, hTERT-HPNE, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.089 | 3/28 (HOP62, HCT15, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10866.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (C-33 A 0.102×; ⚠ cell-cycle shift, explains ~0% of this change); [[Oxaprozin (drug)]] 0.5 µM in 1 line (H4 0.0540×); [[Bestatin (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-423 0.0564×); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (LS 180 0.0594×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | 0.710× | -3.7 | 0.10 | 12/27 (NCI-H460, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10866. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 6.79 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.9× (z +20.2) | — |
| [[HS-578T (line)]] | alt | 4.74 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.75× (z +11.4) | [[Ixazomib citrate (drug)]] 5 µM 0.0778× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 2.65 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.64× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 4.95 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.67× (z +9.7) | [[Bestatin (hydrochloride) (drug)]] 0.05 µM 0.0564× (z -9.8) |
| [[A-172 (line)]] | wt | 18.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -8.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 18.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.200× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +9.4) | — |
| [[C-33 A (line)]] | alt | 49.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.102× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 13.0 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0540× (z -10.3) |
| [[HCT15 (line)]] | alt | 9.41 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +11.8) | — |
| [[J82 (line)]] | alt | 10.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +13.3) | — |
| [[LS 180 (line)]] | wt | 3.94 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0594× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 4.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +11.6) | — |
| [[SW480 (line)]] | alt | 2.81 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.211× (z -9.4) ⚠ cell-cycle shift, explains ~5% of this change |
| [[A549 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.812 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.865 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.958 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.831 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.759 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.894 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.879 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.741 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.930 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.808 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10866), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 20 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TENM3]] | +0.77 | +0.83 / +0.66 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CACNA2D1]] | +0.72 | +0.67 / +0.41 | both halves | 4e-05 |  |
| [[CYP1B1-AS1]] | +0.69 | +0.69 / +0.49 | both halves | 1e-05 | same gene group |
| [[ARHGAP15]] | +0.68 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[CFAP54]] | +0.68 | +0.67 / +0.40 | both halves | 4e-05 |  |
| [[CCDC90B-AS1]] | +0.68 | +0.65 / +0.35 | both halves | 1e-04 | same gene group |
| [[AKT1S1]] | +0.68 | +0.60 / +0.38 | both halves | 7e-05 |  |
| [[GUCY1A2]] | +0.67 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[GALNT7-DT]] | +0.67 | +0.67 / +0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[ANKRD18B]] | +0.67 | +0.63 / +0.27 | both halves | 3e-04 |  |
| [[PCNX4-DT]] | +0.66 | +0.67 / +0.23 | both halves | 5e-04 |  |
| [[MZF1-AS1]] | +0.66 | +0.64 / +0.38 | both halves | 7e-05 | same gene group |
| [[STARD4-AS1]] | +0.65 | +0.59 / +0.39 | both halves | 5e-05 | same gene group |
| [[SYNPO2]] | +0.65 | +0.62 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCMT1]] | -0.67 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[DPY30]] | -0.66 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[NBPF3]] | -0.65 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[HEATR5B]] | -0.63 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[BRAT1]] | -0.62 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[SHQ1]] | -0.62 | -0.61 / -0.35 | both halves | 1e-04 |  |
| [[GTPBP3]] | -0.60 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[ELP1]] | -0.59 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[MTMR12]] | -0.59 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[TAF5L]] | -0.58 | -0.63 / -0.25 | both halves | 4e-04 |  |
| [[UNC45A]] | -0.58 | -0.49 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 9, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR99AHG]] | B | MIR99AHG activity raises TENM3-AS1's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 3.32× lower at baseline in the lines without MIR99AHG | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099 |
| [[FBN2]] | B | FBN2 activity raises TENM3-AS1's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 2.01× lower at baseline in the lines without FBN2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers TENM3-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DPY19L2]] | B | DPY19L2 activity raises TENM3-AS1's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 1.84× lower at baseline in the lines without DPY19L2 | 0.040 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ |
| [[ZFY]] | B | ZFY activity raises TENM3-AS1's level | lines that do not express ZFY (29) vs lines expressing it (21) | 1.82× lower at baseline in the lines without ZFY | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PRKY, RPS4Y1, LINC00278 |
| [[LINC00882]] | B | LINC00882 activity raises TENM3-AS1's level | lines that do not express LINC00882 (17) vs lines expressing it (33) | 2.01× lower at baseline in the lines without LINC00882 | 0.073 | ⚠ within organs, on part of the lines; also absent: TUSC3, B3GALT1, EVC |
| [[ANKRD18B]] | B | ANKRD18B activity raises TENM3-AS1's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.59× lower at baseline in the lines without ANKRD18B | 0.080 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[LINC02240]] | B | LINC02240 activity raises TENM3-AS1's level | lines that do not express LINC02240 (35) vs lines expressing it (15) | 1.68× lower at baseline in the lines without LINC02240 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02941, CHL1, EDNRB; maybe low, not absent |
| [[PSG4]] | B | PSG4 activity raises TENM3-AS1's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 1.66× lower at baseline in the lines without PSG4 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5 |
| [[TENM3]] | C | TENM3 activity raises TENM3-AS1's level | lines that do not express TENM3 (20) vs lines expressing it (30) | 3.76× lower at baseline in the lines without TENM3 | 3e-04 | ⚠ within organs, on part of the lines; also absent: TENM3-AS1, ZEB2, SRPX; co-absent with the target |
| [[TRIML2]] | C | TRIML2 activity raises TENM3-AS1's level | lines that do not express TRIML2 (30) vs lines expressing it (20) | 2.44× lower at baseline in the lines without TRIML2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ZNF471, LINC01010, ENSG00000222032; co-absent with the target |
| [[ANKRD30B]] | C | ANKRD30B activity raises TENM3-AS1's level | lines that do not express ANKRD30B (35) vs lines expressing it (15) | 1.95× lower at baseline in the lines without ANKRD30B | 0.094 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMPH, GYPC, GDNF; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBN2]] | B | TENM3-AS1 activity raises FBN2's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 2.38× lower at baseline in the lines without TENM3-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent |
| [[NLGN4Y]] | B | TENM3-AS1 activity raises NLGN4Y's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 2.31× lower at baseline in the lines without TENM3-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent |
| [[PYGO1]] | B | TENM3-AS1 activity raises PYGO1's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 2.16× lower at baseline in the lines without TENM3-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent |
| [[FGF2]] | B | TENM3-AS1 activity raises FGF2's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 2.58× lower at baseline in the lines without TENM3-AS1 | 0.046 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent |
| [[SOCS2-AS1]] | B | TENM3-AS1 activity raises SOCS2-AS1's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 1.65× lower at baseline in the lines without TENM3-AS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent |
| [[UNC45A]] | B | TENM3-AS1 activity weakens UNC45A's drug response | lines that do not express TENM3-AS1 (19) vs lines expressing it (29) | the lines without TENM3-AS1 respond 1.16× as strongly (z diff -0.37); strongest at Panobinostat 5 µM: 2.08x vs 1.65x (z diff -1.4) | 0.080 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[UHRF2]] | B | TENM3-AS1 activity raises UHRF2's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 1.17× lower at baseline in the lines without TENM3-AS1 | 0.081 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent |
| [[EPHA5]] | B | TENM3-AS1 activity raises EPHA5's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 2.44× lower at baseline in the lines without TENM3-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent |
| [[TENM3]] | C | TENM3-AS1 activity raises TENM3's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 10.02× lower at baseline in the lines without TENM3-AS1 | 4e-05 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent; co-absent with the target |
| [[TRIML2]] | C | TENM3-AS1 activity raises TRIML2's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 2.14× lower at baseline in the lines without TENM3-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent; co-absent with the target |
| [[ANKRD30B]] | C | TENM3-AS1 activity raises ANKRD30B's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 2.26× lower at baseline in the lines without TENM3-AS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent; co-absent with the target |
| [[ALPK2]] | C | TENM3-AS1 activity raises ALPK2's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 2.93× lower at baseline in the lines without TENM3-AS1 | 0.081 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 202]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.826). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.2, 24.2); signed map (44.4, 24.4). **Vector** length 62.3, 13.1% of its response variance represented; |z| ≥ 3 in 697 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +23.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +18.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +12.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +12.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +3.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.1 | -3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.1 | -1.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.8 | -0.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -0.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -2.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | +0.2 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | TENM3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q34.3 — chr4:181,874,438-182,145,249 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously TENM3-AS2 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28076](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28076) · Entrez [90768](https://www.ncbi.nlm.nih.gov/gene/90768) · Ensembl [ENSG00000177822](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177822)

## Data

Gene col 10866: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10866); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10866, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10866]; `tensor/DDL_lfc|DDL_z.npy` [10866]; `embed/gene_vectors.npy` [10866]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10866 or target_col == 10866). Every well: [[TENM3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TENM3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
