---
symbol: "NRP2"
type: "gene"
col: 3975
ensembl_id: "ENSG00000118257"
name: "neuropilin 2"
location: "2q33.3"
module: 66
arm: "+"
pooled_cpm: 78.0
n_lines_expressing: 26
n_dd_up: 11
n_dd_down: 26
n_dd_up_clean: 7
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 17
direction_downstream: 12
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# NRP2

*neuropilin 2* — 2q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.60× (z +10.2, q 9e-22, up in 15 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.502× (z -10.6, q 1e-23, down in 21 of 24 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VCAM1]] (+0.58, fdr 2e-05), [[CDH2]] (+0.50, fdr 6e-05), [[MSC]] (+0.49, fdr 3e-05); moves opposite to [[ZNF235]] (-0.42, fdr 1e-04), [[TUT4]] (-0.42, fdr 4e-05), [[BTBD2]] (-0.42, fdr 1e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[AMIGO2]] → it (grade B ⚠); 12 go from it, the strongest it → [[SMAD3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3975.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +10.2 | 9e-22 | 15/24 (CFPAC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +9.3 | 6e-18 | 12/22 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +7.9 | 4e-13 | 13/24 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.9 | 5e-07 | 10/25 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.46×** | +5.8 | 9e-07 | 19/24 (RPMI-7951, AsPC-1, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 5 µM |  | **1.28×** | +5.4 | 5e-06 | 16/25 (HS-578T, LOX-IMVI, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +4.6 | 3e-04 | 7/22 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.33×** | +4.3 | 1e-03 | 14/24 (AsPC-1, HS-578T, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.002 | 12/24 (SK-MEL-2, HS-578T, …) | top dose only |  |
| [[Tazarotene (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.020 | 4/25 (A549, HS-578T, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~7% of this change | **1.24×** | +3.1 | 0.087 | 6/23 (HOP62, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3975.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.502×** | -10.6 | 1e-23 | 21/24 (Hs 766T, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.528×** | -9.5 | 8e-19 | 16/24 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.593×** | -8.0 | 2e-13 | 14/24 (LOX-IMVI, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.623×** | -7.3 | 3e-11 | 19/23 (Hs 766T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.623×** | -7.3 | 3e-11 | 17/24 (LOX-IMVI, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.660×** | -6.4 | 1e-08 | 16/24 (LOX-IMVI, A498, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.699×** | -5.3 | 8e-06 | 16/23 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.785×** | -5.3 | 9e-06 | 13/24 (Hs 766T, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.711×** | -5.3 | 9e-06 | 14/24 (H4, A498, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.723×** | -5.0 | 3e-05 | 10/24 (Hs 766T, SK-MEL-2, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.800×** | -4.9 | 6e-05 | 11/24 (NCI-H1792, H4, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.742×** | -4.6 | 2e-04 | 15/24 (LOX-IMVI, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.826×** | -4.2 | 0.001 | 11/24 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.767×** | -4.1 | 0.002 | 12/24 (LOX-IMVI, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.768×** | -4.1 | 0.002 | 13/24 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.779×** | -3.9 | 0.004 | 12/24 (C32, A498, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.781×** | -3.8 | 0.004 | 10/24 (Hs 766T, A549, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3975. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 343 | 0 | 12 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -14.9) |
| [[LOX-IMVI (line)]] | wt | 346 | 0 | 11 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.103× (z -19.7) |
| [[A498 (line)]] | wt | 749 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -16.9) |
| [[Hs 766T (line)]] | wt | 111 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -24.2) |
| [[AsPC-1 (line)]] | alt | 62.5 | 0 | 6 | — | [[Harringtonine (drug)]] 5 µM 0.0912× (z -17.3) |
| [[SK-MEL-2 (line)]] | alt | 264 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -18.6) |
| [[CFPAC-1 (line)]] | alt | 34.6 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.38× (z +15.3) | — |
| [[HOP62 (line)]] | alt | 24.5 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 110 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.215× (z -12.4) |
| [[hTERT-HPNE (line)]] | wt | 103 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.09× (z +17.3) | — |
| [[RPMI-7951 (line)]] | alt | 208 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 33.8 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.260× (z -8.8) |
| [[KATO III (line)]] | alt | 32.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -14.0) |
| [[NCI-H1792 (line)]] | alt | 84.4 | 2 (2 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.38× (z +9.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW480 (line)]] | alt | 39.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.364× (z -8.8) |
| [[A549 (line)]] | wt | 85.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -8.9) |
| [[COLO 205 (line)]] | alt | 25.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -12.6) |
| [[H4 (line)]] | wt | 34.7 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.128× (z -10.5) |
| [[SNU-423 (line)]] | alt | 79.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 25.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +9.3) | — |
| [[A-172 (line)]] | wt | 15.7 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.75 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.18 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.86 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.76 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.44 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 15.2 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.58 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.51 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.27 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.52 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 8.63 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.61 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 17.7 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.64 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.94 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.25 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3975), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VCAM1]] | +0.58 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[CDH2]] | +0.50 | +0.50 / +0.39 | both halves | 6e-05 |  |
| [[MSC]] | +0.49 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[NFE2L3]] | +0.49 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[DPYSL3]] | +0.48 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[CDH6]] | +0.48 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[TPM1]] | +0.47 | +0.50 / +0.36 | both halves | 1e-04 |  |
| [[SULF1]] | +0.47 | +0.41 / +0.39 | both halves | 5e-05 |  |
| [[SLC4A4]] | +0.46 | +0.36 / +0.42 | both halves | 9e-05 |  |
| [[MOXD1]] | +0.45 | +0.49 / +0.30 | both halves | 2e-04 |  |
| [[ADAMTS3]] | +0.45 | +0.39 / +0.37 | both halves | 8e-05 |  |
| [[EDIL3-DT]] | +0.44 | +0.34 / +0.49 | both halves | 1e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF235]] | -0.42 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[TUT4]] | -0.42 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[BTBD2]] | -0.42 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[TAF8]] | -0.42 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[MKNK2]] | -0.40 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[EXO5-DT]] | -0.40 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[CRTC1]] | -0.40 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[RGL3]] | -0.39 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[DTWD1]] | -0.39 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[MAP2K7]] | -0.39 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[NISCH]] | -0.38 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[DDX19B]] | -0.38 | -0.22 / -0.42 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 5, C 12. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AMIGO2]] | B | AMIGO2 activity raises NRP2's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 1.85× lower at baseline in the lines without AMIGO2 | 0.050 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[CDH2]] | B | CDH2 activity raises NRP2's level | lines that do not express CDH2 (22) vs lines expressing it (28) | 2.89× lower at baseline in the lines without CDH2 | 0.086 | ⚠ within organs, on part of the lines; also absent: ARMCX1, DKK3, RFTN1 |
| [[RGL3]] | B | RGL3 activity lowers NRP2's level | lines that do not express RGL3 (12) vs lines expressing it (38) | 2.46× higher at baseline in the lines without RGL3 | 0.094 | ⚠ within organs, on part of the lines; also absent: SLC16A14 |
| [[RARA]], [[RARB]], [[RARG]] | B | RARA, RARB, RARG activity raises NRP2's level | compounds that target RARA, RARB, RARG: 2 of 2 raise it (Retinoic acid, Tazarotene) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[RARB]] | B | RARB activity raises NRP2's level | lines that do not express RARB (28) vs lines expressing it (22) | 3.01× lower at baseline in the lines without RARB | 0.096 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA |
| [[DOCK10]] | C | DOCK10 activity raises NRP2's level | lines that do not express DOCK10 (24) vs lines expressing it (26) | 3.56× lower at baseline in the lines without DOCK10 | 0.012 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, TRPA1; co-absent with the target |
| [[FYB1]] | C | FYB1 activity raises NRP2's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 3.30× lower at baseline in the lines without FYB1 | 0.018 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450; co-absent with the target |
| [[C12orf75-AS1]] | C | C12orf75-AS1 activity raises NRP2's level | lines that do not express C12orf75-AS1 (22) vs lines expressing it (28) | 3.56× lower at baseline in the lines without C12orf75-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1; co-absent with the target |
| [[MMP2]] | C | MMP2 activity raises NRP2's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 3.89× lower at baseline in the lines without MMP2 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L; co-absent with the target |
| [[MSC]] | C | MSC activity raises NRP2's level | lines that do not express MSC (34) vs lines expressing it (16) | 5.13× lower at baseline in the lines without MSC | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |
| [[SLC4A4]] | C | SLC4A4 activity raises NRP2's level | lines that do not express SLC4A4 (29) vs lines expressing it (21) | 1.92× lower at baseline in the lines without SLC4A4 | 0.037 | ⚠ within organs, on part of the lines; also absent: PTGS2, LINC00632, AGTR1; co-absent with the target |
| [[ABI3BP]] | C | ABI3BP activity raises NRP2's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 2.02× lower at baseline in the lines without ABI3BP | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 5, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMAD3]] | B | NRP2 activity raises SMAD3's level | lines that do not express NRP2 (24) vs lines expressing it (26) | 2.04× lower at baseline in the lines without NRP2 | 0.024 | ⚠ within organs, on part of the lines; also absent: NLRP1, RFX8, TNFAIP6 |
| [[ZNF235]] | B | NRP2 activity strengthens ZNF235's drug response | lines that do not express NRP2 (23) vs lines expressing it (24) | the lines without NRP2 respond 0.73× as strongly (z diff +1.16); strongest at Homoharringtonine 5 µM: 0.76x vs 0.43x (z diff +4.8) | 0.042 | ⚠ within organs, on part of the lines; also absent: NLRP1, RFX8, TNFAIP6; target measured in part of the lines; artifact flags |
| [[AMIGO2]] | B | NRP2 activity raises AMIGO2's level | lines that do not express NRP2 (24) vs lines expressing it (26) | 1.76× lower at baseline in the lines without NRP2 | 0.048 | ⚠ within organs, on part of the lines; also absent: NLRP1, RFX8, TNFAIP6 |
| [[TAGLN2]] | B | NRP2 activity raises TAGLN2's level | lines that do not express NRP2 (24) vs lines expressing it (26) | 2.01× lower at baseline in the lines without NRP2 | 0.063 | ⚠ within organs, on part of the lines; also absent: NLRP1, RFX8, TNFAIP6 |
| [[RGL3]] | B | NRP2 activity lowers RGL3's level | lines that do not express NRP2 (24) vs lines expressing it (26) | 2.29× higher at baseline in the lines without NRP2 | 0.080 | ⚠ within organs, on part of the lines; also absent: NLRP1, RFX8, TNFAIP6 |
| [[TNC]] | C | NRP2 activity raises TNC's level | lines that do not express NRP2 (24) vs lines expressing it (26) | 5.26× lower at baseline in the lines without NRP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: NLRP1, RFX8, TNFAIP6; co-absent with the target |
| [[CDK15]] | C | NRP2 activity raises CDK15's level | lines that do not express NRP2 (24) vs lines expressing it (26) | 1.97× lower at baseline in the lines without NRP2 | 0.046 | ⚠ within organs, on part of the lines; also absent: NLRP1, RFX8, TNFAIP6; co-absent with the target |
| [[DPYSL3]] | C | NRP2 activity raises DPYSL3's level | lines that do not express NRP2 (24) vs lines expressing it (26) | 3.24× lower at baseline in the lines without NRP2 | 0.068 | ⚠ within organs, on part of the lines; also absent: NLRP1, RFX8, TNFAIP6; co-absent with the target |
| [[MSC]] | C | NRP2 activity raises MSC's level | lines that do not express NRP2 (24) vs lines expressing it (26) | 2.18× lower at baseline in the lines without NRP2 | 0.069 | ⚠ within organs, on part of the lines; also absent: NLRP1, RFX8, TNFAIP6; co-absent with the target |
| [[FYB1]] | C | NRP2 activity raises FYB1's level | lines that do not express NRP2 (24) vs lines expressing it (26) | 1.97× lower at baseline in the lines without NRP2 | 0.069 | ⚠ within organs, on part of the lines; also absent: NLRP1, RFX8, TNFAIP6; co-absent with the target |
| [[MMP2]] | C | NRP2 activity raises MMP2's level | lines that do not express NRP2 (24) vs lines expressing it (26) | 2.91× lower at baseline in the lines without NRP2 | 0.071 | ⚠ within organs, on part of the lines; also absent: NLRP1, RFX8, TNFAIP6; co-absent with the target |
| [[TIMP3]] | C | NRP2 activity raises TIMP3's level | lines that do not express NRP2 (24) vs lines expressing it (26) | 3.68× lower at baseline in the lines without NRP2 | 0.075 | ⚠ within organs, on part of the lines; also absent: NLRP1, RFX8, TNFAIP6; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.500). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.8, 19.2); signed map (46.3, 23.0). **Vector** length 95.7, 27.7% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +0.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.8 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +1.1 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.0 | -2.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.0 | -4.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.8 | -5.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.6 | -5.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -8.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | neuropilin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.3 — chr2:205,681,990-205,798,133 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VEGF165R2 |
| Gene groups (HGNC) | Neuropilin family |
| Hallmark sets | HEDGEHOG_SIGNALING |
| Reactome | 7 pathways, smallest: Neuropilin interactions with VEGF and VEGFR; NrCAM interactions; Signaling by VEGF |
| Matched by | ensembl_id |

