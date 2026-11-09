---
symbol: "MED12"
type: "gene"
col: 11560
ensembl_id: "ENSG00000184634"
name: "mediator complex subunit 12"
location: "Xq13.1"
module: 173
arm: "+"
pooled_cpm: 23.64
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# MED12

*mediator complex subunit 12* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.47× (z +16.9, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.327× (z -14.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARFGAP2]] (+0.75, fdr 7e-06), [[TAPBPL]] (+0.74, fdr 7e-06), [[DDX6]] (+0.74, fdr 2e-05); moves opposite to [[TMEM120B]] (-0.75, fdr 7e-06), [[COG5]] (-0.74, fdr 1e-05), [[ANKRD27]] (-0.69, fdr 2e-05).
> It is in [[Module 173]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11560.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.47×** | +16.9 | 0e+00 | 41/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.26×** | +10.7 | 3e-24 | 43/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.01×** | +7.2 | 1e-10 | 35/48 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.57×** | +6.5 | 1e-08 | 38/48 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +5.1 | 3e-05 | 28/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +5.0 | 6e-05 | 26/47 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +4.6 | 3e-04 | 26/47 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.27×** | +4.5 | 6e-04 | 22/48 (A498, Hs 766T, …) | top dose only | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.83×** | +4.2 | 0.002 | 21/46 (NCI-H1573, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +4.2 | 0.002 | 22/47 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11560.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.327×** | -14.7 | 0e+00 | 47/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.360×** | -13.4 | 2e-38 | 47/48 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.366×** | -13.2 | 2e-37 | 46/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.487×** | -9.5 | 5e-19 | 44/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.707×** | -6.4 | 2e-08 | 30/48 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.667×** | -5.3 | 1e-05 | 33/47 (A-172, NCI-H661, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.542×** | -4.2 | 0.002 | 21/48 (A549, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.827×** | -3.5 | 0.032 | 22/47 (NCI-H460, SNU-423, …) | top dose only | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | 0.632× | -3.1 | 0.10 | 16/46 (H4, CFPAC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | 0.741× | -3.1 | 0.11 | 16/44 (Hs 766T, NCI-H661, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11560. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 31.0 | 4 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.308× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 28.7 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +13.3) | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -13.4) |
| [[A498 (line)]] | wt | 15.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.50× (z +20.0) | — |
| [[HOP62 (line)]] | alt | 22.4 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.253× (z -10.9) |
| [[LoVo (line)]] | wt | 19.4 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.237× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 25.2 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.253× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 29.9 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.260× (z -9.8) |
| [[SNU-423 (line)]] | alt | 37.0 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 22.3 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 34.5 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -11.5) |
| [[PANC-1 (line)]] | alt | 24.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +20.3) | — |
| [[SW480 (line)]] | alt | 32.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.227× (z -13.4) |
| [[A549 (line)]] | wt | 22.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +17.3) | [[Panobinostat (drug)]] 5 µM 0.266× (z -9.1) |
| [[HT-29 (line)]] | alt | 24.4 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.222× (z -10.7) |
| [[KATO III (line)]] | alt | 24.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 25.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.257× (z -8.9) |
| [[SW1417 (line)]] | alt | 29.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.305× (z -9.0) |
| [[A-172 (line)]] | wt | 20.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +13.8) | — |
| [[A-427 (line)]] | wt | 23.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +13.5) | — |
| [[AN3 CA (line)]] | alt | 30.6 | 0 | 1 | — | [[Nevirapine (drug)]] 0.05 µM 0.0735× (z -9.4) |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.105× (z -9.5) |
| [[H4 (line)]] | wt | 18.3 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.103× (z -10.1) |
| [[HCT15 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 21.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 18.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +15.2) | — |
| [[NCI-H2347 (line)]] | alt | 17.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +11.5) | — |
| [[SW 900 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11560), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARFGAP2]] | +0.75 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[TAPBPL]] | +0.74 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[DDX6]] | +0.74 | +0.46 / +0.71 | both halves | 2e-05 |  |
| [[HNRNPH2]] | +0.73 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[UBAP2L]] | +0.73 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[BRPF3]] | +0.73 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[AKT1S1]] | +0.72 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[STRN4]] | +0.72 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[ZNF564]] | +0.72 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[CNOT3]] | +0.71 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[TAF9B]] | +0.70 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[ZNF776]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM120B]] | -0.75 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[COG5]] | -0.74 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[ANKRD27]] | -0.69 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[SPTLC2]] | -0.67 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[EIF4EBP1]] | -0.66 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[CARD19]] | -0.66 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[EEF1AKMT4]] | -0.65 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[MPG]] | -0.65 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[MAP2K1]] | -0.65 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[MYO9B]] | -0.65 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[WDFY2]] | -0.64 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[PCMT1]] | -0.64 | -0.55 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises MED12's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises MED12's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.841). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-9.7, 4.3); signed map (16.4, -22.4). **Vector** length 97.5, 24.0% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.6 | +16.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.9 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.1 | -0.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.1 | -1.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +5.8 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +1.2 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.9 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.4 | +0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +0.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.6 | -13.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.4 | -14.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.2 | -13.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.2 | -9.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.9 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -6.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -4.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:71,118,543-71,144,103 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAGH45, HOPA, OPA1, TRAP230, KIAA0192, OKS, ARC240, Kto; previously TNRC11, FGS1 |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 13 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q93074](https://www.uniprot.org/uniprotkb/Q93074) (Mediator of RNA polymerase II transcription subunit 12):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [9968](https://www.ncbi.nlm.nih.gov/gene/9968):

> The initiation of transcription is controlled in part by a large protein assembly known as the preinitiation complex. A component of this preinitiation complex is a 1.2 MDa protein aggregate called Mediator. This Mediator component binds with a CDK8 subcomplex which contains the protein encoded by this gene, mediator complex subunit 12 (MED12), along with MED13, CDK8 kinase, and cyclin C. The CDK8 subcomplex modulates Mediator-polymerase II interactions and thereby regulates transcription …

**Accessions** — [HGNC:11957](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11957) · Entrez [9968](https://www.ncbi.nlm.nih.gov/gene/9968) · UniProt [Q93074](https://www.uniprot.org/uniprotkb/Q93074) · Ensembl [ENSG00000184634](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184634)

## Data

Gene col 11560: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11560); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11560, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11560]; `tensor/DDL_lfc|DDL_z.npy` [11560]; `embed/gene_vectors.npy` [11560]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11560 or target_col == 11560). Every well: [[MED12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
