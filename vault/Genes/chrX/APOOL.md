---
symbol: "APOOL"
type: "gene"
col: 7860
ensembl_id: "ENSG00000155008"
name: "apolipoprotein O like"
location: "Xq21.1"
module: 17
arm: "+"
pooled_cpm: 55.9
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# APOOL

*apolipoprotein O like* — Xq21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.73× (z +14.7, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.756× (z -10.7, q 7e-24, down in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (A549 0.445×, Hs 766T 0.494×, A-172 0.463×, NCI-H460 0.656×, …); [[Digitoxin (drug)]] 5 µM in 4 lines (NCI-H460 0.400×, LS 180 0.339×, PANC-1 0.501×, SW480 0.532×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.172×, NCI-H661 0.0692×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ipatasertib (drug)]] 0.5 µM in 1 line (SHP-77 0.195×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CWC27]] (+0.70, fdr 7e-06), [[EFCAB7]] (+0.69, fdr 1e-05), [[VPS50]] (+0.66, fdr 7e-06); moves opposite to [[ERF]] (-0.55, fdr 3e-05), [[DOT1L]] (-0.51, fdr 3e-05), [[MAMLD1]] (-0.50, fdr 5e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7860.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.73×** | +14.7 | 0e+00 | 44/48 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.55×** | +12.5 | 3e-33 | 35/48 (HOP62, HEC-1-A, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +11.0 | 8e-26 | 34/48 (HEC-1-A, HOP62, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.31×** | +10.2 | 4e-22 | 31/48 (HT-29, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.31×** | +7.8 | 8e-13 | 28/48 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +6.5 | 9e-09 | 20/42 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.25×** | +6.3 | 2e-08 | 29/48 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.39×** | +4.9 | 6e-05 | 20/47 (Hs 766T, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.13× | +3.5 | 0.029 | 5/49 (RKO, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.13× | +3.4 | 0.042 | 10/47 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.03× | +3.3 | 0.042 | 0/49 | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.12× | +3.2 | 0.059 | 3/48 (Hs 766T, A549, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.12× | +3.1 | 0.074 | 9/47 (SW480, HOP62, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.078 | 10/47 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.08× | +3.1 | 0.079 | 1/48 (AsPC-1) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7860.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (A549 0.445×, Hs 766T 0.494×, A-172 0.463×, NCI-H460 0.656×, …); [[Digitoxin (drug)]] 5 µM in 4 lines (NCI-H460 0.400×, LS 180 0.339×, PANC-1 0.501×, SW480 0.532×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.172×, NCI-H661 0.0692×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ipatasertib (drug)]] 0.5 µM in 1 line (SHP-77 0.195×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -10.7 | 7e-24 | 33/48 (A549, Hs 766T, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.759×** | -7.9 | 1e-12 | 28/47 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.820×** | -5.5 | 9e-06 | 22/47 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.831×** | -5.1 | 5e-05 | 21/47 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.865× | -4.1 | 0.004 | 18/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.899× | -4.0 | 0.007 | 6/48 (SNU-423, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.873× | -3.9 | 0.009 | 14/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | 0.881× | -3.5 | 0.036 | 19/48 (A549, J82, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | 0.888× | -3.4 | 0.044 | 16/48 (SW480, NCI-H460, …) | rises with dose | composition shift |
| [[Mebendazole (drug)]] 5 µM |  | 0.888× | -3.2 | 0.067 | 10/48 (CFPAC-1, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7860. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 91.1 | 1 | 5 (4 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.67× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.400× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.656× (z -9.6) |
| [[SW480 (line)]] | alt | 84.7 | 0 | 6 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.493× (z -11.3) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 53.9 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.07× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.593× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 33.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -10.5) |
| [[A549 (line)]] | wt | 49.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -13.0) |
| [[HOP62 (line)]] | alt | 41.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.98× (z +11.7) | — |
| [[LoVo (line)]] | wt | 34.3 | 1 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.31× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 57.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 62.1 | 1 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 1.71× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.501× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SHP-77 (line)]] | alt | 48.3 | 0 | 2 (1 ⚠) | — | [[Ipatasertib (drug)]] 0.5 µM 0.195× (z -11.1) |
| [[SNU-423 (line)]] | alt | 99.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -11.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -9.4) |
| [[A-427 (line)]] | wt | 51.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 48.6 | 0 | 1 (1 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 5 µM 0.112× (z -8.5) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 70.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -10.6) |
| [[HT-29 (line)]] | alt | 49.2 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.76× (z +8.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 61.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.339× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 79.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.86× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 62.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0692× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 95.7 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.07× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 62.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -9.0) |
| [[A498 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7860), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CWC27]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[EFCAB7]] | +0.69 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[VPS50]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[GTF3C3]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[CCNC]] | +0.64 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[TTC1]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[CUL5]] | +0.63 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[INTU]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[SUDS3]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[FAM204A]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[DMAC2]] | +0.62 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[WDR11]] | +0.61 | +0.50 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERF]] | -0.55 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[DOT1L]] | -0.51 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[MAMLD1]] | -0.50 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[HIVEP1]] | -0.50 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[CFAP45]] | -0.50 | -0.40 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers APOOL's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.397). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-22.9, -0.4); signed map (-21.7, -21.3). **Vector** length 100, 22.2% of its response variance represented; |z| ≥ 3 in 982 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.4 | +14.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.9 | +11.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.5 | +12.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +7.8 | +10.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +6.2 | +6.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.0 | +1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.2 | +3.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -10.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | -5.4 | -5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -4.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -3.1 | -7.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.0 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -4.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | -1.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | apolipoprotein O like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq21.1 — chrX:85,003,877-85,093,315 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UNQ8193, AAIR8193, Mic27, MICOS27; previously CXorf33, FAM121A |
| Gene groups (HGNC) | Mitochondrial contact site and cristae organizing system subunits |
| Reactome | 7 pathways, smallest: Cristae formation; Mitochondrial biogenesis; Platelet degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UXV4](https://www.uniprot.org/uniprotkb/Q6UXV4) (MICOS complex subunit MIC27):

> Component of the MICOS complex, a large protein complex of the mitochondrial inner membrane that plays crucial roles in the maintenance of crista junctions, inner membrane architecture, and formation of contact sites to the outer membrane. Specifically binds to cardiolipin (in vitro) but not to the precursor lipid phosphatidylglycerol. Plays a crucial role in crista junction formation and mitochondrial function,.

**Summary**, from NCBI Gene [139322](https://www.ncbi.nlm.nih.gov/gene/139322):

> This gene encodes a protein which contains an apolipoprotein O superfamily domain. This domain is found on proteins in circulating lipoprotein complexes. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:24009](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24009) · Entrez [139322](https://www.ncbi.nlm.nih.gov/gene/139322) · UniProt [Q6UXV4](https://www.uniprot.org/uniprotkb/Q6UXV4) · Ensembl [ENSG00000155008](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155008)

## Data

Gene col 7860: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7860); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7860, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7860]; `tensor/DDL_lfc|DDL_z.npy` [7860]; `embed/gene_vectors.npy` [7860]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7860 or target_col == 7860). Every well: [[APOOL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APOOL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
