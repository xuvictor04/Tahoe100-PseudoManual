---
symbol: "ATP6V1E1"
type: "gene"
col: 5171
ensembl_id: "ENSG00000131100"
name: "ATPase H+ transporting V1 subunit E1"
location: "22q11.21"
module: 118
arm: "+"
pooled_cpm: 55.24
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# ATP6V1E1

*ATPase H+ transporting V1 subunit E1* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.92× (z +16.3, q 0e+00, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (NCI-H661 0.0809×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6V1G1]] (+0.74, fdr 7e-06), [[EMC3]] (+0.67, fdr 7e-06), [[PIN4]] (+0.67, fdr 7e-06); moves opposite to [[CEP83]] (-0.57, fdr 3e-05), [[H2AX]] (-0.56, fdr 1e-05), [[PPAT]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5171.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +16.3 | 0e+00 | 46/48 (LS 180, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.29×** | +14.6 | 1e-45 | 42/47 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +11.6 | 7e-29 | 35/40 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +10.9 | 2e-25 | 42/48 (LoVo, SNU-423, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +9.3 | 1e-18 | 40/49 (HEC-1-A, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +9.1 | 8e-18 | 45/48 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +8.8 | 2e-16 | 39/48 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.58×** | +8.7 | 2e-16 | 37/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +8.1 | 3e-14 | 37/48 (SW1417, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +8.1 | 5e-14 | 34/44 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.61×** | +7.6 | 2e-12 | 33/48 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +6.9 | 3e-10 | 36/48 (HOP62, NCI-H1573, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +6.7 | 9e-10 | 31/48 (J82, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.44×** | +6.4 | 6e-09 | 37/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +5.8 | 2e-07 | 30/48 (LS 180, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +4.5 | 2e-04 | 24/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.001 | 25/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.001 | 23/48 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.005 | 22/48 (A549, A-427, …) | rises with dose | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (NCI-H661 0.0809×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5171. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 39.0 | 7 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +15.1) | — |
| [[SW480 (line)]] | alt | 49.7 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +14.6) | — |
| [[A498 (line)]] | wt | 84.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 32.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +8.9) | — |
| [[J82 (line)]] | alt | 52.8 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 57.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 45.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +10.3) | — |
| [[A549 (line)]] | wt | 31.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.68× (z +10.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 99.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 80.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +12.4) | — |
| [[LoVo (line)]] | wt | 46.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.10× (z +12.1) | — |
| [[NCI-H1792 (line)]] | alt | 38.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 84.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +13.4) | — |
| [[NCI-H460 (line)]] | wt | 42.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +12.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 45.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 81.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.37× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 97.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +10.7) | — |
| [[A-172 (line)]] | wt | 41.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +8.7) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 54.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 43.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.4) | — |
| [[C32 (line)]] | wt | 53.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +10.2) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 45.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +10.5) | — |
| [[H4 (line)]] | wt | 30.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 50.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +8.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 76.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +11.1) | — |
| [[LS 180 (line)]] | wt | 57.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +16.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 77.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +15.6) | — |
| [[NCI-H1573 (line)]] | alt | 58.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.41× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 54.7 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0809× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 105 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +14.5) | — |
| [[SHP-77 (line)]] | alt | 58.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.89× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 45.8 | 1 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 54.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +11.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5171), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1G1]] | +0.74 | +0.65 / +0.77 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[EMC3]] | +0.67 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[PIN4]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[TMUB2]] | +0.65 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[ARPC3]] | +0.60 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[GPALPP1]] | +0.60 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[C9orf85]] | +0.60 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[ING4]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[PRPF18]] | +0.59 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[ATP6V1H]] | +0.58 | +0.49 / +0.53 | both halves | 1e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[HEXA]] | +0.58 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[ZBTB8OS]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP83]] | -0.57 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[H2AX]] | -0.56 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[PPAT]] | -0.55 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[DNMT1]] | -0.54 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[THEM6]] | -0.54 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[SRSF7]] | -0.54 | -0.36 / -0.65 | both halves | 1e-04 |  |
| [[SRSF2]] | -0.54 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[SCML2]] | -0.53 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[TERT]] | -0.53 | -0.39 / -0.53 | both halves | 5e-05 | pathway: MITF-M-dependent gene expression |
| [[CDCA7]] | -0.52 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[CDC7]] | -0.52 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[NCAPH]] | -0.51 | -0.33 / -0.56 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ATP6V1E1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TERT]] | B | TERT activity lowers ATP6V1E1's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.36× higher at baseline in the lines without TERT | 0.080 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.623). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-27.4, -10.1); signed map (-2.9, -4.7). **Vector** length 91.0, 24.0% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.1 | +8.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.2 | +7.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.1 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +10.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.3 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +8.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +0.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.9 | +1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.6 | +6.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -1.1 |
|  | [[AZD1390 (drug)]] 0.05 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting V1 subunit E1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:17,592,136-17,628,749 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P31, Vma4, ATP6E2; previously ATP6E, ATP6V1E |
| Gene groups (HGNC) | V-type ATPase subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 16 pathways, smallest: Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy; Insulin receptor recycling; ROS and RNS production in phagocytes |
| Matched by | ensembl_id |

**Function**, from UniProt [P36543](https://www.uniprot.org/uniprotkb/P36543) (V-type proton ATPase subunit E 1):

> Subunit of the V1 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons. V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments and in some cell types, is targeted to the plasma membrane, where it promotes acidification of the extracellular environment. The V-ATPase complex also acts as an activator for mTORC1 on lysosomal …

**Summary**, from NCBI Gene [529](https://www.ncbi.nlm.nih.gov/gene/529):

> This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of eukaryotic intracellular organelles. V-ATPase dependent organelle acidification is necessary for such intracellular processes as protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. V-ATPase is composed of a cytosolic V1 domain and a transmembrane V0 domain. The V1 domain consists of three A, three B, and two G …

**Accessions** — [HGNC:857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:857) · Entrez [529](https://www.ncbi.nlm.nih.gov/gene/529) · UniProt [P36543](https://www.uniprot.org/uniprotkb/P36543) · Ensembl [ENSG00000131100](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131100)

## Data

Gene col 5171: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5171); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5171, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5171]; `tensor/DDL_lfc|DDL_z.npy` [5171]; `embed/gene_vectors.npy` [5171]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5171 or target_col == 5171). Every well: [[ATP6V1E1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6V1E1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
