---
symbol: "SLC29A4"
type: "gene"
col: 8978
ensembl_id: "ENSG00000164638"
name: "solute carrier family 29 member 4"
location: "7p22.1"
module: 100
arm: "+"
pooled_cpm: 5.5
n_lines_expressing: 44
n_dd_up: 15
n_dd_down: 15
n_dd_up_clean: 10
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 7
direction_downstream: 22
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# SLC29A4

*solute carrier family 29 member 4* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.28× (z +14.3, q 2e-43, up in 34 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.323× (z -13.3, q 1e-37, down in 30 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIMS3]] (+0.73, fdr 1e-05), [[PDZD7]] (+0.71, fdr 7e-06), [[CIB2]] (+0.70, fdr 1e-05); moves opposite to [[CARD8]] (-0.66, fdr 2e-05), [[CLHC1]] (-0.65, fdr 3e-05), [[INO80D]] (-0.63, fdr 3e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TSPAN33]] → it (grade B ⚠); 22 go from it, the strongest it → [[JAG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8978.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.28×** | +14.3 | 2e-43 | 34/42 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.52×** | +11.3 | 5e-27 | 26/41 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.37×** | +10.6 | 5e-24 | 29/39 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.37×** | +10.6 | 5e-24 | 31/41 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.19×** | +9.6 | 8e-20 | 28/41 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.17×** | +9.5 | 3e-19 | 25/41 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.80×** | +7.2 | 6e-11 | 22/37 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +6.0 | 2e-07 | 4/10 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.22×** | +5.1 | 2e-05 | 14/41 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.47×** | +4.7 | 1e-04 | 10/42 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.04×** | +4.6 | 2e-04 | 5/18 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.054 | 7/38 (HepG2/C3A, NCI-H1792, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.43×** | +3.1 | 0.072 | 2/17 (LoVo, SW480) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.1 | 0.072 | 4/37 (A549, C32, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.1 | 0.072 | 2/15 (SW480, LoVo) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8978.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.323×** | -13.3 | 1e-37 | 30/40 (NCI-H23, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.465×** | -13.2 | 1e-37 | 32/39 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.339×** | -13.2 | 1e-37 | 29/36 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.483×** | -8.9 | 9e-17 | 23/41 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.425×** | -5.5 | 5e-06 | 16/39 (A-427, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.647×** | -5.3 | 1e-05 | 18/41 (HOP62, RPMI-7951, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.670×** | -4.9 | 8e-05 | 16/41 (HT-29, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.698×** | -4.4 | 9e-04 | 11/40 (HT-29, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.700×** | -4.2 | 0.002 | 15/30 (AN3 CA, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.545×** | -3.9 | 0.006 | 9/33 (SK-MEL-2, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.747×** | -3.6 | 0.019 | 13/40 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.590×** | -3.4 | 0.035 | 6/42 (Hs 766T, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.758×** | -3.2 | 0.050 | 5/42 (NCI-H1792, HepG2/C3A, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.768×** | -3.2 | 0.051 | 9/39 (HOP62, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.764×** | -3.2 | 0.061 | 11/40 (SK-MEL-2, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8978. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 10.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0539× (z -22.5) |
| [[PANC-1 (line)]] | alt | 7.42 | 2 | 2 | [[Panobinostat (drug)]] 5 µM 4.29× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -13.1) |
| [[A-172 (line)]] | wt | 15.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -19.2) |
| [[A549 (line)]] | wt | 6.83 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0703× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 14.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -11.0) |
| [[A498 (line)]] | wt | 6.23 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +10.3) ⚠ cell-cycle shift, explains ~10% of this change | — |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -11.4) |
| [[C-33 A (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.108× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[HEC-1-A (line)]] | alt | 2.44 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0260× (z -11.5) |
| [[HT-29 (line)]] | alt | 9.04 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -14.0) |
| [[J82 (line)]] | alt | 5.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 3.77 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0717× (z -8.6) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 8.96 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0774× (z -11.6) |
| [[SW480 (line)]] | alt | 3.95 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.10× (z +9.5) | — |
| [[A-427 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.986 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.884 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.831 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8978), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIMS3]] | +0.73 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[PDZD7]] | +0.71 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[CIB2]] | +0.70 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[TSPAN33]] | +0.67 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[SMARCD3]] | +0.67 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[FOXO6]] | +0.66 | +0.40 / +0.65 | both halves | 5e-05 |  |
| [[STK32C]] | +0.66 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[MAPT]] | +0.66 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[HDAC3]] | +0.65 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SBK1]] | +0.65 | +0.41 / +0.69 | both halves | 4e-05 |  |
| [[TMEM63C]] | +0.65 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[RAB6B]] | +0.64 | +0.42 / +0.65 | both halves | 4e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARD8]] | -0.66 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[CLHC1]] | -0.65 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[INO80D]] | -0.63 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[MCPH1]] | -0.63 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ST7L]] | -0.62 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[GTF2H1]] | -0.62 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[PSME3IP1]] | -0.62 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[RIMOC1]] | -0.61 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[TASOR]] | -0.61 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ZXDB]] | -0.60 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[EFCAB2]] | -0.59 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[MCTS1]] | -0.59 | -0.51 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN33]] | B | TSPAN33 activity raises SLC29A4's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 2.01× lower at baseline in the lines without TSPAN33 | 0.019 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[JAG2]] | B | JAG2 activity raises SLC29A4's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.60× lower at baseline in the lines without JAG2 | 0.051 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[OTUD7A]] | B | OTUD7A activity raises SLC29A4's level | lines that do not express OTUD7A (6) vs lines expressing it (44) | 2.55× lower at baseline in the lines without OTUD7A | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000256673, WWOX, RUNDC3A-AS1; maybe low, not absent |
| [[PARD6G]] | B | PARD6G activity raises SLC29A4's level | lines that do not express PARD6G (10) vs lines expressing it (40) | 2.35× lower at baseline in the lines without PARD6G | 0.081 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent |
| [[MAN1C1]] | B | MAN1C1 activity raises SLC29A4's level | lines that do not express MAN1C1 (11) vs lines expressing it (39) | 1.75× lower at baseline in the lines without MAN1C1 | 0.095 | ⚠ within organs, on part of the lines; also absent: DHRS2; maybe low, not absent |
| [[CTXN1]] | C | CTXN1 activity raises SLC29A4's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 2.99× lower at baseline in the lines without CTXN1 | 0.008 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent; co-absent with the target |
| [[ASAP3]] | C | ASAP3 activity raises SLC29A4's level | lines that do not express ASAP3 (5) vs lines expressing it (45) | 3.15× lower at baseline in the lines without ASAP3 | 0.036 | ⚠ within organs, on part of the lines; also absent: DPF1, SCML2, CCDC102A; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 20, C 2. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAG2]] | B | SLC29A4 activity raises JAG2's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 2.00× lower at baseline in the lines without SLC29A4 | 0.009 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[FADS3]] | B | SLC29A4 activity raises FADS3's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 1.96× lower at baseline in the lines without SLC29A4 | 0.013 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[SEMA6B]] | B | SLC29A4 activity raises SEMA6B's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 3.81× lower at baseline in the lines without SLC29A4 | 0.023 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[GLIPR2]] | B | SLC29A4 activity raises GLIPR2's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 2.91× lower at baseline in the lines without SLC29A4 | 0.042 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[SMARCD3]] | B | SLC29A4 activity raises SMARCD3's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 2.47× lower at baseline in the lines without SLC29A4 | 0.044 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[SSBP4]] | B | SLC29A4 activity raises SSBP4's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 1.82× lower at baseline in the lines without SLC29A4 | 0.046 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[ANKRD27]] | B | SLC29A4 activity raises ANKRD27's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 1.42× lower at baseline in the lines without SLC29A4 | 0.046 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[FOXO6]] | B | SLC29A4 activity raises FOXO6's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 1.72× lower at baseline in the lines without SLC29A4 | 0.049 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[BMP8B]] | B | SLC29A4 activity raises BMP8B's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 1.56× lower at baseline in the lines without SLC29A4 | 0.052 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[MAST1]] | B | SLC29A4 activity raises MAST1's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 2.51× lower at baseline in the lines without SLC29A4 | 0.055 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[TMEM63C]] | B | SLC29A4 activity raises TMEM63C's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 1.76× lower at baseline in the lines without SLC29A4 | 0.065 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[MNX1]] | B | SLC29A4 activity raises MNX1's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 1.07× lower at baseline in the lines without SLC29A4 | 0.068 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.781). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.4, -2.1); signed map (-28.9, 22.2). **Vector** length 70.3, 12.4% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +14.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +10.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.5 | +10.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.6 | +7.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +11.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +4.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.8 | +1.0 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.5 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -13.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.8 | -13.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.8 | -8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -1.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.9 | -13.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 29 member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:5,274,369-5,306,912 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34923, ENT4 |
| Gene groups (HGNC) | Solute carrier family 29 |
| Reactome | 4 pathways, smallest: Transport of nucleosides and free purine and pyrimidine bases across the plasma membrane; Transport of vitamins, nucleosides, and related molecules; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7RTT9](https://www.uniprot.org/uniprotkb/Q7RTT9) (Equilibrative nucleoside transporter 4):

> Electrogenic voltage-dependent transporter that mediates the transport of a variety of endogenous bioactive amines, cationic xenobiotics and drugs. Utilizes the physiologic inside-negative membrane potential as a driving force to facilitate cellular uptake of organic cations. Functions as a Na(+)- and Cl(-)-independent bidirectional transporter. Substrate transport is pH-dependent and enhanced under acidic condition, which is most likely the result of allosteric changes in the transporter …

**Summary**, from NCBI Gene [222962](https://www.ncbi.nlm.nih.gov/gene/222962):

> This gene encodes a member of the SLC29A/ENT transporter protein family. The encoded membrane protein catalyzes the reuptake of monoamines into presynaptic neurons, thus determining the intensity and duration of monoamine neural signaling. It has been shown to transport several compounds, including serotonin, dopamine, and the neurotoxin 1-methyl-4-phenylpyridinium. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:23097](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23097) · Entrez [222962](https://www.ncbi.nlm.nih.gov/gene/222962) · UniProt [Q7RTT9](https://www.uniprot.org/uniprotkb/Q7RTT9) · Ensembl [ENSG00000164638](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164638)

## Data

Gene col 8978: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8978); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8978, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8978]; `tensor/DDL_lfc|DDL_z.npy` [8978]; `embed/gene_vectors.npy` [8978]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8978 or target_col == 8978). Every well: [[SLC29A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC29A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
