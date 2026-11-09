---
symbol: "CAVIN2"
type: "gene"
col: 9662
ensembl_id: "ENSG00000168497"
name: "caveolae associated protein 2"
location: "2q32.3"
module: 217
arm: "+"
pooled_cpm: 7.99
n_lines_expressing: 18
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/217"]
generated_by: "tahoemap"
---

# CAVIN2

*caveolae associated protein 2* — 2q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.14× (z +10.3, q 3e-22, up in 9 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 3.11× (z +7.2, q 2e-10, up in 9 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.433× (z -5.3, q 8e-05, down in 12 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 2 lines (SNU-1 0.0618×, NCI-H460 0.0757×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.0943×, Hs 766T 0.218×; ⚠ cell-cycle shift, would explain all of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (NCI-H460 0.0752×, SNU-1 0.156×); [[Panobinostat (drug)]] 5 µM in 2 lines (SNU-1 0.191×, SW480 0.150×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAVIN2-AS1]] (+0.66, fdr 7e-06, ⚠ same locus), [[JPH2]] (+0.62, fdr 8e-06), [[ADGRG2]] (+0.61, fdr 1e-05), [[SLC7A2]] (+0.58, fdr 1e-05); moves opposite to [[WNT9A]] (-0.62, fdr 1e-05), [[ASPHD1]] (-0.55, fdr 2e-05), [[LINC01705]] (-0.53, fdr 1e-05).
> It is in [[Module 217]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PSTPIP2]] → it (grade B ⚠); 6 go from it, the strongest it → [[PSTPIP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9662.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.14×** | +10.3 | 3e-22 | 9/14 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.00×** | +8.4 | 1e-14 | 4/8 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **3.11×** | +7.2 | 2e-10 | 9/15 (NCI-H460, A549, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.85×** | +6.1 | 1e-07 | 4/10 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Budesonide (drug)]] 0.5 µM |  | **2.34×** | +5.4 | 1e-05 | 7/15 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **2.23×** | +5.1 | 4e-05 | 7/15 (NCI-H460, Hs 766T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.21×** | +4.8 | 1e-04 | 9/15 (NCI-H460, Hs 766T, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.71×** | +4.8 | 1e-04 | 12/15 (SNU-1, J82, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **2.06×** | +4.6 | 3e-04 | 6/15 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.00×** | +4.4 | 7e-04 | 9/15 (NCI-H460, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.95×** | +3.9 | 0.005 | 10/15 (NCI-H460, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.73×** | +3.5 | 0.025 | 8/15 (NCI-H460, Hs 766T, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +3.4 | 0.029 | 7/16 (NCI-H460, Hs 766T, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.74×** | +3.3 | 0.037 | 8/15 (J82, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.080 | 8/15 (Hs 766T, A549, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.62×** | +3.0 | 0.084 | 8/15 (NCI-H460, NCI-H2030, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9662.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 2 lines (SNU-1 0.0618×, NCI-H460 0.0757×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.0943×, Hs 766T 0.218×; ⚠ cell-cycle shift, would explain all of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (NCI-H460 0.0752×, SNU-1 0.156×); [[Panobinostat (drug)]] 5 µM in 2 lines (SNU-1 0.191×, SW480 0.150×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.433×** | -5.3 | 8e-05 | 12/15 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.566×** | -3.6 | 0.096 | 5/14 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.577× | -3.5 | 0.10 | 7/15 (SNU-1, J82, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.582× | -3.2 | 0.23 | 0/16 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9662. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.0 | 5 | 9 (6 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 8.51× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.0943× (z -14.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0752× (z -11.5) |
| [[SNU-1 (line)]] | wt | 137 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -17.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0618× (z -16.2) |
| [[SW480 (line)]] | alt | 11.0 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0763× (z -12.4) |
| [[A-172 (line)]] | wt | 6.79 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 33.0× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 24.5 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.101× (z -8.7) ⚠ cell-cycle shift, explains ~45% of this change |
| [[Hs 766T (line)]] | wt | 58.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 33.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.118× (z -8.7) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A-427 (line)]] | wt | 0.629 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.650 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.685 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.760 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.751 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.825 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.857 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.921 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.706 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.696 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.841 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.661 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.842 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.715 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.726 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.942 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.893 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9662), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAVIN2-AS1]] | +0.66 | +0.71 / +0.60 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[JPH2]] | +0.62 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[ADGRG2]] | +0.61 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[SLC7A2]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SRGN]] | +0.57 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[MAOA]] | +0.57 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[KCNG2]] | +0.56 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[SLC15A5]] | +0.54 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[MAP3K1]] | +0.53 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[YAP1]] | +0.53 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[NFIA]] | +0.53 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[POLR3GL]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[TGFBR2]] | +0.52 | +0.50 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WNT9A]] | -0.62 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[ASPHD1]] | -0.55 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[LINC01705]] | -0.53 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[CELSR1]] | -0.53 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[PPP2R3A]] | -0.52 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[KCNMA1]] | -0.51 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[LTBP4]] | -0.50 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[RABGEF1]] | -0.50 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[PTHLH]] | -0.49 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[GDI1]] | -0.48 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[GPR161]] | -0.48 | -0.36 / -0.59 | both halves | 1e-04 |  |
| [[MMP1]] | -0.46 | -0.45 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSTPIP2]] | B | PSTPIP2 activity raises CAVIN2's level | lines that do not express PSTPIP2 (20) vs lines expressing it (30) | 1.64× lower at baseline in the lines without PSTPIP2 | 0.059 | ⚠ within organs, on part of the lines; also absent: NEDD9, CARD11, BCAT1 |
| [[CAVIN2-AS1]] | C | CAVIN2-AS1 activity raises CAVIN2's level | lines that do not express CAVIN2-AS1 (31) vs lines expressing it (19) | 5.11× lower at baseline in the lines without CAVIN2-AS1 | 1e-04 | ⚠ within organs, on part of the lines; also absent: CAVIN2, NLGN4Y, LINC02154; co-absent with the target |
| [[PAX7]] | C | PAX7 activity raises CAVIN2's level | lines that do not express PAX7 (35) vs lines expressing it (15) | 1.57× lower at baseline in the lines without PAX7 | 0.098 | ⚠ within organs, on part of the lines; also absent: LINC00408, ENSG00000289605, SLC15A5; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSTPIP2]] | B | CAVIN2 activity raises PSTPIP2's level | lines that do not express CAVIN2 (32) vs lines expressing it (18) | 1.75× lower at baseline in the lines without CAVIN2 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CAVIN2-AS1, NLGN4Y, PSG9 |
| [[ADGRG2]] | B | CAVIN2 activity raises ADGRG2's level | lines that do not express CAVIN2 (32) vs lines expressing it (18) | 1.46× lower at baseline in the lines without CAVIN2 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CAVIN2-AS1, NLGN4Y, PSG9 |
| [[TIGD2]] | B | CAVIN2 activity lowers TIGD2's level | lines that do not express CAVIN2 (32) vs lines expressing it (18) | 1.23× higher at baseline in the lines without CAVIN2 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CAVIN2-AS1, NLGN4Y, PSG9 |
| [[TGFBR3]] | B | CAVIN2 activity raises TGFBR3's level | lines that do not express CAVIN2 (32) vs lines expressing it (18) | 1.58× lower at baseline in the lines without CAVIN2 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CAVIN2-AS1, NLGN4Y, PSG9 |
| [[CAVIN2-AS1]] | C | CAVIN2 activity raises CAVIN2-AS1's level | lines that do not express CAVIN2 (32) vs lines expressing it (18) | 6.14× lower at baseline in the lines without CAVIN2 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CAVIN2-AS1, NLGN4Y, PSG9; co-absent with the target |
| [[SRGN]] | C | CAVIN2 activity raises SRGN's level | lines that do not express CAVIN2 (32) vs lines expressing it (18) | 3.37× lower at baseline in the lines without CAVIN2 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CAVIN2-AS1, NLGN4Y, PSG9; co-absent with the target |

