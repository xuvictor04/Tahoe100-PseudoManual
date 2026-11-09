---
symbol: "MYH16"
type: "gene"
col: 18
ensembl_id: "ENSG00000002079"
name: "myosin heavy chain 16"
location: "7q22.1"
module: 229
arm: "+"
pooled_cpm: 4.15
n_lines_expressing: 47
n_dd_up: 12
n_dd_down: 22
n_dd_up_clean: 6
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/229"]
generated_by: "tahoemap"
---

# MYH16

*myosin heavy chain 16* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.68× (z +12.9, q 4e-35, up in 16 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.558× (z -5.4, q 4e-05, down in 16 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAST4]] (+0.66, fdr 7e-06), [[SLC35F4]] (+0.64, fdr 7e-06), [[LTBP2]] (+0.62, fdr 9e-06).
> It is in [[Module 229]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[WFDC10B]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ATP6V0A4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 18.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.68×** | +12.9 | 4e-35 | 16/27 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.27×** | +10.7 | 3e-24 | 17/30 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.07×** | +10.0 | 4e-21 | 7/8 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.53×** | +8.6 | 1e-15 | 6/16 (SNU-423, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.53×** | +7.9 | 2e-13 | 2/10 (SNU-423, Panc 03.27) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.62×** | +6.3 | 3e-08 | 9/41 (A498, C32, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.73×** | +5.0 | 4e-05 | 9/38 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.71×** | +4.9 | 5e-05 | 1/18 (CFPAC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +4.5 | 4e-04 | 7/32 (A549, HS-578T, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +4.2 | 0.001 | 8/35 (C32, AsPC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.03×** | +3.4 | 0.033 | 3/12 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.2 | 0.057 | 4/16 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 18.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.558×** | -5.4 | 4e-05 | 16/38 (HEC-1-A, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.588×** | -4.9 | 3e-04 | 13/40 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.602×** | -4.7 | 5e-04 | 16/34 (SNU-423, Hs 766T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.606×** | -4.6 | 5e-04 | 15/40 (A549, SNU-423, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.613×** | -4.5 | 6e-04 | 12/34 (Panc 03.27, SNU-423, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.615×** | -4.5 | 6e-04 | 17/38 (HEC-1-A, AsPC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.709×** | -4.5 | 6e-04 | 12/41 (Panc 03.27, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.626×** | -4.3 | 0.001 | 10/38 (AsPC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.614×** | -4.1 | 0.002 | 13/41 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.736×** | -4.0 | 0.003 | 13/40 (AsPC-1, HOP62, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.651×** | -4.0 | 0.004 | 12/41 (HEC-1-A, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.656×** | -3.9 | 0.005 | 11/40 (Panc 03.27, HS-578T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.636×** | -3.9 | 0.005 | 11/41 (HEC-1-A, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.760×** | -3.6 | 0.015 | 11/40 (HEC-1-A, SNU-423, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.687×** | -3.5 | 0.019 | 11/39 (HOP62, NCI-H1573, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.703×** | -3.3 | 0.038 | 14/24 (HOP62, LOX-IMVI, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 18. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 29.1 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -14.5) |
| [[HEC-1-A (line)]] | alt | 11.6 | 0 | 4 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0671× (z -10.0) |
| [[A498 (line)]] | wt | 2.47 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.25× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 4.25 | 0 | 2 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.393× (z -10.6) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 18.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0523× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 1.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.6× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 1.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.2× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 4.06 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0775× (z -8.6) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 1.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +12.7) | — |
| [[RPMI-7951 (line)]] | alt | 3.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 8.34 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.122× (z -9.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.993 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.964 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 18), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST4]] | +0.66 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[SLC35F4]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[LTBP2]] | +0.62 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[TRPV3]] | +0.59 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[FGF1]] | +0.59 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[DNAH17]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[WNT7A]] | +0.57 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[ITGB1-DT]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[PLAU]] | +0.57 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[SLC45A3]] | +0.57 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[PLXNA4]] | +0.56 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[ITGA2-AS1]] | +0.56 | +0.56 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WFDC10B]] | B | WFDC10B activity raises MYH16's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 1.52× lower at baseline in the lines without WFDC10B | 0.035 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers MYH16's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[ATG9B]] | B | ATG9B activity raises MYH16's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 1.65× lower at baseline in the lines without ATG9B | 0.053 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[KPNA7]] | B | KPNA7 activity raises MYH16's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 1.91× lower at baseline in the lines without KPNA7 | 0.060 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MYH16's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ADAM8]] | B | ADAM8 activity raises MYH16's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 1.79× lower at baseline in the lines without ADAM8 | 0.081 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[PLAU]] | B | PLAU activity raises MYH16's level | lines that do not express PLAU (26) vs lines expressing it (24) | 1.76× lower at baseline in the lines without PLAU | 0.087 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP6V0A4]] | C | MYH16 activity lowers ATP6V0A4's level | lines that do not express MYH16 (3) vs lines expressing it (47) | 2.19× higher at baseline in the lines without MYH16 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ARSD, PER3, IGF2BP2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 229]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.637). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.3, 0.3); signed map (13.2, 45.2). **Vector** length 79.2, 15.4% of its response variance represented; |z| ≥ 3 in 1,135 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +10.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +12.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.6 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +4.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.1 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -3.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.7 | -2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | myosin heavy chain 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:99,238,829-99,306,809 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | MHC20, MYH16P; previously MYH5 |
| Gene groups (HGNC) | Myosin heavy chains, class II |
| Matched by | symbol |

**Function**, from UniProt [Q9H6N6](https://www.uniprot.org/uniprotkb/Q9H6N6) (Putative uncharacterized protein MYH16):

> Has most probably lost the function in masticatory muscles contraction suspected for its homologs in dog (AC F1PT61) and apes.

**Summary**, from NCBI Gene [84176](https://www.ncbi.nlm.nih.gov/gene/84176):

> The protein coding status of the MYH16 gene is uncertain. In nonhuman primates, this gene encodes a sarcomeric myosin heavy chain expressed in masticatory muscles, but has been hypothesized to be inactivated in humans. Stedman et al. (2004) [PubMed 15042088] suggest that the decrement in masticatory muscle size caused by the inactivation of MYH16 removed an evolutionary constraint on encephalization in early man. However, there is peptide support suggesting that a shorter protein containing …

**Accessions** — [HGNC:31038](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31038) · Entrez [84176](https://www.ncbi.nlm.nih.gov/gene/84176) · UniProt [Q9H6N6](https://www.uniprot.org/uniprotkb/Q9H6N6) · Ensembl [ENSG00000002079](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000002079)

## Data

Gene col 18: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 18); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 18, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 18]; `tensor/DDL_lfc|DDL_z.npy` [18]; `embed/gene_vectors.npy` [18]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 18 or target_col == 18). Every well: [[MYH16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYH16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
