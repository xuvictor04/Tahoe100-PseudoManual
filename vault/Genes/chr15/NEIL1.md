---
symbol: "NEIL1"
type: "gene"
col: 6403
ensembl_id: "ENSG00000140398"
name: "nei like DNA glycosylase 1"
location: "15q24.2"
module: 46
arm: "+"
pooled_cpm: 2.54
n_lines_expressing: 44
n_dd_up: 5
n_dd_down: 17
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# NEIL1

*nei like DNA glycosylase 1* — 15q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.32× (z +7.3, q 1e-10, up in 2 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 1.46× (z +3.4, q 0.067, up in 10 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.330× (z -10.1, q 3e-21, down in 25 of 34 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOTAIR]] (+0.66, fdr 1e-04), [[FCGRT]] (+0.65, fdr 1e-05), [[CES3]] (+0.63, fdr 2e-05); moves opposite to [[NAA10]] (-0.55, fdr 3e-04, ⚠ NAA10 in the vector space only through flagged drug-doses), [[RNF216]] (-0.54, fdr 1e-04), [[SH3BGRL3]] (-0.53, fdr 3e-04), [[KCTD20]] (-0.53, fdr 1e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PLUT]] → it (grade B ⚠); 2 go from it, the strongest it → [[ZNF514]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6403.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +7.3 | 1e-10 | 2/3 (NCI-H2347, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +6.6 | 1e-08 | 1/10 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.52×** | +5.4 | 1e-05 | 8/36 (LoVo, SW480, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +5.0 | 8e-05 | 2/5 (SW480, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.067 | 10/33 (CFPAC-1, Panc 03.27, …) | two highest doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 2.00× | +3.3 | 0.10 | 0/4 | top dose only | noisy plate (z scaled); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.97× | +3.2 | 0.10 | 0/4 | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.64× | +3.2 | 0.10 | 1/21 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | 1.41× | +3.1 | 0.11 | 3/38 (LoVo, NCI-H2030, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.41× | +3.1 | 0.12 | 0/11 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 0.5 µM |  | 1.40× | +3.0 | 0.12 | 4/24 (NCI-H2347, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6403.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.330×** | -10.1 | 3e-21 | 25/34 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.369×** | -9.1 | 3e-17 | 24/36 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.496×** | -6.4 | 3e-08 | 20/38 (SW480, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.505×** | -6.2 | 7e-08 | 19/34 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.543×** | -5.6 | 3e-06 | 23/36 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.548×** | -5.5 | 4e-06 | 13/23 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.554×** | -5.4 | 6e-06 | 12/37 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.558×** | -5.3 | 7e-06 | 15/19 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.558×** | -5.1 | 2e-05 | 17/34 (LoVo, COLO 205, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.583×** | -4.9 | 5e-05 | 18/31 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.587×** | -4.9 | 6e-05 | 17/35 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.600×** | -4.7 | 2e-04 | 17/36 (NCI-H2030, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.660×** | -3.8 | 0.006 | 5/38 (CHP-212, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.673×** | -3.6 | 0.012 | 15/30 (COLO 205, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.484×** | -3.5 | 0.020 | 5/28 (CFPAC-1, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.696×** | -3.2 | 0.048 | 4/37 (MIA PaCa-2, hTERT-HPNE, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6403. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 11.0 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0453× (z -12.8) |
| [[SW480 (line)]] | alt | 4.47 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0514× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.139× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 6.96 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.0540× (z -12.5) |
| [[COLO 205 (line)]] | alt | 5.89 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0584× (z -8.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 3.96 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 2.01 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0782× (z -8.7) |
| [[SW1417 (line)]] | alt | 3.39 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0446× (z -9.7) |
| [[A-172 (line)]] | wt | 0.676 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.563 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.826 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.600 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.974 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.872 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.840 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.917 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.628 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.969 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.947 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6403), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOTAIR]] | +0.66 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[FCGRT]] | +0.65 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[CES3]] | +0.63 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[ZNF362]] | +0.62 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[DMTN]] | +0.61 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[KRBA2]] | +0.60 | +0.37 / +0.41 | both halves | 8e-05 |  |
| [[PLXNB3-AS1]] | +0.60 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[BANK1]] | +0.60 | +0.54 / +0.31 | both halves | 2e-04 |  |
| [[TMEM198B]] | +0.59 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[ACCS]] | +0.58 | +0.44 / +0.37 | both halves | 8e-05 |  |
| [[SH2B1]] | +0.57 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[PGAP3]] | +0.56 | +0.52 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA10]] ⚠ | -0.55 | -0.28 / -0.39 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RNF216]] | -0.54 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[SH3BGRL3]] | -0.53 | -0.36 / -0.28 | both halves | 3e-04 |  |
| [[KCTD20]] | -0.53 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[EHD4]] | -0.52 | -0.37 / -0.27 | both halves | 3e-04 |  |
| [[PUSL1]] | -0.52 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[KIAA1328]] | -0.52 | -0.31 / -0.31 | both halves | 2e-04 |  |
| [[DGKD]] | -0.52 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[ARHGEF10]] | -0.52 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[EPIC1]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[CLTCL1]] | -0.50 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[SH3PXD2B]] | -0.50 | -0.36 / -0.29 | both halves | 2e-04 |  |
| [[PCMT1]] | -0.49 | -0.30 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLUT]] | B | PLUT activity raises NEIL1's level | lines that do not express PLUT (23) vs lines expressing it (27) | 1.45× lower at baseline in the lines without PLUT | 0.058 | ⚠ within organs, on part of the lines; also absent: SHROOM3, MST1R, KCNK5; maybe low, not absent |
| [[OPRD1]] | B | OPRD1 activity raises NEIL1's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 1.43× lower at baseline in the lines without OPRD1 | 0.089 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF514]] | B | NEIL1 activity raises ZNF514's level | lines that do not express NEIL1 (6) vs lines expressing it (44) | 1.98× lower at baseline in the lines without NEIL1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ANO7, PM20D2; maybe low, not absent; its own permutation p |
| [[MINDY1]] | B | NEIL1 activity raises MINDY1's level | lines that do not express NEIL1 (6) vs lines expressing it (44) | 1.42× lower at baseline in the lines without NEIL1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ANO7, PM20D2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.582). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-0.3, 29.7); signed map (38.4, -14.2). **Vector** length 41.9, 5.08% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +3.1 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.0 | +0.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.1 | -5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.0 | -5.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.8 | -6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.7 | -10.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -1.5 | -6.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.1 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -4.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | nei like DNA glycosylase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.2 — chr15:75,346,955-75,357,115 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22402, hFPG1, NEI1, FPG1 |
| Gene groups (HGNC) | DNA glycosylases; DNA-(apurinic or apyrimidinic site) lyases |
| Reactome | 10 pathways, smallest: Diseases of Base Excision Repair; APEX1-Independent Resolution of AP Sites via the Single Nucleotide Replacement Pathway; Cleavage of the damaged pyrimidine |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FI4](https://www.uniprot.org/uniprotkb/Q96FI4) (Endonuclease 8-like 1):

> Involved in base excision repair of DNA damaged by oxidation or by mutagenic agents. Acts as a DNA glycosylase that recognizes and removes damaged bases. Has a preference for oxidized pyrimidines, such as thymine glycol, formamidopyrimidine (Fapy) and 5-hydroxyuracil. Has marginal activity towards 8-oxoguanine. Has AP (apurinic/apyrimidinic) lyase activity and introduces nicks in the DNA strand. Cleaves the DNA backbone by beta-delta elimination to generate a single-strand break at the site of …

**Summary**, from NCBI Gene [79661](https://www.ncbi.nlm.nih.gov/gene/79661):

> This gene is a member of the Nei endonuclease VIII-like gene family which encodes DNA glycosylases. The encoded enzyme participates in the DNA repair pathway by initiating base excision repair by removing damaged bases, primarily oxidized pyrimidines. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:18448](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18448) · Entrez [79661](https://www.ncbi.nlm.nih.gov/gene/79661) · UniProt [Q96FI4](https://www.uniprot.org/uniprotkb/Q96FI4) · Ensembl [ENSG00000140398](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140398)

## Data

Gene col 6403: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6403); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6403, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6403]; `tensor/DDL_lfc|DDL_z.npy` [6403]; `embed/gene_vectors.npy` [6403]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6403 or target_col == 6403). Every well: [[NEIL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEIL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
