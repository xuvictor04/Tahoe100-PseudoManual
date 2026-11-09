---
symbol: "DRAIC"
type: "gene"
col: 14443
ensembl_id: "ENSG00000245750"
name: "downregulated RNA in cancer, inhibitor of cell invasion and migration"
location: "15q23"
module: 26
arm: "+"
pooled_cpm: 6.81
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 3
n_dd_up_clean: 24
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# DRAIC

*downregulated RNA in cancer, inhibitor of cell invasion and migration* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.66× (z +24.9, q 0e+00, up in 35 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.680× (z -4.1, q 0.020, down in 16 of 43 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEB]] (+0.78, fdr 7e-06), [[UNC79]] (+0.77, fdr 1e-05), [[TMEM202-AS1]] (+0.76, fdr 1e-05); moves opposite to [[LCMT1]] (-0.65, fdr 6e-05), [[WRAP73]] (-0.64, fdr 1e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[RIMS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14443.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.66×** | +24.9 | 0e+00 | 35/38 (C32, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.54×** | +24.5 | 0e+00 | 37/38 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.56×** | +17.4 | 0e+00 | 38/44 (SW480, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.98×** | +11.6 | 8e-29 | 9/16 (NCI-H1573, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.54×** | +10.7 | 2e-24 | 17/23 (NCI-H1573, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +10.2 | 1e-22 | 8/11 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +9.5 | 3e-19 | 25/36 (A498, SNU-423, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +8.2 | 1e-14 | 22/40 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.65×** | +8.1 | 3e-14 | 21/45 (SW480, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.94×** | +7.6 | 1e-12 | 16/37 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.94×** | +7.6 | 1e-12 | 24/44 (SK-MEL-2, A-427, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.86×** | +6.9 | 3e-10 | 21/43 (C32, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +5.9 | 2e-07 | 17/46 (A498, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.26×** | +4.9 | 4e-05 | 4/13 (NCI-H2030, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +4.8 | 7e-05 | 11/44 (PANC-1, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +4.6 | 2e-04 | 7/45 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.002 | 15/45 (BT-474, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +4.0 | 0.002 | 13/44 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.88×** | +3.8 | 0.004 | 6/44 (C-33 A, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14443.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.680×** | -4.1 | 0.020 | 16/43 (SW480, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.780×** | -4.0 | 0.020 | 15/44 (HOP62, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.734×** | -3.5 | 0.090 | 9/46 (NCI-H2030, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14443. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 5.36 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 104× (z +20.9) | — |
| [[HOP62 (line)]] | alt | 6.62 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +10.4) | — |
| [[SW480 (line)]] | alt | 15.0 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.62× (z +11.7) | [[Digitoxin (drug)]] 5 µM 0.205× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.220× (z -8.9) |
| [[A498 (line)]] | wt | 5.02 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +15.1) | — |
| [[LoVo (line)]] | wt | 4.46 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +16.3) | — |
| [[LOX-IMVI (line)]] | wt | 4.10 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.5× (z +13.4) | — |
| [[NCI-H23 (line)]] | alt | 8.73 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +11.1) | — |
| [[NCI-H460 (line)]] | wt | 4.91 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.70× (z +13.3) | — |
| [[PANC-1 (line)]] | alt | 6.79 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 6.04 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +11.6) | — |
| [[A549 (line)]] | wt | 5.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.62× (z +9.1) | — |
| [[COLO 205 (line)]] | alt | 7.01 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0485× (z -9.5) ⚠ cell-cycle shift, explains ~6% of this change |
| [[HCT15 (line)]] | alt | 4.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 9.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 2.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.27× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 3.31 | 1 | 0 | [[Auranofin (drug)]] 5 µM 23.8× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 2.91 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.8× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 8.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 4.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.05× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 16.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 2.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.01× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 5.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.36× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 41.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.224× (z -8.5) |
| [[SNU-423 (line)]] | alt | 4.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +10.8) | — |
| [[SW48 (line)]] | wt | 5.54 | 1 | 0 | [[Auranofin (drug)]] 5 µM 38.7× (z +8.5) | — |
| [[A-172 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14443), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEB]] | +0.78 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[UNC79]] | +0.77 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[TMEM202-AS1]] | +0.76 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[CIBAR1-DT]] | +0.76 | +0.80 / +0.48 | both halves | 2e-05 |  |
| [[PSMD7-DT]] | +0.75 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[PKN2-AS1]] | +0.75 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[FBXO38-DT]] | +0.74 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | +0.74 | +0.75 / +0.44 | both halves | 3e-05 |  |
| [[LEKR1]] | +0.72 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[DNAH12]] | +0.72 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[CCDC90B-AS1]] | +0.72 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[INTS6-AS1]] | +0.72 | +0.70 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCMT1]] | -0.65 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[WRAP73]] | -0.64 | -0.51 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIMS2]] | B | RIMS2 activity raises DRAIC's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 1.69× lower at baseline in the lines without RIMS2 | 0.013 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3 |
| [[TOP2A]] | B | TOP2A activity lowers DRAIC's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ID2-AS1]] | B | ID2-AS1 activity raises DRAIC's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.77× lower at baseline in the lines without ID2-AS1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[KATNAL2]] | B | KATNAL2 activity raises DRAIC's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.72× lower at baseline in the lines without KATNAL2 | 0.065 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[NPAS3]] | B | NPAS3 activity raises DRAIC's level | lines that do not express NPAS3 (16) vs lines expressing it (34) | 1.62× lower at baseline in the lines without NPAS3 | 0.073 | ⚠ within organs, on part of the lines; also absent: SLC2A14, MARK1, CAMK4; maybe low, not absent |
| [[CRB1]] | B | CRB1 activity raises DRAIC's level | lines that do not express CRB1 (6) vs lines expressing it (44) | 1.99× lower at baseline in the lines without CRB1 | 0.089 | ⚠ within organs, on part of the lines; also absent: DNAI1, RBFOX1, RHBDL3; maybe low, not absent |
| [[H2AZ1-DT]] | C | H2AZ1-DT's natural level strengthens DRAIC's drug response | H2AZ1-DT's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.05; direction not clear | 0.071 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.795). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.9, 17.8); signed map (28.3, -4.9). **Vector** length 77.3, 13.8% of its response variance represented; |z| ≥ 3 in 1,139 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.4 | +17.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +24.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.7 | +24.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.2 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +4.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +2.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.7 | +5.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -4.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | downregulated RNA in cancer, inhibitor of cell invasion and migration |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q23 — chr15:69,462,921-69,843,120 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27082](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27082) · Entrez [145837](https://www.ncbi.nlm.nih.gov/gene/145837) · Ensembl [ENSG00000245750](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245750)

## Data

Gene col 14443: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14443); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14443, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14443]; `tensor/DDL_lfc|DDL_z.npy` [14443]; `embed/gene_vectors.npy` [14443]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14443 or target_col == 14443). Every well: [[DRAIC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DRAIC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