**Function**, from UniProt [O60462](https://www.uniprot.org/uniprotkb/O60462) (Neuropilin-2):

> High affinity receptor for semaphorins 3C, 3F, VEGF-165 and VEGF-145 isoforms of VEGF, and the PLGF-2 isoform of PGF.; (Microbial infection) Acts as a receptor for human cytomegalovirus pentamer-dependent entry in epithelial and endothelial cells.

**Summary**, from NCBI Gene [8828](https://www.ncbi.nlm.nih.gov/gene/8828):

> This gene encodes a member of the neuropilin family of receptor proteins. The encoded transmembrane protein binds to SEMA3C protein {sema domain, immunoglobulin domain (Ig), short basic domain, secreted, (semaphorin) 3C} and SEMA3F protein {sema domain, immunoglobulin domain (Ig), short basic domain, secreted, (semaphorin) 3F}, and interacts with vascular endothelial growth factor (VEGF). This protein may play a role in cardiovascular development, axon guidance, and tumorigenesis. This protein …

**Accessions** — [HGNC:8005](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8005) · Entrez [8828](https://www.ncbi.nlm.nih.gov/gene/8828) · UniProt [O60462](https://www.uniprot.org/uniprotkb/O60462) · Ensembl [ENSG00000118257](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118257)

## Data

Gene col 3975: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3975); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3975, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3975]; `tensor/DDL_lfc|DDL_z.npy` [3975]; `embed/gene_vectors.npy` [3975]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3975 or target_col == 3975). Every well: [[NRP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
