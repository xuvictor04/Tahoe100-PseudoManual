---
symbol: "WNT7B"
type: "gene"
col: 11973
ensembl_id: "ENSG00000188064"
name: "Wnt family member 7B"
location: "22q13.31"
module: 34
arm: "+"
pooled_cpm: 24.16
n_lines_expressing: 30
n_dd_up: 4
n_dd_down: 64
n_dd_up_clean: 4
n_dd_down_clean: 56
in_vector_space: true
direction_upstream: 40
direction_downstream: 62
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# WNT7B

*Wnt family member 7B* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.57× (z +8.5, q 9e-15, up in 15 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 64 drug-doses (8 with an alert ⚠); the strongest is [[Budesonide (drug)]] 5 µM: 0.438× (z -10.9, q 1e-24, down in 19 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM107B]] (+0.71, fdr 7e-06), [[CDCP1]] (+0.71, fdr 7e-06), [[OTUB2]] (+0.69, fdr 7e-06); moves opposite to [[BATF]] (-0.57, fdr 1e-05), [[ADGRG2]] (-0.56, fdr 1e-05), [[NNMT]] (-0.55, fdr 1e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 40 arrows point to it, the strongest [[C6orf141]] → it (grade B ⚠); 62 go from it, the strongest it → [[CDCP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11973.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +8.5 | 9e-15 | 15/28 (HOP62, J82, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +5.2 | 7e-05 | 13/27 (SW480, KATO III, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +3.8 | 0.024 | 9/28 (J82, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 5 µM |  | 1.19× | +3.4 | 0.090 | 7/28 (HEC-1-A, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.090 | 9/27 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 65 in all, 9 with an alert ⚠; shown: the 15 strongest. 64 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11973.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 5 µM |  | **0.438×** | -10.9 | 1e-24 | 19/28 (A549, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.481×** | -9.6 | 2e-19 | 16/27 (A549, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **0.602×** | -9.4 | 9e-19 | 19/28 (NCI-H1792, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **0.516×** | -8.7 | 5e-16 | 16/28 (NCI-H1792, A549, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.526×** | -8.4 | 3e-15 | 17/28 (NCI-H1792, A549, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.530×** | -8.3 | 7e-15 | 16/27 (NCI-H1792, A549, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.512×** | -8.1 | 3e-14 | 17/26 (NCI-H1792, A549, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.557×** | -7.7 | 1e-12 | 18/27 (A549, NCI-H1792, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.561×** | -7.6 | 2e-12 | 17/27 (NCI-H1792, A549, …) | all doses, flat | position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.564×** | -7.5 | 3e-12 | 17/28 (A549, NCI-H1792, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.570×** | -7.4 | 8e-12 | 14/27 (NCI-H1792, A549, …) | all doses, flat | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.573×** | -7.0 | 9e-11 | 23/28 (HEC-1-A, SW 900, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.597×** | -6.8 | 6e-10 | 17/27 (A549, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.607×** | -6.6 | 2e-09 | 17/27 (NCI-H1792, A549, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.595×** | -6.5 | 2e-09 | 18/27 (A549, NCI-H1792, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11973. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 146 | 0 | 32 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -22.2) |
| [[NCI-H1792 (line)]] | alt | 65.2 | 0 | 27 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0865× (z -23.2) |
| [[Hs 766T (line)]] | wt | 69.1 | 0 | 17 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -15.4) |
| [[NCI-H1573 (line)]] | alt | 25.9 | 0 | 10 | — | [[Budesonide (drug)]] 0.05 µM 0.146× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 51.3 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.102× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -17.4) |
| [[LoVo (line)]] | wt | 41.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -17.3) |
| [[NCI-H2030 (line)]] | alt | 42.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -22.4) |
| [[HOP62 (line)]] | alt | 11.3 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +10.9) | [[Adagrasib (drug)]] 0.05 µM 0.577× (z -8.7) ⚠ position not correctable · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.160× (z -8.7) |
| [[SW 900 (line)]] | alt | 47.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 103 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -13.1) |
| [[H4 (line)]] | wt | 13.6 | 0 | 3 | — | [[Triamcinolone (drug)]] 0.5 µM 0.0339× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 27.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -10.4) |
| [[BT-474 (line)]] | alt | 15.0 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0801× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 95.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -15.3) |
| [[SW480 (line)]] | alt | 12.7 | 0 | 2 | — | [[Cobimetinib (drug)]] 0.5 µM 0.162× (z -9.3) |
| [[HS-578T (line)]] | alt | 29.4 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.162× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -13.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 25.9 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.05× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.149× (z -9.3) |
| [[A-172 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.79 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.90 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.96 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11973), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM107B]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[CDCP1]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[OTUB2]] | +0.69 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[PKIA]] | +0.69 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[WSCD1]] | +0.69 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[SYNJ2]] | +0.68 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[EHD1]] | +0.66 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[ARHGEF4]] | +0.66 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ADAM8]] | +0.66 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[ITGA2]] | +0.65 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[TINAGL1]] | +0.65 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[PLEK2]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BATF]] | -0.57 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[ADGRG2]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[NNMT]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ARMC8]] | -0.53 | -0.54 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 29, C 11. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C6orf141]] | B | C6orf141 activity raises WNT7B's level | lines that do not express C6orf141 (21) vs lines expressing it (29) | 2.84× lower at baseline in the lines without C6orf141 | 0.005 | ⚠ within organs, on part of the lines; also absent: ADAM8, ENSG00000251584, SAMD12-AS1 |
| [[PLEK2]] | B | PLEK2 activity raises WNT7B's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.63× lower at baseline in the lines without PLEK2 | 0.007 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[LAMB3]] | B | LAMB3 activity raises WNT7B's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 3.23× lower at baseline in the lines without LAMB3 | 0.008 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[FAM107B]] | B | FAM107B activity raises WNT7B's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 3.80× lower at baseline in the lines without FAM107B | 0.009 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[TMCC3]] | B | TMCC3 activity raises WNT7B's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 2.73× lower at baseline in the lines without TMCC3 | 0.013 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[CDCP1]] | B | CDCP1 activity raises WNT7B's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 3.00× lower at baseline in the lines without CDCP1 | 0.016 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[TNFRSF11A]] | B | TNFRSF11A activity raises WNT7B's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 2.65× lower at baseline in the lines without TNFRSF11A | 0.022 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[S100A16]] | B | S100A16 activity raises WNT7B's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 4.79× lower at baseline in the lines without S100A16 | 0.022 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[AADACP1]] | B | AADACP1 activity raises WNT7B's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 2.43× lower at baseline in the lines without AADACP1 | 0.025 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1 |
| [[GPRC5A]] | B | GPRC5A activity raises WNT7B's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 3.03× lower at baseline in the lines without GPRC5A | 0.025 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[PRSS3]] | B | PRSS3 activity raises WNT7B's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 2.45× lower at baseline in the lines without PRSS3 | 0.026 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[FA2H]] | B | FA2H activity raises WNT7B's level | lines that do not express FA2H (27) vs lines expressing it (23) | 3.01× lower at baseline in the lines without FA2H | 0.027 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |

