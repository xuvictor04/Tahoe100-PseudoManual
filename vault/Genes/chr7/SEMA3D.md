---
symbol: "SEMA3D"
type: "gene"
col: 7760
ensembl_id: "ENSG00000153993"
name: "semaphorin 3D"
location: "7q21.11"
module: 19
arm: "+"
pooled_cpm: 35.52
n_lines_expressing: 19
n_dd_up: 20
n_dd_down: 21
n_dd_up_clean: 16
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SEMA3D

*semaphorin 3D* — 7q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.99× (z +13.2, q 7e-37, up in 2 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +5.9, q 9e-07, up in 2 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.647× (z -5.4, q 3e-05, down in 8 of 16 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.674× (z -4.9, q 2e-04, down in 12 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01035]] (+0.67, fdr 8e-06), [[TNFRSF11B]] (+0.67, fdr 7e-06), [[GLP2R]] (+0.66, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[MIR99AHG]] → it (grade C ⚠); 3 go from it, the strongest it → [[SEMA3A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7760.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.99×** | +13.2 | 7e-37 | 2/12 (H4, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.73×** | +12.6 | 1e-33 | 4/15 (CFPAC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.9 | 9e-07 | 2/16 (hTERT-HPNE, CHP-212) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +5.3 | 2e-05 | 3/13 (RKO, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +4.9 | 1e-04 | 4/17 (MIA PaCa-2, SNU-423, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.44×** | +4.4 | 1e-03 | 6/15 (MIA PaCa-2, C-33 A, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.003 | 6/17 (MIA PaCa-2, C-33 A, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.004 | 6/15 (C-33 A, MIA PaCa-2, …) | rises with dose |  |
| [[Alpelisib (drug)]] 5 µM |  | **1.81×** | +3.9 | 0.007 | 2/14 (MIA PaCa-2, SNU-423) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.013 | 4/15 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.023 | 1/15 (SNU-423) | top dose only | position effect removed |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.023 | 2/16 (CHP-212, CFPAC-1) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.32×** | +3.5 | 0.024 | 0/15 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Afatinib (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.028 | 0/16 | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.028 | 2/15 (A-427, C-33 A) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.041 | 4/17 (SNU-423, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Meloxicam (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.043 | 0/15 | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.062 | 1/15 (CFPAC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.60×** | +3.1 | 0.063 | 6/16 (A-172, hTERT-HPNE, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7760.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.647×** | -5.4 | 3e-05 | 8/16 (SW480, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.674×** | -4.9 | 2e-04 | 12/15 (RKO, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.698×** | -4.5 | 0.001 | 8/15 (NCI-H460, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.781×** | -4.4 | 0.002 | 15/17 (NCI-H460, A-172, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.711×** | -4.3 | 0.002 | 8/15 (NCI-H460, A-172, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.713×** | -4.2 | 0.002 | 6/16 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.722×** | -4.1 | 0.004 | 8/16 (C-33 A, A-427, …) | top dose only |  |
| [[vincristine (drug)]] 0.05 µM |  | **0.714×** | -4.0 | 0.005 | 5/17 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.736×** | -3.8 | 0.008 | 5/16 (NCI-H1792, H4, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.564×** | -3.7 | 0.010 | 8/15 (A-427, RKO, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.745×** | -3.7 | 0.012 | 11/16 (SW480, C-33 A, …) | rises with dose | position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.728×** | -3.7 | 0.012 | 1/16 (SW 1271) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.754×** | -3.5 | 0.019 | 8/16 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 0.5 µM |  | **0.764×** | -3.4 | 0.032 | 4/16 (C-33 A, RKO, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.767×** | -3.3 | 0.035 | 3/16 (NCI-H460, C-33 A, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.784×** | -3.0 | 0.071 | 4/15 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.782×** | -2.9 | 0.087 | 5/17 (NCI-H1792, NCI-H460, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **0.790×** | -2.9 | 0.087 | 7/16 (NCI-H1792, H4, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 5 µM |  | **0.784×** | -2.9 | 0.092 | 1/16 (SW 1271) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7760. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 187 | 0 | 18 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -18.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -15.0) |
| [[SW480 (line)]] | alt | 53.1 | 0 | 14 (10 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0727× (z -19.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.253× (z -10.1) |
| [[C-33 A (line)]] | alt | 1,270 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -14.3) |
| [[RKO (line)]] | wt | 51.1 | 2 (2 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 5.34× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | [[Auranofin (drug)]] 5 µM 0.0867× (z -14.9) |
| [[A-427 (line)]] | wt | 28.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0852× (z -16.2) |
| [[MIA PaCa-2 (line)]] | alt | 27.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0859× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.39 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.33 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.95 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.98 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.35 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.08 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.15 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.97 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 375 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.71 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.36 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.40 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.21 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.87 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.84 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7760), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01035]] | +0.67 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[TNFRSF11B]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[GLP2R]] | +0.66 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[LINC03000]] | +0.66 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[BMP5]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[GREM2]] | +0.66 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[LINC01967]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[TBXT]] ⚠ | +0.64 | +0.48 / +0.65 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PDE7B]] | +0.64 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[GASK1B]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[CDH7]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[PAX7]] | +0.62 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[CHL1]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR99AHG]] | C | MIR99AHG activity raises SEMA3D's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 4.96× lower at baseline in the lines without MIR99AHG | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |
| [[IGSF1]] | C | IGSF1 activity raises SEMA3D's level | lines that do not express IGSF1 (33) vs lines expressing it (17) | 1.93× lower at baseline in the lines without IGSF1 | 0.069 | ⚠ within organs, on part of the lines; also absent: LINC01885, ZNF208, ENSG00000233358; co-absent with the target |
| [[ADGRL3]] | C | ADGRL3 activity raises SEMA3D's level | lines that do not express ADGRL3 (25) vs lines expressing it (25) | 3.05× lower at baseline in the lines without ADGRL3 | 0.074 | ⚠ within organs, on part of the lines; also absent: CDH18, GRIA2, NTNG1; maybe low, not absent; co-absent with the target |
| [[COL5A2]] | C | COL5A2 activity raises SEMA3D's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 3.09× lower at baseline in the lines without COL5A2 | 0.077 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2; co-absent with the target |
| [[COL8A1]] | C | COL8A1 activity raises SEMA3D's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 2.28× lower at baseline in the lines without COL8A1 | 0.083 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |
| [[CHL1]] | C | CHL1 activity raises SEMA3D's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 3.09× lower at baseline in the lines without CHL1 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168; co-absent with the target |
| [[EPB41L3]] | C | EPB41L3 activity raises SEMA3D's level | lines that do not express EPB41L3 (34) vs lines expressing it (16) | 2.26× lower at baseline in the lines without EPB41L3 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PAX3, ROBO2, PTH2R; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA3A]] | C | SEMA3D activity raises SEMA3A's level | lines that do not express SEMA3D (31) vs lines expressing it (19) | 4.18× lower at baseline in the lines without SEMA3D | 0.001 | ⚠ within organs, on part of the lines; also absent: COL3A1, HS3ST3A1, THY1; co-absent with the target |
| [[COL5A2]] | C | SEMA3D activity raises COL5A2's level | lines that do not express SEMA3D (31) vs lines expressing it (19) | 4.55× lower at baseline in the lines without SEMA3D | 0.068 | ⚠ within organs, on part of the lines; also absent: COL3A1, HS3ST3A1, THY1; co-absent with the target |
| [[MIR99AHG]] | C | SEMA3D activity raises MIR99AHG's level | lines that do not express SEMA3D (31) vs lines expressing it (19) | 2.58× lower at baseline in the lines without SEMA3D | 0.0995 | ⚠ within organs, on part of the lines; also absent: COL3A1, HS3ST3A1, THY1; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.676). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.1, 35.1); signed map (43.3, 42.3). **Vector** length 61.2, 19.7% of its response variance represented; |z| ≥ 3 in 448 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +5.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.1 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | +0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +4.0 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.4 | -2.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -2.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | semaphorin 3D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.11 — chr7:84,995,553-85,187,056 (-) |
| Ensembl biotype | protein_coding |
| Also known as | coll-2, Sema-Z2 |
| Gene groups (HGNC) | V-set domain containing; Semaphorins |
| Matched by | ensembl_id |

**Function**, from UniProt [O95025](https://www.uniprot.org/uniprotkb/O95025) (Semaphorin-3D):

> Induces the collapse and paralysis of neuronal growth cones. Could potentially act as repulsive cues toward specific neuronal populations. Binds to neuropilin (By similarity).

**Summary**, from NCBI Gene [223117](https://www.ncbi.nlm.nih.gov/gene/223117):

> This gene encodes a member of the semaphorin III family of secreted signaling proteins that are involved in axon guidance during neuronal development. The encoded protein contains an N-terminal Sema domain, an immunoglobulin like domain and a C-terminal basic domain. The protein encoded by this gene binds neuropilin and plays an important role in cardiovascular development. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:10726](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10726) · Entrez [223117](https://www.ncbi.nlm.nih.gov/gene/223117) · UniProt [O95025](https://www.uniprot.org/uniprotkb/O95025) · Ensembl [ENSG00000153993](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153993)

## Data

Gene col 7760: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7760); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7760, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7760]; `tensor/DDL_lfc|DDL_z.npy` [7760]; `embed/gene_vectors.npy` [7760]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7760 or target_col == 7760). Every well: [[SEMA3D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEMA3D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
