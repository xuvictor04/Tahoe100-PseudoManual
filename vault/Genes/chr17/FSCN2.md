---
symbol: "FSCN2"
type: "gene"
col: 11850
ensembl_id: "ENSG00000186765"
name: "fascin actin-bundling protein 2, retinal"
location: "17q25.3"
module: 47
arm: "+"
pooled_cpm: 5.1
n_lines_expressing: 46
n_dd_up: 5
n_dd_down: 19
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 8
direction_downstream: 1
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# FSCN2

*fascin actin-bundling protein 2, retinal* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.83× (z +11.3, q 5e-27, up in 39 of 43 measured lines) ⚠ position not correctable. The strongest without an alert is [[Hydroxyurea (drug)]] 0.05 µM: 2.05× (z +3.6, q 0.041, up in 8 of 33 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (PANC-1 2.09×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.325× (z -6.1, q 5e-07, down in 30 of 42 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.459× (z -4.2, q 0.002, down in 24 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPTBN5]] (+0.68, fdr 7e-06), [[ZDHHC11]] (+0.68, fdr 7e-06), [[MMP25]] (+0.66, fdr 1e-05); moves opposite to [[PRKRA]] (-0.62, fdr 1e-05), [[ESD]] (-0.60, fdr 9e-06), [[UBA3]] (-0.59, fdr 1e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LINC01348]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CRBN]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11850.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (PANC-1 2.09×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.83×** | +11.3 | 5e-27 | 39/43 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.12×** | +6.0 | 6e-07 | 2/9 (CFPAC-1, A498) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.89×** | +5.4 | 1e-05 | 3/12 (HOP62, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **2.05×** | +3.6 | 0.041 | 8/33 (C-33 A, A-427, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +3.3 | 0.093 | 2/21 (HEC-1-A, LoVo) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11850.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.325×** | -6.1 | 5e-07 | 30/42 (HT-29, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.329×** | -5.8 | 2e-06 | 28/39 (SW480, LoVo, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.412×** | -4.8 | 3e-04 | 25/41 (COLO 205, LoVo, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.431×** | -4.6 | 7e-04 | 23/34 (HT-29, A549, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.459×** | -4.2 | 0.002 | 24/41 (RPMI-7951, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.578×** | -4.2 | 0.002 | 18/37 (HT-29, SW480, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.465×** | -4.2 | 0.003 | 19/40 (CHP-212, LoVo, …) | all doses, flat | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.493×** | -3.8 | 0.011 | 18/41 (NCI-H23, C32, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.518×** | -3.6 | 0.021 | 19/41 (LoVo, HT-29, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.523×** | -3.5 | 0.021 | 15/41 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.525×** | -3.5 | 0.021 | 15/42 (RPMI-7951, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.525×** | -3.5 | 0.021 | 19/41 (LoVo, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.527×** | -3.5 | 0.021 | 14/41 (SW48, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.636×** | -3.5 | 0.021 | 14/41 (SHP-77, RPMI-7951, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.533×** | -3.4 | 0.023 | 17/36 (SW480, LS 180, …) | rises with dose | position effect removed |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **0.542×** | -3.3 | 0.031 | 19/37 (NCI-H2030, BT-474, …) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.05 µM |  | **0.530×** | -3.2 | 0.045 | 18/38 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.550×** | -3.1 | 0.064 | 21/39 (SHP-77, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.66 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11850. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.5 | 0 | 3 (1 ⚠) | — | [[Cobimetinib (drug)]] 0.05 µM 0.0933× (z -9.0) |
| [[LoVo (line)]] | wt | 10.4 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0491× (z -10.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A549 (line)]] | wt | 5.62 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0344× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0416× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[KATO III (line)]] | alt | 6.30 | 0 | 1 | — | [[Erythromycin (drug)]] 0.05 µM 0.0635× (z -8.7) |
| [[PANC-1 (line)]] | alt | 4.50 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.09× (z +8.8) ⚠ position not correctable | — |
| [[A-172 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.893 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11850), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTBN5]] | +0.68 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[ZDHHC11]] | +0.68 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[MMP25]] | +0.66 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[GAL3ST2]] | +0.66 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[LINC02236]] | +0.63 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[C19orf38]] | +0.63 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[LSMEM2]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[DNAH1]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[NOP14-AS1]] | +0.61 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[SLC22A20P]] | +0.60 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[THOC6]] | +0.60 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[MYADM-AS1]] | +0.59 | +0.58 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKRA]] | -0.62 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[ESD]] | -0.60 | -0.58 / -0.57 | both halves | 9e-06 |  |
| [[UBA3]] | -0.59 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[NSL1]] | -0.58 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[CRYZL1]] | -0.56 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[DPY30]] | -0.56 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[TNRC6A]] | -0.55 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[CRBN]] | -0.55 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[MALSU1]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[NIPSNAP2]] | -0.55 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[SPATA7]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 | STRING 621 |
| [[FAM193B]] | -0.53 | -0.48 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01348]] | B | LINC01348 activity raises FSCN2's level | lines that do not express LINC01348 (10) vs lines expressing it (40) | 1.68× lower at baseline in the lines without LINC01348 | 0.011 | ⚠ within organs, on part of the lines; also absent: ARHGAP42, RIPK4, ABCC3; maybe low, not absent |
| [[ESRP2]] | B | ESRP2 activity raises FSCN2's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 1.76× lower at baseline in the lines without ESRP2 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |
| [[LSMEM2]] | B | LSMEM2 activity raises FSCN2's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 1.77× lower at baseline in the lines without LSMEM2 | 0.031 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[MROH3P]] | B | MROH3P activity raises FSCN2's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 1.71× lower at baseline in the lines without MROH3P | 0.031 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[TNNT2]] | B | TNNT2 activity raises FSCN2's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 1.64× lower at baseline in the lines without TNNT2 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[MFNG]] | B | MFNG activity raises FSCN2's level | lines that do not express MFNG (12) vs lines expressing it (38) | 1.52× lower at baseline in the lines without MFNG | 0.052 | ⚠ within organs, on part of the lines; also absent: CARD10, EPS8L2, KRT8 |
| [[PSD4]] | B | PSD4 activity raises FSCN2's level | lines that do not express PSD4 (8) vs lines expressing it (42) | 1.66× lower at baseline in the lines without PSD4 | 0.073 | ⚠ within organs, on part of the lines; also absent: TBILA, SH2D4A, GPR39 |
| [[HPN]] | B | HPN activity raises FSCN2's level | lines that do not express HPN (6) vs lines expressing it (44) | 1.47× lower at baseline in the lines without HPN | 0.076 | ⚠ within organs, on part of the lines; also absent: NAT14, APBA1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRBN]] | C | FSCN2 activity lowers CRBN's level | lines that do not express FSCN2 (4) vs lines expressing it (46) | 1.63× higher at baseline in the lines without FSCN2 | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000267174, ADCY7, ENSG00000229848; maybe low, not absent |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.689). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.9, -12.5); signed map (19.3, 14.4). **Vector** length 62.3, 9.48% of its response variance represented; |z| ≥ 3 in 1,193 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.3 | +1.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.8 | -6.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -2.6 | -3.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -2.4 | -4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.3 | -4.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | +1.3 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | -1.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | fascin actin-bundling protein 2, retinal |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,528,377-81,537,130 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RP30, RFSN |
| Gene groups (HGNC) | Fascin family |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [O14926](https://www.uniprot.org/uniprotkb/O14926) (Fascin-2):

> Acts as an actin bundling protein. May play a pivotal role in photoreceptor cell-specific events, such as disk morphogenesis.

**Summary**, from NCBI Gene [25794](https://www.ncbi.nlm.nih.gov/gene/25794):

> This gene encodes a member of the fascin protein family. Fascins crosslink actin into filamentous bundles within dynamic cell extensions. This family member is proposed to play a role in photoreceptor disk morphogenesis. A mutation in this gene results in one form of autosomal dominant retinitis pigmentosa and macular degeneration. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3960](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3960) · Entrez [25794](https://www.ncbi.nlm.nih.gov/gene/25794) · UniProt [O14926](https://www.uniprot.org/uniprotkb/O14926) · Ensembl [ENSG00000186765](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186765)

## Data

Gene col 11850: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11850); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11850, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11850]; `tensor/DDL_lfc|DDL_z.npy` [11850]; `embed/gene_vectors.npy` [11850]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11850 or target_col == 11850). Every well: [[FSCN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FSCN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