### Downstream of this gene

*62 arrows, 62 of them with an alert ⚠; grade A 0, B 51, C 11. Shown: the 12 strongest; 50 more arrows (50 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCP1]] | B | WNT7B activity raises CDCP1's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 2.69× lower at baseline in the lines without WNT7B | 0.003 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[GRB10]] | B | WNT7B activity raises GRB10's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 3.47× lower at baseline in the lines without WNT7B | 0.003 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[FAM107B]] | B | WNT7B activity raises FAM107B's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 3.41× lower at baseline in the lines without WNT7B | 0.004 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[PMEPA1]] | B | WNT7B activity raises PMEPA1's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 2.63× lower at baseline in the lines without WNT7B | 0.004 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[TGFA]] | B | WNT7B activity raises TGFA's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 2.98× lower at baseline in the lines without WNT7B | 0.005 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[SYNJ2]] | B | WNT7B activity raises SYNJ2's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 2.24× lower at baseline in the lines without WNT7B | 0.005 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[LAMB3]] | B | WNT7B activity raises LAMB3's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 3.52× lower at baseline in the lines without WNT7B | 0.007 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[PORCN]] | B | WNT7B activity raises PORCN's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 2.06× lower at baseline in the lines without WNT7B | 0.007 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[EHD1]] | B | WNT7B activity raises EHD1's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 1.71× lower at baseline in the lines without WNT7B | 0.007 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[SERINC2]] | B | WNT7B activity raises SERINC2's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 2.34× lower at baseline in the lines without WNT7B | 0.008 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[PTPRE]] | B | WNT7B activity raises PTPRE's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 2.73× lower at baseline in the lines without WNT7B | 0.008 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[ITGA2]] | B | WNT7B activity raises ITGA2's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 3.52× lower at baseline in the lines without WNT7B | 0.013 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.809). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.9, -0.0); signed map (1.5, 45.9). **Vector** length 118, 34.9% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +8.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.1 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | -0.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +5.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +1.8 | +2.3 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -5.2 | -9.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -5.2 | -6.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -5.0 | -9.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -4.9 | -8.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.9 | -7.7 |

## What is on record

|  |  |
|---|---|
| Name | Wnt family member 7B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:45,920,366-45,977,162 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Wnt family |
| Reactome | 5 pathways, smallest: WNT ligand biogenesis and trafficking; Class B/2 (Secretin family receptors); GPCR ligand binding |
| Matched by | ensembl_id |

**Function**, from UniProt [P56706](https://www.uniprot.org/uniprotkb/P56706) (Protein Wnt-7b):

> Ligand for members of the frizzled family of seven transmembrane receptors that functions in the canonical Wnt/beta-catenin signaling pathway. Required for normal fusion of the chorion and the allantois during placenta development (By similarity). Required for central nervous system (CNS) angiogenesis and blood-brain barrier regulation.

**Summary**, from NCBI Gene [7477](https://www.ncbi.nlm.nih.gov/gene/7477):

> This gene is a member of the WNT gene family, which consists of structurally related genes that encode secreted signaling proteins. These proteins have been implicated in oncogenesis and in several developmental processes, including regulation of cell fate and patterning during embryogenesis. Among members of the human WNT family, this gene product is most similar to WNT7A protein. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:12787](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12787) · Entrez [7477](https://www.ncbi.nlm.nih.gov/gene/7477) · UniProt [P56706](https://www.uniprot.org/uniprotkb/P56706) · Ensembl [ENSG00000188064](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188064)

## Data

Gene col 11973: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11973); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11973, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11973]; `tensor/DDL_lfc|DDL_z.npy` [11973]; `embed/gene_vectors.npy` [11973]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11973 or target_col == 11973). Every well: [[WNT7B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WNT7B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
