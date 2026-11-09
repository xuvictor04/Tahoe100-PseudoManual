---
symbol: "PRUNE2"
type: "gene"
col: 2803
ensembl_id: "ENSG00000106772"
name: "prune homolog 2 with BCH domain"
location: "9q21.2"
module: 9
arm: "+"
pooled_cpm: 18.19
n_lines_expressing: 20
n_dd_up: 46
n_dd_down: 5
n_dd_up_clean: 39
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 11
direction_downstream: 16
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PRUNE2

*prune homolog 2 with BCH domain* — 9q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 46 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.02× (z +19.7, q 0e+00, up in 16 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.623× (z -6.0, q 1e-06, down in 9 of 17 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLXDC2]] (+0.60, fdr 1e-05), [[GPNMB]] (+0.58, fdr 1e-05), [[PPARGC1A]] (+0.57, fdr 1e-05); moves opposite to [[SPRED3]] (-0.46, fdr 4e-05), [[SPRY4-AS1]] (-0.43, fdr 4e-05), [[SHC4]] (-0.43, fdr 6e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[SORBS2]] → it (grade B ⚠); 16 go from it, the strongest it → [[LINC02208]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 46 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2803.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.02×** | +19.7 | 0e+00 | 16/18 (LoVo, SW1417, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +15.2 | 0e+00 | 4/18 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +14.0 | 5e-42 | 5/17 (J82, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.79×** | +12.9 | 5e-36 | 14/18 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.50×** | +11.6 | 7e-29 | 11/18 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.45×** | +11.3 | 2e-27 | 12/18 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +10.5 | 6e-24 | 5/12 (J82, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.41×** | +10.3 | 7e-23 | 4/15 (J82, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +9.3 | 1e-18 | 7/18 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.99×** | +8.6 | 3e-16 | 13/18 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.89×** | +8.0 | 7e-14 | 14/18 (A-172, HS-578T, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.66×** | +7.5 | 4e-12 | 11/18 (SK-MEL-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.76×** | +7.1 | 5e-11 | 10/18 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.70×** | +6.4 | 6e-09 | 13/17 (NCI-H460, HS-578T, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.55×** | +6.1 | 5e-08 | 11/18 (SW480, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.48×** | +6.0 | 5e-08 | 13/18 (SW480, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.57×** | +5.6 | 7e-07 | 13/18 (SW480, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +5.6 | 8e-07 | 7/18 (A-172, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2803.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.623×** | -6.0 | 1e-06 | 9/17 (SNU-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.632×** | -5.8 | 2e-06 | 12/18 (SNU-1, hTERT-HPNE, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.734×** | -3.9 | 0.017 | 5/18 (SNU-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.746×** | -3.7 | 0.027 | 12/18 (SNU-1, SW480, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.768×** | -3.3 | 0.092 | 3/18 (CHP-212, J82, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.781× | -3.1 | 0.16 | 6/18 (SNU-1, SW480, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2803. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 271 | 0 | 15 (8 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0398× (z -23.7) |
| [[NCI-H460 (line)]] | wt | 4.89 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 13.0× (z +10.1) | — |
| [[A-172 (line)]] | wt | 12.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.22× (z +13.1) | — |
| [[HS-578T (line)]] | alt | 29.9 | 2 | 0 | [[Ponatinib (drug)]] 5 µM 8.47× (z +9.9) | — |
| [[LoVo (line)]] | wt | 9.86 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 8.65× (z +12.1) | [[Digitoxin (drug)]] 5 µM 0.0463× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SHP-77 (line)]] | alt | 190 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.357× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -9.4) |
| [[SW480 (line)]] | alt | 17.0 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.06× (z +9.6) | [[Digitoxin (drug)]] 0.5 µM 0.178× (z -10.6) ⚠ cell-cycle shift, explains ~20% of this change |
| [[A498 (line)]] | wt | 60.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.287× (z -8.5) ⚠ toxic |
| [[J82 (line)]] | alt | 138 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -10.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 10.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.22× (z +10.8) | — |
| [[A-427 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.28 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.84 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.08 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.30 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.27 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2803), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLXDC2]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[GPNMB]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[PPARGC1A]] | +0.57 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[FAM133A]] | +0.52 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[CNTNAP2]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[NR1H4]] | +0.50 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[CD24]] | +0.49 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[AMOT]] | +0.49 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[STK33]] | +0.49 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[MPP7]] | +0.48 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[LINC00298]] | +0.48 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[MOXD1]] | +0.48 | +0.45 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRED3]] | -0.46 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[SPRY4-AS1]] | -0.43 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[SHC4]] | -0.43 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[NHSL1]] | -0.42 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[OSMR-DT]] | -0.42 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[UBASH3B]] | -0.41 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 3, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SORBS2]] | B | SORBS2 activity raises PRUNE2's level | lines that do not express SORBS2 (17) vs lines expressing it (33) | 1.53× lower at baseline in the lines without SORBS2 | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC00299, ENSG00000228033, HR |
| [[P2RX7]] | B | P2RX7 activity raises PRUNE2's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 2.84× lower at baseline in the lines without P2RX7 | 0.059 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |
| [[NRXN1]] | B | NRXN1 activity raises PRUNE2's level | lines that do not express NRXN1 (19) vs lines expressing it (31) | 1.79× lower at baseline in the lines without NRXN1 | 0.085 | ⚠ within organs, on part of the lines; also absent: CHRM3, MIR2052HG, ENSG00000265994; maybe low, not absent |
| [[PDZRN3]] | C | PDZRN3 activity raises PRUNE2's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 3.37× lower at baseline in the lines without PDZRN3 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098; co-absent with the target |
| [[STK32A]] | C | STK32A activity raises PRUNE2's level | lines that do not express STK32A (23) vs lines expressing it (27) | 2.72× lower at baseline in the lines without STK32A | 0.011 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1; co-absent with the target |
| [[GPNMB]] | C | GPNMB activity raises PRUNE2's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 3.16× lower at baseline in the lines without GPNMB | 0.050 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6; co-absent with the target |
| [[SHC4]] | C | SHC4 activity raises PRUNE2's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 1.83× lower at baseline in the lines without SHC4 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent; co-absent with the target |
| [[DCT]] | C | DCT activity raises PRUNE2's level | lines that do not express DCT (42) vs lines expressing it (8) | 2.72× lower at baseline in the lines without DCT | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1; co-absent with the target |
| [[KCND2]] | C | KCND2 activity raises PRUNE2's level | lines that do not express KCND2 (32) vs lines expressing it (18) | 1.80× lower at baseline in the lines without KCND2 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, SYT4, DCT; maybe low, not absent; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises PRUNE2's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 2.40× lower at baseline in the lines without KCNH7 | 0.082 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises PRUNE2's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.75× lower at baseline in the lines without RUNX1T1 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 9, C 7. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02208]] | B | PRUNE2 activity raises LINC02208's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 1.33× lower at baseline in the lines without PRUNE2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY |
| [[GCNT1]] | B | PRUNE2 activity raises GCNT1's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 2.56× lower at baseline in the lines without PRUNE2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY |
| [[SORBS2]] | B | PRUNE2 activity raises SORBS2's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 2.03× lower at baseline in the lines without PRUNE2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY |
| [[DGKB]] | B | PRUNE2 activity raises DGKB's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 1.77× lower at baseline in the lines without PRUNE2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY |
| [[RALYL]] | B | PRUNE2 activity raises RALYL's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 1.89× lower at baseline in the lines without PRUNE2 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY |
| [[PPP2R2B]] | B | PRUNE2 activity raises PPP2R2B's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 2.36× lower at baseline in the lines without PRUNE2 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY |
| [[FAM13C]] | B | PRUNE2 activity raises FAM13C's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 1.89× lower at baseline in the lines without PRUNE2 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY |
| [[P2RX7]] | B | PRUNE2 activity raises P2RX7's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 1.93× lower at baseline in the lines without PRUNE2 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY |
| [[MIR325HG]] | B | PRUNE2 activity raises MIR325HG's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 1.38× lower at baseline in the lines without PRUNE2 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY |
| [[PDZRN3]] | C | PRUNE2 activity raises PDZRN3's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 5.10× lower at baseline in the lines without PRUNE2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY; co-absent with the target |
| [[SHC4]] | C | PRUNE2 activity raises SHC4's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 2.19× lower at baseline in the lines without PRUNE2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY; co-absent with the target |
| [[KCND2]] | C | PRUNE2 activity raises KCND2's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 1.96× lower at baseline in the lines without PRUNE2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.518). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.3, 37.0); signed map (46.2, 30.1). **Vector** length 64.9, 17.9% of its response variance represented; |z| ≥ 3 in 648 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +19.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +14.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +12.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.1 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +5.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +7.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.2 | +4.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.8 | -6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.6 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | prune homolog 2 with BCH domain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.2 — chr9:76,611,376-76,906,114 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BMCC1, BNIPXL, A214N16.3, bA214N16.3; previously C9orf65, KIAA0367 |
| Gene groups (HGNC) | BCH domain containing ; CRAL-TRIO lipid binding domain containing; PRUNE family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUY3](https://www.uniprot.org/uniprotkb/Q8WUY3) (Protein prune homolog 2):

> May play an important role in regulating differentiation, survival and aggressiveness of the tumor cells.

**Summary**, from NCBI Gene [158471](https://www.ncbi.nlm.nih.gov/gene/158471):

> The protein encoded by this gene belongs to the B-cell CLL/lymphoma 2 and adenovirus E1B 19 kDa interacting family, whose members play roles in many cellular processes including apotosis, cell transformation, and synaptic function. Several functions for this protein have been demonstrated including suppression of Ras homolog family member A activity, which results in reduced stress fiber formation and suppression of oncogenic cellular transformation. A high molecular weight isoform of this …

**Accessions** — [HGNC:25209](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25209) · Entrez [158471](https://www.ncbi.nlm.nih.gov/gene/158471) · UniProt [Q8WUY3](https://www.uniprot.org/uniprotkb/Q8WUY3) · Ensembl [ENSG00000106772](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106772)

## Data

Gene col 2803: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2803); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2803, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2803]; `tensor/DDL_lfc|DDL_z.npy` [2803]; `embed/gene_vectors.npy` [2803]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2803 or target_col == 2803). Every well: [[PRUNE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRUNE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
