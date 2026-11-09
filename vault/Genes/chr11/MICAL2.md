---
symbol: "MICAL2"
type: "gene"
col: 5478
ensembl_id: "ENSG00000133816"
name: "microtubule associated monooxygenase, calponin and LIM domain containing 2"
location: "11p15.3"
module: 78
arm: "+"
pooled_cpm: 142.71
n_lines_expressing: 39
n_dd_up: 2
n_dd_down: 38
n_dd_up_clean: 1
n_dd_down_clean: 34
in_vector_space: true
direction_upstream: 10
direction_downstream: 16
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# MICAL2

*microtubule associated monooxygenase, calponin and LIM domain containing 2* — 11p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 1.43× (z +4.2, q 0.013, up in 24 of 37 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.40× (z +4.0, q 0.022, up in 16 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Belinostat (drug)]] 5 µM in 1 line (SW480 3.22×); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 2.87×; ⚠ cell-cycle shift, explains ~36% of this change); [[5-Azacytidine (drug)]] 5 µM in 1 line (SW480 2.55×).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.380× (z -15.9, q 0e+00, down in 36 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPRIP]] (+0.67, fdr 7e-06), [[NIBAN2]] (+0.66, fdr 7e-06), [[ACTN1]] (+0.66, fdr 7e-06); moves opposite to [[HOXA3]] (-0.70, fdr 7e-06), [[RPRD2]] (-0.63, fdr 3e-05), [[PPP1R3E]] (-0.62, fdr 1e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[ANPEP]] → it (grade B ⚠); 16 go from it, the strongest it → [[ACOT7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5478.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Belinostat (drug)]] 5 µM in 1 line (SW480 3.22×); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 2.87×; ⚠ cell-cycle shift, explains ~36% of this change); [[5-Azacytidine (drug)]] 5 µM in 1 line (SW480 2.55×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.43×** | +4.2 | 0.013 | 24/37 (A498, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.022 | 16/37 (SW480, HCT15, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Filgotinib (drug)]] 5 µM |  | 1.32× | +3.3 | 0.19 | 23/37 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.30× | +3.1 | 0.27 | 16/37 (SW480, HCT15, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5478.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.380×** | -15.9 | 0e+00 | 36/38 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.465×** | -12.6 | 8e-34 | 30/37 (HEC-1-A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.397×** | -10.3 | 9e-23 | 31/37 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.503×** | -8.0 | 2e-13 | 27/37 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.490×** | -8.0 | 2e-13 | 32/36 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.543×** | -7.1 | 1e-10 | 26/37 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.328×** | -6.8 | 9e-10 | 34/37 (H4, LoVo, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.595×** | -6.0 | 1e-07 | 23/37 (H4, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.600×** | -5.7 | 7e-07 | 25/37 (HEC-1-A, H4, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.638×** | -5.2 | 1e-05 | 25/37 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.632×** | -5.1 | 2e-05 | 25/37 (A-172, LoVo, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.645×** | -4.9 | 5e-05 | 25/37 (HOP62, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.703×** | -4.7 | 1e-04 | 24/39 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.719×** | -4.7 | 1e-04 | 25/37 (AsPC-1, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.661×** | -4.6 | 2e-04 | 27/36 (A-172, AsPC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.664×** | -4.6 | 2e-04 | 25/38 (LoVo, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.682×** | -4.4 | 3e-04 | 24/37 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5478. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 388 | 0 | 14 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -19.9) |
| [[LoVo (line)]] | wt | 280 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -18.2) |
| [[H4 (line)]] | wt | 302 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -13.9) |
| [[AsPC-1 (line)]] | alt | 191 | 0 | 8 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -12.4) |
| [[hTERT-HPNE (line)]] | wt | 362 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -15.4) |
| [[LS 180 (line)]] | wt | 231 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -19.2) |
| [[HEC-1-A (line)]] | alt | 132 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -21.0) |
| [[PANC-1 (line)]] | alt | 137 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -20.1) |
| [[RPMI-7951 (line)]] | alt | 193 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -19.4) |
| [[HS-578T (line)]] | alt | 507 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -14.7) |
| [[SNU-1 (line)]] | wt | 280 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -21.0) |
| [[SW1417 (line)]] | alt | 191 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -20.6) |
| [[SW480 (line)]] | alt | 53.6 | 4 (2 ⚠) | 1 | [[Belinostat (drug)]] 5 µM 3.22× (z +11.9) | [[Harringtonine (drug)]] 5 µM 0.276× (z -12.6) |
| [[A-172 (line)]] | wt | 196 | 0 | 4 | — | [[Cobimetinib (drug)]] 5 µM 0.250× (z -12.3) |
| [[A549 (line)]] | wt | 254 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -20.8) |
| [[BT-474 (line)]] | alt | 134 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -9.6) |
| [[HT-29 (line)]] | alt | 168 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -15.9) |
| [[J82 (line)]] | alt | 402 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -11.7) |
| [[KATO III (line)]] | alt | 69.0 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 213 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -13.4) |
| [[MIA PaCa-2 (line)]] | alt | 47.1 | 0 | 3 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.639× (z -12.4) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -11.1) |
| [[SW 1088 (line)]] | alt | 340 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -11.9) |
| [[Hs 766T (line)]] | wt | 195 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.192× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 126 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 146 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -12.5) |
| [[SHP-77 (line)]] | alt | 56.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.292× (z -8.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.298× (z -8.5) |
| [[A498 (line)]] | wt | 78.8 | 1 (1 ⚠) | 0 | [[Daptomycin (drug)]] 5 µM 2.90× (z +8.8) ⚠ unreliable plate only | — |
| [[COLO 205 (line)]] | alt | 103 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -11.4) |
| [[HCT15 (line)]] | alt | 38.8 | 0 | 1 | — | [[venetoclax (drug)]] 5 µM 0.0472× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 101 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -9.1) |
| [[RKO (line)]] | wt | 64.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -10.0) |
| [[SNU-423 (line)]] | alt | 289 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -11.4) |
| [[SW 1271 (line)]] | alt | 201 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -10.0) |
| [[A-427 (line)]] | wt | 27.0 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 32.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 14.0 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.3 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.7 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 14.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.1 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5478), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPRIP]] | +0.67 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[NIBAN2]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[ACTN1]] | +0.66 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[PLXNA1]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[CORO1C]] | +0.65 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[ASAP2]] | +0.65 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[MYEOV]] | +0.64 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[SEPTIN10]] | +0.64 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[KIF21B]] | +0.64 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[ELK3]] | +0.64 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[BCAR3]] | +0.64 | +0.66 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA3]] | -0.70 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[RPRD2]] | -0.63 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[PPP1R3E]] | -0.62 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[BTN3A3]] | -0.60 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[FAM111A-DT]] | -0.59 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[LINC02100]] | -0.59 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[STAP2]] | -0.58 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[DNAJC27]] | -0.58 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[PUS10]] | -0.57 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[ACBD5]] | -0.56 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[HOXA5]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[HOXA6]] | -0.56 | -0.47 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANPEP]] | B | ANPEP activity raises MICAL2's level | lines that do not express ANPEP (33) vs lines expressing it (17) | 2.60× lower at baseline in the lines without ANPEP | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LINC01615, ENSG00000224865 |
| [[NLRP3]] | B | NLRP3 activity raises MICAL2's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 2.41× lower at baseline in the lines without NLRP3 | 0.028 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |
| [[SERPINE1]] | B | SERPINE1 activity raises MICAL2's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 2.45× lower at baseline in the lines without SERPINE1 | 0.063 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[F3]] | B | F3 activity raises MICAL2's level | lines that do not express F3 (24) vs lines expressing it (26) | 2.79× lower at baseline in the lines without F3 | 0.064 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[CLMP]] | B | CLMP activity raises MICAL2's level | lines that do not express CLMP (25) vs lines expressing it (25) | 1.84× lower at baseline in the lines without CLMP | 0.074 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10 |
| [[RASA3]] | B | RASA3 activity raises MICAL2's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 2.65× lower at baseline in the lines without RASA3 | 0.077 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[CD44]] | B | CD44 activity raises MICAL2's level | lines that do not express CD44 (15) vs lines expressing it (35) | 2.43× lower at baseline in the lines without CD44 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[KIAA1549L]] | B | KIAA1549L activity raises MICAL2's level | lines that do not express KIAA1549L (20) vs lines expressing it (30) | 2.07× lower at baseline in the lines without KIAA1549L | 0.093 | ⚠ within organs, on part of the lines; also absent: NLRP3, PLPP4, PHACTR1 |
| [[ITGA3]] | B | ITGA3 activity raises MICAL2's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 2.92× lower at baseline in the lines without ITGA3 | 0.096 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[PLXNA2]] | B | PLXNA2 activity raises MICAL2's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 2.74× lower at baseline in the lines without PLXNA2 | 0.097 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACOT7]] | B | MICAL2 activity lowers ACOT7's level | lines that do not express MICAL2 (11) vs lines expressing it (39) | 2.01× higher at baseline in the lines without MICAL2 | 0.008 | ⚠ within organs, on part of the lines; also absent: UBA7, ENSG00000285906, SERPINB1 |
| [[F3]] | B | MICAL2 activity raises F3's level | lines that do not express MICAL2 (11) vs lines expressing it (39) | 4.69× lower at baseline in the lines without MICAL2 | 0.009 | ⚠ within organs, on part of the lines; also absent: UBA7, ENSG00000285906, SERPINB1 |
| [[TBC1D2]] | B | MICAL2 activity raises TBC1D2's level | lines that do not express MICAL2 (11) vs lines expressing it (39) | 2.28× lower at baseline in the lines without MICAL2 | 0.017 | ⚠ within organs, on part of the lines; also absent: UBA7, ENSG00000285906, SERPINB1 |
| [[DUSP5]] | B | MICAL2 activity raises DUSP5's level | lines that do not express MICAL2 (11) vs lines expressing it (39) | 2.02× lower at baseline in the lines without MICAL2 | 0.022 | ⚠ within organs, on part of the lines; also absent: UBA7, ENSG00000285906, SERPINB1 |
| [[ITGA3]] | B | MICAL2 activity raises ITGA3's level | lines that do not express MICAL2 (11) vs lines expressing it (39) | 2.93× lower at baseline in the lines without MICAL2 | 0.023 | ⚠ within organs, on part of the lines; also absent: UBA7, ENSG00000285906, SERPINB1 |
| [[CAPN2]] | B | MICAL2 activity raises CAPN2's level | lines that do not express MICAL2 (11) vs lines expressing it (39) | 1.88× lower at baseline in the lines without MICAL2 | 0.028 | ⚠ within organs, on part of the lines; also absent: UBA7, ENSG00000285906, SERPINB1 |
| [[S100A16]] | B | MICAL2 activity raises S100A16's level | lines that do not express MICAL2 (11) vs lines expressing it (39) | 3.06× lower at baseline in the lines without MICAL2 | 0.036 | ⚠ within organs, on part of the lines; also absent: UBA7, ENSG00000285906, SERPINB1 |
| [[TGFA]] | B | MICAL2 activity raises TGFA's level | lines that do not express MICAL2 (11) vs lines expressing it (39) | 3.13× lower at baseline in the lines without MICAL2 | 0.044 | ⚠ within organs, on part of the lines; also absent: UBA7, ENSG00000285906, SERPINB1 |
| [[MINDY1]] | B | MICAL2 activity raises MINDY1's level | lines that do not express MICAL2 (11) vs lines expressing it (39) | 1.35× lower at baseline in the lines without MICAL2 | 0.063 | ⚠ within organs, on part of the lines; also absent: UBA7, ENSG00000285906, SERPINB1 |
| [[SLC25A51]] | B | MICAL2 activity raises SLC25A51's level | lines that do not express MICAL2 (11) vs lines expressing it (39) | 1.67× lower at baseline in the lines without MICAL2 | 0.066 | ⚠ within organs, on part of the lines; also absent: UBA7, ENSG00000285906, SERPINB1 |
| [[MYEOV]] | B | MICAL2 activity raises MYEOV's level | lines that do not express MICAL2 (11) vs lines expressing it (39) | 3.13× lower at baseline in the lines without MICAL2 | 0.076 | ⚠ within organs, on part of the lines; also absent: UBA7, ENSG00000285906, SERPINB1 |
| [[TOR4A]] | B | MICAL2 activity raises TOR4A's level | lines that do not express MICAL2 (11) vs lines expressing it (39) | 2.48× lower at baseline in the lines without MICAL2 | 0.084 | ⚠ within organs, on part of the lines; also absent: UBA7, ENSG00000285906, SERPINB1 |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.758). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.4, 6.0); signed map (6.6, 45.1). **Vector** length 140, 47.7% of its response variance represented; |z| ≥ 3 in 1,418 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *apical junction* (hallmark, mean cos +0.57 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +7.7 | +2.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +7.3 | +3.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.1 | +4.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.4 | +4.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +4.6 | +2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.5 | +2.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.0 | +0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | +2.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +3.5 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +1.3 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -8.4 | -4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.6 | -5.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -7.5 | -4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.8 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.4 | -4.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -6.3 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated monooxygenase, calponin and LIM domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.3 — chr11:12,094,008-12,359,144 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0750, FLJ14966; previously MICALCL |
| Gene groups (HGNC) | LIM domain containing; MicroRNA protein coding host genes; Bivalent Mical/EHBP Rab binding domain containing; Flavoproteins; MICAL oxygenase family |
| Matched by | ensembl_id |

