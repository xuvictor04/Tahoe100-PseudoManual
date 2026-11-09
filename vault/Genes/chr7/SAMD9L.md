---
symbol: "SAMD9L"
type: "gene"
col: 10818
ensembl_id: "ENSG00000177409"
name: "sterile alpha motif domain containing 9 like"
location: "7q21.2"
module: 32
arm: "+"
pooled_cpm: 38.62
n_lines_expressing: 32
n_dd_up: 22
n_dd_down: 41
n_dd_up_clean: 22
n_dd_down_clean: 34
in_vector_space: true
direction_upstream: 56
direction_downstream: 102
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# SAMD9L

*sterile alpha motif domain containing 9 like* — 7q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.96× (z +8.2, q 2e-13, up in 26 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.126× (z -15.5, q 0e+00, down in 30 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XAF1]] (+0.94, fdr 7e-06), [[OAS2]] (+0.91, fdr 7e-06), [[SAMD9]] (+0.91, fdr 7e-06, ⚠ same locus), [[EPSTI1]] (+0.91, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 56 arrows point to it, the strongest [[RASGRP3]] → it (grade B ⚠); 102 go from it, the strongest it → [[DDX60]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, none with an alert; shown: the 15 strongest. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10818.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.96×** | +8.2 | 2e-13 | 26/29 (NCI-H2347, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **2.54×** | +6.7 | 5e-09 | 27/29 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **2.08×** | +5.5 | 6e-06 | 26/30 (NCI-H2347, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.74×** | +5.0 | 8e-05 | 22/30 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.85×** | +4.9 | 1e-04 | 23/30 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.89×** | +4.6 | 4e-04 | 21/30 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.74×** | +4.6 | 4e-04 | 21/30 (AsPC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +4.4 | 7e-04 | 17/29 (NCI-H2347, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.79×** | +4.4 | 8e-04 | 23/29 (AsPC-1, Hs 766T, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.60×** | +4.3 | 8e-04 | 25/30 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.71×** | +4.0 | 0.003 | 19/30 (HS-578T, NCI-H2347, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.69×** | +3.9 | 0.004 | 22/30 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.76×** | +3.9 | 0.004 | 20/30 (CFPAC-1, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **1.53×** | +3.8 | 0.005 | 23/30 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.008 | 19/30 (AsPC-1, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10818.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.126×** | -15.5 | 0e+00 | 30/30 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.149×** | -14.3 | 1e-43 | 28/30 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.166×** | -13.4 | 7e-39 | 29/30 (RPMI-7951, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.386×** | -10.1 | 1e-21 | 24/30 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.406×** | -9.5 | 2e-19 | 25/30 (LoVo, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.287×** | -9.3 | 1e-18 | 27/29 (RPMI-7951, SNU-423, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.311×** | -8.7 | 2e-16 | 27/30 (RKO, LoVo, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.332×** | -8.2 | 1e-14 | 24/30 (RKO, LoVo, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.380×** | -7.2 | 3e-11 | 27/30 (SNU-423, LoVo, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.380×** | -7.2 | 3e-11 | 24/30 (RKO, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.532×** | -6.6 | 2e-09 | 24/30 (COLO 205, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.548×** | -6.3 | 1e-08 | 23/30 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.415×** | -6.3 | 1e-08 | 24/28 (LoVo, SNU-423, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.368×** | -6.1 | 3e-08 | 25/30 (RKO, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.579×** | -5.7 | 3e-07 | 17/29 (NCI-H1573, A549, …) | top dose only | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.252×** | -5.4 | 2e-06 | 27/30 (RPMI-7951, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.612×** | -5.2 | 7e-06 | 22/30 (RPMI-7951, SK-MEL-2, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10818. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 187 | 0 | 16 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0331× (z -22.2) |
| [[LoVo (line)]] | wt | 47.1 | 0 | 14 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0817× (z -13.4) |
| [[SNU-423 (line)]] | alt | 77.0 | 0 | 13 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0478× (z -14.9) |
| [[RKO (line)]] | wt | 43.4 | 0 | 11 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0489× (z -15.5) |
| [[RPMI-7951 (line)]] | alt | 154 | 0 | 11 | — | [[Panobinostat (drug)]] 0.5 µM 0.0463× (z -20.3) |
| [[A549 (line)]] | wt | 32.3 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -12.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0918× (z -11.0) |
| [[COLO 205 (line)]] | alt | 146 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0558× (z -17.0) |
| [[NCI-H2347 (line)]] | alt | 36.2 | 2 | 6 | [[Harringtonine (drug)]] 0.5 µM 7.44× (z +10.5) | [[Tofacitinib (drug)]] 5 µM 0.244× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 60.6 | 0 | 7 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.201× (z -12.5) |
| [[HS-578T (line)]] | alt | 77.4 | 3 | 4 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.81× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.0655× (z -15.6) |
| [[SK-MEL-2 (line)]] | alt | 76.3 | 1 | 6 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.97× (z +8.9) | [[Belinostat (drug)]] 5 µM 0.116× (z -14.0) |
| [[A498 (line)]] | wt | 72.8 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 25.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -14.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0851× (z -13.4) |
| [[NCI-H1792 (line)]] | alt | 115 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0712× (z -16.1) |
| [[CFPAC-1 (line)]] | alt | 123 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.104× (z -14.3) |
| [[C32 (line)]] | wt | 52.7 | 1 | 2 | [[Harringtonine (drug)]] 0.5 µM 6.06× (z +8.8) | [[TAK-901 (drug)]] 0.05 µM 0.129× (z -9.2) |
| [[H4 (line)]] | wt | 81.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0677× (z -13.1) |
| [[Hs 766T (line)]] | wt | 121 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0831× (z -14.6) |
| [[J82 (line)]] | alt | 28.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.11× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 13.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.111× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 38.0 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.224× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 33.5 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 5.07× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0725× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 13.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0603× (z -10.0) |
| [[A-427 (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.12 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.95 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.07 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.99 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.42 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.42 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.96 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.69 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.15 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.89 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.83 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10818), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XAF1]] | +0.94 | +0.87 / +0.96 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 870 |
| [[OAS2]] | +0.91 | +0.84 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 835 |
| [[SAMD9]] | +0.91 | +0.86 / +0.93 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 794; ⚠ same locus (12.0 kb, same strand: neighbours can correlate without regulation) |
| [[EPSTI1]] | +0.91 | +0.81 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 890 |
| [[PARP14]] | +0.91 | +0.82 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 841 |
| [[IFIT3]] | +0.90 | +0.84 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 913 |
| [[DDX60L]] | +0.90 | +0.86 / +0.92 | both halves | 7e-06 | STRING 843 |
| [[IFI35]] | +0.90 | +0.83 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 820 |
| [[RSAD2]] | +0.90 | +0.83 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 781 |
| [[MX2]] | +0.89 | +0.82 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 636 |
| [[DDX60]] | +0.89 | +0.82 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 872 |
| [[SLC15A3]] | +0.89 | +0.81 / +0.92 | both halves | 7e-06 |  |
| [[IFI44]] | +0.89 | +0.82 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 914 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*56 arrows, 56 of them with an alert ⚠; grade A 0, B 36, C 20. Shown: the 12 strongest; 44 more arrows (44 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGRP3]] | B | RASGRP3 activity raises SAMD9L's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 3.86× lower at baseline in the lines without RASGRP3 | 0.001 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[OAS1]] | B | OAS1 activity raises SAMD9L's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 3.82× lower at baseline in the lines without OAS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[MX1]] | B | MX1 activity raises SAMD9L's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.86× lower at baseline in the lines without MX1 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[NRIR]] | B | NRIR activity raises SAMD9L's level | lines that do not express NRIR (14) vs lines expressing it (36) | 3.75× lower at baseline in the lines without NRIR | 0.003 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[IFITM1]] | B | IFITM1 activity raises SAMD9L's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 3.62× lower at baseline in the lines without IFITM1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[IFI6]] | B | IFI6 activity raises SAMD9L's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 3.99× lower at baseline in the lines without IFI6 | 0.004 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[APOL6]] | B | APOL6 activity raises SAMD9L's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 5.51× lower at baseline in the lines without APOL6 | 0.006 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[UBA7]] | B | UBA7 activity raises SAMD9L's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 5.38× lower at baseline in the lines without UBA7 | 0.007 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[RSAD2]] | B | RSAD2 activity raises SAMD9L's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 3.83× lower at baseline in the lines without RSAD2 | 0.007 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[NLRC5]] | B | NLRC5 activity raises SAMD9L's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 5.19× lower at baseline in the lines without NLRC5 | 0.007 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[MMP13]] | B | MMP13 activity raises SAMD9L's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 3.02× lower at baseline in the lines without MMP13 | 0.008 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[CASP10]] | B | CASP10 activity raises SAMD9L's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.57× lower at baseline in the lines without CASP10 | 0.009 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |

### Downstream of this gene

*102 arrows, 102 of them with an alert ⚠; grade A 0, B 85, C 17. Shown: the 12 strongest; 90 more arrows (90 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDX60]] | B | SAMD9L activity raises DDX60's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 3.27× lower at baseline in the lines without SAMD9L | 3e-04 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[DDX60L]] | B | SAMD9L activity raises DDX60L's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 3.40× lower at baseline in the lines without SAMD9L | 4e-04 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[NLRC5]] | B | SAMD9L activity raises NLRC5's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.23× lower at baseline in the lines without SAMD9L | 6e-04 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[HERC6]] | B | SAMD9L activity raises HERC6's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.43× lower at baseline in the lines without SAMD9L | 7e-04 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[SAMD9]] | B | SAMD9L activity raises SAMD9's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 4.29× lower at baseline in the lines without SAMD9L | 8e-04 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[CARD6]] | B | SAMD9L activity raises CARD6's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.65× lower at baseline in the lines without SAMD9L | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[PARP10]] | B | SAMD9L activity raises PARP10's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.92× lower at baseline in the lines without SAMD9L | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[IFI44L]] | B | SAMD9L activity raises IFI44L's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 5.17× lower at baseline in the lines without SAMD9L | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[PARP14]] | B | SAMD9L activity raises PARP14's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.11× lower at baseline in the lines without SAMD9L | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[OAS1]] | B | SAMD9L activity raises OAS1's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.94× lower at baseline in the lines without SAMD9L | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[IFI6]] | B | SAMD9L activity raises IFI6's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.89× lower at baseline in the lines without SAMD9L | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[MYD88]] | B | SAMD9L activity raises MYD88's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.78× lower at baseline in the lines without SAMD9L | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.928). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.4, 53.5); signed map (63.5, 31.5). **Vector** length 153, 57.2% of its response variance represented; |z| ≥ 3 in 1,251 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interferon Signaling* (reactome, mean cos +0.79 to 45); *Interferon alpha/beta signaling* (reactome, mean cos +0.80 to 27); *Interferon gamma signaling* (reactome, mean cos +0.77 to 17).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +11.3 | +8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.0 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.5 | +4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | +1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.2 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.6 | +4.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.4 | +4.9 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -8.0 | -10.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -7.2 | -9.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -7.0 | -8.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -6.7 | -8.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -6.6 | -7.2 |

## What is on record

|  |  |
|---|---|
| Name | sterile alpha motif domain containing 9 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.2 — chr7:93,130,056-93,148,385 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA2005, FLJ39885; previously C7orf6 |
| Gene groups (HGNC) | Sterile alpha motif domain containing |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVG5](https://www.uniprot.org/uniprotkb/Q8IVG5) (Sterile alpha motif domain-containing protein 9-like):

> May be involved in endosome fusion. Mediates down-regulation of growth factor signaling via internalization of growth factor receptors.

**Summary**, from NCBI Gene [219285](https://www.ncbi.nlm.nih.gov/gene/219285):

> This gene encodes a cytoplasmic protein that acts as a tumor suppressor but also plays a key role in cell proliferation and the innate immune response to viral infection. The encoded protein contains an N-terminal sterile alpha motif domain. Naturally occurring mutations in this gene are associated with myeloid disorders such as juvenile myelomonocytic leukemia, acute myeloid leukemia, and myelodysplastic syndrome. Naturally occurring mutations are also associated with hepatitis-B related …

**Accessions** — [HGNC:1349](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1349) · Entrez [219285](https://www.ncbi.nlm.nih.gov/gene/219285) · UniProt [Q8IVG5](https://www.uniprot.org/uniprotkb/Q8IVG5) · Ensembl [ENSG00000177409](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177409)

## Data

Gene col 10818: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10818); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10818, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10818]; `tensor/DDL_lfc|DDL_z.npy` [10818]; `embed/gene_vectors.npy` [10818]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10818 or target_col == 10818). Every well: [[SAMD9L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAMD9L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
