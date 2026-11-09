---
symbol: "SLC35F4"
type: "gene"
col: 7569
ensembl_id: "ENSG00000151812"
name: "solute carrier family 35 member F4"
location: "14q22.3-q23.1"
module: 90
arm: "+"
pooled_cpm: 5.77
n_lines_expressing: 44
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# SLC35F4

*solute carrier family 35 member F4* — 14q22.3-q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.15× (z +19.5, q 0e+00, up in 22 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Dihydroartemisinin (drug)]] 5 µM: 0.654× (z -4.1, q 0.022, down in 7 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (CFPAC-1 0.0814×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.180×); [[Methotrexate (drug)]] 0.5 µM in 1 line (NCI-H23 0.0520×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CFPAC-1 0.105×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNBD1]] (+0.72, fdr 1e-05), [[LINC02511]] (+0.69, fdr 2e-05), [[PTPRT]] (+0.67, fdr 1e-05).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[CCDC26]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7569.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.15×** | +19.5 | 0e+00 | 22/29 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.27×** | +11.3 | 5e-27 | 28/38 (KATO III, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.12×** | +10.6 | 5e-24 | 0/3 | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.72×** | +9.7 | 3e-20 | 24/35 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.98×** | +9.7 | 4e-20 | 0/6 | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.56×** | +9.1 | 7e-18 | 2/15 (A498, LS 180) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.29×** | +8.1 | 7e-14 | 17/33 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.97×** | +6.6 | 3e-09 | 18/32 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +6.3 | 1e-08 | 8/29 (LOX-IMVI, A549, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +5.2 | 1e-05 | 8/31 (BT-474, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +5.1 | 1e-05 | 8/23 (A549, A498, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.9 | 4e-05 | 7/38 (LS 180, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.55×** | +4.2 | 1e-03 | 12/40 (NCI-H2030, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.11×** | +3.8 | 0.006 | 0/6 | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.09×** | +3.8 | 0.007 | 8/25 (HEC-1-A, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.022 | 3/26 (HS-578T, NCI-H1573, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.029 | 1/29 (NCI-H460) | rises with dose | position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.063 | 6/37 (SHP-77, HT-29, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.78×** | +2.9 | 0.096 | 6/17 (SW1417, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7569.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (CFPAC-1 0.0814×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.180×); [[Methotrexate (drug)]] 0.5 µM in 1 line (NCI-H23 0.0520×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CFPAC-1 0.105×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.654×** | -4.1 | 0.022 | 7/37 (HCT15, BT-474, …) | rises with dose |  |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | 0.682× | -3.6 | 0.10 | 7/33 (NCI-H23, SW1417, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.717× | -3.2 | 0.24 | 10/35 (SHP-77, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | 0.724× | -3.1 | 0.25 | 3/33 (hTERT-HPNE, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7569. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 9.48 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0814× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.180× (z -9.2) |
| [[A549 (line)]] | wt | 2.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.30× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 1.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 45.9× (z +11.4) | — |
| [[KATO III (line)]] | alt | 2.18 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 16.2× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 4.35 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.11× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 2.95 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 20.6× (z +8.8) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H23 (line)]] | alt | 3.71 | 0 | 1 | — | [[Methotrexate (drug)]] 0.5 µM 0.0520× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 1.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.85× (z +8.7) | — |
| [[SW480 (line)]] | alt | 2.68 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.50× (z +8.7) | — |
| [[A-172 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7569), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNBD1]] | +0.72 | +0.57 / +0.78 | both halves | 1e-05 |  |
| [[LINC02511]] | +0.69 | +0.46 / +0.76 | both halves | 2e-05 |  |
| [[PTPRT]] | +0.67 | +0.51 / +0.76 | both halves | 1e-05 |  |
| [[ATP8A2]] | +0.66 | +0.41 / +0.76 | both halves | 4e-05 |  |
| [[MTUS2]] | +0.65 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[ENTPD1]] | +0.64 | +0.42 / +0.71 | both halves | 4e-05 |  |
| [[MYH16]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[SORCS1]] | +0.63 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[ATP6V0A4]] | +0.62 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[CCDC26]] | +0.61 | +0.39 / +0.71 | both halves | 5e-05 |  |
| [[CFAP20DC-AS1]] | +0.60 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[PWRN1]] | +0.60 | +0.32 / +0.71 | both halves | 2e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC35F4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DYSF]] | B | DYSF activity lowers SLC35F4's level | lines that do not express DYSF (11) vs lines expressing it (39) | 1.63× higher at baseline in the lines without DYSF | 0.072 | ⚠ within organs, on part of the lines; also absent: ISM2, IRX3, DNAAF9; maybe low, not absent |
| [[LHFPL5]] | C | LHFPL5's natural level weakens SLC35F4's drug response | LHFPL5's natural level across 38 lines (lineage-adjusted; a glimpse) | r -0.73, reverse -0.59; direction not clear | 0.057 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC26]] | B | SLC35F4 activity lowers CCDC26's level | lines that do not express SLC35F4 (6) vs lines expressing it (44) | 2.95× higher at baseline in the lines without SLC35F4 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC01811, LINC01482; maybe low, not absent |
| [[CLVS1]] | C | SLC35F4's natural level weakens CLVS1's drug response | SLC35F4's natural level across 39 lines (lineage-adjusted; a glimpse) | r -0.80, reverse -0.49; direction clear | 0.005 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.680). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.2, 30.8); signed map (32.5, 17.4). **Vector** length 55.4, 8.83% of its response variance represented; |z| ≥ 3 in 834 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +19.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +11.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +4.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.0 | +2.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member F4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.3-q23.1 — chr14:57,563,920-57,982,194 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37712; previously C14orf36 |
| Gene groups (HGNC) | Solute carrier family 35 |
| Matched by | ensembl_id |

**Function**, from UniProt [A4IF30](https://www.uniprot.org/uniprotkb/A4IF30) (Solute carrier family 35 member F4):

> Mediates choline transport, although the underlying transport mechanism remains to be elucidated.

**Summary**, from NCBI Gene [341880](https://www.ncbi.nlm.nih.gov/gene/341880):

> Enables choline transmembrane transporter activity. Involved in choline transport. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19845](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19845) · Entrez [341880](https://www.ncbi.nlm.nih.gov/gene/341880) · UniProt [A4IF30](https://www.uniprot.org/uniprotkb/A4IF30) · Ensembl [ENSG00000151812](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151812)

## Data

Gene col 7569: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7569); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7569, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7569]; `tensor/DDL_lfc|DDL_z.npy` [7569]; `embed/gene_vectors.npy` [7569]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7569 or target_col == 7569). Every well: [[SLC35F4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35F4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
