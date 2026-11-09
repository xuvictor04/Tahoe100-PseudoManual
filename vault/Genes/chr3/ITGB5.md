---
symbol: "ITGB5"
type: "gene"
col: 1355
ensembl_id: "ENSG00000082781"
name: "integrin subunit beta 5"
location: "3q21.2"
module: 174
arm: "+"
pooled_cpm: 147.22
n_lines_expressing: 48
n_dd_up: 0
n_dd_down: 63
n_dd_up_clean: 0
n_dd_down_clean: 51
in_vector_space: true
direction_upstream: 20
direction_downstream: 0
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# ITGB5

*integrin subunit beta 5* — 3q21.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 3.66×).
> Pooled over the cell lines (median), lowered significantly by 63 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.352× (z -25.9, q 0e+00, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHC2]] (+0.79, fdr 7e-06), [[ETV4]] (+0.79, fdr 7e-06), [[SPRY4-AS1]] (+0.78, fdr 7e-06).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[DIO3OS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1355.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 3.66×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | 1.15× | +3.6 | 0.15 | 13/47 (CFPAC-1, SK-MEL-2, …) | top dose only |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.21× | +3.2 | 0.31 | 20/46 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.13× | +3.1 | 0.31 | 8/46 (A-172, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 71 in all, 18 with an alert ⚠; shown: the 15 strongest. 63 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1355.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.352×** | -25.9 | 0e+00 | 42/46 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.383×** | -17.2 | 0e+00 | 43/48 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.366×** | -16.9 | 0e+00 | 41/45 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.392×** | -16.4 | 0e+00 | 44/46 (HepG2/C3A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.395×** | -16.3 | 0e+00 | 42/47 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.406×** | -15.8 | 0e+00 | 42/46 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.397×** | -15.6 | 0e+00 | 43/46 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.505×** | -14.9 | 0e+00 | 41/46 (NCI-H1573, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.437×** | -14.5 | 1e-45 | 42/46 (SK-MEL-2, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.454×** | -14.4 | 6e-45 | 42/47 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.445×** | -14.2 | 7e-44 | 46/46 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.445×** | -13.7 | 1e-40 | 35/46 (NCI-H1573, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.528×** | -13.4 | 3e-39 | 39/46 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.597×** | -12.8 | 1e-35 | 39/47 (HepG2/C3A, A549, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.475×** | -12.1 | 6e-32 | 40/46 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1355. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 156 | 0 | 34 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -25.9) |
| [[HepG2_C3A (line)]] | wt | 367 | 0 | 27 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.134× (z -21.9) |
| [[SK-MEL-2 (line)]] | alt | 277 | 0 | 26 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -28.5) |
| [[SW480 (line)]] | alt | 215 | 0 | 26 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.247× (z -18.5) |
| [[HOP62 (line)]] | alt | 144 | 0 | 24 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.590× (z -21.6) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.194× (z -18.4) |
| [[LoVo (line)]] | wt | 164 | 0 | 22 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -22.4) |
| [[NCI-H1573 (line)]] | alt | 162 | 0 | 20 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -27.6) |
| [[A549 (line)]] | wt | 334 | 0 | 19 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -25.2) |
| [[SW 900 (line)]] | alt | 257 | 0 | 19 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -25.1) |
| [[AsPC-1 (line)]] | alt | 155 | 0 | 18 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -15.0) |
| [[C32 (line)]] | wt | 144 | 0 | 18 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -22.9) |
| [[NCI-H23 (line)]] | alt | 127 | 0 | 18 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -23.4) |
| [[LS 180 (line)]] | wt | 137 | 0 | 17 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.256× (z -11.2) |
| [[PANC-1 (line)]] | alt | 214 | 0 | 17 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 114 | 0 | 16 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -25.9) |
| [[NCI-H1792 (line)]] | alt | 158 | 0 | 16 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -18.4) |
| [[Panc 03.27 (line)]] | alt | 133 | 0 | 16 | — | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -14.3) |
| [[HS-578T (line)]] | alt | 182 | 0 | 15 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -19.7) |
| [[NCI-H2030 (line)]] | alt | 333 | 0 | 15 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -28.7) |
| [[J82 (line)]] | alt | 130 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -16.8) |
| [[CFPAC-1 (line)]] | alt | 68.9 | 0 | 11 | — | [[Binimetinib (drug)]] 0.5 µM 0.317× (z -13.3) |
| [[Hs 766T (line)]] | wt | 114 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -14.4) |
| [[RKO (line)]] | wt | 90.1 | 0 | 10 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.189× (z -16.4) |
| [[RPMI-7951 (line)]] | alt | 174 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -21.2) |
| [[SW48 (line)]] | wt | 114 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -15.0) |
| [[LOX-IMVI (line)]] | wt | 84.3 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -17.6) |
| [[BT-474 (line)]] | alt | 167 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -15.6) |
| [[MIA PaCa-2 (line)]] | alt | 56.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -13.2) |
| [[SNU-423 (line)]] | alt | 108 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -21.2) |
| [[SW1417 (line)]] | alt | 143 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.399× (z -11.8) |
| [[H4 (line)]] | wt | 90.8 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.239× (z -10.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -9.7) |
| [[HT-29 (line)]] | alt | 133 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.324× (z -11.7) |
| [[NCI-H2347 (line)]] | alt | 102 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.531× (z -9.5) |
| [[SHP-77 (line)]] | alt | 52.0 | 0 | 3 | — | [[Binimetinib (drug)]] 0.05 µM 0.351× (z -8.8) |
| [[A-427 (line)]] | wt | 76.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -11.9) |
| [[COLO 205 (line)]] | alt | 101 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.66× (z +11.2) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.356× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 102 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -10.7) |
| [[A-172 (line)]] | wt | 72.9 | 0 | 1 | — | [[Trametinib (drug)]] 5 µM 0.399× (z -8.6) |
| [[AN3 CA (line)]] | alt | 85.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -11.8) |
| [[C-33 A (line)]] | alt | 53.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -8.9) |
| [[CHP-212 (line)]] | wt | 80.3 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.134× (z -9.5) |
| [[HCT15 (line)]] | alt | 85.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.256× (z -10.9) |
| [[SW 1271 (line)]] | alt | 161 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0854× (z -14.9) |
| [[A498 (line)]] | wt | 85.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 18.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 85.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1355), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHC2]] | +0.79 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[ETV4]] | +0.79 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[SPRY4-AS1]] | +0.78 | +0.74 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[SPRY4]] | +0.78 | +0.77 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[SPRED2]] | +0.78 | +0.78 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[DUSP6]] | +0.76 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.75 | +0.79 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 980 |
| [[NPAS2]] | +0.74 | +0.78 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[DUSP4]] | +0.74 | +0.69 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[NT5E]] | +0.73 | +0.75 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[SPRED1]] | +0.73 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[ETV5]] | +0.72 | +0.78 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 17, C 3. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DIO3OS]] | B | DIO3OS activity raises ITGB5's level | lines that do not express DIO3OS (25) vs lines expressing it (25) | 1.61× lower at baseline in the lines without DIO3OS | 0.011 | ⚠ within organs, on part of the lines; also absent: NPSR1-AS1, ENSG00000258919, TOX3 |
| [[TBC1D8]] | B | TBC1D8 activity raises ITGB5's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 1.83× lower at baseline in the lines without TBC1D8 | 0.019 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[TBC1D8]] | B | TBC1D8 activity strengthens ITGB5's drug response | lines that do not express TBC1D8 (5) vs lines expressing it (43) | the lines without TBC1D8 respond 0.82× as strongly (z diff +2.19); strongest at Binimetinib 5 µM: 0.70x vs 0.42x (z diff +4.5) | 0.020 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[RAB32]] | B | RAB32 activity raises ITGB5's level | lines that do not express RAB32 (7) vs lines expressing it (43) | 1.59× lower at baseline in the lines without RAB32 | 0.027 | ⚠ within organs, on part of the lines; also absent: PTPRH, INPP4B, ENSG00000285155 |
| [[NPAS2]] | B | NPAS2 activity raises ITGB5's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 1.67× lower at baseline in the lines without NPAS2 | 0.029 | ⚠ within organs, on part of the lines |
| [[S100A16]] | B | S100A16 activity raises ITGB5's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 2.11× lower at baseline in the lines without S100A16 | 0.037 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[SMOX]] | B | SMOX activity raises ITGB5's level | lines that do not express SMOX (6) vs lines expressing it (44) | 2.60× lower at baseline in the lines without SMOX | 0.042 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[ITGA2]] | B | ITGA2 activity raises ITGB5's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 1.82× lower at baseline in the lines without ITGA2 | 0.042 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[ADGRE2]] | B | ADGRE2 activity raises ITGB5's level | lines that do not express ADGRE2 (25) vs lines expressing it (25) | 1.50× lower at baseline in the lines without ADGRE2 | 0.042 | ⚠ within organs, on part of the lines; also absent: CRLF2, ENSG00000272297, RSPO3 |
| [[MYEOV]] | B | MYEOV activity raises ITGB5's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 1.28× lower at baseline in the lines without MYEOV | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |
| [[MAP2K1]] | B | MAP2K1 activity raises ITGB5's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 9.8% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NIBAN2]] | B | NIBAN2 activity raises ITGB5's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 3.11× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.856). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.1, 6.0); signed map (7.9, 47.7). **Vector** length 131, 52.0% of its response variance represented; |z| ≥ 3 in 2,177 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.6 | -14.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.4 | -14.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | -16.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +3.3 | +2.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.3 | -7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | -1.3 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +3.2 | +1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +0.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.9 | +3.6 |
| fall | [[Trametinib (drug)]] 5 µM |  | -14.2 | -17.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -13.8 | -14.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -13.0 | -16.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -12.9 | -14.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -12.7 | -16.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -12.5 | -15.6 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit beta 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.2 — chr3:124,761,948-124,901,418 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Integrin beta subunits |
| Hallmark sets | MYOGENESIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 16 pathways, smallest: Cross-presentation of particulate exogenous antigens (phagosomes); Syndecan interactions; Molecules associated with elastic fibres |
| Matched by | ensembl_id |

