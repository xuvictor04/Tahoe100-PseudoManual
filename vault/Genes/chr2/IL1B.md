---
symbol: "IL1B"
type: "gene"
col: 4630
ensembl_id: "ENSG00000125538"
name: "interleukin 1 beta"
location: "2q14.1"
module: 81
arm: "+"
pooled_cpm: 23.28
n_lines_expressing: 20
n_dd_up: 7
n_dd_down: 35
n_dd_up_clean: 5
n_dd_down_clean: 34
in_vector_space: true
direction_upstream: 43
direction_downstream: 46
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# IL1B

*interleukin 1 beta* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.30× (z +5.3, q 7e-05, up in 2 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Retinoic acid (drug)]] 5 µM: 1.55× (z +4.0, q 0.015, up in 13 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.307× (z -7.7, q 8e-12, down in 17 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL33]] (+0.73, fdr 7e-06), [[IL1A]] (+0.70, fdr 7e-06, ⚠ same locus), [[GPR68]] (+0.69, fdr 7e-06), [[GDNF]] (+0.67, fdr 1e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 43 arrows point to it, the strongest [[FAM107B]] → it (grade B ⚠); 46 go from it, the strongest it → [[MARCHF3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4630.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +5.3 | 7e-05 | 2/13 (LOX-IMVI, NCI-H460) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Retinoic acid (drug)]] 5 µM |  | **1.55×** | +4.0 | 0.015 | 13/18 (A-172, SW 900, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +3.4 | 0.073 | 7/18 (J82, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.67×** | +3.4 | 0.073 | 13/18 (SW 900, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.073 | 5/18 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.70×** | +3.4 | 0.073 | 10/18 (HOP62, J82, …) | rises with dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.01×** | +3.3 | 0.093 | 9/18 (Hs 766T, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4630.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.307×** | -7.7 | 8e-12 | 17/18 (Hs 766T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.437×** | -5.4 | 2e-05 | 14/18 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.452×** | -5.2 | 4e-05 | 17/18 (Hs 766T, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.453×** | -5.1 | 4e-05 | 18/18 (HOP62, NCI-H1792, …) | rises with dose | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.464×** | -5.0 | 7e-05 | 15/18 (NCI-H1792, HS-578T, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.459×** | -4.7 | 3e-04 | 9/18 (HOP62, Hs 766T, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.498×** | -4.5 | 5e-04 | 10/18 (A498, NCI-H1792, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.621×** | -4.3 | 0.001 | 10/18 (Hs 766T, A549, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.531×** | -4.1 | 0.003 | 16/18 (LoVo, A-172, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.542×** | -4.0 | 0.004 | 16/18 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.544×** | -4.0 | 0.004 | 14/18 (HS-578T, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.507×** | -3.9 | 0.005 | 12/18 (Hs 766T, HOP62, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.558×** | -3.8 | 0.007 | 13/18 (Hs 766T, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Anethole trithione (drug)]] 5 µM |  | **0.658×** | -3.8 | 0.007 | 9/18 (HOP62, SW 1088, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.861× | -3.5 | 0.021 | 2/18 (HOP62, NCI-H1792) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.591×** | -3.4 | 0.023 | 14/18 (HS-578T, LoVo, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.574×** | -3.3 | 0.029 | 11/17 (HS-578T, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4630. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 117 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0485× (z -17.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0487× (z -12.3) |
| [[HS-578T (line)]] | alt | 68.6 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0482× (z -11.8) |
| [[HOP62 (line)]] | alt | 247 | 0 | 6 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.312× (z -16.8) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0495× (z -12.5) |
| [[Hs 766T (line)]] | wt | 71.7 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0599× (z -13.5) |
| [[RPMI-7951 (line)]] | alt | 264 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0549× (z -11.2) |
| [[A-172 (line)]] | wt | 16.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0346× (z -12.4) |
| [[LoVo (line)]] | wt | 9.88 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0894× (z -10.0) |
| [[A549 (line)]] | wt | 13.1 | 0 | 2 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0815× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 63.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.36× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 14.4 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0652× (z -10.4) |
| [[A498 (line)]] | wt | 5.96 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.05 µM 0.0685× (z -10.0) |
| [[LS 180 (line)]] | wt | 7.45 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 9.85 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0540× (z -10.6) |
| [[A-427 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.52 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.39 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.59 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.77 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.91 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4630), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL33]] | +0.73 | +0.68 / +0.78 | both halves | 7e-06 | same gene group; pathway: HALLMARK_KRAS_SIGNALING_UP; STRING 890 |
| [[IL1A]] | +0.70 | +0.58 / +0.75 | both halves | 7e-06 | same gene group; pathway: HALLMARK_APOPTOSIS; STRING 999; ⚠ same locus (45.3 kb, same strand: neighbours can correlate without regulation) |
| [[GPR68]] | +0.69 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[GDNF]] | +0.67 | +0.57 / +0.69 | both halves | 1e-05 | STRING 582 |
| [[PTGS2]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP; STRING 974 |
| [[IL11]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 752 |
| [[LINC00973]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[PTHLH]] | +0.65 | +0.60 / +0.67 | both halves | 7e-06 | STRING 455 |
| [[HMGN2P46]] | +0.65 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[ANXA10]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[INHBA]] | +0.63 | +0.55 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[AADACP1]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[AFF3]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 6, C 37. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM107B]] | B | FAM107B activity raises IL1B's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 3.22× lower at baseline in the lines without FAM107B | 0.045 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[SOX9]] | B | SOX9 activity raises IL1B's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 3.20× lower at baseline in the lines without SOX9 | 0.048 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[CMKLR2]] | B | CMKLR2 activity raises IL1B's level | lines that do not express CMKLR2 (16) vs lines expressing it (34) | 2.65× lower at baseline in the lines without CMKLR2 | 0.067 | ⚠ within organs, on part of the lines; also absent: SATB1-AS1, ENSG00000231772, NYAP2; maybe low, not absent |
| [[CEMIP]] | B | CEMIP activity raises IL1B's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 2.44× lower at baseline in the lines without CEMIP | 0.085 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[LINC01204]] | B | LINC01204 activity raises IL1B's level | lines that do not express LINC01204 (22) vs lines expressing it (28) | 2.51× lower at baseline in the lines without LINC01204 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC00460, WNT5A, LNCOG; maybe low, not absent |
| [[CD44]] | B | CD44 activity raises IL1B's level | lines that do not express CD44 (15) vs lines expressing it (35) | 3.14× lower at baseline in the lines without CD44 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[CDH13]] | C | CDH13 activity raises IL1B's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 5.38× lower at baseline in the lines without CDH13 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[IL33]] | C | IL33 activity raises IL1B's level | lines that do not express IL33 (35) vs lines expressing it (15) | 4.35× lower at baseline in the lines without IL33 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01133, MUC2, LINC01411; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises IL1B's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 7.09× lower at baseline in the lines without LINC01411 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[SIRLNT]] | C | SIRLNT activity raises IL1B's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 5.01× lower at baseline in the lines without SIRLNT | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1; co-absent with the target |
| [[SHISAL1]] | C | SHISAL1 activity raises IL1B's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 3.65× lower at baseline in the lines without SHISAL1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11; co-absent with the target |
| [[COL15A1]] | C | COL15A1 activity raises IL1B's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 4.09× lower at baseline in the lines without COL15A1 | 0.005 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC; co-absent with the target |

### Downstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 18, C 28. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MARCHF3]] | B | IL1B activity raises MARCHF3's level | lines that do not express IL1B (30) vs lines expressing it (20) | 2.50× lower at baseline in the lines without IL1B | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |
| [[SOX9]] | B | IL1B activity raises SOX9's level | lines that do not express IL1B (30) vs lines expressing it (20) | 1.86× lower at baseline in the lines without IL1B | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |
| [[MARCHF3]] | B | IL1B activity weakens MARCHF3's drug response | lines that do not express IL1B (25) vs lines expressing it (19) | the lines without IL1B respond 0.90× as strongly (z diff +0.06); strongest at Panobinostat 5 µM: 3.02x vs 1.75x (z diff -2.5) | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA; target measured in part of the lines; both ways; artifact flags |
| [[CD44]] | B | IL1B activity raises CD44's level | lines that do not express IL1B (30) vs lines expressing it (20) | 4.55× lower at baseline in the lines without IL1B | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |
| [[GSDME]] | B | IL1B activity raises GSDME's level | lines that do not express IL1B (30) vs lines expressing it (20) | 3.12× lower at baseline in the lines without IL1B | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |
| [[ARL4C]] | B | IL1B activity raises ARL4C's level | lines that do not express IL1B (30) vs lines expressing it (20) | 2.64× lower at baseline in the lines without IL1B | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |
| [[TMEM132A]] | B | IL1B activity raises TMEM132A's level | lines that do not express IL1B (30) vs lines expressing it (20) | 2.01× lower at baseline in the lines without IL1B | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |
| [[PTPRE]] | B | IL1B activity raises PTPRE's level | lines that do not express IL1B (30) vs lines expressing it (20) | 2.02× lower at baseline in the lines without IL1B | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |
| [[DYRK3]] | B | IL1B activity raises DYRK3's level | lines that do not express IL1B (30) vs lines expressing it (20) | 2.48× lower at baseline in the lines without IL1B | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |
| [[SYNJ2]] | B | IL1B activity raises SYNJ2's level | lines that do not express IL1B (30) vs lines expressing it (20) | 1.80× lower at baseline in the lines without IL1B | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |
| [[STK10]] | B | IL1B activity raises STK10's level | lines that do not express IL1B (30) vs lines expressing it (20) | 1.94× lower at baseline in the lines without IL1B | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |
| [[ANTXR2]] | B | IL1B activity raises ANTXR2's level | lines that do not express IL1B (30) vs lines expressing it (20) | 2.39× lower at baseline in the lines without IL1B | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.7, 13.2); signed map (18.5, 50.0). **Vector** length 99.8, 38.1% of its response variance represented; |z| ≥ 3 in 799 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.1 | +2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.4 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +0.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +1.3 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -4.1 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.1 | -5.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.9 | -5.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.8 | -2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 1 beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1 — chr2:112,829,751-112,836,816 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IL1F2, IL-1B, IL1-BETA |
| Gene groups (HGNC) | Interleukins; Interleukin 1 family |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE, APOPTOSIS, KRAS_SIGNALING_UP, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 21 pathways, smallest: CASP5-mediated substrate cleavage; CASP4-mediated substrate cleavage; CLEC7A/inflammasome pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P01584](https://www.uniprot.org/uniprotkb/P01584) (Interleukin-1 beta):

> Potent pro-inflammatory cytokine. Initially discovered as the major endogenous pyrogen, induces prostaglandin synthesis, neutrophil influx and activation, T-cell activation and cytokine production, B-cell activation and antibody production, and fibroblast proliferation and collagen production. Promotes Th17 differentiation of T-cells. Synergizes with IL12/interleukin-12 to induce IFNG synthesis from T-helper 1 (Th1) cells. Plays a role in angiogenesis by inducing VEGF production synergistically …

**Summary**, from NCBI Gene [3553](https://www.ncbi.nlm.nih.gov/gene/3553):

> The protein encoded by this gene is a member of the interleukin 1 cytokine family. This cytokine is produced by activated macrophages as a proprotein, which is proteolytically processed to its active form by caspase 1 (CASP1/ICE). This cytokine is an important mediator of the inflammatory response, and is involved in a variety of cellular activities, including cell proliferation, differentiation, and apoptosis. The induction of cyclooxygenase-2 (PTGS2/COX2) by this cytokine in the central …

**Accessions** — [HGNC:5992](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5992) · Entrez [3553](https://www.ncbi.nlm.nih.gov/gene/3553) · UniProt [P01584](https://www.uniprot.org/uniprotkb/P01584) · Ensembl [ENSG00000125538](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125538)

## Data

Gene col 4630: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4630); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4630, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4630]; `tensor/DDL_lfc|DDL_z.npy` [4630]; `embed/gene_vectors.npy` [4630]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4630 or target_col == 4630). Every well: [[IL1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
