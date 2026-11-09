---
symbol: "CNNM1"
type: "gene"
col: 4141
ensembl_id: "ENSG00000119946"
name: "cyclin and CBS domain divalent metal cation transport mediator 1"
location: "10q24.2"
module: 33
arm: "+"
pooled_cpm: 8.08
n_lines_expressing: 26
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 18
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# CNNM1

*cyclin and CBS domain divalent metal cation transport mediator 1* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.28× (z +16.3, q 0e+00, up in 10 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.44× (z +7.4, q 2e-11, up in 13 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.674× (z -5.6, q 1e-05, down in 11 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FXN]] (+0.64, fdr 7e-06), [[ZNF485]] (+0.63, fdr 7e-06), [[MPV17L]] (+0.62, fdr 1e-05); moves opposite to [[CDKL5]] (-0.54, fdr 3e-05), [[SYNJ1]] (-0.50, fdr 4e-05), [[MIR22HG]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EMSLR]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PTPN20]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4141.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.28×** | +16.3 | 0e+00 | 10/13 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.07×** | +16.0 | 0e+00 | 10/19 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +10.8 | 5e-25 | 9/17 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.69×** | +7.5 | 1e-11 | 15/24 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +7.4 | 2e-11 | 13/24 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +6.9 | 6e-10 | 10/24 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +5.8 | 5e-07 | 10/24 (NCI-H1573, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +4.7 | 2e-04 | 7/23 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +4.5 | 4e-04 | 7/23 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.38×** | +4.3 | 1e-03 | 7/22 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.3 | 1e-03 | 11/20 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.002 | 5/22 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.74×** | +4.1 | 0.002 | 7/22 (NCI-H1573, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **1.34×** | +4.0 | 0.002 | 9/21 (A549, SW 900, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +4.0 | 0.002 | 8/23 (A549, NCI-H1792, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.9 | 0.003 | 8/23 (A549, NCI-H1573, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.004 | 7/23 (RPMI-7951, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.20×** | +3.7 | 0.006 | 4/23 (CFPAC-1, HOP62, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.007 | 3/23 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.015 | 3/22 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.015 | 6/23 (PANC-1, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4141.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.674×** | -5.6 | 1e-05 | 11/23 (SNU-423, NCI-H460, …) | two highest doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.781×** | -5.0 | 2e-04 | 9/22 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.748×** | -4.1 | 0.007 | 4/24 (NCI-H23, PANC-1, …) | two highest doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.822×** | -3.9 | 0.011 | 8/24 (AsPC-1, LS 180, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.592×** | -3.9 | 0.011 | 7/23 (LS 180, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.842× | -3.5 | 0.052 | 8/24 (NCI-H1792, NCI-H2030, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.779×** | -3.4 | 0.053 | 6/23 (NCI-H460, SNU-423, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.784×** | -3.3 | 0.058 | 7/23 (MIA PaCa-2, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.792×** | -3.3 | 0.058 | 4/24 (CHP-212, MIA PaCa-2, …) | top dose only |  |
| [[Ivermectin (drug)]] 0.05 µM |  | **0.799×** | -3.2 | 0.083 | 1/23 (NCI-H2030) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4141. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 26.6 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -18.5) |
| [[PANC-1 (line)]] | alt | 15.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -20.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -10.7) |
| [[HOP62 (line)]] | alt | 6.34 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 23.6× (z +13.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 34.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -12.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 14.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.87× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 8.30 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.223× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 10.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.25× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.663 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.880 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.827 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.858 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.944 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.795 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.981 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.856 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.994 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.901 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.962 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4141), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FXN]] | +0.64 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[ZNF485]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[MPV17L]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[MTARC1]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[NEK6]] | +0.59 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[SFXN4]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ACBD6]] | +0.58 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[TARBP1]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[EMSLR]] | +0.56 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[PRTG]] | +0.55 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[MTARC2]] | +0.55 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[CCDC88C]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKL5]] | -0.54 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[SYNJ1]] | -0.50 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[MIR22HG]] | -0.49 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[SHOC2]] | -0.47 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[NUMB]] | -0.47 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[PPARD]] | -0.46 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[RUBCN]] | -0.46 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[FAM83A]] | -0.45 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[LRRC8A]] | -0.45 | -0.41 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EMSLR]] | B | EMSLR activity raises CNNM1's level | lines that do not express EMSLR (15) vs lines expressing it (35) | 2.52× lower at baseline in the lines without EMSLR | 0.091 | ⚠ within organs, on part of the lines; also absent: MLXIPL, GAL, P2RX5 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPN20]] | C | CNNM1 activity raises PTPN20's level | lines that do not express CNNM1 (24) vs lines expressing it (26) | 1.69× lower at baseline in the lines without CNNM1 | 0.048 | ⚠ within organs, on part of the lines; also absent: GAL, SLC35F3, RHCG; co-absent with the target |

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-0.5, 42.3); signed map (-6.6, -58.3). **Vector** length 56.4, 13.6% of its response variance represented; |z| ≥ 3 in 466 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +16.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +10.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +16.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +6.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +3.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +4.0 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -5.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -3.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -0.9 | -3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | +0.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.8 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | cyclin and CBS domain divalent metal cation transport mediator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.2 — chr10:99,329,356-99,394,330 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SLC70A1; previously ACDP1 |
| Gene groups (HGNC) | Solute carrier family 70, cyclin and CBS domain divalent metal cation transport mediators |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRU3](https://www.uniprot.org/uniprotkb/Q9NRU3) (Metal transporter CNNM1):

> Probable metal transporter.

**Summary**, from NCBI Gene [26507](https://www.ncbi.nlm.nih.gov/gene/26507):

> This gene encodes a member of the ancient conserved domain protein family. The encoded protein may bind copper. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:102](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:102) · Entrez [26507](https://www.ncbi.nlm.nih.gov/gene/26507) · UniProt [Q9NRU3](https://www.uniprot.org/uniprotkb/Q9NRU3) · Ensembl [ENSG00000119946](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119946)

## Data

Gene col 4141: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4141); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4141, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4141]; `tensor/DDL_lfc|DDL_z.npy` [4141]; `embed/gene_vectors.npy` [4141]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4141 or target_col == 4141). Every well: [[CNNM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNNM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