**Function**, from UniProt [P18084](https://www.uniprot.org/uniprotkb/P18084) (Integrin beta-5):

> Integrin alpha-V/beta-5 (ITGAV:ITGB5) is a receptor for fibronectin. It recognizes the sequence R-G-D in its ligand.; (Microbial infection) Integrin ITGAV:ITGB5 acts as a receptor for adenovirus type C.

**Summary**, from NCBI Gene [3693](https://www.ncbi.nlm.nih.gov/gene/3693):

> This gene encodes a beta subunit of integrin, which can combine with different alpha chains to form a variety of integrin heterodimers. Integrins are integral cell-surface receptors that participate in cell adhesion as well as cell-surface mediated signaling. The alphav beta5 integrin is involved in adhesion to vitronectin. [provided by RefSeq, Aug 2017]

**Accessions** — [HGNC:6160](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6160) · Entrez [3693](https://www.ncbi.nlm.nih.gov/gene/3693) · UniProt [P18084](https://www.uniprot.org/uniprotkb/P18084) · Ensembl [ENSG00000082781](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082781)

## Data

Gene col 1355: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1355); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1355, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1355]; `tensor/DDL_lfc|DDL_z.npy` [1355]; `embed/gene_vectors.npy` [1355]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1355 or target_col == 1355). Every well: [[ITGB5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGB5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
