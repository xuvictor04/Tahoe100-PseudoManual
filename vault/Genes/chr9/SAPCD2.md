---
symbol: "SAPCD2"
type: "gene"
col: 11790
ensembl_id: "ENSG00000186193"
name: "suppressor APC domain containing 2"
location: "9q34.3"
module: 22
arm: "+"
pooled_cpm: 17.45
n_lines_expressing: 47
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 14
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# SAPCD2

*suppressor APC domain containing 2* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.35× (z +8.6, q 4e-15, up in 33 of 34 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Peretinoin (drug)]] 0.05 µM: 1.79× (z +3.4, q 0.040, up in 19 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 7.35×, KATO III 8.37×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-172 10.2×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 7.30×).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.436× (z -4.9, q 5e-04, down in 31 of 42 measured lines) ⚠ cell-cycle shift, explains ~56% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.279× (z -4.2, q 0.007, down in 30 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNF]] (+0.79, fdr 7e-06), [[PSRC1]] (+0.76, fdr 7e-06), [[CDC20]] (+0.75, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); 14 go from it, the strongest it → [[MKI67]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11790.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 7.35×, KATO III 8.37×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-172 10.2×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 7.30×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **4.35×** | +8.6 | 4e-15 | 33/34 (A-172, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **3.91×** | +8.3 | 4e-14 | 22/25 (A-172, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.75×** | +6.4 | 4e-08 | 31/44 (A-172, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.63×** | +6.1 | 2e-07 | 32/44 (Hs 766T, RKO, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **2.48×** | +5.7 | 1e-06 | 36/40 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.34×** | +5.0 | 7e-05 | 21/29 (A-172, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.62×** | +4.3 | 0.002 | 31/45 (CFPAC-1, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.93×** | +4.1 | 0.003 | 23/44 (A-172, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | **1.89×** | +3.8 | 0.008 | 23/39 (A-172, SW48, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.79×** | +3.4 | 0.040 | 19/44 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.40× | +3.0 | 0.13 | 21/45 (HT-29, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11790.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.436×** | -4.9 | 5e-04 | 31/42 (SNU-1, SW480, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.279×** | -4.2 | 0.007 | 30/42 (HCT15, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.551×** | -3.7 | 0.033 | 30/45 (SW1417, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.670×** | -3.6 | 0.039 | 26/45 (Hs 766T, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.570×** | -3.5 | 0.039 | 22/42 (SNU-1, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.558×** | -3.5 | 0.039 | 26/43 (A-427, NCI-H1573, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.557×** | -3.4 | 0.048 | 24/44 (A549, NCI-H1573, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.584×** | -3.4 | 0.050 | 22/44 (LS 180, A-172, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.378×** | -3.2 | 0.086 | 25/44 (SW480, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.614× | -3.1 | 0.12 | 17/44 (LS 180, LoVo, …) | top dose only | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.597× | -3.0 | 0.14 | 17/44 (SW480, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +1.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11790. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 30.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 10.2× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.170× (z -9.0) ⚠ cell-cycle shift, explains ~68% of this change |
| [[C-33 A (line)]] | alt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0730× (z -9.1) |
| [[COLO 205 (line)]] | alt | 9.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.30× (z +8.8) | — |
| [[H4 (line)]] | wt | 12.0 | 0 | 1 | — | [[Amsacrine (drug)]] 0.5 µM 0.0204× (z -10.8) |
| [[KATO III (line)]] | alt | 27.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.37× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SNU-1 (line)]] | wt | 26.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0573× (z -11.0) |
| [[A-427 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.30 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.09 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 34.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11790), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNF]] | +0.79 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[PSRC1]] | +0.76 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[CDC20]] | +0.75 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[CDKN3]] | +0.74 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[DLGAP5]] | +0.74 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[CDCA8]] | +0.73 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[PTTG1]] | +0.73 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[CENPF]] | +0.73 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[HJURP]] | +0.73 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[CDCA2]] | +0.72 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[PIMREG]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 | STRING 438 |
| [[CENPE]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises SAPCD2's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.00× lower at baseline in the lines without PIMREG | 0.093 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers SAPCD2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises SAPCD2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FAM72D]] | C | FAM72D activity raises SAPCD2's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.05× lower at baseline in the lines without FAM72D | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 0, C 14. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MKI67]] | C | SAPCD2 activity raises MKI67's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.79× lower at baseline in the lines without SAPCD2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |
| [[CDKN3]] | C | SAPCD2 activity raises CDKN3's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.46× lower at baseline in the lines without SAPCD2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |
| [[KIF4A]] | C | SAPCD2 activity raises KIF4A's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.30× lower at baseline in the lines without SAPCD2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |
| [[CEP55]] | C | SAPCD2 activity raises CEP55's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.20× lower at baseline in the lines without SAPCD2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |
| [[TACC3]] | C | SAPCD2 activity raises TACC3's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.17× lower at baseline in the lines without SAPCD2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |
| [[ERCC6L]] | C | SAPCD2 activity raises ERCC6L's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.38× lower at baseline in the lines without SAPCD2 | 0.067 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent |
| [[CENPI]] | C | SAPCD2, [[SHMT1]] activity raises CENPI's level | lines that do not express SAPCD2, SHMT1 (3) vs lines expressing them (47) | 2.39× lower at baseline in the lines without SAPCD2, SHMT1 | 0.068 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; co-absent genes |
| [[CCNB1]] | C | SAPCD2 activity raises CCNB1's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.59× lower at baseline in the lines without SAPCD2 | 0.073 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent |
| [[INCENP]] | C | SAPCD2 activity raises INCENP's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.09× lower at baseline in the lines without SAPCD2 | 0.073 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent |
| [[KIF20A]] | C | SAPCD2 activity raises KIF20A's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.58× lower at baseline in the lines without SAPCD2 | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent |
| [[LMNB1]] | C | SAPCD2, [[SHMT1]] activity raises LMNB1's level | lines that do not express SAPCD2, SHMT1 (3) vs lines expressing them (47) | 2.92× lower at baseline in the lines without SAPCD2, SHMT1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p; co-absent genes |
| [[TOP2A]] | C | SAPCD2 activity raises TOP2A's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.80× lower at baseline in the lines without SAPCD2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.6, -58.9); signed map (-51.0, -40.6). **Vector** length 79.8, 23.2% of its response variance represented; |z| ≥ 3 in 805 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.57 to 60); *DREAM G2/M down* (control, mean cos +0.65 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.52 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +3.7 | +4.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.6 | +6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.2 | +6.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +2.8 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.7 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.7 | +2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +1.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | -4.7 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -4.2 | -3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.0 | +1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -2.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.7 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -1.5 | -0.4 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -1.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | suppressor APC domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,062,127-137,070,557 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p42.3; previously C9orf140 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UD0](https://www.uniprot.org/uniprotkb/Q86UD0) (Suppressor APC domain-containing protein 2):

> Plays a role in planar mitotic spindle orientation in retinal progenitor cells (RPCs) and promotes the production of symmetric terminal divisions (By similarity). Negatively regulates the mitotic apical cortex localization of GPSM2. Involved also in positive regulation of cell proliferation and tumor cell growth.

**Summary**, from NCBI Gene [89958](https://www.ncbi.nlm.nih.gov/gene/89958):

> Involved in negative regulation of protein localization to cell cortex and positive regulation of cell population proliferation. Located in several cellular components, including apical cortex; apical junction complex; and nuclear lumen. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28055](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28055) · Entrez [89958](https://www.ncbi.nlm.nih.gov/gene/89958) · UniProt [Q86UD0](https://www.uniprot.org/uniprotkb/Q86UD0) · Ensembl [ENSG00000186193](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186193)

## Data

Gene col 11790: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11790); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11790, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11790]; `tensor/DDL_lfc|DDL_z.npy` [11790]; `embed/gene_vectors.npy` [11790]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11790 or target_col == 11790). Every well: [[SAPCD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAPCD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
