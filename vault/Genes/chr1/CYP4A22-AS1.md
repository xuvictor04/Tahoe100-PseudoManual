---
symbol: "CYP4A22-AS1"
type: "gene"
col: 13463
ensembl_id: "ENSG00000225506"
name: "CYP4A22 antisense RNA 1"
location: "1p33"
module: 3
arm: "-"
pooled_cpm: 8.03
n_lines_expressing: 48
n_dd_up: 2
n_dd_down: 28
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CYP4A22-AS1

*CYP4A22 antisense RNA 1* — 1p33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 0.5 µM: 1.64× (z +3.8, q 0.068, up in 16 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (15 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.189× (z -13.4, q 6e-38, down in 39 of 44 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.281× (z -10.2, q 7e-22, down in 33 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02666]] (+0.56, fdr 3e-05), [[ADAMTS13]] (+0.56, fdr 1e-04), [[SRSF3]] (+0.55, fdr 3e-05); moves opposite to [[WDR44]] (-0.53, fdr 2e-05), [[ZCCHC24]] (-0.53, fdr 4e-05), [[FAM193B]] (-0.51, fdr 3e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC00886]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13463.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.64×** | +3.8 | 0.068 | 16/41 (CFPAC-1, A549, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +3.7 | 0.068 | 10/43 (MIA PaCa-2, A-427, …) | rises with dose | low cells (technical?); position effect removed |
| [[Finasteride (drug)]] 5 µM |  | 1.55× | +3.1 | 0.21 | 6/42 (A498, RKO, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.48× | +3.1 | 0.21 | 9/44 (CFPAC-1, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.46× | +3.1 | 0.21 | 11/40 (C-33 A, CFPAC-1, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.65× | +3.0 | 0.21 | 8/41 (NCI-H2030, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.53× | +3.0 | 0.21 | 14/40 (CFPAC-1, A549, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13463.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.189×** | -13.4 | 6e-38 | 39/44 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.281×** | -10.2 | 7e-22 | 33/42 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.297×** | -9.7 | 4e-20 | 38/42 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.450×** | -9.0 | 2e-17 | 29/39 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.329×** | -7.9 | 4e-13 | 24/31 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.406×** | -7.2 | 4e-11 | 29/41 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.410×** | -7.1 | 7e-11 | 23/37 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.369×** | -7.1 | 1e-10 | 28/41 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.537×** | -7.0 | 1e-10 | 23/41 (NCI-H1573, NCI-H23, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.479×** | -5.9 | 2e-07 | 25/41 (HCT15, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.477×** | -5.6 | 1e-06 | 28/45 (CFPAC-1, SNU-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.481×** | -5.2 | 1e-05 | 22/34 (NCI-H23, SNU-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.545×** | -4.9 | 5e-05 | 24/43 (RKO, HEC-1-A, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.574×** | -4.4 | 4e-04 | 21/43 (CFPAC-1, A-427, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.541×** | -4.4 | 5e-04 | 22/39 (MIA PaCa-2, SNU-1, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.590×** | -4.0 | 0.002 | 21/41 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.636×** | -3.4 | 0.016 | 14/43 (CFPAC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.750×** | -3.2 | 0.029 | 16/42 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.686×** | -3.0 | 0.056 | 13/39 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.696×** | -2.9 | 0.077 | 17/42 (MIA PaCa-2, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.73 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13463. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 37.8 | 0 | 10 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0528× (z -13.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -9.7) |
| [[PANC-1 (line)]] | alt | 6.35 | 0 | 10 (6 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0134× (z -20.5) |
| [[NCI-H1573 (line)]] | alt | 21.4 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0424× (z -22.1) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0725× (z -18.3) |
| [[MIA PaCa-2 (line)]] | alt | 21.9 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -15.0) |
| [[LoVo (line)]] | wt | 10.1 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0562× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -14.6) |
| [[NCI-H23 (line)]] | alt | 17.7 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0908× (z -17.2) |
| [[A-427 (line)]] | wt | 13.3 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0984× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.101× (z -11.9) |
| [[HT-29 (line)]] | alt | 11.8 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0376× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -8.6) |
| [[SNU-1 (line)]] | wt | 17.2 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0487× (z -11.0) |
| [[A549 (line)]] | wt | 6.28 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0513× (z -9.6) |
| [[COLO 205 (line)]] | alt | 13.8 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0222× (z -14.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0956× (z -12.9) |
| [[HCT15 (line)]] | alt | 8.64 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0503× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 5.00 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -12.0) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0751× (z -10.4) |
| [[SW1417 (line)]] | alt | 7.19 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0785× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[A498 (line)]] | wt | 15.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -9.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 2.95 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0343× (z -8.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[Panc 03.27 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0927× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 4.76 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0539× (z -9.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[RPMI-7951 (line)]] | alt | 4.82 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0724× (z -10.6) |
| [[A-172 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13463), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02666]] | +0.56 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[ADAMTS13]] | +0.56 | +0.64 / +0.35 | both halves | 1e-04 |  |
| [[SRSF3]] | +0.55 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[B3GALT9]] | +0.54 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[SLC24A1]] | +0.54 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[PPP2CA]] | +0.53 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[C22orf46]] | +0.53 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[EWSR1]] | +0.52 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[SAYSD1]] | +0.52 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[YWHAE]] | +0.52 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[DHX9]] | +0.52 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[TTC30A]] | +0.51 | +0.52 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR44]] | -0.53 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[ZCCHC24]] | -0.53 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[FAM193B]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[TULP3]] | -0.51 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[TBC1D20]] | -0.51 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[MAP3K3]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[PRKRA]] | -0.50 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[MFSD8]] | -0.50 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[MRPS6]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[SRGAP2D]] | -0.48 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[NARF]] | -0.47 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[SFXN3]] | -0.47 | -0.48 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00886]] | B | LINC00886 activity raises CYP4A22-AS1's level | lines that do not express LINC00886 (16) vs lines expressing it (34) | 1.45× lower at baseline in the lines without LINC00886 | 0.055 | ⚠ within organs, on part of the lines; also absent: RASEF; maybe low, not absent |
| [[ZNF521]] | B | ZNF521 activity lowers CYP4A22-AS1's level | lines that do not express ZNF521 (27) vs lines expressing it (23) | 1.71× higher at baseline in the lines without ZNF521 | 0.084 | ⚠ within organs, on part of the lines; also absent: LEF1, SNAI2, ITGA4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.471). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-29.2, 24.6); signed map (19.3, -42.1). **Vector** length 68.1, 13.0% of its response variance represented; |z| ≥ 3 in 1,023 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | -0.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.9 | +3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +2.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.4 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.3 | +2.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.2 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -7.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.7 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -10.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.3 | -4.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.5 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | CYP4A22 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p33 — chr1:47,096,653-47,179,271 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ncRNA-a3 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43715](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43715) · Entrez [105378701](https://www.ncbi.nlm.nih.gov/gene/105378701) · Ensembl [ENSG00000225506](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225506)

## Data

Gene col 13463: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13463); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13463, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13463]; `tensor/DDL_lfc|DDL_z.npy` [13463]; `embed/gene_vectors.npy` [13463]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13463 or target_col == 13463). Every well: [[CYP4A22-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP4A22-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