## Where it sits

- **Module**: [[Module 217]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.743). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.4, 18.0); signed map (18.3, 30.9). **Vector** length 63.1, 19.5% of its response variance represented; |z| ≥ 3 in 544 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +4.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +1.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +8.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.3 | +4.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.2 | +7.2 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.2 | +4.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.1 | +5.4 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -3.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | caveolae associated protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.3 — chr2:191,834,310-191,847,088 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SDR, PS-p68, cavin-2; previously SDPR |
| Gene groups (HGNC) | Cavins |
| Hallmark sets | ADIPOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [O95810](https://www.uniprot.org/uniprotkb/O95810) (Caveolae-associated protein 2):

> Plays an important role in caveolar biogenesis and morphology. Regulates caveolae morphology by inducing membrane curvature within caveolae. Plays a role in caveola formation in a tissue-specific manner. Required for the formation of caveolae in the lung and fat endothelia but not in the heart endothelia. Negatively regulates the size or stability of CAVIN complexes in the lung endothelial cells. May play a role in targeting PRKCA to caveolae (By similarity).

**Summary**, from NCBI Gene [8436](https://www.ncbi.nlm.nih.gov/gene/8436):

> This gene encodes a calcium-independent phospholipid-binding protein whose expression increases in serum-starved cells. This protein is a substrate for protein kinase C (PKC) phosphorylation and recruits polymerase I and transcript release factor (PTRF) to caveolae. Removal of this protein causes caveolae loss and its over-expression results in caveolae deformation and membrane tubulation.[provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:10690](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10690) · Entrez [8436](https://www.ncbi.nlm.nih.gov/gene/8436) · UniProt [O95810](https://www.uniprot.org/uniprotkb/O95810) · Ensembl [ENSG00000168497](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168497)

## Data

Gene col 9662: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9662); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9662, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9662]; `tensor/DDL_lfc|DDL_z.npy` [9662]; `embed/gene_vectors.npy` [9662]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9662 or target_col == 9662). Every well: [[CAVIN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAVIN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
