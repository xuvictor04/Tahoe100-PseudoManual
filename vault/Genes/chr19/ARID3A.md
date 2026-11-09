---
symbol: "ARID3A"
type: "gene"
col: 3752
ensembl_id: "ENSG00000116017"
name: "AT-rich interaction domain 3A"
location: "19p13.3"
module: 3
arm: "+"
pooled_cpm: 72.02
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 24
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# ARID3A

*AT-rich interaction domain 3A* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.30× (z +4.5, q 0.002, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.377× (z -11.5, q 7e-28, down in 36 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.575× (z -9.6, q 1e-19, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AFMID]] (+0.74, fdr 7e-06), [[MARCHF9]] (+0.74, fdr 1e-05), [[CDKN2D]] (+0.72, fdr 7e-06); moves opposite to [[EIF4G2]] (-0.71, fdr 7e-06), [[EWSR1]] (-0.70, fdr 7e-06), [[CAPRIN1]] (-0.70, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3752.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.5 | 0.002 | 29/48 (KATO III, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.66×** | +4.5 | 0.002 | 41/48 (A-427, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +4.3 | 0.003 | 29/49 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM |  | **1.32×** | +3.5 | 0.079 | 36/49 (PANC-1, HOP62, …) | all doses, flat | position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.080 | 26/48 (A-427, NCI-H2030, …) | all doses, flat | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.68×** | +3.3 | 0.080 | 28/48 (SW480, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.080 | 24/48 (KATO III, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.42× | +3.1 | 0.16 | 19/49 (MIA PaCa-2, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3752.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.377×** | -11.5 | 7e-28 | 36/44 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.439×** | -10.1 | 1e-21 | 42/49 (HCT15, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.575×** | -9.6 | 1e-19 | 38/49 (MIA PaCa-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.436×** | -9.4 | 6e-19 | 39/45 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.561×** | -6.8 | 1e-09 | 38/48 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.690×** | -6.4 | 1e-08 | 35/48 (NCI-H1792, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.620×** | -5.9 | 4e-07 | 34/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.714×** | -5.8 | 4e-07 | 30/48 (C32, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.616×** | -5.7 | 7e-07 | 33/48 (HS-578T, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.622×** | -5.6 | 1e-06 | 30/47 (C32, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.642×** | -5.4 | 3e-06 | 27/48 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.658×** | -4.9 | 4e-05 | 36/48 (NCI-H1792, RKO, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.760×** | -4.7 | 9e-05 | 33/48 (A-172, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.705×** | -4.3 | 7e-04 | 25/48 (HepG2/C3A, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.697×** | -4.3 | 8e-04 | 27/50 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.723×** | -3.8 | 0.006 | 26/47 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.761×** | -3.3 | 0.024 | 24/48 (HepG2/C3A, HOP62, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.781×** | -3.0 | 0.059 | 19/48 (SW48, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3752. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 129 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0718× (z -23.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -18.4) |
| [[A-172 (line)]] | wt | 118 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0817× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.237× (z -16.1) |
| [[C32 (line)]] | wt | 87.8 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -19.8) |
| [[HEC-1-A (line)]] | alt | 69.4 | 0 | 7 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0741× (z -13.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.389× (z -13.3) |
| [[HS-578T (line)]] | alt | 70.4 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -17.2) |
| [[NCI-H2030 (line)]] | alt | 85.7 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -16.9) |
| [[HepG2_C3A (line)]] | wt | 255 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -14.1) |
| [[C-33 A (line)]] | alt | 116 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 55.8 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -14.1) |
| [[NCI-H23 (line)]] | alt | 97.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 55.5 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.347× (z -12.3) |
| [[PANC-1 (line)]] | alt | 57.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.492× (z -10.0) |
| [[SW 900 (line)]] | alt | 60.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.265× (z -10.0) |
| [[A549 (line)]] | wt | 54.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -11.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 74.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -11.1) |
| [[KATO III (line)]] | alt | 18.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.7× (z +22.7) | — |
| [[LoVo (line)]] | wt | 84.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.365× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 70.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -8.5) |
| [[A-427 (line)]] | wt | 83.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.393× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 93.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.297× (z -9.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 55.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.206× (z -9.2) ⚠ toxic |
| [[HCT15 (line)]] | alt | 125 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0360× (z -21.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 77.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 72.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -11.7) |
| [[SW480 (line)]] | alt | 105 | 1 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.31× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -11.7) |
| [[A498 (line)]] | wt | 56.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -10.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 43.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -10.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 32.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -9.8) |
| [[HT-29 (line)]] | alt | 53.1 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.426× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 50.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 52.9 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.342× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 56.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -10.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 77.9 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0444× (z -10.6) |
| [[SW 1271 (line)]] | alt | 71.8 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0941× (z -9.0) |
| [[SW48 (line)]] | wt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -10.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 132 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 74.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3752), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AFMID]] | +0.74 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[MARCHF9]] | +0.74 | +0.49 / +0.79 | both halves | 1e-05 |  |
| [[CDKN2D]] | +0.72 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[SH3GL1]] | +0.71 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[ATG4B]] | +0.71 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[CCDC107]] | +0.71 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.71 | +0.55 / +0.75 | both halves | 1e-05 |  |
| [[CDC34]] | +0.70 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[LAMTOR5]] | +0.70 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[INAFM1]] | +0.70 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[EML2]] | +0.70 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[LIN7B]] | +0.69 | +0.54 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.71 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[EWSR1]] | -0.70 | -0.58 / -0.74 | both halves | 7e-06 |  |
| [[CAPRIN1]] | -0.70 | -0.53 / -0.74 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.70 | -0.48 / -0.73 | both halves | 2e-05 |  |
| [[PSME3]] | -0.70 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[RCN1]] | -0.69 | -0.46 / -0.68 | both halves | 3e-05 |  |
| [[XRCC6]] | -0.68 | -0.58 / -0.68 | both halves | 7e-06 |  |
| [[SF3B4]] | -0.68 | -0.48 / -0.70 | both halves | 2e-05 |  |
| [[XRCC5]] | -0.67 | -0.57 / -0.69 | both halves | 1e-05 |  |
| [[ILF3]] | -0.67 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[TMX3]] | -0.66 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[LIN7C]] | -0.66 | -0.52 / -0.72 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ARID3A's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.795). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-32.4, -26.2); signed map (-28.0, 14.1). **Vector** length 142, 48.1% of its response variance represented; |z| ≥ 3 in 1,075 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.9 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.7 | +4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.8 | -0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +5.6 | +4.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +5.4 | -3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.2 | +3.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.8 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +0.2 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.2 | -9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.2 | -10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.2 | -11.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.3 | -4.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.2 | -5.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -4.2 | -3.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -4.0 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | AT-rich interaction domain 3A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:925,781-975,939 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BRIGHT; previously DRIL1 |
| Gene groups (HGNC) | AT-rich interaction domain containing |
| Reactome | 3 pathways, smallest: TP53 Regulates Transcription of Genes Involved in G1 Cell Cycle Arrest; TP53 Regulates Transcription of Cell Cycle Genes; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99856](https://www.uniprot.org/uniprotkb/Q99856) (AT-rich interactive domain-containing protein 3A):

> Transcription factor which may be involved in the control of cell cycle progression by the RB1/E2F1 pathway and in B-cell differentiation.

**Summary**, from NCBI Gene [1820](https://www.ncbi.nlm.nih.gov/gene/1820):

> This gene encodes a member of the ARID (AT-rich interaction domain) family of DNA binding proteins. It was found by homology to the Drosophila dead ringer gene, which is important for normal embryogenesis. Other ARID family members have roles in embryonic patterning, cell lineage gene regulation, cell cycle control, transcriptional regulation, and possibly in chromatin structure modification. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3031](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3031) · Entrez [1820](https://www.ncbi.nlm.nih.gov/gene/1820) · UniProt [Q99856](https://www.uniprot.org/uniprotkb/Q99856) · Ensembl [ENSG00000116017](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116017)

## Data

Gene col 3752: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3752); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3752, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3752]; `tensor/DDL_lfc|DDL_z.npy` [3752]; `embed/gene_vectors.npy` [3752]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3752 or target_col == 3752). Every well: [[ARID3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARID3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
