---
symbol: "ZBED8"
type: "gene"
col: 13313
ensembl_id: "ENSG00000221886"
name: "zinc finger BED-type containing 8"
location: "5q33.3"
module: 16
arm: "+"
pooled_cpm: 3.24
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZBED8

*zinc finger BED-type containing 8* — 5q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.83× (z +7.8, q 3e-12, up in 16 of 45 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.54× (z +3.9, q 0.013, up in 11 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.268× (z -12.1, q 7e-31, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALG10B]] (+0.68, fdr 7e-06), [[ZNF607]] (+0.65, fdr 7e-06), [[LINC03015]] (+0.65, fdr 1e-05); moves opposite to [[PITPNA]] (-0.59, fdr 2e-05), [[EIF3K]] (-0.58, fdr 1e-05), [[DAP3]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DPY19L2P2-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13313.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.83×** | +7.8 | 3e-12 | 16/45 (NCI-H460, SW480, …) | rises with dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +4.1 | 0.013 | 6/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +3.9 | 0.013 | 11/44 (MIA PaCa-2, A-427, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +3.9 | 0.013 | 1/6 (HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +3.8 | 0.015 | 2/8 (NCI-H2347, HEC-1-A) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +3.6 | 0.034 | 9/37 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.061 | 3/47 (HS-578T, HEC-1-A, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.44×** | +3.3 | 0.069 | 6/39 (HEC-1-A, HT-29, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.093 | 5/45 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Ferulic acid (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.093 | 4/41 (HS-578T, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.093 | 5/42 (SK-MEL-2, LoVo, …) | rises with dose |  |
| [[Larotrectinib (drug)]] 5 µM |  | 1.27× | +3.0 | 0.12 | 2/46 (SK-MEL-2, CFPAC-1) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13313.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.268×** | -12.1 | 7e-31 | 37/47 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.338×** | -10.0 | 5e-21 | 31/44 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.382×** | -8.8 | 2e-16 | 27/43 (HOP62, KATO III, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.392×** | -8.6 | 1e-15 | 30/42 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.421×** | -7.9 | 2e-13 | 20/24 (SW480, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.411×** | -7.9 | 4e-13 | 18/22 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.412×** | -7.7 | 1e-12 | 25/41 (HEC-1-A, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.482×** | -6.7 | 1e-09 | 26/42 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.632×** | -4.2 | 0.001 | 20/46 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.669×** | -3.7 | 0.012 | 5/47 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.781×** | -3.2 | 0.060 | 9/45 (RPMI-7951, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.617×** | -3.2 | 0.070 | 6/45 (LOX-IMVI, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.521×** | -3.1 | 0.075 | 5/38 (HS-578T, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.532×** | -3.0 | 0.097 | 7/9 (HEC-1-A, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13313. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.13 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0437× (z -12.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.105× (z -9.2) |
| [[J82 (line)]] | alt | 4.23 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0631× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 4.58 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0415× (z -10.2) |
| [[SW480 (line)]] | alt | 3.65 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0613× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.124× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 8.08 | 0 | 1 | — | [[EX229 (drug)]] 5 µM 0.0279× (z -9.3) |
| [[HOP62 (line)]] | alt | 3.57 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0808× (z -9.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 2.24 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0919× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 8.45 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0684× (z -11.6) |
| [[A-172 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.914 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13313), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG10B]] | +0.68 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[ZNF607]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[LINC03015]] | +0.65 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ZBED5-AS1]] | +0.61 | +0.73 / +0.44 | both halves | 3e-05 |  |
| [[MBLAC2]] | +0.61 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[ZNF606]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[POMK]] | +0.59 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[ZNF681]] | +0.59 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[BBS10]] | +0.59 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[ZNF772]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[FNBP1P1]] | +0.58 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[LINC00412]] | +0.58 | +0.62 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PITPNA]] | -0.59 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[EIF3K]] | -0.58 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[DAP3]] | -0.58 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[SS18L1]] | -0.55 | -0.63 / -0.35 | both halves | 1e-04 |  |
| [[CMTM8]] | -0.55 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[MBOAT7]] | -0.54 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[CSNK1G2]] | -0.54 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[AHCYL2]] | -0.54 | -0.43 / -0.48 | both halves | 4e-05 |  |
| [[MROH1]] | -0.53 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[DDT]] | -0.53 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[LMBR1]] | -0.52 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[TRIM62]] | -0.52 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPY19L2P2-1]] | B | DPY19L2P2-1 activity raises ZBED8's level | lines that do not express DPY19L2P2-1 (17) vs lines expressing it (33) | 1.20× lower at baseline in the lines without DPY19L2P2-1 | 0.090 | ⚠ within organs, on part of the lines; also absent: RNF182, ENSG00000234405, FGF2 |
| [[PSMB5]] | B | PSMB5 activity raises ZBED8's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.604). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-31.6, 16.3); signed map (-0.2, -32.5). **Vector** length 51.9, 6.37% of its response variance represented; |z| ≥ 3 in 1,209 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.0 | +7.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.6 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.3 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +3.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.3 | -10.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.9 | -7.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -8.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.4 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -6.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -3.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.2 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger BED-type containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.3 — chr5:160,393,148-160,400,054 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Buster3; previously C5orf54, FAM200C |
| Gene groups (HGNC) | Zinc fingers BED-type |
| Matched by | ensembl_id |

UniProt [Q8IZ13](https://www.uniprot.org/uniprotkb/Q8IZ13) carries no function annotation.

**Summary**, from NCBI Gene [63920](https://www.ncbi.nlm.nih.gov/gene/63920):

> Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30804](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30804) · Entrez [63920](https://www.ncbi.nlm.nih.gov/gene/63920) · UniProt [Q8IZ13](https://www.uniprot.org/uniprotkb/Q8IZ13) · Ensembl [ENSG00000221886](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221886)

## Data

Gene col 13313: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13313); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13313, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13313]; `tensor/DDL_lfc|DDL_z.npy` [13313]; `embed/gene_vectors.npy` [13313]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13313 or target_col == 13313). Every well: [[ZBED8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBED8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
