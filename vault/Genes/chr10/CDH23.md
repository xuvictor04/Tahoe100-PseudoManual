---
symbol: "CDH23"
type: "gene"
col: 2872
ensembl_id: "ENSG00000107736"
name: "cadherin related 23"
location: "10q22.1"
module: 102
arm: "+"
pooled_cpm: 3.36
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# CDH23

*cadherin related 23* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.14× (z +22.8, q 0e+00, up in 30 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.904× (z -4.2, q 0.013, down in 12 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Artesunate (drug)]] 5 µM: 0.798× (z -3.6, q 0.078, down in 7 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.0997×, NCI-H23 0.182×, A549 0.213×); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.108×; ⚠ cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.140×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib (drug)]] 0.05 µM in 1 line (AN3 CA 0.0383×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBFOX3]] (+0.73, fdr 7e-06), [[PLD5]] (+0.72, fdr 7e-06), [[RFPL1S]] (+0.71, fdr 7e-06).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[JPH3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2872.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.14×** | +22.8 | 0e+00 | 30/34 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.59×** | +15.3 | 0e+00 | 30/44 (SW480, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.72×** | +10.9 | 2e-25 | 3/4 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.51×** | +10.5 | 1e-23 | 22/35 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +10.5 | 1e-23 | 16/31 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +9.5 | 2e-19 | 6/14 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +6.9 | 4e-10 | 2/9 (SW480, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.72×** | +6.2 | 5e-08 | 15/46 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.1 | 5e-08 | 11/45 (SW480, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +6.1 | 6e-08 | 15/46 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +5.9 | 2e-07 | 11/36 (SW480, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.59×** | +5.3 | 7e-06 | 15/41 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +4.7 | 1e-04 | 9/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.65×** | +4.1 | 0.002 | 1/6 (A549) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +4.1 | 0.002 | 11/44 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.020 | 3/23 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.34×** | +3.1 | 0.052 | 1/15 (SW480) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2872.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.0997×, NCI-H23 0.182×, A549 0.213×); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.108×; ⚠ cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.140×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib (drug)]] 0.05 µM in 1 line (AN3 CA 0.0383×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.904× | -4.2 | 0.013 | 12/47 (HOP62, LoVo, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | **0.798×** | -3.6 | 0.078 | 7/45 (C-33 A, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.741× | -3.2 | 0.24 | 3/44 (HS-578T, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2872. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.67 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 9.63× (z +10.0) | — |
| [[A-427 (line)]] | wt | 32.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0997× (z -20.0) |
| [[SW480 (line)]] | alt | 5.06 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 7.10× (z +14.6) | — |
| [[A549 (line)]] | wt | 10.00 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.34× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -9.5) |
| [[AN3 CA (line)]] | alt | 35.0 | 0 | 1 | — | [[Ixazomib (drug)]] 0.05 µM 0.0383× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 11.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 1.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.1× (z +12.1) | — |
| [[A-172 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.987 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2872), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBFOX3]] | +0.73 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[PLD5]] | +0.72 | +0.69 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[RFPL1S]] | +0.71 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.70 | +0.54 / +0.81 | both halves | 1e-05 |  |
| [[RHBDL3]] | +0.69 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[GBX1]] | +0.69 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[CELF5]] | +0.69 | +0.62 / +0.78 | both halves | 7e-06 |  |
| [[EFHD1]] | +0.68 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[CACNA2D2]] | +0.68 | +0.69 / +0.70 | both halves | 7e-06 | pathway: Sensory Perception |
| [[SLC27A6]] | +0.68 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[GRID1]] | +0.68 | +0.56 / +0.65 | both halves | 1e-05 | same gene group |
| [[ATP8A2]] | +0.67 | +0.51 / +0.78 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JPH3]] | B | JPH3 activity strengthens CDH23's drug response | lines that do not express JPH3 (29) vs lines expressing it (17) | the lines without JPH3 respond 0.65× as strongly (z diff +0.87); strongest at Dinaciclib 5 µM: 0.84x vs 2.68x (z diff +3.9) | 0.036 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ELFN1]] | B | ELFN1 activity raises CDH23's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.58× lower at baseline in the lines without ELFN1 | 0.041 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[CHD5]] | B | CHD5 activity raises CDH23's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.67× lower at baseline in the lines without CHD5 | 0.048 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[PDZD4]] | B | PDZD4 activity raises CDH23's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 1.71× lower at baseline in the lines without PDZD4 | 0.050 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[RET]] | B | RET activity raises CDH23's level | lines that do not express RET (28) vs lines expressing it (22) | 1.89× lower at baseline in the lines without RET | 0.052 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[MAP6]] | B | MAP6 activity strengthens CDH23's drug response | lines that do not express MAP6 (22) vs lines expressing it (24) | the lines without MAP6 respond 0.60× as strongly (z diff +0.97); strongest at Panobinostat 0.05 µM: 1.30x vs 2.35x (z diff +2.2) | 0.068 | ⚠ within organs, on part of the lines; also absent: PCSK1N, ZFP28, SNAP91; target measured in part of the lines; artifact flags |
| [[DPYSL5]] | B | DPYSL5 activity raises CDH23's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 1.64× lower at baseline in the lines without DPYSL5 | 0.072 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[CYS1]] | B | CYS1 activity raises CDH23's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 1.48× lower at baseline in the lines without CYS1 | 0.080 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4 |
| [[PAX2]] | B | PAX2 activity raises CDH23's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.01× lower at baseline in the lines without PAX2 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[LRRC4B]] | B | LRRC4B activity raises CDH23's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 1.61× lower at baseline in the lines without LRRC4B | 0.098 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[KIAA2012]] | C | KIAA2012 activity lowers CDH23's level | lines that do not express KIAA2012 (3) vs lines expressing it (47) | 2.18× higher at baseline in the lines without KIAA2012 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OPN3, SMAD7, TESK2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.807). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.6, 34.6); signed map (27.7, 21.8). **Vector** length 53.4, 6.93% of its response variance represented; |z| ≥ 3 in 1,170 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.53 to 8); *Transmission across Chemical Synapses* (reactome, mean cos +0.56 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +22.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +15.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.5 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +6.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -4.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -1.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | cadherin related 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:71,396,920-71,815,947 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDHR23; previously DFNB12, USH1D |
| Gene groups (HGNC) | Cadherin related; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H251](https://www.uniprot.org/uniprotkb/Q9H251) (Cadherin-23):

> Cadherins are calcium-dependent cell adhesion proteins. They preferentially interact with themselves in a homophilic manner in connecting cells. CDH23 is required for establishing and/or maintaining the proper organization of the stereocilia bundle of hair cells in the cochlea and the vestibule during late embryonic/early postnatal development. It is part of the functional network formed by USH1C, USH1G, CDH23 and MYO7A that mediates mechanotransduction in cochlear hair cells. Required for …

**Summary**, from NCBI Gene [64072](https://www.ncbi.nlm.nih.gov/gene/64072):

> This gene is a member of the cadherin superfamily, whose genes encode calcium dependent cell-cell adhesion glycoproteins. The encoded protein is thought to be involved in stereocilia organization and hair bundle formation. The gene is located in a region containing the human deafness loci DFNB12 and USH1D. Usher syndrome 1D and nonsyndromic autosomal recessive deafness DFNB12 are caused by allelic mutations of this cadherin-like gene. Upregulation of this gene may also be associated with breast …

**Accessions** — [HGNC:13733](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13733) · Entrez [64072](https://www.ncbi.nlm.nih.gov/gene/64072) · UniProt [Q9H251](https://www.uniprot.org/uniprotkb/Q9H251) · Ensembl [ENSG00000107736](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107736)

## Data

Gene col 2872: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2872); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2872, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2872]; `tensor/DDL_lfc|DDL_z.npy` [2872]; `embed/gene_vectors.npy` [2872]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2872 or target_col == 2872). Every well: [[CDH23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDH23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
