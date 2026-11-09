---
symbol: "SH3GL1"
type: "gene"
col: 6588
ensembl_id: "ENSG00000141985"
name: "SH3 domain containing GRB2 like 1, endophilin A2"
location: "19p13.3"
module: 3
arm: "+"
pooled_cpm: 81.11
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SH3GL1

*SH3 domain containing GRB2 like 1, endophilin A2* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.78× (z +8.1, q 4e-13, up in 40 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.23× (z +5.8, q 1e-06, up in 35 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.634× (z -8.4, q 2e-14, down in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.745× (z -5.5, q 8e-06, down in 31 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATG4B]] (+0.79, fdr 7e-06), [[ARID3A]] (+0.71, fdr 7e-06), [[TRPT1]] (+0.71, fdr 7e-06); moves opposite to [[ZXDA]] (-0.70, fdr 2e-05), [[ZXDB]] (-0.69, fdr 1e-05), [[EIF4G2]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NAB2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6588.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.78×** | +8.1 | 4e-13 | 40/48 (SW480, AsPC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.55×** | +6.1 | 4e-07 | 35/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.23×** | +5.8 | 1e-06 | 35/49 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +4.4 | 0.002 | 34/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.36×** | +4.2 | 0.003 | 28/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.27×** | +3.3 | 0.087 | 26/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.088 | 24/48 (HEC-1-A, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6588.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.634×** | -8.4 | 2e-14 | 41/48 (Hs 766T, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.745×** | -5.5 | 8e-06 | 31/49 (CFPAC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.664×** | -5.5 | 8e-06 | 28/43 (NCI-H23, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.718×** | -4.6 | 5e-04 | 29/48 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.774×** | -4.6 | 5e-04 | 26/48 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.746×** | -3.8 | 0.015 | 31/50 (NCI-H23, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.784×** | -3.4 | 0.059 | 22/47 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.842× | -3.3 | 0.077 | 19/48 (hTERT-HPNE, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.779×** | -3.2 | 0.083 | 22/48 (NCI-H23, A-427, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.790×** | -3.1 | 0.093 | 23/47 (NCI-H23, hTERT-HPNE, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.658× | -3.0 | 0.12 | 18/50 (NCI-H23, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6588. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 56.3 | 5 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.94× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.64× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 90.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.401× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 41.0 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +9.5) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 110 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 78.3 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +12.6) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[HEC-1-A (line)]] | alt | 103 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -8.6) |
| [[Hs 766T (line)]] | wt | 70.1 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.362× (z -12.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 81.4 | 1 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.59× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 128 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -19.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 61.7 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +11.0) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A-427 (line)]] | wt | 71.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.445× (z -11.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[AN3 CA (line)]] | alt | 70.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 103 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -11.2) |
| [[HCT15 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 138 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -11.3) |
| [[KATO III (line)]] | alt | 46.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.444× (z -8.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 46.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.95× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 91.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.499× (z -8.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[Panc 03.27 (line)]] | alt | 77.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -14.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 76.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 177 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 72.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 82.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 70.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 87.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 75.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6588), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG4B]] | +0.79 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[ARID3A]] | +0.71 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[TRPT1]] | +0.71 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[ATG101]] | +0.70 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[MYO9B]] | +0.69 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[MPG]] | +0.69 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[SLC35E1]] | +0.69 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[B3GAT3]] | +0.69 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[SDHAP2]] | +0.68 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[ARID3B]] | +0.68 | +0.71 / +0.45 | both halves | 3e-05 |  |
| [[YIF1B]] | +0.67 | +0.65 / +0.40 | both halves | 5e-05 |  |
| [[KDM4B]] | +0.66 | +0.61 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDA]] | -0.70 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[ZXDB]] | -0.69 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.66 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.66 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[FGF2]] | -0.65 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[ZNF300]] | -0.65 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[RNF6]] | -0.65 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[UTP20]] | -0.64 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[FAIM]] | -0.63 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[ZNF507]] | -0.63 | -0.68 / -0.44 | both halves | 3e-05 |  |
| [[POLR2M]] | -0.62 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[BAG2]] | -0.62 | -0.61 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAB2]] | C | NAB2 activity raises SH3GL1's level | lines that do not express NAB2 (3) vs lines expressing it (47) | 1.88× lower at baseline in the lines without NAB2 | 0.047 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.755). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (4.9, 0.2); signed map (-30.7, 14.3). **Vector** length 118, 36.1% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.6 | +1.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.2 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +5.0 | +4.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | +2.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.0 | +3.3 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +2.7 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | -0.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.5 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -8.9 | -8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.5 | -4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.4 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.1 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | SH3 domain containing GRB2 like 1, endophilin A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,360,370-4,400,547 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SH3P8, SH3D2B, CNSA1, EEN, MGC111371 |
| Gene groups (HGNC) | N-BAR domain containing; SH3 domain containing |
| Reactome | 12 pathways, smallest: InlB-mediated entry of Listeria monocytogenes into host cell; Listeria monocytogenes entry into host cells; Negative regulation of MET activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99961](https://www.uniprot.org/uniprotkb/Q99961) (Endophilin-A2):

> Implicated in endocytosis. In a first step mediates neck formation during ultrafast endocytosis and function at a second step to aid in the removal of clathrin coats from the regenerated vesicles (By similarity). May recruit other proteins to membranes with high curvature (By similarity).

**Summary**, from NCBI Gene [6455](https://www.ncbi.nlm.nih.gov/gene/6455):

> This gene encodes a member of the endophilin family of Src homology 3 domain-containing proteins. The encoded protein is involved in endocytosis and may also play a role in the cell cycle. Overexpression of this gene may play a role in leukemogenesis, and the encoded protein has been implicated in acute myeloid leukemia as a fusion partner of the myeloid-lymphoid leukemia protein. Pseudogenes of this gene are located on the long arm of chromosomes 11 and 17. Alternatively spliced transcript …

**Accessions** — [HGNC:10830](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10830) · Entrez [6455](https://www.ncbi.nlm.nih.gov/gene/6455) · UniProt [Q99961](https://www.uniprot.org/uniprotkb/Q99961) · Ensembl [ENSG00000141985](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141985)

## Data

Gene col 6588: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6588); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6588, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6588]; `tensor/DDL_lfc|DDL_z.npy` [6588]; `embed/gene_vectors.npy` [6588]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6588 or target_col == 6588). Every well: [[SH3GL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3GL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
