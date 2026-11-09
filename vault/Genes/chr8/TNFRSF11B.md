---
symbol: "TNFRSF11B"
type: "gene"
col: 9005
ensembl_id: "ENSG00000164761"
name: "TNF receptor superfamily member 11b"
location: "8q24.12"
module: 19
arm: "+"
pooled_cpm: 9.94
n_lines_expressing: 24
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 6
direction_downstream: 14
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# TNFRSF11B

*TNF receptor superfamily member 11b* — 8q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.57× (z +11.6, q 4e-28, up in 8 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.85× (z +7.9, q 4e-13, up in 10 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.472× (z -6.8, q 6e-09, down in 17 of 21 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.519× (z -5.7, q 1e-06, down in 10 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C5orf46]] (+0.69, fdr 7e-06), [[SEMA3D]] (+0.67, fdr 7e-06), [[PDE7B]] (+0.62, fdr 7e-06); moves opposite to [[SEC14L2]] (-0.47, fdr 8e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MAP2K2]] → it (grade B ⚠); 14 go from it, the strongest it → [[CASC15]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9005.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.57×** | +11.6 | 4e-28 | 8/17 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.91×** | +9.3 | 3e-18 | 5/12 (J82, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.68×** | +8.3 | 2e-14 | 5/14 (J82, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +7.9 | 4e-13 | 10/21 (A498, NCI-H1792, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +4.2 | 0.003 | 10/21 (A498, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +4.1 | 0.004 | 2/15 (SNU-423, SW1417) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.47×** | +4.0 | 0.005 | 7/22 (NCI-H460, HS-578T, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.076 | 5/21 (NCI-H460, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9005.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.472×** | -6.8 | 6e-09 | 17/21 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.491×** | -6.5 | 3e-08 | 17/21 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.501×** | -6.3 | 7e-08 | 14/21 (SNU-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.519×** | -5.7 | 1e-06 | 10/21 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.620×** | -4.3 | 0.002 | 8/19 (Hs 766T, BT-474, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.627×** | -4.2 | 0.002 | 8/21 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.741×** | -3.8 | 0.010 | 12/22 (BT-474, SHP-77, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.666×** | -3.7 | 0.015 | 8/21 (NCI-H460, Panc 03.27, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.667×** | -3.7 | 0.015 | 13/21 (Hs 766T, NCI-H460, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.670×** | -3.6 | 0.016 | 11/21 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.756×** | -3.6 | 0.018 | 9/21 (Hs 766T, HS-578T, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.676×** | -3.5 | 0.019 | 7/21 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.494×** | -3.3 | 0.036 | 9/22 (SNU-423, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.701×** | -3.2 | 0.052 | 10/21 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.705×** | -3.2 | 0.058 | 6/21 (Hs 766T, NCI-H460, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.785×** | -3.1 | 0.071 | 10/21 (Hs 766T, BT-474, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9005. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 31.0 | 12 (2 ⚠) | 16 (10 ⚠) | [[Trametinib (drug)]] 0.5 µM 7.08× (z +14.2) | [[Homoharringtonine (drug)]] 5 µM 0.0197× (z -32.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.0901× (z -14.1) |
| [[SNU-1 (line)]] | wt | 345 | 0 | 9 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0139× (z -26.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[J82 (line)]] | alt | 27.3 | 3 (3 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 9.41× (z +12.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -9.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 38.6 | 1 (1 ⚠) | 4 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 7.13× (z +9.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 8.16 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 15.8 | 0 | 3 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0599× (z -11.0) ⚠ transcription drop · without an alert: [[Dexamethasone (drug)]] 0.05 µM 0.0965× (z -9.1) |
| [[CHP-212 (line)]] | wt | 24.3 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0281× (z -9.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 13.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0676× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.63 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0562× (z -9.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 14.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.144× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0789× (z -8.5) |
| [[SHP-77 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.135× (z -8.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 0.754 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.819 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.998 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.983 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.952 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.959 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.39 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9005), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C5orf46]] | +0.69 | +0.60 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[SEMA3D]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[PDE7B]] | +0.62 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[CDH11]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[GLP2R]] | +0.60 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[MYPN]] | +0.60 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[RIMS1]] | +0.60 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[SYTL2]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[ZSCAN31]] | +0.59 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[RMDN2-AS1]] | +0.58 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[NKAIN2]] | +0.57 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[NOVA1]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC14L2]] | -0.47 | -0.37 / -0.43 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K2]] | B | MAP2K2 activity lowers TNFRSF11B's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[PTN]] | C | PTN activity raises TNFRSF11B's level | lines that do not express PTN (28) vs lines expressing it (22) | 1.95× lower at baseline in the lines without PTN | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises TNFRSF11B's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 2.34× lower at baseline in the lines without DPP10 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[INHBA]] | C | INHBA activity raises TNFRSF11B's level | lines that do not express INHBA (32) vs lines expressing it (18) | 1.88× lower at baseline in the lines without INHBA | 0.061 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3; co-absent with the target |
| [[LRP1B]] | C | LRP1B activity raises TNFRSF11B's level | lines that do not express LRP1B (24) vs lines expressing it (26) | 2.20× lower at baseline in the lines without LRP1B | 0.062 | ⚠ within organs, on part of the lines; also absent: GLRB, VEGFC, SPANXA2-OT1; maybe low, not absent; co-absent with the target |
| [[LINC01035]] | C | LINC01035 activity raises TNFRSF11B's level | lines that do not express LINC01035 (43) vs lines expressing it (7) | 2.31× lower at baseline in the lines without LINC01035 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, CALCA, GSG1L2; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 4, C 10. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASC15]] | B | TNFRSF11B activity raises CASC15's level | lines that do not express TNFRSF11B (26) vs lines expressing it (24) | 1.90× lower at baseline in the lines without TNFRSF11B | 0.064 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12 |
| [[LINC02466]] | B | TNFRSF11B activity raises LINC02466's level | lines that do not express TNFRSF11B (26) vs lines expressing it (24) | 1.65× lower at baseline in the lines without TNFRSF11B | 0.070 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12 |
| cells under [[Daptomycin (drug)]] 5 µM | B | TNFRSF11B activity lowers the cells' numbers under Daptomycin 5 µM (makes them more sensitive) | lines that do not express TNFRSF11B (26) vs lines expressing it (22) | the lines without TNFRSF11B: 1.19× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12; cell counts less trustworthy |
| [[NHS]] | B | TNFRSF11B activity raises NHS's level | lines that do not express TNFRSF11B (26) vs lines expressing it (24) | 2.85× lower at baseline in the lines without TNFRSF11B | 0.089 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12 |
| [[INHBA]] | C | TNFRSF11B activity raises INHBA's level | lines that do not express TNFRSF11B (26) vs lines expressing it (24) | 4.94× lower at baseline in the lines without TNFRSF11B | 0.008 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12; co-absent with the target |
| [[BMPER]] | C | TNFRSF11B activity raises BMPER's level | lines that do not express TNFRSF11B (26) vs lines expressing it (24) | 3.03× lower at baseline in the lines without TNFRSF11B | 0.010 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12; co-absent with the target |
| [[MN1]] | C | TNFRSF11B activity raises MN1's level | lines that do not express TNFRSF11B (26) vs lines expressing it (24) | 2.29× lower at baseline in the lines without TNFRSF11B | 0.020 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12; co-absent with the target |
| [[COL4A6]] | C | TNFRSF11B activity raises COL4A6's level | lines that do not express TNFRSF11B (26) vs lines expressing it (24) | 2.26× lower at baseline in the lines without TNFRSF11B | 0.031 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12; co-absent with the target |
| [[PDE7B]] | C | TNFRSF11B activity raises PDE7B's level | lines that do not express TNFRSF11B (26) vs lines expressing it (24) | 2.44× lower at baseline in the lines without TNFRSF11B | 0.031 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12; co-absent with the target |
| [[C5orf46]] | C | TNFRSF11B activity raises C5orf46's level | lines that do not express TNFRSF11B (26) vs lines expressing it (24) | 1.97× lower at baseline in the lines without TNFRSF11B | 0.044 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12; co-absent with the target |
| [[SHISAL1]] | C | TNFRSF11B activity raises SHISAL1's level | lines that do not express TNFRSF11B (26) vs lines expressing it (24) | 2.75× lower at baseline in the lines without TNFRSF11B | 0.045 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12; co-absent with the target |
| [[LUM]] | C | TNFRSF11B activity raises LUM's level | lines that do not express TNFRSF11B (26) vs lines expressing it (24) | 2.81× lower at baseline in the lines without TNFRSF11B | 0.076 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.596). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.0, 34.5); signed map (43.2, 41.9). **Vector** length 69.8, 17.5% of its response variance represented; |z| ≥ 3 in 760 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.2 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +0.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.1 | +1.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.1 | -3.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.7 | -2.9 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.6 | -2.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.4 | -3.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor superfamily member 11b |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.12 — chr8:118,923,557-118,951,885 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OCIF, TR1; previously OPG |
| Gene groups (HGNC) | Tumor necrosis factor receptor superfamily |
| Hallmark sets | APICAL_JUNCTION, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 3 pathways, smallest: TNFs bind their physiological receptors; TNFR2 non-canonical NF-kB pathway; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [O00300](https://www.uniprot.org/uniprotkb/O00300) (Tumor necrosis factor receptor superfamily member 11B):

> Acts as a decoy receptor for TNFSF11/RANKL and thereby neutralizes its function in osteoclastogenesis. Inhibits the activation of osteoclasts and promotes osteoclast apoptosis in vitro. Bone homeostasis seems to depend on the local ratio between TNFSF11 and TNFRSF11B. May also play a role in preventing arterial calcification. May act as decoy receptor for TNFSF10/TRAIL and protect against apoptosis. TNFSF10/TRAIL binding blocks the inhibition of osteoclastogenesis.

**Summary**, from NCBI Gene [4982](https://www.ncbi.nlm.nih.gov/gene/4982):

> The protein encoded by this gene is a member of the TNF-receptor superfamily. This protein is an osteoblast-secreted decoy receptor that functions as a negative regulator of bone resorption. This protein specifically binds to its ligand, osteoprotegerin ligand, both of which are key extracellular regulators of osteoclast development. Studies of the mouse counterpart also suggest that this protein and its ligand play a role in lymph-node organogenesis and vascular calcification. Alternatively …

**Accessions** — [HGNC:11909](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11909) · Entrez [4982](https://www.ncbi.nlm.nih.gov/gene/4982) · UniProt [O00300](https://www.uniprot.org/uniprotkb/O00300) · Ensembl [ENSG00000164761](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164761)

## Data

Gene col 9005: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9005); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9005, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9005]; `tensor/DDL_lfc|DDL_z.npy` [9005]; `embed/gene_vectors.npy` [9005]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9005 or target_col == 9005). Every well: [[TNFRSF11B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFRSF11B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
