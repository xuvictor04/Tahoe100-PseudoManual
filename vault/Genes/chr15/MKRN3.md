---
symbol: "MKRN3"
type: "gene"
col: 11035
ensembl_id: "ENSG00000179455"
name: "makorin ring finger protein 3"
location: "15q11.2"
module: 23
arm: "+"
pooled_cpm: 17.61
n_lines_expressing: 27
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# MKRN3

*makorin ring finger protein 3* — 15q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +10.1, q 4e-21, up in 17 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.700× (z -4.7, q 0.002, down in 13 of 25 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.762× (z -3.6, q 0.067, down in 10 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-172 0.149×, C-33 A 0.131×, SK-MEL-2 0.141×, RPMI-7951 0.142×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (KATO III 0.157×, C32 0.129×, PANC-1 0.296×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C32 0.149×; ⚠ toxic; cell-cycle shift, explains ~67% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAS2R4]] (+0.75, fdr 7e-06), [[ANKRD17-DT]] (+0.71, fdr 1e-05), [[CDKL3]] (+0.70, fdr 1e-05); moves opposite to [[MPP1]] (-0.56, fdr 1e-04), [[APMAP]] (-0.55, fdr 5e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 2 go from it, the strongest it → [[LRRTM4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11035.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +10.1 | 4e-21 | 17/25 (PANC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +6.8 | 3e-09 | 13/25 (SHP-77, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +5.2 | 3e-05 | 4/19 (J82, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +5.0 | 8e-05 | 10/24 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.9 | 1e-04 | 13/25 (SW1417, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +4.3 | 0.001 | 13/24 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.009 | 10/24 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.025 | 9/24 (HS-578T, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.026 | 12/25 (KATO III, PANC-1, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.029 | 14/25 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.044 | 8/24 (HepG2/C3A, NCI-H1792, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.056 | 6/25 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.18× | +3.1 | 0.073 | 9/25 (H4, HS-578T, …) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11035.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-172 0.149×, C-33 A 0.131×, SK-MEL-2 0.141×, RPMI-7951 0.142×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (KATO III 0.157×, C32 0.129×, PANC-1 0.296×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C32 0.149×; ⚠ toxic; cell-cycle shift, explains ~67% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.700×** | -4.7 | 0.002 | 13/25 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.742×** | -3.9 | 0.027 | 11/25 (SW480, SW 1088, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.762×** | -3.6 | 0.067 | 10/25 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.771×** | -3.4 | 0.092 | 6/25 (SW480, C-33 A, …) | all doses, flat |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.783× | -3.2 | 0.16 | 7/25 (J82, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11035. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 35.5 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -12.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 31.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 54.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +10.7) | — |
| [[A-172 (line)]] | wt | 56.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 79.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -14.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 39.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +10.0) | — |
| [[A-427 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.08 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 44.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11035), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAS2R4]] | +0.75 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[ANKRD17-DT]] | +0.71 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[CDKL3]] | +0.70 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[MAIP1]] | +0.68 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[ZNF721]] | +0.68 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[PRANCR]] | +0.67 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[RFX3-DT]] | +0.67 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[ATE1OSP]] | +0.66 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[CHD1-DT]] | +0.65 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[THAP2]] | +0.65 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[THBS4]] | +0.65 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[LATS1]] | +0.64 | +0.63 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPP1]] | -0.56 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[APMAP]] | -0.55 | -0.44 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises MKRN3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers MKRN3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LRRTM4]] | C | LRRTM4 activity raises MKRN3's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 6.77× lower at baseline in the lines without LRRTM4 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRTM4]] | C | MKRN3 activity raises LRRTM4's level | lines that do not express MKRN3 (23) vs lines expressing it (27) | 4.79× lower at baseline in the lines without MKRN3 | 0.005 | ⚠ within organs, on part of the lines; also absent: GABRA3, LRRTM4, MAGEA3-DT; co-absent with the target |
| [[LINC02008]] | C | MKRN3 activity raises LINC02008's level | lines that do not express MKRN3 (23) vs lines expressing it (27) | 2.84× lower at baseline in the lines without MKRN3 | 0.056 | ⚠ within organs, on part of the lines; also absent: GABRA3, LRRTM4, MAGEA3-DT; co-absent with the target |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.716). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (3.5, 16.9); signed map (25.6, -8.1). **Vector** length 56.4, 12.9% of its response variance represented; |z| ≥ 3 in 462 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.9 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.6 | +4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +10.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +3.2 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | -2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -2.3 | -3.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -1.2 | -2.3 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.2 | -3.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | makorin ring finger protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q11.2 — chr15:23,565,674-23,630,075 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RNF63, ZFP127, MGC88288; previously ZNF127, D15S9 |
| Gene groups (HGNC) | Ring finger proteins; Zinc fingers CCCH-type; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13064](https://www.uniprot.org/uniprotkb/Q13064) (E3 ubiquitin-protein ligase makorin-3):

> E3 ubiquitin ligase catalyzing the covalent attachment of ubiquitin moieties onto substrate proteins. Acts as a key developmental timer that helps ensure puberty begins at the appropriate age, by inhibiting premature activation of the reproductive hormone cascade. Epigenetically regulates GNRH1 transcription by disrupting the binding of methyl-DNA binding protein 3/MBD3 to the promoter of GNRH1. Mechanistically, mediates the non-proteolytic ubiquitination of MBD3 at multiple sites with 'Lys27' …

**Summary**, from NCBI Gene [7681](https://www.ncbi.nlm.nih.gov/gene/7681):

> The protein encoded by this gene contains a RING (C3HC4) zinc finger motif and several C3H zinc finger motifs. This gene is intronless and imprinted, with expression only from the paternal allele. Disruption of the imprinting at this locus may contribute to Prader-Willi syndrome. An antisense RNA of unknown function has been found overlapping this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7114](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7114) · Entrez [7681](https://www.ncbi.nlm.nih.gov/gene/7681) · UniProt [Q13064](https://www.uniprot.org/uniprotkb/Q13064) · Ensembl [ENSG00000179455](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179455)

## Data

Gene col 11035: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11035); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11035, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11035]; `tensor/DDL_lfc|DDL_z.npy` [11035]; `embed/gene_vectors.npy` [11035]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11035 or target_col == 11035). Every well: [[MKRN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MKRN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
