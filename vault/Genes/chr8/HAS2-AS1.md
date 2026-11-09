---
symbol: "HAS2-AS1"
type: "gene"
col: 14562
ensembl_id: "ENSG00000248690"
name: "HAS2 antisense RNA 1"
location: "8q24.13"
module: 26
arm: "+"
pooled_cpm: 10.64
n_lines_expressing: 40
n_dd_up: 14
n_dd_down: 15
n_dd_up_clean: 10
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# HAS2-AS1

*HAS2 antisense RNA 1* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.75× (z +27.5, q 0e+00, up in 30 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.627× (z -5.8, q 4e-06, down in 21 of 36 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01135]] (+0.71, fdr 7e-06), [[OBI1-AS1]] (+0.68, fdr 1e-05), [[DKK2]] (+0.67, fdr 1e-05); moves opposite to [[MTMR12]] (-0.56, fdr 3e-05), [[NAA40]] (-0.55, fdr 7e-05), [[WRAP73]] (-0.55, fdr 3e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[LINC00310]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14562.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.75×** | +27.5 | 0e+00 | 30/34 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.46×** | +15.5 | 0e+00 | 27/35 (NCI-H2347, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +12.8 | 4e-35 | 7/15 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.45×** | +11.2 | 7e-27 | 25/36 (NCI-H2347, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.24×** | +10.1 | 1e-21 | 10/24 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.70×** | +9.4 | 6e-19 | 23/37 (NCI-H2030, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +8.7 | 2e-16 | 14/34 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +8.3 | 6e-15 | 19/37 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +8.2 | 2e-14 | 19/32 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +6.9 | 4e-10 | 8/18 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +6.6 | 2e-09 | 18/35 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +5.5 | 1e-06 | 20/36 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +5.5 | 2e-06 | 12/33 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.30×** | +3.3 | 0.037 | 3/33 (J82, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14562.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.627×** | -5.8 | 4e-06 | 21/36 (HS-578T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.645×** | -5.4 | 1e-05 | 19/37 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.753×** | -5.0 | 1e-04 | 13/37 (C32, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.678×** | -4.8 | 2e-04 | 17/35 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.682×** | -4.7 | 2e-04 | 13/36 (C32, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.490×** | -4.6 | 3e-04 | 14/33 (C32, NCI-H1792, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.694×** | -4.5 | 5e-04 | 17/35 (C32, SW480, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.697×** | -4.5 | 5e-04 | 17/35 (C32, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.730×** | -3.9 | 0.006 | 16/36 (C32, HS-578T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.736×** | -3.8 | 0.008 | 13/35 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.736×** | -3.8 | 0.008 | 12/36 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.735×** | -3.5 | 0.021 | 7/36 (COLO 205, AsPC-1, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.588×** | -3.4 | 0.024 | 9/29 (C32, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.762×** | -3.4 | 0.031 | 10/36 (C32, SW480, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.763×** | -3.3 | 0.031 | 14/34 (COLO 205, C32, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14562. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 145 | 0 | 25 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0671× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.172× (z -17.2) |
| [[SW480 (line)]] | alt | 21.7 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 9.41 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +17.9) | — |
| [[HS-578T (line)]] | alt | 39.1 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +11.0) | [[Belinostat (drug)]] 5 µM 0.170× (z -10.0) |
| [[COLO 205 (line)]] | alt | 18.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 17.7× (z +16.2) | [[Digitoxin (drug)]] 5 µM 0.0908× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1792 (line)]] | alt | 22.5 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.114× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.202× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 11.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.55× (z +12.4) | — |
| [[A-172 (line)]] | wt | 4.70 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.53× (z +8.8) | [[Almonertinib (mesylate) (drug)]] 0.05 µM 0.0756× (z -8.6) |
| [[A549 (line)]] | wt | 5.51 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +9.3) | [[Naproxen (drug)]] 0.05 µM 0.0931× (z -8.9) |
| [[HOP62 (line)]] | alt | 12.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 4.22 | 2 | 0 | [[Auranofin (drug)]] 5 µM 50.0× (z +13.3) | — |
| [[LOX-IMVI (line)]] | wt | 13.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.27× (z +13.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.109× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~51% of this change |
| [[NCI-H23 (line)]] | alt | 12.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.63× (z +14.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0718× (z -12.5) ⚠ toxic; cell-cycle shift, explains ~64% of this change |
| [[NCI-H2347 (line)]] | alt | 3.74 | 2 | 0 | [[Auranofin (drug)]] 5 µM 33.4× (z +15.6) | — |
| [[AsPC-1 (line)]] | alt | 4.08 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM 0.0634× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 6.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.99× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 18.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0632× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[J82 (line)]] | alt | 2.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.95× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 7.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +12.5) | — |
| [[RKO (line)]] | wt | 5.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 4.13 | 1 | 0 | [[Auranofin (drug)]] 5 µM 24.2× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.84× (z +11.2) | — |
| [[A-427 (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14562), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01135]] | +0.71 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[OBI1-AS1]] | +0.68 | +0.57 / +0.58 | both halves | 1e-05 | same gene group |
| [[DKK2]] | +0.67 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[UBA6-DT]] | +0.66 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[HPSE2]] | +0.66 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[LHFPL3]] | +0.66 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ZEB1-AS1]] | +0.66 | +0.61 / +0.49 | both halves | 1e-05 | same gene group |
| [[GRM8]] | +0.65 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[LRP2BP]] | +0.65 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[CD96]] | +0.65 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[PELO-AS1]] | +0.65 | +0.50 / +0.62 | both halves | 1e-05 | same gene group |
| [[CFAP418-AS1]] | +0.64 | +0.57 / +0.54 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTMR12]] | -0.56 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[NAA40]] | -0.55 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[WRAP73]] | -0.55 | -0.40 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HAS2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAGI2]] | B | MAGI2 activity raises HAS2-AS1's level | lines that do not express MAGI2 (30) vs lines expressing it (20) | 2.13× lower at baseline in the lines without MAGI2 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGI2-AS3, MMP2, PHACTR1 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00310]] | B | HAS2-AS1 activity raises LINC00310's level | lines that do not express HAS2-AS1 (10) vs lines expressing it (40) | 1.92× lower at baseline in the lines without HAS2-AS1 | 0.040 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[DIRC3]] | B | HAS2-AS1 activity raises DIRC3's level | lines that do not express HAS2-AS1 (10) vs lines expressing it (40) | 2.83× lower at baseline in the lines without HAS2-AS1 | 0.090 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MAGI2]] | B | HAS2-AS1 activity raises MAGI2's level | lines that do not express HAS2-AS1 (10) vs lines expressing it (40) | 4.13× lower at baseline in the lines without HAS2-AS1 | 0.099 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.9, 14.8); signed map (27.3, 2.1). **Vector** length 82.3, 17.0% of its response variance represented; |z| ≥ 3 in 914 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.2 | +27.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.1 | +15.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +12.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +8.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.4 | +1.6 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.1 | -5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.8 | -3.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -2.8 | -3.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.3 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -4.5 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | HAS2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q24.13 — chr8:121,639,293-121,994,185 (+) |
| Ensembl biotype | lncRNA |
| Also known as | HASNT, NCRNA00077; previously HAS2AS, HAS2-AS |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:34340](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34340) · Entrez [594842](https://www.ncbi.nlm.nih.gov/gene/594842) · Ensembl [ENSG00000248690](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248690)

## Data

Gene col 14562: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14562); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14562, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14562]; `tensor/DDL_lfc|DDL_z.npy` [14562]; `embed/gene_vectors.npy` [14562]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14562 or target_col == 14562). Every well: [[HAS2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAS2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
