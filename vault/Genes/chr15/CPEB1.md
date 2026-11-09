---
symbol: "CPEB1"
type: "gene"
col: 13209
ensembl_id: "ENSG00000214575"
name: "cytoplasmic polyadenylation element binding protein 1"
location: "15q25.2"
module: 125
arm: "+"
pooled_cpm: 7.53
n_lines_expressing: 26
n_dd_up: 37
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 9
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# CPEB1

*cytoplasmic polyadenylation element binding protein 1* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.10× (z +32.3, q 0e+00, up in 20 of 22 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (NCI-H23 0.0780×, A-427 0.253×; ⚠ cell-cycle shift, explains ~81% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RPMI-7951 0.0872×, PANC-1 0.327×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (PANC-1 0.362×, NCI-H23 0.361×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (J82 0.0637×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.306×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02154]] (+0.66, fdr 1e-05), [[RNLS]] (+0.66, fdr 1e-05), [[SYT14]] (+0.65, fdr 7e-06); moves opposite to [[MLEC]] (-0.61, fdr 1e-05), [[POGLUT2]] (-0.61, fdr 5e-05), [[ATP6AP2]] (-0.58, fdr 2e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ZSCAN12]] → it (grade B ⚠); 9 go from it, the strongest it → [[TRAPPC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13209.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.10×** | +32.3 | 0e+00 | 20/22 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.49×** | +22.4 | 0e+00 | 7/22 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.55×** | +16.0 | 0e+00 | 16/22 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.12×** | +13.8 | 2e-41 | 4/11 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.48×** | +11.0 | 3e-26 | 14/22 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.27×** | +10.4 | 3e-23 | 13/22 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.38×** | +10.2 | 2e-22 | 2/13 (NCI-H460, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.16×** | +9.2 | 3e-18 | 18/22 (HOP62, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +9.1 | 5e-18 | 10/23 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.00×** | +8.7 | 1e-16 | 14/22 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.90×** | +8.1 | 2e-14 | 9/22 (NCI-H460, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +6.7 | 8e-10 | 1/17 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +6.5 | 3e-09 | 10/22 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +6.3 | 1e-08 | 13/23 (NCI-H460, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.54×** | +5.5 | 2e-06 | 11/22 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.80×** | +5.3 | 4e-06 | 1/19 (SNU-423) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.64×** | +4.5 | 3e-04 | 1/22 (HOP62) | all doses, flat | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.001 | 9/23 (RPMI-7951, H4, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13209.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (NCI-H23 0.0780×, A-427 0.253×; ⚠ cell-cycle shift, explains ~81% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RPMI-7951 0.0872×, PANC-1 0.327×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (PANC-1 0.362×, NCI-H23 0.361×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (J82 0.0637×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.306×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | 0.775× | -3.2 | 0.25 | 10/21 (RPMI-7951, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Lipoic acid (drug)]] 5 µM |  | 0.838× | -3.1 | 0.25 | 0/23 | rises with dose |  |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.779× | -3.1 | 0.25 | 1/22 (A498) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM |  | 0.770× | -3.1 | 0.25 | 3/21 (C-33 A, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13209. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.88 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.1× (z +20.3) | — |
| [[A-172 (line)]] | wt | 28.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +23.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.113× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 28.1 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -9.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 8.82 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +15.6) | — |
| [[NCI-H23 (line)]] | alt | 24.0 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0780× (z -16.8) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 18.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +24.7) | — |
| [[PANC-1 (line)]] | alt | 27.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -11.7) |
| [[H4 (line)]] | wt | 18.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.74× (z +12.4) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.123× (z -8.5) |
| [[J82 (line)]] | alt | 7.82 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +14.7) | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0637× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 41.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +14.1) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0872× (z -13.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 34.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +16.5) | — |
| [[A498 (line)]] | wt | 7.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +12.6) | — |
| [[C32 (line)]] | wt | 1.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 38.3× (z +10.9) | — |
| [[HS-578T (line)]] | alt | 5.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 7.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.18× (z +11.6) | — |
| [[A549 (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.925 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.804 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.830 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.576 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.727 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.661 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.831 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.554 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.884 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.851 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.645 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.643 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.736 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.667 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13209), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02154]] | +0.66 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[RNLS]] | +0.66 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[SYT14]] | +0.65 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[C12orf50]] | +0.63 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[PAPLN]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[TRIML2]] | +0.62 | +0.68 / +0.41 | both halves | 4e-05 |  |
| [[CLIC2]] | +0.61 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[SLC35F1]] | +0.60 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[KCNMB3]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[HDAC9]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[CRYM]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[PLD6]] | +0.60 | +0.53 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLEC]] | -0.61 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[POGLUT2]] | -0.61 | -0.63 / -0.40 | both halves | 5e-05 |  |
| [[ATP6AP2]] | -0.58 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[GLT8D1]] | -0.58 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[CHPF]] | -0.57 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[SMAP2]] | -0.57 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[SPICE1]] | -0.57 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[P3H1]] | -0.57 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[RPN2]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[GLG1]] | -0.56 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[TRAPPC1]] | -0.55 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[CRLS1]] | -0.53 | -0.60 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZSCAN12]] | B | ZSCAN12 activity raises CPEB1's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 2.33× lower at baseline in the lines without ZSCAN12 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |
| [[SNHG26]] | B | SNHG26 activity raises CPEB1's level | lines that do not express SNHG26 (11) vs lines expressing it (39) | 2.83× lower at baseline in the lines without SNHG26 | 0.089 | ⚠ within organs, on part of the lines; also absent: HEG1, GPR63, FAM171A1 |
| [[KIAA0408]] | C | KIAA0408 activity raises CPEB1's level | lines that do not express KIAA0408 (22) vs lines expressing it (28) | 3.87× lower at baseline in the lines without KIAA0408 | 0.042 | ⚠ within organs, on part of the lines; also absent: SOGA3, ENSG00000255330, RFTN1; co-absent with the target |
| [[ZNF382]] | C | ZNF382 activity raises CPEB1's level | lines that do not express ZNF382 (18) vs lines expressing it (32) | 3.27× lower at baseline in the lines without ZNF382 | 0.069 | ⚠ within organs, on part of the lines; also absent: AFF3, DZIP1, MMP16; co-absent with the target |
| [[ELFN1]] | C | ELFN1 activity raises CPEB1's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 2.88× lower at baseline in the lines without ELFN1 | 0.094 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRAPPC1]] | B | CPEB1 activity raises TRAPPC1's level | lines that do not express CPEB1 (24) vs lines expressing it (26) | 1.47× lower at baseline in the lines without CPEB1 | 0.032 | ⚠ within organs, on part of the lines; also absent: GLIS1, COLEC12, TUB |
| [[VPS35L]] | B | CPEB1 activity raises VPS35L's level | lines that do not express CPEB1 (24) vs lines expressing it (26) | 2.61× lower at baseline in the lines without CPEB1 | 0.039 | ⚠ within organs, on part of the lines; also absent: GLIS1, COLEC12, TUB |
| [[RTL8C]] | B | CPEB1 activity raises RTL8C's level | lines that do not express CPEB1 (24) vs lines expressing it (26) | 3.26× lower at baseline in the lines without CPEB1 | 0.060 | ⚠ within organs, on part of the lines; also absent: GLIS1, COLEC12, TUB |
| [[GLT8D1]] | B | CPEB1 activity raises GLT8D1's level | lines that do not express CPEB1 (24) vs lines expressing it (26) | 1.62× lower at baseline in the lines without CPEB1 | 0.063 | ⚠ within organs, on part of the lines; also absent: GLIS1, COLEC12, TUB |
| [[P3H1]] | B | CPEB1 activity raises P3H1's level | lines that do not express CPEB1 (24) vs lines expressing it (26) | 2.25× lower at baseline in the lines without CPEB1 | 0.068 | ⚠ within organs, on part of the lines; also absent: GLIS1, COLEC12, TUB |
| [[TMED9]] | B | CPEB1 activity raises TMED9's level | lines that do not express CPEB1 (24) vs lines expressing it (26) | 1.33× lower at baseline in the lines without CPEB1 | 0.075 | ⚠ within organs, on part of the lines; also absent: GLIS1, COLEC12, TUB |
| [[SNHG26]] | B | CPEB1 activity raises SNHG26's level | lines that do not express CPEB1 (24) vs lines expressing it (26) | 2.19× lower at baseline in the lines without CPEB1 | 0.080 | ⚠ within organs, on part of the lines; also absent: GLIS1, COLEC12, TUB |
| [[LINC00882]] | C | CPEB1 activity raises LINC00882's level | lines that do not express CPEB1 (24) vs lines expressing it (26) | 3.96× lower at baseline in the lines without CPEB1 | 0.045 | ⚠ within organs, on part of the lines; also absent: GLIS1, COLEC12, TUB; co-absent with the target |
| [[ZNF829]] | C | CPEB1 activity raises ZNF829's level | lines that do not express CPEB1 (24) vs lines expressing it (26) | 2.98× lower at baseline in the lines without CPEB1 | 0.047 | ⚠ within organs, on part of the lines; also absent: GLIS1, COLEC12, TUB; co-absent with the target |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.9, 22.7); signed map (39.0, 20.3). **Vector** length 70.3, 19.3% of its response variance represented; |z| ≥ 3 in 564 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +13.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +32.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +10.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +16.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +8.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +5.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -2.2 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | +0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -2.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | +0.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.5 | -0.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | cytoplasmic polyadenylation element binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.2 — chr15:82,543,201-82,648,861 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13203, CPEB |
| Reactome | 2 pathways, smallest: M-decay: degradation of maternal mRNAs by maternally stored factors; Maternal to zygotic transition (MZT) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZB8](https://www.uniprot.org/uniprotkb/Q9BZB8) (Cytoplasmic polyadenylation element-binding protein 1):

> Sequence-specific RNA-binding protein that regulates mRNA cytoplasmic polyadenylation and translation initiation during oocyte maturation, early development and at postsynapse sites of neurons. Binds to the cytoplasmic polyadenylation element (CPE), an uridine-rich sequence element (consensus sequence 5'-UUUUUAU-3') within the mRNA 3'-UTR. RNA binding results in a clear conformational change analogous to the Venus fly trap mechanism. In absence of phosphorylation and in association with TACC3 …

**Summary**, from NCBI Gene [64506](https://www.ncbi.nlm.nih.gov/gene/64506):

> This gene encodes a member of the cytoplasmic polyadenylation element binding protein family. This highly conserved protein binds to a specific RNA sequence, called the cytoplasmic polyadenylation element, found in the 3' untranslated region of some mRNAs. The encoded protein functions in both the cytoplasm and the nucleus. It is involved in the regulation of mRNA translation, as well as processing of the 3' untranslated region, and may play a role in cell proliferation and tumorigenesis. …

**Accessions** — [HGNC:21744](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21744) · Entrez [64506](https://www.ncbi.nlm.nih.gov/gene/64506) · UniProt [Q9BZB8](https://www.uniprot.org/uniprotkb/Q9BZB8) · Ensembl [ENSG00000214575](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214575)

## Data

Gene col 13209: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13209); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13209, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13209]; `tensor/DDL_lfc|DDL_z.npy` [13209]; `embed/gene_vectors.npy` [13209]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13209 or target_col == 13209). Every well: [[CPEB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPEB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
