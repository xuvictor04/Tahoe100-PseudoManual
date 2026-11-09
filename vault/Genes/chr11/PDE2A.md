---
symbol: "PDE2A"
type: "gene"
col: 11840
ensembl_id: "ENSG00000186642"
name: "phosphodiesterase 2A"
location: "11q13.4"
module: 34
arm: "+"
pooled_cpm: 11.95
n_lines_expressing: 46
n_dd_up: 11
n_dd_down: 32
n_dd_up_clean: 11
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 11
direction_downstream: 3
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# PDE2A

*phosphodiesterase 2A* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.87× (z +5.7, q 5e-06, up in 22 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.354× (z -9.6, q 6e-19, down in 32 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A51]] (+0.74, fdr 7e-06), [[TTLL13]] (+0.72, fdr 7e-06), [[SMIM41]] (+0.72, fdr 7e-06); moves opposite to [[PAIP1]] (-0.61, fdr 1e-05), [[USP24]] (-0.58, fdr 2e-05), [[CHPT1]] (-0.58, fdr 1e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TGFA]] → it (grade B ⚠); 3 go from it, the strongest it → [[LUCAT1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11840.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.87×** | +5.7 | 5e-06 | 22/43 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.77×** | +5.2 | 5e-05 | 19/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **1.48×** | +5.1 | 8e-05 | 23/43 (SW480, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +4.5 | 8e-04 | 20/43 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +4.5 | 8e-04 | 20/44 (BT-474, LOX-IMVI, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +4.4 | 9e-04 | 16/43 (PANC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.51×** | +3.8 | 0.013 | 15/43 (SW480, HOP62, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.022 | 9/42 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | **1.46×** | +3.5 | 0.028 | 9/42 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.037 | 10/41 (hTERT-HPNE, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.3 | 0.049 | 9/44 (SNU-423, COLO 205, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.90×** | +3.1 | 0.099 | 10/39 (SW480, Hs 766T, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11840.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.354×** | -9.6 | 6e-19 | 32/43 (RPMI-7951, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.449×** | -7.4 | 5e-11 | 32/43 (H4, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.413×** | -7.1 | 2e-10 | 27/42 (J82, NCI-H1792, …) | rises with dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.427×** | -6.8 | 1e-09 | 27/38 (Hs 766T, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.281×** | -6.1 | 1e-07 | 28/41 (BT-474, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.535×** | -5.8 | 8e-07 | 24/38 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.542×** | -5.7 | 1e-06 | 26/43 (BT-474, H4, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.610×** | -5.5 | 2e-06 | 24/43 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.598×** | -5.4 | 4e-06 | 23/44 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.579×** | -5.0 | 3e-05 | 22/42 (HS-578T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.603×** | -4.7 | 2e-04 | 22/42 (HepG2/C3A, AsPC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.616×** | -4.5 | 4e-04 | 20/44 (HS-578T, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.617×** | -4.4 | 4e-04 | 19/43 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.625×** | -4.3 | 6e-04 | 19/38 (NCI-H2347, CFPAC-1, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **0.732×** | -4.1 | 0.002 | 19/43 (AsPC-1, RKO, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.634×** | -3.9 | 0.004 | 18/43 (SW 1271, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.747×** | -3.8 | 0.005 | 16/43 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.664×** | -3.8 | 0.005 | 18/43 (HEC-1-A, AsPC-1, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.634×** | -3.7 | 0.007 | 19/41 (NCI-H460, HT-29, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11840. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 23.5 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0391× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0992× (z -10.5) |
| [[J82 (line)]] | alt | 20.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0732× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.115× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 26.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -13.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -9.8) |
| [[HOP62 (line)]] | alt | 22.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0412× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -8.6) |
| [[H4 (line)]] | wt | 30.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0375× (z -11.8) |
| [[HepG2_C3A (line)]] | wt | 16.9 | 0 | 2 | — | [[Ponatinib (drug)]] 5 µM 0.0472× (z -11.5) |
| [[Hs 766T (line)]] | wt | 33.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0316× (z -13.6) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 11.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -9.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[RPMI-7951 (line)]] | alt | 12.1 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0656× (z -10.3) |
| [[A-172 (line)]] | wt | 10.1 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0773× (z -9.0) |
| [[A-427 (line)]] | wt | 11.5 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0683× (z -8.9) |
| [[A549 (line)]] | wt | 12.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0732× (z -9.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 12.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.121× (z -9.2) |
| [[LoVo (line)]] | wt | 5.65 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0784× (z -9.4) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0779× (z -10.5) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 13.5 | 0 | 1 | — | [[Fenofibrate (drug)]] 5 µM 0.0640× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.132× (z -8.5) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 9.22 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0823× (z -9.1) |
| [[PANC-1 (line)]] | alt | 4.04 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.30× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 21.8 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 5 µM 0.0630× (z -9.7) |
| [[A498 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11840), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A51]] | +0.74 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[TTLL13]] | +0.72 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.72 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[ADAM8]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[PPARD]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[A3GALT2]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[POU2F2]] | +0.69 | +0.65 / +0.73 | both halves | 7e-06 | same gene group |
| [[FAM131A]] | +0.69 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[MOCS2-DT]] | +0.68 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[UCKL1-AS1]] | +0.68 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[NLRP1]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[HPX]] | +0.67 | +0.57 / +0.67 | both halves | 9e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAIP1]] | -0.61 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[USP24]] | -0.58 | -0.53 / -0.49 | both halves | 2e-05 |  |
| [[CHPT1]] | -0.58 | -0.58 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGFA]] | B | TGFA activity raises PDE2A's level | lines that do not express TGFA (17) vs lines expressing it (33) | 1.55× lower at baseline in the lines without TGFA | 0.031 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[RAC2]] | B | RAC2 activity raises PDE2A's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 1.71× lower at baseline in the lines without RAC2 | 0.032 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[TNFRSF6B]] | B | TNFRSF6B activity raises PDE2A's level | lines that do not express TNFRSF6B (33) vs lines expressing it (17) | 1.63× lower at baseline in the lines without TNFRSF6B | 0.035 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19 |
| [[SCAT1]] | B | SCAT1 activity raises PDE2A's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 1.44× lower at baseline in the lines without SCAT1 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[ITGA2]] | B | ITGA2 activity raises PDE2A's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 2.14× lower at baseline in the lines without ITGA2 | 0.040 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[TMCC3]] | B | TMCC3 activity raises PDE2A's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 1.64× lower at baseline in the lines without TMCC3 | 0.062 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[RAI14]] | B | RAI14 activity raises PDE2A's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 2.13× lower at baseline in the lines without RAI14 | 0.068 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[PTPRE]] | B | PTPRE activity raises PDE2A's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without PTPRE | 0.081 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers PDE2A's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers PDE2A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LUCAT1]] | C | LUCAT1 activity raises PDE2A's level | lines that do not express LUCAT1 (8) vs lines expressing it (42) | 2.57× lower at baseline in the lines without LUCAT1 | 0.007 | ⚠ within organs, on part of the lines; also absent: TBILA, C3orf52, SPAG16; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LUCAT1]] | C | PDE2A activity raises LUCAT1's level | lines that do not express PDE2A (4) vs lines expressing it (46) | 5.06× lower at baseline in the lines without PDE2A | 0.024 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GOLGA8N, TMEFF1, LUCAT1; maybe low, not absent; co-absent with the target |
| [[BLZF1]] | C | PDE2A activity raises BLZF1's level | lines that do not express PDE2A (4) vs lines expressing it (46) | 1.82× lower at baseline in the lines without PDE2A | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GOLGA8N, TMEFF1, LUCAT1; maybe low, not absent |
| [[PITRM1-AS1]] | C | PDE2A activity raises PITRM1-AS1's level | lines that do not express PDE2A (4) vs lines expressing it (46) | 1.77× lower at baseline in the lines without PDE2A | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GOLGA8N, TMEFF1, LUCAT1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.3, -2.4); signed map (-0.0, 46.4). **Vector** length 113, 28.7% of its response variance represented; |z| ≥ 3 in 1,274 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.7 | +1.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +4.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.9 | +3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.4 | +5.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.2 | +2.0 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.4 | -5.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.3 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.1 | -3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.9 | -5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.8 | -4.7 |
|  | [[Binimetinib (drug)]] 0.5 µM | ⚠ position correction uncertain | -4.7 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.5 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | phosphodiesterase 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:72,576,141-72,674,591 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phosphodiesterases; MicroRNA protein coding host genes |
| Reactome | 7 pathways, smallest: cGMP effects; Nitric oxide stimulates guanylate cyclase; Platelet homeostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [O00408](https://www.uniprot.org/uniprotkb/O00408) (cGMP-dependent 3',5'-cyclic phosphodiesterase):

> cGMP-activated cyclic nucleotide phosphodiesterase with a dual-specificity for the second messengers cAMP and cGMP, which are key regulators of many important physiological processes. Has a higher efficiency with cGMP compared to cAMP. Plays a role in cell growth and migration.; [Isoform PDE2A2]: Regulates mitochondrial cAMP levels and respiration (By similarity). Involved in the regulation of mitochondria morphology/dynamics and apoptotic cell death via local modulation of cAMP/PKA signaling …

**Summary**, from NCBI Gene [5138](https://www.ncbi.nlm.nih.gov/gene/5138):

> Enables several functions, including 3',5'-cyclic-nucleotide phosphodiesterase activity; anion binding activity; and metal ion binding activity. Involved in several processes, including cGMP catabolic process; cellular response to cytokine stimulus; and regulation of vascular permeability. Located in several cellular components, including cytosol; mitochondrial membrane; and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:8777](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8777) · Entrez [5138](https://www.ncbi.nlm.nih.gov/gene/5138) · UniProt [O00408](https://www.uniprot.org/uniprotkb/O00408) · Ensembl [ENSG00000186642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186642)

## Data

Gene col 11840: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11840); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11840, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11840]; `tensor/DDL_lfc|DDL_z.npy` [11840]; `embed/gene_vectors.npy` [11840]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11840 or target_col == 11840). Every well: [[PDE2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