**Function**, from UniProt [O94851](https://www.uniprot.org/uniprotkb/O94851) ([F-actin]-monooxygenase MICAL2):

> Methionine monooxygenase that promotes depolymerization of F-actin by mediating oxidation of residues 'Met-44' and 'Met-47' on actin to form methionine-sulfoxide, resulting in actin filament disassembly and preventing repolymerization. Regulates the disassembly of branched actin networks also by oxidizing ARP3B-containing ARP2/3 complexes leading to ARP3B dissociation from the network. Acts as a key regulator of the SRF signaling pathway elicited by nerve growth factor and serum: mediates …

**Summary**, from NCBI Gene [9645](https://www.ncbi.nlm.nih.gov/gene/9645):

> The protein encoded by this gene is a monooxygenase that enhances depolymerization of F-actin and is therefore involved in cytoskeletal dynamics. The encoded protein is a regulator of the SRF signaling pathway. Increased expression of this gene has been associated with cancer progression and metastasis. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:24693](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24693) · Entrez [9645](https://www.ncbi.nlm.nih.gov/gene/9645) · UniProt [O94851](https://www.uniprot.org/uniprotkb/O94851) · Ensembl [ENSG00000133816](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133816)

## Data

Gene col 5478: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5478); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5478, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5478]; `tensor/DDL_lfc|DDL_z.npy` [5478]; `embed/gene_vectors.npy` [5478]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5478 or target_col == 5478). Every well: [[MICAL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MICAL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
