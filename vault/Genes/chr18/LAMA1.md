---
symbol: "LAMA1"
type: "gene"
col: 2165
ensembl_id: "ENSG00000101680"
name: "laminin subunit alpha 1"
location: "18p11.31"
module: 116
arm: "+"
pooled_cpm: 29.87
n_lines_expressing: 19
n_dd_up: 36
n_dd_down: 10
n_dd_up_clean: 24
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 7
direction_downstream: 26
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# LAMA1

*laminin subunit alpha 1* — 18p11.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.56× (z +14.6, q 1e-45, up in 6 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.58× (z +7.6, q 6e-12, up in 7 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.578× (z -6.1, q 8e-07, down in 6 of 16 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LNCOG]] (+0.61, fdr 1e-05), [[IL13RA2]] (+0.61, fdr 1e-05), [[COLEC10]] (+0.60, fdr 1e-05); moves opposite to [[SAMD11]] (-0.43, fdr 6e-05), [[NCOA2]] (-0.41, fdr 4e-05), [[ANKRD54]] (-0.41, fdr 2e-04).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 26 go from it, the strongest it → [[DYRK3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2165.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.56×** | +14.6 | 1e-45 | 6/11 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.26×** | +14.1 | 7e-43 | 6/15 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.19×** | +8.6 | 1e-15 | 6/15 (SK-MEL-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +7.6 | 6e-12 | 7/17 (A-427, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +7.4 | 2e-11 | 7/16 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.81×** | +7.1 | 1e-10 | 9/16 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +6.6 | 4e-09 | 11/16 (A-172, C32, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +6.4 | 9e-09 | 11/16 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.1 | 6e-08 | 3/16 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.6 | 2e-06 | 2/16 (hTERT-HPNE, A-172) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +5.1 | 2e-05 | 9/16 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.08×** | +4.6 | 2e-04 | 13/16 (NCI-H460, A-172, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.66×** | +4.3 | 7e-04 | 2/16 (H4, SW 900) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.3 | 7e-04 | 5/16 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.001 | 6/17 (C32, H4, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.9 | 0.003 | 7/16 (NCI-H460, RKO, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 0.05 µM |  | **1.37×** | +3.8 | 0.005 | 7/17 (NCI-H460, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.009 | 0/16 | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.011 | 6/16 (NCI-H460, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.030 | 3/16 (H4, RKO, …) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.66×** | +3.2 | 0.035 | 1/17 (C32) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2165.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.578×** | -6.1 | 8e-07 | 6/16 (RKO, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.747×** | -4.9 | 2e-04 | 6/17 (NCI-H23, H4, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.656×** | -4.8 | 2e-04 | 11/16 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.692×** | -4.4 | 0.002 | 9/17 (NCI-H23, RKO, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.731×** | -3.7 | 0.017 | 12/16 (H4, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.731×** | -3.7 | 0.017 | 9/16 (hTERT-HPNE, RKO, …) | two highest doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.578×** | -3.4 | 0.050 | 4/17 (NCI-H23, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.792×** | -3.2 | 0.084 | 6/17 (NCI-H23, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.824×** | -3.2 | 0.091 | 0/17 | rises with dose |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.752×** | -3.2 | 0.092 | 1/16 (SW 900) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -3.1 | 0.10 | 3/17 (NCI-H23, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2165. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 10.6 | 6 (4 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 7.64× (z +12.9) | — |
| [[NCI-H23 (line)]] | alt | 51.8 | 2 (2 ⚠) | 2 (1 ⚠) | [[Belinostat (drug)]] 5 µM 4.00× (z +8.7) ⚠ cell-cycle shift, explains ~64% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -10.1) |
| [[A-172 (line)]] | wt | 15.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +11.5) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.64× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 11.7 | 0 | 2 | — | [[Phenytoin (sodium) (drug)]] 0.05 µM 0.0603× (z -9.0) |
| [[RKO (line)]] | wt | 70.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 407 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -9.9) |
| [[A498 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.26 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.10 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.79 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.78 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.63 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.74 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.33 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.91 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.59 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.65 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2165), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LNCOG]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[IL13RA2]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[COLEC10]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MCTP1]] | +0.54 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[CNST]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[RAB3B]] | +0.54 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[TFPI2]] | +0.53 | +0.55 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[RDUR]] | +0.53 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[FSTL5]] | +0.52 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[ADTRP]] | +0.52 | +0.40 / +0.56 | both halves | 4e-05 |  |
| [[SGIP1]] | +0.51 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[ESM1]] | +0.51 | +0.32 / +0.64 | both halves | 2e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD11]] | -0.43 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[NCOA2]] | -0.41 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[ANKRD54]] | -0.41 | -0.50 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises LAMA1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |
| [[MAP2K2]] | B | MAP2K2 activity raises LAMA1's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[SGIP1]] | C | SGIP1 activity raises LAMA1's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 2.41× lower at baseline in the lines without SGIP1 | 0.009 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG; co-absent with the target |
| [[LNCOG]] | C | LNCOG activity raises LAMA1's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 3.26× lower at baseline in the lines without LNCOG | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1; co-absent with the target |
| [[LCP1]] | C | LCP1 activity raises LAMA1's level | lines that do not express LCP1 (33) vs lines expressing it (17) | 2.49× lower at baseline in the lines without LCP1 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000237268, GRIN2A, ENSG00000234352; co-absent with the target |
| [[IL13RA2]] | C | IL13RA2 activity raises LAMA1's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 2.99× lower at baseline in the lines without IL13RA2 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3; co-absent with the target |
| [[ESM1]] | C | ESM1 activity raises LAMA1's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 2.66× lower at baseline in the lines without ESM1 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 17, C 9. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYRK3]] | B | LAMA1 activity raises DYRK3's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 3.07× lower at baseline in the lines without LAMA1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |
| [[C12orf50]] | B | LAMA1 activity raises C12orf50's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 1.61× lower at baseline in the lines without LAMA1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |
| [[DLC1]] | B | LAMA1 activity raises DLC1's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 2.47× lower at baseline in the lines without LAMA1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |
| [[RAB3B]] | B | LAMA1 activity raises RAB3B's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 1.90× lower at baseline in the lines without LAMA1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |
| cells under [[Doxorubicin (hydrochloride) (drug)]] 5 µM | B | LAMA1 activity lowers the cells' numbers under Doxorubicin (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express LAMA1 (31) vs lines expressing it (17) | the lines without LAMA1: 1.80× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |
| [[LINC02454]] | B | LAMA1 activity raises LINC02454's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 2.14× lower at baseline in the lines without LAMA1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |
| [[CD274]] | B | LAMA1 activity raises CD274's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 1.98× lower at baseline in the lines without LAMA1 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |
| cells under [[Pasireotide (acetate) (drug)]] 5 µM | B | LAMA1 activity lowers the cells' numbers under Pasireotide (acetate) 5 µM (makes them more sensitive) | lines that do not express LAMA1 (31) vs lines expressing it (17) | the lines without LAMA1: 1.15× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |
| [[CFAP58]] | B | LAMA1 activity raises CFAP58's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 1.51× lower at baseline in the lines without LAMA1 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | LAMA1 activity raises the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (protects the cells) | lines that do not express LAMA1 (31) vs lines expressing it (17) | the lines without LAMA1: 0.87× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |
| [[NCOA2]] | B | LAMA1 activity lowers NCOA2's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 1.27× higher at baseline in the lines without LAMA1 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |
| [[ERCC1]] | B | LAMA1 activity raises ERCC1's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 1.28× lower at baseline in the lines without LAMA1 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.568). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.9, 12.9); signed map (4.9, 53.9). **Vector** length 58.5, 18.9% of its response variance represented; |z| ≥ 3 in 415 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.5 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.2 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +4.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +3.6 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -6.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -2.2 | -4.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.8 | -4.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -3.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -3.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -1.5 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.5 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | laminin subunit alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.31 — chr18:6,941,742-7,117,797 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously LAMA |
| Gene groups (HGNC) | Laminin subunits |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 21 pathways, smallest: Attachment of bacteria to epithelial cells; Biofilm formation; Developmental Lineage of Pancreatic Ductal Cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P25391](https://www.uniprot.org/uniprotkb/P25391) (Laminin subunit alpha-1):

> Binding to cells via a high affinity receptor, laminin is thought to mediate the attachment, migration and organization of cells into tissues during embryonic development by interacting with other extracellular matrix components. As a ligand for alpha-dystroglycan, it is involved in a number of processes including epithelium branching morphogenesis, down-regulation of apoptotic signals in muscle via the activation of PI3K/AKT signaling, and activation of RAC1 signaling. As a subunit of …

**Summary**, from NCBI Gene [284217](https://www.ncbi.nlm.nih.gov/gene/284217):

> This gene encodes one of the alpha 1 subunits of laminin. The laminins are a family of extracellular matrix glycoproteins that have a heterotrimeric structure consisting of an alpha, beta and gamma chain. These proteins make up a major component of the basement membrane and have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Mutations in this gene may be associated with …

**Accessions** — [HGNC:6481](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6481) · Entrez [284217](https://www.ncbi.nlm.nih.gov/gene/284217) · UniProt [P25391](https://www.uniprot.org/uniprotkb/P25391) · Ensembl [ENSG00000101680](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101680)

## Data

Gene col 2165: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2165); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2165, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2165]; `tensor/DDL_lfc|DDL_z.npy` [2165]; `embed/gene_vectors.npy` [2165]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2165 or target_col == 2165). Every well: [[LAMA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
