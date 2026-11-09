---
symbol: "KMT5C"
type: "gene"
col: 5433
ensembl_id: "ENSG00000133247"
name: "lysine methyltransferase 5C"
location: "19q13.42"
module: 40
arm: "+"
pooled_cpm: 10.91
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 25
n_dd_up_clean: 7
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# KMT5C

*lysine methyltransferase 5C* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.79× (z +7.3, q 1e-10, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.404× (z -11.4, q 2e-27, down in 39 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.498× (z -8.8, q 2e-16, down in 29 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEKHH3]] (+0.71, fdr 7e-06), [[YIPF2]] (+0.71, fdr 7e-06), [[SPSB3]] (+0.70, fdr 7e-06); moves opposite to [[UTP20]] (-0.75, fdr 7e-06), [[GPATCH4]] (-0.70, fdr 7e-06), [[COMMD10]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[COMMD10]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5433.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.79×** | +7.3 | 1e-10 | 28/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +5.5 | 1e-05 | 22/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +4.5 | 0.001 | 14/47 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +4.1 | 0.005 | 14/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.009 | 10/42 (C32, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.018 | 13/42 (SW480, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.019 | 16/43 (A549, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +3.2 | 0.095 | 3/22 (A-172, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5433.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.404×** | -11.4 | 2e-27 | 39/47 (PANC-1, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.404×** | -11.0 | 2e-25 | 17/20 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.434×** | -10.5 | 2e-23 | 30/35 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.498×** | -8.8 | 2e-16 | 29/44 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.509×** | -8.5 | 2e-15 | 28/46 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.537×** | -7.8 | 5e-13 | 30/46 (A-427, Panc 03.27, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.319×** | -7.5 | 4e-12 | 29/44 (SW1417, C32, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.542×** | -7.1 | 8e-11 | 18/27 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.582×** | -6.5 | 3e-09 | 25/46 (NCI-H23, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.370×** | -6.5 | 3e-09 | 26/41 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.424×** | -5.6 | 9e-07 | 24/45 (SW1417, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.630×** | -5.6 | 1e-06 | 22/45 (COLO 205, NCI-H1573, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.437×** | -5.4 | 2e-06 | 19/44 (A498, PANC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.680×** | -4.9 | 5e-05 | 21/47 (HT-29, KATO III, …) | two highest doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.523×** | -4.3 | 8e-04 | 17/40 (A498, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.720×** | -4.1 | 0.001 | 16/47 (A498, HS-578T, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.803×** | -3.9 | 0.003 | 21/47 (A498, HCT15, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.805×** | -3.9 | 0.004 | 16/48 (SW 900, SW1417, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.737×** | -3.8 | 0.004 | 16/48 (A498, LS 180, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5433. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 28.6 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0914× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.306× (z -12.5) |
| [[Hs 766T (line)]] | wt | 7.38 | 0 | 3 | — | [[Retinoic acid (drug)]] 0.05 µM 0.0873× (z -9.1) |
| [[PANC-1 (line)]] | alt | 13.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.225× (z -9.5) |
| [[A-172 (line)]] | wt | 16.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -12.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 6.70 | 0 | 2 (1 ⚠) | — | [[Procainamide (hydrochloride) (drug)]] 0.5 µM 0.0796× (z -10.7) |
| [[HT-29 (line)]] | alt | 26.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0552× (z -17.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 5.75 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0846× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 9.81 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.101× (z -10.1) |
| [[SW480 (line)]] | alt | 10.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0632× (z -17.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 9.01 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0339× (z -16.0) |
| [[C32 (line)]] | wt | 6.41 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0834× (z -8.9) |
| [[COLO 205 (line)]] | alt | 9.06 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0635× (z -8.7) |
| [[H4 (line)]] | wt | 18.9 | 0 | 1 | — | [[Clotrimazole (drug)]] 0.5 µM 0.0816× (z -10.9) |
| [[HCT15 (line)]] | alt | 20.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -9.2) |
| [[HOP62 (line)]] | alt | 5.98 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -9.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 12.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -8.7) |
| [[LS 180 (line)]] | wt | 17.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -9.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 8.68 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0666× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 8.51 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.100× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 8.20 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0833× (z -10.2) |
| [[SW1417 (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -9.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5433), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHH3]] | +0.71 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.71 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[SPSB3]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[NARF]] | +0.69 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[C2CD2L]] | +0.69 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.69 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[RAB40C]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[PPOX]] | +0.68 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[COX14]] | +0.67 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[ULK1]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CDK2AP2]] | +0.66 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[IFT20]] | +0.66 | +0.58 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP20]] | -0.75 | -0.71 / -0.71 | both halves | 7e-06 |  |
| [[GPATCH4]] | -0.70 | -0.74 / -0.59 | both halves | 7e-06 |  |
| [[COMMD10]] | -0.66 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[COA7]] | -0.66 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[DNAJC11]] | -0.66 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[FKTN]] | -0.65 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[ABCE1]] | -0.65 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[RRP15]] | -0.64 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[TRIM44]] | -0.63 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[PTPN11]] | -0.63 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[NOC3L]] | -0.62 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[GTF2H3]] | -0.62 | -0.54 / -0.67 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers KMT5C's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COMMD10]] | C | KMT5C's natural level weakens COMMD10's drug response | KMT5C's natural level across 50 lines (lineage-adjusted; a glimpse) | r -0.61, reverse -0.10; direction not clear | 0.086 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.705). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (4.9, -40.1); signed map (-22.1, 11.7). **Vector** length 96.1, 20.2% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +3.0 | +4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +5.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.7 | +7.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +0.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.6 | +2.3 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.6 | +1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.6 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.1 | -8.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.1 | -11.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -8.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.2 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -4.1 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -6.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.7 | -7.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.6 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | lysine methyltransferase 5C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:55,339,853-55,348,121 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2705; previously SUV420H2 |
| Gene groups (HGNC) | Histone lysine methyltransferases; SET domain containing |
| Reactome | 3 pathways, smallest: PKMTs methylate histone lysines; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86Y97](https://www.uniprot.org/uniprotkb/Q86Y97) (Histone-lysine N-methyltransferase KMT5C):

> Histone methyltransferase that specifically methylates monomethylated 'Lys-20' (H4K20me1) and dimethylated 'Lys-20' (H4K20me2) of histone H4 to produce respectively dimethylated 'Lys-20' (H4K20me2) and trimethylated 'Lys-20' (H4K20me3) and thus regulates transcription and maintenance of genome integrity. In vitro also methylates unmodified 'Lys-20' (H4K20me0) of histone H4 and nucleosomes. H4 'Lys-20' trimethylation represents a specific tag for epigenetic transcriptional repression. Mainly …

**Summary**, from NCBI Gene [84787](https://www.ncbi.nlm.nih.gov/gene/84787):

> SUV420H2 and the related enzyme SUV420H1 (MIM 610881) function as histone methyltransferases that specifically trimethylate nucleosomal histone H4 (see MIM 602822) on lysine-20 (K20) (Schotta et al., 2004 [PubMed 15145825]).[supplied by OMIM, Dec 2009]

**Accessions** — [HGNC:28405](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28405) · Entrez [84787](https://www.ncbi.nlm.nih.gov/gene/84787) · UniProt [Q86Y97](https://www.uniprot.org/uniprotkb/Q86Y97) · Ensembl [ENSG00000133247](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133247)

## Data

Gene col 5433: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5433); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5433, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5433]; `tensor/DDL_lfc|DDL_z.npy` [5433]; `embed/gene_vectors.npy` [5433]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5433 or target_col == 5433). Every well: [[KMT5C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KMT5C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
