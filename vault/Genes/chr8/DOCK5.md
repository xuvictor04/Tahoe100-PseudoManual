---
symbol: "DOCK5"
type: "gene"
col: 7187
ensembl_id: "ENSG00000147459"
name: "dedicator of cytokinesis 5"
location: "8p21.2"
module: 174
arm: "+"
pooled_cpm: 441.21
n_lines_expressing: 47
n_dd_up: 1
n_dd_down: 44
n_dd_up_clean: 1
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 9
direction_downstream: 4
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# DOCK5

*dedicator of cytokinesis 5* — 8p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[BAY1125976 (drug)]] 5 µM: 1.63× (z +4.1, q 0.025, up in 31 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (A498 2.29×; ⚠ cell-cycle shift, explains ~35% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (A498 2.18×; ⚠ cell-cycle shift, explains ~84% of this change).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.280× (z -28.7, q 0e+00, down in 42 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASAP2]] (+0.71, fdr 7e-06), [[ITGB5]] (+0.69, fdr 7e-06), [[ITGA2]] (+0.67, fdr 7e-06); moves opposite to [[NUPR1]] (-0.54, fdr 2e-05), [[YY1AP1]] (-0.52, fdr 3e-05), [[DNAJC27]] (-0.50, fdr 3e-05).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MET]] → it (grade B ⚠); 4 go from it, the strongest it → cells under [[olaparib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7187.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (A498 2.29×; ⚠ cell-cycle shift, explains ~35% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (A498 2.18×; ⚠ cell-cycle shift, explains ~84% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[BAY1125976 (drug)]] 5 µM |  | **1.63×** | +4.1 | 0.025 | 31/45 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.23× | +3.4 | 0.20 | 24/45 (J82, LoVo, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.23× | +3.2 | 0.29 | 23/45 (RPMI-7951, SHP-77, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 20 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7187.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.280×** | -28.7 | 0e+00 | 42/45 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.198×** | -25.8 | 0e+00 | 45/45 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.237×** | -22.9 | 0e+00 | 45/45 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.304×** | -19.0 | 0e+00 | 44/45 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.516×** | -14.9 | 0e+00 | 41/46 (NCI-H1792, A549, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.405×** | -13.8 | 2e-41 | 43/45 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.406×** | -13.8 | 2e-41 | 45/45 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.484×** | -11.6 | 5e-29 | 38/45 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.524×** | -9.5 | 1e-19 | 38/43 (NCI-H1792, HepG2/C3A, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.551×** | -9.5 | 2e-19 | 38/45 (HepG2/C3A, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.579×** | -8.7 | 2e-16 | 37/45 (HepG2/C3A, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.586×** | -8.2 | 2e-14 | 36/45 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **0.617×** | -7.7 | 7e-13 | 32/46 (AsPC-1, NCI-H1792, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.622×** | -7.5 | 2e-12 | 33/45 (LoVo, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **0.636×** | -6.9 | 2e-10 | 29/42 (NCI-H23, NCI-H1573, …) | all doses, flat | composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.532×** | -5.3 | 5e-06 | 41/45 (CFPAC-1, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.719×** | -5.2 | 5e-06 | 33/45 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.552×** | -4.9 | 2e-05 | 30/46 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.732×** | -4.9 | 2e-05 | 31/45 (HepG2/C3A, BT-474, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.739×** | -4.8 | 4e-05 | 31/46 (BT-474, A-172, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.744×** | -4.7 | 7e-05 | 28/45 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.813×** | -4.6 | 9e-05 | 25/45 (RKO, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7187. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 340 | 0 | 33 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -17.1) |
| [[NCI-H460 (line)]] | wt | 667 | 0 | 21 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -25.4) |
| [[SHP-77 (line)]] | alt | 408 | 0 | 19 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -25.9) |
| [[CFPAC-1 (line)]] | alt | 621 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -29.9) |
| [[HepG2_C3A (line)]] | wt | 455 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -27.1) |
| [[H4 (line)]] | wt | 470 | 0 | 16 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0981× (z -23.1) |
| [[HOP62 (line)]] | alt | 444 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -28.2) |
| [[NCI-H1573 (line)]] | alt | 1,032 | 0 | 16 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0741× (z -47.0) |
| [[NCI-H1792 (line)]] | alt | 869 | 0 | 16 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -33.2) |
| [[LoVo (line)]] | wt | 455 | 0 | 15 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -20.6) |
| [[LOX-IMVI (line)]] | wt | 340 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -25.2) |
| [[SW 900 (line)]] | alt | 594 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -24.6) |
| [[PANC-1 (line)]] | alt | 334 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -30.4) |
| [[SW48 (line)]] | wt | 692 | 0 | 12 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.175× (z -17.5) |
| [[A-172 (line)]] | wt | 422 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -23.3) |
| [[HS-578T (line)]] | alt | 656 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0907× (z -26.3) |
| [[SW480 (line)]] | alt | 328 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -32.8) |
| [[A498 (line)]] | wt | 400 | 2 (2 ⚠) | 7 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +9.5) ⚠ cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -21.1) |
| [[J82 (line)]] | alt | 304 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -24.6) |
| [[RKO (line)]] | wt | 233 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -20.0) |
| [[SNU-423 (line)]] | alt | 251 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -22.5) |
| [[AsPC-1 (line)]] | alt | 1,159 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -20.9) |
| [[KATO III (line)]] | alt | 441 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.130× (z -23.8) |
| [[NCI-H2030 (line)]] | alt | 770 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -20.9) |
| [[NCI-H23 (line)]] | alt | 596 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -22.8) |
| [[Panc 03.27 (line)]] | alt | 289 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -19.1) |
| [[RPMI-7951 (line)]] | alt | 479 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -22.8) |
| [[A549 (line)]] | wt | 910 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.0492× (z -24.6) |
| [[Hs 766T (line)]] | wt | 737 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.107× (z -19.8) |
| [[hTERT-HPNE (line)]] | wt | 348 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -17.0) |
| [[MIA PaCa-2 (line)]] | alt | 148 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.300× (z -13.9) |
| [[NCI-H2347 (line)]] | alt | 256 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -11.9) |
| [[SK-MEL-2 (line)]] | alt | 227 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -24.9) |
| [[SW1417 (line)]] | alt | 203 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -18.2) |
| [[C32 (line)]] | wt | 147 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -10.3) |
| [[COLO 205 (line)]] | alt | 201 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -20.5) |
| [[HCT15 (line)]] | alt | 330 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -13.3) |
| [[HT-29 (line)]] | alt | 175 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -18.5) |
| [[HEC-1-A (line)]] | alt | 286 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.290× (z -19.2) |
| [[LS 180 (line)]] | wt | 261 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.226× (z -20.1) |
| [[SNU-1 (line)]] | wt | 240 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.382× (z -9.8) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.538× (z -9.2) |
| [[CHP-212 (line)]] | wt | 146 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -9.1) |
| [[SW 1271 (line)]] | alt | 229 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -9.8) |
| [[A-427 (line)]] | wt | 146 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 69.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 83.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 548 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 431 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 452 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 92.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7187), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASAP2]] | +0.71 | +0.69 / +0.69 | both halves | 7e-06 | same gene group |
| [[ITGB5]] | +0.69 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.67 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[HMGA2]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[PITPNC1]] | +0.66 | +0.70 / +0.65 | both halves | 7e-06 | same gene group |
| [[ELK3]] | +0.66 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[ST3GAL1]] | +0.66 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[BCAR3]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[EFNA5]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[NIBAN2]] | +0.63 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[DLC1]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 | pathway: RAC1 GTPase cycle |
| [[SPRY4-AS1]] | +0.62 | +0.62 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUPR1]] | -0.54 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[YY1AP1]] | -0.52 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[DNAJC27]] | -0.50 | -0.53 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MET]] | B | MET activity raises DOCK5's level | lines that do not express MET (9) vs lines expressing it (41) | 2.35× lower at baseline in the lines without MET | 0.013 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[CEMIP]] | B | CEMIP activity raises DOCK5's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 1.79× lower at baseline in the lines without CEMIP | 0.013 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[PI3]] | B | PI3 activity raises DOCK5's level | lines that do not express PI3 (27) vs lines expressing it (23) | 1.78× lower at baseline in the lines without PI3 | 0.024 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |
| [[CD59]] | B | CD59 activity raises DOCK5's level | lines that do not express CD59 (7) vs lines expressing it (43) | 1.96× lower at baseline in the lines without CD59 | 0.048 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[ITGA2]] | B | ITGA2 activity raises DOCK5's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 1.98× lower at baseline in the lines without ITGA2 | 0.051 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[EVA1C]] | B | EVA1C activity raises DOCK5's level | lines that do not express EVA1C (15) vs lines expressing it (35) | 1.79× lower at baseline in the lines without EVA1C | 0.055 | ⚠ within organs, on part of the lines; also absent: PI3, ENSG00000260877, CYB5R2 |
| [[C11orf91]] | B | C11orf91 activity raises DOCK5's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 1.84× lower at baseline in the lines without C11orf91 | 0.079 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[ABCC3]] | B | ABCC3 activity raises DOCK5's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 1.76× lower at baseline in the lines without ABCC3 | 0.097 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[ERRFI1]] | C | ERRFI1 activity raises DOCK5's level | lines that do not express ERRFI1 (4) vs lines expressing it (46) | 2.90× lower at baseline in the lines without ERRFI1 | 0.072 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000256029; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[olaparib (drug)]] 5 µM | C | DOCK5 activity lowers the cells' numbers under olaparib 5 µM (makes them more sensitive) | lines that do not express DOCK5 (3) vs lines expressing it (45) | the lines without DOCK5: 1.58× the cells of the other lines | 0.051 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: PMAIP1, FZD6, GCA; maybe low, not absent |
| cells under [[Pimozide (drug)]] 0.5 µM | C | DOCK5 activity raises the cells' numbers under Pimozide 0.5 µM (protects the cells) | lines that do not express DOCK5 (3) vs lines expressing it (45) | the lines without DOCK5: 0.73× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: PMAIP1, FZD6, GCA; maybe low, not absent |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM | C | DOCK5 activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express DOCK5 (3) vs lines expressing it (45) | the lines without DOCK5: 0.77× the cells of the other lines | 0.073 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: PMAIP1, FZD6, GCA; maybe low, not absent |
| cells under [[Pemigatinib (drug)]] 5 µM | C | DOCK5 activity raises the cells' numbers under Pemigatinib 5 µM (protects the cells) | lines that do not express DOCK5 (3) vs lines expressing it (45) | the lines without DOCK5: 0.71× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: PMAIP1, FZD6, GCA; maybe low, not absent |

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.756). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.1, 6.3); signed map (7.8, 47.7). **Vector** length 108, 43.4% of its response variance represented; |z| ≥ 3 in 1,993 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | -2.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.6 | +2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.5 | +2.8 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +3.2 | +2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.9 | +4.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +1.4 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.5 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.3 | -4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -7.0 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -7.0 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.0 | -4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.6 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | dedicator of cytokinesis 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.2 — chr8:25,184,689-25,418,082 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21034 |
| Gene groups (HGNC) | DOCK family Rho GEFs; MicroRNA protein coding host genes; SH3 domain containing |
| Reactome | 7 pathways, smallest: RHOG GTPase cycle; Factors involved in megakaryocyte development and platelet production; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7D0](https://www.uniprot.org/uniprotkb/Q9H7D0) (Dedicator of cytokinesis protein 5):

> Guanine nucleotide exchange factor (GEF) for Rho and Rac. GEF proteins activate small GTPases by exchanging bound GDP for free GTP (By similarity). Together with ELMO1, activates RAC1; the activity is stimulated by RHOG. Along with DOCK1, mediates CRK/CRKL regulation of epithelial and endothelial cell spreading and migration on type IV collagen.

**Summary**, from NCBI Gene [80005](https://www.ncbi.nlm.nih.gov/gene/80005):

> This gene encodes a member of the dedicator of cytokinesis protein family. Members of this family act as guanine nucleotide exchange factors for small Rho family G proteins. The protein encoded by this gene is thought to associate with adaptors CRK and CRKL, and function in regulation of intestinal epithelial cell spreading and migration on collagen IV. Similar proteins in mouse and zebrafish also function in myoblast fusion. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:23476](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23476) · Entrez [80005](https://www.ncbi.nlm.nih.gov/gene/80005) · UniProt [Q9H7D0](https://www.uniprot.org/uniprotkb/Q9H7D0) · Ensembl [ENSG00000147459](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147459)

## Data

Gene col 7187: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7187); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7187, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7187]; `tensor/DDL_lfc|DDL_z.npy` [7187]; `embed/gene_vectors.npy` [7187]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7187 or target_col == 7187). Every well: [[DOCK5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOCK5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
