---
symbol: "C5orf24"
type: "gene"
col: 11224
ensembl_id: "ENSG00000181904"
name: "chromosome 5 open reading frame 24"
location: "5q31.1"
module: 51
arm: "+"
pooled_cpm: 45.12
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# C5orf24

*chromosome 5 open reading frame 24* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.98× (z +11.1, q 8e-26, up in 39 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.38× (z +5.2, q 2e-05, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.469× (z -6.4, q 9e-08, down in 36 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCOA5]] (+0.61, fdr 7e-06), [[DNAH14]] (+0.57, fdr 1e-05), [[EXOSC6]] (+0.55, fdr 1e-05); moves opposite to [[VSIG10L]] (-0.50, fdr 3e-05), [[KATNB1]] (-0.49, fdr 4e-05), [[LINC02656]] (-0.48, fdr 3e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ALDH2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11224.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +11.1 | 8e-26 | 39/47 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.98×** | +10.7 | 4e-24 | 42/47 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +10.1 | 8e-22 | 35/42 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +8.5 | 3e-15 | 30/45 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +5.2 | 2e-05 | 31/48 (A-172, HS-578T, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +4.9 | 8e-05 | 26/48 (A498, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.33×** | +4.6 | 3e-04 | 25/48 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.28×** | +4.0 | 0.005 | 25/48 (HOP62, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.008 | 24/48 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.025 | 19/47 (A-427, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.026 | 20/48 (NCI-H460, PANC-1, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.052 | 12/48 (HT-29, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.052 | 13/46 (NCI-H460, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.052 | 15/48 (C32, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.2 | 0.052 | 20/45 (NCI-H1792, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.070 | 13/48 (KATO III, SW 1088, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11224.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.469×** | -6.4 | 9e-08 | 36/49 (A-427, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.707×** | -5.6 | 6e-06 | 33/48 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.523×** | -5.5 | 8e-06 | 29/48 (A-427, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.748×** | -4.7 | 4e-04 | 29/48 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -4.4 | 0.001 | 0/48 | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.764×** | -4.1 | 0.004 | 26/48 (SK-MEL-2, J82, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.811×** | -3.4 | 0.058 | 18/48 (PANC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.823× | -3.1 | 0.12 | 19/47 (HepG2/C3A, PANC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.874× | -3.1 | 0.14 | 21/48 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11224. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 64.6 | 0 | 4 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.381× (z -14.0) |
| [[HOP62 (line)]] | alt | 40.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +11.2) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 44.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 24.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 44.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 52.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 58.9 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.65× (z +10.3) ⚠ toxic | — |
| [[Hs 766T (line)]] | wt | 61.5 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.64× (z +9.5) ⚠ toxic | — |
| [[SK-MEL-2 (line)]] | alt | 62.8 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.273× (z -12.2) |
| [[A549 (line)]] | wt | 32.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +10.2) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 32.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.21× (z +9.5) ⚠ toxic | — |
| [[LOX-IMVI (line)]] | wt | 45.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.77× (z +9.0) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 69.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -10.0) ⚠ cell-cycle shift, explains ~4% of this change |
| [[NCI-H460 (line)]] | wt | 57.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +10.2) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 39.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +9.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 38.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 46.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0820× (z -15.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 50.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.33× (z +9.3) ⚠ toxic | — |
| [[A498 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 59.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11224), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCOA5]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[DNAH14]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[EXOSC6]] | +0.55 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[MATR3-1]] | +0.54 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[TLCD5]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[COA7]] | +0.51 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[MAPK1IP1L]] | +0.51 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[ZNF260]] | +0.50 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[RPL7L1]] | +0.50 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[GCFC2]] | +0.50 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[ADNP]] | +0.50 | +0.38 / +0.53 | both halves | 7e-05 |  |
| [[STAT5B]] | +0.49 | +0.44 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VSIG10L]] | -0.50 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[KATNB1]] | -0.49 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[LINC02656]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[XAB2]] | -0.47 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[ZNHIT1]] | -0.47 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[EEF1G]] | -0.47 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[NEDD8]] | -0.46 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[NUCB1]] | -0.46 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[GDAP2]] | -0.46 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[RELCH]] | -0.46 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[SAP130]] | -0.45 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[KDELR1]] | -0.45 | -0.56 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALDH2]] | B | ALDH2 activity lowers C5orf24's level | lines that do not express ALDH2 (9) vs lines expressing it (41) | 1.26× higher at baseline in the lines without ALDH2 | 0.047 | ⚠ within organs, on part of the lines; also absent: MTARC2, SLC12A7; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises C5orf24's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.411). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (4.2, -38.8); signed map (8.0, -45.1). **Vector** length 82.2, 18.6% of its response variance represented; |z| ≥ 3 in 756 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.4 | +10.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.5 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +4.5 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.8 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +5.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -7.9 | -3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.6 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.0 | -5.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -5.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 5 open reading frame 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:134,845,680-134,859,735 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37562 |
| Matched by | ensembl_id |

UniProt [Q7Z6I8](https://www.uniprot.org/uniprotkb/Q7Z6I8) carries no function annotation.

**Summary**, from NCBI Gene [134553](https://www.ncbi.nlm.nih.gov/gene/134553):

> Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26746](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26746) · Entrez [134553](https://www.ncbi.nlm.nih.gov/gene/134553) · UniProt [Q7Z6I8](https://www.uniprot.org/uniprotkb/Q7Z6I8) · Ensembl [ENSG00000181904](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181904)

## Data

Gene col 11224: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11224); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11224, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11224]; `tensor/DDL_lfc|DDL_z.npy` [11224]; `embed/gene_vectors.npy` [11224]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11224 or target_col == 11224). Every well: [[C5orf24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C5orf24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
