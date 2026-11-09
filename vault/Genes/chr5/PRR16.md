---
symbol: "PRR16"
type: "gene"
col: 11580
ensembl_id: "ENSG00000184838"
name: "proline rich 16"
location: "5q23.1"
module: 13
arm: "+"
pooled_cpm: 51.99
n_lines_expressing: 26
n_dd_up: 4
n_dd_down: 50
n_dd_up_clean: 4
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 14
direction_downstream: 25
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# PRR16

*proline rich 16* — 5q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.77× (z +7.2, q 3e-10, up in 11 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 50 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.466× (z -13.6, q 2e-39, down in 19 of 24 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.558× (z -10.4, q 2e-23, down in 18 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRB3]] (+0.67, fdr 7e-06), [[PTGFR]] (+0.64, fdr 1e-05), [[ADAMTS2]] (+0.62, fdr 1e-05); moves opposite to [[PATJ]] (-0.50, fdr 4e-05), [[AP1G2]] (-0.47, fdr 5e-05), [[SPATA6L]] (-0.45, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[LPAR5]] → it (grade B ⚠); 25 go from it, the strongest it → [[CACNA1C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11580.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +7.2 | 3e-10 | 11/24 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +5.0 | 1e-04 | 12/24 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.12×** | +5.0 | 1e-04 | 12/24 (NCI-H2347, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.8 | 2e-04 | 10/24 (SK-MEL-2, C32, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | 1.27× | +3.1 | 0.22 | 9/23 (NCI-H2347, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 50 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11580.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.466×** | -13.6 | 2e-39 | 19/24 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.342×** | -12.5 | 1e-33 | 17/21 (NCI-H1792, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.397×** | -11.6 | 1e-28 | 19/22 (SNU-423, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.416×** | -10.6 | 3e-24 | 18/21 (NCI-H1792, A-172, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.558×** | -10.4 | 2e-23 | 18/24 (NCI-H1792, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.449×** | -10.1 | 5e-22 | 21/24 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.470×** | -9.5 | 1e-19 | 21/24 (C32, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.457×** | -9.3 | 8e-19 | 19/24 (NCI-H2030, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.482×** | -9.2 | 2e-18 | 18/24 (NCI-H1792, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.493×** | -8.9 | 4e-17 | 16/24 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.497×** | -8.5 | 1e-15 | 18/23 (NCI-H2030, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.519×** | -8.3 | 6e-15 | 18/24 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.525×** | -8.1 | 2e-14 | 16/24 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.559×** | -7.3 | 9e-12 | 20/24 (HS-578T, NCI-H1792, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **0.570×** | -7.1 | 5e-11 | 19/23 (NCI-H2030, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.422×** | -5.7 | 4e-07 | 14/24 (CHP-212, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.452×** | -5.2 | 4e-06 | 15/23 (NCI-H1792, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.453×** | -5.2 | 4e-06 | 15/24 (NCI-H1792, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.670×** | -5.0 | 1e-05 | 14/24 (SW 1271, hTERT-HPNE, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.757×** | -4.9 | 2e-05 | 16/24 (NCI-H1792, SNU-423, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.682×** | -4.8 | 3e-05 | 13/23 (J82, LOX-IMVI, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -4.7 | 5e-05 | 14/24 (A-427, SNU-423, …) | top dose only | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11580. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 272 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -31.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.225× (z -15.2) |
| [[NCI-H2030 (line)]] | alt | 273 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -19.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -14.2) |
| [[SNU-423 (line)]] | alt | 257 | 0 | 11 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -13.0) |
| [[HS-578T (line)]] | alt | 237 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -17.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.257× (z -13.2) |
| [[hTERT-HPNE (line)]] | wt | 274 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -16.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -11.8) |
| [[J82 (line)]] | alt | 78.5 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.312× (z -13.2) |
| [[A-172 (line)]] | wt | 47.0 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0671× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.196× (z -10.8) |
| [[A-427 (line)]] | wt | 320 | 0 | 6 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -13.1) |
| [[H4 (line)]] | wt | 74.0 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0587× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -10.0) |
| [[HOP62 (line)]] | alt | 52.9 | 0 | 5 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.191× (z -11.5) |
| [[C32 (line)]] | wt | 59.5 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.141× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 71.5 | 4 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.24× (z +9.4) | — |
| [[SW 1271 (line)]] | alt | 266 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0402× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0510× (z -12.9) |
| [[RPMI-7951 (line)]] | alt | 55.5 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.223× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 42.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.257× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 29.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.05 µM 4.05× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.209× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H661 (line)]] | alt | 271 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -13.5) |
| [[CHP-212 (line)]] | wt | 73.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -9.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.84 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.09 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.74 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.95 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.22 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.18 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.84 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.41 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.02 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.13 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.03 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11580), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRB3]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[PTGFR]] | +0.64 | +0.53 / +0.72 | both halves | 1e-05 | **novel candidate** |
| [[ADAMTS2]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[GLIS1]] | +0.62 | +0.58 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[SLC8A1]] | +0.62 | +0.52 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[CCDC102B]] | +0.59 | +0.51 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[LOX]] | +0.58 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[CARMN]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[KCTD16]] | +0.57 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[PCBP3]] | +0.57 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[PDGFRB]] | +0.54 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[RARB]] | +0.54 | +0.41 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATJ]] | -0.50 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[AP1G2]] | -0.47 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[SPATA6L]] | -0.45 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[KLHL2P1]] | -0.45 | -0.42 / -0.37 | both halves | 7e-05 |  |
| [[NEIL1]] | -0.45 | -0.47 / -0.23 | both halves | 5e-04 |  |
| [[PDCD6P1]] | -0.44 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[PRR15-DT]] | -0.43 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[LPAR5]] | -0.43 | -0.35 / -0.28 | both halves | 3e-04 |  |
| [[ACTR3C]] | -0.42 | -0.40 / -0.26 | both halves | 4e-04 |  |
| [[FAM83F]] | -0.42 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[DMTN]] | -0.42 | -0.29 / -0.39 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 5, C 9. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LPAR5]] | B | LPAR5 activity lowers PRR16's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 5.33× higher at baseline in the lines without LPAR5 | 0.027 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers PRR16's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[DMTN]] | B | DMTN activity lowers PRR16's level | lines that do not express DMTN (14) vs lines expressing it (36) | 4.25× higher at baseline in the lines without DMTN | 0.053 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[PRR15-DT]] | B | PRR15-DT activity lowers PRR16's level | lines that do not express PRR15-DT (25) vs lines expressing it (25) | 4.80× higher at baseline in the lines without PRR15-DT | 0.065 | ⚠ within organs, on part of the lines; also absent: PRR15, FAM110C, PLEKHG6; maybe low, not absent |
| [[GAL]] | B | GAL activity lowers PRR16's level | lines that do not express GAL (27) vs lines expressing it (23) | 2.08× higher at baseline in the lines without GAL | 0.083 | ⚠ within organs, on part of the lines; also absent: HEYL, ACP7, SEC14L4 |
| [[GLIS1]] | C | GLIS1 activity raises PRR16's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 7.41× lower at baseline in the lines without GLIS1 | 0.008 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent; co-absent with the target |
| [[TWIST1]] | C | TWIST1 activity raises PRR16's level | lines that do not express TWIST1 (26) vs lines expressing it (24) | 9.73× lower at baseline in the lines without TWIST1 | 0.011 | ⚠ within organs, on part of the lines; also absent: PCDH10, MDGA2, FAP; co-absent with the target |
| [[CCNYL2]] | C | CCNYL2 activity raises PRR16's level | lines that do not express CCNYL2 (29) vs lines expressing it (21) | 8.31× lower at baseline in the lines without CCNYL2 | 0.015 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target |
| [[MME]] | C | MME activity raises PRR16's level | lines that do not express MME (30) vs lines expressing it (20) | 6.93× lower at baseline in the lines without MME | 0.028 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC; co-absent with the target |
| [[KC6]] | C | KC6 activity raises PRR16's level | lines that do not express KC6 (32) vs lines expressing it (18) | 8.37× lower at baseline in the lines without KC6 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1; co-absent with the target |
| [[FBN1]] | C | FBN1 activity raises PRR16's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 4.93× lower at baseline in the lines without FBN1 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241; co-absent with the target |
| [[ADAMTS2]] | C | ADAMTS2 activity raises PRR16's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 5.92× lower at baseline in the lines without ADAMTS2 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 6, C 19. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA1C]] | B | PRR16 activity raises CACNA1C's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 2.81× lower at baseline in the lines without PRR16 | 0.016 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2 |
| [[PATJ]] | B | PRR16 activity lowers PATJ's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 3.26× higher at baseline in the lines without PRR16 | 0.028 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2 |
| [[SYTL3]] | B | PRR16 activity raises SYTL3's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 1.83× lower at baseline in the lines without PRR16 | 0.056 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2 |
| [[CCDC102B]] | B | PRR16 activity raises CCDC102B's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 3.12× lower at baseline in the lines without PRR16 | 0.069 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2 |
| [[SH3RF3]] | B | PRR16 activity raises SH3RF3's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 2.28× lower at baseline in the lines without PRR16 | 0.084 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2 |
| [[LTBP1]] | B | PRR16 activity raises LTBP1's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 2.21× lower at baseline in the lines without PRR16 | 0.092 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2 |
| [[GLIS1]] | C | PRR16 activity raises GLIS1's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 3.70× lower at baseline in the lines without PRR16 | 0.009 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2; co-absent with the target |
| [[LAYN]] | C | PRR16 activity raises LAYN's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 4.19× lower at baseline in the lines without PRR16 | 0.013 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2; co-absent with the target |
| [[GNB4]] | C | PRR16 activity raises GNB4's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 9.19× lower at baseline in the lines without PRR16 | 0.018 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2; co-absent with the target |
| [[PDGFRB]] | C | PRR16 activity raises PDGFRB's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 4.32× lower at baseline in the lines without PRR16 | 0.034 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2; co-absent with the target |
| [[MME]] | C | PRR16 activity raises MME's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 7.22× lower at baseline in the lines without PRR16 | 0.034 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2; co-absent with the target |
| [[FBN1]] | C | PRR16 activity raises FBN1's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 4.73× lower at baseline in the lines without PRR16 | 0.037 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.463). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.3, 20.7); signed map (27.8, 45.7). **Vector** length 97.0, 29.9% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.7 | +7.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +3.1 | -6.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.1 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | -5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | -3.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.0 | -0.1 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -4.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -3.1 | -2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.8 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -8.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.4 | -7.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | proline rich 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.1 — chr5:120,464,300-120,687,332 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DSC54 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q569H4](https://www.uniprot.org/uniprotkb/Q569H4) (Protein Largen):

> Regulator of cell size that promotes cell size increase independently of mTOR and Hippo signaling pathways. Acts by stimulating the translation of specific mRNAs, including those encoding proteins affecting mitochondrial functions. Increases mitochondrial mass and respiration.

**Summary**, from NCBI Gene [51334](https://www.ncbi.nlm.nih.gov/gene/51334):

> Involved in positive regulation of cell size and positive regulation of translation. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29654](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29654) · Entrez [51334](https://www.ncbi.nlm.nih.gov/gene/51334) · UniProt [Q569H4](https://www.uniprot.org/uniprotkb/Q569H4) · Ensembl [ENSG00000184838](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184838)

## Data

Gene col 11580: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11580); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11580, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11580]; `tensor/DDL_lfc|DDL_z.npy` [11580]; `embed/gene_vectors.npy` [11580]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11580 or target_col == 11580). Every well: [[PRR16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRR16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
