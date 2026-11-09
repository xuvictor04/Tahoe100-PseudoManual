---
symbol: "MGA"
type: "gene"
col: 10471
ensembl_id: "ENSG00000174197"
name: "MAX dimerization protein MGA"
location: "15q15"
module: 1
arm: "+"
pooled_cpm: 92.5
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MGA

*MAX dimerization protein MGA* — 15q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.45× (z +9.8, q 5e-20, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.667× (z -6.4, q 7e-08, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UTP14A]] (+0.81, fdr 7e-06), [[COA7]] (+0.79, fdr 7e-06), [[ZNF121]] (+0.77, fdr 7e-06); moves opposite to [[TMEM50B]] (-0.70, fdr 7e-06), [[GNRH1]] (-0.66, fdr 7e-06), [[SRP54-AS1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10471.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +9.8 | 5e-20 | 30/46 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +8.4 | 1e-14 | 32/46 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +7.0 | 6e-10 | 31/46 (A-172, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +5.6 | 3e-06 | 30/46 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +4.5 | 9e-04 | 25/46 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.4 | 0.001 | 20/46 (Panc 03.27, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.26×** | +4.3 | 0.001 | 25/46 (HOP62, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +4.2 | 0.002 | 21/46 (A-172, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.9 | 0.006 | 23/45 (BT-474, SW48, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.22×** | +3.8 | 0.010 | 20/46 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.059 | 21/45 (MIA PaCa-2, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +3.1 | 0.089 | 17/46 (LOX-IMVI, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.0 | 0.11 | 18/46 (HOP62, AsPC-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10471.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.667×** | -6.4 | 7e-08 | 29/48 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.819×** | -5.3 | 3e-05 | 24/47 (NCI-H2030, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.748×** | -5.0 | 8e-05 | 29/43 (RKO, SW48, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.773×** | -4.8 | 2e-04 | 29/47 (A-427, C-33 A, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.758×** | -4.4 | 0.001 | 26/46 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.796×** | -4.3 | 0.002 | 22/46 (PANC-1, SW480, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.777×** | -3.4 | 0.060 | 20/45 (SHP-77, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | 0.823× | -3.1 | 0.13 | 18/45 (PANC-1, A498, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | 0.823× | -3.1 | 0.13 | 20/42 (C-33 A, LS 180, …) | all doses, flat | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10471. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 70.9 | 2 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +12.0) | [[Digitoxin (drug)]] 0.5 µM 0.423× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -10.8) |
| [[A-427 (line)]] | wt | 129 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -14.1) |
| [[A-172 (line)]] | wt | 57.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.94× (z +27.7) | — |
| [[A498 (line)]] | wt | 186 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 153 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 154 | 0 | 4 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -11.7) |
| [[PANC-1 (line)]] | alt | 131 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +13.2) | [[Digitoxin (drug)]] 5 µM 0.405× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H2347 (line)]] | alt | 88.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +23.2) | — |
| [[SW480 (line)]] | alt | 98.5 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.465× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A549 (line)]] | wt | 84.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.334× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[C-33 A (line)]] | alt | 161 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[H4 (line)]] | wt | 69.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HEC-1-A (line)]] | alt | 80.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -10.6) |
| [[RKO (line)]] | wt | 112 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -11.5) |
| [[SW48 (line)]] | wt | 69.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -14.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 60.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.89× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 102 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.135× (z -8.6) |
| [[HOP62 (line)]] | alt | 87.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.12× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 61.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +12.2) | — |
| [[LoVo (line)]] | wt | 81.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.493× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LOX-IMVI (line)]] | wt | 68.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 62.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[MIA PaCa-2 (line)]] | alt | 98.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.305× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 79.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +15.0) | — |
| [[NCI-H1792 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.336× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[Panc 03.27 (line)]] | alt | 55.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 95.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +11.6) | — |
| [[SHP-77 (line)]] | alt | 202 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.471× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SK-MEL-2 (line)]] | alt | 96.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +13.3) | — |
| [[SNU-423 (line)]] | alt | 101 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +14.5) | — |
| [[SW 1088 (line)]] | alt | 67.5 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.5 µM 0.0761× (z -8.7) |
| [[AN3 CA (line)]] | alt | 112 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 77.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 98.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.98 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 74.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10471), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP14A]] | +0.81 | +0.78 / +0.78 | both halves | 7e-06 |  |
| [[COA7]] | +0.79 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[ZNF121]] | +0.77 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[TMEM185B]] | +0.77 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[MAK16]] | +0.76 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[BYSL]] | +0.75 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[DDX10]] | +0.74 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[NOP14]] | +0.74 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[NOL11]] | +0.73 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[RPL7L1]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[POGK]] | +0.72 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[ABCE1]] | +0.71 | +0.69 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM50B]] | -0.70 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[GNRH1]] | -0.66 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | -0.64 | -0.70 / -0.51 | both halves | 1e-05 |  |
| [[APTR]] | -0.64 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[RAB6A]] | -0.64 | -0.72 / -0.55 | both halves | 1e-05 |  |
| [[TMEM59]] | -0.64 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[NARF]] | -0.61 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[KDELR1]] | -0.61 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[MPC2]] | -0.61 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[ELF2]] | -0.60 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[SEC11A]] | -0.60 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[APAF1]] | -0.60 | -0.61 / -0.60 | both halves | 7e-06 | pathway: Transcriptional Regulation by E2F6 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MGA's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.806). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.1, -36.9); signed map (1.0, -42.1). **Vector** length 113, 31.0% of its response variance represented; |z| ≥ 3 in 842 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.54 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.56 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.57 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.9 | +8.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.8 | +7.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.5 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.7 | +4.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.4 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +1.7 |
|  | [[EX229 (drug)]] 5 µM |  | +3.3 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -4.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -6.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -2.5 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | +0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | +0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | MAX dimerization protein MGA |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15 — chr15:41,621,134-41,773,081 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0518, MAD5, MXD5, FLJ12634 |
| Gene groups (HGNC) | MAX dimerization proteins; T-box transcription factors; MicroRNA protein coding host genes |
| Reactome | 1 pathways, smallest: Transcriptional Regulation by E2F6 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWI9](https://www.uniprot.org/uniprotkb/Q8IWI9) (MAX gene-associated protein):

> Functions as a dual-specificity transcription factor, regulating the expression of both MAX-network and T-box family target genes. Functions as a repressor or an activator. Binds to 5'-AATTTCACACCTAGGTGTGAAATT-3' core sequence and seems to regulate MYC-MAX target genes. Suppresses transcriptional activation by MYC and inhibits MYC-dependent cell transformation. Function activated by heterodimerization with MAX. This heterodimerization serves the dual function of both generating an E-box-binding …

**Summary**, from NCBI Gene [23269](https://www.ncbi.nlm.nih.gov/gene/23269):

> Predicted to enable DNA-binding transcription activator activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in cell fate specification and positive regulation of transcription by RNA polymerase II. Predicted to act upstream of or within cellular response to leukemia inhibitory factor. Part of MLL1 complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14010](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14010) · Entrez [23269](https://www.ncbi.nlm.nih.gov/gene/23269) · UniProt [Q8IWI9](https://www.uniprot.org/uniprotkb/Q8IWI9) · Ensembl [ENSG00000174197](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174197)

## Data

Gene col 10471: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10471); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10471, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10471]; `tensor/DDL_lfc|DDL_z.npy` [10471]; `embed/gene_vectors.npy` [10471]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10471 or target_col == 10471). Every well: [[MGA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MGA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
