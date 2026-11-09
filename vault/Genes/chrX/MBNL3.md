---
symbol: "MBNL3"
type: "gene"
col: 1163
ensembl_id: "ENSG00000076770"
name: "muscleblind like splicing regulator 3"
location: "Xq26.2"
module: 2
arm: "-"
pooled_cpm: 10.27
n_lines_expressing: 34
n_dd_up: 16
n_dd_down: 14
n_dd_up_clean: 13
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 10
direction_downstream: 15
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# MBNL3

*muscleblind like splicing regulator 3* — Xq26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.05× (z +14.8, q 0e+00, up in 9 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.74× (z +14.4, q 2e-44, up in 26 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.550× (z -6.6, q 2e-08, down in 19 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX5]] (+0.66, fdr 1e-05), [[PNPO]] (+0.65, fdr 7e-06), [[TMEM123]] (+0.65, fdr 7e-06); moves opposite to [[ZNF611]] (-0.66, fdr 1e-05), [[TECPR1]] (-0.65, fdr 2e-05), [[KCTD21]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[MGC32805]] → it (grade B ⚠); 15 go from it, the strongest it → [[SH3BGRL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1163.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.05×** | +14.8 | 0e+00 | 9/9 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.74×** | +14.4 | 2e-44 | 26/29 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.49×** | +13.8 | 6e-41 | 19/21 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.77×** | +10.4 | 5e-23 | 11/13 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +7.6 | 4e-12 | 21/28 (SW480, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +6.2 | 5e-08 | 18/27 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.75×** | +6.2 | 5e-08 | 16/29 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.9 | 2e-07 | 11/31 (SW480, A498, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.56×** | +4.7 | 2e-04 | 7/30 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +4.2 | 0.001 | 11/31 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.42×** | +3.9 | 0.006 | 7/30 (HepG2/C3A, AsPC-1, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.010 | 9/31 (LS 180, SK-MEL-2, …) | rises with dose |  |
| [[Alpelisib (drug)]] 0.5 µM |  | **1.49×** | +3.1 | 0.081 | 2/31 (A498, SW480) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.081 | 6/30 (CFPAC-1, SW480, …) | all doses, flat |  |
| [[Erlotinib (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.081 | 5/30 (COLO 205, C-33 A, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.083 | 4/30 (KATO III, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1163.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.550×** | -6.6 | 2e-08 | 19/31 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.561×** | -6.4 | 5e-08 | 18/30 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.577×** | -6.1 | 2e-07 | 17/30 (HepG2/C3A, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.593×** | -5.8 | 1e-06 | 17/30 (LS 180, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.685×** | -5.4 | 7e-06 | 16/30 (HepG2/C3A, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.627×** | -5.2 | 2e-05 | 16/30 (SHP-77, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.625×** | -4.9 | 8e-05 | 16/30 (HepG2/C3A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.668×** | -4.5 | 6e-04 | 8/31 (HepG2/C3A, LS 180, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.685×** | -4.2 | 0.002 | 15/30 (HepG2/C3A, LS 180, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.715×** | -3.7 | 0.012 | 11/31 (SW48, RKO, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.714×** | -3.6 | 0.017 | 12/30 (HepG2/C3A, HT-29, …) | all doses, flat |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.648×** | -3.4 | 0.030 | 10/30 (HepG2/C3A, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.669×** | -3.2 | 0.064 | 15/30 (HT-29, LS 180, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.670×** | -3.2 | 0.064 | 13/28 (A498, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1163. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 305 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -21.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.167× (z -12.5) |
| [[LS 180 (line)]] | wt | 32.4 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +8.8) | [[Ixazomib citrate (drug)]] 5 µM 0.137× (z -13.2) |
| [[SW480 (line)]] | alt | 14.6 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.195× (z -9.8) |
| [[COLO 205 (line)]] | alt | 18.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0352× (z -15.0) |
| [[A-427 (line)]] | wt | 4.19 | 0 | 1 | — | [[Aspirin (drug)]] 0.5 µM 0.0676× (z -9.8) |
| [[A498 (line)]] | wt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 18.8 | 0 | 1 | — | [[vincristine (drug)]] 0.5 µM 0.0776× (z -9.3) |
| [[LoVo (line)]] | wt | 7.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 13.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.56× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 13.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.116× (z -9.5) |
| [[SW48 (line)]] | wt | 20.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.121× (z -9.1) |
| [[A-172 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.806 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.892 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.955 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.841 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.972 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.819 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 8.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1163), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX5]] | +0.66 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[PNPO]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[TMEM123]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[CHRAC1]] | +0.62 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[TMPO]] | +0.62 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[MOB1A]] | +0.61 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[FUCA2]] | +0.61 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[SLC12A2-DT]] | +0.61 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[RCC2]] | +0.60 | +0.56 / +0.39 | both halves | 6e-05 |  |
| [[CRPPA]] | +0.60 | +0.44 / +0.40 | both halves | 5e-05 |  |
| [[SUMO3]] | +0.60 | +0.37 / +0.47 | both halves | 7e-05 |  |
| [[MYB]] | +0.60 | +0.65 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF611]] | -0.66 | -0.54 / -0.71 | both halves | 1e-05 |  |
| [[TECPR1]] | -0.65 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[KCTD21]] | -0.65 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[SAMD4B]] | -0.64 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[PLIN3]] | -0.64 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[VRK3]] | -0.63 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[ATG4B]] | -0.62 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[TMEM184B]] | -0.61 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[SUGP1]] | -0.61 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[UBE2B]] | -0.60 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[RPL36AL]] ⚠ | -0.60 | -0.44 / -0.64 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NOL7]] ⚠ | -0.60 | -0.40 / -0.53 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[POLR2J4]] | -0.60 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[NOSIP]] | -0.60 | -0.43 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MGC32805]] | B | MGC32805 activity raises MBNL3's level | lines that do not express MGC32805 (32) vs lines expressing it (18) | 1.95× lower at baseline in the lines without MGC32805 | 0.004 | ⚠ within organs, on part of the lines; also absent: CEACAM5, ST18, PRR15L; maybe low, not absent |
| [[GRHL2]] | B | GRHL2 activity raises MBNL3's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 2.13× lower at baseline in the lines without GRHL2 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[TOP2A]] | B | TOP2A activity lowers MBNL3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[S100A14]] | B | S100A14 activity raises MBNL3's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 2.66× lower at baseline in the lines without S100A14 | 0.018 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |
| [[HSD11B2]] | B | HSD11B2 activity raises MBNL3's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 2.44× lower at baseline in the lines without HSD11B2 | 0.051 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |
| [[HNF1A]] | B | HNF1A activity raises MBNL3's level | lines that do not express HNF1A (30) vs lines expressing it (20) | 2.76× lower at baseline in the lines without HNF1A | 0.062 | ⚠ within organs, on part of the lines; also absent: HNF1A-AS1, GPX2, HNF4A; maybe low, not absent |
| [[MEIS3]] | B | MEIS3 activity lowers MBNL3's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 1.15× higher at baseline in the lines without MEIS3 | 0.065 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| [[ESRP2]] | B | ESRP2 activity raises MBNL3's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 2.30× lower at baseline in the lines without ESRP2 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |
| [[SH3BGRL2]] | B | SH3BGRL2 activity raises MBNL3's level | lines that do not express SH3BGRL2 (16) vs lines expressing it (34) | 2.44× lower at baseline in the lines without SH3BGRL2 | 0.089 | ⚠ within organs, on part of the lines; also absent: LSR, HOOK1, SMPDL3B; maybe low, not absent |
| [[TNNT1]] | B | TNNT1 activity lowers MBNL3's level | lines that do not express TNNT1 (9) vs lines expressing it (41) | 2.70× higher at baseline in the lines without TNNT1 | 0.093 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, HDAC9; maybe low, not absent |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH3BGRL2]] | B | MBNL3 activity raises SH3BGRL2's level | lines that do not express MBNL3 (16) vs lines expressing it (34) | 3.53× lower at baseline in the lines without MBNL3 | 0.001 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| [[C5orf15]] | B | MBNL3 activity lowers C5orf15's level | lines that do not express MBNL3 (16) vs lines expressing it (34) | 1.22× higher at baseline in the lines without MBNL3 | 0.038 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| [[S100A14]] | B | MBNL3 activity raises S100A14's level | lines that do not express MBNL3 (16) vs lines expressing it (34) | 2.78× lower at baseline in the lines without MBNL3 | 0.043 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| [[PPP2R5B]] | B | MBNL3 activity lowers PPP2R5B's level | lines that do not express MBNL3 (16) vs lines expressing it (34) | 1.41× higher at baseline in the lines without MBNL3 | 0.046 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| [[ZNF165]] | B | MBNL3 activity raises ZNF165's level | lines that do not express MBNL3 (16) vs lines expressing it (34) | 2.24× lower at baseline in the lines without MBNL3 | 0.061 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| cells under [[Imiquimod (hydrochloride) (drug)]] 5 µM | B | MBNL3 activity raises the cells' numbers under Imiquimod (hydrochloride) 5 µM (protects the cells) | lines that do not express MBNL3 (16) vs lines expressing it (32) | the lines without MBNL3: 0.83× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| [[PEG10]] | B | MBNL3 activity raises PEG10's level | lines that do not express MBNL3 (16) vs lines expressing it (34) | 1.60× lower at baseline in the lines without MBNL3 | 0.073 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| [[RPS6KC1]] | B | MBNL3 activity lowers RPS6KC1's level | lines that do not express MBNL3 (16) vs lines expressing it (34) | 1.33× higher at baseline in the lines without MBNL3 | 0.080 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| cells under [[Furosemide (drug)]] 0.5 µM | B | MBNL3 activity raises the cells' numbers under Furosemide 0.5 µM (protects the cells) | lines that do not express MBNL3 (16) vs lines expressing it (32) | the lines without MBNL3: 0.86× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| [[GRHL2]] | B | MBNL3 activity raises GRHL2's level | lines that do not express MBNL3 (16) vs lines expressing it (34) | 3.44× lower at baseline in the lines without MBNL3 | 0.081 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| cells under [[Canagliflozin (drug)]] 5 µM | B | MBNL3 activity raises the cells' numbers under Canagliflozin 5 µM (protects the cells) | lines that do not express MBNL3 (16) vs lines expressing it (32) | the lines without MBNL3: 0.86× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| [[GRIN2D]] | B | MBNL3 activity raises GRIN2D's level | lines that do not express MBNL3 (16) vs lines expressing it (34) | 2.39× lower at baseline in the lines without MBNL3 | 0.092 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **-** arm (projection on the module's main direction -0.305). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (2.5, 1.3); signed map (-18.5, -40.2). **Vector** length 77.6, 19.1% of its response variance represented; |z| ≥ 3 in 666 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +13.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +14.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +4.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +3.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -6.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -5.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.4 | -5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.4 | -4.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.4 | -6.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.8 | -4.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -6.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | muscleblind like splicing regulator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.2 — chrX:132,369,320-132,489,968 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CHCR, FLJ11316, MBLX39, MBXL |
| Gene groups (HGNC) | Zinc fingers CCCH-type; Muscleblind like splicing regulator family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUK0](https://www.uniprot.org/uniprotkb/Q9NUK0) (Muscleblind-like protein 3):

> Mediates pre-mRNA alternative splicing regulation. Acts either as activator or repressor of splicing on specific pre-mRNA targets. Inhibits cardiac troponin-T (TNNT2) pre-mRNA exon inclusion but induces insulin receptor (IR) pre-mRNA exon inclusion in muscle. Antagonizes the alternative splicing activity pattern of CELF proteins. May play a role in myotonic dystrophy pathophysiology (DM). Could inhibit terminal muscle differentiation, acting at approximately the time of myogenin induction.

**Summary**, from NCBI Gene [55796](https://www.ncbi.nlm.nih.gov/gene/55796):

> This gene encodes a member of the muscleblind-like family of proteins. The encoded protein may function in regulation of alternative splicing and may play a role in the pathophysiology of myotonic dystrophy. Alternatively spliced transcript variants have been described. [provided by RefSeq, Dec 2009]

**Accessions** — [HGNC:20564](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20564) · Entrez [55796](https://www.ncbi.nlm.nih.gov/gene/55796) · UniProt [Q9NUK0](https://www.uniprot.org/uniprotkb/Q9NUK0) · Ensembl [ENSG00000076770](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076770)

## Data

Gene col 1163: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1163); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1163, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1163]; `tensor/DDL_lfc|DDL_z.npy` [1163]; `embed/gene_vectors.npy` [1163]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1163 or target_col == 1163). Every well: [[MBNL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MBNL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
