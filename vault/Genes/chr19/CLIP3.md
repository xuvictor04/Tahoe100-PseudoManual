---
symbol: "CLIP3"
type: "gene"
col: 2574
ensembl_id: "ENSG00000105270"
name: "CAP-Gly domain containing linker protein 3"
location: "19q13.12"
module: 71
arm: "+"
pooled_cpm: 5.42
n_lines_expressing: 46
n_dd_up: 19
n_dd_down: 14
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 8
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# CLIP3

*CAP-Gly domain containing linker protein 3* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.87× (z +7.6, q 2e-11, up in 4 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 0.5 µM: 1.52× (z +5.2, q 2e-05, up in 12 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.452× (z -10.0, q 8e-21, down in 26 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THAP8]] (+0.63, fdr 1e-05, ⚠ same locus), [[RNF10]] (+0.62, fdr 2e-05), [[TBC1D17]] (+0.61, fdr 1e-05), [[GDPD3]] (+0.58, fdr 4e-05); moves opposite to [[SNRPB]] (-0.65, fdr 1e-05), [[SRPK1]] (-0.63, fdr 7e-06), [[PKP4]] (-0.59, fdr 1e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PTPRN]] → it (grade B ⚠); 8 go from it, the strongest it → [[LRRC27]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2574.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +7.6 | 2e-11 | 4/9 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +5.4 | 2e-05 | 2/9 (HS-578T, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.3 | 2e-05 | 10/43 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.52×** | +5.2 | 2e-05 | 12/40 (LOX-IMVI, SK-MEL-2, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.34×** | +4.5 | 6e-04 | 10/42 (NCI-H2030, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +4.5 | 6e-04 | 12/41 (LoVo, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.43×** | +4.5 | 6e-04 | 7/39 (C32, NCI-H460, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.45×** | +4.4 | 8e-04 | 6/41 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.002 | 9/38 (NCI-H460, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.004 | 6/43 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.25×** | +3.9 | 0.005 | 6/43 (LOX-IMVI, NCI-H460, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.008 | 10/39 (NCI-H2030, SK-MEL-2, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.010 | 6/42 (NCI-H2030, C-33 A, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.34×** | +3.6 | 0.011 | 6/23 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.48×** | +3.5 | 0.015 | 6/36 (NCI-H2030, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.015 | 4/42 (C-33 A, SW480, …) | two highest doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.015 | 5/35 (A549, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2574.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.452×** | -10.0 | 8e-21 | 26/40 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.512×** | -8.5 | 8e-15 | 26/43 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.541×** | -7.7 | 2e-12 | 22/36 (SHP-77, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.591×** | -6.6 | 5e-09 | 19/40 (SW 900, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.629×** | -5.9 | 6e-07 | 12/41 (H4, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.648×** | -5.5 | 4e-06 | 17/43 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.696×** | -4.4 | 9e-04 | 8/40 (HT-29, SW1417, …) | two highest doses | composition shift; position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.715×** | -4.1 | 0.003 | 6/42 (LOX-IMVI, SNU-1, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.732×** | -3.9 | 0.005 | 14/42 (Hs 766T, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.735×** | -3.9 | 0.006 | 15/40 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.739×** | -3.8 | 0.007 | 15/39 (NCI-H460, HEC-1-A, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.574×** | -3.7 | 0.012 | 8/33 (CHP-212, SHP-77, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.767×** | -3.3 | 0.036 | 7/41 (NCI-H2030, HEC-1-A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.785×** | -3.1 | 0.092 | 9/41 (HT-29, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2574. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 3.79 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0570× (z -11.2) |
| [[SHP-77 (line)]] | alt | 8.92 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0947× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 6.31 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0842× (z -8.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2574), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP8]] | +0.63 | +0.69 / +0.49 | both halves | 1e-05 | STRING 407; ⚠ same locus (1.6 kb, same strand: neighbours can correlate without regulation) |
| [[RNF10]] | +0.62 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[TBC1D17]] | +0.61 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[GDPD3]] | +0.58 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[KLC4]] | +0.57 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[TOM1]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[UBXN6]] | +0.56 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[NOP53]] | +0.56 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[ALG12]] | +0.56 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[OSCP1]] | +0.56 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ZNF292]] | +0.55 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[CCDC115]] | +0.55 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[PRKAB2]] | +0.55 | +0.41 / +0.58 | both halves | 4e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPB]] | -0.65 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[SRPK1]] | -0.63 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[PKP4]] | -0.59 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[DDIAS]] | -0.58 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[C9orf40]] | -0.56 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[VRK1]] | -0.56 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[LYAR]] | -0.56 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[XRCC2]] | -0.55 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[BRI3BP]] | -0.55 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[NUDCD1]] | -0.55 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[CTPS1]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[SUV39H2]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRN]] | B | PTPRN activity raises CLIP3's level | lines that do not express PTPRN (31) vs lines expressing it (19) | 2.29× lower at baseline in the lines without PTPRN | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers CLIP3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[ARMCX1]] | B | ARMCX1 activity raises CLIP3's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 1.80× lower at baseline in the lines without ARMCX1 | 0.072 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1 |
| [[TCEA3]] | B | TCEA3 activity raises CLIP3's level | lines that do not express TCEA3 (14) vs lines expressing it (36) | 1.49× lower at baseline in the lines without TCEA3 | 0.082 | ⚠ within organs, on part of the lines; also absent: ZNF43, ENSG00000267383, ZNF681; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC27]] | C | CLIP3 activity raises LRRC27's level | lines that do not express CLIP3 (4) vs lines expressing it (46) | 2.11× lower at baseline in the lines without CLIP3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RAPGEF4, MEGF11, TMEM170B; maybe low, not absent; its own permutation p |
| [[THAP8]] | C | CLIP3 activity raises THAP8's level | lines that do not express CLIP3 (4) vs lines expressing it (46) | 2.09× lower at baseline in the lines without CLIP3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RAPGEF4, MEGF11, TMEM170B; maybe low, not absent; its own permutation p |
| [[NPHP1]] | C | CLIP3 activity raises NPHP1's level | lines that do not express CLIP3 (4) vs lines expressing it (46) | 2.08× lower at baseline in the lines without CLIP3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RAPGEF4, MEGF11, TMEM170B; maybe low, not absent; its own permutation p |
| [[TBC1D17]] | C | CLIP3 activity raises TBC1D17's level | lines that do not express CLIP3 (4) vs lines expressing it (46) | 1.69× lower at baseline in the lines without CLIP3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RAPGEF4, MEGF11, TMEM170B; maybe low, not absent; its own permutation p |
| [[HS1BP3]] | C | CLIP3 activity raises HS1BP3's level | lines that do not express CLIP3 (4) vs lines expressing it (46) | 1.44× lower at baseline in the lines without CLIP3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RAPGEF4, MEGF11, TMEM170B; maybe low, not absent; its own permutation p |
| [[ODAD4]] | C | CLIP3 activity raises ODAD4's level | lines that do not express CLIP3 (4) vs lines expressing it (46) | 1.60× lower at baseline in the lines without CLIP3 | 0.077 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RAPGEF4, MEGF11, TMEM170B; maybe low, not absent |
| [[WBP1]] | C | CLIP3 activity raises WBP1's level | lines that do not express CLIP3 (4) vs lines expressing it (46) | 1.25× lower at baseline in the lines without CLIP3 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RAPGEF4, MEGF11, TMEM170B; maybe low, not absent |
| [[AMZ2P1-1]] | C | CLIP3 activity raises AMZ2P1-1's level | lines that do not express CLIP3 (4) vs lines expressing it (46) | 1.64× lower at baseline in the lines without CLIP3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RAPGEF4, MEGF11, TMEM170B; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction -0.415). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.9, -51.2); signed map (-17.2, 5.8). **Vector** length 46.0, 5.52% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +7.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.5 | +4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +3.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -10.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -3.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.9 | -3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.3 | -1.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.3 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | +0.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.1 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | CAP-Gly domain containing linker protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:36,014,660-36,033,343 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CLIPR-59, RSNL1 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Reactome | 3 pathways, smallest: Regulation of TNFR1 signaling; TNF signaling; Death Receptor Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DZ5](https://www.uniprot.org/uniprotkb/Q96DZ5) (CAP-Gly domain-containing linker protein 3):

