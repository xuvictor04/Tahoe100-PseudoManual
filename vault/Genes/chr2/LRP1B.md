---
symbol: "LRP1B"
type: "gene"
col: 9686
ensembl_id: "ENSG00000168702"
name: "LDL receptor related protein 1B"
location: "2q22.1-q22.2"
module: 117
arm: "+"
pooled_cpm: 51.05
n_lines_expressing: 26
n_dd_up: 44
n_dd_down: 6
n_dd_up_clean: 37
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# LRP1B

*LDL receptor related protein 1B* — 2q22.1-q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.66× (z +17.7, q 0e+00, up in 12 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.717× (z -4.3, q 0.006, down in 7 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNT2]] (+0.75, fdr 7e-06), [[ALOX12P2-1]] (+0.70, fdr 7e-06), [[ZSCAN31]] (+0.69, fdr 9e-06); moves opposite to [[ZHX3]] (-0.60, fdr 1e-05), [[SOCS7]] (-0.55, fdr 3e-05), [[OSTF1]] (-0.55, fdr 1e-04).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CYP39A1]] → it (grade B ⚠); 4 go from it, the strongest it → [[UNC5C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9686.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.66×** | +17.7 | 0e+00 | 12/24 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +11.1 | 6e-26 | 8/22 (LOX-IMVI, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +11.0 | 9e-26 | 17/23 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.45×** | +10.8 | 5e-25 | 19/23 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.06×** | +9.2 | 4e-18 | 13/24 (LOX-IMVI, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +8.8 | 8e-17 | 6/20 (RPMI-7951, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +8.6 | 5e-16 | 13/23 (HOP62, J82, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +8.1 | 5e-14 | 12/24 (J82, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.92×** | +7.7 | 8e-13 | 10/21 (BT-474, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.79×** | +7.4 | 8e-12 | 18/23 (HOP62, J82, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.75×** | +7.1 | 5e-11 | 17/23 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.81×** | +6.9 | 2e-10 | 16/19 (HOP62, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +6.0 | 1e-07 | 12/23 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.1 | 1e-05 | 5/25 (J82, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.67×** | +4.7 | 1e-04 | 10/25 (HOP62, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.46×** | +4.7 | 1e-04 | 10/23 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +4.5 | 2e-04 | 17/22 (NCI-H460, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +4.2 | 7e-04 | 14/23 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.1 | 0.001 | 5/22 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9686.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.717×** | -4.3 | 0.006 | 7/23 (NCI-H1573, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.719×** | -4.2 | 0.006 | 14/22 (NCI-H1573, NCI-H23, …) | two highest doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.728×** | -4.1 | 0.008 | 8/23 (NCI-H1573, NCI-H23, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.746×** | -3.8 | 0.023 | 8/23 (NCI-H1573, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.764×** | -3.5 | 0.061 | 10/23 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.772×** | -3.3 | 0.082 | 9/23 (NCI-H1573, Panc 03.27, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | 0.785× | -3.1 | 0.13 | 7/21 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.785× | -3.1 | 0.13 | 8/24 (NCI-H1573, Panc 03.27, …) | rises with dose | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | 0.790× | -3.0 | 0.15 | 7/24 (NCI-H1573, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9686. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 814 | 0 | 9 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0659× (z -19.5) ⚠ toxic; cell-cycle shift, explains ~14% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.207× (z -11.7) |
| [[HOP62 (line)]] | alt | 35.5 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +19.2) | — |
| [[J82 (line)]] | alt | 30.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +19.1) | — |
| [[Panc 03.27 (line)]] | alt | 98.7 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -11.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H460 (line)]] | wt | 48.9 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 7.03× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 34.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +10.7) | — |
| [[hTERT-HPNE (line)]] | wt | 21.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.9× (z +16.8) | — |
| [[SHP-77 (line)]] | alt | 122 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -9.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 22.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 17.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 42.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 49.9 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.87× (z +10.2) ⚠ position not correctable | — |
| [[A-172 (line)]] | wt | 9.06 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.58 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.98 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 213 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.64 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.68 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.06 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.62 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 98.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.13 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.90 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.30 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.73 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.84 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.30 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.19 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.59 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.75 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9686), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNT2]] | +0.75 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[ALOX12P2-1]] | +0.70 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[ZSCAN31]] | +0.69 | +0.71 / +0.57 | both halves | 9e-06 |  |
| [[GNGT1]] | +0.68 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[CAPS2]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[TLR6]] | +0.65 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[GULP1]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[TRIM16L]] | +0.64 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[CLIC2]] | +0.63 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[EPHA5]] | +0.62 | +0.60 / +0.58 | both halves | 7e-06 | STRING 402 |
| [[TLR1]] | +0.62 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[LINC02328]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZHX3]] | -0.60 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[SOCS7]] | -0.55 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[OSTF1]] | -0.55 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[AP1M1]] | -0.54 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[MTMR12]] | -0.54 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[MINK1]] | -0.53 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[SH3GL1]] | -0.51 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[CRLS1]] | -0.51 | -0.56 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP39A1]] | B | CYP39A1 activity raises LRP1B's level | lines that do not express CYP39A1 (14) vs lines expressing it (36) | 1.74× lower at baseline in the lines without CYP39A1 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC25A27, ENSG00000259345; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers LRP1B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UNC5C]] | B | LRP1B activity lowers UNC5C's level | lines that do not express LRP1B (24) vs lines expressing it (26) | 1.10× higher at baseline in the lines without LRP1B | 0.040 | ⚠ within organs, on part of the lines; also absent: GLRB, VEGFC, SPANXA2-OT1; maybe low, not absent |
| [[GULP1]] | B | LRP1B activity lowers GULP1's level | lines that do not express LRP1B (24) vs lines expressing it (26) | 1.10× higher at baseline in the lines without LRP1B | 0.054 | ⚠ within organs, on part of the lines; also absent: GLRB, VEGFC, SPANXA2-OT1; maybe low, not absent |
| [[LINC01122]] | B | LRP1B activity raises LINC01122's level | lines that do not express LRP1B (24) vs lines expressing it (26) | 1.02× lower at baseline in the lines without LRP1B | 0.068 | ⚠ within organs, on part of the lines; also absent: GLRB, VEGFC, SPANXA2-OT1; maybe low, not absent |
| [[TNFRSF11B]] | C | LRP1B activity raises TNFRSF11B's level | lines that do not express LRP1B (24) vs lines expressing it (26) | 2.20× lower at baseline in the lines without LRP1B | 0.062 | ⚠ within organs, on part of the lines; also absent: GLRB, VEGFC, SPANXA2-OT1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.727). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-6.4, 48.1); signed map (50.2, -8.3). **Vector** length 86.7, 26.3% of its response variance represented; |z| ≥ 3 in 722 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.6 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +17.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +4.5 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.4 | -4.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.5 | -3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -2.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.4 | -3.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.4 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | LDL receptor related protein 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q22.1-q22.2 — chr2:140,231,423-142,131,016 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LRP-DIT, LRPDIT |
| Gene groups (HGNC) | Low density lipoprotein receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZR2](https://www.uniprot.org/uniprotkb/Q9NZR2) (Low-density lipoprotein receptor-related protein 1B):

> Potential cell surface proteins that bind and internalize ligands in the process of receptor-mediated endocytosis.

**Summary**, from NCBI Gene [53353](https://www.ncbi.nlm.nih.gov/gene/53353):

> This gene encodes a member of the low density lipoprotein (LDL) receptor family. These receptors play a wide variety of roles in normal cell function and development due to their interactions with multiple ligands. Disruption of this gene has been reported in several types of cancer. [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:6693](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6693) · Entrez [53353](https://www.ncbi.nlm.nih.gov/gene/53353) · UniProt [Q9NZR2](https://www.uniprot.org/uniprotkb/Q9NZR2) · Ensembl [ENSG00000168702](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168702)

## Data

Gene col 9686: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9686); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9686, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9686]; `tensor/DDL_lfc|DDL_z.npy` [9686]; `embed/gene_vectors.npy` [9686]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9686 or target_col == 9686). Every well: [[LRP1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRP1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
