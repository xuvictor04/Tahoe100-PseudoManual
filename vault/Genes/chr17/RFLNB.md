---
symbol: "RFLNB"
type: "gene"
col: 11437
ensembl_id: "ENSG00000183688"
name: "refilin B"
location: "17p13.3"
module: 28
arm: "-"
pooled_cpm: 9.99
n_lines_expressing: 34
n_dd_up: 30
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 13
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# RFLNB

*refilin B* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (20 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.23× (z +15.6, q 0e+00, up in 23 of 24 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.29× (z +11.1, q 3e-26, up in 23 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.583× (z -4.7, q 0.002, down in 16 of 29 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (LOX-IMVI 0.250×); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-427 0.182×; ⚠ cell-cycle shift, explains ~0% of this change); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (J82 0.142×); [[Mifepristone (drug)]] 0.05 µM in 1 line (AN3 CA 0.0608×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GATAD2A]] (+0.50, fdr 3e-05), [[SPCS3]] (+0.49, fdr 2e-04), [[TMEM181]] (+0.48, fdr 4e-05); moves opposite to [[BTN3A1]] (-0.48, fdr 4e-05), [[IFT74]] (-0.47, fdr 4e-05), [[ZSCAN26]] (-0.47, fdr 1e-04).
> It sits in the **-** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[RAPGEF5]] → it (grade B ⚠); 13 go from it, the strongest it → [[TTL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 20 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11437.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **5.23×** | +15.6 | 0e+00 | 23/24 (A498, HOP62, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.94×** | +11.9 | 2e-30 | 17/18 (A498, HOP62, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.63×** | +11.3 | 4e-27 | 17/20 (HOP62, SNU-423, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +11.1 | 3e-26 | 23/30 (A549, A498, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.53×** | +8.8 | 2e-16 | 22/31 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.44×** | +7.8 | 8e-13 | 21/25 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.92×** | +6.1 | 7e-08 | 20/29 (PANC-1, SHP-77, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.70×** | +5.0 | 3e-05 | 15/31 (A498, NCI-H23, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.78×** | +5.0 | 3e-05 | 16/29 (SNU-423, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.70×** | +5.0 | 3e-05 | 17/31 (A498, SW480, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.67×** | +4.8 | 7e-05 | 15/31 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.66×** | +4.8 | 8e-05 | 13/28 (SHP-77, HOP62, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.65×** | +4.7 | 9e-05 | 17/30 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.56×** | +4.2 | 9e-04 | 13/30 (HOP62, NCI-H460, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.56×** | +4.2 | 9e-04 | 14/30 (A-172, H4, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.002 | 14/31 (NCI-H2030, A-172, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.52×** | +3.9 | 0.002 | 11/31 (A-172, NCI-H460, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.77×** | +3.7 | 0.005 | 12/29 (NCI-H2030, HS-578T, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.011 | 11/31 (MIA PaCa-2, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.014 | 12/32 (NCI-H2030, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.056 | 11/31 (A-172, HOP62, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **1.80×** | +2.9 | 0.077 | 6/22 (NCI-H460, NCI-H2030, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11437.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (LOX-IMVI 0.250×); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-427 0.182×; ⚠ cell-cycle shift, explains ~0% of this change); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (J82 0.142×); [[Mifepristone (drug)]] 0.05 µM in 1 line (AN3 CA 0.0608×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.583×** | -4.7 | 0.002 | 16/29 (C32, C-33 A, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.724× | -3.0 | 0.45 | 9/30 (J82, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11437. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 14.7 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.35× (z +14.7) | — |
| [[SNU-423 (line)]] | alt | 8.05 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 22.1× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.86× (z +10.0) | — |
| [[A549 (line)]] | wt | 13.4 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.45× (z +14.9) | — |
| [[HOP62 (line)]] | alt | 16.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.2× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 25.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.17× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-172 (line)]] | wt | 18.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 10.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.4× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LOX-IMVI (line)]] | wt | 14.4 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.250× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 46.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RPMI-7951 (line)]] | alt | 12.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.54× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-427 (line)]] | wt | 18.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.182× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 31.3 | 0 | 1 | — | [[Mifepristone (drug)]] 0.05 µM 0.0608× (z -8.9) |
| [[J82 (line)]] | alt | 8.66 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.142× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 10.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW480 (line)]] | alt | 8.41 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.96× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[AsPC-1 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.936 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.867 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.578 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.689 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.552 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.751 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.962 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11437), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATAD2A]] | +0.50 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[SPCS3]] | +0.49 | +0.54 / +0.31 | both halves | 2e-04 |  |
| [[TMEM181]] | +0.48 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[VOPP1]] | +0.47 | +0.38 / +0.47 | both halves | 6e-05 |  |
| [[DIAPH1]] | +0.46 | +0.45 / +0.39 | both halves | 5e-05 |  |
| [[MYO1D]] | +0.46 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[TTL]] | +0.45 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[APPL2]] | +0.44 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[ADAM10]] | +0.44 | +0.41 / +0.35 | both halves | 1e-04 |  |
| [[RELL1]] | +0.44 | +0.42 / +0.38 | both halves | 7e-05 |  |
| [[CMTM4]] | +0.43 | +0.39 / +0.41 | both halves | 6e-05 |  |
| [[CBL]] | +0.43 | +0.47 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN3A1]] | -0.48 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[IFT74]] | -0.47 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[ZSCAN26]] | -0.47 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[NUDT12]] | -0.46 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[DHX58]] | -0.46 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[LINC02335]] | -0.45 | -0.19 / -0.42 | ⚠ not reproduced | 9e-04 |  |
| [[SUGT1P4-STRA6LP-CCDC180]] | -0.45 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[THAP8]] | -0.45 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[BNIP1]] | -0.45 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[ZSCAN12]] | -0.44 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[ADAMTS10]] | -0.44 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[STRA6LP]] | -0.44 | -0.50 / -0.43 | both halves | 4e-05 |  |
| [[MKS1]] | -0.44 | -0.32 / -0.42 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAPGEF5]] | B | RAPGEF5 activity lowers RFLNB's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 3.28× higher at baseline in the lines without RAPGEF5 | 0.017 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[GBX2-AS1]] | B | GBX2-AS1 activity raises RFLNB's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 4.10× lower at baseline in the lines without GBX2-AS1 | 0.026 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B |
| [[TOP2A]] | B | TOP2A activity lowers RFLNB's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZSCAN12]] | B | ZSCAN12 activity raises RFLNB's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 2.08× lower at baseline in the lines without ZSCAN12 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |
| [[ADAMTS10]] | C | ADAMTS10 activity raises RFLNB's level | lines that do not express ADAMTS10 (27) vs lines expressing it (23) | 3.62× lower at baseline in the lines without ADAMTS10 | 0.010 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTL]] | B | RFLNB activity raises TTL's level | lines that do not express RFLNB (16) vs lines expressing it (34) | 2.04× lower at baseline in the lines without RFLNB | 0.005 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1 |
| [[GBX2-AS1]] | B | RFLNB activity raises GBX2-AS1's level | lines that do not express RFLNB (16) vs lines expressing it (34) | 2.36× lower at baseline in the lines without RFLNB | 0.020 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1 |
| [[NBPF20]] | B | RFLNB activity raises NBPF20's level | lines that do not express RFLNB (16) vs lines expressing it (34) | 1.69× lower at baseline in the lines without RFLNB | 0.024 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1 |
| [[MXRA7]] | B | RFLNB activity raises MXRA7's level | lines that do not express RFLNB (16) vs lines expressing it (34) | 3.08× lower at baseline in the lines without RFLNB | 0.031 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1 |
| [[SNTB2]] | B | RFLNB activity raises SNTB2's level | lines that do not express RFLNB (16) vs lines expressing it (34) | 1.20× lower at baseline in the lines without RFLNB | 0.035 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1 |
| [[IFIH1]] | B | RFLNB activity lowers IFIH1's level | lines that do not express RFLNB (16) vs lines expressing it (34) | 1.24× higher at baseline in the lines without RFLNB | 0.044 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1 |
| [[TSPAN14]] | B | RFLNB activity lowers TSPAN14's level | lines that do not express RFLNB (16) vs lines expressing it (34) | 1.65× higher at baseline in the lines without RFLNB | 0.046 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1 |
| [[TMEM181]] | B | RFLNB activity raises TMEM181's level | lines that do not express RFLNB (16) vs lines expressing it (34) | 1.03× lower at baseline in the lines without RFLNB | 0.055 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1 |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM | B | RFLNB activity raises the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (protects the cells) | lines that do not express RFLNB (16) vs lines expressing it (32) | the lines without RFLNB: 0.83× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1 |
| [[DIAPH1]] | B | RFLNB activity lowers DIAPH1's level | lines that do not express RFLNB (16) vs lines expressing it (34) | 1.65× higher at baseline in the lines without RFLNB | 0.091 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | RFLNB activity raises the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (protects the cells) | lines that do not express RFLNB (16) vs lines expressing it (32) | the lines without RFLNB: 0.85× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1 |
| cells under [[Afatinib (drug)]] 0.5 µM | B | RFLNB activity raises the cells' numbers under Afatinib 0.5 µM (protects the cells) | lines that do not express RFLNB (16) vs lines expressing it (32) | the lines without RFLNB: 0.88× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1 |

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **-** arm (projection on the module's main direction -0.365). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (28.9, -41.8); signed map (-1.6, -60.8). **Vector** length 63.6, 14.7% of its response variance represented; |z| ≥ 3 in 675 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.3 | +8.8 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +2.8 | +4.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +2.5 | +4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +2.4 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +2.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.0 | +3.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +0.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.6 | +0.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.2 | -2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | refilin B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:439,978-445,939 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC45871, RefilinB, Cfm1; previously FAM101B |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5W9](https://www.uniprot.org/uniprotkb/Q8N5W9) (Refilin-B):

> Involved in the regulation of the perinuclear actin network and nuclear shape through interaction with filamins. Plays an essential role in the formation of cartilaginous skeletal elements.

**Summary**, from NCBI Gene [359845](https://www.ncbi.nlm.nih.gov/gene/359845):

> Enables filamin binding activity. Predicted to be involved in several processes, including actin filament bundle organization; negative regulation of bone mineralization involved in bone maturation; and negative regulation of chondrocyte development. Predicted to act upstream of or within actin cytoskeleton organization and epithelial to mesenchymal transition. Located in actin cytoskeleton. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28705](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28705) · Entrez [359845](https://www.ncbi.nlm.nih.gov/gene/359845) · UniProt [Q8N5W9](https://www.uniprot.org/uniprotkb/Q8N5W9) · Ensembl [ENSG00000183688](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183688)

## Data

Gene col 11437: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11437); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11437, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11437]; `tensor/DDL_lfc|DDL_z.npy` [11437]; `embed/gene_vectors.npy` [11437]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11437 or target_col == 11437). Every well: [[RFLNB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFLNB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
