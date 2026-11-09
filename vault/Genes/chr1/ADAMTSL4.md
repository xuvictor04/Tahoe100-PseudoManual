---
symbol: "ADAMTSL4"
type: "gene"
col: 6731
ensembl_id: "ENSG00000143382"
name: "ADAMTS like 4"
location: "1q21.2"
module: 113
arm: "+"
pooled_cpm: 8.22
n_lines_expressing: 47
n_dd_up: 21
n_dd_down: 21
n_dd_up_clean: 18
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 7
direction_downstream: 2
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# ADAMTSL4

*ADAMTS like 4* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.88× (z +10.3, q 5e-22, up in 33 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.451× (z -9.2, q 3e-17, down in 28 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VSTM2L]] (+0.62, fdr 1e-05), [[MT1A]] (+0.59, fdr 1e-05), [[TLR2]] (+0.58, fdr 1e-05); moves opposite to [[NAALADL2]] (-0.45, fdr 4e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[RTN4RL1]] → it (grade B ⚠); 2 go from it, the strongest it → [[KLF9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6731.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.88×** | +10.3 | 5e-22 | 33/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.00×** | +8.0 | 4e-13 | 27/40 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.82×** | +6.9 | 9e-10 | 26/45 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.59×** | +5.3 | 1e-05 | 23/43 (HOP62, NCI-H460, …) | all doses, flat | position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.56×** | +5.1 | 4e-05 | 20/44 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.54×** | +5.0 | 7e-05 | 19/40 (PANC-1, NCI-H2030, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.33×** | +4.6 | 3e-04 | 12/43 (PANC-1, RPMI-7951, …) | all doses, flat | low cells (technical?) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.46×** | +4.4 | 8e-04 | 15/44 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.47×** | +4.4 | 8e-04 | 15/42 (NCI-H460, SNU-423, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.31×** | +4.3 | 8e-04 | 15/44 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.44×** | +4.2 | 0.001 | 17/40 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Econazole (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.004 | 15/44 (Hs 766T, NCI-H460, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.40×** | +3.9 | 0.005 | 14/41 (HOP62, A549, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.005 | 14/44 (NCI-H460, Hs 766T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.012 | 14/41 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.36×** | +3.6 | 0.012 | 19/44 (HOP62, Hs 766T, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.016 | 14/44 (Hs 766T, NCI-H1792, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6731.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.451×** | -9.2 | 3e-17 | 28/44 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.542×** | -6.8 | 3e-09 | 21/42 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.565×** | -6.6 | 9e-09 | 24/43 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.576×** | -6.4 | 3e-08 | 21/42 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.595×** | -6.0 | 2e-07 | 21/39 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.594×** | -5.8 | 7e-07 | 15/32 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.615×** | -5.6 | 2e-06 | 19/44 (A-172, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.638×** | -5.2 | 2e-05 | 16/43 (NCI-H460, NCI-H23, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.642×** | -5.1 | 2e-05 | 19/38 (MIA PaCa-2, J82, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.666×** | -4.7 | 2e-04 | 17/44 (NCI-H460, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.697×** | -4.2 | 0.002 | 15/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.706×** | -4.0 | 0.004 | 16/43 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.793×** | -3.8 | 0.007 | 13/44 (HepG2/C3A, J82, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.729×** | -3.6 | 0.011 | 15/44 (NCI-H23, NCI-H1792, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.729×** | -3.5 | 0.017 | 14/38 (BT-474, PANC-1, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.748×** | -3.3 | 0.028 | 12/42 (A549, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.05 µM |  | **0.748×** | -3.3 | 0.028 | 11/43 (SNU-423, A549, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.614×** | -2.9 | 0.098 | 8/34 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.777×** | -2.9 | 0.099 | 9/44 (BT-474, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6731. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.217× (z -9.8) |
| [[J82 (line)]] | alt | 33.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 6.77 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.101× (z -8.5) |
| [[BT-474 (line)]] | alt | 9.14 | 0 | 1 | — | [[Trametinib (drug)]] 0.5 µM 0.130× (z -9.7) |
| [[C32 (line)]] | wt | 3.95 | 0 | 1 (1 ⚠) | — | [[Ribociclib (drug)]] 0.05 µM 0.0549× (z -8.8) ⚠ unreliable plate only; position not correctable |
| [[Hs 766T (line)]] | wt | 17.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0866× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 6.64 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.133× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 3.69 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0743× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 18.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.231× (z -9.1) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 17.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.146× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 3.33 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.66× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 9.94 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.200× (z -11.2) |
| [[A-172 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6731), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VSTM2L]] | +0.62 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[MT1A]] | +0.59 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[TLR2]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[GALK1]] | +0.57 | +0.62 / +0.48 | both halves | 2e-05 | pathway: Diseases of glycosylation |
| [[MT1X]] | +0.55 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[MT1M]] | +0.55 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[IRAK3]] | +0.54 | +0.41 / +0.54 | both halves | 4e-05 | same gene group |
| [[PID1]] | +0.53 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[TANC2]] | +0.53 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[KCNG2]] | +0.52 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[JPH2]] | +0.52 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[MT1E]] | +0.52 | +0.52 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAALADL2]] | -0.45 | -0.41 / -0.47 | both halves | 4e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RTN4RL1]] | B | RTN4RL1 activity raises ADAMTSL4's level | lines that do not express RTN4RL1 (14) vs lines expressing it (36) | 1.78× lower at baseline in the lines without RTN4RL1 | 0.021 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity raises ADAMTSL4's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[C3]] | B | C3 activity lowers ADAMTSL4's level | lines that do not express C3 (32) vs lines expressing it (18) | 1.13× higher at baseline in the lines without C3 | 0.052 | ⚠ within organs, on part of the lines; also absent: TNFSF14, CP, CARD11 |
| [[ADGRG2]] | B | ADGRG2 activity raises ADAMTSL4's level | lines that do not express ADGRG2 (10) vs lines expressing it (40) | 1.28× lower at baseline in the lines without ADGRG2 | 0.053 | ⚠ within organs, on part of the lines; also absent: KCNN3, SLC17A7, STARD8; maybe low, not absent |
| [[MEIS3]] | B | MEIS3 activity raises ADAMTSL4's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 1.61× lower at baseline in the lines without MEIS3 | 0.058 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| [[NAALADL2]] | B | NAALADL2 activity lowers ADAMTSL4's level | lines that do not express NAALADL2 (11) vs lines expressing it (39) | 1.59× higher at baseline in the lines without NAALADL2 | 0.088 | ⚠ within organs, on part of the lines; also absent: CA3, PCNX2, CA13 |
| [[SLCO2A1]] | B | SLCO2A1 activity raises ADAMTSL4's level | lines that do not express SLCO2A1 (16) vs lines expressing it (34) | 1.83× lower at baseline in the lines without SLCO2A1 | 0.092 | ⚠ within organs, on part of the lines; also absent: FHL1, CYS1, LIMS2 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLF9]] | C | ADAMTSL4 activity raises KLF9's level | lines that do not express ADAMTSL4 (3) vs lines expressing it (47) | 4.02× lower at baseline in the lines without ADAMTSL4 | 0.058 | ⚠ few lines (3 vs 47); across organs; also absent: BLVRA, ITGA2B, SOAT1; maybe low, not absent |
| cells under [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM | C | ADAMTSL4 activity lowers the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (makes them more sensitive) | lines that do not express ADAMTSL4 (3) vs lines expressing it (45) | the lines without ADAMTSL4: 1.23× the cells of the other lines | 0.096 | ⚠ few lines (3 vs 47); across organs; also absent: BLVRA, ITGA2B, SOAT1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.665). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.8, 14.0); signed map (15.2, 31.8). **Vector** length 85.9, 16.8% of its response variance represented; |z| ≥ 3 in 1,111 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Metallothioneins bind metals* (reactome, mean cos +0.52 to 5); *metallothionein* (control, mean cos +0.52 to 5); *Response to metal ions* (reactome, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +8.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.3 | +4.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.5 | +5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | +1.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.3 | +4.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.1 | +4.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.9 | +4.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -6.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.4 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -9.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -5.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.1 | -3.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | ADAMTS like 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:150,549,369-150,560,937 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434K1772; previously TSRC1 |
| Gene groups (HGNC) | ADAMTS like; MicroRNA protein coding host genes |
| Reactome | 6 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UY14](https://www.uniprot.org/uniprotkb/Q6UY14) (ADAMTS-like protein 4):

> Positive regulation of apoptosis. May facilitate FBN1 microfibril biogenesis.

**Summary**, from NCBI Gene [54507](https://www.ncbi.nlm.nih.gov/gene/54507):

> This gene is a member of ADAMTS (a disintegrin and metalloproteinase with thrombospondin motifs)-like gene family and encodes a protein with seven thrombospondin type 1 repeats. The thrombospondin type 1 repeat domain is found in many proteins with diverse biological functions including cellular adhesion, angiogenesis, and patterning of the developing nervous system. Alternate transcriptional splice variants, encoding different isoforms, have been characterized. [provided by RefSeq, Sep 2014]

**Accessions** — [HGNC:19706](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19706) · Entrez [54507](https://www.ncbi.nlm.nih.gov/gene/54507) · UniProt [Q6UY14](https://www.uniprot.org/uniprotkb/Q6UY14) · Ensembl [ENSG00000143382](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143382)

## Data

Gene col 6731: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6731); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6731, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6731]; `tensor/DDL_lfc|DDL_z.npy` [6731]; `embed/gene_vectors.npy` [6731]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6731 or target_col == 6731). Every well: [[ADAMTSL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTSL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
