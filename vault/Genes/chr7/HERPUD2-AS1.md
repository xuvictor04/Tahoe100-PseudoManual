---
symbol: "HERPUD2-AS1"
type: "gene"
col: 15676
ensembl_id: "ENSG00000271122"
name: "HERPUD2 antisense RNA 1"
location: "7p14.2"
module: 16
arm: "+"
pooled_cpm: 2.86
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 16
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# HERPUD2-AS1

*HERPUD2 antisense RNA 1* — 7p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.13× (z +9.7, q 2e-19, up in 0 of 0 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 3.23× (z +8.3, q 2e-14, up in 34 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.357× (z -7.3, q 2e-10, down in 30 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B3GALT9]] (+0.72, fdr 7e-06), [[PLPP6]] (+0.68, fdr 7e-06), [[PIGM]] (+0.63, fdr 1e-05); moves opposite to [[VDAC1P8]] (-0.59, fdr 2e-05), [[TRMT2B]] (-0.55, fdr 1e-05), [[ORC3]] (-0.52, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15676.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.13×** | +9.7 | 2e-19 | 0/0 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.23×** | +8.3 | 2e-14 | 34/44 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +7.9 | 7e-13 | 13/17 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.92×** | +7.6 | 4e-12 | 29/42 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.84×** | +7.4 | 1e-11 | 30/42 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +6.4 | 2e-08 | 15/32 (HEC-1-A, BT-474, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **2.43×** | +6.3 | 2e-08 | 23/31 (BT-474, SHP-77, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.30×** | +5.8 | 4e-07 | 27/45 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.33×** | +5.6 | 2e-06 | 3/3 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.74×** | +5.6 | 2e-06 | 11/42 (HEC-1-A, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +4.5 | 3e-04 | 11/31 (A-172, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.4 | 5e-04 | 9/45 (A498, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +4.4 | 6e-04 | 14/44 (SHP-77, H4, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.72×** | +3.8 | 0.005 | 8/45 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.72×** | +3.8 | 0.005 | 7/26 (A-172, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.64×** | +3.5 | 0.015 | 11/42 (A-172, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.50×** | +3.4 | 0.022 | 3/38 (A-172, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.54×** | +3.1 | 0.064 | 7/38 (A-427, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15676.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.357×** | -7.3 | 2e-10 | 30/42 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.417×** | -6.2 | 2e-07 | 26/41 (A-427, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.404×** | -6.1 | 3e-07 | 26/38 (HEC-1-A, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.455×** | -5.6 | 4e-06 | 24/45 (A-427, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.512×** | -4.7 | 2e-04 | 21/41 (A-427, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.566×** | -4.0 | 0.005 | 17/40 (RPMI-7951, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.609×** | -3.5 | 0.041 | 12/44 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.629×** | -3.3 | 0.073 | 11/45 (SW48, RKO, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | **0.725×** | -3.2 | 0.081 | 8/44 (SHP-77, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.651× | -3.0 | 0.13 | 14/24 (LoVo, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15676. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 6.89 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0474× (z -11.9) |
| [[HT-29 (line)]] | alt | 3.21 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0354× (z -10.0) |
| [[SW480 (line)]] | alt | 1.47 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0351× (z -10.9) |
| [[A-172 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.972 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15676), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GALT9]] | +0.72 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[PLPP6]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[PIGM]] | +0.63 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[TTC30A]] | +0.62 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[ZFP41]] | +0.60 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[CENPB]] | +0.59 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[MAGEF1]] | +0.59 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[B3GALT6]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[C6orf120]] | +0.57 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[PURB]] | +0.57 | +0.72 / +0.41 | both halves | 4e-05 |  |
| [[RAP2C-AS1]] | +0.56 | +0.74 / +0.59 | both halves | 7e-06 | same gene group |
| [[CEP19]] | +0.56 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VDAC1P8]] | -0.59 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[TRMT2B]] | -0.55 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[ORC3]] | -0.52 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[CCDC32]] | -0.51 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[CLCC1]] | -0.51 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[DONSON]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[PPP1R32]] | -0.48 | -0.54 / -0.40 | both halves | 4e-05 |  |
| [[DYRK4]] | -0.48 | -0.32 / -0.48 | both halves | 1e-04 |  |
| [[PI4K2B]] | -0.48 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[PMS2P4-1]] | -0.48 | -0.59 / -0.37 | both halves | 7e-05 |  |
| [[INTS8]] | -0.48 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[SLC30A6]] | -0.48 | -0.57 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises HERPUD2-AS1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ID2-AS1]] | B | ID2-AS1 activity raises HERPUD2-AS1's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.64× lower at baseline in the lines without ID2-AS1 | 0.099 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.515). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.4, 18.0); signed map (-1.7, -30.8). **Vector** length 53.9, 8.13% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +5.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +0.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.0 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +9.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +1.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.8 | -7.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.4 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.5 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | HERPUD2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7p14.2 — chr7:35,695,214-35,699,413 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55258](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55258) · Entrez [101930085](https://www.ncbi.nlm.nih.gov/gene/101930085) · Ensembl [ENSG00000271122](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000271122)

## Data

Gene col 15676: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15676); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15676, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15676]; `tensor/DDL_lfc|DDL_z.npy` [15676]; `embed/gene_vectors.npy` [15676]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15676 or target_col == 15676). Every well: [[HERPUD2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HERPUD2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
