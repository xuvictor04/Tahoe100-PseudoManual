---
symbol: "NPTX2"
type: "gene"
col: 2730
ensembl_id: "ENSG00000106236"
name: "neuronal pentraxin 2"
location: "7q22.1"
module: 165
arm: "+"
pooled_cpm: 2.49
n_lines_expressing: 22
n_dd_up: 40
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# NPTX2

*neuronal pentraxin 2* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (21 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.25× (z +16.9, q 0e+00, up in 15 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DISP3]] (+0.63, fdr 7e-06), [[ARC]] (+0.59, fdr 1e-05), [[CHST8]] (+0.57, fdr 5e-05); moves opposite to [[ZNF624]] (-0.51, fdr 6e-05), [[LRRC27]] (-0.47, fdr 2e-04), [[LYPLAL1-DT]] (-0.45, fdr 1e-04).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[VGF]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LONRF3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 21 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2730.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.25×** | +16.9 | 0e+00 | 15/16 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **5.74×** | +14.0 | 6e-42 | 15/17 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **11.8×** | +13.5 | 4e-39 | 2/3 (C32, A498) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **9.44×** | +12.7 | 7e-35 | 10/10 (NCI-H460, A-427, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **7.02×** | +11.0 | 3e-26 | 19/19 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **3.97×** | +11.0 | 3e-26 | 17/18 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **6.47×** | +10.6 | 3e-24 | 18/18 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **5.93×** | +10.1 | 5e-22 | 18/18 (SW480, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **6.01×** | +9.8 | 1e-20 | 9/10 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **5.93×** | +9.3 | 7e-19 | 4/4 (LoVo, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **3.68×** | +7.4 | 1e-11 | 13/16 (NCI-H460, SK-MEL-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.31×** | +6.7 | 7e-10 | 7/11 (SW480, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.18×** | +6.5 | 3e-09 | 19/19 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.17×** | +6.5 | 3e-09 | 12/17 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.21×** | +6.3 | 1e-08 | 8/19 (NCI-H2347, NCI-H460, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **2.00×** | +5.5 | 1e-06 | 4/19 (SW480, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.35×** | +4.8 | 4e-05 | 14/15 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.82×** | +3.3 | 0.018 | 0/12 | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.83×** | +3.1 | 0.033 | 0/10 | all doses, stronger at high dose | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **2.15×** | +3.1 | 0.038 | 3/13 (A498, NCI-H1792, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.14×** | +3.1 | 0.039 | 1/9 (A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.72×** | +3.0 | 0.039 | 11/18 (NCI-H2347, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.47×** | +3.0 | 0.039 | 2/15 (A498, SW480) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2730.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.496× | -3.7 | 0.10 | 5/20 (C32, SW480, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.548× | -3.2 | 0.36 | 3/18 (BT-474, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.03 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2730. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.45 | 7 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.4× (z +12.2) | — |
| [[SW480 (line)]] | alt | 4.14 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 21.3× (z +11.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 8.23× (z +11.6) | — |
| [[C32 (line)]] | wt | 13.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.20× (z +11.3) | — |
| [[A-427 (line)]] | wt | 24.7 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.30× (z +9.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A498 (line)]] | wt | 3.16 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 28.6× (z +11.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 12.1× (z +9.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 9.30 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 10.1× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 1.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 0.988 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 94.3× (z +8.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 4.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.4× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 4.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.33× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 1.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.7× (z +8.7) | — |
| [[A-172 (line)]] | wt | 0.194 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.163 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.921 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.329 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.166 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.180 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.181 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.190 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.216 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.140 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.202 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.235 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.170 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.163 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.215 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.174 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.134 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.132 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.150 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.165 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.153 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.168 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.178 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.231 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2730), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DISP3]] | +0.63 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[ARC]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CHST8]] | +0.57 | +0.67 / +0.40 | both halves | 5e-05 |  |
| [[AP3B2]] | +0.56 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[TEX15]] | +0.56 | +0.55 / +0.62 | both halves | 1e-05 | STRING 429 |
| [[CAMK2B]] | +0.56 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[RUNDC3B]] | +0.54 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[SH3RF3]] | +0.53 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[PPP1R14C]] | +0.53 | +0.52 / +0.59 | both halves | 1e-05 | STRING 466 |
| [[SYN1]] | +0.52 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[LPAR3]] | +0.52 | +0.39 / +0.65 | both halves | 6e-05 |  |
| [[OTULINL]] | +0.52 | +0.38 / +0.63 | both halves | 6e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF624]] | -0.51 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[LRRC27]] | -0.47 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[LYPLAL1-DT]] | -0.45 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[LINC01139]] | -0.44 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[WHAMMP2]] | -0.44 | -0.40 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VGF]] | B | VGF activity strengthens NPTX2's drug response | lines that do not express VGF (12) vs lines expressing it (7) | the lines without VGF respond 0.78× as strongly (z diff +1.31); strongest at Dinaciclib 5 µM: 1.52x vs 12x (z diff +7.4) | 0.059 | ⚠ within organs, on part of the lines; also absent: RAB3C, KCNH5, CSMD3; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers NPTX2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.4% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LONRF3]] | B | NPTX2 activity raises LONRF3's level | lines that do not express NPTX2 (28) vs lines expressing it (22) | 1.50× lower at baseline in the lines without NPTX2 | 0.063 | ⚠ within organs, on part of the lines; also absent: TEX15, RUNX3, ZYG11A |

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.499). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.7, 33.1); signed map (28.7, 19.9). **Vector** length 51.8, 12.7% of its response variance represented; |z| ≥ 3 in 599 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.4 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +4.3 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +4.0 | +9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +6.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.4 | +2.4 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -2.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.2 | -1.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.1 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | neuronal pentraxin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:98,617,285-98,629,869 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Long pentraxins |
| Hallmark sets | UV_RESPONSE_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [P47972](https://www.uniprot.org/uniprotkb/P47972) (Neuronal pentraxin-2):

> Likely to play role in the modification of cellular properties that underlie long-term plasticity. Binds to agar matrix in a calcium-dependent manner (By similarity).

**Summary**, from NCBI Gene [4885](https://www.ncbi.nlm.nih.gov/gene/4885):

> This gene encodes a member of the family of neuronal petraxins, synaptic proteins that are related to C-reactive protein. This protein is involved in excitatory synapse formation. It also plays a role in clustering of alpha-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid (AMPA)-type glutamate receptors at established synapses, resulting in non-apoptotic cell death of dopaminergic nerve cells. Up-regulation of this gene in Parkinson disease (PD) tissues suggests that the protein may be …

**Accessions** — [HGNC:7953](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7953) · Entrez [4885](https://www.ncbi.nlm.nih.gov/gene/4885) · UniProt [P47972](https://www.uniprot.org/uniprotkb/P47972) · Ensembl [ENSG00000106236](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106236)

## Data

Gene col 2730: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2730); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2730, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2730]; `tensor/DDL_lfc|DDL_z.npy` [2730]; `embed/gene_vectors.npy` [2730]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2730 or target_col == 2730). Every well: [[NPTX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPTX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
