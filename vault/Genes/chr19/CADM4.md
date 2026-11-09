---
symbol: "CADM4"
type: "gene"
col: 2662
ensembl_id: "ENSG00000105767"
name: "cell adhesion molecule 4"
location: "19q13.31"
module: 161
arm: "+"
pooled_cpm: 6.52
n_lines_expressing: 45
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# CADM4

*cell adhesion molecule 4* — 19q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 6.09× (z +24.8, q 0e+00, up in 41 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.794× (z -4.5, q 0.004, down in 14 of 42 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.763× (z -3.7, q 0.027, down in 12 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 1 line (RKO 0.0879×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW48 0.0885×); [[Pimitespib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0729×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FCHO1]] (+0.70, fdr 2e-05), [[ATP1A3]] (+0.65, fdr 9e-05), [[BCAM]] (+0.63, fdr 4e-05); moves opposite to [[DDX59]] (-0.62, fdr 1e-04), [[SENP8]] (-0.61, fdr 2e-04), [[RNF146]] (-0.61, fdr 3e-04).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SEMA3F]] → it (grade B ⚠); 4 go from it, the strongest it → [[PRDX6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2662.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **6.09×** | +24.8 | 0e+00 | 41/42 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **4.66×** | +21.1 | 0e+00 | 39/42 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.81×** | +18.4 | 0e+00 | 38/42 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.58×** | +17.5 | 0e+00 | 22/27 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.49×** | +16.5 | 0e+00 | 11/11 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +11.2 | 4e-27 | 26/42 (HT-29, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.15×** | +10.5 | 8e-24 | 31/42 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +9.3 | 8e-19 | 13/17 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.87×** | +8.6 | 4e-16 | 20/41 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.61×** | +6.5 | 4e-09 | 20/40 (AsPC-1, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.30×** | +6.0 | 1e-07 | 10/41 (SW480, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +5.8 | 3e-07 | 16/40 (SW480, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **1.38×** | +4.4 | 4e-04 | 6/25 (A498, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.2 | 0.001 | 11/39 (HepG2/C3A, AsPC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.21×** | +3.7 | 0.008 | 12/35 (SW480, SK-MEL-2, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.023 | 7/33 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.4 | 0.023 | 5/43 (A-172, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Levobupivacaine (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.050 | 3/41 (HOP62, LoVo, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.35×** | +2.9 | 0.085 | 4/36 (LoVo, SW1417, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2662.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 1 line (RKO 0.0879×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW48 0.0885×); [[Pimitespib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0729×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.794×** | -4.5 | 0.004 | 14/42 (J82, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.731×** | -4.3 | 0.005 | 7/42 (HEC-1-A, SW 900, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -3.9 | 0.016 | 10/43 (NCI-H661, SHP-77, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.763×** | -3.7 | 0.027 | 12/42 (A-427, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.786× | -3.3 | 0.10 | 6/41 (HCT15, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.790× | -3.2 | 0.10 | 10/41 (HCT15, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.794× | -3.2 | 0.10 | 7/41 (A-427, CFPAC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.794× | -3.2 | 0.10 | 12/39 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.851× | -3.2 | 0.10 | 8/41 (Panc 03.27, BT-474, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.855× | -3.1 | 0.13 | 5/42 (AsPC-1, A498, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2662. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +11.8) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.42× (z +8.7) | — |
| [[A-172 (line)]] | wt | 27.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +10.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 3.19 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 18.9× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 5.89 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 12.0× (z +10.0) | — |
| [[BT-474 (line)]] | alt | 9.69 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.125× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 4.64 | 0 | 1 | — | [[Pimitespib (drug)]] 0.05 µM 0.0729× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 5.00 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.122× (z -9.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 8.81 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0879× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +10.6) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[SW1417 (line)]] | alt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.59× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0885× (z -9.6) |
| [[A-427 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2662), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHO1]] | +0.70 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ATP1A3]] | +0.65 | +0.37 / +0.56 | both halves | 9e-05 |  |
| [[BCAM]] | +0.63 | +0.42 / +0.54 | both halves | 4e-05 | same gene group |
| [[ANKDD1A]] | +0.63 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[SHF]] | +0.63 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[SEMA3F]] | +0.62 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[KCTD17]] | +0.62 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[GDF11]] | +0.62 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[AFAP1]] | +0.62 | +0.51 / +0.32 | both halves | 2e-04 |  |
| [[LMTK3]] | +0.61 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[SIPA1]] | +0.61 | +0.38 / +0.42 | both halves | 6e-05 |  |
| [[GPRIN1]] | +0.61 | +0.36 / +0.47 | both halves | 1e-04 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX59]] | -0.62 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[SENP8]] | -0.61 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[RNF146]] | -0.61 | -0.28 / -0.41 | both halves | 3e-04 |  |
| [[PAAF1]] | -0.60 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[KLHL42]] | -0.60 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[FAIM]] | -0.59 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[DICER1-AS1]] | -0.59 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[NNT-AS1]] | -0.59 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[SPRY3]] | -0.58 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[POLR3C]] | -0.58 | -0.23 / -0.40 | both halves | 5e-04 |  |
| [[DHRS4-AS1]] | -0.58 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[ANGEL2]] | -0.57 | -0.44 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA3F]] | B | SEMA3F activity raises CADM4's level | lines that do not express SEMA3F (6) vs lines expressing it (44) | 2.22× lower at baseline in the lines without SEMA3F | 0.050 | ⚠ within organs, on part of the lines; also absent: MCM2, PIMREG, GKAP1 |
| [[FCHO1]] | B | FCHO1 activity raises CADM4's level | lines that do not express FCHO1 (5) vs lines expressing it (45) | 2.47× lower at baseline in the lines without FCHO1 | 0.074 | ⚠ within organs, on part of the lines; also absent: AMOTL2; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRDX6]] | B | CADM4 activity raises PRDX6's level | lines that do not express CADM4 (5) vs lines expressing it (45) | 1.26× lower at baseline in the lines without CADM4 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[CCDC122]] | B | CADM4 activity lowers CCDC122's level | lines that do not express CADM4 (5) vs lines expressing it (45) | 1.88× higher at baseline in the lines without CADM4 | 0.083 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TMEM184B]] | B | CADM4 activity raises TMEM184B's level | lines that do not express CADM4 (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without CADM4 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[ACAP3]] | B | CADM4 activity raises ACAP3's level | lines that do not express CADM4 (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without CADM4 | 0.093 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.5, 1.0); signed map (-22.1, 29.4). **Vector** length 59.4, 8.25% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +11.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +24.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +21.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +8.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.7 | +18.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +6.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +1.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.6 | -4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +1.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.7 | -1.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.5 | -3.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cell adhesion molecule 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.31 — chr19:43,622,368-43,639,850 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TSLL2, Necl-4, SynCAM4; previously IGSF4C |
| Gene groups (HGNC) | V-set domain containing; C2-set domain containing; Nectins and nectin-like molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFZ8](https://www.uniprot.org/uniprotkb/Q8NFZ8) (Cell adhesion molecule 4):

> Cell adhesion molecule, exhibiting calcium- and magnesium-independent cell-cell adhesion activity. In its palmitoylated form, is required for proper oligodendrocyte maturation and myelination in CNS via its association with other cell adhesion molecules such as CADM2/3 and MAG (By similarity). May have tumor-suppressor activity.

**Summary**, from NCBI Gene [199731](https://www.ncbi.nlm.nih.gov/gene/199731):

> Enables vascular endothelial growth factor receptor 2 binding activity. Involved in several processes, including negative regulation of protein phosphorylation; regulation of Rac protein signal transduction; and regulation of wound healing. Located in cell leading edge and cell-cell contact zone. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30825](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30825) · Entrez [199731](https://www.ncbi.nlm.nih.gov/gene/199731) · UniProt [Q8NFZ8](https://www.uniprot.org/uniprotkb/Q8NFZ8) · Ensembl [ENSG00000105767](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105767)

## Data

Gene col 2662: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2662); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2662, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2662]; `tensor/DDL_lfc|DDL_z.npy` [2662]; `embed/gene_vectors.npy` [2662]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2662 or target_col == 2662). Every well: [[CADM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CADM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
