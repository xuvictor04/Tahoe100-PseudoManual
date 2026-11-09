---
symbol: "IFI44L"
type: "gene"
col: 6099
ensembl_id: "ENSG00000137959"
name: "interferon induced protein 44 like"
location: "1p31.1"
module: 32
arm: "+"
pooled_cpm: 74.37
n_lines_expressing: 28
n_dd_up: 23
n_dd_down: 65
n_dd_up_clean: 21
n_dd_down_clean: 51
in_vector_space: true
direction_upstream: 49
direction_downstream: 68
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# IFI44L

*interferon induced protein 44 like* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 2.31× (z +7.1, q 5e-10, up in 24 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 65 drug-doses (14 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.105× (z -19.9, q 0e+00, down in 25 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFI44]] (+0.93, fdr 7e-06, ⚠ same locus), [[MX1]] (+0.92, fdr 7e-06), [[OAS2]] (+0.92, fdr 7e-06), [[XAF1]] (+0.90, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 49 arrows point to it, the strongest [[SAMD9L]] → it (grade B ⚠); 68 go from it, the strongest it → [[PARP12]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6099.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **2.31×** | +7.1 | 5e-10 | 24/25 (Hs 766T, J82, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.90×** | +5.5 | 1e-05 | 21/25 (Hs 766T, LoVo, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.47×** | +4.7 | 4e-04 | 18/26 (Hs 766T, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.67×** | +4.6 | 4e-04 | 20/26 (Hs 766T, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.54×** | +4.6 | 4e-04 | 21/26 (Hs 766T, HS-578T, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.57×** | +4.6 | 4e-04 | 21/26 (Hs 766T, HS-578T, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.67×** | +4.5 | 4e-04 | 22/25 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.41×** | +4.3 | 0.001 | 20/26 (Hs 766T, HS-578T, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.44×** | +4.2 | 0.002 | 20/26 (Hs 766T, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.56×** | +4.0 | 0.004 | 19/27 (Hs 766T, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +3.9 | 0.006 | 4/25 (J82, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.74×** | +3.5 | 0.020 | 14/26 (NCI-H1573, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.48×** | +3.5 | 0.022 | 17/26 (BT-474, NCI-H2030, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.50×** | +3.4 | 0.025 | 16/26 (Hs 766T, RPMI-7951, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.50×** | +3.4 | 0.025 | 17/26 (LoVo, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **2.04×** | +3.3 | 0.033 | 10/26 (Hs 766T, C32, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.035 | 14/26 (NCI-H1792, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 65 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 65 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6099.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.105×** | -19.9 | 0e+00 | 25/26 (RPMI-7951, SNU-423, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.124×** | -18.4 | 0e+00 | 26/26 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.242×** | -17.7 | 0e+00 | 24/26 (RPMI-7951, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.150×** | -16.8 | 0e+00 | 26/26 (RPMI-7951, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.181×** | -15.1 | 0e+00 | 24/26 (RPMI-7951, LoVo, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.217×** | -13.5 | 2e-39 | 24/26 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.353×** | -13.0 | 1e-36 | 25/26 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.360×** | -12.7 | 4e-35 | 23/26 (RPMI-7951, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.365×** | -12.6 | 2e-34 | 23/26 (NCI-H1573, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.276×** | -11.3 | 5e-28 | 25/26 (RPMI-7951, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.278×** | -11.3 | 8e-28 | 25/26 (BT-474, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.301×** | -10.6 | 2e-24 | 24/26 (NCI-H1573, LoVo, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.328×** | -9.8 | 4e-21 | 24/26 (SNU-423, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.321×** | -9.6 | 2e-20 | 23/25 (NCI-H1792, SNU-423, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.388×** | -7.9 | 1e-13 | 23/26 (LoVo, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.181×** | -7.9 | 1e-13 | 24/26 (A-172, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6099. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 117 | 0 | 29 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0240× (z -31.5) |
| [[LoVo (line)]] | wt | 103 | 0 | 26 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0152× (z -26.0) |
| [[A-172 (line)]] | wt | 133 | 0 | 25 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.00878× (z -29.3) |
| [[SNU-423 (line)]] | alt | 93.3 | 0 | 25 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.00765× (z -31.5) |
| [[NCI-H1792 (line)]] | alt | 289 | 0 | 24 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0790× (z -29.0) |
| [[RPMI-7951 (line)]] | alt | 383 | 0 | 24 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0124× (z -38.8) |
| [[BT-474 (line)]] | alt | 61.3 | 0 | 23 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0477× (z -20.8) |
| [[A498 (line)]] | wt | 333 | 0 | 21 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0327× (z -25.4) |
| [[HS-578T (line)]] | alt | 113 | 0 | 20 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0198× (z -24.9) |
| [[CHP-212 (line)]] | wt | 113 | 0 | 17 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0123× (z -18.4) |
| [[CFPAC-1 (line)]] | alt | 137 | 0 | 16 (6 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.0973× (z -24.1) |
| [[Hs 766T (line)]] | wt | 187 | 1 | 15 (1 ⚠) | [[Cobimetinib (drug)]] 5 µM 4.01× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.0450× (z -20.4) |
| [[SW 900 (line)]] | alt | 187 | 0 | 15 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -20.5) |
| [[NCI-H2347 (line)]] | alt | 204 | 0 | 14 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.176× (z -21.7) |
| [[SK-MEL-2 (line)]] | alt | 165 | 0 | 13 | — | [[Belinostat (drug)]] 5 µM 0.0176× (z -24.0) |
| [[C32 (line)]] | wt | 43.2 | 0 | 12 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0526× (z -15.3) |
| [[KATO III (line)]] | alt | 41.3 | 0 | 12 | — | [[Belinostat (drug)]] 5 µM 0.0378× (z -16.1) |
| [[Panc 03.27 (line)]] | alt | 167 | 0 | 11 | — | [[Panobinostat (drug)]] 0.5 µM 0.0795× (z -17.1) |
| [[LOX-IMVI (line)]] | wt | 39.2 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -12.9) |
| [[J82 (line)]] | alt | 69.0 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 9.63× (z +12.5) ⚠ toxic; transcription drop | [[Tofacitinib (drug)]] 5 µM 0.224× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 31.5 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 19.2 | 0 | 4 | — | [[Auranofin (drug)]] 5 µM 0.0650× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 19.1 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.0282× (z -14.8) |
| [[SW1417 (line)]] | alt | 20.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -9.6) |
| [[H4 (line)]] | wt | 22.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0849× (z -9.3) |
| [[A-427 (line)]] | wt | 3.75 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 16.7 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.00 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.07 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.36 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.12 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.3 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.29 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.41 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.17 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.21 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.12 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.89 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.08 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6099), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFI44]] | +0.93 | +0.87 / +0.96 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 999; ⚠ same locus (3.7 kb, same strand: neighbours can correlate without regulation) |
| [[MX1]] | +0.92 | +0.85 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 965 |
| [[OAS2]] | +0.92 | +0.86 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 935 |
| [[XAF1]] | +0.90 | +0.78 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 981 |
| [[CMPK2]] | +0.90 | +0.80 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 855 |
| [[EPSTI1]] | +0.89 | +0.79 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 921 |
| [[PARP9]] | +0.89 | +0.78 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 931 |
| [[OAS1]] | +0.88 | +0.78 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 955 |
| [[RSAD2]] | +0.88 | +0.79 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 999 |
| [[IFIT1]] | +0.87 | +0.77 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 967 |
| [[MX2]] | +0.87 | +0.78 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 837 |
| [[IFI35]] | +0.87 | +0.76 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 902 |
| [[IFIT3]] | +0.87 | +0.79 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 982 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 35, C 14. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD9L]] | B | SAMD9L activity raises IFI44L's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 5.17× lower at baseline in the lines without SAMD9L | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[OAS1]] | B | OAS1 activity raises IFI44L's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 5.03× lower at baseline in the lines without OAS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[IFITM1]] | B | IFITM1 activity raises IFI44L's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 4.01× lower at baseline in the lines without IFITM1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[CTSS]] | B | CTSS activity raises IFI44L's level | lines that do not express CTSS (15) vs lines expressing it (35) | 4.19× lower at baseline in the lines without CTSS | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[SRMS]] | B | SRMS activity raises IFI44L's level | lines that do not express SRMS (14) vs lines expressing it (36) | 3.73× lower at baseline in the lines without SRMS | 0.008 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[OASL]] | B | OASL activity raises IFI44L's level | lines that do not express OASL (10) vs lines expressing it (40) | 5.41× lower at baseline in the lines without OASL | 0.009 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[RSAD2]] | B | RSAD2 activity raises IFI44L's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 3.78× lower at baseline in the lines without RSAD2 | 0.011 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[IFI6]] | B | IFI6 activity raises IFI44L's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 5.12× lower at baseline in the lines without IFI6 | 0.016 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[XAF1]] | B | XAF1 activity raises IFI44L's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 4.49× lower at baseline in the lines without XAF1 | 0.021 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[SLC15A3]] | B | SLC15A3 activity raises IFI44L's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 4.31× lower at baseline in the lines without SLC15A3 | 0.023 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[IFI16]] | B | IFI16 activity raises IFI44L's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 4.54× lower at baseline in the lines without IFI16 | 0.025 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[CCDC194]] | B | CCDC194 activity raises IFI44L's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 3.36× lower at baseline in the lines without CCDC194 | 0.035 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |

### Downstream of this gene

*68 arrows, 68 of them with an alert ⚠; grade A 0, B 59, C 9. Shown: the 12 strongest; 56 more arrows (56 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARP12]] | B | IFI44L activity raises PARP12's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 2.08× lower at baseline in the lines without IFI44L | 0.003 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[HLA-F]] | B | IFI44L activity raises HLA-F's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 2.47× lower at baseline in the lines without IFI44L | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[GBP3]] | B | IFI44L activity raises GBP3's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 2.64× lower at baseline in the lines without IFI44L | 0.006 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[UNC93B1]] | B | IFI44L activity raises UNC93B1's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 1.38× lower at baseline in the lines without IFI44L | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[PML]] | B | IFI44L activity raises PML's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 1.80× lower at baseline in the lines without IFI44L | 0.009 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[IFITM3]] | B | IFI44L activity raises IFITM3's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 2.14× lower at baseline in the lines without IFI44L | 0.011 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[PSMB8]] | B | IFI44L activity raises PSMB8's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 2.20× lower at baseline in the lines without IFI44L | 0.011 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[HELZ2]] | B | IFI44L activity raises HELZ2's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 1.79× lower at baseline in the lines without IFI44L | 0.013 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[SLC15A3]] | B | IFI44L activity raises SLC15A3's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 2.48× lower at baseline in the lines without IFI44L | 0.013 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[OAS1]] | B | IFI44L activity raises OAS1's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 2.36× lower at baseline in the lines without IFI44L | 0.014 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[PLSCR1]] | B | IFI44L activity raises PLSCR1's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 2.22× lower at baseline in the lines without IFI44L | 0.014 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[IFITM1]] | B | IFI44L activity raises IFITM1's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 3.14× lower at baseline in the lines without IFI44L | 0.015 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.909). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.6, 53.5); signed map (64.9, 31.2). **Vector** length 139, 50.3% of its response variance represented; |z| ≥ 3 in 1,436 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interferon alpha/beta signaling* (reactome, mean cos +0.82 to 27); *Interferon gamma signaling* (reactome, mean cos +0.75 to 17); *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.81 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.4 | -3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.3 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.8 | +5.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +4.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.4 | +4.6 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -9.3 | -17.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -7.7 | -12.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -7.7 | -13.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -7.1 | -10.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.9 | -12.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -6.6 | -15.1 |

## What is on record

|  |  |
|---|---|
| Name | interferon induced protein 44 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:78,619,902-78,646,145 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GS3686, TLDC5B; previously C1orf29 |
| Gene groups (HGNC) | TLDc domain containing |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, KRAS_SIGNALING_DN, INTERFERON_GAMMA_RESPONSE |
| Reactome | 3 pathways, smallest: Modulation of host responses by IFN-stimulated genes; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53G44](https://www.uniprot.org/uniprotkb/Q53G44) (Interferon-induced protein 44-like):

> Type I interferon-stimulated gene (ISG) that plays a critical role in antiviral and antibacterial activity. During bacterial infection, promotes macrophage differentiation and facilitates inflammatory cytokine secretion. Plays a role in the control of respiratory syncytial virus/RSV infection, reducing the ability of the virus to replicate. Exhibits a low antiviral activity against hepatitis C virus. Also acts as a feedback regulator of IFN responses by negatively regulating IKBKB and IKBKE …

**Summary**, from NCBI Gene [10964](https://www.ncbi.nlm.nih.gov/gene/10964):

> Predicted to be involved in immune response. Predicted to act upstream of or within cellular response to virus. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17817](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17817) · Entrez [10964](https://www.ncbi.nlm.nih.gov/gene/10964) · UniProt [Q53G44](https://www.uniprot.org/uniprotkb/Q53G44) · Ensembl [ENSG00000137959](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137959)

## Data

Gene col 6099: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6099); `tables/drug_effects.parquet` (88 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6099, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6099]; `tensor/DDL_lfc|DDL_z.npy` [6099]; `embed/gene_vectors.npy` [6099]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6099 or target_col == 6099). Every well: [[IFI44L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFI44L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
