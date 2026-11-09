---
symbol: "BANK1"
type: "gene"
col: 7685
ensembl_id: "ENSG00000153064"
name: "B cell scaffold protein with ankyrin repeats 1"
location: "4q24"
module: 27
arm: "+"
pooled_cpm: 7.88
n_lines_expressing: 38
n_dd_up: 24
n_dd_down: 14
n_dd_up_clean: 21
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 11
direction_downstream: 9
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# BANK1

*B cell scaffold protein with ankyrin repeats 1* — 4q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.51× (z +23.2, q 0e+00, up in 21 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.597× (z -5.6, q 1e-05, down in 19 of 33 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00649]] (+0.70, fdr 1e-05), [[DIP2C-AS1]] (+0.70, fdr 7e-06), [[PKHD1]] (+0.70, fdr 7e-06); moves opposite to [[ZNF549]] (-0.57, fdr 4e-05), [[ZCCHC17]] (-0.56, fdr 5e-05), [[AP1M1]] (-0.55, fdr 5e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[GNGT1]] → it (grade B ⚠); 9 go from it, the strongest it → [[PLCH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7685.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.51×** | +23.2 | 0e+00 | 21/29 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.41×** | +13.3 | 3e-38 | 22/31 (A549, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +10.2 | 5e-22 | 11/18 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +9.8 | 2e-20 | 5/10 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +7.9 | 3e-13 | 12/29 (LS 180, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +7.4 | 2e-11 | 3/12 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +6.2 | 4e-08 | 12/33 (A549, A498, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +5.7 | 8e-07 | 8/22 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.69×** | +5.5 | 2e-06 | 13/28 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +5.5 | 2e-06 | 14/33 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +4.6 | 2e-04 | 14/33 (KATO III, SW480, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.35×** | +4.5 | 3e-04 | 12/32 (SW480, CFPAC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.52×** | +4.5 | 3e-04 | 13/32 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.1 | 0.001 | 9/25 (LS 180, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.46×** | +4.1 | 0.002 | 12/32 (KATO III, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +4.0 | 0.002 | 8/27 (LS 180, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.006 | 7/30 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.017 | 11/34 (SW480, HCT15, …) | all doses, flat | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7685.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.597×** | -5.6 | 1e-05 | 19/33 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.620×** | -5.2 | 6e-05 | 16/26 (HCT15, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.628×** | -5.1 | 8e-05 | 17/31 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.663×** | -4.5 | 0.001 | 18/33 (HT-29, SW480, …) | two highest doses | cell-cycle shift (explains ~23% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.689×** | -4.1 | 0.005 | 9/27 (SW480, MIA PaCa-2, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.691×** | -4.0 | 0.005 | 18/31 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.694×** | -4.0 | 0.006 | 15/34 (SW480, HT-29, …) | two highest doses | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.717×** | -3.6 | 0.021 | 12/33 (SW480, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.719×** | -3.6 | 0.021 | 15/35 (SW480, HT-29, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.727×** | -3.5 | 0.031 | 12/32 (HT-29, KATO III, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.723×** | -3.4 | 0.037 | 7/33 (RPMI-7951, MIA PaCa-2, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.808×** | -3.3 | 0.049 | 11/33 (HT-29, MIA PaCa-2, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.747×** | -3.2 | 0.066 | 14/30 (SW480, A549, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.736×** | -3.2 | 0.066 | 4/32 (KATO III, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7685. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 18.7 | 0 | 16 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0615× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.142× (z -11.9) |
| [[HT-29 (line)]] | alt | 59.8 | 0 | 13 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0721× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0820× (z -15.1) |
| [[KATO III (line)]] | alt | 38.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -14.4) |
| [[NCI-H1792 (line)]] | alt | 19.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0350× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.195× (z -10.9) |
| [[LS 180 (line)]] | wt | 5.21 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 17.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0448× (z -12.4) |
| [[SHP-77 (line)]] | alt | 33.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[CFPAC-1 (line)]] | alt | 6.02 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.5 µM 0.107× (z -9.1) |
| [[HCT15 (line)]] | alt | 15.5 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0565× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 8.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +9.5) | — |
| [[LoVo (line)]] | wt | 7.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.81× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 5.02 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0602× (z -8.7) |
| [[A-172 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7685), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00649]] | +0.70 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[DIP2C-AS1]] | +0.70 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[PKHD1]] | +0.70 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[LIPC]] | +0.66 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[LINC01748]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[CCDC170]] | +0.65 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[DLEU1]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[CES3]] | +0.65 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[LINC01091]] | +0.64 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[B3GAT1-DT]] | +0.64 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[TAPBPL]] | +0.64 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[GUCY1B2]] | +0.63 | +0.67 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF549]] | -0.57 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[ZCCHC17]] | -0.56 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[AP1M1]] | -0.55 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[PBX4]] | -0.55 | -0.54 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNGT1]] | B | GNGT1 activity raises BANK1's level | lines that do not express GNGT1 (30) vs lines expressing it (20) | 1.99× lower at baseline in the lines without GNGT1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3 |
| [[LINC01611]] | B | LINC01611 activity raises BANK1's level | lines that do not express LINC01611 (34) vs lines expressing it (16) | 2.05× lower at baseline in the lines without LINC01611 | 0.013 | ⚠ within organs, on part of the lines; also absent: CDH13, ENSG00000248973, LINC02377 |
| [[TOP2A]] | B | TOP2A activity lowers BANK1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MIR4713HG]] | B | MIR4713HG activity raises BANK1's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 2.38× lower at baseline in the lines without MIR4713HG | 0.017 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA |
| [[GLDN]] | B | GLDN activity raises BANK1's level | lines that do not express GLDN (25) vs lines expressing it (25) | 2.13× lower at baseline in the lines without GLDN | 0.022 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595 |
| [[NIHCOLE]] | B | NIHCOLE activity raises BANK1's level | lines that do not express NIHCOLE (22) vs lines expressing it (28) | 2.13× lower at baseline in the lines without NIHCOLE | 0.023 | ⚠ within organs, on part of the lines; also absent: RORC, TSPAN1, VIL1 |
| [[HFE]] | B | HFE activity lowers BANK1's level | lines that do not express HFE (5) vs lines expressing it (45) | 1.48× higher at baseline in the lines without HFE | 0.060 | ⚠ within organs, on part of the lines; also absent: HOXA-AS2, PIM1, CBR1; its own permutation p |
| [[GOLGA2P5-1]] | B | GOLGA2P5-1 activity raises BANK1's level | lines that do not express GOLGA2P5-1 (8) vs lines expressing it (42) | 2.18× lower at baseline in the lines without GOLGA2P5-1 | 0.063 | ⚠ within organs, on part of the lines; also absent: GOLGA2P5, ENSG00000257489, KCNIP3; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers BANK1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LIPC]] | B | LIPC activity raises BANK1's level | lines that do not express LIPC (18) vs lines expressing it (32) | 1.61× lower at baseline in the lines without LIPC | 0.092 | ⚠ within organs, on part of the lines; also absent: TNFSF10, NIHCOLE, HNMT; maybe low, not absent |
| [[LINC01748]] | B | LINC01748 activity raises BANK1's level | lines that do not express LINC01748 (34) vs lines expressing it (16) | 2.05× lower at baseline in the lines without LINC01748 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CALB1, ATP10B, CLRN3 |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLCH1]] | B | BANK1 activity raises PLCH1's level | lines that do not express BANK1 (12) vs lines expressing it (38) | 2.43× lower at baseline in the lines without BANK1 | 0.032 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[BCAR3-AS1]] | B | BANK1 activity raises BCAR3-AS1's level | lines that do not express BANK1 (12) vs lines expressing it (38) | 1.55× lower at baseline in the lines without BANK1 | 0.049 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[EPCAM-DT]] | B | BANK1 activity raises EPCAM-DT's level | lines that do not express BANK1 (12) vs lines expressing it (38) | 2.46× lower at baseline in the lines without BANK1 | 0.050 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TMEM184A]] | B | BANK1 activity raises TMEM184A's level | lines that do not express BANK1 (12) vs lines expressing it (38) | 1.71× lower at baseline in the lines without BANK1 | 0.057 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NIHCOLE]] | B | BANK1 activity raises NIHCOLE's level | lines that do not express BANK1 (12) vs lines expressing it (38) | 3.62× lower at baseline in the lines without BANK1 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[OVOL2]] | B | BANK1 activity raises OVOL2's level | lines that do not express BANK1 (12) vs lines expressing it (38) | 1.58× lower at baseline in the lines without BANK1 | 0.074 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FCGRT]] | B | BANK1 activity raises FCGRT's level | lines that do not express BANK1 (12) vs lines expressing it (38) | 1.99× lower at baseline in the lines without BANK1 | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CHDH]] | B | BANK1 activity raises CHDH's level | lines that do not express BANK1 (12) vs lines expressing it (38) | 1.74× lower at baseline in the lines without BANK1 | 0.083 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[EPS15-AS1]] | B | BANK1 activity raises EPS15-AS1's level | lines that do not express BANK1 (12) vs lines expressing it (38) | 1.71× lower at baseline in the lines without BANK1 | 0.084 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.4, 44.4); signed map (58.3, 16.7). **Vector** length 71.2, 14.8% of its response variance represented; |z| ≥ 3 in 880 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +23.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +5.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +3.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.9 | -5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -4.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.5 | -5.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.5 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -2.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -3.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -2.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | B cell scaffold protein with ankyrin repeats 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q24 — chr4:101,411,286-102,074,812 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BANK, FLJ20706 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDB2](https://www.uniprot.org/uniprotkb/Q8NDB2) (B-cell scaffold protein with ankyrin repeats):

> Involved in B-cell receptor (BCR)-induced Ca(2+) mobilization from intracellular stores. Promotes Lyn-mediated phosphorylation of IP3 receptors 1 and 2.

**Summary**, from NCBI Gene [55024](https://www.ncbi.nlm.nih.gov/gene/55024):

> The protein encoded by this gene is a B-cell-specific scaffold protein that functions in B-cell receptor-induced calcium mobilization from intracellular stores. This protein can also promote Lyn-mediated tyrosine phosphorylation of inositol 1,4,5-trisphosphate receptors. Polymorphisms in this gene are associated with susceptibility to systemic lupus erythematosus. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:18233](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18233) · Entrez [55024](https://www.ncbi.nlm.nih.gov/gene/55024) · UniProt [Q8NDB2](https://www.uniprot.org/uniprotkb/Q8NDB2) · Ensembl [ENSG00000153064](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153064)

## Data

Gene col 7685: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7685); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7685, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7685]; `tensor/DDL_lfc|DDL_z.npy` [7685]; `embed/gene_vectors.npy` [7685]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7685 or target_col == 7685). Every well: [[BANK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BANK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