> Functions as a cytoplasmic linker protein. Involved in TGN-endosome dynamics. May modulate the cellular compartmentalization of AKT kinase family and promote its cell membrane localization, thereby playing a role in glucose transport in adipocytes.

**Summary**, from NCBI Gene [25999](https://www.ncbi.nlm.nih.gov/gene/25999):

> This gene encodes a member of the cytoplasmic linker protein 170 family. Members of this protein family contain a cytoskeleton-associated protein glycine-rich domain and mediate the interaction of microtubules with cellular organelles. The encoded protein plays a role in T cell apoptosis by facilitating the association of tubulin and the lipid raft ganglioside GD3. The encoded protein also functions as a scaffold protein mediating membrane localization of phosphorylated protein kinase B. …

**Accessions** — [HGNC:24314](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24314) · Entrez [25999](https://www.ncbi.nlm.nih.gov/gene/25999) · UniProt [Q96DZ5](https://www.uniprot.org/uniprotkb/Q96DZ5) · Ensembl [ENSG00000105270](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105270)

## Data

Gene col 2574: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2574); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2574, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2574]; `tensor/DDL_lfc|DDL_z.npy` [2574]; `embed/gene_vectors.npy` [2574]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2574 or target_col == 2574). Every well: [[CLIP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLIP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
