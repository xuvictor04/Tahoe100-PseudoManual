---
symbol: "FAM106A"
type: "gene"
col: 15758
ensembl_id: "ENSG00000273018"
name: "family with sequence similarity 106 member A"
location: "17p11.2"
module: 108
arm: "+"
pooled_cpm: 5.6
n_lines_expressing: 20
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# FAM106A

*family with sequence similarity 106 member A* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.47× (z +13.8, q 7e-41, up in 1 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.82× (z +5.0, q 7e-05, up in 1 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.688× (z -4.3, q 0.010, down in 9 of 17 measured lines).
> Its strongest partners by |cos| (79 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IHO1]] (+0.57, fdr 2e-05), [[CCNYL2]] (+0.53, fdr 5e-05), [[GLIS1]] (+0.48, fdr 1e-04); moves opposite to [[C2orf76]] (-0.53, fdr 9e-05), [[CCNO-DT]] (-0.49, fdr 2e-04), [[LINC00534]] (-0.49, fdr 2e-04).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CCDC144BP]] → it (grade C ⚠); 3 go from it, the strongest it → [[USP34-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15758.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.47×** | +13.8 | 7e-41 | 1/8 (SHP-77) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.81×** | +11.0 | 7e-26 | 1/10 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.44×** | +10.3 | 8e-23 | 1/15 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.04×** | +5.9 | 5e-07 | 0/11 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.35×** | +5.0 | 7e-05 | 9/16 (A498, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.82×** | +5.0 | 7e-05 | 1/13 (SHP-77) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +4.3 | 0.001 | 11/17 (HT-29, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.48×** | +4.2 | 0.002 | 11/16 (SHP-77, A498, …) | inconsistent across doses | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.41×** | +4.0 | 0.004 | 2/14 (Panc 03.27, SW 900) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Folic acid (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.012 | 2/17 (A-172, HOP62) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +3.4 | 0.035 | 0/8 | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +3.4 | 0.037 | 0/10 | top dose only | noisy plate (z scaled) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.066 | 2/15 (AN3 CA, SW 900) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15758.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.688×** | -4.3 | 0.010 | 9/17 (LOX-IMVI, A498, …) | two highest doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.692×** | -3.9 | 0.027 | 1/16 (HOP62) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.730×** | -3.6 | 0.059 | 8/16 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 0.745× | -3.4 | 0.10 | 0/17 | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.755× | -3.2 | 0.12 | 1/17 (CHP-212) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | 0.748× | -3.2 | 0.12 | 1/16 (AN3 CA) | top dose only | plate-row cell shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.757× | -3.2 | 0.12 | 1/17 (CHP-212) | top dose only |  |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.762× | -3.1 | 0.13 | 3/16 (AN3 CA, A498, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | 0.767× | -3.0 | 0.15 | 1/16 (LOX-IMVI) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15758. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 30.5 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 20.1 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 13.8 | 0 | 2 (1 ⚠) | — | [[Simotinib (drug)]] 0.05 µM 0.142× (z -8.9) |
| [[A-172 (line)]] | wt | 16.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -12.2) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 9.16 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0924× (z -9.5) ⚠ transcription drop |
| [[HS-578T (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.881 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.777 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.610 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.507 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.735 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.534 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.629 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.888 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.547 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.608 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.934 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.629 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.559 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15758), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IHO1]] | +0.57 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[CCNYL2]] | +0.53 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[GLIS1]] | +0.48 | +0.47 / +0.35 | both halves | 1e-04 |  |
| [[JAKMIP2]] | +0.47 | +0.51 / +0.35 | both halves | 1e-04 |  |
| [[ADAMTS2]] | +0.47 | +0.30 / +0.51 | both halves | 2e-04 |  |
| [[PREX2]] | +0.46 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[BICC1]] | +0.45 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[EVC]] | +0.45 | +0.26 / +0.49 | both halves | 4e-04 |  |
| [[APBB1IP]] | +0.45 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[CCDC144BP]] | +0.45 | +0.36 / +0.48 | both halves | 9e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[LINC01446]] | +0.44 | +0.34 / +0.33 | both halves | 1e-04 |  |
| [[COX7B2]] | +0.43 | +0.35 / +0.38 | both halves | 1e-04 |  |
| [[MSC-AS1]] | +0.43 | +0.41 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 17 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2orf76]] | -0.53 | -0.37 / -0.42 | both halves | 9e-05 |  |
| [[CCNO-DT]] | -0.49 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[LINC00534]] | -0.49 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[KANSL1]] | -0.48 | -0.23 / -0.36 | both halves | 5e-04 |  |
| [[DLEU7]] | -0.48 | -0.32 / -0.38 | both halves | 1e-04 |  |
| [[HOXC9]] | -0.46 | -0.19 / -0.33 | ⚠ not reproduced | 8e-04 |  |
| [[KLF3-AS1]] | -0.45 | -0.26 / -0.31 | both halves | 4e-04 |  |
| [[SLC12A9]] | -0.44 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[CCDC115]] | -0.44 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[SYT17]] | -0.44 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[INHA]] | -0.42 | -0.22 / -0.36 | both halves | 6e-04 |  |
| [[CHD6]] | -0.42 | -0.41 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[DNASE1]] | -0.42 | -0.26 / -0.28 | both halves | 4e-04 |  |
| [[MGST2]] | -0.42 | -0.28 / -0.34 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC144BP]] | C | CCDC144BP activity raises FAM106A's level | lines that do not express CCDC144BP (23) vs lines expressing it (27) | 4.36× lower at baseline in the lines without CCDC144BP | 6e-04 | ⚠ within organs, on part of the lines; also absent: FAM106A, ENSG00000266302, CCDC144A; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[USP34-DT]] | B | FAM106A activity lowers USP34-DT's level | lines that do not express FAM106A (30) vs lines expressing it (20) | 1.26× higher at baseline in the lines without FAM106A | 0.097 | ⚠ within organs, on part of the lines; also absent: CCDC144BP, SULF1, POSTN |
| [[CCDC144BP]] | C | FAM106A activity raises CCDC144BP's level | lines that do not express FAM106A (30) vs lines expressing it (20) | 7.20× lower at baseline in the lines without FAM106A | 3e-04 | ⚠ within organs, on part of the lines; also absent: CCDC144BP, SULF1, POSTN; co-absent with the target |
| [[JAKMIP2]] | C | FAM106A activity raises JAKMIP2's level | lines that do not express FAM106A (30) vs lines expressing it (20) | 2.47× lower at baseline in the lines without FAM106A | 0.061 | ⚠ within organs, on part of the lines; also absent: CCDC144BP, SULF1, POSTN; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.458). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (50.4, 24.0); signed map (31.3, 45.9). **Vector** length 32.4, 6.63% of its response variance represented; |z| ≥ 3 in 355 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +11.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.4 | +2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.2 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.6 | -0.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +0.5 | +1.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +0.5 | +0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.4 | +0.0 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.1 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.0 | -2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | -1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.6 | -0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -0.6 | -0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.6 | -0.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 106 member A |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17p11.2 — chr17:18,511,221-18,551,705 (-) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ11800 |
| Gene groups (HGNC) | Long non-coding RNAs with FAM root symbol |
| Matched by | ensembl_id |

UniProt [Q4KMX7](https://www.uniprot.org/uniprotkb/Q4KMX7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25682](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25682) · Entrez [80039](https://www.ncbi.nlm.nih.gov/gene/80039) · UniProt [Q4KMX7](https://www.uniprot.org/uniprotkb/Q4KMX7) · Ensembl [ENSG00000273018](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000273018)

## Data

Gene col 15758: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15758); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15758, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15758]; `tensor/DDL_lfc|DDL_z.npy` [15758]; `embed/gene_vectors.npy` [15758]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15758 or target_col == 15758). Every well: [[FAM106A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM106A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
