---
symbol: "LURAP1"
type: "gene"
col: 10096
ensembl_id: "ENSG00000171357"
name: "leucine rich adaptor protein 1"
location: "1p34.1"
module: 155
arm: "+"
pooled_cpm: 2.12
n_lines_expressing: 37
n_dd_up: 11
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# LURAP1

*leucine rich adaptor protein 1* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.82× (z +13.4, q 2e-38, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +7.8, q 2e-12, up in 9 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.424× (z -7.6, q 1e-11, down in 18 of 30 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.609× (z -4.4, q 0.001, down in 11 of 20 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01503]] (+0.63, fdr 1e-05), [[LINC01440]] (+0.62, fdr 1e-05), [[ST8SIA6]] (+0.58, fdr 1e-05); moves opposite to [[MFF]] (-0.40, fdr 2e-04), [[ITPR2]] (-0.39, fdr 1e-04), [[SPECC1L]] (-0.38, fdr 2e-04).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SNCG]] → it (grade B ⚠); 5 go from it, the strongest it → [[ATAD3C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10096.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.82×** | +13.4 | 2e-38 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +7.8 | 2e-12 | 9/24 (NCI-H1792, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.54×** | +7.7 | 4e-12 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +6.1 | 1e-07 | 1/10 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +5.4 | 6e-06 | 0/11 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.49×** | +5.0 | 6e-05 | 1/30 (A-172) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +4.4 | 7e-04 | 9/25 (BT-474, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.64×** | +4.4 | 9e-04 | 8/31 (MIA PaCa-2, C-33 A, …) | rises with dose |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.50×** | +3.6 | 0.020 | 2/17 (SHP-77, BT-474) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.72×** | +3.4 | 0.035 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.047 | 7/30 (BT-474, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Drospirenone (drug)]] 0.5 µM |  | 1.41× | +3.0 | 0.11 | 3/21 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10096.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.424×** | -7.6 | 1e-11 | 18/30 (BT-474, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.508×** | -5.8 | 2e-06 | 16/27 (CFPAC-1, BT-474, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.599×** | -4.6 | 1e-03 | 11/24 (CFPAC-1, BT-474, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.609×** | -4.4 | 0.001 | 11/20 (CFPAC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.607×** | -4.3 | 0.002 | 4/28 (HCT15, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.655×** | -3.8 | 0.016 | 10/22 (BT-474, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.662×** | -3.4 | 0.055 | 6/27 (BT-474, HT-29, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.700× | -3.2 | 0.11 | 9/31 (SNU-423, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.713× | -3.0 | 0.16 | 12/29 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10096. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 9.68 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0683× (z -13.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Erlotinib (drug)]] 5 µM 0.0759× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 4.67 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0622× (z -12.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0278× (z -11.4) |
| [[HT-29 (line)]] | alt | 9.19 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0618× (z -11.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0430× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 4.76 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.101× (z -8.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SHP-77 (line)]] | alt | 3.04 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0490× (z -8.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.525 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.335 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.255 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.622 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.824 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.663 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.547 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.604 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.313 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.851 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.598 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.452 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.864 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.568 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10096), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01503]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[LINC01440]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[ST8SIA6]] | +0.58 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[TSPAN1]] | +0.56 | +0.56 / +0.43 | both halves | 3e-05 | ⚠ same locus (17.4 kb, same strand: neighbours can correlate without regulation) |
| [[TNNT2]] | +0.55 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[ARHGAP30]] | +0.53 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[EPHA1-AS1]] | +0.50 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[LINC00672]] | +0.49 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[ITGB6]] | +0.49 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[S100A8]] | +0.49 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[PLA2R1]] | +0.48 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[KCNIP3]] | +0.48 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[AQP3]] | +0.48 | +0.40 / +0.49 | both halves | 5e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFF]] | -0.40 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[ITPR2]] | -0.39 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[SPECC1L]] | -0.38 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[MAP7D3]] | -0.38 | -0.39 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNCG]] | B | SNCG activity raises LURAP1's level | lines that do not express SNCG (30) vs lines expressing it (20) | 1.52× lower at baseline in the lines without SNCG | 0.042 | ⚠ within organs, on part of the lines; also absent: CST6, ENSG00000286546, IGFL2-AS1 |
| [[C2CD4A]] | B | C2CD4A activity raises LURAP1's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 1.64× lower at baseline in the lines without C2CD4A | 0.052 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L |
| [[SERPINB4]] | B | SERPINB4 activity raises LURAP1's level | lines that do not express SERPINB4 (39) vs lines expressing it (11) | 1.56× lower at baseline in the lines without SERPINB4 | 0.079 | ⚠ within organs, on part of the lines; also absent: SERPINB3, GABRP, S100A9 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATAD3C]] | B | LURAP1 activity raises ATAD3C's level | lines that do not express LURAP1 (13) vs lines expressing it (37) | 1.62× lower at baseline in the lines without LURAP1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ZG16B; maybe low, not absent |
| [[GUCY1A1]] | B | LURAP1 activity raises GUCY1A1's level | lines that do not express LURAP1 (13) vs lines expressing it (37) | 1.38× lower at baseline in the lines without LURAP1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ZG16B; maybe low, not absent |
| [[UGT1A8]] | B | LURAP1 activity raises UGT1A8's level | lines that do not express LURAP1 (13) vs lines expressing it (37) | 2.58× lower at baseline in the lines without LURAP1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ZG16B; maybe low, not absent |
| [[GSTM2]] | B | LURAP1 activity raises GSTM2's level | lines that do not express LURAP1 (13) vs lines expressing it (37) | 1.18× lower at baseline in the lines without LURAP1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ZG16B; maybe low, not absent |
| [[TMEM45B]] | B | LURAP1 activity raises TMEM45B's level | lines that do not express LURAP1 (13) vs lines expressing it (37) | 2.84× lower at baseline in the lines without LURAP1 | 0.072 | ⚠ within organs, on part of the lines; also absent: ZG16B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.5, 49.5); signed map (55.2, 22.4). **Vector** length 45.5, 7.49% of its response variance represented; |z| ≥ 3 in 757 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +7.7 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.8 | +1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +13.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.6 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +1.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.9 | -0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +4.4 |
|  | [[Pyridoxine (drug)]] 0.5 µM |  | +0.7 | +2.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.1 | -7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.0 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -0.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -0.9 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.7 | -1.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -0.7 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich adaptor protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:46,203,334-46,221,256 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25163, LRAP35a; previously C1orf190 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96LR2](https://www.uniprot.org/uniprotkb/Q96LR2) (Leucine rich adaptor protein 1):

> Acts as an activator of the canonical NF-kappa-B pathway and drive the production of pro-inflammatory cytokines. Promotes the antigen (Ag)-presenting and priming function of dendritic cells via the canonical NF-kappa-B pathway. In concert with MYO18A and CDC42BPA/CDC42BPB, is involved in modulating lamellar actomyosin retrograde flow that is crucial to cell protrusion and migration. Activates CDC42BPA/CDC42BPB and targets it to actomyosin through its interaction with MYO18A, leading to …

**Summary**, from NCBI Gene [541468](https://www.ncbi.nlm.nih.gov/gene/541468):

> Involved in positive regulation of canonical NF-kappaB signal transduction and positive regulation of cytokine production. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:32327](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32327) · Entrez [541468](https://www.ncbi.nlm.nih.gov/gene/541468) · UniProt [Q96LR2](https://www.uniprot.org/uniprotkb/Q96LR2) · Ensembl [ENSG00000171357](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171357)

## Data

Gene col 10096: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10096); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10096, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10096]; `tensor/DDL_lfc|DDL_z.npy` [10096]; `embed/gene_vectors.npy` [10096]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10096 or target_col == 10096). Every well: [[LURAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LURAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
