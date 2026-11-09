---
symbol: "ROR1-AS1"
type: "gene"
col: 13370
ensembl_id: "ENSG00000223949"
name: "ROR1 antisense RNA 1"
location: "1p31.3"
module: 125
arm: "+"
pooled_cpm: 11.35
n_lines_expressing: 24
n_dd_up: 39
n_dd_down: 17
n_dd_up_clean: 29
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 9
direction_downstream: 29
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# ROR1-AS1

*ROR1 antisense RNA 1* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.15× (z +10.7, q 6e-24, up in 13 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.609× (z -4.9, q 5e-04, down in 17 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLAMF7]] (+0.77, fdr 7e-06), [[SHISAL1]] (+0.72, fdr 7e-06), [[C12orf50]] (+0.72, fdr 7e-06); moves opposite to [[PIGS]] (-0.51, fdr 3e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 29 go from it, the strongest it → [[RPLP0P2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13370.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.15×** | +10.7 | 6e-24 | 13/20 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.57×** | +8.8 | 3e-16 | 14/18 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.42×** | +8.7 | 6e-16 | 16/20 (C32, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.19×** | +7.7 | 2e-12 | 12/20 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +7.6 | 3e-12 | 1/16 (A549) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +7.0 | 2e-10 | 4/13 (SK-MEL-2, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.97×** | +6.3 | 2e-08 | 14/20 (SNU-423, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +6.2 | 4e-08 | 4/18 (A549, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.92×** | +6.1 | 7e-08 | 18/20 (HS-578T, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +6.0 | 9e-08 | 0/12 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.78×** | +5.7 | 7e-07 | 16/20 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.00×** | +5.7 | 7e-07 | 9/11 (HEC-1-A, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.73×** | +5.1 | 1e-05 | 8/20 (SK-MEL-2, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +5.0 | 2e-05 | 10/19 (HOP62, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.9 | 3e-05 | 11/22 (J82, HS-578T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +4.6 | 1e-04 | 12/21 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pralsetinib (drug)]] 5 µM |  | **2.38×** | +4.5 | 2e-04 | 7/16 (HS-578T, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +4.4 | 3e-04 | 11/20 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.55×** | +4.3 | 4e-04 | 10/20 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +3.8 | 0.003 | 8/20 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +3.7 | 0.006 | 13/20 (SK-MEL-2, hTERT-HPNE, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13370.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.609×** | -4.9 | 5e-04 | 17/21 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.875× | -4.5 | 0.002 | 6/22 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.649×** | -4.3 | 0.003 | 15/20 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.653×** | -4.2 | 0.003 | 9/21 (SNU-423, NCI-H1792, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.655×** | -4.2 | 0.003 | 10/21 (NCI-H1792, SNU-423, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.660×** | -3.9 | 0.009 | 9/19 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.682×** | -3.8 | 0.012 | 12/21 (SNU-423, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **0.688×** | -3.7 | 0.012 | 9/21 (SNU-423, NCI-H1792, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.769×** | -3.7 | 0.012 | 8/21 (NCI-H1792, A549, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.689×** | -3.7 | 0.012 | 10/20 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.691×** | -3.7 | 0.012 | 7/20 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **0.523×** | -3.4 | 0.037 | 5/20 (SNU-423, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.720×** | -3.3 | 0.047 | 12/20 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.723×** | -3.2 | 0.050 | 6/20 (NCI-H1792, SNU-423, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.732×** | -3.1 | 0.072 | 8/21 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.735×** | -3.1 | 0.079 | 11/21 (SNU-423, NCI-H1792, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13370. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 13.3 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +17.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0719× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.115× (z -9.3) |
| [[SNU-423 (line)]] | alt | 60.6 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.217× (z -9.2) |
| [[A498 (line)]] | wt | 3.90 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 17.6 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 8.20× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 197 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -14.1) |
| [[CFPAC-1 (line)]] | alt | 5.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.94× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 4.75 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0752× (z -9.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HOP62 (line)]] | alt | 23.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.65× (z +8.8) | — |
| [[J82 (line)]] | alt | 5.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 38.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 11.2× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0804× (z -9.1) |
| [[A-427 (line)]] | wt | 0.873 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.17 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13370), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLAMF7]] | +0.77 | +0.75 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SHISAL1]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[C12orf50]] | +0.72 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[ENTHD1]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[LINC02154]] | +0.69 | +0.54 / +0.76 | both halves | 1e-05 |  |
| [[CSF2]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[ANKRD30B]] | +0.68 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[CRYM]] | +0.67 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[NGF]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[MIR155HG]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[NAALADL2-AS2]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 | same gene group |
| [[DYRK3]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGS]] | -0.51 | -0.47 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers ROR1-AS1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.8% of all compounds | 0.028 | ⚠ off-target possible; 3 compounds |
| [[LINC02605]] | B | LINC02605 activity raises ROR1-AS1's level | lines that do not express LINC02605 (15) vs lines expressing it (35) | 2.48× lower at baseline in the lines without LINC02605 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000285744, FAR2, ENSG00000285517 |
| [[LIF]] | B | LIF activity raises ROR1-AS1's level | lines that do not express LIF (10) vs lines expressing it (40) | 2.12× lower at baseline in the lines without LIF | 0.095 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213 |
| [[LINC02154]] | C | LINC02154 activity raises ROR1-AS1's level | lines that do not express LINC02154 (37) vs lines expressing it (13) | 3.99× lower at baseline in the lines without LINC02154 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FCRLA, ENSG00000234426, ENSG00000289530; co-absent with the target |
| [[LINC02509]] | C | LINC02509 activity raises ROR1-AS1's level | lines that do not express LINC02509 (35) vs lines expressing it (15) | 2.46× lower at baseline in the lines without LINC02509 | 0.025 | ⚠ within organs, on part of the lines; also absent: POSTN, ITGA11, IRAG2; co-absent with the target |
| [[TNFRSF9]] | C | TNFRSF9 activity raises ROR1-AS1's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 2.99× lower at baseline in the lines without TNFRSF9 | 0.038 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises ROR1-AS1's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 2.83× lower at baseline in the lines without CDH13 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[ATP6V0D2]] | C | ATP6V0D2 activity raises ROR1-AS1's level | lines that do not express ATP6V0D2 (18) vs lines expressing it (32) | 2.77× lower at baseline in the lines without ATP6V0D2 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D, ARID1A; also absent: GBP5, NALCN, IGFBP7; maybe low, not absent; co-absent with the target |
| [[IGFN1]] | C | IGFN1 activity raises ROR1-AS1's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 2.71× lower at baseline in the lines without IGFN1 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9; co-absent with the target |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 13, C 16. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPLP0P2]] | B | ROR1-AS1 activity raises RPLP0P2's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 1.94× lower at baseline in the lines without ROR1-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2 |
| [[ZNF469]] | B | ROR1-AS1 activity raises ZNF469's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 2.97× lower at baseline in the lines without ROR1-AS1 | 0.022 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2 |
| [[UBTD2]] | B | ROR1-AS1 activity raises UBTD2's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 1.46× lower at baseline in the lines without ROR1-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2 |
| [[TUSC3]] | B | ROR1-AS1 activity strengthens TUSC3's drug response | lines that do not express ROR1-AS1 (10) vs lines expressing it (22) | the lines without ROR1-AS1 respond 0.48× as strongly (z diff +2.81); strongest at Auranofin 5 µM: 0.91x vs 1.77x (z diff +5.8) | 0.047 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2; target measured in part of the lines; artifact flags |
| [[LINC01828]] | B | ROR1-AS1 activity raises LINC01828's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 2.52× lower at baseline in the lines without ROR1-AS1 | 0.049 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2 |
| [[AMPD3]] | B | ROR1-AS1 activity raises AMPD3's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 1.88× lower at baseline in the lines without ROR1-AS1 | 0.050 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2 |
| [[LINC00536]] | B | ROR1-AS1 activity raises LINC00536's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 2.58× lower at baseline in the lines without ROR1-AS1 | 0.050 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2 |
| [[CRYM]] | B | ROR1-AS1 activity raises CRYM's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 1.97× lower at baseline in the lines without ROR1-AS1 | 0.053 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2 |
| [[CXCL8]] | B | ROR1-AS1 activity raises CXCL8's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 3.41× lower at baseline in the lines without ROR1-AS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2 |
| [[LIF]] | B | ROR1-AS1 activity raises LIF's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 2.17× lower at baseline in the lines without ROR1-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2 |
| [[TRAF1]] | B | ROR1-AS1 activity raises TRAF1's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 2.46× lower at baseline in the lines without ROR1-AS1 | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2 |
| [[GEM]] | B | ROR1-AS1 activity raises GEM's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 1.65× lower at baseline in the lines without ROR1-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2 |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.804). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.3, 21.6); signed map (38.4, 22.5). **Vector** length 68.6, 20.2% of its response variance represented; |z| ≥ 3 in 584 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.5 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +7.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.5 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +3.7 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.8 | -3.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.5 | -3.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.3 | -4.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.3 | -2.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ROR1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p31.3 — chr1:64,094,379-64,171,342 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40508](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40508) · Entrez [101927034](https://www.ncbi.nlm.nih.gov/gene/101927034) · Ensembl [ENSG00000223949](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223949)

## Data

Gene col 13370: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13370); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13370, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13370]; `tensor/DDL_lfc|DDL_z.npy` [13370]; `embed/gene_vectors.npy` [13370]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13370 or target_col == 13370). Every well: [[ROR1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ROR1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
