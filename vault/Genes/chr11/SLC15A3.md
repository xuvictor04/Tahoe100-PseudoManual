---
symbol: "SLC15A3"
type: "gene"
col: 3142
ensembl_id: "ENSG00000110446"
name: "solute carrier family 15 member 3"
location: "11q12.2"
module: 32
arm: "+"
pooled_cpm: 5.84
n_lines_expressing: 34
n_dd_up: 24
n_dd_down: 34
n_dd_up_clean: 21
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 37
direction_downstream: 73
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# SLC15A3

*solute carrier family 15 member 3* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.16× (z +6.3, q 2e-07, up in 19 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.225× (z -12.2, q 2e-31, down in 27 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFI35]] (+0.91, fdr 7e-06), [[TRIM22]] (+0.91, fdr 7e-06), [[PARP10]] (+0.91, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 37 arrows point to it, the strongest [[OAS1]] → it (grade B ⚠); 73 go from it, the strongest it → [[TMEM140]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3142.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.16×** | +6.3 | 2e-07 | 19/30 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.90×** | +5.3 | 4e-05 | 16/29 (NCI-H2347, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +5.1 | 7e-05 | 1/12 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.67×** | +5.0 | 7e-05 | 16/30 (RKO, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +5.0 | 8e-05 | 13/32 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.85×** | +4.8 | 1e-04 | 20/29 (AsPC-1, SNU-423, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.82×** | +4.7 | 2e-04 | 15/28 (AsPC-1, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **1.55×** | +4.2 | 0.002 | 16/31 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.58×** | +3.9 | 0.007 | 13/31 (AsPC-1, RKO, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.007 | 13/30 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.60×** | +3.8 | 0.007 | 14/29 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.38×** | +3.7 | 0.012 | 10/30 (CFPAC-1, Hs 766T, …) | all doses, flat | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.016 | 11/30 (KATO III, AsPC-1, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +3.5 | 0.017 | 5/19 (SW 900, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[venetoclax (drug)]] 0.05 µM |  | **1.57×** | +3.5 | 0.018 | 14/30 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.029 | 3/31 (LoVo, A-172, …) | inconsistent across doses | position effect removed |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.50×** | +3.3 | 0.030 | 11/29 (KATO III, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +3.3 | 0.030 | 9/29 (PANC-1, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3142.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.225×** | -12.2 | 2e-31 | 27/30 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.228×** | -12.1 | 5e-31 | 27/29 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.357×** | -11.9 | 2e-30 | 24/29 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.246×** | -11.4 | 4e-28 | 27/29 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.296×** | -9.9 | 3e-21 | 24/29 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.347×** | -8.6 | 5e-16 | 22/25 (RPMI-7951, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.505×** | -7.9 | 3e-13 | 26/30 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.513×** | -7.7 | 1e-12 | 20/28 (RKO, LoVo, …) | top dose only | composition shift |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.391×** | -7.7 | 1e-12 | 21/28 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.403×** | -7.4 | 7e-12 | 23/29 (RPMI-7951, LoVo, …) | top dose only | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.450×** | -6.5 | 4e-09 | 23/27 (A-172, LoVo, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.499×** | -5.4 | 4e-06 | 17/28 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.633×** | -5.3 | 6e-06 | 15/30 (RKO, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.301×** | -5.1 | 1e-05 | 20/29 (LoVo, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.557×** | -4.6 | 2e-04 | 17/22 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.595×** | -4.2 | 8e-04 | 18/29 (KATO III, SNU-423, …) | rises with dose | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.05 µM |  | **0.606×** | -4.1 | 0.001 | 9/29 (HOP62, LoVo, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3142. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 14.7 | 0 | 15 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.00526× (z -25.0) |
| [[A-172 (line)]] | wt | 18.1 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0363× (z -17.9) |
| [[RPMI-7951 (line)]] | alt | 21.6 | 0 | 7 (1 ⚠) | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.0757× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 12.1 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0371× (z -13.3) |
| [[NCI-H2347 (line)]] | alt | 20.3 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -13.9) |
| [[RKO (line)]] | wt | 15.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -12.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0716× (z -10.5) |
| [[KATO III (line)]] | alt | 6.55 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0440× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 7.92 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0348× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 8.94 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.152× (z -10.7) |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0906× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 5.64 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0376× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 5.00 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0331× (z -10.5) |
| [[SNU-423 (line)]] | alt | 15.8 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0308× (z -15.2) |
| [[BT-474 (line)]] | alt | 3.01 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.0599× (z -9.2) |
| [[J82 (line)]] | alt | 6.66 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.5× (z +8.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 3.98 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -9.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW1417 (line)]] | alt | 2.87 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0419× (z -8.5) |
| [[A-427 (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.926 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.867 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.752 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.808 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.816 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.675 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.564 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3142), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFI35]] | +0.91 | +0.81 / +0.92 | both halves | 7e-06 | **novel candidate** |
| [[TRIM22]] | +0.91 | +0.87 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[PARP10]] | +0.91 | +0.85 / +0.92 | both halves | 7e-06 | **novel candidate** |
| [[EPSTI1]] | +0.90 | +0.84 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[XAF1]] | +0.90 | +0.81 / +0.92 | both halves | 7e-06 |  |
| [[PARP9]] | +0.89 | +0.80 / +0.92 | both halves | 7e-06 |  |
| [[SAMD9L]] | +0.89 | +0.81 / +0.92 | both halves | 7e-06 |  |
| [[OAS2]] | +0.89 | +0.83 / +0.92 | both halves | 7e-06 |  |
| [[RSAD2]] | +0.88 | +0.81 / +0.91 | both halves | 7e-06 |  |
| [[CMPK2]] | +0.87 | +0.79 / +0.91 | both halves | 7e-06 |  |
| [[IFI44]] | +0.87 | +0.81 / +0.91 | both halves | 7e-06 |  |
| [[OAS1]] | +0.87 | +0.80 / +0.90 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 21, C 16. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS1]] | B | OAS1 activity raises SLC15A3's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.52× lower at baseline in the lines without OAS1 | 0.008 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[IFI44L]] | B | IFI44L activity raises SLC15A3's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 2.48× lower at baseline in the lines without IFI44L | 0.013 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[EPSTI1]] | B | EPSTI1 activity raises SLC15A3's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.55× lower at baseline in the lines without EPSTI1 | 0.014 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[MX1]] | B | MX1 activity raises SLC15A3's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.91× lower at baseline in the lines without MX1 | 0.016 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[GMPR]] | B | GMPR activity raises SLC15A3's level | lines that do not express GMPR (14) vs lines expressing it (36) | 2.08× lower at baseline in the lines without GMPR | 0.017 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PLAAT4]] | B | PLAAT4 activity raises SLC15A3's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.24× lower at baseline in the lines without PLAAT4 | 0.018 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[CASP10]] | B | CASP10 activity raises SLC15A3's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.13× lower at baseline in the lines without CASP10 | 0.029 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[SAMD9]] | B | SAMD9 activity raises SLC15A3's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 2.81× lower at baseline in the lines without SAMD9 | 0.036 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[BATF2]] | B | BATF2 activity raises SLC15A3's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.96× lower at baseline in the lines without BATF2 | 0.049 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[NRIR]] | B | NRIR activity raises SLC15A3's level | lines that do not express NRIR (14) vs lines expressing it (36) | 1.85× lower at baseline in the lines without NRIR | 0.052 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[IFI16]] | B | IFI16 activity raises SLC15A3's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.15× lower at baseline in the lines without IFI16 | 0.056 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[RSAD2]] | B | RSAD2 activity raises SLC15A3's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.00× lower at baseline in the lines without RSAD2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |

### Downstream of this gene

*73 arrows, 73 of them with an alert ⚠; grade A 0, B 58, C 15. Shown: the 12 strongest; 61 more arrows (61 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM140]] | B | SLC15A3 activity raises TMEM140's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 3.05× lower at baseline in the lines without SLC15A3 | 0.001 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[N4BP1]] | B | SLC15A3 activity raises N4BP1's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 1.26× lower at baseline in the lines without SLC15A3 | 0.003 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[PLSCR1]] | B | SLC15A3 activity raises PLSCR1's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 2.85× lower at baseline in the lines without SLC15A3 | 0.005 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[PML]] | B | SLC15A3 activity raises PML's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 2.06× lower at baseline in the lines without SLC15A3 | 0.005 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[CMPK2]] | B | SLC15A3 activity raises CMPK2's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 2.63× lower at baseline in the lines without SLC15A3 | 0.005 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[UBE2L6]] | B | SLC15A3 activity raises UBE2L6's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 3.22× lower at baseline in the lines without SLC15A3 | 0.006 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[PARP10]] | B | SLC15A3 activity raises PARP10's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 1.97× lower at baseline in the lines without SLC15A3 | 0.006 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[MX1]] | B | SLC15A3 activity raises MX1's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 3.57× lower at baseline in the lines without SLC15A3 | 0.006 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[PARP14]] | B | SLC15A3 activity raises PARP14's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 2.26× lower at baseline in the lines without SLC15A3 | 0.007 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[SAMHD1]] | B | SLC15A3 activity strengthens SAMHD1's drug response | lines that do not express SLC15A3 (16) vs lines expressing it (29) | the lines without SLC15A3 respond 0.43× as strongly (z diff +2.11); strongest at Selinexor 5 µM: 0.74x vs 0.49x (z diff +4.2) | 0.008 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4; target measured in part of the lines; artifact flags |
| [[LAP3]] | B | SLC15A3 activity raises LAP3's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 1.63× lower at baseline in the lines without SLC15A3 | 0.010 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[IRF9]] | B | SLC15A3 activity raises IRF9's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 1.85× lower at baseline in the lines without SLC15A3 | 0.010 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.927). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.7, 53.6); signed map (63.9, 31.5). **Vector** length 102, 30.5% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.77 to 56); *interferon gamma response* (hallmark, mean cos +0.78 to 60); *interferon* (control, mean cos +0.83 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.9 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.7 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.7 | +3.9 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -5.9 | -11.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -5.0 | -7.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -5.0 | -7.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.9 | -7.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.7 | -6.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 15 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:60,937,060-60,952,653 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PHT2, hPTR3 |
| Gene groups (HGNC) | Solute carrier family 15 |
| Reactome | 4 pathways, smallest: Proton/oligopeptide cotransporters; SLC-mediated transport of oligopeptides; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IY34](https://www.uniprot.org/uniprotkb/Q8IY34) (Solute carrier family 15 member 3):

> Proton-coupled amino-acid transporter that transports free histidine and certain di- and tripeptides, and is involved in innate immune response. Preferably binds to short peptides with a basic residue at the first position and a hydrophobic residue at the second position. Also able to transport carnosine. Involved in the detection of microbial pathogens by toll-like receptors (TLRs) and NOD-like receptors (NLRs), probably by mediating transport of bacterial peptidoglycans across the …

**Summary**, from NCBI Gene [51296](https://www.ncbi.nlm.nih.gov/gene/51296):

> Enables dipeptide transmembrane transporter activity. Involved in dipeptide import across plasma membrane. Located in lysosomal membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18068](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18068) · Entrez [51296](https://www.ncbi.nlm.nih.gov/gene/51296) · UniProt [Q8IY34](https://www.uniprot.org/uniprotkb/Q8IY34) · Ensembl [ENSG00000110446](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110446)

## Data

Gene col 3142: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3142); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3142, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3142]; `tensor/DDL_lfc|DDL_z.npy` [3142]; `embed/gene_vectors.npy` [3142]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3142 or target_col == 3142). Every well: [[SLC15A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC15A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
